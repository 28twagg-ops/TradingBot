"""Offline regression checks: local JSON recovery and conservative research gating."""
import io
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from local_ollama import OllamaResearch
from groq_research import one_turn
from run_virtual import initial, UTC
import datetime as dt


class ResearchQualityFixTests(unittest.TestCase):
    def test_invalid_json_retries_once_from_original_context_and_forces_hold(self):
        calls = []
        replies = [
            {"message": {"content": "{broken JSON"}},
            {"message": {"content": "```json\n" + json.dumps({
                "research_topic": "valid hourly research",
                "hypothesis": "Test hourly closes"
            }) + "\n```"}}
        ]
        def local_request(request, timeout):
            calls.append(json.loads(request.data))
            return io.BytesIO(json.dumps(replies.pop(0)).encode())
        with patch("local_ollama.urllib.request.urlopen", side_effect=local_request):
            result = OllamaResearch("llama3.2:3b")("research only", {"worker": "S07"})
        self.assertEqual(len(calls), 2)
        self.assertEqual(result["research_topic"], "valid hourly research")
        self.assertEqual(result["action"], "HOLD")
        self.assertIsNone(result["symbol"])
        self.assertEqual(result["allocation_fraction"], 0)
        self.assertEqual(calls[1]["options"]["temperature"], 0)
        self.assertNotIn("{broken JSON", json.dumps(calls[1]))
        self.assertEqual(calls[1]["model"], "llama3.2:3b")

    def test_permanent_malformed_json_fails_closed_after_two_calls(self):
        calls = []
        def bad(request, timeout):
            calls.append(request.full_url)
            return io.BytesIO(json.dumps({"message": {"content": "bad"}}).encode())
        with patch("local_ollama.urllib.request.urlopen", side_effect=bad):
            with self.assertRaisesRegex(RuntimeError, "OLLAMA_INVALID_JSON"):
                OllamaResearch()("safe", {})
        self.assertEqual(calls, ["http://127.0.0.1:11434/api/chat"] * 2)

    def test_hidden_volume_test_does_not_backtest_or_trade(self):
        now = dt.datetime(2026, 10, 26, 20, 40, tzinfo=UTC)
        start = now - dt.timedelta(hours=140)
        bars = [((start + dt.timedelta(hours=i)).isoformat(), 100.0 + i * .1)
                for i in range(139)]
        raw = {
            "research_topic": "BTC hourly momentum",
            "hypothesis": "BTC-USD hourly momentum persists",
            "falsification_test": "Confirm order book depth and volume",
            "candidate": {"family": "momentum", "lookback": 12, "threshold": .01},
            "study_symbol": "BTC-USD", "action": "BUY", "symbol": "BTC-USD",
            "allocation_fraction": .2, "next_search_query": "BTC hourly tests",
            "research_data_requirements": ["hourly_close", "hourly_close"],
            "hypothesis_timeframe": "hourly", "rule_expressible_as_candidate": True
        }
        accounts = initial()
        with patch("groq_research.discover", return_value={
             "query": "BTC", "attempted": [], "found": []}), patch(
             "groq_research.tradable", return_value={}):
            result = one_turn(accounts, {"BTC-USD": bars}, lambda *_: raw, now, worker_id="S01")
        self.assertEqual(result["status"], "RESEARCH_IDEA_NEEDS_DATA")
        self.assertEqual(result["test"]["status"], "PENDING_PROPER_HISTORICAL_DATA")
        self.assertEqual(accounts["S01"]["events"], [])
        self.assertEqual(accounts["S01"]["groq_experiments"][0][
                         "research_data_requirements"], ["hourly_close"])


if __name__ == "__main__":
    unittest.main()
