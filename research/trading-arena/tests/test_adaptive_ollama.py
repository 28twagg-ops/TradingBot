"""No-network tests for adaptive local inference, evidence mentorship and live gates."""
import datetime as dt
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from local_adaptive import AdaptiveRouter, BASE, STRONG, score, format_report
from mentor_planner import plan
from approval_readiness import readiness
from local_ollama import OllamaResearch
from run_virtual import UTC


def hardware(free=12.0, cpu=20.0):
    return {"free_ram_gb": free, "total_ram_gb": 32, "cpu_percent": cpu}


class AdaptiveLocalTests(unittest.TestCase):
    def test_large_model_canary_after_stable_baseline_then_auto_fallback(self):
        with tempfile.TemporaryDirectory() as root:
            r = AdaptiveRouter(root, [BASE, STRONG], sample_hardware=lambda:hardware())
            for i in range(4):
                self.assertEqual(r.choose("S01"), BASE)
                r.record({"worker":"S01","model":BASE,"status":"RESEARCHED",
                          "local_metrics":{"tokens_per_second":15.0,
                                           "elapsed_seconds":25.0}})
            self.assertEqual(r.choose("S05"), STRONG)
            for i in range(2):
                r.record({"worker":"S05","model":STRONG,
                          "status":"AI_UNAVAILABLE","safe_error":"OLLAMA_INVALID_JSON",
                          "local_metrics":{"tokens_per_second":1.2,
                                           "elapsed_seconds":200}})
            for i in range(8):
                self.assertEqual(r.choose("S06"), BASE)
            self.assertEqual(score(r._rows(STRONG))["valid_percent"], 0.0)
            restored = AdaptiveRouter(root,[BASE,STRONG], sample_hardware=lambda:hardware())
            self.assertEqual(restored.choose("S08"),BASE)
            self.assertIn("Valid output", format_report(restored.summary()))

    def test_unknown_or_insufficient_headroom_never_guesses_8b_is_safe(self):
        with tempfile.TemporaryDirectory() as root:
            for hw in ({"cpu_percent":None,"free_ram_gb":None,"total_ram_gb":None},
                       hardware(6.0,20),hardware(20.0,94.0)):
                r=AdaptiveRouter(root,[BASE,STRONG],sample_hardware=lambda h=hw:h)
                for i in range(5):
                    r.record({"worker":"S01","model":BASE,"status":"RESEARCHED"})
                for i in range(8):
                    self.assertEqual(r.choose("S01"), BASE)

    def test_manual_auto_once_selects_installed_model_without_broker_calls(self):
        from overnight_local import main
        with tempfile.TemporaryDirectory() as root:
            selected=[]
            def dry_run(data, model, stats, **kwargs):
                selected.append((model, kwargs["model_selector"]("S01")))
                kwargs["on_result"]({
                    "model":model,"worker":"S01","status":"RESEARCHED",
                    "local_metrics":{"tokens_per_second":14.2,"elapsed_seconds":9.7}})
                return 1
            with patch("overnight_local.available_models",return_value=[BASE,STRONG]), patch(
                "overnight_local.run_round",side_effect=dry_run), patch(
                "local_adaptive.hardware",return_value=hardware()):
                self.assertEqual(main(["--model","auto","--parallel","1",
                                       "--once","--data-dir",root]),0)
            self.assertEqual(selected[0],(BASE,BASE))
            report=Path(root,"MORNING_REPORT.md").read_text()
            self.assertIn("Adaptive local model telemetry",report)
            self.assertIn("qwen3:4b-instruct",report)
            records=json.loads(Path(root,"model_runtime.json").read_text())
            self.assertEqual(records["records"][0]["model"],BASE)

    def test_no_cloud_fallback_or_uninstalled_models(self):
        with tempfile.TemporaryDirectory() as root:
            r=AdaptiveRouter(root,["llama3.2:3b"],sample_hardware=lambda:hardware())
            self.assertEqual(r.choose("S01"),"llama3.2:3b")
            self.assertNotIn("qwen3:8b",r.summary()["models"])

    def test_real_ollama_usage_counts_come_from_api_not_predictions(self):
        model_data={"message":{"content":json.dumps({"research_topic":"Defined signal",
                 "hypothesis":"Test hourly returns","candidate":{"family":"trend",
                 "lookback":12,"threshold":0.02}})},
                 "eval_count":120,"eval_duration":6000000000,
                 "prompt_eval_count":400,"load_duration":800000000}
        with patch("local_ollama.urllib.request.urlopen",
                   return_value=io.BytesIO(json.dumps(model_data).encode())):
            model=OllamaResearch(BASE)
            value=model("research",{"worker":"S07"})
        self.assertEqual(value["action"],"HOLD")
        self.assertEqual(model.last_metrics["tokens_per_second"],20)
        self.assertEqual(model.last_metrics["prompt_eval_count"],400)
        self.assertEqual(model.last_metrics["load_seconds"],.8)
        self.assertEqual(model.last_metrics["retries"],0)

    def test_mentor_is_checklist_not_model_trading_permission(self):
        with tempfile.TemporaryDirectory() as root:
            record={"groq_experiments":[
                {"hypothesis":"Maybe option spread with unavailable bid/ask",
                 "test":{"status":"PENDING_PROPER_HISTORICAL_DATA"}}],
                "generation_index":1}
            Path(root,"gemini_special.json").write_text(json.dumps({
                "judges":{"J02":{"requested_check":"Falsify out of sample"}}}))
            p=plan(root,"S07",record)
            self.assertEqual(p["phase"],"DATA_AUDIT")
            self.assertEqual(p["allowed_trade_action"],"HOLD")
            self.assertIn("Falsify",p["external_council_suggestion_unverified"])
            self.assertIn("unavailable bid/ask",p["previous_idea_unverified"])

    def test_no_paper_strategy_can_approve_live_from_indicative_bars(self):
        now=dt.datetime(2026,11,1,tzinfo=UTC)
        marks=[(now-dt.timedelta(days=i),
                {"equity":110.0,"missing_quotes":False}) for i in range(70)]
        output=readiness("S07",{"events":[{"side":"SELL"} for _ in range(40)]},
                         marks, {"status":"AUDIT_PASSED"})
        self.assertFalse(output["approval_requested"])
        self.assertFalse(output["live_trading_enabled"])
        self.assertIn("NO_VERIFIED_EXECUTABLE_QUOTES_AND_SLIPPAGE",
                      output["blockers"])
        self.assertNotEqual(output["status"],"READY_TO_TRADE")


if __name__ == "__main__":
    unittest.main()
