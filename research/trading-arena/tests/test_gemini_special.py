"""No-key council tests. Never calls Gemini while running GitHub CI."""
import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from gemini_special import special_review

class GeminiSpecialTests(unittest.TestCase):
    def test_no_research_means_no_ai_requests(self):
        import tempfile
        with tempfile.TemporaryDirectory() as t:
            def forbidden(*args,**kwargs):
                self.fail("Gemini should not be called without research")
            result=special_review(t,forbidden)
            self.assertEqual(result["provider_requests"],0)
    def test_gemini_reviews_local_llama_even_if_groq_has_no_results(self):
        import tempfile,json
        from pathlib import Path
        with tempfile.TemporaryDirectory() as d:
            source=Path(d,"local_research","2026-10-31")
            source.mkdir(parents=True)
            source.joinpath("S07_"+"a"*32+".json").write_text(json.dumps({
                "kind":"local_research_only","research_only":True,
                "live_trading":False,"event_id":"a"*32,"worker":"S07",
                "cycle":"2026-10-31T05:00Z","model":"llama3.2:3b",
                "event":{"status":"RESEARCH_IDEA_NEEDS_DATA","action":"HOLD"},
                "experiment":{"topic":"Unverified idea","hypothesis":"Test a hypothesis"}
            }))
            observed=[]
            def reviewer(role,payload):
                observed.append(payload)
                return {"verdict":"NEEDS_MORE_EVIDENCE",
                        "finding":"Independent validation missing",
                        "requested_check":"Run a fresh holdout"}
            r=special_review(d,reviewer)
            self.assertEqual(r["provider_requests"],3)
            self.assertEqual(r["source_counts"]["local_llama"],1)
            self.assertEqual(r["source_counts"]["groq"],0)
            self.assertEqual(observed[0]["local_llama_unverified_hypotheses"][0]["worker"],"S07")
            self.assertFalse(r["live_trading_authorized"])

    def test_three_independent_specialist_votes(self):
        import tempfile,json
        from pathlib import Path
        with tempfile.TemporaryDirectory() as d:
            Path(d,"groq_research.json").write_text(json.dumps([{"worker":"S01",
                "topic":"volatility filter","status":"RESEARCHED",
                "test":{"retrospective_validation":{"returns_pct":-2.3}}}]))
            calls=[]
            payloads=[]
            def fake(role,payload):
                calls.append(role)
                payloads.append(payload)
                return {"verdict":"NEEDS_MORE_EVIDENCE",
                        "finding":"No independent executable fills",
                        "requested_check":"Collect forward price data"}
            result=special_review(d,fake)
            self.assertEqual(result["provider_requests"],3)
            self.assertEqual(len(result["judges"]),3)
            self.assertEqual(result["paper_promotions"],0)
            self.assertEqual(result["live_trading_authorized"],False)
            self.assertEqual(len(set(calls)),3)
            self.assertEqual(result["source_counts"]["groq"],1)
            self.assertEqual(result["source_counts"]["local_llama"],0)

if __name__=="__main__":unittest.main()
