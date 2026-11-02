"""Contract tests for the independent, research-only daily-bar validator."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"simulations"))
from validate_rubber_band import signals, simulate, stats

def bar(date, op, hi, lo, cl):
    return {"date":date,"Open":op,"High":hi,"Low":lo,"Close":cl,"Volume":1000}

class ValidationTests(unittest.TestCase):
    def fixture(self):
        b=[bar(f"2020-01-{i:02d}",100,101,99,100) for i in range(1,22)]
        # Day 21 signal: gap down from 100, close above intraday midpoint
        b[-1]=bar("2020-01-21",98,101,96,100)
        b.extend([bar("2020-01-22",102,105,101,104),
                  bar("2020-01-23",104,106,103,105),
                  bar("2020-01-24",105,107,104,106)])
        return b
    def test_entry_is_after_signal_close(self):
        b=self.fixture()
        self.assertEqual(list(signals(b)),[20])
        t=simulate({"TEST":b},0,0,2,0,500,"2020-01-23")
        self.assertEqual(len(t),1)
        self.assertEqual(t[0]["signal_date"],"2020-01-21")
        self.assertEqual(t[0]["entry_date"],"2020-01-22")
        self.assertEqual(t[0]["entry_price"],102)
        self.assertEqual(t[0]["period"],"in_sample")
    def test_costs_reduce_returns(self):
        b=self.fixture()
        ideal=simulate({"TEST":b},0,0,2,0,500,"2020-01-01")[0]
        harsh=simulate({"TEST":b},30,2,2,0,500,"2020-01-01")[0]
        self.assertLess(harsh["net_pnl_per_share"],ideal["net_pnl_per_share"])
    def test_gap_stop_fills_at_open_not_stop(self):
        b=self.fixture()
        b[22]=bar("2020-01-23",90,91,89,90)
        t=simulate({"TEST":b},0,0,2,.05,500,"2020-01-01")[0]
        self.assertEqual(t["reason"],"gap_stop")
        self.assertEqual(t["exit_price"],90)
    def test_missing_data_not_success(self):
        self.assertEqual(stats([])["status"],"INSUFFICIENT_DATA")
if __name__=="__main__":unittest.main()
