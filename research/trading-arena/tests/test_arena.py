import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from arena import PaperAccount, council


class PaperArenaTests(unittest.TestCase):
    t = "2026-10-25T12:00:00Z"
    def transact(self, acc, asset="crypto", sym="BTC/USD", side="BUY",
                 qty=.0001, price=50000, fee=0):
        return acc.trade(timestamp=self.t, asset_class=asset, symbol=sym,
                         side=side, qty=qty, price=price, fee=fee,
                         source_id="TEST-SYNTHETIC")

    def test_all_workers_start_equal_and_isolated(self):
        a, b = PaperAccount("S01"), PaperAccount("S02")
        self.assertEqual(a.cash, 100)
        self.assertEqual(b.cash, 100)
        self.transact(a)
        self.assertEqual(a.cash, 95)
        self.assertEqual(b.cash, 100)

    def test_fails_closed_on_insufficient_cash(self):
        a = PaperAccount("S01")
        with self.assertRaises(ValueError):
            self.transact(a, qty=.01)

    def test_whole_options_contract_and_multiplier(self):
        a = PaperAccount("S10")
        with self.assertRaises(ValueError):
            self.transact(a,"us_option_long","SPY261120C00600000",qty=.5,price=.2)
        self.transact(a,"us_option_long","SPY261120C00600000",qty=1,price=.5)
        self.assertEqual(a.cash,50)
        with self.assertRaises(ValueError):
            self.transact(a,"us_option_long","SPY261120C00600000",qty=1,price=1)
        self.transact(a,"us_option_long","SPY261120C00600000",side="SELL",qty=1,price=.75)
        self.assertEqual(a.cash,125)

    def test_naked_options_and_short_crypto_forbidden(self):
        a = PaperAccount("S01")
        with self.assertRaises(ValueError):
            self.transact(a,side="SELL")

    def test_council_rejects_tampered_ledger(self):
        a = PaperAccount("S01")
        self.transact(a)
        s = a.statement()
        s["events"][0]["price"] = 1
        self.assertEqual(council(s)["status"], "REJECT_AND_QUARANTINE")

    def test_council_demands_independent_evidence(self):
        a = PaperAccount("S01")
        self.transact(a)
        self.assertEqual(council(a.statement())["status"], "REVIEW_REQUIRED")
        checked = council(a.statement(), {"TEST-SYNTHETIC": {
            "symbol":"BTC/USD", "asset_class":"crypto",
            "timestamp":self.t, "execution_price":50000}})
        self.assertEqual(checked["status"],"AUDIT_PASSED")

    def test_council_rejects_source_discrepancy(self):
        a = PaperAccount("S01")
        self.transact(a)
        result = council(a.statement(),{"TEST-SYNTHETIC":{
            "symbol":"ETH/USD", "asset_class":"crypto",
            "timestamp":self.t,"execution_price":50000}})
        self.assertEqual(result["status"],"REJECT_AND_QUARANTINE")


if __name__ == "__main__":
    unittest.main()
