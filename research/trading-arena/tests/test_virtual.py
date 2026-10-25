import datetime as dt
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from run_virtual import initial,run_one,UTC
from arena import PaperAccount

class AutonomousTenWorkerTests(unittest.TestCase):
    def test_ten_account_balances_and_isolation(self):
        s=initial()
        self.assertEqual(len(s),10)
        self.assertTrue(all(v["cash"]==100 and not v["events"] for v in s.values()))
    def test_missing_quotes_never_fabricate_performance(self):
        s=initial();now=dt.datetime(2026,10,25,20,tzinfo=UTC)
        r=run_one(s,{},now)
        self.assertEqual(len(r),10)
        self.assertTrue(all(not v["events"] for v in s.values()))
        self.assertTrue(all(x["equity"]==100 for x in r.values()))
    def test_tampered_worker_is_quarantined(self):
        s=initial()
        a=PaperAccount("S09")
        a.trade(timestamp="2026-10-25T20:00:00Z",asset_class="crypto",
            symbol="BTC-USD",side="BUY",qty=.0001,price=80000,
            source_id="SYNTHETIC-TEST")
        s["S09"]={"cash":a.cash,"positions":a.holdings,"events":a.events,"seen":{}}
        s["S09"]["events"][0]["price"]=20
        result=run_one(s,{},dt.datetime(2026,10,25,20,tzinfo=UTC))
        self.assertEqual(result["S09"]["action"],"QUARANTINED")
        self.assertEqual(result["S01"]["action"],"HOLD")

if __name__=="__main__":unittest.main()
