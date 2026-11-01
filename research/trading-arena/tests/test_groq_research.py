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
                "falsification_test":"Compare next 60 future closes",
                "next_search_query":"alternative models on forums",
                "preferred_sources":["reddit","youtube","github"],
                "site_domain":None,
                "research_data_requirements":["hourly_close"],
                "hypothesis_timeframe":"hourly",
                "rule_expressible_as_candidate":True,
                "source_indices":[0]}
        with patch("groq_research.tradable",tradable), patch("groq_research.discover",
                return_value={"query":"example","attempted":["web"],"found":[
                    {"platform":"reddit","title":"An unpopular trade idea",
                     "url":"https://www.reddit.com/r/algotrading/comments/example",
                     "snippet":"unverified hypothesis","read_level":"public_search_result_only"}]}):
            event=one_turn(accounts,feed,fake_model,self.now,local_leads=[{
                "source":"UNVERIFIED_LOCAL_LLAMA_RESEARCH_ONLY",
                "worker":"S01","hypothesis":"No trade until out-of-sample validation"}])
        self.assertEqual(event["status"],"RESEARCHED")
        self.assertEqual(len(calls),1)
        self.assertIn("eligible_symbols",calls[0])
        self.assertEqual(len(calls[0]["local_llama_hypotheses_untrusted"]),1)
        self.assertTrue(calls[0]["local_ideas_are_only_leads"])
        self.assertEqual(event["sources_found"],1)
        self.assertEqual(event["source_leads"][0]["platform"],"reddit")
        self.assertEqual(accounts[event["worker"]]["groq_experiments"][0]["next_search_query"],
                         "alternative models on forums")
        self.assertEqual(event["test"]["status"],"HISTORICAL_PROXY_ONLY")
        self.assertEqual(sum(len(x["events"]) for x in accounts.values()),0)
        again=one_turn(accounts,feed,fake_model,self.now)
        self.assertEqual(again["status"],"ALREADY_EVALUATED")
        self.assertEqual(len(calls),1)
    def test_agent_can_investigate_unavailable_data_without_fake_backtest_or_trade(self):
        accounts=initial()
        feed=synthetic_feed(self.now)
        def agent(policy,context):
            return {"research_topic":"TikTok price microstructure hypothesis",
                "hypothesis":"5 minute orderbook imbalance predicts next candle",
                "candidate":{"family":"breakout","lookback":8,"threshold":.01},
                "study_symbol":"BTC-USD","action":"BUY","symbol":"BTC-USD",
                "allocation_fraction":.3,"reason":"platform tip",
                "falsification_test":"Compare signed imbalances to future returns",
                "next_search_query":"BTC order flow TikTok strategy",
                "preferred_sources":["tiktok","reddit","github"],
                "site_domain":"example.com",
                "research_data_requirements":["minute_bars","order_book"],
                "hypothesis_timeframe":"minute",
                "rule_expressible_as_candidate":False,
                "source_indices":[]}
        with patch("groq_research.discover",return_value={
            "query":"BTC orderflow","attempted":["tiktok"],"found":[]}):
            result=one_turn(accounts,feed,agent,self.now,worker_id="S10")
        self.assertEqual(result["status"],"RESEARCH_IDEA_NEEDS_DATA")
        self.assertEqual(result["action"],"RESEARCH_ONLY_NEEDS_DATA")
        self.assertEqual(result["test"]["status"],"PENDING_PROPER_HISTORICAL_DATA")
        self.assertEqual(accounts["S10"]["groq_experiments"][0]["preferred_sources"],
                         ["tiktok","reddit","github"])
        self.assertEqual(accounts["S10"]["cash"],100)
        self.assertEqual(accounts["S10"]["events"],[])

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
            past.append({"worker":wid,"cycle":"2026-10-26T20:39Z","status":"RESEARCHED"})
        second=choose_due_workers(accounts,past,self.now+dt.timedelta(hours=1),5)
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
        self.assertEqual(MAX_GROQ_REQUESTS_PER_UTC_DAY,72)

    def test_s07_invalid_candidate_is_saved_for_research_but_never_traded(self):
        from personas import PERSONAS
        self.assertEqual(len(PERSONAS),10)
        self.assertEqual(len({p["name"] for p in PERSONAS.values()}),10)
        accounts=initial()
        seen=[]
        def poorly_formatted_bot(policy,context):
            seen.append(context)
            return {"research_topic":"Test unverified trend idea",
                    "hypothesis":"A novel market trend should persist, unless costs erase it",
                    "candidate":{"family":"trend","lookback":900,"threshold":.5},
                    "study_symbol":"BTC-USD","action":"BUY","symbol":"BTC-USD",
                    "allocation_fraction":.3,"reason":"preliminary",
                    "falsification_test":"Test unseen later data",
                    "next_search_query":"trend regime shift research",
                    "preferred_sources":["academic","blog"],"site_domain":None,
                    "research_data_requirements":["hourly_close"],
                    "hypothesis_timeframe":"hourly",
                    "rule_expressible_as_candidate":True,"source_indices":[]}
        with patch("groq_research.discover",return_value={
                "query":"test","attempted":[],"found":[]}), patch(
                "groq_research.tradable",return_value={}):
            event=one_turn(accounts,synthetic_feed(self.now),poorly_formatted_bot,
                           self.now,worker_id="S07")
        self.assertEqual(event["status"],"RESEARCH_IDEA_NEEDS_REVISION")
        self.assertEqual(event["validation_issue"],"INVALID_EXECUTABLE_CANDIDATE")
        self.assertEqual(event["action"],"RESEARCH_ONLY_NEEDS_REVISION")
        self.assertEqual(accounts["S07"]["cash"],100)
        self.assertEqual(accounts["S07"]["events"],[])
        self.assertEqual(len(accounts["S07"]["groq_experiments"]),1)
        self.assertEqual(seen[0]["research_personality"]["name"],"Patient Trend Pilot")
        self.assertTrue(seen[0]["personality_is_not_a_constraint"])

    def test_groq_uses_json_object_with_safe_local_validation(self):
        import io,json,os
        from groq_research import groq_json,groq_error_category,bounded_json_context
        payload={"idea":"value","untrusted_search_results":[
            {"title":"example","snippet":"x"*9000,"platform":"web"}]}
        bounded=bounded_json_context(payload)
        self.assertLessEqual(len(bounded),7200)
        self.assertIsInstance(json.loads(bounded),dict)
        response=io.BytesIO(json.dumps({"choices":[{"message":{
            "content":json.dumps({"research_topic":"mock"})}}]}).encode())
        response.headers={}
        captured={}
        def no_network(request,timeout):
            captured["body"]=json.loads(request.data)
            return response
        with patch.dict(os.environ,{"GROQ_API_KEY":"test-only-key"}),patch(
                "groq_research.urllib.request.urlopen",side_effect=no_network):
            self.assertEqual(groq_json("Research only",{"worker":"S07"}),
                             {"research_topic":"mock"})
        self.assertEqual(captured["body"]["response_format"],{"type":"json_object"})
        self.assertEqual(captured["body"]["reasoning_effort"],"low")
        self.assertEqual(groq_error_category({
            "message":"Generated JSON does not match the expected schema."}),
            "JSON_VALIDATION")
        self.assertEqual(groq_error_category({"message":"secret arbitrary output"}),
                         "UNCLASSIFIED")

    def test_no_live_order_functions_exist(self):
        import groq_research
        self.assertFalse(hasattr(groq_research,"place_live_order"))

if __name__=="__main__":unittest.main()
