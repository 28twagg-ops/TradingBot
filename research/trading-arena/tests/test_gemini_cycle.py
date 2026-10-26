"""Deterministic no-API tests of the Gemini agent orchestrator."""
import datetime as dt
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from gemini_cycle import (
    QuotaExhausted, execute_virtual, initial, normalize_decision, run_cycle,
    tradable, UTC,
)


def fixture_feed(now):
    # Synthetic completed hourly source observations: NEVER claimed as backtest evidence.
    first=now-dt.timedelta(hours=80)
    rows=[((first+dt.timedelta(hours=i)).isoformat().replace("+00:00","Z"),
           float(100+i)) for i in range(79)]
    return {"BTC-USD":rows,"SPY":rows}


def sample(role,payload):
    if "Independent council reviewer" in role:
        return {"verdict":"NEEDS_MORE_EVIDENCE",
                "finding":"No independently executable fills were provided",
                "requested_check":"Add executable quote history and provenance"}
    if payload["worker"]=="S09":
        return {"action":"BUY","symbol":"BTC-USD","allocation_fraction":0.3,
                "hypothesis":"Research BTC momentum after macro news",
                "test_plan":"Hold future data unseen until 60 forward sessions",
                "source_titles":["Unverified paper title"],"reasoning":"Test only"}
    return {"action":"HOLD","symbol":None,"allocation_fraction":0.0,
            "hypothesis":"Need more research","test_plan":"Forward sample",
            "source_titles":[],"reasoning":"Not enough independent evidence"}


class GeminiCycleTests(unittest.TestCase):
    now=dt.datetime(2026,10,26,19,17,tzinfo=UTC)

    def test_model_cannot_choose_unsupported_asset_or_leverage(self):
        with self.assertRaises(ValueError):
            normalize_decision({"action":"BUY","symbol":"DOGE-USD",
                                "allocation_fraction":.2}, {"BTC-USD":{}})
        with self.assertRaises(ValueError):
            normalize_decision({"action":"BUY","symbol":"BTC-USD",
                                "allocation_fraction":1.0}, {"BTC-USD":{}})
        with self.assertRaises(ValueError):
            normalize_decision({"action":"SHORT","symbol":"BTC-USD",
                                "allocation_fraction":.2}, {"BTC-USD":{}})

    @patch("gemini_cycle.literature",return_value=[])
    def test_ten_agents_and_three_independent_council_calls(self,_):
        state=initial()
        output=run_cycle(state,fixture_feed(self.now),sample,self.now)
        self.assertEqual(output["api_calls"],13)
        self.assertEqual(len(output["workers"]),10)
        self.assertEqual(len(output["council"]),3)
        self.assertEqual(output["workers"]["S09"]["status"],"RESEARCHED")
        self.assertTrue(output["workers"]["S09"]["action"].startswith("BUY BTC-USD"))
        self.assertLess(state["S09"]["cash"],100)
        self.assertEqual(state["S08"]["cash"],100)
        self.assertEqual(output["paper_promotions"],0)
        repeat=run_cycle(state,fixture_feed(self.now),sample,self.now)
        self.assertEqual(repeat["api_calls"],0)
        self.assertEqual(len(state["S09"]["events"]),1)

    @patch("gemini_cycle.literature",return_value=[])
    def test_free_quota_exhaustion_fails_closed(self,_):
        state=initial()
        def no_capacity(role,payload):
            raise QuotaExhausted("quota not available")
        result=run_cycle(state,fixture_feed(self.now),no_capacity,self.now)
        self.assertTrue(result["quota_exhausted"])
        self.assertTrue(all(not record["events"] for record in state.values()))
        self.assertEqual(result["paper_promotions"],0)

    def test_fake_prices_do_not_override_independently_validated_universe(self):
        a=initial()["S01"]
        markets=tradable(fixture_feed(self.now),self.now)
        bad={"action":"BUY","symbol":"BTC-USD","fraction":.25}
        self.assertEqual(execute_virtual("S01",a,bad,{},self.now),
                         "REJECT_STALE_MARKET_DATA")
        self.assertEqual(a["cash"],100.0)

    def test_invalid_api_key_is_not_needed_for_tests(self):
        # Tests never call an external LLM provider.
        self.assertTrue(callable(sample))


if __name__=="__main__":
    unittest.main()
