"""
options_morning_bot.py — Phase 4 paper bot: multi-strategy options (PAPER).

Runs research-ranked strategies on the Alpaca PAPER account:
  S165 GapDown long call 3 DTE (control)
  S164 GapDown ATM 1-DTE — P2B
  S168 GapDown ATM 5-DTE — P2B
  S167 GapDown 1-strike OTM ~3-DTE — P2C (reclaims S174 buckets)
  S166 GapDown strong call (gap <= -3%)
  S163 A1 GapDown ATM call EOD (~7 DTE / P2B 7-DTE arm)
  S173 MomReversal long call — DROPPED 2026-07-20 (no new entries; open lots still exit)
  S174 RubberBand long call EOD — DROPPED permanent (no new entries; excluded from reflected P&L)

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
import time
import csv
import json
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
    active_bucket_count, arms_for_signal,
    build_bucket_leaderboard, build_reflected_leaderboard,
    cancel_dropped_strategy_entries, cancel_unfilled_lab_entries,
    DROPPED_STRATEGIES,
    entry_limit_price, exit_limit_price,
    exit_reason_for_lot, has_open_lab_entry, load_state,
    lock_entry_slot, make_entry_client_order_id,
    make_exit_client_order_id, open_option_sell_symbols,
    print_exit_summary, print_trial_stats, reconcile_summary,
    reconcile_with_broker, register_pending, register_pending_exit,
    save_state, size_for_arm, trial_root,
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
SCAN_LOOKBACK_DAYS  = 260  # need ~200+ bars for MA200 pattern scanners (S170/S172)

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

# Set OPTIONS_BOT_VERBOSE=1 for per-bucket skip/entry lines (default: summary only).
BOT_VERBOSE = os.getenv("OPTIONS_BOT_VERBOSE", "").strip().lower() in (
    "1", "true", "yes",
)

REPO_ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = trial_root() / "runs"
RUNS_CSV = trial_root() / "runs.csv"
RUNS_JSONL = trial_root() / "runs.jsonl"
OCC_RE = re.compile(r"^[A-Z]+\d{6}[CP]\d{8}$")

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("options_morning_bot")
_run_log: list[str] = []
_run_t0: float | None = None
_run_phases: dict[str, float] = {}
W = 72
_BARS_CACHE: dict[str, tuple[pd.DataFrame | None, list[str]]] = {}


def _now_et() -> datetime:
    return datetime.now(ET)


def _hm_ge(now: datetime, hm: tuple[int, int]) -> bool:
    return (now.hour, now.minute) >= hm


def _hm_between(now: datetime, lo: tuple[int, int], hi: tuple[int, int]) -> bool:
    return lo <= (now.hour, now.minute) <= hi


def _in_trading_window(now: datetime) -> bool:
    """9:28–16:05 ET — entries, exits, and manage runs."""
    return _hm_between(now, ENTRY_START, HARD_STOP)


def _after_hours(now: datetime) -> bool:
    return not _in_trading_window(now)


def _parse_hm(hm: str) -> tuple[int, int]:
    try:
        h, m = hm.split(":", 1)
        return int(h), int(m)
    except Exception:
        return ENTRY_START


def _arm_entry_window_open(arm: EffectiveArm, now: datetime) -> bool:
    return _hm_between(now, _parse_hm(arm.buy_start_hm), _parse_hm(arm.buy_end_hm))


def rl(msg: str, *, console: bool = True) -> None:
    """Record a line in the markdown run log; echo to console when console=True."""
    _run_log.append(msg)
    if console:
        print(msg, flush=True)


def rl_file(msg: str) -> None:
    """File-only detail line (included in logs/options_trial/runs/YYYY-MM-DD.md)."""
    rl(msg, console=False)


def section(title: str) -> None:
    """Visual section marker for human-readable run output."""
    rl("")
    rl(f"[{title}]")


def _box_border(ch: str = "=") -> str:
    return "+" + (ch * W) + "+"


def _box_line(msg: str = "") -> str:
    msg = str(msg)
    if len(msg) > W:
        msg = msg[:W]
    return f"|{msg:<{W}}|"


def _box_title(title: str) -> None:
    rl(_box_border("="))
    rl(_box_line(f"  {title}"))
    rl(_box_border("-"))


def _box_end() -> None:
    rl(_box_border("="))


def _console_account_summary(state: LabState, equity: float | None, positions: list[dict],
                             *, mode: str, signals: int, placed: int,
                             rec: dict | None = None) -> None:
    rec = rec or reconcile_summary(state, positions)
    _box_title("OPTIONS BOT SUMMARY")
    rl(_box_line(f"  Mode                          {mode}"))
    if equity is not None:
        rl(_box_line(f"  Equity                        ${equity:,.2f}"))
    rl(_box_line(f"  Signals this run              {signals}"))
    rl(_box_line(f"  Orders submitted (session)    {rec.get('submitted_today', 0)}"))
    rl(_box_line(f"  Orders filled today (ledger)  {rec.get('filled_today', 0)}"))
    rl(_box_line(f"  Entries placed this run       {placed}"))
    rl(_box_line(f"  Open virtual lots             {rec.get('open_lots', 0)}"))
    rl(_box_line(f"  Broker option positions       {rec.get('broker_positions', len(positions))}"))
    unatt = rec.get("unattributed_contracts", 0)
    if unatt:
        rl(_box_line(f"  Unattributed contracts        {unatt} (orphan reconcile)"))
    rl(_box_line(f"  Pending orders                {rec.get('pending_orders', 0)}"))
    _box_end()


def _console_positions_table(positions: list[dict], *, max_rows: int = 8) -> None:
    _box_title(f"OPEN OPTIONS ({len(positions)})")
    if not positions:
        rl(_box_line("  No open option positions"))
        _box_end()
        return
    rl(_box_line("  SYMBOL                      QTY    RET%        OPEN P&L"))
    rl(_box_line("-" * W))
    shown = 0
    for p in sorted(positions, key=lambda x: abs(float(x.get("unrealized_pl", 0) or 0)), reverse=True):
        if shown >= max_rows:
            break
        shown += 1
        sym = str(p.get("symbol", ""))[:25]
        qty = int(p.get("qty", 0) or 0)
        ret = float(p.get("plpc", 0) or 0) * 100.0
        upl = float(p.get("unrealized_pl", 0) or 0)
        rl(_box_line(f"  {sym:25s}  {qty:4d}  {ret:+7.1f}%   ${upl:+10,.2f}"))
    if len(positions) > shown:
        rl(_box_line(f"  ... {len(positions)-shown} more position(s)"))
    _box_end()


def _console_pending_summary(state: LabState, *, max_rows: int = 5) -> None:
    pending = state.pending_orders
    pending_ex = state.pending_exits
    if not pending and not pending_ex:
        return
    if pending:
        from collections import Counter
        groups = Counter(f"{p.strategy_id}:{p.underlying}" for p in pending)
        top = ", ".join(f"{k}({v})" for k, v in groups.most_common(3))
        _box_title(f"PENDING ORDERS ({len(pending)})")
        rl(_box_line(f"  Top groups                    {top}"))
        rl(_box_border("-"))
        for p in pending[:max_rows]:
            sym = p.underlying[:8]
            rl(_box_line(
                f"  b{p.bucket_id:<3d} {p.strategy_id} {sym:8s} limit={p.limit:.2f}"))
        if len(pending) > max_rows:
            rl(_box_line(f"  ... {len(pending) - max_rows} more pending order(s)"))
        _box_end()
    if pending_ex:
        _box_title(f"PENDING EXITS ({len(pending_ex)})")
        for pe in pending_ex[:max_rows]:
            rl(_box_line(
                f"  b{pe.bucket_id:<3d} {pe.strategy_id} {pe.occ_symbol[:22]} "
                f"x{pe.qty} {pe.reason[:20]}"))
        if len(pending_ex) > max_rows:
            rl(_box_line(f"  ... {len(pending_ex) - max_rows} more pending exit(s)"))
        _box_end()


def _console_bucket_leaderboard(state: LabState, *, top_n: int = 8) -> None:
    """Human-readable per-bucket stats — reflected (ex-dropped) is primary."""
    board = build_reflected_leaderboard(state)
    today = TODAY.isoformat()
    today_board = build_reflected_leaderboard(state, day=today)
    raw = build_bucket_leaderboard(state) if DROPPED_STRATEGIES else None

    drop_tag = ",".join(sorted(DROPPED_STRATEGIES)) if DROPPED_STRATEGIES else ""
    title = f"BUCKET LEADERBOARD (reflected ex-{drop_tag})" if drop_tag else "BUCKET LEADERBOARD"
    _box_title(title)
    if board.total_exits == 0:
        rl(_box_line(f"  {board.buckets_defined} buckets defined — no completed trades yet"))
        _box_end()
        return

    rl(_box_line(
        f"  Reflected trades={board.total_exits}  buckets={board.buckets_with_exits}"
        f"  win={board.win_rate_pct:.0f}%"
    ))
    rl(_box_line(
        f"  Returns   avg={board.avg_return_pct:+.1f}%  med={board.med_return_pct:+.1f}%"
        f"  p10={board.p10_return_pct:+.1f}%  p90={board.p90_return_pct:+.1f}%"
    ))
    rl(_box_line(f"  Realized  ${board.total_realized_usd:+,.2f}"))
    if raw is not None and abs(raw.total_realized_usd - board.total_realized_usd) > 0.01:
        rl(_box_line(
            f"  Raw incl dropped  trades={raw.total_exits}  "
            f"real=${raw.total_realized_usd:+,.2f}"
        ))
    if today_board.total_exits:
        rl(_box_line(
            f"  Today     trades={today_board.total_exits}  "
            f"avg={today_board.avg_return_pct:+.1f}%  "
            f"med={today_board.med_return_pct:+.1f}%  "
            f"real=${today_board.total_realized_usd:+,.2f}"
        ))

    rl(_box_border("-"))
    rl(_box_line("  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$"))
    rl(_box_border("-"))
    for row in board.rows[:top_n]:
        prof = row.profile[:18]
        win_pct = 100.0 * row.wins / row.exits if row.exits else 0.0
        rl(_box_line(
            f"  b{row.bucket_id:<3d} {prof:18s} {row.exits:2d} "
            f"{win_pct:3.0f}% {row.avg_return_pct:+5.1f} {row.med_return_pct:+5.1f} "
            f"{row.best_return_pct:+5.1f} ${row.realized_usd:+7.0f}"
        ))
    omitted = len(board.rows) - min(top_n, len(board.rows))
    if omitted > 0:
        rl(_box_line(f"  ... {omitted} more bucket(s) with exits"))
    if len(board.rows) >= 3:
        worst = board.rows[-1]
        wprof = worst.profile[:18]
        wwin = 100.0 * worst.wins / worst.exits if worst.exits else 0.0
        rl(_box_border("-"))
        rl(_box_line(
            f"  Low  b{worst.bucket_id:<3d} {wprof:18s} {worst.exits:2d} "
            f"{wwin:3.0f}% {worst.avg_return_pct:+5.1f} {worst.med_return_pct:+5.1f} "
            f"{worst.worst_return_pct:+5.1f} ${worst.realized_usd:+7.0f}"
        ))
    _box_end()


# --------------------------------------------------------------------------- #
#  Clients
# --------------------------------------------------------------------------- #

def get_paper_account_safe(client, retries=3, wait=10):
    """Retry wrapper for paper Alpaca get_account (mirrors rubber band helper)."""
    for i in range(retries):
        try:
            return client.get_account()
        except Exception as e:
            if i < retries - 1:
                log.warning("paper get_account failed attempt %s/%s: %s", i + 1, retries, e)
                time.sleep(wait)
            else:
                log.error("paper get_account failed after %s attempts: %s", retries, e)
                raise


def get_clients():
    trade = TradingClient(API_KEY, API_SECRET, paper=PAPER_TRADING)
    opt = OptionHistoricalDataClient(API_KEY, API_SECRET)
    stock = StockHistoricalDataClient(API_KEY, API_SECRET)
    ref = make_trading_client(API_KEY, API_SECRET, paper=PAPER_TRADING)
    return trade, opt, stock, ref


def verify_paper_auth(trade) -> bool:
    """Fail fast with a clear log if paper keys are wrong or missing."""
    try:
        acct = get_paper_account_safe(trade)
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
    """Cancel non-LAB option orders. LAB-tagged orders use dedicated cancel paths."""
    n = 0
    try:
        req = GetOrdersRequest(status=QueryOrderStatus.OPEN, limit=200)
        for o in trade.get_orders(req):
            cid = getattr(o, "client_order_id", "") or ""
            if cid.startswith("LB") or cid.startswith("LX"):
                continue
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
        rl(f"Cancelled {n} stale non-LAB option order(s).")
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
    """Scan universe for paper strategy hits.

    CONTROLLED_LAYOUT: emit every matching strategy per symbol so each
    strategy's buckets receive signals. Otherwise keep one hit per symbol
    (highest-priority strategy wins).
    """
    out: list[SignalHit] = []
    start = datetime.now(ET) - timedelta(days=SCAN_LOOKBACK_DAYS)
    df, failed = _fetch_daily_bars_cached(stock, universe, start)
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
    controlled = bool(os.getenv("OPTIONS_CONTROLLED_LAYOUT"))
    for sym in universe:
        try:
            alpaca_sym = to_alpaca_symbol(sym)
            if alpaca_sym not in symbols_in_df:
                continue
            sub = df.xs(alpaca_sym, level=0)
            hits = scan_symbol(sub, sym, TODAY, MIN_UNDERLYING_PX)
            if not hits:
                continue
            if controlled:
                # Controlled layout: emit ALL strategy hits per symbol so every
                # strategy bucket receives signals. arms_for_signal() already
                # routes each hit to its own bucket — no double-buying risk.
                for hit in hits:
                    out.append(hit)
            else:
                # Non-controlled: original behavior, one hit per symbol
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


def _fetch_daily_bars_cached(stock, universe: list[str], start: datetime):
    """Session cache: daily bars keyed by calendar day (ET)."""
    key = TODAY.isoformat()
    if key in _BARS_CACHE:
        rl_file(f"  Daily bars cache hit ({key})")
        return _BARS_CACHE[key]
    result = _fetch_daily_bars(stock, universe, start)
    _BARS_CACHE[key] = result
    return result


def _entries_blocked(state: LabState, signals: list[SignalHit], equity: float,
                     now: datetime, trade) -> bool:
    """True when no bucket can accept a new entry this run."""
    if not signals:
        return True
    for hit in signals:
        strat = _strategy_by_id(hit.strategy_id)
        if not strat:
            continue
        for arm in arms_for_signal(hit.strategy_id, equity):
            if not _arm_entry_window_open(arm, now):
                continue
            if state.bucket_has_strategy(arm.bucket_id, hit.strategy_id):
                continue
            if state.pending_for_bucket_strategy(arm.bucket_id, hit.strategy_id):
                continue
            if state.pending_for_bucket_underlying(arm.bucket_id, hit.symbol):
                continue
            if state.entry_slot_locked(arm.bucket_id, hit.strategy_id):
                continue
            if has_open_lab_entry(trade, arm.bucket_id, hit.strategy_id):
                continue
            if state.bucket_holds_underlying(arm.bucket_id, hit.symbol):
                continue
            return False
    return True


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


def _fetch_option_chain(opt, api_sym: str, exp_lo, exp_hi, strike_lo, strike_hi):
    req = OptionChainRequest(
        underlying_symbol=api_sym,
        expiration_date_gte=exp_lo, expiration_date_lte=exp_hi,
        strike_price_gte=strike_lo, strike_price_lte=strike_hi,
    )
    return opt.get_option_chain(req)


def _fetch_oi_map(ref, api_sym: str, strike_lo, strike_hi, exp_lo, exp_hi):
    return fetch_open_interest(ref, api_sym, strike_gte=strike_lo,
                               strike_lte=strike_hi,
                               exp_gte=exp_lo, exp_lte=exp_hi)


def score_call_for_mode(strike: float, price: float, dte: int, dte_target: int,
                        strike_mode: str = "atm") -> tuple[float, int] | None:
    """Rank key for call selection. Lower is better. None = ineligible.

    atm:  closest to spot, then nearest DTE to target
    otm1: lowest strike strictly above spot, then nearest DTE to target
    """
    if strike_mode == "otm1":
        if strike <= price:
            return None
        return (strike - price, abs(dte - dte_target))
    return (abs(strike - price), abs(dte - dte_target))


def _pick_call_from_chain(opt, ref, symbol: str, price: float,
                          dte_min: int, dte_max: int, dte_target: int,
                          arm: EffectiveArm, *, chain_cache: dict | None = None,
                          oi_cache: dict | None = None,
                          strike_mode: str = "atm"):
    """Return best tradeable call under strike_mode ('atm' or 'otm1')."""
    api_sym = to_alpaca_symbol(symbol)
    max_premium = arm.max_premium
    max_spread = arm.max_spread_frac
    min_oi = arm.min_open_interest
    exp_lo = TODAY + timedelta(days=dte_min)
    exp_hi = TODAY + timedelta(days=dte_max)
    strike_lo = round(price * (1 - STRIKE_PCT), 2)
    strike_hi = round(price * (1 + STRIKE_PCT), 2)
    cache_key = (api_sym, dte_min, dte_max, strike_lo, strike_hi)

    chain = None
    used_cache = False
    if chain_cache is not None and cache_key in chain_cache:
        chain = chain_cache[cache_key]
        used_cache = True

    if chain is None:
        try:
            chain = _fetch_option_chain(opt, api_sym, exp_lo, exp_hi, strike_lo, strike_hi)
            if chain_cache is not None and chain:
                chain_cache[cache_key] = chain
        except Exception as exc:
            rl_file(f"  [{symbol}] chain error: {exc}")
            if chain_cache is not None and cache_key in chain_cache:
                del chain_cache[cache_key]
            try:
                chain = _fetch_option_chain(opt, api_sym, exp_lo, exp_hi, strike_lo, strike_hi)
            except Exception as exc2:
                rl_file(f"  [{symbol}] chain fallback error: {exc2}")
                return None

    # Empty cached chain may be stale — one uncached retry (old behavior).
    if used_cache and not chain:
        try:
            chain = _fetch_option_chain(opt, api_sym, exp_lo, exp_hi, strike_lo, strike_hi)
            if chain_cache is not None and chain:
                chain_cache[cache_key] = chain
        except Exception as exc:
            rl_file(f"  [{symbol}] chain refresh error: {exc}")
            return None

    if not chain:
        return None

    oi_map = {}
    oi_from_cache = False
    if oi_cache is not None and cache_key in oi_cache:
        oi_map = oi_cache[cache_key]
        oi_from_cache = True
    else:
        try:
            oi_map = _fetch_oi_map(ref, api_sym, strike_lo, strike_hi, exp_lo, exp_hi)
            if oi_cache is not None and oi_map:
                oi_cache[cache_key] = oi_map
        except Exception as exc:
            rl_file(f"  [{symbol}] OI error: {exc}")
            try:
                oi_map = _fetch_oi_map(ref, api_sym, strike_lo, strike_hi, exp_lo, exp_hi)
            except Exception:
                oi_map = {}

    if oi_from_cache and not oi_map:
        try:
            fresh_oi = _fetch_oi_map(ref, api_sym, strike_lo, strike_hi, exp_lo, exp_hi)
            if fresh_oi:
                oi_map = fresh_oi
                if oi_cache is not None:
                    oi_cache[cache_key] = oi_map
        except Exception:
            pass

    best = None
    for csym, snap in chain.items():
        expiry, right, strike = _parse_occ(csym, api_sym)
        if right != "C" or strike is None or expiry is None:
            continue
        if strike_mode == "otm1":
            # 1-strike OTM: only calls strictly above spot
            if strike <= price:
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
        score = score_call_for_mode(strike, price, dte, dte_target, strike_mode)
        if score is None:
            continue
        cand = {"symbol": csym, "underlying": symbol, "strike": strike,
                "expiry": expiry, "dte": dte, "bid": bid, "ask": ask, "mid": mid,
                "spread_frac": spread_frac, "cost": cost, "oi": oi, "score": score}
        if best is None or score < best["score"]:
            best = cand
    return best


def pick_atm_call(opt, ref, symbol: str, price: float,
                  dte_min: int, dte_max: int, dte_target: int,
                  arm: EffectiveArm, *, chain_cache: dict | None = None,
                  oi_cache: dict | None = None):
    """Return dict for the best ATM call, or None if nothing tradeable."""
    return _pick_call_from_chain(
        opt, ref, symbol, price, dte_min, dte_max, dte_target, arm,
        chain_cache=chain_cache, oi_cache=oi_cache, strike_mode="atm")


def pick_otm_call_1strike(opt, ref, symbol: str, price: float,
                          dte_min: int, dte_max: int, dte_target: int,
                          arm: EffectiveArm, *, chain_cache: dict | None = None,
                          oi_cache: dict | None = None):
    """Return dict for the lowest call strike strictly above spot (1-OTM)."""
    return _pick_call_from_chain(
        opt, ref, symbol, price, dte_min, dte_max, dte_target, arm,
        chain_cache=chain_cache, oi_cache=oi_cache, strike_mode="otm1")


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
        rl(f"  EXIT {tag} SELL {qty} {sym} @<= {limit:.2f}  id={o.id}", console=False)
        log.info(f"  EXIT {tag} SELL {qty} {sym} @<= {limit:.2f}")
        return str(o.id)
    except Exception as exc:
        rl(f"  EXIT {tag} SELL failed {sym}: {exc}")
        return None


def manage_exits(trade, opt, state: LabState, now: datetime) -> None:
    eod = _hm_ge(now, EOD_SWEEP)
    occ_symbols = {l.occ_symbol for l in state.lots if l.qty > 0}
    pos_by_occ = {getattr(p, "symbol", ""): p for p in option_positions(trade)}
    open_sells = open_option_sell_symbols(trade)

    for occ in occ_symbols:
        if occ in open_sells or state.pending_exit_for_occ(occ):
            rl(f"  EXIT skip {occ}: open sell already pending", console=False)
            continue
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
            if state.pending_exit_for_lot(lot.lot_id):
                continue
            reason = exit_reason_for_lot(lot, plpc, eod)
            if not reason:
                continue
            sell_qty = min(lot.qty, pos_qty)
            if sell_qty <= 0:
                continue
            # Re-check broker open sells (another lot on same OCC may have just submitted).
            if occ in open_sells or state.pending_exit_for_occ(occ):
                rl(f"  EXIT skip {occ}: open sell already pending", console=False)
                break
            ret_pct = plpc * 100.0
            tag = f"[b{lot.bucket_id}|{lot.profile_name}|{lot.strategy_id}] {reason}"
            cid = make_exit_client_order_id(lot.bucket_id, lot.strategy_id, lot.lot_id)

            sell_limit = exit_limit_price(lot, bid or 0.01, bid or 0.01, (bid or 0.01))
            if bid:
                ask_est = bid * 1.02
                sell_limit = exit_limit_price(lot, bid, ask_est, (bid + ask_est) / 2)

            use_market = _hm_ge(now, EOD_MARKET) or (not bid and lot.market_exit_eod)
            # Worthless / no-quote options: Alpaca rejects market sells with
            # "no available quote" — always prefer a $0.01 limit in that case.
            no_quote = (not bid) or float(bid or 0) <= 0.01 or ret_pct <= -99.0
            if no_quote:
                use_market = False
                sell_limit = 0.01

            exit_oid = None
            if use_market:
                try:
                    from alpaca.trading.requests import MarketOrderRequest
                    o = trade.submit_order(MarketOrderRequest(
                        symbol=occ, qty=sell_qty, side=OrderSide.SELL,
                        time_in_force=TimeInForce.DAY,
                        client_order_id=cid[:48]))
                    exit_oid = str(o.id)
                    exit_msg = (
                        f"  EXIT {tag} MARKET SELL {sell_qty} {occ} "
                        f"return={ret_pct:+.1f}%  id={o.id}"
                    )
                    rl_file(exit_msg)
                    rl(f"  EXIT {tag} MARKET SELL {sell_qty} {occ} "
                       f"return={ret_pct:+.1f}%")
                except Exception as exc:
                    # Fallback: limit at $0.01 when market is rejected (no quote).
                    rl_file(f"  EXIT {tag} market failed {occ}: {exc}")
                    exit_oid = _sell_limit(trade, occ, sell_qty, 0.01, tag, cid)
                    if not exit_oid:
                        rl(f"  EXIT {tag} market+limit failed {occ}: {exc}")
                        continue
                    rl(f"  EXIT {tag} LIMIT fallback SELL {sell_qty} {occ} @<= 0.01 "
                       f"return={ret_pct:+.1f}%")
            else:
                exit_oid = _sell_limit(trade, occ, sell_qty, sell_limit, tag, cid)
                if not exit_oid:
                    continue

            # Ledger + lot reduction happen on fill in reconcile — not on submit.
            # Registering early caused double-sells when $0.01 limits sat unfilled.
            register_pending_exit(state, lot, exit_oid, sell_qty, reason)
            open_sells.add(occ)
            pos_qty -= sell_qty
            # One open sell per OCC is enough; further lots wait for fill/reconcile.
            break


# --------------------------------------------------------------------------- #
#  Entries
# --------------------------------------------------------------------------- #

def place_entries(trade, opt, ref, signals: list[SignalHit], state: LabState,
                  now: datetime) -> int:
    try:
        acct = get_paper_account_safe(trade)
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
    skip_no_chain = skip_cap = skip_full = 0
    skip_locked = skip_open = skip_pending = 0
    chain_cache: dict = {}
    oi_cache: dict = {}
    if _entries_blocked(state, signals, equity, now, trade):
        rl("  All bucket slots blocked or closed for today's signals — skip entry loop.")
        return 0
    for hit in signals:
        if placed >= MAX_NEW_ENTRIES_PER_RUN:
            break
        strat = _strategy_by_id(hit.strategy_id)
        if not strat:
            continue
        for arm in arms_for_signal(hit.strategy_id, equity):
            if placed >= MAX_NEW_ENTRIES_PER_RUN:
                break
            if not _arm_entry_window_open(arm, now):
                continue
            if state.bucket_has_strategy(arm.bucket_id, hit.strategy_id):
                continue
            if state.pending_for_bucket_strategy(arm.bucket_id, hit.strategy_id):
                skip_pending += 1
                continue
            if state.pending_for_bucket_underlying(arm.bucket_id, hit.symbol):
                continue
            if state.entry_slot_locked(arm.bucket_id, hit.strategy_id):
                skip_locked += 1
                continue
            if has_open_lab_entry(trade, arm.bucket_id, hit.strategy_id):
                skip_open += 1
                continue
            if state.bucket_holds_underlying(arm.bucket_id, hit.symbol):
                continue
            if hit.strategy_id == "S167":
                cand = pick_otm_call_1strike(
                    opt, ref, hit.symbol, hit.price,
                    strat.dte_min, strat.dte_max, strat.dte_target, arm,
                    chain_cache=chain_cache, oi_cache=oi_cache)
            else:
                cand = pick_atm_call(
                    opt, ref, hit.symbol, hit.price,
                    strat.dte_min, strat.dte_max, strat.dte_target, arm,
                    chain_cache=chain_cache, oi_cache=oi_cache)
            if not cand:
                skip_no_chain += 1
                rl_file(f"  [b{arm.bucket_id}|{arm.profile_name}] {hit.strategy_id} "
                        f"{hit.symbol}: no tradeable call")
                continue
            if real_open + cand["cost"] > real_cap:
                skip_cap += 1
                rl_file(f"  [b{arm.bucket_id}] real account cap (${real_cap:.0f}) — skip")
                continue
            qty = size_for_arm(arm, state, cand["cost"])
            if qty < 1:
                skip_full += 1
                rl_file(f"  [b{arm.bucket_id}|{arm.profile_name}] bucket full "
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
                register_pending(
                    state, arm, cand["symbol"], hit.symbol, qty, limit, str(o.id),
                    detail=hit.detail, spread_frac=cand["spread_frac"])
                lock_entry_slot(state, arm.bucket_id, hit.strategy_id)
                entry_msg = (
                    f"  ENTRY [b{arm.bucket_id}|{arm.profile_name}|{hit.strategy_id}] "
                    f"BUY {qty}x {cand['symbol']} ({hit.detail}) "
                    f"limit={limit:.2f} (ask={cand['ask']:.2f} "
                    f"off={arm.buy_limit_offset:+.2f}) "
                    f"tp={arm.take_profit:+.0%} sl={arm.stop_loss:+.0%} "
                    f"pending id={o.id}"
                )
                rl_file(entry_msg)
                if BOT_VERBOSE:
                    log.info(entry_msg)
            except Exception as exc:
                rl(f"  [b{arm.bucket_id} {hit.symbol}] ENTRY failed: {exc}")
    if skip_no_chain or skip_cap or skip_full or skip_locked or skip_open or skip_pending:
        parts = []
        if skip_no_chain:
            parts.append(f"{skip_no_chain} no tradeable call")
        if skip_cap:
            parts.append(f"{skip_cap} account cap")
        if skip_full:
            parts.append(f"{skip_full} bucket full")
        if skip_locked:
            parts.append(f"{skip_locked} already attempted today")
        if skip_open:
            parts.append(f"{skip_open} open order exists")
        if skip_pending:
            parts.append(f"{skip_pending} pending order")
        rl(f"  Skipped: {', '.join(parts)}")
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
        return float(get_paper_account_safe(trade).equity)
    except Exception:
        return None

def _mark_phase(name: str, t0: float) -> None:
    _run_phases[name] = round(time.perf_counter() - t0, 2)


def _elapsed_total() -> float:
    if _run_t0 is None:
        return 0.0
    return round(time.perf_counter() - _run_t0, 1)


def _format_timing(elapsed_s: float, phases: dict[str, float]) -> str:
    parts = [f"elapsed={elapsed_s}s"]
    for key in ("reconcile", "cancel", "manage", "scan", "entries"):
        if key in phases:
            parts.append(f"{key}={phases[key]}s")
    return " ".join(parts)


def write_run_log(now: datetime, header: str, *,
                  elapsed_s: float | None = None,
                  phases: dict[str, float] | None = None) -> None:
    try:
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        md_path = LOG_DIR / f"{TODAY.isoformat()}.md"
        log_path = LOG_DIR / f"{TODAY.isoformat()}.log"
        new = not md_path.exists()
        with open(md_path, "a", encoding="utf-8") as f:
            if new:
                f.write(f"# Options morning bot (PAPER) — {TODAY.isoformat()}\n\n")
                f.write("_Paper lab: virtual $500 buckets, per-bucket buy/sell experiments._\n\n")
            f.write(f"## {now.strftime('%H:%M:%S')} ET — {header}\n\n")
            if elapsed_s is not None:
                timing = _format_timing(elapsed_s, phases or {})
                f.write(f"_{timing}_\n\n")
            for line in _run_log:
                f.write(f"- {line}\n")
            f.write("\n")
        with open(log_path, "a", encoding="utf-8") as f:
            timing = ""
            if elapsed_s is not None:
                timing = f" [{_format_timing(elapsed_s, phases or {})}]"
            f.write(f"=== {now.strftime('%H:%M:%S')} ET — {header}{timing} ===\n")
            for line in _run_log:
                f.write(f"{line}\n")
            f.write("\n")
    except Exception as exc:
        log.error("Failed to write run log: %s", exc)


RUN_CSV_FIELDS = [
    "timestamp", "date", "mode", "elapsed_s", "signals", "placed", "equity",
    "reconcile_s", "cancel_s", "manage_s", "scan_s", "entries_s",
]


def log_run_csv(now: datetime, mode: str, *,
                elapsed_s: float, signals: int = 0, placed: int = 0,
                equity: float | None = None,
                phases: dict[str, float] | None = None) -> None:
    """Append one row to logs/options_trial/runs.csv (mirrors rubber_band runs.csv)."""
    try:
        trial_root().mkdir(parents=True, exist_ok=True)
        phases = phases or {}
        init = not RUNS_CSV.exists()
        with open(RUNS_CSV, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=RUN_CSV_FIELDS, extrasaction="ignore")
            if init:
                w.writeheader()
            w.writerow({
                "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
                "date": TODAY.isoformat(),
                "mode": mode,
                "elapsed_s": elapsed_s,
                "signals": signals,
                "placed": placed,
                "equity": round(equity, 2) if equity is not None else "",
                "reconcile_s": phases.get("reconcile", ""),
                "cancel_s": phases.get("cancel", ""),
                "manage_s": phases.get("manage", ""),
                "scan_s": phases.get("scan", ""),
                "entries_s": phases.get("entries", ""),
            })
    except Exception as exc:
        log.error("Failed to write runs.csv: %s", exc)


def _finish_run(now: datetime, header: str, mode: str, *,
                signals: int = 0, placed: int = 0,
                equity: float | None = None) -> float:
    """Write logs, CSV row, and return total elapsed seconds."""
    elapsed = _elapsed_total()
    timing = _format_timing(elapsed, _run_phases)
    rl(timing)
    write_run_log(now, header, elapsed_s=elapsed, phases=_run_phases)
    log_run_csv(now, mode, elapsed_s=elapsed, signals=signals, placed=placed,
                equity=equity, phases=_run_phases)
    return elapsed


def log_run_json(now: datetime, mode: str, *, header: str, elapsed_s: float,
                 signals: int, placed: int, equity: float | None,
                 positions: list[dict], state: LabState,
                 top_signals: list[str]) -> None:
    """Append one structured run record for fast review/parsing."""
    try:
        trial_root().mkdir(parents=True, exist_ok=True)
        rec_sum = reconcile_summary(state, positions)
        run_no = os.getenv("GITHUB_RUN_NUMBER", "")
        run_id = os.getenv("GITHUB_RUN_ID", "")
        rec = {
            "ts_et": now.isoformat(),
            "date": TODAY.isoformat(),
            "mode": mode,
            "header": header,
            "elapsed_s": elapsed_s,
            "phases_s": dict(_run_phases),
            "signals": signals,
            "placed": placed,
            "equity": round(equity, 2) if equity is not None else None,
            "open_positions": len(positions),
            "pending_orders": rec_sum.get("pending_orders", 0),
            "open_lots": rec_sum.get("open_lots", 0),
            "submitted_today": rec_sum.get("submitted_today", 0),
            "filled_today": rec_sum.get("filled_today", 0),
            "unattributed_contracts": rec_sum.get("unattributed_contracts", 0),
            "top_signals": top_signals[:12],
            "github_run": run_no,
            "github_run_id": run_id,
            "status": "ok",
        }
        with open(RUNS_JSONL, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, separators=(",", ":")) + "\n")
    except Exception as exc:
        log.error("Failed to write runs.jsonl: %s", exc)


def _status_line(label: str, elapsed: float) -> None:
    run_no = os.getenv("GITHUB_RUN_NUMBER", "")
    repo = os.getenv("GITHUB_REPOSITORY", "")
    run_id = os.getenv("GITHUB_RUN_ID", "")
    extra = ""
    if run_no and repo and run_id:
        extra = f" run=#{run_no} https://github.com/{repo}/actions/runs/{run_id}"
    print(f"STATUS: {label} elapsed={elapsed}s.{extra}", flush=True)


# --------------------------------------------------------------------------- #
#  Orchestration
# --------------------------------------------------------------------------- #

def run() -> int:
    global _run_log, _run_t0, _run_phases
    _run_log = []
    _run_phases = {}
    _run_t0 = time.perf_counter()

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
    section("Run context")

    # Outside trading window — exit summary + stats (no trading)
    if _after_hours(now):
        rl(f"After hours ({now.strftime('%H:%M')} ET) — exit summary only.")
        state = load_state()
        equity = None
        positions = []
        try:
            trade, _, _, _ = get_clients()
            if verify_paper_auth(trade):
                t0 = time.perf_counter()
                equity = _snapshot_equity(trade)
                positions = _position_snapshots(trade)
                state = reconcile_with_broker(trade, state, log_fn=rl_file)
                _mark_phase("reconcile", t0)
        except Exception:
            pass
        section("Exit summary")
        print_exit_summary(state, equity, positions, file_fn=rl_file, console_fn=None, compact=True)
        section("Portfolio snapshot")
        print_trial_stats(state, equity, positions, file_fn=rl_file, console_fn=None, compact=True)
        rec = reconcile_summary(state, positions)
        _console_account_summary(state, equity, positions, mode="after_hours",
                                 signals=0, placed=0, rec=rec)
        _console_bucket_leaderboard(state)
        _console_pending_summary(state)
        _console_positions_table(positions)
        rl(f"Full detail: logs/options_trial/runs/{TODAY.isoformat()}.log")
        elapsed = _finish_run(now, "after hours (exit summary)", "after_hours",
                              equity=equity)
        log_run_json(now, "after_hours", header="after hours (exit summary)",
                     elapsed_s=elapsed, signals=0, placed=0, equity=equity,
                     positions=positions, state=state, top_signals=[])
        _status_line("options_morning_bot after-hours summary (PAPER)", elapsed)
        return 0

    trade, opt, stock, ref = get_clients()

    if not verify_paper_auth(trade):
        state = load_state()
        print_trial_stats(state, None, [], file_fn=rl_file, console_fn=None)
        elapsed = _finish_run(now, "FATAL auth failed (wrong keys?)", "auth_failed")
        log_run_json(now, "auth_failed", header="FATAL auth failed (wrong keys?)",
                     elapsed_s=elapsed, signals=0, placed=0, equity=None,
                     positions=[], state=state, top_signals=[])
        _status_line("options_morning_bot auth failed (PAPER)", elapsed)
        return 1

    equity = _snapshot_equity(trade)
    state = load_state()
    t0 = time.perf_counter()
    state = reconcile_with_broker(trade, state, log_fn=rl_file)
    _mark_phase("reconcile", t0)

    section("Setup")
    rl(f"Active buckets: {active_bucket_count(equity or 0)} | "
       f"Strategies: {', '.join(s.id for s in PAPER_STRATEGIES)}")
    if DROPPED_STRATEGIES:
        rl(f"Dropped (no new entries; ex-reflected P&L): "
           f"{', '.join(sorted(DROPPED_STRATEGIES))}")

    t0 = time.perf_counter()
    cancel_stale_option_orders(trade)
    n_drop = cancel_dropped_strategy_entries(trade, log_fn=rl_file)
    if n_drop:
        rl(f"Cancelled {n_drop} dropped-strategy entry order(s).")
    # Drop pending entry records for paused strategies so slots free up.
    if DROPPED_STRATEGIES and state.pending_orders:
        before = len(state.pending_orders)
        state.pending_orders = [
            p for p in state.pending_orders
            if p.strategy_id not in DROPPED_STRATEGIES
        ]
        cleared = before - len(state.pending_orders)
        if cleared:
            save_state(state)
            rl(f"Cleared {cleared} pending entry slot(s) for dropped strategies.")
    if not _hm_between(now, ENTRY_START, ENTRY_END):
        n_unfilled = cancel_unfilled_lab_entries(trade, log_fn=rl_file)
        if n_unfilled:
            rl(f"Cancelled {n_unfilled} unfilled LAB entry order(s).")
    _mark_phase("cancel", t0)

    t0 = time.perf_counter()
    manage_exits(trade, opt, state, now)
    _mark_phase("manage", t0)

    placed = 0
    signals_n = 0
    top_signals: list[str] = []
    if _hm_between(now, ENTRY_START, ENTRY_END):
        section("Scan + entries")
        universe = get_universe()
        strat_ids = ", ".join(s.id for s in PAPER_STRATEGIES)
        rl(f"Scanning {len(universe)} symbols for [{strat_ids}] …")
        t0 = time.perf_counter()
        signals = scan_all_signals(stock, universe)
        _mark_phase("scan", t0)
        signals_n = len(signals)
        if signals:
            top_signals = [f"{h.strategy_id}:{h.symbol}" for h in signals[:8]]
            rl(f"Found {signals_n} signal(s); top: {top_signals}")
        else:
            rl("Found 0 signals across top-5 strategies")
        t0 = time.perf_counter()
        placed = place_entries(trade, opt, ref, signals, state, now)
        _mark_phase("entries", t0)
        rl(f"Placed {placed} new entry order(s).")
        # Re-reconcile so same-run fills land in ledger/lots before summary.
        if placed or state.pending_orders:
            t0 = time.perf_counter()
            state = reconcile_with_broker(trade, state, log_fn=rl_file)
            _mark_phase("reconcile2", t0)
        header = f"entry+manage ({placed} new)"
        mode = "entry+manage"
    else:
        header = "manage-only (past entry window)"
        section("Manage only")
        rl("Past entry window; manage/exit only.")
        mode = "manage-only"

    positions = _position_snapshots(trade)
    rec = reconcile_summary(state, positions)
    section("Portfolio snapshot")
    print_trial_stats(state, equity, positions, file_fn=rl_file, console_fn=None, compact=True)
    if _hm_ge(now, (16, 0)):
        section("Exit summary")
        print_exit_summary(state, equity, positions, file_fn=rl_file, console_fn=None, compact=True)
    _console_account_summary(state, equity, positions, mode=mode, signals=signals_n,
                             placed=placed, rec=rec)
    _console_bucket_leaderboard(state)
    _console_pending_summary(state)
    _console_positions_table(positions)
    rl(f"Full detail: logs/options_trial/runs/{TODAY.isoformat()}.log")
    elapsed = _finish_run(now, header, mode, signals=signals_n, placed=placed,
                          equity=equity)
    log_run_json(now, mode, header=header, elapsed_s=elapsed, signals=signals_n,
                 placed=placed, equity=equity, positions=positions, state=state,
                 top_signals=top_signals)
    _status_line("options_morning_bot run complete (PAPER)", elapsed)
    return 0


if __name__ == "__main__":
    sys.exit(run())
