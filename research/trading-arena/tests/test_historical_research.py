"""Offline historical-research regression tests."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from historical_research import simulate, research

class HistoricalResearchTests(unittest.TestCase):
    def test_next_open_prevents_same_close_fill(self):
        closes = [100.] * 100 + [200.] * 20
        opens = [100.] * 100 + [300.] * 20
        # S02a trend: buy only after previous close has moved above averages.
        result = simulate(closes, opens, "S02", 0, 95, 120)
        self.assertGreater(result["fills"], 0)
        self.assertLess(result["net_return_pct"], 0)
    def test_costs_reduce_return(self):
        closes = [100.] * 110 + [120.] * 20
        opens = [100.] * 110 + [120.] * 20
        free = simulate(closes, opens, "S02", 0, 95, 130, fee=0)
        costly = simulate(closes, opens, "S02", 0, 95, 130, fee=.01)
        self.assertLessEqual(costly["net_return_pct"], free["net_return_pct"])
    def test_short_history_rejected(self):
        self.assertEqual(research("SPY", [100.]*200, [100.]*200, "S01", 0, 1)["status"],
                         "INSUFFICIENT_HISTORY")
    def test_bad_prices_rejected(self):
        with self.assertRaises(ValueError):
            simulate([100.]*100 + [float("nan")], [100.]*101, "S01", 0, 90, 101)

if __name__ == "__main__":
    unittest.main()
