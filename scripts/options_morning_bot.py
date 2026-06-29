"""
options_morning_bot.py — Phase 4 Task 4.1 (PAPER mode) + Task 4.3 sizing.

A standalone morning options bot that trades the PRELIMINARY Verdict-B finding
from the correlation study:

    The equity bot's dip/gap-down signals predict SAME-DAY option moves, and
    the edge is strongest on STRONG signals. So: on a strong gap-down
    (gap_pct < -2%), buy an ATM CALL (bounce thesis) and CLOSE SAME DAY.

This runs SEPARATELY from rubber_band_bot.py and NEVER touches it. It uses the
Alpaca PAPER account/endpoint. It does not affect the live equity bot.

IMPORTANT STATUS LABELS
  - PAPER ONLY. PAPER_TRADING is hard-locked True; the bot refuses to run live.
  - The strategy is the PRELIMINARY Verdict-B heuristic, NOT a Phase-3-validated
    variant (no real 1-min data exists yet). Treat results as plumbing/early
    validation, not proven edge.

What each cron run does (entry window 9:28-11:35 ET):
  1. Cancel any still-open option orders from the prior run (Option-1 fill: one
     window then cancel).
  2. Manage exits on open option positions: +50% / -50% of premium -> close.
  3. Scan the universe for strong gap-downs (gap_pct < GAP_THRESHOLD).
  4. For each new signal: pick ATM call, apply liquidity + Tier-0 sizing, place
     a BUY limit at ask-$0.01.
EOD (>= 15:30 ET): close ALL open option positions (limit at bid; market at 15:50).

Tier 0 sizing (Task 4.3, hard caps): 1 contract, <= $75 premium, <= 20% of
account equity in options premium.

Run (paper keys required — NOT the live equity-bot keys):
    ALPACA_PAPER_API_KEY=... ALPACA_PAPER_SECRET_KEY=... python scripts/options_morning_bot.py
"""

from __future__ import annotations

import logging
import os
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import LimitOrderRequest, GetOrdersRequest
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
from alpaca.data.historical import OptionHistoricalDataClient, StockHistoricalDataClient
from alpaca.data.requests import OptionChainRequest, StockBarsRequest
from alpaca.data.timeframe import TimeFrame

sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_universe import get_universe
from options_oi import make_trading_client, fetch_open_interest

# --------------------------------------------------------------------------- #
#  HARD SAFETY LOCK
# --------------------------------------------------------------------------- #
PAPER_TRADING = True   # DO NOT flip to False here. Going live = Phase 5, with
                       # shared-account coordination (Task 5.2) implemented first.

# --------------------------------------------------------------------------- #
#  Strategy / risk config (Verdict-B preliminary + Tier 0)
# --------------------------------------------------------------------------- #
GAP_THRESHOLD       = -0.02     # strong gap-down: (open - prior_close)/prior_close
RIGHT               = "C"       # bullish bounce thesis -> CALL
DTE_MIN, DTE_MAX    = 2, 10     # short-dated (Verdict B); target ~7
DTE_TARGET          = 7
STRIKE_PCT          = 0.10      # search strikes within +/-10% of price

MIN_OPEN_INTEREST   = 100
MAX_SPREAD_FRAC     = 0.25
TIER0_MAX_CONTRACTS = 1
TIER0_MAX_PREMIUM   = 75.0      # per-contract premium cap ($)
TIER0_ACCOUNT_CAP   = 0.20      # <= 20% of equity in options premium
MIN_UNDERLYING_PX   = 3.0       # ignore sub-$3 names

TAKE_PROFIT_PCT     = 0.50
STOP_LOSS_PCT       = -0.50
MAX_NEW_ENTRIES_PER_RUN = 2     # safety throttle

# Time windows (ET)
ENTRY_START = (9, 28)
ENTRY_END   = (11, 35)
EOD_SWEEP   = (15, 30)
EOD_MARKET  = (15, 50)
HARD_STOP   = (16, 5)

ET = ZoneInfo("America/New_York")
TODAY = date.today()

# Paper credentials ONLY — do not use live ALPACA_API_KEY (equity bot keys).
# GitHub Actions: secrets ALPACA_PAPER_API_KEY / ALPACA_PAPER_SECRET_KEY
API_KEY = os.getenv("ALPACA_PAPER_API_KEY")
API_SECRET = os.getenv("ALPACA_PAPER_SECRET_KEY")

REPO_ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = REPO_ROOT / "logs" / "options"
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
        rl("FATAL: paper API auth failed. This bot requires ALPACA_PAPER_API_KEY and "
           "ALPACA_PAPER_SECRET_KEY (not the live equity-bot keys). "
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
#  Signal scan (strong gap-downs)
# --------------------------------------------------------------------------- #

def scan_gap_downs(stock, universe: list[str]) -> list[tuple[str, float, float]]:
    """Return [(symbol, gap_pct, today_open)] for strong gap-downs today."""
    out: list[tuple[str, float, float]] = []
    try:
        req = StockBarsRequest(
            symbol_or_symbols=universe, timeframe=TimeFrame.Day,
            start=datetime.now(ET) - timedelta(days=7),
        )
        df = stock.get_stock_bars(req).df
    except Exception as exc:
        rl(f"ERROR fetching daily bars for scan: {exc}")
        return out
    if df is None or df.empty:
        return out

    today_str = TODAY.isoformat()
    for sym in universe:
        try:
            if sym not in df.index.get_level_values(0):
                continue
            sub = df.xs(sym, level=0)
            if len(sub) < 2:
                continue
            last_ts = sub.index[-1]
            # only act on a bar dated today (market open established)
            if str(last_ts.date()) != today_str:
                continue
            prior_close = float(sub["close"].iloc[-2])
            today_open = float(sub["open"].iloc[-1])
            if prior_close <= 0 or today_open < MIN_UNDERLYING_PX:
                continue
            gap = (today_open - prior_close) / prior_close
            if gap <= GAP_THRESHOLD:
                out.append((sym, gap, today_open))
        except Exception:
            continue
    out.sort(key=lambda x: x[1])   # most negative gap first
    return out


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


def pick_atm_call(opt, ref, symbol: str, price: float):
    """Return dict for the best ATM call, or None if nothing tradeable."""
    exp_lo = TODAY + timedelta(days=DTE_MIN)
    exp_hi = TODAY + timedelta(days=DTE_MAX)
    strike_lo = round(price * (1 - STRIKE_PCT), 2)
    strike_hi = round(price * (1 + STRIKE_PCT), 2)
    try:
        req = OptionChainRequest(
            underlying_symbol=symbol,
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
        oi_map = fetch_open_interest(ref, symbol, strike_gte=strike_lo,
                                    strike_lte=strike_hi,
                                    exp_gte=exp_lo, exp_lte=exp_hi)
    except Exception:
        oi_map = {}

    best = None
    for csym, snap in chain.items():
        expiry, right, strike = _parse_occ(csym, symbol)
        if right != "C" or strike is None or expiry is None:
            continue
        lq = getattr(snap, "latest_quote", None)
        bid = getattr(lq, "bid_price", None) if lq else None
        ask = getattr(lq, "ask_price", None) if lq else None
        if not bid or not ask or bid <= 0 or ask <= 0:
            continue
        mid = (bid + ask) / 2
        spread_frac = (ask - bid) / mid if mid > 0 else 9.9
        if spread_frac > MAX_SPREAD_FRAC:
            continue
        cost = ask * 100
        if cost > TIER0_MAX_PREMIUM:
            continue
        oi = (oi_map.get(csym) or {}).get("open_interest")
        if oi is not None and oi < MIN_OPEN_INTEREST:
            continue
        try:
            dte = (date.fromisoformat(expiry) - TODAY).days
        except Exception:
            continue
        moneyness = abs(strike - price)
        # rank: closest to ATM, then closest DTE to target
        score = (moneyness, abs(dte - DTE_TARGET))
        cand = {"symbol": csym, "underlying": symbol, "strike": strike,
                "expiry": expiry, "dte": dte, "bid": bid, "ask": ask, "mid": mid,
                "spread_frac": spread_frac, "cost": cost, "oi": oi, "score": score}
        if best is None or score < best["score"]:
            best = cand
    return best


# --------------------------------------------------------------------------- #
#  Sizing (Tier 0, Task 4.3)
# --------------------------------------------------------------------------- #

def size_contracts(equity: float, open_premium: float, contract_cost: float) -> int:
    cap = TIER0_ACCOUNT_CAP * equity
    headroom = cap - open_premium
    if contract_cost <= 0:
        return 0
    affordable = int(headroom // contract_cost)
    return max(0, min(TIER0_MAX_CONTRACTS, affordable))


# --------------------------------------------------------------------------- #
#  Exits
# --------------------------------------------------------------------------- #

def _sell_limit(trade, sym: str, qty: int, limit: float, tag: str):
    try:
        o = trade.submit_order(LimitOrderRequest(
            symbol=sym, qty=qty, side=OrderSide.SELL,
            time_in_force=TimeInForce.DAY, limit_price=round(max(0.01, limit), 2)))
        rl(f"  EXIT {tag} SELL {qty} {sym} @<= {limit:.2f}  id={o.id}")
    except Exception as exc:
        rl(f"  EXIT {tag} SELL failed {sym}: {exc}")


def manage_exits(trade, opt, now: datetime) -> None:
    eod = _hm_ge(now, EOD_SWEEP)
    for p in option_positions(trade):
        sym = getattr(p, "symbol", "")
        try:
            qty = int(float(getattr(p, "qty", 0)))
        except Exception:
            qty = 0
        if qty <= 0:
            continue
        try:
            plpc = float(getattr(p, "unrealized_plpc", 0) or 0.0)
        except Exception:
            plpc = 0.0
        # current bid for limit price
        bid = None
        try:
            m = re.match(r"^[A-Z]+", sym)
            underlying = m.group(0) if m else None
            if underlying:
                ch = opt.get_option_chain(OptionChainRequest(underlying_symbol=underlying))
                snap = ch.get(sym) if ch else None
                lq = getattr(snap, "latest_quote", None) if snap else None
                bid = getattr(lq, "bid_price", None) if lq else None
        except Exception:
            bid = None

        reason = None
        if eod:
            reason = "EOD"
        elif plpc >= TAKE_PROFIT_PCT:
            reason = f"take_profit ({plpc:+.0%})"
        elif plpc <= STOP_LOSS_PCT:
            reason = f"stop_loss ({plpc:+.0%})"
        if not reason:
            continue

        if _hm_ge(now, EOD_MARKET) or not bid:
            # last-resort market exit (only allowed exit-side market order)
            try:
                from alpaca.trading.requests import MarketOrderRequest
                o = trade.submit_order(MarketOrderRequest(
                    symbol=sym, qty=qty, side=OrderSide.SELL,
                    time_in_force=TimeInForce.DAY))
                rl(f"  EXIT {reason} MARKET SELL {qty} {sym}  id={o.id}")
            except Exception as exc:
                rl(f"  EXIT {reason} market failed {sym}: {exc}")
        else:
            _sell_limit(trade, sym, qty, bid - 0.01, reason)


# --------------------------------------------------------------------------- #
#  Entries
# --------------------------------------------------------------------------- #

def place_entries(trade, opt, ref, signals, now: datetime) -> int:
    try:
        acct = trade.get_account()
        equity = float(acct.equity)
    except Exception as exc:
        rl(f"ERROR reading account: {exc}")
        return 0

    held_underlyings = set()
    for p in option_positions(trade):
        m = re.match(r"^[A-Z]+", getattr(p, "symbol", ""))
        if m:
            held_underlyings.add(m.group(0))

    placed = 0
    for sym, gap, price in signals:
        if placed >= MAX_NEW_ENTRIES_PER_RUN:
            break
        if sym in held_underlyings:
            rl(f"  [{sym}] skip: already hold an option on it")
            continue
        cand = pick_atm_call(opt, ref, sym, price)
        if not cand:
            rl(f"  [{sym}] gap {gap:+.1%}: no tradeable ATM call (liquidity/cost)")
            continue
        open_prem = open_option_premium(trade)
        qty = size_contracts(equity, open_prem, cand["cost"])
        if qty < 1:
            rl(f"  [{sym}] at options cap (equity ${equity:.0f}, open ${open_prem:.0f}) "
               f"- skip")
            continue
        limit = round(cand["ask"] - 0.01, 2)
        try:
            o = trade.submit_order(LimitOrderRequest(
                symbol=cand["symbol"], qty=qty, side=OrderSide.BUY,
                time_in_force=TimeInForce.DAY, limit_price=limit))
            placed += 1
            rl(f"  ENTRY BUY {qty}x {cand['symbol']} (gap {gap:+.1%}, ATM "
               f"{cand['strike']} {cand['expiry']} {cand['dte']}DTE) @<= {limit:.2f} "
               f"cost~${cand['cost']:.0f} id={o.id}")
        except Exception as exc:
            rl(f"  [{sym}] ENTRY failed: {exc}")
    return placed


# --------------------------------------------------------------------------- #
#  Logging to logs/options/<date>.md
# --------------------------------------------------------------------------- #

def write_run_log(now: datetime, header: str) -> None:
    try:
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        path = LOG_DIR / f"{TODAY.isoformat()}.md"
        new = not path.exists()
        with open(path, "a", encoding="utf-8") as f:
            if new:
                f.write(f"# Options morning bot (PAPER) — {TODAY.isoformat()}\n\n")
                f.write("_PRELIMINARY Verdict-B strategy. PAPER account. "
                        "Not a validated edge._\n\n")
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
    if not PAPER_TRADING:
        print("REFUSING TO RUN: PAPER_TRADING is False. This bot is paper-only "
              "until Phase 5 (live integration + shared-account coordination).")
        return 2
    if not API_KEY or not API_SECRET:
        print("ERROR: set ALPACA_PAPER_API_KEY and ALPACA_PAPER_SECRET_KEY "
              "(paper account keys — not the live equity-bot keys).")
        return 1

    now = _now_et()
    rl(f"=== options_morning_bot (PAPER) {now.isoformat()} ===")

    # Outside the trading day entirely -> nothing to do.
    if not _hm_between(now, ENTRY_START, HARD_STOP):
        rl(f"Outside trading window ({now.strftime('%H:%M')} ET). Exiting.")
        write_run_log(now, "idle (outside window)")
        return 0

    trade, opt, stock, ref = get_clients()

    if not verify_paper_auth(trade):
        write_run_log(now, "FATAL auth failed (wrong keys?)")
        return 1

    # 1. cancel stale orders (Option-1 fill)
    cancel_stale_option_orders(trade)

    # 2. manage exits (always; EOD sweep handled inside)
    manage_exits(trade, opt, now)

    # 3+4. entries only within the entry window
    if _hm_between(now, ENTRY_START, ENTRY_END):
        universe = get_universe()
        rl(f"Scanning {len(universe)} symbols for gap-downs <= {GAP_THRESHOLD:.0%} …")
        signals = scan_gap_downs(stock, universe)
        rl(f"Found {len(signals)} strong gap-down signal(s)"
           + (f"; top: {[ (s,round(g,3)) for s,g,_ in signals[:5] ]}" if signals else ""))
        placed = place_entries(trade, opt, ref, signals, now)
        rl(f"Placed {placed} new entry order(s).")
        header = f"entry+manage ({placed} new)"
    else:
        header = "manage-only (past entry window)"
        rl("Past entry window; manage/exit only.")

    write_run_log(now, header)
    print("STATUS: options_morning_bot run complete (PAPER).")
    return 0


if __name__ == "__main__":
    sys.exit(run())
