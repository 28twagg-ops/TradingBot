"""
options_morning_bot.py — Phase 4 paper bot: TOP 5 strategies (multi-slot).

Runs five research-ranked strategies in parallel on the Alpaca PAPER account:
  S173 MomReversal long call
  S174 RubberBand long call EOD
  S165 GapDown long call 3 DTE
  S166 GapDown strong call (gap <= -3%, green close)
  S163 A1 GapDown ATM call EOD (control)

P&L is tracked and logged as **return % per trade** (not dollar matrices).

Paper lab: virtual $500 buckets → logs/options_trial/ (NOT rubber_band logs/)

Run:
    ALPACA_PAPER_KEY=... ALPACA_PAPER_SECRET=... python scripts/options_morning_bot.py
"""

from __future__ import annotations

import logging
import os
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import LimitOrderRequest, GetOrdersRequest
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
from alpaca.data.historical import OptionHistoricalDataClient, StockHistoricalDataClient
from alpaca.data.requests import OptionChainRequest, StockBarsRequest
from alpaca.data.timeframe import TimeFrame

sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_universe import get_universe, to_alpaca_symbol
from options_oi import make_trading_client, fetch_open_interest
from options_signals import PAPER_STRATEGIES, SignalHit, scan_symbol, StrategyConfig
from options_lab import (
    VIRTUAL_BUCKET_USD, PAPER_UNLIMITED_BUCKETS, EffectiveArm, LabState,
    active_bucket_count,
    append_ledger, arms_for_signal, entry_limit_price, exit_limit_price,
    exit_reason_for_lot, load_state, make_entry_client_order_id,
    make_exit_client_order_id, print_trial_stats, reconcile_with_broker,
    register_entry_immediate, register_exit, size_for_arm, trial_root,
)

# --------------------------------------------------------------------------- #
#  HARD SAFETY LOCK
# --------------------------------------------------------------------------- #
PAPER_TRADING = True   # DO NOT flip to False here. Going live = Phase 5, with
                       # shared-account coordination (Task 5.2) implemented first.

# --------------------------------------------------------------------------- #
#  Shared filters (per-arm caps applied in options_lab)
# --------------------------------------------------------------------------- #
RIGHT               = "C"
STRIKE_PCT          = 0.10

MIN_OPEN_INTEREST   = 100          # default; arms may override
MAX_SPREAD_FRAC     = 0.25         # default; arms may override
MIN_UNDERLYING_PX   = 3.0
REAL_ACCOUNT_OPTIONS_CAP = 0.90   # never deploy >90% of real equity in options

MAX_NEW_ENTRIES_PER_RUN = 100     # signals x buckets (grid mode)
BAR_CHUNK_SIZE      = 80
SCAN_LOOKBACK_DAYS  = 90

# Time windows (ET)
ENTRY_START = (9, 28)
ENTRY_END   = (11, 35)
EOD_SWEEP   = (15, 30)
EOD_MARKET  = (15, 50)
HARD_STOP   = (16, 5)

ET = ZoneInfo("America/New_York")
TODAY = date.today()

# Paper credentials ONLY — do not use live ALPACA_API_KEY (equity bot keys).
# GitHub Actions: secrets ALPACA_PAPER_KEY / ALPACA_PAPER_SECRET
API_KEY = os.getenv("ALPACA_PAPER_KEY")
API_SECRET = os.getenv("ALPACA_PAPER_SECRET")

REPO_ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = trial_root() / "runs"
OCC_RE = re.compile(r"^[A-Z]+\d{6}[CP]\d{8}$")

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("options_morning_bot")
_run_log: list[str] = []


def _now_et() -> datetime:
    return datetime.now(ET)


def _hm_ge(now: datetime, hm: tuple[int, int]) -> bool:
    return (now.hour, now.minute) >= hm


def _hm_between(now: datetime, lo: tuple[int, int], hi: tuple[int, int]) -> bool:
    return lo <= (now.hour, now.minute) <= hi


def rl(msg: str) -> None:
    """Record a line for both the python log and the markdown run log."""
    log.info(msg)
    _run_log.append(msg)


# --------------------------------------------------------------------------- #
#  Clients
# --------------------------------------------------------------------------- #

def get_clients():
    trade = TradingClient(API_KEY, API_SECRET, paper=PAPER_TRADING)
    opt = OptionHistoricalDataClient(API_KEY, API_SECRET)
    stock = StockHistoricalDataClient(API_KEY, API_SECRET)
    ref = make_trading_client(API_KEY, API_SECRET, paper=PAPER_TRADING)
    return trade, opt, stock, ref


def verify_paper_auth(trade) -> bool:
    """Fail fast with a clear log if paper keys are wrong or missing."""
    try:
        acct = trade.get_account()
        rl(f"Paper auth OK — equity ${float(acct.equity):.2f}, "
           f"account {getattr(acct, 'account_number', '?')}")
        return True
    except Exception as exc:
        rl("FATAL: paper API auth failed. This bot requires ALPACA_PAPER_KEY and "
           "ALPACA_PAPER_SECRET (not the live equity-bot keys). "
           f"Detail: {exc}")
        return False

def _is_option_symbol(sym: str) -> bool:
    return bool(OCC_RE.match(sym or ""))


def option_positions(trade) -> list:
    out = []
    try:
        for p in trade.get_all_positions():
            ac = str(getattr(p, "asset_class", "") or "")
            if "option" in ac.lower() or _is_option_symbol(getattr(p, "symbol", "")):
                out.append(p)
    except Exception as exc:
        rl(f"ERROR reading positions: {exc}")
    return out


def open_option_premium(trade) -> float:
    total = 0.0
    for p in option_positions(trade):
        try:
            total += abs(float(getattr(p, "cost_basis", 0)) or 0.0)
        except Exception:
            pass
    return total


def cancel_stale_option_orders(trade) -> int:
    """Option-1 fill behavior: cancel option orders left open from prior runs."""
    n = 0
    try:
        req = GetOrdersRequest(status=QueryOrderStatus.OPEN, limit=200)
        for o in trade.get_orders(req):
            sym = getattr(o, "symbol", "")
            ac = str(getattr(o, "asset_class", "") or "")
            if "option" in ac.lower() or _is_option_symbol(sym):
                try:
                    trade.cancel_order_by_id(o.id)
                    n += 1
                except Exception as exc:
                    rl(f"  cancel failed {sym}: {exc}")
    except Exception as exc:
        rl(f"ERROR listing open orders: {exc}")
    if n:
        rl(f"Cancelled {n} stale option order(s) from prior run.")
    return n


# --------------------------------------------------------------------------- #
#  Signal scan (top 5 strategies)
# --------------------------------------------------------------------------- #

def _strategy_by_id(sid: str) -> StrategyConfig | None:
    for s in PAPER_STRATEGIES:
        if s.id == sid:
            return s
    return None


def scan_all_signals(stock, universe: list[str]) -> list[SignalHit]:
    """Scan universe; one hit per symbol (highest-priority strategy wins)."""
    out: list[SignalHit] = []
    start = datetime.now(ET) - timedelta(days=SCAN_LOOKBACK_DAYS)
    df, failed = _fetch_daily_bars(stock, universe, start)
    if df is None or df.empty:
        rl("ERROR fetching daily bars for scan: no data returned")
        return out

    symbols_in_df = set(df.index.get_level_values(0))
    n_ok = sum(1 for sym in universe if to_alpaca_symbol(sym) in symbols_in_df)
    if failed:
        rl(f"Fetched daily bars for {n_ok}/{len(universe)} symbols "
           f"({len(failed)} skipped: {', '.join(failed[:8])}"
           f"{', …' if len(failed) > 8 else ''})")
    else:
        rl(f"Fetched daily bars for {n_ok}/{len(universe)} symbols")

    priority = {s.id: i for i, s in enumerate(PAPER_STRATEGIES)}
    for sym in universe:
        try:
            alpaca_sym = to_alpaca_symbol(sym)
            if alpaca_sym not in symbols_in_df:
                continue
            sub = df.xs(alpaca_sym, level=0)
            hits = scan_symbol(sub, sym, TODAY, MIN_UNDERLYING_PX)
            if not hits:
                continue
            hits.sort(key=lambda h: priority.get(h.strategy_id, 99))
            out.append(hits[0])
        except Exception:
            continue
    out.sort(key=lambda h: priority.get(h.strategy_id, 99))
    return out


def _fetch_one_bar(stock, alpaca_sym: str, start: datetime):
    """Return daily bars df for one Alpaca symbol, or None."""
    try:
        req = StockBarsRequest(
            symbol_or_symbols=alpaca_sym,
            timeframe=TimeFrame.Day,
            start=start,
        )
        df = stock.get_stock_bars(req).df
        if df is not None and not df.empty:
            return df
    except Exception:
        pass
    return None


def _fetch_daily_bars(stock, universe: list[str], start: datetime):
    """Fetch daily bars in chunks; per-symbol fallback if a chunk fails."""
    chunks: list[pd.DataFrame] = []
    failed: list[str] = []

    for i in range(0, len(universe), BAR_CHUNK_SIZE):
        batch = universe[i:i + BAR_CHUNK_SIZE]
        alpaca_batch = [to_alpaca_symbol(s) for s in batch]
        try:
            req = StockBarsRequest(
                symbol_or_symbols=alpaca_batch,
                timeframe=TimeFrame.Day,
                start=start,
            )
            df = stock.get_stock_bars(req).df
            if df is not None and not df.empty:
                chunks.append(df)
                continue
        except Exception as exc:
            log.warning("Bar chunk %d-%d failed: %s", i, i + len(batch), exc)

        for sym in batch:
            df = _fetch_one_bar(stock, to_alpaca_symbol(sym), start)
            if df is not None:
                chunks.append(df)
            else:
                failed.append(sym)

    if not chunks:
        return None, failed
    combined = pd.concat(chunks)
    if combined.index.duplicated().any():
        combined = combined[~combined.index.duplicated(keep="last")]
    return combined, failed


# --------------------------------------------------------------------------- #
#  ATM call selection
# --------------------------------------------------------------------------- #

def _parse_occ(contract_sym: str, underlying: str):
    pfx = contract_sym[len(underlying):]
    if len(pfx) < 8:
        return None, None, None
    try:
        expiry = f"20{pfx[:2]}-{pfx[2:4]}-{pfx[4:6]}"
        right = "C" if pfx[6] == "C" else "P"
        strike = int(pfx[7:]) / 1000.0
        return expiry, right, strike
    except Exception:
        return None, None, None


def pick_atm_call(opt, ref, symbol: str, price: float,
                  dte_min: int, dte_max: int, dte_target: int,
                  arm: EffectiveArm):
    """Return dict for the best ATM call, or None if nothing tradeable."""
    api_sym = to_alpaca_symbol(symbol)
    max_premium = arm.max_premium
    max_spread = arm.max_spread_frac
    min_oi = arm.min_open_interest
    exp_lo = TODAY + timedelta(days=dte_min)
    exp_hi = TODAY + timedelta(days=dte_max)
    strike_lo = round(price * (1 - STRIKE_PCT), 2)
    strike_hi = round(price * (1 + STRIKE_PCT), 2)
    try:
        req = OptionChainRequest(
            underlying_symbol=api_sym,
            expiration_date_gte=exp_lo, expiration_date_lte=exp_hi,
            strike_price_gte=strike_lo, strike_price_lte=strike_hi,
        )
        chain = opt.get_option_chain(req)
    except Exception as exc:
        rl(f"  [{symbol}] chain error: {exc}")
        return None
    if not chain:
        return None

    oi_map = {}
    try:
        oi_map = fetch_open_interest(ref, api_sym, strike_gte=strike_lo,
                                    strike_lte=strike_hi,
                                    exp_gte=exp_lo, exp_lte=exp_hi)
    except Exception:
        oi_map = {}

    best = None
    for csym, snap in chain.items():
        expiry, right, strike = _parse_occ(csym, api_sym)
        if right != "C" or strike is None or expiry is None:
            continue
        lq = getattr(snap, "latest_quote", None)
        bid = getattr(lq, "bid_price", None) if lq else None
        ask = getattr(lq, "ask_price", None) if lq else None
        if not bid or not ask or bid <= 0 or ask <= 0:
            continue
        mid = (bid + ask) / 2
        spread_frac = (ask - bid) / mid if mid > 0 else 9.9
        if spread_frac > max_spread:
            continue
        cost = ask * 100
        if cost > max_premium:
            continue
        oi = (oi_map.get(csym) or {}).get("open_interest")
        if oi is not None and oi < min_oi:
            continue
        try:
            dte = (date.fromisoformat(expiry) - TODAY).days
        except Exception:
            continue
        moneyness = abs(strike - price)
        # rank: closest to ATM, then closest DTE to target
        score = (moneyness, abs(dte - dte_target))
        cand = {"symbol": csym, "underlying": symbol, "strike": strike,
                "expiry": expiry, "dte": dte, "bid": bid, "ask": ask, "mid": mid,
                "spread_frac": spread_frac, "cost": cost, "oi": oi, "score": score}
        if best is None or score < best["score"]:
            best = cand
    return best


# --------------------------------------------------------------------------- #
#  Exits (per virtual lot / arm stop rules)
# --------------------------------------------------------------------------- #

def _sell_limit(trade, sym: str, qty: int, limit: float, tag: str,
                client_order_id: str | None = None):
    try:
        kwargs = dict(
            symbol=sym, qty=qty, side=OrderSide.SELL,
            time_in_force=TimeInForce.DAY, limit_price=round(max(0.01, limit), 2))
        if client_order_id:
            kwargs["client_order_id"] = client_order_id[:48]
        o = trade.submit_order(LimitOrderRequest(**kwargs))
        rl(f"  EXIT {tag} SELL {qty} {sym} @<= {limit:.2f}  id={o.id}")
    except Exception as exc:
        rl(f"  EXIT {tag} SELL failed {sym}: {exc}")


def manage_exits(trade, opt, state: LabState, now: datetime) -> None:
    eod = _hm_ge(now, EOD_SWEEP)
    occ_symbols = {l.occ_symbol for l in state.lots if l.qty > 0}
    pos_by_occ = {getattr(p, "symbol", ""): p for p in option_positions(trade)}

    for occ in occ_symbols:
        p = pos_by_occ.get(occ)
        if not p:
            continue
        try:
            pos_qty = int(float(getattr(p, "qty", 0)))
            plpc = float(getattr(p, "unrealized_plpc", 0) or 0.0)
        except Exception:
            continue
        if pos_qty <= 0:
            continue

        bid = None
        try:
            m = re.match(r"^[A-Z]+", occ)
            underlying = m.group(0) if m else None
            if underlying:
                ch = opt.get_option_chain(OptionChainRequest(underlying_symbol=underlying))
                snap = ch.get(occ) if ch else None
                lq = getattr(snap, "latest_quote", None) if snap else None
                bid = getattr(lq, "bid_price", None) if lq else None
        except Exception:
            bid = None

        for lot in list(state.lots_for_occ(occ)):
            if lot.qty <= 0:
                continue
            reason = exit_reason_for_lot(lot, plpc, eod)
            if not reason:
                continue
            sell_qty = min(lot.qty, pos_qty)
            if sell_qty <= 0:
                continue
            ret_pct = plpc * 100.0
            tag = f"[b{lot.bucket_id}|{lot.profile_name}|{lot.strategy_id}] {reason}"
            cid = make_exit_client_order_id(lot.bucket_id, lot.strategy_id, lot.lot_id)
            cost_sold = (
                lot.entry_cost * (sell_qty / lot.qty) if lot.qty else lot.entry_cost
            )
            pnl_usd = cost_sold * (ret_pct / 100.0)

            sell_limit = exit_limit_price(lot, bid or 0.01, bid or 0.01, (bid or 0.01))
            if bid:
                ask_est = bid * 1.02
                sell_limit = exit_limit_price(lot, bid, ask_est, (bid + ask_est) / 2)

            use_market = _hm_ge(now, EOD_MARKET) or (not bid and lot.market_exit_eod)
            if use_market:
                try:
                    from alpaca.trading.requests import MarketOrderRequest
                    o = trade.submit_order(MarketOrderRequest(
                        symbol=occ, qty=sell_qty, side=OrderSide.SELL,
                        time_in_force=TimeInForce.DAY,
                        client_order_id=cid[:48]))
                    rl(f"  EXIT {tag} MARKET SELL {sell_qty} {occ} "
                       f"return={ret_pct:+.1f}%  id={o.id}")
                except Exception as exc:
                    rl(f"  EXIT {tag} market failed {occ}: {exc}")
                    continue
            else:
                _sell_limit(trade, occ, sell_qty, sell_limit, tag, cid)

            append_ledger({
                "ts": now.isoformat(),
                "event": "exit",
                "bucket_id": lot.bucket_id,
                "profile": lot.profile_name,
                "strategy_id": lot.strategy_id,
                "lot_id": lot.lot_id,
                "symbol": lot.underlying,
                "occ": occ,
                "qty": sell_qty,
                "cost": round(cost_sold, 2),
                "return_pct": round(ret_pct, 2),
                "pnl_usd": round(pnl_usd, 2),
                "reason": reason,
                "sell_offset": lot.sell_limit_offset,
                "take_profit": lot.take_profit,
                "stop_loss": lot.stop_loss,
            })
            register_exit(state, lot, sell_qty)
            pos_qty -= sell_qty


# --------------------------------------------------------------------------- #
#  Entries
# --------------------------------------------------------------------------- #

def place_entries(trade, opt, ref, signals: list[SignalHit], state: LabState,
                  now: datetime) -> int:
    try:
        acct = trade.get_account()
        equity = float(acct.equity)
    except Exception as exc:
        rl(f"ERROR reading account: {exc}")
        return 0

    buckets = active_bucket_count(equity)
    rl(f"Paper lab: ${equity:.0f} broker equity -> {buckets} bucket(s) "
       f"(${VIRTUAL_BUCKET_USD:.0f} virtual each"
       f"{', unlimited paper' if PAPER_UNLIMITED_BUCKETS else ''})")

    real_open = open_option_premium(trade)
    real_cap = REAL_ACCOUNT_OPTIONS_CAP * equity

    placed = 0
    for hit in signals:
        if placed >= MAX_NEW_ENTRIES_PER_RUN:
            break
        strat = _strategy_by_id(hit.strategy_id)
        if not strat:
            continue
        for arm in arms_for_signal(hit.strategy_id, equity):
            if placed >= MAX_NEW_ENTRIES_PER_RUN:
                break
            if state.bucket_has_strategy(arm.bucket_id, hit.strategy_id):
                continue
            if state.pending_for_bucket_strategy(arm.bucket_id, hit.strategy_id):
                continue
            if state.bucket_holds_underlying(arm.bucket_id, hit.symbol):
                continue
            cand = pick_atm_call(opt, ref, hit.symbol, hit.price,
                                 strat.dte_min, strat.dte_max, strat.dte_target, arm)
            if not cand:
                rl(f"  [b{arm.bucket_id}|{arm.profile_name}] {hit.strategy_id} "
                   f"{hit.symbol}: no tradeable call")
                continue
            if real_open + cand["cost"] > real_cap:
                rl(f"  [b{arm.bucket_id}] real account cap (${real_cap:.0f}) — skip")
                continue
            qty = size_for_arm(arm, state, cand["cost"])
            if qty < 1:
                rl(f"  [b{arm.bucket_id}|{arm.profile_name}] bucket full "
                   f"({arm.account_cap:.0%} of ${arm.virtual_equity:.0f}) — skip")
                continue
            limit = entry_limit_price(arm, cand["bid"], cand["ask"], cand["mid"])
            cid = make_entry_client_order_id(arm.bucket_id, hit.strategy_id)
            try:
                o = trade.submit_order(LimitOrderRequest(
                    symbol=cand["symbol"], qty=qty, side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY, limit_price=limit,
                    client_order_id=cid))
                placed += 1
                entry_cost = cand["cost"] * qty
                real_open += entry_cost
                lot = register_entry_immediate(
                    state, arm, cand["symbol"], hit.symbol, qty,
                    entry_cost, limit, str(o.id))
                append_ledger({
                    "ts": now.isoformat(),
                    "event": "entry",
                    "bucket_id": arm.bucket_id,
                    "profile": arm.profile_name,
                    "strategy_id": hit.strategy_id,
                    "lot_id": lot.lot_id,
                    "symbol": hit.symbol,
                    "occ": cand["symbol"],
                    "qty": qty,
                    "limit": limit,
                    "cost": round(entry_cost, 2),
                    "buy_offset": arm.buy_limit_offset,
                    "take_profit": arm.take_profit,
                    "stop_loss": arm.stop_loss,
                    "spread_frac": round(cand["spread_frac"], 3),
                    "detail": hit.detail,
                })
                rl(f"  ENTRY [b{arm.bucket_id}|{arm.profile_name}|{hit.strategy_id}] "
                   f"BUY {qty}x {cand['symbol']} ({hit.detail}) "
                   f"limit={limit:.2f} (ask={cand['ask']:.2f} off={arm.buy_limit_offset:+.2f}) "
                   f"tp={arm.take_profit:+.0%} sl={arm.stop_loss:+.0%} lot={lot.lot_id} "
                   f"id={o.id}")
            except Exception as exc:
                rl(f"  [b{arm.bucket_id} {hit.symbol}] ENTRY failed: {exc}")
    return placed


def _position_snapshots(trade) -> list[dict]:
    out = []
    for p in option_positions(trade):
        try:
            plpc = float(getattr(p, "unrealized_plpc", 0) or 0.0)
        except Exception:
            plpc = 0.0
        try:
            qty = int(float(getattr(p, "qty", 0)))
        except Exception:
            qty = 0
        try:
            upl = float(getattr(p, "unrealized_pl", 0) or 0.0)
        except Exception:
            upl = 0.0
        try:
            cost = abs(float(getattr(p, "cost_basis", 0) or 0.0))
        except Exception:
            cost = 0.0
        out.append({
            "symbol": getattr(p, "symbol", ""),
            "qty": qty,
            "plpc": plpc,
            "unrealized_pl": upl,
            "cost_basis": cost,
        })
    return out


def _snapshot_equity(trade) -> float | None:
    try:
        return float(trade.get_account().equity)
    except Exception:
        return None

def write_run_log(now: datetime, header: str) -> None:
    try:
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        path = LOG_DIR / f"{TODAY.isoformat()}.md"
        new = not path.exists()
        with open(path, "a", encoding="utf-8") as f:
            if new:
                f.write(f"# Options morning bot (PAPER) — {TODAY.isoformat()}\n\n")
                f.write("_Paper lab: virtual $500 buckets, per-bucket buy/sell experiments._\n\n")
            f.write(f"## {now.strftime('%H:%M:%S')} ET — {header}\n\n")
            for line in _run_log:
                f.write(f"- {line}\n")
            f.write("\n")
    except Exception as exc:
        log.error("Failed to write run log: %s", exc)


# --------------------------------------------------------------------------- #
#  Orchestration
# --------------------------------------------------------------------------- #

def run() -> int:
    global _run_log
    _run_log = []

    if not PAPER_TRADING:
        print("REFUSING TO RUN: PAPER_TRADING is False. This bot is paper-only "
              "until Phase 5 (live integration + shared-account coordination).")
        return 2
    if not API_KEY or not API_SECRET:
        print("ERROR: set ALPACA_PAPER_KEY and ALPACA_PAPER_SECRET "
              "(paper account keys — not the live equity-bot keys).")
        return 1

    now = _now_et()
    rl(f"=== options_morning_bot (PAPER) {now.isoformat()} ===")

    # Outside trading window — still show stats if keys work
    if not _hm_between(now, ENTRY_START, HARD_STOP):
        rl(f"Outside trading window ({now.strftime('%H:%M')} ET).")
        state = load_state()
        equity = None
        positions = []
        try:
            trade, _, _, _ = get_clients()
            if verify_paper_auth(trade):
                equity = _snapshot_equity(trade)
                positions = _position_snapshots(trade)
                state = reconcile_with_broker(trade, state, log_fn=lambda m: rl(m))
        except Exception:
            pass
        print_trial_stats(state, equity, positions, log_fn=rl)
        write_run_log(now, "idle (outside window)")
        return 0

    trade, opt, stock, ref = get_clients()

    if not verify_paper_auth(trade):
        state = load_state()
        print_trial_stats(state, None, [], log_fn=rl)
        write_run_log(now, "FATAL auth failed (wrong keys?)")
        return 1

    equity = _snapshot_equity(trade)
    state = load_state()
    state = reconcile_with_broker(trade, state, log_fn=lambda m: rl(m))

    rl(f"Active buckets: {active_bucket_count(equity or 0)} | "
       f"Strategies: {', '.join(s.id for s in PAPER_STRATEGIES)}")

    # 1. cancel stale orders (Option-1 fill)
    cancel_stale_option_orders(trade)

    # 2. manage exits (per-arm stop rules)
    manage_exits(trade, opt, state, now)

    # 3+4. entries only within the entry window
    if _hm_between(now, ENTRY_START, ENTRY_END):
        universe = get_universe()
        strat_ids = ", ".join(s.id for s in PAPER_STRATEGIES)
        rl(f"Scanning {len(universe)} symbols for [{strat_ids}] …")
        signals = scan_all_signals(stock, universe)
        if signals:
            summary = [f"{h.strategy_id}:{h.symbol}" for h in signals[:8]]
            rl(f"Found {len(signals)} signal(s); top: {summary}")
        else:
            rl("Found 0 signals across top-5 strategies")
        placed = place_entries(trade, opt, ref, signals, state, now)
        rl(f"Placed {placed} new entry order(s).")
        header = f"entry+manage ({placed} new)"
    else:
        header = "manage-only (past entry window)"
        rl("Past entry window; manage/exit only.")

    positions = _position_snapshots(trade)
    print_trial_stats(state, equity, positions, log_fn=rl)
    write_run_log(now, header)
    print("STATUS: options_morning_bot run complete (PAPER).", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(run())
