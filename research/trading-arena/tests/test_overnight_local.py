"""Offline safety and integration tests for overnight laptop research."""
import datetime as dt
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))

from local_ollama import OllamaResearch, local_model_name, available_models
from overnight_local import (WORKERS, within_window, queue_record, read_history,
                             research_account, sync_pending, run_round, lock_acquire)
from run_virtual import initial, UTC


class LocalLlamaTests(unittest.TestCase):
    def test_only_local_llama_models_are_accepted(self):
        self.assertEqual(local_model_name("llama3.2:3b"),"llama3.2:3b")
        for name in ("llama3.2:cloud","http://localhost:11434",
                     "example/remote-model","",None):
            with self.assertRaises(ValueError):
                local_model_name(name)

    def test_laptop_forces_hold_even_on_llama_buy_request(self):
        blob={"message":{"content":json.dumps({
            "research_topic":"Plausible signal","hypothesis":"test it first",
            "action":"BUY","symbol":"BTC-USD","allocation_fraction":0.4})}}
        sample=io.BytesIO(json.dumps(blob).encode())
        captured={}
        def mock_post(request,timeout):
            captured["url"]=request.full_url
            captured["body"]=json.loads(request.data)
            return sample
        with patch("local_ollama.urllib.request.urlopen",side_effect=mock_post):
            x=OllamaResearch("llama3.2:3b")("Research scientifically",{"worker":"S07"})
        self.assertEqual(x["action"],"HOLD")
        self.assertIsNone(x["symbol"])
        self.assertEqual(x["allocation_fraction"],0)
        self.assertEqual(captured["url"],"http://127.0.0.1:11434/api/chat")
        self.assertEqual(captured["body"]["stream"],False)
        self.assertEqual(captured["body"]["format"],"json")
        self.assertEqual(captured["body"]["model"],"llama3.2:3b")
        self.assertNotIn("tools",captured["body"])

    def test_invalid_local_json_fails_without_execution(self):
        sample=io.BytesIO(json.dumps({"message":{"content":"not JSON"}}).encode())
        with patch("local_ollama.urllib.request.urlopen",return_value=sample):
            with self.assertRaisesRegex(RuntimeError,"OLLAMA_INVALID_JSON"):
                OllamaResearch()("safe",{})

    def test_local_model_probe_never_uses_cloud(self):
        sample=io.BytesIO(json.dumps({"models":[{"name":"llama3.2:3b"}]}).encode())
        with patch("local_ollama.urllib.request.urlopen",return_value=sample):
            self.assertEqual(available_models(),["llama3.2:3b"])

    def test_dst_midnight_to_seven_in_central_time(self):
        self.assertTrue(within_window(dt.datetime(2026,10,31,6,30,tzinfo=UTC)))
        self.assertFalse(within_window(dt.datetime(2026,10,31,13,1,tzinfo=UTC)))
        self.assertTrue(within_window(dt.datetime(2026,11,1,7,20,tzinfo=UTC)))
        self.assertFalse(within_window(dt.datetime(2026,11,1,14,1,tzinfo=UTC)))

    def test_history_is_per_bot_not_canonical_accounts(self):
        with tempfile.TemporaryDirectory() as folder:
            data=Path(folder)
            repo=data/"ledger"
            (repo/"records/arena").mkdir(parents=True)
            (repo/"records/arena/ai_state.json").write_text(
                json.dumps(initial()),encoding="utf-8")
            queue_record(data,"S07",{"cycle":"2026-10-31T07:00Z",
                                    "status":"RESEARCHED"},
                         {"topic":"S07 novel test","paper_action":"HOLD"},"llama3.2:3b")
            queue_record(data,"S08",{"cycle":"2026-10-31T07:01Z",
                                    "status":"RESEARCHED"},
                         {"topic":"S08 separate idea"},"llama3.2:3b")
            self.assertEqual(len(read_history(repo,data/"pending","S07")),1)
            a=research_account(repo,data/"pending","S07")
            self.assertEqual(a["S07"]["groq_experiments"][0]["topic"],"S07 novel test")
            self.assertEqual(a["S07"]["cash"],100)
            self.assertEqual(a["S07"]["events"],[])
            self.assertEqual(json.loads((repo/"records/arena/ai_state.json").read_text())["S07"].get("groq_experiments"),None)

    def test_competing_process_lock_and_crash_recovery(self):
        with tempfile.TemporaryDirectory() as root:
            data=Path(root)
            acquired=lock_acquire(data)
            with self.assertRaisesRegex(RuntimeError,"ANOTHER_RUN_ALREADY_ACTIVE"):
                lock_acquire(data)
            acquired.write_text("99999999",encoding="utf-8")
            with patch("overnight_local.os.kill",side_effect=ProcessLookupError):
                renewed=lock_acquire(data)
            self.assertEqual(renewed,acquired)

    def test_a_research_round_queues_ten_isolated_no_trade_events(self):
        with tempfile.TemporaryDirectory() as root:
            data=Path(root)
            repo=data/"ledger"
            (repo/"records/arena").mkdir(parents=True)
            (repo/"records/arena/ai_state.json").write_text(json.dumps(initial()))
            clock=dt.datetime(2026,10,31,6,0,tzinfo=UTC)
            bars={"BTC-USD":[(clock.isoformat(),100.0)]*139}
            def model_turn(accounts,feed,provider,now,worker_id):
                accounts[worker_id].setdefault("groq_experiments",[]).append({
                    "cycle":now.isoformat(),"topic":worker_id+" unique idea"})
                return {"worker":worker_id,"cycle":now.strftime("%Y-%m-%dT%H:%MZ"),
                        "status":"RESEARCHED","action":"HOLD","live_trading":False}
            stats={}
            with patch("overnight_local.init_ledger",return_value=repo),patch(
                "overnight_local.refresh_ledger"),patch(
                "overnight_local.market",return_value=bars),patch(
                "overnight_local.one_turn",side_effect=model_turn),patch(
                "overnight_local.sync_pending",return_value=0),patch(
                "overnight_local.time.sleep"),patch(
                "overnight_local.shutil.disk_usage",return_value=type("Space",(),{"free":9000000000})()):
                count=run_round(data,"llama3.2:3b",stats,now_fn=lambda:clock)
            self.assertEqual(count,10)
            self.assertEqual(len(list((data/"pending").glob("*.json"))),10)
            self.assertEqual(set(stats),set(WORKERS))
            self.assertEqual(json.loads((repo/"records/arena/ai_state.json").read_text()),initial())

    @unittest.skipUnless(sys.platform!="win32","Requires Git subprocess in CI")
    def test_git_sync_is_immutable_and_idempotent(self):
        with tempfile.TemporaryDirectory() as root:
            root=Path(root)
            remote=root/"remote.git"
            seed=root/"seed"
            data=root/"data"
            data.mkdir()
            def command(*args):
                subprocess.run(["git",*map(str,args)],stdout=subprocess.DEVNULL,
                               stderr=subprocess.PIPE,check=True,timeout=20)
            command("init","--bare","--initial-branch=arena-ledger",remote)
            command("clone",remote,seed)
            (seed/"records/arena").mkdir(parents=True)
            (seed/"records/arena/ai_state.json").write_text(json.dumps(initial()))
            command("-C",seed,"add","records")
            command("-C",seed,"-c","user.name=CI","-c","user.email=ci@example.invalid",
                    "commit","-m","seed")
            command("-C",seed,"push","origin","HEAD:arena-ledger")
            item=queue_record(data,"S07",
                              {"cycle":"2026-10-31T06:00Z","status":"RESEARCHED"},
                              {"topic":"durable local idea"},"llama3.2:3b")
            with patch("overnight_local.REPO",str(remote)):
                self.assertEqual(sync_pending(data),1)
                self.assertEqual(sync_pending(data),0)
            self.assertFalse(item.exists())
            self.assertEqual(len(list((data/"sent").glob("*.json"))),1)
            command("-C",seed,"fetch","origin","arena-ledger")
            output=subprocess.check_output(
                ["git","-C",str(seed),"ls-tree","-r","--name-only","FETCH_HEAD"])
            self.assertIn(b"records/arena/local_research/2026-10-31/S07_",output)


if __name__=="__main__":
    unittest.main()
