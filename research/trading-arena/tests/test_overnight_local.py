"""Offline safety and integration tests for overnight laptop research."""
import datetime as dt
import ctypes
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest
from unittest.mock import Mock, patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))

from local_ollama import OllamaResearch, local_model_name, available_models
from overnight_local import (WORKERS, within_window, queue_record, read_history,
                             research_account, sync_pending, run_round, lock_acquire, process_running, init_upload)
from run_virtual import initial, UTC


class LocalLlamaTests(unittest.TestCase):
    def test_only_local_llama_models_are_accepted(self):
        self.assertEqual(local_model_name("llama3.2:3b"),"llama3.2:3b")
        self.assertEqual(local_model_name("qwen3:8b"),"qwen3:8b")
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
        self.assertEqual(captured["body"]["format"]["type"],"object")
        self.assertIn("research_topic",captured["body"]["format"]["required"])
        self.assertEqual(captured["body"]["model"],"llama3.2:3b")
        self.assertNotIn("tools",captured["body"])

    def test_qwen3_uses_non_thinking_json_schema(self):
        blob={"message":{"content":json.dumps({"research_topic":"hypothesis",
              "hypothesis":"null test","candidate":{"family":"trend",
              "lookback":12,"threshold":0.01}})}}
        captured={}
        def handler(req,timeout):
            captured.update(json.loads(req.data))
            return io.BytesIO(json.dumps(blob).encode())
        with patch("local_ollama.urllib.request.urlopen",side_effect=handler):
            output=OllamaResearch("qwen3:8b")("research",{})
        self.assertFalse(captured["think"])
        self.assertEqual(captured["format"]["type"],"object")
        self.assertEqual(output["action"],"HOLD")
        self.assertIsNone(output["symbol"])

    def test_smoke_does_not_abort_for_partial_but_safe_research_reply(self):
        # An intermittent 3B answer omitting research_topic is a research
        # quality issue, not a failed Ollama or GitHub installation.
        from overnight_local import smoke
        with patch("overnight_local.available_models",return_value=["llama3.2:3b"]), patch(
                "overnight_local.OllamaResearch",return_value=lambda *_: {
                    "action":"HOLD","symbol":None,"hypothesis":"needs independent review"}):
            self.assertEqual(smoke("llama3.2:3b"),None)

    def test_smoke_rejects_unsafe_action(self):
        from overnight_local import smoke
        with patch("overnight_local.available_models",return_value=["llama3.2:3b"]), patch(
                "overnight_local.OllamaResearch",return_value=lambda *_: {
                    "action":"BUY","symbol":"BTC-USD","research_topic":"unsafe"}):
            with self.assertRaisesRegex(RuntimeError,"OLLAMA_SMOKE_UNSAFE_ACTION"):
                smoke("llama3.2:3b")

    def test_invalid_local_json_fails_without_execution(self):
        sample=io.BytesIO(json.dumps({"message":{"content":"not JSON"}}).encode())
        with patch("local_ollama.urllib.request.urlopen",return_value=sample):
            with self.assertRaisesRegex(RuntimeError,"OLLAMA_INVALID_JSON"):
                OllamaResearch()("safe",{})

    def test_local_model_probe_never_uses_cloud(self):
        sample=io.BytesIO(json.dumps({"models":[{"name":"llama3.2:3b"}]}).encode())
        with patch("local_ollama.urllib.request.urlopen",return_value=sample):
            self.assertEqual(available_models(),["llama3.2:3b"])

    def test_central_time_weekend_extended_window_and_fall_dst(self):
        # 2026-10-31 Saturday, still in Central Daylight Time (UTC-5).
        self.assertFalse(within_window(dt.datetime(2026,10,31,4,59,tzinfo=UTC)))
        self.assertTrue(within_window(dt.datetime(2026,10,31,5,0,tzinfo=UTC)))
        self.assertTrue(within_window(dt.datetime(2026,10,31,14,59,tzinfo=UTC)))
        self.assertFalse(within_window(dt.datetime(2026,10,31,15,0,tzinfo=UTC)))
        # 2026-11-01 Sunday switches from CDT to CST. Both 01:30 hours count.
        self.assertTrue(within_window(dt.datetime(2026,11,1,5,0,tzinfo=UTC)))
        self.assertTrue(within_window(dt.datetime(2026,11,1,6,30,tzinfo=UTC)))
        self.assertTrue(within_window(dt.datetime(2026,11,1,7,30,tzinfo=UTC)))
        self.assertTrue(within_window(dt.datetime(2026,11,1,15,59,tzinfo=UTC)))
        self.assertFalse(within_window(dt.datetime(2026,11,1,16,0,tzinfo=UTC)))
        # Monday returns to 07:00 CST cutoff.
        self.assertFalse(within_window(dt.datetime(2026,11,2,5,59,tzinfo=UTC)))
        self.assertTrue(within_window(dt.datetime(2026,11,2,6,0,tzinfo=UTC)))
        self.assertTrue(within_window(dt.datetime(2026,11,2,12,59,tzinfo=UTC)))
        self.assertFalse(within_window(dt.datetime(2026,11,2,13,0,tzinfo=UTC)))

    def test_weekday_friday_still_stops_at_seven(self):
        self.assertTrue(within_window(dt.datetime(2026,10,30,11,59,tzinfo=UTC)))
        self.assertFalse(within_window(dt.datetime(2026,10,30,12,0,tzinfo=UTC)))

    def test_windows_schedule_runtime_covers_dst_fallback(self):
        from setup_local import register_windows
        with patch("setup_local.run") as runner:
            register_windows("C:\\Python311\\python.exe", "llama3.2:3b")
        command = runner.call_args.args[-1]
        self.assertIn('-At "00:00"', command)
        self.assertIn("-ExecutionTimeLimit (New-TimeSpan -Hours 12)", command)

    def test_parallel_two_workers_overlap_but_preserve_isolated_ledgers(self):
        with tempfile.TemporaryDirectory() as root:
            data=Path(root)
            repo=data/"ledger"
            (repo/"records/arena").mkdir(parents=True)
            original=initial()
            (repo/"records/arena/ai_state.json").write_text(json.dumps(original))
            clock=dt.datetime(2026,11,1,7,10,tzinfo=UTC)
            feed={"BTC-USD":[(clock.isoformat(),100.0)]*139}
            gate=threading.Barrier(2)
            overlap=[]
            def model_turn(accounts,feed,provider,now,worker_id):
                gate.wait(timeout=5)
                overlap.append(worker_id)
                accounts[worker_id].setdefault("groq_experiments",[]).append({
                    "cycle":now.isoformat(),"topic":worker_id+" independent parallel research"})
                return {"worker":worker_id,"cycle":now.strftime("%Y-%m-%dT%H:%MZ"),
                        "status":"RESEARCHED","action":"HOLD","live_trading":False}
            stats={}
            with patch("overnight_local.init_ledger",return_value=repo), patch(
                "overnight_local.refresh_ledger"), patch(
                "overnight_local.market",return_value=feed), patch(
                "overnight_local.one_turn",side_effect=model_turn), patch(
                "overnight_local.sync_pending",return_value=0), patch(
                "overnight_local.shutil.disk_usage",return_value=type(
                    "Space",(),{"free":9000000000})()):
                count=run_round(data,"qwen3:8b",stats,parallel=2,now_fn=lambda:clock)
            self.assertEqual(count,10)
            self.assertEqual(len(overlap),10)
            self.assertEqual(set(overlap),set(WORKERS))
            self.assertEqual(len(list((data/"pending").glob("*.json"))),10)
            self.assertEqual(json.loads((repo/"records/arena/ai_state.json").read_text()),original)
            self.assertEqual(set(stats),set(WORKERS))
            for event_path in (data/"pending").glob("*.json"):
                record=json.loads(event_path.read_text())
                self.assertEqual(record["model"],"qwen3:8b")
                self.assertEqual(record["event"]["action"],"HOLD")

    def test_report_includes_finite_model_error_reason_and_pending_count(self):
        from overnight_local import write_summary
        with tempfile.TemporaryDirectory() as d:
            write_summary(d,{"S01":{"failed":1,"last_error":"OLLAMA_OFFLINE_OR_TIMEOUT"}})
            report=(Path(d)/"MORNING_REPORT.md").read_text()
            self.assertIn("S01: OLLAMA_OFFLINE_OR_TIMEOUT",report)
            self.assertIn("Pending GitHub sync: 0",report)

    def test_two_worker_trial_only_runs_s01_and_s02(self):
        with tempfile.TemporaryDirectory() as root:
            data=Path(root)
            repo=data/"ledger"
            (repo/"records/arena").mkdir(parents=True)
            original=initial()
            (repo/"records/arena/ai_state.json").write_text(json.dumps(original))
            clock=dt.datetime(2026,11,1,7,10,tzinfo=UTC)
            feed={"BTC-USD":[(clock.isoformat(),100.0)]*139}
            observed=[]
            def fake_turn(accounts,feed,provider,now,worker_id):
                observed.append(worker_id)
                accounts[worker_id].setdefault("groq_experiments",[]).append({
                    "cycle":now.isoformat(),"topic":worker_id+" trial idea"})
                return {"worker":worker_id,"cycle":now.strftime("%Y-%m-%dT%H:%MZ"),
                        "status":"RESEARCHED","action":"HOLD","live_trading":False}
            with patch("overnight_local.init_ledger",return_value=repo), patch(
                "overnight_local.refresh_ledger"), patch(
                "overnight_local.market",return_value=feed), patch(
                "overnight_local.one_turn",side_effect=fake_turn), patch(
                "overnight_local.sync_pending",return_value=0), patch(
                "overnight_local.shutil.disk_usage",return_value=type(
                    "Space",(),{"free":9000000000})()):
                stats={}
                self.assertEqual(run_round(data,"qwen3:8b",stats,parallel=2,
                    workers=("S01","S02"),now_fn=lambda:clock),2)
            self.assertEqual(set(observed),{"S01","S02"})
            self.assertEqual(len(list((data/"pending").glob("*.json"))),2)
            self.assertEqual(json.loads((repo/"records/arena/ai_state.json").read_text()),original)

    def test_sync_only_never_calls_ollama_or_market_feed(self):
        from overnight_local import main
        with tempfile.TemporaryDirectory() as root:
            with patch("overnight_local.available_models",side_effect=AssertionError(
                    "sync-only must not invoke Ollama")), patch(
                    "overnight_local.market",side_effect=AssertionError(
                        "sync-only must not download market data")), patch(
                    "overnight_local.sync_pending",return_value=0):
                self.assertEqual(main(["--sync-only","--data-dir",root]),0)

    def test_parallel_request_limit_prevents_ten_worker_fanout(self):
        with self.assertRaisesRegex(ValueError,"PARALLEL_RESEARCH_LANES"):
            run_round(Path("."),"qwen3:8b",{},parallel=10)

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

    def test_windows_lock_probe_never_sends_kill_zero(self):
        # os.kill(pid, 0) terminates the target on Windows, unlike POSIX.
        kernel32 = Mock()
        kernel32.OpenProcess.return_value = 123
        def live_exit_code(handle, output):
            output._obj.value = 259  # STILL_ACTIVE
            return 1
        kernel32.GetExitCodeProcess.side_effect = live_exit_code
        with patch("overnight_local.os.name", "nt"), patch.object(
                ctypes, "WinDLL", return_value=kernel32, create=True), patch(
                "overnight_local.os.kill", side_effect=AssertionError("Unsafe Windows signal")):
            self.assertTrue(process_running(4321))
            kernel32.OpenProcess.assert_called_with(0x1000, False, 4321)
            kernel32.CloseHandle.assert_called_with(123)
            kernel32.OpenProcess.return_value = None
            with patch.object(ctypes, "get_last_error", return_value=87, create=True):
                self.assertFalse(process_running(999999))
            with patch.object(ctypes, "get_last_error", return_value=5, create=True):
                with self.assertRaises(PermissionError):
                    process_running(4321)

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

    def test_new_local_events_use_lf_only_on_any_platform(self):
        with tempfile.TemporaryDirectory() as d:
            item=queue_record(Path(d),"S01",
                {"cycle":"2026-11-01T00:58Z","status":"AI_UNAVAILABLE",
                 "action":"HOLD"},
                {"topic":"test a defensible hypothesis"},"qwen3:8b")
            self.assertNotIn(b"\r\n",item.read_bytes())
            self.assertIn(b"\n",item.read_bytes())

    @unittest.skipUnless(sys.platform!="win32","Requires Git subprocess in CI")
    def test_recovers_legacy_windows_crlf_records_with_autocrlf_true(self):
        # Reproduce the field report: events reach GitHub on Windows but
        # remote-ack fails because Git normalized CRLF to LF when committing.
        with tempfile.TemporaryDirectory() as root:
            root=Path(root)
            remote=root/"remote.git"
            seed=root/"seed"
            data=root/"data"
            data.mkdir()
            def command(*args):
                return subprocess.run(["git",*map(str,args)],capture_output=True,
                    check=True,timeout=30).stdout
            command("init","--bare","--initial-branch=arena-local-research",remote)
            command("clone",remote,seed)
            (seed/"records/arena").mkdir(parents=True)
            (seed/"records/arena/ai_state.json").write_text(json.dumps(initial()))
            command("-C",seed,"add","records")
            command("-C",seed,"-c","user.name=CI","-c",
                    "user.email=ci@example.invalid","commit","-m","seed")
            command("-C",seed,"push","origin","HEAD:arena-local-research")
            item=queue_record(data,"S01",
                {"cycle":"2026-11-01T00:58Z","status":"RESEARCH_IDEA_NEEDS_DATA",
                 "action":"HOLD"},
                {"topic":"an unverified idea","test":{"status":"PENDING_PROPER_HISTORICAL_DATA"}},
                "qwen3:8b")
            legacy=item.read_bytes().replace(b"\n",b"\r\n")
            item.write_bytes(legacy)
            with patch("overnight_local.REPO",str(remote)):
                upload=init_upload(data)
                command("-C",upload,"config","core.autocrlf","true")
                self.assertEqual(sync_pending(data,attempts=2),1)
                self.assertEqual(sync_pending(data,attempts=1),0)
            self.assertFalse(item.exists())
            archived=data/"sent"/item.name
            self.assertEqual(archived.read_bytes(),legacy)
            filename=archived.name
            payload=command("--git-dir",remote,"show",
                "arena-local-research:records/arena/local_research/2026-11-01/"
                + "S01_"+filename.split("_")[-1])
            self.assertEqual(payload,legacy.replace(b"\r\n",b"\n"))
            # Simulate the exact field failure: uploaded event stays pending
            # despite already being present on the remote branch.
            restored=data/"pending"/item.name
            restored.parent.mkdir(exist_ok=True)
            restored.write_bytes(legacy)
            with patch("overnight_local.REPO",str(remote)):
                self.assertEqual(sync_pending(data,attempts=2),1)
            self.assertFalse(restored.exists())

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
            command("init","--bare","--initial-branch=arena-local-research",remote)
            command("clone",remote,seed)
            (seed/"records/arena").mkdir(parents=True)
            (seed/"records/arena/ai_state.json").write_text(json.dumps(initial()))
            command("-C",seed,"add","records")
            command("-C",seed,"-c","user.name=CI","-c","user.email=ci@example.invalid",
                    "commit","-m","seed")
            command("-C",seed,"push","origin","HEAD:arena-local-research")
            item=queue_record(data,"S07",
                              {"cycle":"2026-10-31T06:00Z","status":"RESEARCHED"},
                              {"topic":"durable local idea"},"llama3.2:3b")
            with patch("overnight_local.REPO",str(remote)):
                self.assertEqual(sync_pending(data),1)
                self.assertEqual(sync_pending(data),0)
            self.assertFalse(item.exists())
            self.assertEqual(len(list((data/"sent").glob("*.json"))),1)
            command("-C",seed,"fetch","origin","arena-local-research")
            output=subprocess.check_output(
                ["git","-C",str(seed),"ls-tree","-r","--name-only","FETCH_HEAD"])
            self.assertIn(b"records/arena/local_research/2026-10-31/S07_",output)


if __name__=="__main__":
    unittest.main()
