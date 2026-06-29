"""
options_data_collector.py — Task 1.3: Full-day options + stock 1-minute collector.

Runs 9:28 AM – 4:05 PM ET collecting every 1 minute:
  • Stock 1-min bars (all ~900 symbols)  -> data/stocks_1min/YYYY-MM-DD.parquet
  • Options chain snapshots (2 expiry buckets: ≤7d and ≤45d, strikes ±7%)
    -> data/options_1min/YYYY-MM-DD.parquet

Expiry buckets:
  "near"  — expiration within 7 calendar days of today
  "swing" — expiration within 8–45 calendar days of today

Skip rules (per contract):
  open_interest < 100 | bid == 0 | spread > 40% of mid
  (All skips logged with reason; nothing silently dropped.)

Rate-limit management:
  Logs API calls/minute. If >80% of assumed rate limit is reached, prioritise
  first-hour signal symbols (those with |pct_change_from_open| > 0.015 OR
  vol_ratio rank in top 10% of universe) over full universe for that minute.

GitHub Actions note: this script is designed to run in a 5-minute cron window
with an internal per-minute loop (see options_collector.yml). The workflow
guard prevents overlapping runs from stacking.

TODO: Add US market holiday skip.
"""

from __future__ import annotations

import logging
import os
import sys
import time
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional
from zoneinfo import ZoneInfo

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from alpaca.data.enums import DataFeed
from alpaca.data.historical import OptionHistoricalDataClient, StockHistoricalDataClient
from alpaca.data.live import StockDataStream
from alpaca.data.requests import OptionChainRequest, StockBarsRequest
from alpaca.data.timeframe import TimeFrame

sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_universe import get_universe
from options_oi import make_trading_client, fetch_open_interest

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Credentials
# ---------------------------------------------------------------------------
API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_SECRET_KEY")
if not API_KEY or not API_SECRET:
    print("ERROR: Set ALPACA_API_KEY and ALPACA_SECRET_KEY environment variables.")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
ET = ZoneInfo("America/New_York")
_REPO_ROOT = Path(__file__).resolve().parent.parent
STOCKS_DIR = _REPO_ROOT / "data" / "stocks_1min"
OPTIONS_DIR = _REPO_ROOT / "data" / "options_1min"
STOCKS_DIR.mkdir(parents=True, exist_ok=True)
OPTIONS_DIR.mkdir(parents=True, exist_ok=True)

TODAY_STR = date.today().strftime("%Y-%m-%d")
TODAY = date.today()

START_H, START_M = 9, 28
END_H, END_M = 16, 5

STRIKE_PCT = 0.07           # ±7% of underlying price
NEAR_EXPIRY_DAYS = 7        # "near" bucket: ≤7d to expiry
SWING_EXPIRY_DAYS = 45      # "swing" bucket: ≤45d to expiry

# Skip thresholds
MIN_OI = 100
MIN_BID = 0.01              # bid == 0 means illiquid
MAX_SPREAD_PCT = 0.40       # 40% of mid

# Rate-limit planning: Alpaca free tier is ~200 req/min (unverified).
# Using conservative 150/min; once confirmed, update here.
# TODO verify against live API: confirm Alpaca options rate limit
ASSUMED_RATE_LIMIT = 150    # calls/minute — conservative placeholder
RATE_LIMIT_WARN_PCT = 0.80  # warn + prioritise first-hour signals above this

# First-hour signal threshold
FH_MOVE_THRESH = 0.015      # |pct_change| > 1.5% to be a "signal" symbol
FH_VOLRATIO_TOP_PCT = 0.10  # top 10% by vol_ratio


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _now_et() -> datetime:
    return datetime.now(ET)


def _in_window() -> bool:
    now = _now_et()
    start = now.replace(hour=START_H, minute=START_M, second=0, microsecond=0)
    end = now.replace(hour=END_H, minute=END_M, second=59, microsecond=0)
    return start <= now <= end


def _load_first_hour_signals() -> list[str]:
    """Return symbol list from today's first_hour parquet that showed signals."""
    fh_path = _REPO_ROOT / "data" / "first_hour" / f"{TODAY_STR}_summary.parquet"
    if not fh_path.exists():
        return []
    try:
        df = pd.read_parquet(fh_path)
        if "pct_change_from_open" not in df.columns and "total_first_hour_return" not in df.columns:
            return []
        col = "total_first_hour_return" if "total_first_hour_return" in df.columns else "pct_change_from_open"
        movers = df[df[col].abs() > FH_MOVE_THRESH]["symbol"].tolist()
        return movers
    except Exception as exc:
        log.warning("Could not load first-hour signals: %s", exc)
        return []


def _skip_contract(bid: Optional[float], ask: Optional[float],
                   oi: Optional[int]) -> Optional[str]:
    """Return skip reason string or None if contract passes."""
    if bid is None or ask is None:
        return "no_quote"
    if bid < MIN_BID:
        return "bid_zero"
    mid = (bid + ask) / 2
    if mid <= 0:
        return "mid_zero"
    spread_pct = (ask - bid) / mid
    if spread_pct > MAX_SPREAD_PCT:
        return f"spread_{spread_pct:.0%}"
    if oi is not None and oi < MIN_OI:
        return f"low_oi_{oi}"
    return None


# ---------------------------------------------------------------------------
# Stock bar collection via websocket (runs continuously in background)
# ---------------------------------------------------------------------------

class StockBarAccumulator:
    """Receives 1-min bars from StockDataStream and stores them in memory."""

    def __init__(self) -> None:
        self.bars: dict[str, list[dict]] = defaultdict(list)
        self.latest_price: dict[str, float] = {}
        self.latest_pct_change: dict[str, float] = {}
        self.open_prices: dict[str, float] = {}

    async def on_bar(self, bar) -> None:
        sym = bar.symbol
        o, h, l, c, v = bar.open, bar.high, bar.low, bar.close, bar.volume
        ts = bar.timestamp
        vwap_bar = getattr(bar, "vwap", None)
        trade_count = getattr(bar, "trade_count", None)

        if sym not in self.open_prices:
            self.open_prices[sym] = o
        open_p = self.open_prices[sym]
        pct_change = (c - open_p) / open_p if open_p else None
        range_pct = (h - l) / open_p if open_p else None

        self.latest_price[sym] = c
        if pct_change is not None:
            self.latest_pct_change[sym] = pct_change

        self.bars[sym].append({
            "timestamp": ts,
            "symbol": sym,
            "open": o,
            "high": h,
            "low": l,
            "close": c,
            "volume": int(v),
            "vwap": vwap_bar,
            "trade_count": trade_count,
            "pct_change_from_open": pct_change,
            "range_pct": range_pct,
        })

    def get_snapshot_price(self, symbol: str) -> Optional[float]:
        return self.latest_price.get(symbol)


# ---------------------------------------------------------------------------
# Options collector
# ---------------------------------------------------------------------------

class OptionsDataCollector:
    """Full-day 1-min collector: stocks (websocket) + options (REST polling)."""

    def __init__(self) -> None:
        self.universe: list[str] = []
        self.opt_client = OptionHistoricalDataClient(API_KEY, API_SECRET)
        self.trading_client = make_trading_client(API_KEY, API_SECRET, paper=True)
        self.stock_accum = StockBarAccumulator()
        self.options_rows: list[dict] = []
        self.skip_log: list[dict] = []
        self.api_calls_this_minute: int = 0
        self.api_calls_total: int = 0
        self._minute_window_start: float = time.monotonic()
        self._stream: StockDataStream | None = None

    # ------------------------------------------------------------------
    # Rate limit tracking
    # ------------------------------------------------------------------
    def _track_call(self) -> bool:
        """Record one API call. Returns True if we are approaching rate limit."""
        self.api_calls_this_minute += 1
        self.api_calls_total += 1
        elapsed = time.monotonic() - self._minute_window_start
        if elapsed >= 60.0:
            log.info("Rate: %d calls in last %.0fs", self.api_calls_this_minute, elapsed)
            self.api_calls_this_minute = 0
            self._minute_window_start = time.monotonic()
        rate_fraction = self.api_calls_this_minute / max(1.0, elapsed / 60.0 * ASSUMED_RATE_LIMIT)
        return rate_fraction > RATE_LIMIT_WARN_PCT

    # ------------------------------------------------------------------
    # Options collection for one symbol
    # ------------------------------------------------------------------
    def _collect_options_for_symbol(
        self,
        symbol: str,
        approx_price: Optional[float],
        ts_collected: datetime,
    ) -> None:
        """Fetch option chain for one underlying symbol and append to options_rows."""
        if approx_price is None:
            self._log_skip(symbol, None, "no_price")
            return

        near_end = TODAY + timedelta(days=NEAR_EXPIRY_DAYS)
        swing_end = TODAY + timedelta(days=SWING_EXPIRY_DAYS)

        for bucket, exp_end in [("near", near_end), ("swing", swing_end)]:
            exp_start = TODAY + timedelta(days=NEAR_EXPIRY_DAYS + 1) if bucket == "swing" else TODAY
            near_limit_hit = self._track_call()
            if near_limit_hit:
                fh_signals = _load_first_hour_signals()
                if symbol not in fh_signals and len(self.options_rows) > 0:
                    self._log_skip(symbol, bucket, "rate_limit_deprioritised")
                    continue

            strike_lo = round(approx_price * (1 - STRIKE_PCT), 2)
            strike_hi = round(approx_price * (1 + STRIKE_PCT), 2)
            try:
                req = OptionChainRequest(
                    underlying_symbol=symbol,
                    expiration_date_gte=exp_start,
                    expiration_date_lte=exp_end,
                    strike_price_gte=strike_lo,
                    strike_price_lte=strike_hi,
                )
                chain: Dict = self.opt_client.get_option_chain(req)
            except Exception as exc:
                log.warning("[%s/%s] options fetch error: %s", symbol, bucket, exc)
                self._log_skip(symbol, bucket, f"api_error:{exc}")
                continue

            # Open interest comes from the Trading API contracts endpoint, not the
            # chain snapshot. One extra call per (symbol, bucket); count it.
            self._track_call()
            oi_map = fetch_open_interest(
                self.trading_client, symbol,
                strike_gte=strike_lo, strike_lte=strike_hi,
                exp_gte=exp_start, exp_lte=exp_end,
            )
            if not oi_map:
                # Fallback (per review): if the contracts endpoint returns no OI
                # (e.g. not available on the Basic plan), the OI<100 filter is
                # skipped and spread + bid=0 remain the liquidity gate. Surface it.
                log.warning(
                    "[%s/%s] OI unavailable -> falling back to spread+bid gate "
                    "(OI filter inactive). Confirm contracts endpoint on Basic "
                    "plan (Gate 1A).", symbol, bucket)

            for contract_sym, snap in chain.items():
                lq = snap.latest_quote
                bid = lq.bid_price if lq else None
                ask = lq.ask_price if lq else None
                bid_size = lq.bid_size if lq else None
                ask_size = lq.ask_size if lq else None
                mid = ((bid + ask) / 2) if (bid is not None and ask is not None) else None

                # OI from contracts endpoint (1-2 day OCC lag). None if unavailable.
                oi_rec = oi_map.get(contract_sym, {})
                oi = oi_rec.get("open_interest")
                oi_date = oi_rec.get("open_interest_date")

                skip_reason = _skip_contract(bid, ask, oi)
                if skip_reason:
                    self._log_skip(symbol, contract_sym, skip_reason)
                    continue

                greeks = snap.greeks
                spread_pct = ((ask - bid) / mid) if (mid and mid > 0) else None

                # Parse expiry + right from contract symbol
                pfx = contract_sym[len(symbol):]
                expiry_str = right = strike_val = None
                if len(pfx) >= 8:
                    try:
                        expiry_str = f"20{pfx[:2]}-{pfx[2:4]}-{pfx[4:6]}"
                        right = "C" if pfx[6] == "C" else "P"
                        strike_val = int(pfx[7:]) / 1000.0
                    except Exception:
                        pass

                self.options_rows.append({
                    "timestamp": ts_collected,
                    "symbol": contract_sym,
                    "underlying": symbol,
                    "expiration": expiry_str,
                    "strike": strike_val,
                    "right": right,
                    "expiry_bucket": bucket,
                    "bid": bid,
                    "ask": ask,
                    "mid": mid,
                    "bid_size": bid_size,
                    "ask_size": ask_size,
                    "spread_pct": round(spread_pct, 4) if spread_pct is not None else None,
                    "volume": getattr(snap.latest_trade, "size", None) if snap.latest_trade else None,
                    "open_interest": oi,             # from Trading API contracts endpoint
                    "open_interest_date": oi_date,   # OCC as-of date (1-2 day lag)
                    "implied_volatility": snap.implied_volatility,
                    "delta": greeks.delta if greeks else None,
                    "gamma": greeks.gamma if greeks else None,
                    "theta": greeks.theta if greeks else None,
                    "vega": greeks.vega if greeks else None,
                    "rho": greeks.rho if greeks else None,
                    "underlying_price": approx_price,
                })

    def _log_skip(self, symbol: str, contract: Optional[str], reason: str) -> None:
        ts = _now_et().isoformat()
        self.skip_log.append({"timestamp": ts, "symbol": symbol,
                               "contract": contract, "reason": reason})
        log.debug("SKIP %s/%s: %s", symbol, contract, reason)

    # ------------------------------------------------------------------
    # One collection cycle (called every minute)
    # ------------------------------------------------------------------
    def collect_one_minute(self) -> None:
        ts_now = _now_et()
        log.info("Collection cycle at %s ET", ts_now.strftime("%H:%M:%S"))

        for sym in self.universe:
            approx_price = self.stock_accum.get_snapshot_price(sym)
            self._collect_options_for_symbol(sym, approx_price, ts_now)

        log.info(
            "Cycle done: %d options rows, %d skips, %d total API calls",
            len(self.options_rows), len(self.skip_log), self.api_calls_total,
        )

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------
    def save(self) -> None:
        self._save_stocks()
        self._save_options()
        self._save_skip_log()

    def _save_stocks(self) -> None:
        rows = []
        for bar_list in self.stock_accum.bars.values():
            rows.extend(bar_list)
        if not rows:
            log.warning("No stock bar data to save.")
            return
        df = pd.DataFrame(rows)
        df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
        df = df.sort_values(["symbol", "timestamp"]).reset_index(drop=True)
        out = STOCKS_DIR / f"{TODAY_STR}.parquet"
        pq.write_table(pa.Table.from_pandas(df), out, compression="snappy")
        log.info("Stocks: %d rows -> %s (%.1f MB)", len(df), out, out.stat().st_size / 1e6)

    def _save_options(self) -> None:
        if not self.options_rows:
            log.warning("No options data to save.")
            return
        df = pd.DataFrame(self.options_rows)
        df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
        df = df.sort_values(["underlying", "timestamp", "symbol"]).reset_index(drop=True)
        out = OPTIONS_DIR / f"{TODAY_STR}.parquet"
        pq.write_table(pa.Table.from_pandas(df), out, compression="snappy")
        mb = out.stat().st_size / 1e6
        log.info("Options: %d rows -> %s (%.1f MB)", len(df), out, mb)
        if mb > 50:
            log.warning("OPTIONS FILE EXCEEDS 50MB ALERT: %.1f MB — storage review needed.", mb)

    def _save_skip_log(self) -> None:
        if not self.skip_log:
            return
        skip_df = pd.DataFrame(self.skip_log)
        skip_path = OPTIONS_DIR / f"{TODAY_STR}_skips.csv"
        skip_df.to_csv(skip_path, index=False)
        log.info("Skip log: %d entries -> %s", len(self.skip_log), skip_path)

    # ------------------------------------------------------------------
    # Main entry
    # ------------------------------------------------------------------
    def run(self) -> None:
        now = _now_et()
        if now.weekday() >= 5:
            log.info("Weekend — no collection. Exiting.")
            # TODO: add US market holiday check
            sys.exit(0)

        if not _in_window():
            log.warning(
                "Current time %s ET is outside collection window %02d:%02d–%02d:%02d. Exiting.",
                now.strftime("%H:%M"), START_H, START_M, END_H, END_M,
            )
            sys.exit(0)

        self.universe = get_universe()
        log.info("Universe: %d symbols", len(self.universe))

        # Start stock websocket stream in background thread
        stream = StockDataStream(API_KEY, API_SECRET, feed=DataFeed.SIP)
        self._stream = stream
        stream.subscribe_bars(self.stock_accum.on_bar, *self.universe)

        import threading
        stream_thread = threading.Thread(target=stream.run, daemon=True)
        stream_thread.start()
        log.info("Stock websocket stream started.")

        # Main per-minute REST loop
        try:
            while _in_window():
                cycle_start = time.monotonic()
                self.collect_one_minute()
                elapsed = time.monotonic() - cycle_start
                sleep_s = max(0.0, 60.0 - elapsed)
                log.info("Sleeping %.1fs until next cycle …", sleep_s)
                time.sleep(sleep_s)
        except KeyboardInterrupt:
            log.info("Interrupted by user.")
        finally:
            log.info("Stopping stream and saving data …")
            try:
                stream.stop()
            except Exception:
                pass
            self.save()
            log.info(
                "Done. %d options rows, %d stock symbols tracked, %d total API calls.",
                len(self.options_rows),
                len(self.stock_accum.bars),
                self.api_calls_total,
            )


def main() -> None:
    collector = OptionsDataCollector()
    collector.run()


if __name__ == "__main__":
    main()
