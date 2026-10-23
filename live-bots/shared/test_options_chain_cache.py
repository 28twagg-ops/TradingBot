"""Unit tests for pick_atm_call chain/OI cache fallback (no Alpaca credentials)."""
from __future__ import annotations

import sys
import unittest
from datetime import date
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parent))

import options_morning_bot as bot  # noqa: E402
from options_lab import EffectiveArm  # noqa: E402


def _fake_chain(bid=1.0, ask=1.1):
    sym = "AVGO260710C00400000"
    snap = SimpleNamespace(latest_quote=SimpleNamespace(bid_price=bid, ask_price=ask))
    return {sym: snap}


def _arm():
    return EffectiveArm(
        bucket_id=0,
        profile_name="test",
        strategy_id="S173",
        buy_limit_offset=-0.01,
        max_premium=500.0,
        max_spread_frac=0.25,
        min_open_interest=0,
        market_exit_eod=False,
    )


class PickAtmCallCacheTests(unittest.TestCase):
    def setUp(self):
        self.opt = MagicMock()
        self.ref = MagicMock()
        self.arm = _arm()

    @patch.object(bot, "TODAY", date(2026, 7, 7))
    @patch.object(bot, "rl_file")
    @patch.object(bot, "_fetch_oi_map", return_value={})
    @patch.object(bot, "_fetch_option_chain")
    def test_cache_hit_skips_api(self, mock_chain, _mock_oi, _rl):
        cached = _fake_chain()
        chain_cache = {("AVGO", 3, 7, 360.0, 440.0): cached}
        result = bot.pick_atm_call(
            self.opt, self.ref, "AVGO", 400.0, 3, 7, 5, self.arm,
            chain_cache=chain_cache, oi_cache={},
        )
        mock_chain.assert_not_called()
        self.assertIsNotNone(result)
        self.assertEqual(result["symbol"], "AVGO260710C00400000")

    @patch.object(bot, "TODAY", date(2026, 7, 7))
    @patch.object(bot, "rl_file")
    @patch.object(bot, "_fetch_oi_map", return_value={})
    @patch.object(bot, "_fetch_option_chain")
    def test_empty_cache_refreshes(self, mock_chain, _mock_oi, _rl):
        mock_chain.return_value = _fake_chain()
        chain_cache = {("AVGO", 3, 7, 360.0, 440.0): {}}
        bot.pick_atm_call(
            self.opt, self.ref, "AVGO", 400.0, 3, 7, 5, self.arm,
            chain_cache=chain_cache, oi_cache={},
        )
        mock_chain.assert_called_once()

    @patch.object(bot, "TODAY", date(2026, 7, 7))
    @patch.object(bot, "rl_file")
    @patch.object(bot, "_fetch_oi_map", return_value={})
    @patch.object(bot, "_fetch_option_chain")
    def test_api_error_retries_uncached(self, mock_chain, _mock_oi, _rl):
        mock_chain.side_effect = [RuntimeError("rate limit"), _fake_chain()]
        result = bot.pick_atm_call(
            self.opt, self.ref, "AVGO", 400.0, 3, 7, 5, self.arm,
            chain_cache={}, oi_cache={},
        )
        self.assertEqual(mock_chain.call_count, 2)
        self.assertIsNotNone(result)

    @patch.object(bot, "TODAY", date(2026, 7, 7))
    @patch.object(bot, "rl_file")
    @patch.object(bot, "_fetch_oi_map")
    @patch.object(bot, "_fetch_option_chain", return_value=_fake_chain())
    def test_oi_error_retries(self, _mock_chain, mock_oi, _rl):
        mock_oi.side_effect = [RuntimeError("oi down"), {}]
        result = bot.pick_atm_call(
            self.opt, self.ref, "AVGO", 400.0, 3, 7, 5, self.arm,
            chain_cache={}, oi_cache={},
        )
        self.assertEqual(mock_oi.call_count, 2)
        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()
