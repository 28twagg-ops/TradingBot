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
    def test_three_independent_specialist_votes(self):
        import tempfile,json
        from pathlib import Path
        with tempfile.TemporaryDirectory() as d:
            Path(d,"groq_research.json").write_text(json.dumps([{"worker":"S01",
                "topic":"volatility filter","status":"RESEARCHED",
                "test":{"retrospective_validation":{"returns_pct":-2.3}}}]))
            calls=[]
            def fake(role,payload):
                calls.append(role)
                return {"verdict":"NEEDS_MORE_EVIDENCE",
                        "finding":"No independent executable fills",
                        "requested_check":"Collect forward price data"}
            result=special_review(d,fake)
            self.assertEqual(result["provider_requests"],3)
            self.assertEqual(len(result["judges"]),3)
            self.assertEqual(result["paper_promotions"],0)
            self.assertEqual(result["live_trading_authorized"],False)
            self.assertEqual(len(set(calls)),3)

if __name__=="__main__":unittest.main()
