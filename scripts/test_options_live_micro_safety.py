"""Fail-closed / allocation / duplicate-entry tests for options_live_micro.

No live credentials required — broker clients are mocked.
"""
from __future__ import annotations

import os
import sys
import unittest
from datetime import datetime
from types import SimpleNamespace
from unittest.mock import MagicMock, patch
from zoneinfo import ZoneInfo

sys.path.insert(0, str(__file__).rsplit("\\", 1)[0] if "\\" in __file__ else str(__file__).rsplit("/", 1)[0])

import options_live_micro as olm  # noqa: E402

ET = ZoneInfo("America/New_York")


class ParseFlagsTests(unittest.TestCase):
    def test_entries_missing_fail_closed(self):
        self.assertFalse(olm.parse_entries_enabled(None))
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("LIVE_OPTIONS_ENTRIES", None)
            self.assertFalse(olm.parse_entries_enabled())

    def test_entries_empty_and_invalid_fail_closed(self):
        self.assertFalse(olm.parse_entries_enabled(""))
        self.assertFalse(olm.parse_entries_enabled("   "))
        self.assertFalse(olm.parse_entries_enabled("maybe"))
        self.assertFalse(olm.parse_entries_enabled("2"))
        self.assertFalse(olm.parse_entries_enabled("enabled"))

    def test_entries_explicit_on_off(self):
        self.assertTrue(olm.parse_entries_enabled("1"))
        self.assertTrue(olm.parse_entries_enabled("true"))
        self.assertTrue(olm.parse_entries_enabled("YES"))
        self.assertFalse(olm.parse_entries_enabled("0"))
        self.assertFalse(olm.parse_entries_enabled("false"))
        self.assertFalse(olm.parse_entries_enabled("off"))

    def test_max_cap_defaults_to_250(self):
        self.assertEqual(olm.parse_max_options_cap(None), 250.0)
        self.assertEqual(olm.parse_max_options_cap(""), 250.0)
        self.assertEqual(olm.parse_max_options_cap("0"), 250.0)
        self.assertEqual(olm.parse_max_options_cap("-1"), 250.0)
        self.assertEqual(olm.parse_max_options_cap("bogus"), 250.0)
        self.assertEqual(olm.parse_max_options_cap("250"), 250.0)
        self.assertEqual(olm.parse_max_options_cap("100"), 100.0)

    def test_stock_reserve_defaults_to_250(self):
        self.assertEqual(olm.parse_stock_cash_reserve(None), 250.0)
        self.assertEqual(olm.parse_stock_cash_reserve(""), 250.0)
        self.assertEqual(olm.parse_stock_cash_reserve("bad"), 250.0)
        self.assertEqual(olm.parse_stock_cash_reserve("0"), 0.0)


class AllocationTests(unittest.TestCase):
    def setUp(self):
        olm.MAX_OPTIONS_CAP = 250.0
        olm.STOCK_CASH_RESERVE = 250.0
        olm.SHARE = 0.25

    def test_options_sleeve_hard_capped(self):
        # 25% of $10k = $2500, but hard cap is $250
        self.assertEqual(olm.options_sleeve(10_000), 250.0)
        olm.MAX_OPTIONS_CAP = 250.0
        self.assertEqual(olm.options_sleeve(800), 200.0)  # 25% of 800

    def test_allocated_counts_positions_pending_reserved(self):
        trade = MagicMock()
        pos = SimpleNamespace(
            symbol="AAPL261016C00150000",
            asset_class="us_option",
            market_value="100",
            qty="1",
        )
        trade.get_all_positions.return_value = [pos]
        trade.get_orders.return_value = []
        state = {
            "lots": [{
                "strategy_id": "S404",
                "occ": "MSFT261016C00400000",
                "qty": 1,
                "entry_price": 0.50,
                "pending": True,
            }],
            "reserved_notional": 25.0,
        }
        # position $100 + pending $50 + reserved $25
        self.assertAlmostEqual(olm.allocated_options_notional(trade, state), 175.0)

    def test_partial_fill_counts_remaining_buy(self):
        trade = MagicMock()
        occ = "AAPL261016C00150000"
        pos = SimpleNamespace(
            symbol=occ, asset_class="us_option", market_value="40", qty="1",
        )
        trade.get_all_positions.return_value = [pos]
        open_buy = SimpleNamespace(
            symbol=occ, side="buy", qty="2", filled_qty="1",
            limit_price="0.55", client_order_id="OLB|20261023|abcd",
            id="ord1",
        )
        trade.get_orders.return_value = [open_buy]
        state = {
            "lots": [{
                "strategy_id": "S406",
                "occ": occ,
                "qty": 2,
                "entry_price": 0.55,
                "pending": True,
            }],
        }
        # MV 40 + remaining 1 * 0.55 * 100 = 55 → 95
        self.assertAlmostEqual(olm.allocated_options_notional(trade, state), 95.0)

    def test_entry_room_respects_stock_reserve_and_cap(self):
        trade = MagicMock()
        trade.get_all_positions.return_value = []
        trade.get_orders.return_value = []
        state: dict = {"lots": []}
        # cash 300, reserve 250 → cash room 50; sleeve 250 → room 50
        room = olm.entry_room(300.0, 2000.0, trade, state)
        self.assertAlmostEqual(room, 50.0)
        # cash at reserve → no room
        room2 = olm.entry_room(250.0, 2000.0, trade, state)
        self.assertAlmostEqual(room2, 0.0)


class DuplicateAndEntriesGateTests(unittest.TestCase):
    def setUp(self):
        olm.ENTRIES_ENABLED = False
        olm.MAX_OPTIONS_CAP = 250.0
        olm.STOCK_CASH_RESERVE = 250.0

    def test_place_disabled_returns_zero_without_scan(self):
        trade = MagicMock()
        now = datetime(2026, 10, 23, 10, 0, tzinfo=ET)
        with patch.object(olm, "scan_hits") as scan:
            n = olm.place(trade, MagicMock(), MagicMock(), MagicMock(),
                          2000.0, 500.0, {"lots": []}, now)
        self.assertEqual(n, 0)
        scan.assert_not_called()

    def test_place_skips_already_used_strategy(self):
        olm.ENTRIES_ENABLED = True
        trade = MagicMock()
        trade.get_all_positions.return_value = []
        trade.get_orders.return_value = []
        now = datetime(2026, 10, 23, 10, 0, tzinfo=ET)
        hit = SimpleNamespace(
            strategy_id="S404", symbol="AAPL", price=150.0, detail="gap",
        )
        state = {
            "used_day": now.date().isoformat(),
            "used_strategies": ["S404"],
            "lots": [],
        }
        with patch.object(olm, "scan_hits", return_value=[hit]):
            with patch.object(olm, "_allow_strats", return_value=[
                SimpleNamespace(id="S404", dte_min=1, dte_max=7, dte_target=3),
            ]):
                n = olm.place(trade, MagicMock(), MagicMock(), MagicMock(),
                              2000.0, 500.0, state, now)
        self.assertEqual(n, 0)
        trade.submit_order.assert_not_called()

    def test_mark_before_submit_blocks_retry(self):
        """Even if submit raises, strategy is marked used (no duplicate retry)."""
        olm.ENTRIES_ENABLED = True
        trade = MagicMock()
        trade.get_all_positions.return_value = []
        trade.get_orders.return_value = []
        trade.submit_order.side_effect = RuntimeError("broker down")
        now = datetime(2026, 10, 23, 10, 0, tzinfo=ET)
        hit = SimpleNamespace(
            strategy_id="S404", symbol="AAPL", price=150.0, detail="gap",
        )
        state = {"lots": [], "used_day": now.date().isoformat(), "used_strategies": []}
        arm = MagicMock(
            max_premium=75.0, take_profit=0.5, stop_loss=-0.4,
            buy_limit_offset=-0.01,
        )
        cand = {
            "symbol": "AAPL261016C00150000", "bid": 0.50, "ask": 0.55,
            "mid": 0.52, "cost": 54.0,
        }
        with patch.object(olm, "scan_hits", return_value=[hit]), \
             patch.object(olm, "_allow_strats", return_value=[
                 SimpleNamespace(id="S404", dte_min=1, dte_max=7, dte_target=3),
             ]), \
             patch.object(olm, "make_arm", return_value=arm), \
             patch.object(olm, "_strat", return_value=SimpleNamespace(
                 id="S404", dte_min=1, dte_max=7, dte_target=3,
             )), \
             patch.object(olm.om, "_pick_option_from_chain", return_value=cand), \
             patch.object(olm, "entry_limit_price", return_value=0.54), \
             patch.object(olm, "save_state"), \
             patch.object(olm, "append_ledger"):
            n = olm.place(trade, MagicMock(), MagicMock(), MagicMock(),
                          2000.0, 500.0, state, now)
        self.assertEqual(n, 0)
        self.assertIn("S404", state.get("used_strategies", []))


class ManageStillRunsWhenEntriesOff(unittest.TestCase):
    def test_run_calls_manage_when_entries_disabled(self):
        olm.ENTRIES_ENABLED = False
        with patch.object(olm, "API_KEY", "k"), \
             patch.object(olm, "API_SECRET", "s"), \
             patch.object(olm, "reload_live_flags_from_env"), \
             patch.object(olm, "_now", return_value=datetime(2026, 10, 23, 10, 30, tzinfo=ET)), \
             patch.object(olm, "TradingClient") as TC, \
             patch.object(olm, "OptionHistoricalDataClient"), \
             patch.object(olm, "StockHistoricalDataClient"), \
             patch.object(olm, "make_trading_client"), \
             patch.object(olm, "load_state", return_value={"lots": []}), \
             patch.object(olm, "reconcile", side_effect=lambda t, s, n: s), \
             patch.object(olm, "manage") as manage, \
             patch.object(olm, "ensure_stops"), \
             patch.object(olm, "place") as place, \
             patch.object(olm, "_cancel_stale_exit_sells"), \
             patch.object(olm, "option_positions", return_value=[]), \
             patch.object(olm, "active_lots", return_value=[]):
            acct = SimpleNamespace(
                equity="1000", cash="500", account_number="X",
                options_trading_level=2,
            )
            TC.return_value.get_account.return_value = acct
            # Force entries flag off inside run after reload is no-op
            olm.ENTRIES_ENABLED = False
            rc = olm.run()
        self.assertEqual(rc, 0)
        manage.assert_called()
        place.assert_called()  # place itself no-ops when disabled

    def test_broker_unavailable_returns_zero(self):
        with patch.object(olm, "API_KEY", "k"), \
             patch.object(olm, "API_SECRET", "s"), \
             patch.object(olm, "reload_live_flags_from_env"), \
             patch.object(olm, "_now", return_value=datetime(2026, 10, 23, 10, 30, tzinfo=ET)), \
             patch.object(olm, "TradingClient", side_effect=RuntimeError("no network")):
            rc = olm.run()
        self.assertEqual(rc, 0)


if __name__ == "__main__":
    unittest.main()
