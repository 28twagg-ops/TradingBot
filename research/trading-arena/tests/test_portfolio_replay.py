"""Offline deterministic portfolio replay tests; no Yahoo or broker calls."""
import datetime as dt
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from portfolio_replay import replay, compare_all

UTC = dt.timezone.utc

def series(symbol, n=360, spike=False):
    start = dt.datetime(2026, 1, 1, tzinfo=UTC)
    output = []
    for i in range(n):
        value = 100. + (i * .2 if spike else 0.)
        output.append((start + dt.timedelta(hours=i), value, value))
    return output

class PortfolioReplayTests(unittest.TestCase):
    def test_all_ten_workers_included(self):
        registry = {"workers": {"S%02d" % i: {"index": 0} for i in range(1, 11)}}
        result = compare_all({"BTC-USD": series("BTC-USD")}, registry)
        self.assertEqual(set(result), set(registry["workers"]))
        self.assertEqual(result["S09"]["status"], "RESEARCH_ONLY_NO_PROMOTION")
    def test_crypto_only_worker_does_not_trade_equities(self):
        with self.assertRaisesRegex(ValueError, "NO_ELIGIBLE_BARS"):
            replay("S09", 0, {"SPY": series("SPY")})
    def test_no_market_data_rejected(self):
        with self.assertRaisesRegex(ValueError, "NO_ELIGIBLE_BARS"):
            replay("S01", 0, {})
    def test_naive_timestamps_rejected(self):
        rows = series("BTC-USD")
        rows[0] = (rows[0][0].replace(tzinfo=None), 100., 100.)
        with self.assertRaisesRegex(ValueError, "NAIVE_TIMESTAMP"):
            replay("S01", 0, {"BTC-USD": rows})
    def test_non_monotonic_bars_rejected(self):
        rows = series("BTC-USD")
        rows[2] = rows[1]
        with self.assertRaisesRegex(ValueError, "NON_MONOTONIC_BARS"):
            replay("S01", 0, {"BTC-USD": rows})
    def test_replay_is_deterministic(self):
        bars = {"BTC-USD": series("BTC-USD", spike=True)}
        self.assertEqual(replay("S01", 0, bars), replay("S01", 0, bars))
    def test_unsupported_worker_rejected(self):
        with self.assertRaisesRegex(ValueError, "UNKNOWN_WORKER"):
            replay("S11", 0, {"BTC-USD": series("BTC-USD")})

if __name__ == "__main__":
    unittest.main()
