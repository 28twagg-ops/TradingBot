"""
options_reconcile.py — Detect lots in state that are no longer in Alpaca, and clean them up.

If an open lot in lab_state.json is NOT in the Alpaca positions list, it means it
was closed manually, expired, or otherwise removed from the broker. This script
backfills exit P&L from filled sell orders when possible, otherwise zeroes the
lot and appends a missing_from_broker reconcile row.

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
    ORDER_FETCH_LIMIT,
    STATE_PATH,
    append_ledger,
    attribute_vanished_lots,
    load_state,
    save_state,
)

log = logging.getLogger("options_reconcile")
logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(levelname)-8s  %(message)s")

PAPER_TRADING = True

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


def _fetch_closed_orders(trade) -> list:
    from alpaca.trading.requests import GetOrdersRequest
    from alpaca.trading.enums import QueryOrderStatus

    try:
        return list(trade.get_orders(
            GetOrdersRequest(status=QueryOrderStatus.CLOSED, limit=ORDER_FETCH_LIMIT)
        ) or [])
    except Exception as e:
        log.warning("could not list closed orders: %s", e)
        return []


def run(dry_run: bool = False) -> int:
    key = os.getenv("ALPACA_PAPER_KEY")
    secret = os.getenv("ALPACA_PAPER_SECRET")
    keys_ok = bool(key and secret)

    state = load_state()
    open_lots = [l for l in state.lots if int(l.qty) > 0]

    print(f"options_reconcile: state={STATE_PATH}")
    print(f"  open_lots={len(open_lots)} "
          f"paper_keys={'yes' if keys_ok else 'NO'} dry_run={dry_run}")

    if not keys_ok:
        print("  Paper keys unavailable — skipping reconcile.")
        return 0

    try:
        from alpaca.trading.client import TradingClient
        trade = TradingClient(key, secret, paper=PAPER_TRADING)
        positions = _position_symbols(trade)
        print(f"  alpaca positions={len(positions)}")
    except Exception as e:
        print(f"  WARN: paper client init failed: {e}")
        return 0

    missing = [l for l in open_lots if l.occ_symbol not in positions]
    if not missing:
        print("  No missing lots.")
        print("options_reconcile: done")
        return 0

    print(f"  FLAG {len(missing)} lot(s) missing from Alpaca")
    for lot in missing:
        print(f"    b{lot.bucket_id}|{lot.strategy_id}|{lot.lot_id[:8]} {lot.occ_symbol}")

    if dry_run:
        print("  dry-run — no state/ledger changes")
        print("options_reconcile: done")
        return 0

    orders = _fetch_closed_orders(trade)
    n = attribute_vanished_lots(state, missing, orders, log_fn=print)
    # Any leftovers without qty still get a ghost clear (attribute sets qty=0).
    leftover = [l for l in state.lots if int(l.qty) > 0 and l.occ_symbol not in positions]
    for lot in leftover:
        lot.qty = 0
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
                "qty": 0,
                "limit": "",
                "fill_price": "",
                "cost": round(lot.entry_cost, 2),
                "return_pct": "",
                "pnl_usd": "",
                "reason": "missing_from_broker",
                "buy_offset": "",
                "sell_offset": "",
                "take_profit": lot.take_profit,
                "stop_loss": lot.stop_loss,
                "spread_frac": "",
                "detail": "lot closed outside of bot (expired/manual)",
                "order_id": "",
            })
        except Exception as e:
            log.warning("ledger append failed: %s", e)
    state.lots = [l for l in state.lots if int(l.qty) > 0]
    save_state(state)
    print(f"  State updated (attributed/cleared={n}, leftover={len(leftover)}).")
    print("options_reconcile: done")
    return 0

def main() -> int:
    ap = argparse.ArgumentParser(description="Options missing-lot reconcile (paper)")
    ap.add_argument("--dry-run", action="store_true", help="Detect only; do not modify state")
    ap.add_argument("--no-exit", action="store_true", help="Ignored, kept for compatibility")
    args = ap.parse_args()
    try:
        return run(dry_run=args.dry_run)
    except Exception as e:
        print(f"reconcile failed (non-fatal): {e}")
        return 0

if __name__ == "__main__":
    raise SystemExit(main())
