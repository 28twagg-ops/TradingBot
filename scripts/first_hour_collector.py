"""
first_hour_collector.py — Task 1.2: First-hour stock data collection.

Runs 9:28–10:35 AM ET (first 65 minutes of trading) collecting 1-minute bars
for all ~900 S&P 500 + S&P 400 MidCap symbols via Alpaca StockDataStream websocket.

Outputs:
  data/first_hour/YYYY-MM-DD.parquet       — one row per symbol per minute
  data/first_hour/YYYY-MM-DD_summary.parquet — one summary row per symbol

Derived fields computed in real time:
  pct_change_from_open, vol_ratio (raw volume fallback until 30-day history exists),
  range_pct, gap_pct (from prior close if available), above_vwap,
  opening_range_high / opening_range_low (locked at 9:45 ET).

Run:
    ALPACA_API_KEY=... ALPACA_SECRET_KEY=... python scripts/first_hour_collector.py

Reads creds from env; exits with message if missing.
TODO: Add US market holiday skip (currently only skips weekends).
"""

from __future__ import annotations

import asyncio
import logging
import os
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from alpaca.data.enums import DataFeed
from alpaca.data.live import StockDataStream
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest, StockLatestQuoteRequest
from alpaca.data.timeframe import TimeFrame

# Import universe helper (no Alpaca creds required for this module)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_universe import get_universe

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
DATA_DIR = _REPO_ROOT / "data" / "first_hour"
DATA_DIR.mkdir(parents=True, exist_ok=True)

TODAY_STR = date.today().strftime("%Y-%m-%d")

# Collection window: 9:28 – 10:35 ET
START_H, START_M = 9, 28
END_H, END_M = 10, 35

# Opening range: 9:30–9:45 ET; locked after 9:45
OR_LOCK_H, OR_LOCK_M = 9, 45


# ---------------------------------------------------------------------------
# Collector state
# ---------------------------------------------------------------------------
class FirstHourCollector:
    """Manages websocket bar collection and in-memory state for one session."""

    def __init__(self) -> None:
        self.universe: list[str] = []
        self.bars: dict[str, list[dict]] = defaultdict(list)  # symbol -> list of bar dicts
        self.open_prices: dict[str, float] = {}               # first bar open
        self.prior_closes: dict[str, float] = {}              # loaded from yesterday
        self.running_vwap_num: dict[str, float] = defaultdict(float)  # price*vol sum
        self.running_vwap_den: dict[str, float] = defaultdict(float)  # vol sum
        self.or_high: dict[str, float] = {}   # opening range high (locked at 9:45)
        self.or_low: dict[str, float] = {}    # opening range low  (locked at 9:45)
        self.or_locked: bool = False
        self.or_candidates: dict[str, list[float]] = defaultdict(list)  # pre-lock highs
        self.or_low_candidates: dict[str, list[float]] = defaultdict(list)
        self.stream: StockDataStream | None = None
        self._stop_event = asyncio.Event()

    # ------------------------------------------------------------------
    # Prior-close loading
    # ------------------------------------------------------------------
    def load_prior_closes(self) -> None:
        """Load prior session close from yesterday's first_hour parquet if it exists.
        Falls back to Alpaca historical bars for symbols not in the file.
        gap_pct will be None for symbols where prior close is unavailable.
        """
        yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        # Scan backwards up to 5 calendar days for most-recent trading day
        for delta in range(1, 6):
            d = (date.today() - timedelta(days=delta)).strftime("%Y-%m-%d")
            path = DATA_DIR / f"{d}_summary.parquet"
            if path.exists():
                try:
                    df = pd.read_parquet(path, columns=["symbol", "close"])
                    self.prior_closes = dict(zip(df["symbol"], df["close"]))
                    log.info("Loaded %d prior closes from %s", len(self.prior_closes), path.name)
                    return
                except Exception as exc:
                    log.warning("Could not load prior closes from %s: %s", path.name, exc)

        log.info("No prior-day parquet found; gap_pct will be None for all symbols.")

    # ------------------------------------------------------------------
    # Bar handler
    # ------------------------------------------------------------------
    async def on_bar(self, bar) -> None:
        """Callback fired by StockDataStream for each 1-minute bar."""
        sym = bar.symbol
        ts = bar.timestamp  # timezone-aware UTC from Alpaca
        ts_et = ts.astimezone(ET)

        # Guard: only record bars within our window
        now = datetime.now(ET)
        window_start = now.replace(hour=START_H, minute=START_M, second=0, microsecond=0)
        window_end = now.replace(hour=END_H, minute=END_M, second=59, microsecond=0)
        if not (window_start <= ts_et <= window_end):
            return

        o, h, l, c, v = bar.open, bar.high, bar.low, bar.close, bar.volume
        vwap_bar = getattr(bar, "vwap", None)
        trade_count = getattr(bar, "trade_count", None)

        # Derived: open price (first bar for this symbol)
        if sym not in self.open_prices:
            self.open_prices[sym] = o

        open_price = self.open_prices[sym]
        pct_change_from_open = (c - open_price) / open_price if open_price else None
        range_pct = (h - l) / open_price if open_price else None
        prior_close = self.prior_closes.get(sym)
        gap_pct = (open_price - prior_close) / prior_close if prior_close else None

        # Running VWAP
        self.running_vwap_num[sym] += c * v
        self.running_vwap_den[sym] += v
        vwap_running = (
            self.running_vwap_num[sym] / self.running_vwap_den[sym]
            if self.running_vwap_den[sym] > 0 else None
        )
        above_vwap = (c > vwap_running) if vwap_running is not None else None

        # Opening range candidates (before 9:45 lock)
        or_lock_time = ts_et.replace(hour=OR_LOCK_H, minute=OR_LOCK_M, second=0, microsecond=0)
        if ts_et < or_lock_time:
            self.or_candidates[sym].append(h)
            self.or_low_candidates[sym].append(l)

        # Lock opening range at 9:45 (first bar AT or AFTER 9:45)
        if not self.or_locked and ts_et >= or_lock_time:
            self.or_locked = True
            for s in self.universe:
                if self.or_candidates.get(s):
                    self.or_high[s] = max(self.or_candidates[s])
                    self.or_low[s] = min(self.or_low_candidates[s])
            log.info("Opening range locked at %s", ts_et.strftime("%H:%M ET"))

        # vol_ratio: if we had 30-day history loaded we would compute here.
        # For now, use raw volume as documented fallback.
        # TODO: after 2 weeks of data, replace with avg_30day_volume_same_time
        vol_ratio = float(v)  # raw volume fallback — see SCHEMA.md for field description

        row = {
            "timestamp": ts,
            "symbol": sym,
            "open": o,
            "high": h,
            "low": l,
            "close": c,
            "volume": int(v),
            "vwap": vwap_bar,
            "trade_count": trade_count,
            # derived
            "pct_change_from_open": pct_change_from_open,
            "vol_ratio": vol_ratio,           # raw-volume fallback documented above
            "range_pct": range_pct,
            "gap_pct": gap_pct,
            "above_vwap": above_vwap,
            "opening_range_high": self.or_high.get(sym),
            "opening_range_low": self.or_low.get(sym),
        }
        self.bars[sym].append(row)

    # ------------------------------------------------------------------
    # Stop trigger
    # ------------------------------------------------------------------
    async def _auto_stop(self) -> None:
        """Sleep until collection window closes, then stop the stream."""
        now = datetime.now(ET)
        stop_dt = now.replace(hour=END_H, minute=END_M, second=30, microsecond=0)
        if now >= stop_dt:
            log.warning("Already past collection window end; stopping immediately.")
            self._stop_event.set()
            return
        wait_s = (stop_dt - now).total_seconds()
        log.info("Collection will stop at %s ET (~%.0f min)", stop_dt.strftime("%H:%M"), wait_s / 60)
        await asyncio.sleep(wait_s)
        log.info("Collection window closed — stopping stream.")
        self._stop_event.set()
        if self.stream:
            self.stream.stop()

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------
    def _to_dataframe(self) -> pd.DataFrame:
        rows = []
        for bar_list in self.bars.values():
            rows.extend(bar_list)
        if not rows:
            return pd.DataFrame()
        df = pd.DataFrame(rows)
        df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
        df = df.sort_values(["symbol", "timestamp"]).reset_index(drop=True)
        return df

    def save_parquet(self) -> None:
        df = self._to_dataframe()
        if df.empty:
            log.warning("No bar data collected; not writing parquet.")
            return

        out_path = DATA_DIR / f"{TODAY_STR}.parquet"
        pq.write_table(pa.Table.from_pandas(df), out_path, compression="snappy")
        log.info("Saved %d rows to %s (%.1f MB)", len(df), out_path, out_path.stat().st_size / 1e6)

        # Summary parquet
        self._save_summary(df)

    def _save_summary(self, df: pd.DataFrame) -> None:
        """One row per symbol: first-hour aggregates."""
        summary_rows = []
        for sym, grp in df.groupby("symbol"):
            if grp.empty:
                continue
            first = grp.iloc[0]
            last = grp.iloc[-1]
            open_p = first["open"]
            close_p = last["close"]
            total_first_hour_return = (
                (close_p - open_p) / open_p if open_p else None
            )

            # vol_ratio summary: same raw-volume fallback applies
            total_vol = grp["volume"].sum()
            first_hour_volume_ratio = float(total_vol)  # raw fallback

            prior_close = self.prior_closes.get(sym)
            opened_above_prior_close = (
                bool(open_p > prior_close) if prior_close else None
            )

            or_h = self.or_high.get(sym)
            or_l = self.or_low.get(sym)
            all_highs = grp["high"]
            all_lows = grp["low"]
            touched_or_high = bool((all_highs >= or_h).any()) if or_h is not None else None
            touched_or_low = bool((all_lows <= or_l).any()) if or_l is not None else None

            summary_rows.append({
                "date": TODAY_STR,
                "symbol": sym,
                "open": open_p,
                "high": float(grp["high"].max()),
                "low": float(grp["low"].min()),
                "close": close_p,
                "volume": int(total_vol),
                "bars_collected": len(grp),
                "total_first_hour_return": total_first_hour_return,
                "first_hour_volume_ratio": first_hour_volume_ratio,
                "opened_above_prior_close": opened_above_prior_close,
                "opening_range_high": or_h,
                "opening_range_low": or_l,
                "touched_opening_range_high": touched_or_high,
                "touched_opening_range_low": touched_or_low,
            })

        if not summary_rows:
            log.warning("No summary data to write.")
            return

        sum_df = pd.DataFrame(summary_rows)
        sum_path = DATA_DIR / f"{TODAY_STR}_summary.parquet"
        pq.write_table(pa.Table.from_pandas(sum_df), sum_path, compression="snappy")
        log.info("Summary: %d symbols -> %s", len(sum_df), sum_path)

    # ------------------------------------------------------------------
    # Main entry
    # ------------------------------------------------------------------
    def run(self) -> None:
        now = datetime.now(ET)
        if now.weekday() >= 5:
            log.info("Weekend — no collection today. Exiting.")
            # TODO: add US market holiday check
            sys.exit(0)

        self.universe = get_universe()
        log.info("Universe: %d symbols", len(self.universe))
        self.load_prior_closes()

        stream = StockDataStream(API_KEY, API_SECRET, feed=DataFeed.SIP)
        self.stream = stream

        async def _run() -> None:
            stream.subscribe_bars(self.on_bar, *self.universe)
            stop_task = asyncio.create_task(self._auto_stop())
            stream_task = asyncio.create_task(asyncio.to_thread(stream.run))
            await self._stop_event.wait()
            stop_task.cancel()
            # Give stream a moment to flush
            await asyncio.sleep(2)
            stream_task.cancel()
            try:
                await stream_task
            except (asyncio.CancelledError, Exception):
                pass

        try:
            asyncio.run(_run())
        except KeyboardInterrupt:
            log.info("Interrupted by user.")
        finally:
            log.info("Saving data …")
            self.save_parquet()
            total_bars = sum(len(v) for v in self.bars.values())
            symbols_with_data = len(self.bars)
            log.info(
                "Done. %d bars across %d symbols collected.",
                total_bars, symbols_with_data,
            )


def main() -> None:
    collector = FirstHourCollector()
    collector.run()


if __name__ == "__main__":
    main()
