# -*- coding: utf-8 -*-
"""
options_live_micro.py -- LIVE options sleeve on the rubber-band brokerage account.

NOT the 1024-bucket paper lab. Live-specific caps only:
  - LIVE_OPTIONS_SHARE of equity reserved for options (default 25%)
  - allow-list of paper KEEP names, ranked by CLEAN win rate
  - one strategy per signal family (only one GapDown: S404, not S397/S350 too)
  - LIVE_OPTIONS_ENTRIES=0 pauses new buys (manage/orphan adopt still run)

Trade mechanics = paper baseline bucket 0 (options_lab.py):
  1 contract per allow-list strategy (same as paper max_contracts per bucket),
  buy ask-0.01, max_premium $75, min cost $20, account_cap 95%, OI>=100, spread<=25%,
  TP +50% / SL -40%, EOD 15:30, market exit 15:50, broker-resting protective stop-market.

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
from alpaca.data.requests import OptionChainRequest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_lab import EffectiveArm, entry_limit_price, _merge_arm, BUCKET_EXPERIMENTS, VIRTUAL_BUCKET_USD  # noqa: E402
from options_oi import make_trading_client  # noqa: E402
from options_signals import PAPER_STRATEGIES  # noqa: E402
from options_universe import get_universe, to_alpaca_symbol  # noqa: E402

import options_morning_bot as om  # noqa: E402

ET = ZoneInfo("America/New_York")
OCC_RE = re.compile(r"^[A-Z]+\d{6}[CP]\d{8}$")

API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_SECRET_KEY")

SHARE = float(os.getenv("LIVE_OPTIONS_SHARE", "0.25"))
# 0/false = manage + orphan adopt only (no new buys).
ENTRIES_ENABLED = os.getenv("LIVE_OPTIONS_ENTRIES", "1").strip().lower() not in (
    "0", "false", "no", "off",
)
# Skip lottery-ticket premiums (cost = premium * 100).
MIN_ENTRY_COST = float(os.getenv("LIVE_OPTIONS_MIN_COST", "20"))
# Paper baseline bucket 0 — do not override these with live-only values.
PAPER_BASELINE = BUCKET_EXPERIMENTS[0]
PAPER_MAX_PREMIUM = float(PAPER_BASELINE.max_premium)
TAKE_PROFIT = float(PAPER_BASELINE.take_profit)
STOP_LOSS = float(PAPER_BASELINE.stop_loss)
BUY_LIMIT_OFFSET = float(PAPER_BASELINE.buy_limit_offset)
SELL_LIMIT_OFFSET = float(PAPER_BASELINE.sell_limit_offset)
MIN_OPEN_INTEREST = int(PAPER_BASELINE.min_open_interest)
MAX_SPREAD_FRAC = float(PAPER_BASELINE.max_spread_frac)
# Membership list. Trade order is CLEAN win rate (then median), not this string order.
# Default drops S210 (full-sample paper median non-positive).
ALLOW = [
    s.strip()
    for s in os.getenv(
        "LIVE_OPTIONS_ALLOW",
        "S404,S406,S218",
    ).split(",")
    if s.strip()
]
# CLEAN 2026-08-17: (win%, median%). Live always tries higher win first.
CLEAN_RANK = {
    "S404": (100.0, 80.1),
    "S397": (100.0, 71.8),
    "S406": (56.2, 58.3),
    "S218": (55.6, 48.9),
    "S210": (55.0, 46.6),
    "S350": (53.8, 53.3),
}
SIGNAL_FAMILY = {
    "S404": "gapdown", "S397": "gapdown", "S350": "gapdown",
    "S398": "gapdown", "S165": "gapdown",
    "S406": "rubberband", "S174": "rubberband",
    "S218": "bb",
    "S210": "ma",
}

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


def _win_key(sid: str) -> tuple:
    win, med = CLEAN_RANK.get(sid, (0.0, -999.0))
    return (-win, -med, sid)


def _strat(sid: str):
    for s in PAPER_STRATEGIES:
        if s.id == sid:
            return s
    return None


def _allow_strats() -> list:
    seen: set[str] = set()
    out = []
    allow = set(ALLOW)
    for s in PAPER_STRATEGIES:
        if s.id not in allow or s.id in seen:
            continue
        seen.add(s.id)
        out.append(s)
    out.sort(key=lambda s: _win_key(s.id))
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


def _today_iso() -> str:
    return date.today().isoformat()


def used_strategies_today(state: dict) -> set[str]:
    """One live attempt per allow-list strategy per day (paper max_contracts=1)."""
    if state.get("used_day") != _today_iso():
        state["used_day"] = _today_iso()
        state["used_strategies"] = []
    return {str(s) for s in (state.get("used_strategies") or []) if s}


def mark_strategy_used(state: dict, sid: str) -> None:
    used = used_strategies_today(state)
    used.add(str(sid))
    state["used_day"] = _today_iso()
    state["used_strategies"] = sorted(used)
    save_state(state)


def open_strategy_ids(trade, state: dict) -> set[str]:
    """Strategies with an active tracked lot (not merely attempted today)."""
    out: set[str] = set()
    for lot in active_lots(state):
        sid = lot.get("strategy_id")
        if sid and sid != "ORPHAN":
            out.add(str(sid))
    return out


_WORKING = {
    "new", "accepted", "pending_new", "accepted_for_bidding",
    "partially_filled", "held", "pending_replace", "pending_cancel",
    "done_for_day",
}
_FILLED = {"filled"}
_DEAD = {"canceled", "cancelled", "expired", "rejected", "replaced"}


def _order_status(trade, order_id: str) -> str:
    if not order_id:
        return ""
    try:
        o = trade.get_order_by_id(order_id)
        return str(getattr(o, "status", "") or "").lower().replace(" ", "_")
    except Exception:
        return ""


def make_arm(sid: str) -> EffectiveArm | None:
    """Paper baseline bucket 0 arm — same virtual $500 / max_contracts=1 as paper lab."""
    if not _strat(sid):
        return None
    return _merge_arm(PAPER_BASELINE, sid, VIRTUAL_BUCKET_USD)


def cid_entry() -> str:
    return f"OLB|{date.today().strftime('%Y%m%d')}|{uuid.uuid4().hex[:8]}"[:48]


def cid_exit() -> str:
    return f"OLX|{uuid.uuid4().hex[:12]}"[:48]


def cid_stop() -> str:
    return f"OLS|{uuid.uuid4().hex[:12]}"[:48]


def _norm_occ(sym: str) -> str:
    """Normalize OCC-ish symbols for comparison (case, non-alnum stripped)."""
    return re.sub(r"[^A-Z0-9]", "", str(sym or "").upper())


def _parse_occ(sym: str) -> tuple[str, str, str, str] | None:
    """Return (root, yymmdd, cp, strike8) or None."""
    m = re.match(r"^([A-Z]+)(\d{6})([CP])(\d{8})$", _norm_occ(sym))
    if not m:
        return None
    return m.group(1), m.group(2), m.group(3), m.group(4)


def _order_matches_occ(order_sym: str, occ: str) -> bool:
    """Robust OCC match — Alpaca sometimes differs on formatting/strike padding."""
    a, b = _norm_occ(order_sym), _norm_occ(occ)
    if not a or not b:
        return False
    if a == b:
        return True
    if a.endswith(b) or b.endswith(a):
        return True
    pa, pb = _parse_occ(a), _parse_occ(b)
    if not pa or not pb:
        # Fallback: same root ticker contained + same trailing 15 chars (date+cp+strike-ish)
        return a[-15:] == b[-15:] if len(a) >= 15 and len(b) >= 15 else False
    root_a, d_a, cp_a, k_a = pa
    root_b, d_b, cp_b, k_b = pb
    if root_a != root_b or d_a != d_b or cp_a != cp_b:
        return False
    # Strike: compare as ints (leading zeros / padding differences).
    try:
        return int(k_a) == int(k_b)
    except Exception:
        return k_a == k_b


def _list_open_orders(trade, occ: str | None = None) -> list:
    """List open orders; optionally filter to those matching OCC."""
    try:
        req = GetOrdersRequest(status=QueryOrderStatus.OPEN, limit=200)
        orders = list(trade.get_orders(req) or [])
    except Exception as exc:
        rl(f"Live micro list open orders failed: {exc}")
        return []
    if occ is None:
        return orders
    return [o for o in orders if _order_matches_occ(str(getattr(o, "symbol", "") or ""), occ)]


def _order_dbg(o) -> str:
    return (
        f"id={getattr(o, 'id', '?')} "
        f"sym={getattr(o, 'symbol', '?')!r} "
        f"side={getattr(o, 'side', '?')} "
        f"status={getattr(o, 'status', '?')} "
        f"cid={getattr(o, 'client_order_id', '') or '-'!r} "
        f"type={getattr(o, 'type', getattr(o, 'order_type', '?'))}"
    )


def _extract_wash_existing_order_id(exc: Exception) -> str | None:
    """Pull existing_order_id from Alpaca wash-trade rejection JSON/text."""
    text = str(exc)
    m = re.search(r'"existing_order_id"\s*:\s*"([0-9a-fA-F-]{20,})"', text)
    if m:
        return m.group(1)
    m = re.search(r"existing_order_id['\"]?\s*[:=]\s*['\"]([0-9a-fA-F-]{20,})", text)
    if m:
        return m.group(1)
    # Dict-like repr from alpaca-py
    m = re.search(r"existing_order_id['\"]:\s*['\"]([0-9a-fA-F-]{20,})", text)
    if m:
        return m.group(1)
    return None


def _cancel_order_id(trade, order_id: str, reason: str) -> bool:
    if not order_id:
        return False
    try:
        trade.cancel_order_by_id(order_id)
        rl(f"Live micro cancel by id ({reason}) id={order_id}")
        return True
    except Exception as exc:
        rl(f"Live micro cancel by id failed ({reason}) id={order_id}: {exc}")
        return False


def _cancel_stale_exit_sells(trade, occ: str) -> int:
    """Cancel open non-OLS sells on OCC (unblocks wash-trade; keeps OLS stops)."""
    n = 0
    scoped: list = []
    try:
        req = GetOrdersRequest(status=QueryOrderStatus.OPEN, symbols=[occ], limit=50)
        scoped = list(trade.get_orders(req) or [])
    except Exception as exc:
        rl(f"Live micro symbol-scoped orders query failed {occ}: {exc}")
        scoped = []

    if scoped:
        candidates = scoped
        rl(f"Live micro cancel-scan {occ}: symbol-scoped n={len(candidates)}")
    else:
        try:
            req = GetOrdersRequest(status=QueryOrderStatus.OPEN, limit=200)
            all_open = list(trade.get_orders(req) or [])
        except Exception as exc:
            rl(f"Live micro list orders failed {occ}: {exc}")
            return 0
        # Debug: dump every open order when OCC-scoped query is empty so we
        # can see how Alpaca labels the COST sell (symbol format mismatch).
        rl(f"Live micro cancel-scan {occ}: symbol-scoped empty; open_book n={len(all_open)}")
        for o in all_open:
            rl(f"  open_order {_order_dbg(o)}")
        candidates = [
            o for o in all_open
            if _order_matches_occ(str(getattr(o, "symbol", "") or ""), occ)
        ]
        rl(f"Live micro cancel-scan {occ}: matched n={len(candidates)}")

    for o in candidates:
        cid = str(getattr(o, "client_order_id", "") or "")
        side = str(getattr(o, "side", "") or "").lower()
        if "sell" not in side:
            continue
        if cid.startswith("OLS"):
            continue
        try:
            trade.cancel_order_by_id(o.id)
            n += 1
            rl(f"Live micro cancel stale sell {occ} id={o.id} cid={cid or '-'} "
               f"broker_sym={getattr(o, 'symbol', '')!r}")
        except Exception as exc:
            rl(f"Live micro cancel sell failed {occ} id={getattr(o, 'id', '?')}: {exc}")
    if n == 0:
        rl(f"Live micro cancel-scan {occ}: no non-OLS sell to cancel")
    return n


def _underlying_from_occ(occ: str) -> str:
    m = re.match(r"^([A-Z]+)", occ or "")
    return m.group(1) if m else (occ or "")


def reconcile(trade, state: dict, now: datetime) -> dict:
    used_strategies_today(state)
    for lot in active_lots(state):
        sid = str(lot.get("strategy_id") or "")
        if sid and sid not in (state.get("used_strategies") or []) and sid != "ORPHAN":
            state.setdefault("used_strategies", []).append(sid)
    pos = {str(getattr(p, "symbol", "")): p for p in option_positions(trade)}
    kept = []
    for lot in active_lots(state):
        occ = lot.get("occ")
        sid = str(lot.get("strategy_id") or "")
        if occ in pos:
            if lot.get("pending"):
                lot["pending"] = False
                rl(f"Live micro fill confirmed {sid} {occ}")
                append_ledger({
                    "ts": now.isoformat(), "event": "fill_confirm",
                    "strategy_id": sid, "occ": occ, "qty": lot.get("qty"),
                    "order_id": lot.get("order_id"),
                    "reason": "broker_position",
                })
            kept.append(lot)
            continue
        st = _order_status(trade, str(lot.get("order_id") or ""))
        if st in _WORKING or st in _FILLED or not st:
            # Empty status = lookup failed; keep the lot so we do not rebuy.
            lot["pending"] = True
            kept.append(lot)
            rl(f"Live micro pending {sid} {occ} order_status={st or 'unknown'}")
            continue
        rl(f"Live micro reconcile: unfilled {occ} {sid} status={st} (slot kept for today)")
        append_ledger({
            "ts": now.isoformat(), "event": "unfilled",
            "strategy_id": sid, "occ": occ,
            "qty": lot.get("qty"), "reason": st or "missing_from_broker",
            "order_id": lot.get("order_id"),
        })
        if sid and sid != "ORPHAN":
            mark_strategy_used(state, sid)
    state["lots"] = kept

    # Adopt broker option positions the bot does not track (bleed-stop P0).
    tracked = {str(l.get("occ") or "") for l in active_lots(state)}
    for occ, p in pos.items():
        if not occ or occ in tracked:
            continue
        try:
            qty = int(float(getattr(p, "qty", 0) or 0))
        except Exception:
            continue
        if qty <= 0:
            continue
        entry = float(getattr(p, "avg_entry_price", 0) or 0)
        if entry <= 0:
            rl(f"WARN orphan_adopt {occ}: avg_entry_price missing; "
               f"using 0.01 placeholder (TP/SL % will be wrong until filled mark)")
            entry = 0.01
        _cancel_stale_exit_sells(trade, occ)
        lot = {
            "lot_id": uuid.uuid4().hex[:12],
            "strategy_id": "ORPHAN",
            "occ": occ,
            "underlying": _underlying_from_occ(occ),
            "qty": qty,
            "entry_price": entry,
            "take_profit": TAKE_PROFIT,
            "stop_loss": STOP_LOSS,
            "order_id": f"orphan:{occ}",
            "pending": False,
        }
        state.setdefault("lots", []).append(lot)
        append_ledger({
            "ts": now.isoformat(), "event": "orphan_adopt",
            "strategy_id": "ORPHAN", "occ": occ, "qty": qty,
            "limit": entry, "cost": round(entry * 100 * qty, 2),
            "reason": "broker_position_untracked",
            "order_id": lot["order_id"],
        })
        rl(f"Live micro orphan_adopt {occ} x{qty} entry={entry:.2f}")

    save_state(state)
    return state


def _cancel_protective(trade, occ: str) -> None:
    for o in _list_open_orders(trade, occ):
        cid = getattr(o, "client_order_id", "") or ""
        if cid.startswith("OLS"):
            try:
                trade.cancel_order_by_id(o.id)
                rl(f"Live micro cancel OLS stop {occ} id={o.id}")
            except Exception as exc:
                rl(f"Live micro cancel OLS failed {occ}: {exc}")


def _option_bid(opt, occ: str) -> float | None:
    try:
        m = re.match(r"^[A-Z]+", occ or "")
        underlying = m.group(0) if m else None
        if not underlying:
            return None
        ch = opt.get_option_chain(OptionChainRequest(underlying_symbol=underlying))
        snap = ch.get(occ) if ch else None
        lq = getattr(snap, "latest_quote", None) if snap else None
        bid = getattr(lq, "bid_price", None) if lq else None
        if bid and float(bid) > 0:
            return float(bid)
    except Exception:
        return None
    return None


def manage(trade, opt, state: dict, now: datetime) -> None:
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
            rl(
                f"Live micro hold {lot.get('strategy_id')} {occ} "
                f"{plpc:+.1%} (tp {tp:+.0%} / sl {sl:+.0%})"
            )
            continue
        _cancel_protective(trade, occ)
        _cancel_stale_exit_sells(trade, occ)
        sell_qty = min(qty, int(lot["qty"]))
        bid = _option_bid(opt, occ)
        sell_limit = round(max(0.01, (bid or 0.01) + SELL_LIMIT_OFFSET), 2)
        use_market = _ge(now, om.EOD_MARKET) or (not bid)
        no_quote = (not bid) or float(bid or 0) <= 0.01 or plpc <= -0.99
        if no_quote:
            use_market = False
            sell_limit = 0.01
        try:
            if use_market:
                o = trade.submit_order(MarketOrderRequest(
                    symbol=occ, qty=sell_qty, side=OrderSide.SELL,
                    time_in_force=TimeInForce.DAY, client_order_id=cid_exit(),
                ))
            else:
                o = trade.submit_order(LimitOrderRequest(
                    symbol=occ, qty=sell_qty, side=OrderSide.SELL,
                    time_in_force=TimeInForce.DAY, limit_price=sell_limit,
                    client_order_id=cid_exit(),
                ))
            how = "MARKET" if use_market else f"limit={sell_limit:.2f}"
            rl(f"LIVE EXIT {reason} {occ} x{sell_qty} {how} id={o.id}")
            lot["qty"] = 0
            append_ledger({
                "ts": now.isoformat(), "event": "exit",
                "strategy_id": lot.get("strategy_id"), "occ": occ, "qty": sell_qty,
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
        if not occ:
            continue
        p = pos.get(occ)
        if p is None:
            for sym, cand in pos.items():
                if _order_matches_occ(sym, str(occ)):
                    p = cand
                    break
        if p is None:
            rl(f"LIVE PROT skip {occ}: not in broker positions")
            continue
        have = False
        ols_id = None
        try:
            open_for_occ = _list_open_orders(trade, str(occ))
            for o in open_for_occ:
                cid = str(getattr(o, "client_order_id", "") or "")
                if cid.startswith("OLS"):
                    have = True
                    ols_id = getattr(o, "id", None)
                    break
            rl(
                f"LIVE PROT check {occ}: have_ols={have} "
                f"open_matched={len(open_for_occ)} ols_id={ols_id or '-'}"
            )
        except Exception as exc:
            rl(f"LIVE PROT check failed {occ} (will still try place): {exc}")
            have = False
        if have:
            continue
        entry = float(lot.get("entry_price") or 0) or float(
            getattr(p, "avg_entry_price", 0) or 0
        )
        sl = float(lot.get("stop_loss") or STOP_LOSS)
        if entry <= 0 or sl >= 0:
            rl(f"LIVE PROT skip {occ}: bad entry/sl entry={entry} sl={sl}")
            continue
        stop_px = round(max(0.01, entry * (1.0 + sl)), 2)
        lim = round(max(0.01, stop_px * 0.92), 2)
        qty = int(lot["qty"])
        # Prefer stop-market so gaps still exit (stop-limit often never fills).
        try:
            o = trade.submit_order(StopOrderRequest(
                symbol=str(getattr(p, "symbol", None) or occ), qty=qty,
                side=OrderSide.SELL,
                time_in_force=TimeInForce.DAY, stop_price=stop_px,
                client_order_id=cid_stop(),
            ))
            rl(f"LIVE PROT STOP-MKT {occ} x{qty} stop={stop_px:.2f} id={o.id}")
        except Exception as exc:
            rl(f"LIVE PROT STOP-MKT rejected {occ}: {exc}; trying stop-limit")
            try:
                o = trade.submit_order(StopLimitOrderRequest(
                    symbol=str(getattr(p, "symbol", None) or occ), qty=qty,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.GTC,
                    stop_price=stop_px, limit_price=lim,
                    client_order_id=cid_stop(),
                ))
                rl(f"LIVE PROT STOP {occ} x{qty} stop={stop_px:.2f} lim={lim:.2f} id={o.id}")
            except Exception as exc2:
                rl(f"LIVE PROT STOP failed {occ} (both market+limit): mkt={exc} lim={exc2}")


def _dedupe_hits(hits: list) -> list:
    """One hit per (signal family, symbol). Keeps the higher-win-rate strategy."""
    best: dict = {}
    for h in hits:
        fam = SIGNAL_FAMILY.get(h.strategy_id, h.strategy_id)
        key = (fam, h.symbol)
        prev = best.get(key)
        if prev is None or _win_key(h.strategy_id) < _win_key(prev.strategy_id):
            best[key] = h
    out = list(best.values())
    out.sort(key=lambda h: (_win_key(h.strategy_id), h.symbol))
    return out


def scan_hits(stock) -> list:
    strats = _allow_strats()
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
    hits.sort(key=lambda h: _win_key(h.strategy_id))
    return _dedupe_hits(hits)


def place(trade, opt, ref, stock, equity: float, cash: float, state: dict,
          now: datetime) -> int:
    if not _between(now, om.ENTRY_START, om.ENTRY_END):
        rl("Live micro: outside entry window")
        return 0
    if not ENTRIES_ENABLED:
        rl("Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only")
        return 0
    sleeve = max(0.0, equity * SHARE)
    deployed = option_mv(trade)
    open_strats = open_strategy_ids(trade, state)
    used_today = used_strategies_today(state)
    allow = [s.id for s in _allow_strats()]
    rank_txt = ", ".join(
        f"{sid} {CLEAN_RANK.get(sid, (0, 0))[0]:.0f}%win"
        for sid in allow
    )
    rl(
        f"Live micro sleeve ${sleeve:.0f} ({SHARE:.0%} of ${equity:.0f}) "
        f"deployed ${deployed:.0f} open_strategies={len(open_strats)}/{len(allow)} "
        f"(paper baseline ${PAPER_MAX_PREMIUM:.0f} / tp={TAKE_PROFIT:+.0%} "
        f"sl={STOP_LOSS:+.0%} / 1 contract per strategy / min_cost ${MIN_ENTRY_COST:.0f})"
    )
    rl(f"Live micro entry order (CLEAN win): {rank_txt}")
    hits = scan_hits(stock)
    rl(f"Live micro signals: {len(hits)}")
    placed = 0
    chain_cache: dict = {}
    oi_cache: dict = {}
    for hit in hits:
        if hit.strategy_id in used_today:
            rl(f"  skip {hit.strategy_id} {hit.symbol}: already attempted today")
            continue
        if hit.strategy_id in open_strats:
            rl(f"  skip {hit.strategy_id} {hit.symbol}: strategy already open (paper bucket rule)")
            continue
        win, med = CLEAN_RANK.get(hit.strategy_id, (0.0, 0.0))
        rl(f"  try {hit.strategy_id} {win:.0f}%win/{med:+.0f}%med {hit.symbol}")
        arm = make_arm(hit.strategy_id)
        if not arm:
            continue
        st = _strat(hit.strategy_id)
        if not st:
            continue
        room = min(max(0.0, cash), max(0.0, sleeve - option_mv(trade)))
        max_prem = min(float(arm.max_premium), room)
        if max_prem <= 0:
            rl(f"  skip {hit.strategy_id} {hit.symbol}: no sleeve/cash room")
            continue
        cand = om._pick_option_from_chain(
            opt, ref, hit.symbol, hit.price,
            st.dte_min, st.dte_max, st.dte_target, arm,
            chain_cache=chain_cache, oi_cache=oi_cache,
        )
        if not cand:
            rl(f"  skip {hit.strategy_id} {hit.symbol}: no contract under ${max_prem:.0f}")
            continue
        if cand["cost"] < MIN_ENTRY_COST - 0.01:
            rl(
                f"  skip {hit.strategy_id} {hit.symbol}: cost ${cand['cost']:.0f} "
                f"< min ${MIN_ENTRY_COST:.0f} (lottery ticket filter)"
            )
            continue
        if cand["cost"] > max_prem + 0.01:
            rl(f"  skip {hit.strategy_id} {hit.symbol}: cost ${cand['cost']:.0f} > ${max_prem:.0f}")
            continue
        limit = entry_limit_price(arm, cand["bid"], cand["ask"], cand["mid"])
        try:
            o = trade.submit_order(LimitOrderRequest(
                symbol=cand["symbol"], qty=1, side=OrderSide.BUY,
                time_in_force=TimeInForce.DAY,
                limit_price=limit,
                client_order_id=cid_entry(),
            ))
            lot = {
                "lot_id": uuid.uuid4().hex[:12],
                "strategy_id": hit.strategy_id,
                "occ": cand["symbol"],
                "underlying": hit.symbol,
                "qty": 1,
                "entry_price": float(limit),
                "take_profit": arm.take_profit,
                "stop_loss": arm.stop_loss,
                "order_id": str(o.id),
                "pending": True,
            }
            state.setdefault("lots", []).append(lot)
            mark_strategy_used(state, hit.strategy_id)
            save_state(state)
            append_ledger({
                "ts": now.isoformat(), "event": "entry",
                "strategy_id": hit.strategy_id, "occ": cand["symbol"],
                "qty": 1, "limit": limit, "cost": cand["cost"],
                "order_id": str(o.id), "reason": hit.detail,
            })
            rl(
                f"LIVE BUY {hit.strategy_id} {win:.0f}%win {hit.symbol} {cand['symbol']} "
                f"limit={limit:.2f} ask={cand['ask']:.2f} cost=${cand['cost']:.0f} id={o.id}"
            )
            placed += 1
            open_strats.add(hit.strategy_id)
            used_today.add(hit.strategy_id)
        except Exception as exc:
            rl(f"LIVE BUY failed {hit.strategy_id} {hit.symbol}: {exc}")
            oid = _extract_wash_existing_order_id(exc)
            if oid:
                rl(f"Live micro wash-trade self-heal: cancel existing_order_id={oid}")
                if _cancel_order_id(trade, oid, "wash_trade_existing_order_id"):
                    # Also clear any other stale sells on candidate OCC if known.
                    try:
                        _cancel_stale_exit_sells(trade, cand["symbol"])
                    except Exception:
                        pass
            continue
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
        opt_lvl = (
            getattr(acct, "options_trading_level", None)
            or getattr(acct, "options_approved_level", None)
            or "?"
        )
        rl(f"Live account equity ${equity:.2f} cash ${cash:.2f} "
           f"#{getattr(acct, 'account_number', '?')} options_level={opt_lvl}")
    except Exception as exc:
        rl(f"FATAL live get_account: {exc}")
        return 0

    state = load_state()
    state = reconcile(trade, state, now)

    in_session = _between(now, om.ENTRY_START, om.HARD_STOP)
    if not in_session:
        if _ge(now, om.HARD_STOP):
            manage(trade, opt, state, now)
        else:
            rl("Live micro: outside 9:28-16:05 ET")
        n = len(option_positions(trade))
        rl(f"Live micro done. open_options={n} lots={len(active_lots(state))}")
        return 0

    manage(trade, opt, state, now)
    # Clear leftover exit sells on tracked lots so protective stops can rest.
    for lot in active_lots(state):
        occ = lot.get("occ")
        if occ:
            _cancel_stale_exit_sells(trade, str(occ))
    ensure_stops(trade, state)
    if _between(now, om.ENTRY_START, om.ENTRY_END):
        place(trade, opt, ref, stock, equity, cash, state, now)
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
