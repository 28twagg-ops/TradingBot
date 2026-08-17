# -*- coding: utf-8 -*-
"""
options_live_micro.py -- LIVE options sleeve on the rubber-band brokerage account.

NOT the 1024-bucket paper lab. Caps (the $467-account rules we discussed):
  - 50% of equity reserved for options (LIVE_OPTIONS_SHARE)
  - 1 open contract
  - premium <= 25% of that sleeve (~12.5% of total equity, hard-capped at $60)
  - take-profit +50% / stop-loss -40% + broker-resting protective stop
  - allow-list only (CLEAN KEEP / cheap-premium names)

Uses ALPACA_API_KEY / ALPACA_SECRET_KEY (live). Always exits 0 for GHA.
"""
from __future__ import annotations

import csv
import json
import logging
import os
import re
import sys
import uuid
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, QueryOrderStatus, TimeInForce
from alpaca.trading.requests import (
    GetOrdersRequest,
    LimitOrderRequest,
    MarketOrderRequest,
    StopLimitOrderRequest,
    StopOrderRequest,
)
from alpaca.data.historical import OptionHistoricalDataClient, StockHistoricalDataClient

sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_lab import EffectiveArm  # noqa: E402
from options_oi import make_trading_client  # noqa: E402
from options_signals import PAPER_STRATEGIES  # noqa: E402
from options_universe import get_universe, to_alpaca_symbol  # noqa: E402

import options_morning_bot as om  # noqa: E402

ET = ZoneInfo("America/New_York")
OCC_RE = re.compile(r"^[A-Z]+\d{6}[CP]\d{8}$")

API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_SECRET_KEY")

SHARE = float(os.getenv("LIVE_OPTIONS_SHARE", "0.50"))
MAX_POS = int(os.getenv("LIVE_OPTIONS_MAX_POS", "1"))
PREMIUM_FRAC = float(os.getenv("LIVE_OPTIONS_PREMIUM_FRAC", "0.25"))
MAX_PREMIUM_ABS = float(os.getenv("LIVE_OPTIONS_MAX_PREMIUM", "60"))
TAKE_PROFIT = 0.50
STOP_LOSS = -0.40
ALLOW = [
    s.strip()
    for s in os.getenv(
        "LIVE_OPTIONS_ALLOW",
        "S210,S406,S218,S350,S404,S397",
    ).split(",")
    if s.strip()
]
PRIORITY = {sid: i for i, sid in enumerate(ALLOW)}

ROOT = Path(__file__).resolve().parent.parent / "logs" / "options_live_micro"
STATE_PATH = ROOT / "state.json"
LEDGER_PATH = ROOT / "ledger.csv"
LOG_PATH = ROOT / "runs" / f"{date.today().isoformat()}.log"
LEDGER_FIELDS = [
    "ts", "event", "strategy_id", "occ", "qty", "limit", "cost",
    "reason", "return_pct", "order_id",
]

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("options_live_micro")


def _now() -> datetime:
    return datetime.now(ET)


def _hm(now: datetime) -> tuple[int, int]:
    return now.hour, now.minute


def _ge(now: datetime, hm: tuple[int, int]) -> bool:
    return _hm(now) >= hm


def _between(now: datetime, a, b) -> bool:
    return a <= _hm(now) < b


def rl(msg: str) -> None:
    print(msg, flush=True)
    log.info(msg)
    try:
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(msg + "\n")
    except Exception:
        pass


def load_state() -> dict:
    ROOT.mkdir(parents=True, exist_ok=True)
    if not STATE_PATH.exists():
        return {"lots": []}
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def save_state(state: dict) -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2), encoding="utf-8")


def append_ledger(row: dict) -> None:
    LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)
    hdr = not LEDGER_PATH.exists()
    full = {k: row.get(k, "") for k in LEDGER_FIELDS}
    with open(LEDGER_PATH, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=LEDGER_FIELDS)
        if hdr:
            w.writeheader()
        w.writerow(full)


def _strat(sid: str):
    for s in PAPER_STRATEGIES:
        if s.id == sid:
            return s
    return None


def _allow_strats(skip_0dte: bool) -> list:
    seen: set[str] = set()
    out = []
    for s in PAPER_STRATEGIES:
        if s.id not in PRIORITY or s.id in seen:
            continue
        if skip_0dte and (s.id == "S350" or int(getattr(s, "dte_target", 3) or 3) == 0):
            continue
        seen.add(s.id)
        out.append(s)
    out.sort(key=lambda s: PRIORITY.get(s.id, 99))
    return out


def option_positions(trade) -> list:
    out = []
    try:
        for p in trade.get_all_positions() or []:
            sym = str(getattr(p, "symbol", "") or "")
            ac = str(getattr(p, "asset_class", "") or "")
            if "option" in ac.lower() or OCC_RE.match(sym):
                out.append(p)
    except Exception as exc:
        rl(f"ERROR positions: {exc}")
    return out


def option_mv(trade) -> float:
    total = 0.0
    for p in option_positions(trade):
        try:
            total += abs(float(getattr(p, "market_value", 0) or 0))
        except Exception:
            pass
    return total


def active_lots(state: dict) -> list:
    return [l for l in state.get("lots", []) if int(l.get("qty") or 0) > 0]


def open_count(trade, state: dict) -> int:
    return max(len(option_positions(trade)), len(active_lots(state)))


def make_arm(sid: str, sleeve: float, max_premium: float) -> EffectiveArm | None:
    st = _strat(sid)
    if not st:
        return None
    return EffectiveArm(
        bucket_id=0,
        profile_name="live_micro",
        strategy_id=sid,
        virtual_equity=sleeve,
        max_premium=max_premium,
        max_spread_frac=0.25,
        min_open_interest=50,
        account_cap=1.0,
        max_contracts=1,
        take_profit=TAKE_PROFIT,
        stop_loss=STOP_LOSS,
        option_type=getattr(st, "option_type", "call") or "call",
        strike_offset=int(getattr(st, "strike_offset", 0) or 0),
        dte_target=st.dte_target,
        dte_min=st.dte_min,
        dte_max=st.dte_max,
    )


def cid_entry() -> str:
    return f"OLB|{date.today().strftime('%Y%m%d')}|{uuid.uuid4().hex[:8]}"[:48]


def cid_exit() -> str:
    return f"OLX|{uuid.uuid4().hex[:12]}"[:48]


def cid_stop() -> str:
    return f"OLS|{uuid.uuid4().hex[:12]}"[:48]


def reconcile(trade, state: dict, now: datetime) -> dict:
    pos = {str(getattr(p, "symbol", "")): p for p in option_positions(trade)}
    kept = []
    for lot in active_lots(state):
        occ = lot.get("occ")
        if occ in pos:
            kept.append(lot)
            continue
        pending = False
        try:
            req = GetOrdersRequest(status=QueryOrderStatus.OPEN, symbols=[occ], limit=20)
            for o in trade.get_orders(req) or []:
                cid = getattr(o, "client_order_id", "") or ""
                if cid.startswith("OLB") and o.side == OrderSide.BUY:
                    pending = True
                    break
        except Exception:
            pending = True
        if pending:
            kept.append(lot)
        else:
            rl(f"Live micro reconcile: drop {occ} {lot.get('strategy_id')} (not at broker)")
            append_ledger({
                "ts": now.isoformat(), "event": "reconcile_drop",
                "strategy_id": lot.get("strategy_id"), "occ": occ,
                "qty": lot.get("qty"), "reason": "missing_from_broker",
            })
    state["lots"] = kept
    save_state(state)
    return state


def _cancel_protective(trade, occ: str) -> None:
    try:
        req = GetOrdersRequest(status=QueryOrderStatus.OPEN, symbols=[occ], limit=50)
        for o in trade.get_orders(req) or []:
            cid = getattr(o, "client_order_id", "") or ""
            if cid.startswith("OLS"):
                try:
                    trade.cancel_order_by_id(o.id)
                except Exception:
                    pass
    except Exception:
        pass


def manage(trade, state: dict, now: datetime) -> None:
    eod = _ge(now, om.EOD_SWEEP)
    pos = {str(getattr(p, "symbol", "")): p for p in option_positions(trade)}
    for lot in active_lots(state):
        occ = lot.get("occ")
        p = pos.get(occ)
        if not p:
            continue
        try:
            plpc = float(getattr(p, "unrealized_plpc", 0) or 0)
            qty = int(float(getattr(p, "qty", 0) or 0))
        except Exception:
            continue
        if qty <= 0:
            continue
        tp = float(lot.get("take_profit") or TAKE_PROFIT)
        sl = float(lot.get("stop_loss") or STOP_LOSS)
        reason = None
        if plpc <= sl:
            reason = f"stop_loss ({plpc:+.1%})"
        elif plpc >= tp:
            reason = f"take_profit ({plpc:+.1%})"
        elif eod:
            reason = "EOD"
        if not reason:
            continue
        _cancel_protective(trade, occ)
        try:
            o = trade.submit_order(MarketOrderRequest(
                symbol=occ, qty=min(qty, int(lot["qty"])),
                side=OrderSide.SELL, time_in_force=TimeInForce.DAY,
                client_order_id=cid_exit(),
            ))
            rl(f"LIVE EXIT {reason} {occ} x{qty} id={o.id}")
            lot["qty"] = 0
            append_ledger({
                "ts": now.isoformat(), "event": "exit",
                "strategy_id": lot.get("strategy_id"), "occ": occ, "qty": qty,
                "reason": reason, "return_pct": round(plpc * 100, 2),
                "order_id": str(o.id),
            })
        except Exception as exc:
            rl(f"LIVE EXIT failed {occ}: {exc}")
    state["lots"] = active_lots(state)
    save_state(state)


def ensure_stops(trade, state: dict) -> None:
    pos = {str(getattr(p, "symbol", "")): p for p in option_positions(trade)}
    for lot in active_lots(state):
        occ = lot.get("occ")
        if not occ or occ not in pos:
            continue
        try:
            req = GetOrdersRequest(status=QueryOrderStatus.OPEN, symbols=[occ], limit=20)
            have = False
            for o in trade.get_orders(req) or []:
                cid = getattr(o, "client_order_id", "") or ""
                if cid.startswith("OLS"):
                    have = True
                    break
            if have:
                continue
        except Exception:
            continue
        entry = float(lot.get("entry_price") or 0) or float(
            getattr(pos[occ], "avg_entry_price", 0) or 0
        )
        sl = float(lot.get("stop_loss") or STOP_LOSS)
        if entry <= 0 or sl >= 0:
            continue
        stop_px = round(max(0.01, entry * (1.0 + sl)), 2)
        lim = round(max(0.01, stop_px * 0.92), 2)
        qty = int(lot["qty"])
        try:
            o = trade.submit_order(StopLimitOrderRequest(
                symbol=occ, qty=qty, side=OrderSide.SELL,
                time_in_force=TimeInForce.GTC,
                stop_price=stop_px, limit_price=lim,
                client_order_id=cid_stop(),
            ))
            rl(f"LIVE PROT STOP {occ} x{qty} stop={stop_px:.2f} id={o.id}")
        except Exception as exc:
            try:
                o = trade.submit_order(StopOrderRequest(
                    symbol=occ, qty=qty, side=OrderSide.SELL,
                    time_in_force=TimeInForce.DAY, stop_price=stop_px,
                    client_order_id=cid_stop(),
                ))
                rl(f"LIVE PROT STOP-MKT {occ} x{qty} stop={stop_px:.2f} id={o.id}")
            except Exception as exc2:
                rl(f"LIVE PROT STOP failed {occ}: {exc2 or exc}")


def scan_hits(stock, skip_0dte: bool) -> list:
    strats = _allow_strats(skip_0dte)
    if not strats:
        return []
    universe = get_universe()
    start = datetime.now(ET) - timedelta(days=om.SCAN_LOOKBACK_DAYS)
    df, failed = om._fetch_daily_bars_cached(stock, universe, start)
    if df is None or df.empty:
        rl("No daily bars for live micro scan")
        return []
    symbols_in = set(df.index.get_level_values(0))
    hits = []
    today = date.today()
    for sym in universe:
        try:
            alp = to_alpaca_symbol(sym)
            if alp not in symbols_in:
                continue
            sub = df.xs(alp, level=0)
            for st in strats:
                try:
                    hit = st.scanner(sub, sym, today, om.MIN_UNDERLYING_PX)
                except Exception:
                    continue
                if hit:
                    hits.append(hit)
        except Exception:
            continue
    hits.sort(key=lambda h: PRIORITY.get(h.strategy_id, 99))
    return hits


def place(trade, opt, ref, stock, equity: float, cash: float, state: dict,
          now: datetime, skip_0dte: bool) -> int:
    if not _between(now, om.ENTRY_START, om.ENTRY_END):
        rl("Live micro: outside entry window")
        return 0
    if open_count(trade, state) >= MAX_POS:
        rl(f"Live micro: already at max {MAX_POS} option position")
        return 0
    sleeve = max(0.0, equity * SHARE)
    deployed = option_mv(trade)
    room = min(max(0.0, cash - equity * 0.05), max(0.0, sleeve - deployed))
    max_prem = min(MAX_PREMIUM_ABS, sleeve * PREMIUM_FRAC, room)
    if max_prem < 15:
        rl(f"Live micro: premium room ${max_prem:.0f} too small -- skip entries")
        return 0
    allow = [s.id for s in _allow_strats(skip_0dte)]
    rl(
        f"Live micro sleeve ${sleeve:.0f} ({SHARE:.0%} of ${equity:.0f}) "
        f"deployed ${deployed:.0f} max_prem ${max_prem:.0f} "
        f"tp={TAKE_PROFIT:+.0%} sl={STOP_LOSS:+.0%} allow={','.join(allow)}"
    )
    if skip_0dte:
        rl("Live micro: skipping 0DTE (S350) -- equity under $25k PDT")
    hits = scan_hits(stock, skip_0dte)
    rl(f"Live micro signals: {len(hits)}")
    placed = 0
    chain_cache: dict = {}
    oi_cache: dict = {}
    for hit in hits:
        if placed or open_count(trade, state) >= MAX_POS:
            break
        arm = make_arm(hit.strategy_id, sleeve, max_prem)
        if not arm:
            continue
        st = _strat(hit.strategy_id)
        cand = om._pick_option_from_chain(
            opt, ref, hit.symbol, hit.price,
            st.dte_min, st.dte_max, st.dte_target, arm,
            chain_cache=chain_cache, oi_cache=oi_cache,
        )
        if not cand:
            rl(f"  skip {hit.strategy_id} {hit.symbol}: no contract under ${max_prem:.0f}")
            continue
        if cand["cost"] > max_prem + 0.01:
            continue
        try:
            o = trade.submit_order(LimitOrderRequest(
                symbol=cand["symbol"], qty=1, side=OrderSide.BUY,
                time_in_force=TimeInForce.DAY,
                limit_price=round(float(cand["ask"]), 2),
                client_order_id=cid_entry(),
            ))
            lot = {
                "lot_id": uuid.uuid4().hex[:12],
                "strategy_id": hit.strategy_id,
                "occ": cand["symbol"],
                "underlying": hit.symbol,
                "qty": 1,
                "entry_price": float(cand["ask"]),
                "take_profit": TAKE_PROFIT,
                "stop_loss": STOP_LOSS,
                "order_id": str(o.id),
            }
            state.setdefault("lots", []).append(lot)
            save_state(state)
            append_ledger({
                "ts": now.isoformat(), "event": "entry",
                "strategy_id": hit.strategy_id, "occ": cand["symbol"],
                "qty": 1, "limit": cand["ask"], "cost": cand["cost"],
                "order_id": str(o.id), "reason": hit.detail,
            })
            rl(
                f"LIVE BUY {hit.strategy_id} {hit.symbol} {cand['symbol']} "
                f"ask={cand['ask']:.2f} cost=${cand['cost']:.0f} id={o.id}"
            )
            placed = 1
        except Exception as exc:
            rl(f"LIVE BUY failed {hit.strategy_id} {hit.symbol}: {exc}")
            break
    return placed


def run() -> int:
    if not API_KEY or not API_SECRET:
        rl("ERROR: ALPACA_API_KEY / ALPACA_SECRET_KEY required for live micro")
        return 0
    now = _now()
    rl(f"=== options_live_micro LIVE {now.isoformat()} share={SHARE:.0%} ===")
    if now.weekday() >= 5:
        rl("Weekend -- skip")
        return 0

    trade = TradingClient(API_KEY, API_SECRET, paper=False)
    opt = OptionHistoricalDataClient(API_KEY, API_SECRET)
    stock = StockHistoricalDataClient(API_KEY, API_SECRET)
    ref = make_trading_client(API_KEY, API_SECRET, paper=False)
    try:
        acct = trade.get_account()
        equity = float(acct.equity)
        cash = float(acct.cash)
        rl(f"Live account equity ${equity:.2f} cash ${cash:.2f} "
           f"#{getattr(acct, 'account_number', '?')}")
    except Exception as exc:
        rl(f"FATAL live get_account: {exc}")
        return 0

    state = load_state()
    state = reconcile(trade, state, now)

    in_session = _between(now, om.ENTRY_START, om.HARD_STOP)
    if not in_session:
        if _ge(now, om.HARD_STOP):
            manage(trade, state, now)
        else:
            rl("Live micro: outside 9:28-16:05 ET")
        n = len(option_positions(trade))
        rl(f"Live micro done. open_options={n} lots={len(active_lots(state))}")
        return 0

    manage(trade, state, now)
    ensure_stops(trade, state)
    if _between(now, om.ENTRY_START, om.ENTRY_END):
        allow_0dte = os.getenv("LIVE_OPTIONS_ALLOW_0DTE", "").strip().lower() in (
            "1", "true", "yes",
        )
        skip_0dte = (equity < 25000) and not allow_0dte
        place(trade, opt, ref, stock, equity, cash, state, now, skip_0dte)
        ensure_stops(trade, state)
    else:
        rl("Live micro: manage/exits only")
    n = len(option_positions(trade))
    rl(f"Live micro done. open_options={n} lots={len(active_lots(state))}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(run())
    except Exception as e:
        print(f"options_live_micro failed (non-fatal): {e}")
        raise SystemExit(0)
