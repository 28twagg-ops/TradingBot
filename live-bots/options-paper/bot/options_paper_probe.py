#!/usr/bin/env python3
"""
Paper options connectivity + optional smoke entry.

Default (--check-only): verify Alpaca paper auth, account, open option orders.
--smoke-entry: submit one cheap liquid SPY call limit (paper only) when market
is open — use to confirm order routing without waiting for a signal.

Requires ALPACA_PAPER_KEY / ALPACA_PAPER_SECRET (same as options_morning_bot).
"""
from __future__ import annotations

import argparse
import os
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from alpaca.trading.client import TradingClient
from alpaca.trading.enums import AssetClass, OrderSide, QueryOrderStatus, TimeInForce
from alpaca.trading.requests import GetOrdersRequest, LimitOrderRequest
from alpaca.data.historical import OptionHistoricalDataClient, StockHistoricalDataClient
from alpaca.data.requests import OptionChainRequest, StockLatestQuoteRequest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_universe import to_alpaca_symbol  # noqa: E402

ET = ZoneInfo("America/New_York")
API_KEY = os.getenv("ALPACA_PAPER_KEY")
API_SECRET = os.getenv("ALPACA_PAPER_SECRET")
PROBE_SYMBOL = os.getenv("OPTIONS_PROBE_SYMBOL", "SPY")


def _fail(msg: str, code: int = 1) -> int:
    print(f"PROBE FAIL: {msg}")
    return code


def _market_open(now: datetime | None = None) -> bool:
    now = now or datetime.now(ET)
    if now.weekday() >= 5:
        return False
    hm = now.hour * 60 + now.minute
    return 9 * 60 + 30 <= hm < 16 * 60


def _pick_cheap_call(opt: OptionHistoricalDataClient, stock: StockHistoricalDataClient,
                     underlying: str) -> dict | None:
    sym = to_alpaca_symbol(underlying)
    try:
        q = stock.get_stock_latest_quote(StockLatestQuoteRequest(symbol_or_symbols=sym))
        spot = float(q[sym].ask_price or q[sym].bid_price or 0)
    except Exception:
        spot = 0.0
    if spot <= 0:
        return None
    today = date.today()
    chain = opt.get_option_chain(OptionChainRequest(
        underlying_symbol=sym,
        expiration_date_gte=today + timedelta(days=2),
        expiration_date_lte=today + timedelta(days=7),
    ))
    best = None
    for occ, snap in (chain or {}).items():
        if not occ.endswith("C"):
            continue
        bid = float(getattr(snap, "bid_price", 0) or 0)
        ask = float(getattr(snap, "ask_price", 0) or 0)
        if bid <= 0 or ask <= 0 or ask > 3.0:
            continue
        mid = (bid + ask) / 2
        cost = mid * 100
        if cost < 25 or cost > 200:
            continue
        cand = {"occ": occ, "bid": bid, "ask": ask, "mid": mid, "cost": cost}
        if best is None or cand["cost"] < best["cost"]:
            best = cand
    return best


def run_check(trade: TradingClient) -> int:
    acct = trade.get_account()
    print(f"PROBE OK: paper account status={acct.status} equity=${float(acct.equity):,.2f}")
    print(f"  buying_power=${float(acct.buying_power):,.2f} cash=${float(acct.cash):,.2f}")
    orders = trade.get_orders(GetOrdersRequest(
        status=QueryOrderStatus.OPEN, nested=True, limit=20))
    opts = [o for o in orders if getattr(o, "asset_class", None) == AssetClass.US_OPTION
            or (o.symbol and len(o.symbol) > 10)]
    print(f"  open option orders: {len(opts)}")
    for o in opts[:5]:
        print(f"    {o.symbol} {o.side} qty={o.qty} status={o.status} limit={o.limit_price}")
    positions = trade.get_all_positions()
    opt_pos = [p for p in positions if len(p.symbol) > 10]
    print(f"  open option positions: {len(opt_pos)}")
    for p in opt_pos[:5]:
        print(f"    {p.symbol} qty={p.qty} mkt=${float(p.market_value):,.2f}")
    return 0


def run_smoke_entry(trade: TradingClient, opt: OptionHistoricalDataClient,
                    stock: StockHistoricalDataClient) -> int:
    if not _market_open():
        return _fail("market closed — smoke entry only runs 9:30-16:00 ET weekdays")
    cand = _pick_cheap_call(opt, stock, PROBE_SYMBOL)
    if not cand:
        return _fail(f"no cheap {PROBE_SYMBOL} call found in 2-7 DTE window")
    limit = round(max(0.01, cand["ask"] - 0.01), 2)
    cid = f"LB99|PROBE|{date.today().strftime('%Y%m%d')}|smoke"
    o = trade.submit_order(LimitOrderRequest(
        symbol=cand["occ"],
        qty=1,
        side=OrderSide.BUY,
        time_in_force=TimeInForce.DAY,
        limit_price=limit,
        client_order_id=cid[:48],
    ))
    print(
        f"PROBE SMOKE: submitted BUY 1x {cand['occ']} limit={limit:.2f} "
        f"(~${cand['cost']:.0f}) id={o.id}"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Paper options probe")
    parser.add_argument(
        "--smoke-entry",
        action="store_true",
        help="Place one small SPY call limit order (paper only)",
    )
    args = parser.parse_args()
    if not API_KEY or not API_SECRET:
        return _fail("set ALPACA_PAPER_KEY and ALPACA_PAPER_SECRET")
    trade = TradingClient(API_KEY, API_SECRET, paper=True)
    opt = OptionHistoricalDataClient(API_KEY, API_SECRET)
    stock = StockHistoricalDataClient(API_KEY, API_SECRET)
    try:
        rc = run_check(trade)
        if rc != 0:
            return rc
        if args.smoke_entry:
            return run_smoke_entry(trade, opt, stock)
        print("PROBE: check-only pass (use --smoke-entry to place a test order)")
        return 0
    except Exception as e:
        return _fail(str(e))


if __name__ == "__main__":
    raise SystemExit(main())
