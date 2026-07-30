"""
options_reconcile.py — Detect lots in state that are no longer in Alpaca, and clean them up.

If an open lot in lab_state.json is NOT in the Alpaca positions list, it means it
was closed manually, expired, or otherwise removed from the broker. This script
zeroes the quantity in the state and appends a reconcile exit to the ledger.

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

    mutated = False
    for lot in open_lots:
        if lot.occ_symbol not in positions:
            print(f"  FLAG b{lot.bucket_id}|{lot.strategy_id}|{lot.lot_id[:8]} missing from Alpaca")
            if not dry_run:
                # Lot is no longer in broker. Reconcile it out.
                lot.qty = 0
                mutated = True
                
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
                        "cost": 0,
                        "return_pct": "",
                        "pnl_usd": "",
                        "reason": "missing_from_broker",
                        "buy_offset": "",
                        "sell_offset": "",
                        "take_profit": "",
                        "stop_loss": "",
                        "spread_frac": "",
                        "detail": "lot closed outside of bot (expired/manual)",
                        "order_id": "",
                    })
                except Exception as e:
                    log.warning("ledger append failed: %s", e)

    if mutated and not dry_run:
        save_state(state)
        print("  State updated with reconciled lots.")
        
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
