"""
options_reconcile.py — Detect zombie paper options lots and optionally exit them.

A zombie = open lot in lab_state.json with no covering sell order / pending exit,
older than ZOMBIE_AGE_MINUTES, and notional > MIN_NOTIONAL_USD.

PAPER ONLY (ALPACA_PAPER_KEY / ALPACA_PAPER_SECRET). Always exits 0 for GHA.

Usage:
  python scripts/options_reconcile.py
  python scripts/options_reconcile.py --dry-run
"""
from __future__ import annotations

import argparse
import logging
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from options_lab import (  # noqa: E402
    STATE_PATH,
    append_ledger,
    load_state,
    save_state,
)

log = logging.getLogger("options_reconcile")
logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(levelname)-8s  %(message)s")

ZOMBIE_AGE_MINUTES = 60
MIN_NOTIONAL_USD = 5.0  # entry_price * qty * 100
PAPER_TRADING = True


def _norm_status(val) -> str:
    if val is None:
        return ""
    if hasattr(val, "value"):
        try:
            return str(val.value).lower()
        except Exception:
            pass
    s = str(val).lower()
    if "." in s:
        s = s.rsplit(".", 1)[-1]
    return s


def _lot_age_minutes(lot) -> float:
    raw = (lot.entry_date or "").strip()
    if not raw:
        return 0.0
    for fmt in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            dt = datetime.strptime(raw[:19] if "T" in raw or " " in raw else raw[:10], fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return max(0.0, (datetime.now(timezone.utc) - dt.astimezone(timezone.utc)).total_seconds() / 60.0)
        except ValueError:
            continue
    return 0.0


def _notional(lot) -> float:
    px = float(lot.entry_price or 0.0)
    if px <= 0 and lot.entry_cost and lot.qty:
        # entry_cost is already premium dollars for the lot
        return float(lot.entry_cost)
    return px * int(lot.qty) * 100.0


def _open_sell_symbols(trade) -> set[str]:
    """OCC symbols with an open sell order on the paper account."""
    out: set[str] = set()
    try:
        from alpaca.trading.requests import GetOrdersRequest
        from alpaca.trading.enums import QueryOrderStatus, OrderSide
        req = GetOrdersRequest(status=QueryOrderStatus.OPEN, limit=500)
        orders = trade.get_orders(filter=req)
        for o in orders or []:
            side = _norm_status(getattr(o, "side", None))
            if side not in ("sell", str(OrderSide.SELL).lower()):
                # also accept enum name
                if "sell" not in side:
                    continue
            sym = getattr(o, "symbol", None)
            if sym:
                out.add(str(sym))
    except Exception as e:
        log.warning("could not list open orders: %s", e)
    return out


def _position_symbols(trade) -> set[str]:
    out: set[str] = set()
    try:
        for p in trade.get_all_positions() or []:
            sym = getattr(p, "symbol", None)
            if sym:
                out.add(str(sym))
    except Exception as e:
        log.warning("could not list positions: %s", e)
    return out


def _emergency_exit(trade, lot, dry_run: bool) -> str:
    """Place market sell for zombie lot. Returns status string."""
    if dry_run:
        return "dry_run_skip"
    try:
        from alpaca.trading.requests import MarketOrderRequest
        from alpaca.trading.enums import OrderSide, TimeInForce
        req = MarketOrderRequest(
            symbol=lot.occ_symbol,
            qty=int(lot.qty),
            side=OrderSide.SELL,
            time_in_force=TimeInForce.DAY,
        )
        o = trade.submit_order(req)
        oid = getattr(o, "id", "")
        return f"submitted:{oid}"
    except Exception as e:
        return f"error:{e}"


def run(dry_run: bool = False, place_exits: bool = True) -> int:
    key = os.getenv("ALPACA_PAPER_KEY")
    secret = os.getenv("ALPACA_PAPER_SECRET")
    keys_ok = bool(key and secret)

    state = load_state()
    open_lots = [l for l in state.lots if int(l.qty) > 0]
    pending_exit_lots = {pe.lot_id for pe in state.pending_exits}
    pending_exit_occs = {pe.occ_symbol for pe in state.pending_exits}

    print(f"options_reconcile: state={STATE_PATH}")
    print(f"  open_lots={len(open_lots)} pending_exits={len(state.pending_exits)} "
          f"paper_keys={'yes' if keys_ok else 'NO'} dry_run={dry_run}")

    trade = None
    open_sells: set[str] = set()
    positions: set[str] = set()
    if keys_ok:
        try:
            from alpaca.trading.client import TradingClient
            trade = TradingClient(key, secret, paper=PAPER_TRADING)
            open_sells = _open_sell_symbols(trade)
            positions = _position_symbols(trade)
            print(f"  alpaca open sell orders={len(open_sells)} positions={len(positions)}")
        except Exception as e:
            print(f"  WARN: paper client init failed: {e}")
            trade = None
            keys_ok = False
    else:
        print("  Paper keys unavailable — detection/logging only; exit placement stubbed.")

    zombies = []
    for lot in open_lots:
        age = _lot_age_minutes(lot)
        notion = _notional(lot)
        has_pending = lot.lot_id in pending_exit_lots or lot.occ_symbol in pending_exit_occs
        has_sell = lot.occ_symbol in open_sells
        if has_pending or has_sell:
            continue
        if age < ZOMBIE_AGE_MINUTES:
            continue
        if notion < MIN_NOTIONAL_USD:
            continue
        zombies.append((lot, age, notion))

    print(f"  zombies_flagged={len(zombies)}")
    for lot, age, notion in zombies:
        action = "detect_only"
        if keys_ok and trade is not None and place_exits:
            # Only emergency-exit if Alpaca still shows a position
            if lot.occ_symbol in positions:
                action = _emergency_exit(trade, lot, dry_run=dry_run)
            else:
                action = "no_broker_position"
        elif not keys_ok:
            action = "TODO_place_exit_when_keys_available"
        detail = (
            f"zombie age_min={age:.0f} notional=${notion:.2f} "
            f"occ={lot.occ_symbol} action={action}"
        )
        print(f"  FLAG b{lot.bucket_id}|{lot.strategy_id}|{lot.lot_id[:8]} {detail}")
        try:
            append_ledger({
                "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "event": "reconcile",
                "bucket_id": lot.bucket_id,
                "profile": lot.profile_name,
                "strategy_id": lot.strategy_id,
                "lot_id": lot.lot_id,
                "symbol": lot.underlying,
                "occ": lot.occ_symbol,
                "qty": lot.qty,
                "limit": "",
                "fill_price": "",
                "cost": notion,
                "return_pct": "",
                "pnl_usd": "",
                "reason": "zombie_lot",
                "buy_offset": "",
                "sell_offset": "",
                "take_profit": "",
                "stop_loss": "",
                "spread_frac": "",
                "detail": detail,
                "order_id": "",
            })
        except Exception as e:
            log.warning("ledger append failed: %s", e)

    # Touch state write only if we mutated (we don't mutate lots here yet)
    _ = save_state  # imported for future use / API stability
    print("options_reconcile: done")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Options zombie-lot reconcile (paper)")
    ap.add_argument("--dry-run", action="store_true", help="Detect only; never submit exits")
    ap.add_argument("--no-exit", action="store_true", help="Never place emergency exits")
    args = ap.parse_args()
    try:
        return run(dry_run=args.dry_run, place_exits=not args.no_exit)
    except Exception as e:
        print(f"reconcile failed (non-fatal): {e}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
