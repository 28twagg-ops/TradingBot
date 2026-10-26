"""API-free tests of rotating Groq research agents and non-executable backtests."""
import datetime as dt
import sys
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from groq_research import backtest, strategy_spec, one_turn, choose_due_workers, MAX_GROQ_REQUESTS_PER_UTC_DAY
from run_virtual import initial, UTC

def synthetic_feed(now):
    first=now-dt.timedelta(hours=140)
    # 139 completed hourly bars, each strictly older than UTC now.
    bars=[((first+dt.timedelta(hours=i)).isoformat().replace("+00:00","Z"),
           100.+i*.3) for i in range(139)]
    return {"BTC-USD":bars,"SPY":bars}

class GroqResearchTests(unittest.TestCase):
    now=dt.datetime(2026,10,26,20,40,tzinfo=UTC)
    def test_reject_arbitrary_generated_code_and_invalid_specs(self):
        for candidate in ({"family":"shell","lookback":10,"threshold":.01},
                          {"family":"trend","lookback":-1,"threshold":0},
                          {"family":"trend","lookback":20,"threshold":float("nan")},
                          {"family":"trend","lookback":300,"threshold":.01}):
            with self.assertRaises(ValueError):
                strategy_spec({"candidate":candidate})
    def test_historical_tests_use_only_delayed_close_proxy(self):
        bar=synthetic_feed(self.now)["BTC-USD"]
        a=backtest(bar,{"family":"trend","lookback":12,"threshold":.001})
        self.assertEqual(a["status"],"HISTORICAL_PROXY_ONLY")
        self.assertGreaterEqual(a["research"]["entries"],0)
        self.assertIn("retrospective_validation",a)
    @patch("groq_research.tradable")
    def test_independent_agent_research_uses_mock_api_and_persists(self,tradable):
        feed=synthetic_feed(self.now)
        tradable.return_value={"BTC-USD":{"source_time":feed["BTC-USD"][-1][0],
                        "indicative_price":feed["BTC-USD"][-1][1]}}
        accounts=initial()
        calls=[]
        def fake_model(policy,context):
            calls.append(context)
            return {"research_topic":"original crypto trend/volatility hybrid",
                "hypothesis":"Falsify trend persistence under spreads",
                "candidate":{"family":"trend","lookback":12,"threshold":.001},
                "study_symbol":"BTC-USD","action":"HOLD","symbol":None,
                "allocation_fraction":0,"reason":"research before trading",
                "falsification_test":"Compare next 60 future closes"}
        with patch("groq_research.tradable",tradable), patch("groq_research.literature",return_value=[]):
            event=one_turn(accounts,feed,fake_model,self.now)
        self.assertEqual(event["status"],"RESEARCHED")
        self.assertEqual(len(calls),1)
        self.assertIn("eligible_symbols",calls[0])
        self.assertEqual(event["test"]["status"],"HISTORICAL_PROXY_ONLY")
        self.assertEqual(sum(len(x["events"]) for x in accounts.values()),0)
        again=one_turn(accounts,feed,fake_model,self.now)
        self.assertEqual(again["status"],"ALREADY_EVALUATED")
        self.assertEqual(len(calls),1)
    def test_bad_ledger_is_quarantined_pre_inference(self):
        accounts=initial()
        now=self.now
        target=int(now.timestamp()//1800)%10
        wid=f"S{target+1:02d}"
        accounts[wid]["cash"]=-5
        event=one_turn(accounts,synthetic_feed(now),lambda *_:self.fail("Provider should not be called"),now)
        self.assertEqual(event["status"],"QUARANTINED_BAD_BALANCE")
    def test_missed_scheduled_runs_prioritize_all_ten_accounts(self):
        accounts=initial()
        past=[{"worker":"S04","cycle":"2026-10-26T03:59Z","status":"RESEARCHED"},
              {"worker":"S05","cycle":"2026-10-26T04:01Z","status":"RESEARCHED"},
              {"worker":"S07","cycle":"2026-10-26T10:01Z","status":"RESEARCHED"}]
        first=choose_due_workers(accounts,past,self.now,5)
        self.assertEqual(first,["S01","S02","S03","S06","S08"])
        for wid in first:
            past.append({"worker":wid,"cycle":"2026-10-26T20:41Z","status":"RESEARCHED"})
        second=choose_due_workers(accounts,past,self.now,5)
        self.assertEqual(set(second),{"S04","S05","S07","S09","S10"})
        self.assertFalse(set(first).intersection(second))

    def test_explicit_target_worker_and_batch_bounds(self):
        accounts=initial()
        with self.assertRaises(ValueError):
            choose_due_workers(accounts,[],self.now,6)
        with self.assertRaises(ValueError):
            one_turn(accounts,synthetic_feed(self.now),
                     lambda *_:self.fail("Unknown worker must not invoke model"),
                     self.now,worker_id="S99")
        self.assertEqual(MAX_GROQ_REQUESTS_PER_UTC_DAY,40)

    def test_no_live_order_functions_exist(self):
        import groq_research
        self.assertFalse(hasattr(groq_research,"place_live_order"))

if __name__=="__main__":unittest.main()
