"""Scheduled local Ollama research: midnight–7 weekdays, midnight–10 weekends Central.

This program is NOT a GitHub self-hosted runner, a broker or a trading executor.
It never edits the canonical Arena account ledgers. The immutable local research
records can be consumed/reviewed later without cloud-writer state conflicts.
"""
import argparse
import copy
from concurrent.futures import ThreadPoolExecutor, as_completed
import datetime as dt
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
import uuid
from zoneinfo import ZoneInfo

from local_ollama import OllamaResearch, available_models, local_model_name
from local_adaptive import AdaptiveRouter, format_report, score, hardware
from mentor_planner import plan as mentor_plan
from groq_research import one_turn
from run_virtual import CONFIG, UTC, market

REPO = "https://github.com/28twagg-ops/TradingBot.git"
RELATIVE = Path("records/arena/local_research")
LOCAL_TZ = ZoneInfo("America/Chicago")
DATA = Path.home() / ".trading-arena"
WORKERS = tuple(w["id"] for w in CONFIG["workers"])
MIN_DISK_FREE = 600 * 1024 * 1024


def json_atomic(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + "." + uuid.uuid4().hex + ".tmp")
    try:
        # Always LF even on Windows: Git can normalize CRLF on commit, which
        # otherwise breaks the byte-for-byte remote acknowledgement check.
        with temp.open("w", encoding="utf-8", newline="\n") as f:
            json.dump(data, f, ensure_ascii=False, indent=2, allow_nan=False)
            f.write("\n")
            f.flush()
            os.fsync(f.fileno())
        os.replace(temp, path)
    finally:
        if temp.exists():
            temp.unlink()


def git(*args, cwd=None, timeout=100):
    try:
        p = subprocess.run(["git", *map(str, args)], cwd=cwd, text=True,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           timeout=timeout, check=False)
    except (OSError, subprocess.TimeoutExpired):
        raise RuntimeError("GIT_UNAVAILABLE_OR_TIMED_OUT") from None
    if p.returncode:
        raise RuntimeError("GIT_COMMAND_FAILED") from None
    return p.stdout.strip()


def init_ledger(data=DATA):
    """Sparse read of persistent Arena evidence; no other bot source or secrets."""
    folder = Path(data) / "ledger"
    if not (folder / ".git").exists():
        folder.parent.mkdir(parents=True, exist_ok=True)
        git("clone", "--quiet", "--filter=blob:none", "--depth", "1",
            "--single-branch", "--sparse", "--branch", "arena-ledger",
            REPO, folder, timeout=180)
        git("sparse-checkout", "set", "records/arena", cwd=folder)
    return folder


def refresh_ledger(folder):
    git("fetch", "--quiet", "--depth", "1", "origin", "arena-ledger", cwd=folder)
    # This is an app-owned isolated checkout; all unsynced events live outside it.
    git("reset", "--quiet", "--hard", "FETCH_HEAD", cwd=folder)
    # Pending events are separately durable. Clean files left by interrupted pushes.
    git("clean", "-fd", "--", RELATIVE.as_posix(), cwd=folder)


def init_upload(data=DATA):
    """Dedicated local-only branch so laptop pushes never race cloud Arena jobs."""
    folder = Path(data) / "upload"
    if not (folder / ".git").exists():
        folder.parent.mkdir(parents=True, exist_ok=True)
        git("clone", "--quiet", "--filter=blob:none", "--depth", "1",
            "--single-branch", "--sparse", "--branch", "arena-local-research",
            REPO, folder, timeout=180)
        git("sparse-checkout", "set", "records/arena", cwd=folder)
    return folder


def refresh_upload(folder):
    git("fetch", "--quiet", "--depth", "1", "origin", "arena-local-research", cwd=folder)
    git("reset", "--quiet", "--hard", "FETCH_HEAD", cwd=folder)
    git("clean", "-fd", "--", RELATIVE.as_posix(), cwd=folder)


def event_paths(folder, pending):
    # Immutable records only; never read or stage production data.
    for path in (folder / RELATIVE).glob("*/*.json"):
        if path.is_file():
            yield path
    for source in (Path(pending), Path(pending).parent / "sent"):
        for path in source.glob("*.json"):
            if path.is_file():
                yield path


def read_history(folder, pending, worker, max_items=12, generation_index=None):
    rows = {}
    for path in event_paths(folder, pending):
        try:
            x = json.loads(path.read_text(encoding="utf-8"))
            if x.get("worker") != worker:
                continue
            if generation_index is not None and x.get("generation_index", 0) != generation_index:
                continue
            if not isinstance(x.get("experiment"), dict) or not x["experiment"].get("topic"):
                continue
            if x.get("kind") != "local_research_only":
                continue
            rows[x["event_id"]] = x
        except (ValueError, TypeError, KeyError, OSError):
            continue
    return sorted(rows.values(), key=lambda x: x.get("cycle", ""))[-max_items:]


def research_account(folder, pending, worker):
    state_file = folder / "records/arena/ai_state.json"
    from run_virtual import initial
    accounts = json.loads(state_file.read_text(encoding="utf-8")) if state_file.exists() else initial()
    if set(accounts) != set(WORKERS):
        raise ValueError("ARENA_ACCOUNT_ROSTER_MISMATCH")
    record = copy.deepcopy(accounts[worker])
    history = list(record.get("groq_experiments", []))[-6:]
    history.extend(x["experiment"] for x in read_history(
        folder, pending, worker, generation_index=record.get("generation_index",0)))
    # Local experimental history is private to the research identity; account
    # positions/real ledger events remain untouched. Only history is appended.
    record["groq_experiments"] = history
    record["mentor_research_plan_untrusted"] = mentor_plan(folder / "records/arena", worker, record)
    return {worker: record}


def within_window(when):
    """Weekday stop 07:00; Saturday/Sunday stop 10:00 America/Chicago.

    Resolve in local civil time so daylight-saving transitions are handled
    correctly, including the repeated hour on fall-back Sunday.
    """
    here = when.astimezone(LOCAL_TZ)
    stop_hour = 10 if here.weekday() >= 5 else 7
    return 0 <= here.hour < stop_hour


def queue_record(data, worker, event, experiment, model):
    if worker not in WORKERS:
        raise ValueError("UNKNOWN_WORKER")
    identifier = uuid.uuid4().hex
    cycle = str(event.get("cycle", ""))[:20]
    record = {"schema_version":1,"kind":"local_research_only",
              "event_id":identifier,"worker":worker,"cycle":cycle,
              "generation_index":event.get("generation_index",0),
              "model":model,"research_only":True,"live_trading":False,
              "event":event,"experiment":experiment}
    path = Path(data) / "pending" / (cycle[:10] + "_" + worker + "_" + identifier + ".json")
    json_atomic(path, record)
    return path


def canonical_json_bytes(payload):
    """Normalize only JSON whitespace line endings for cross-platform Git.

    JSON strings cannot contain raw CR or LF characters, so converting line
    endings cannot modify an actual JSON string value. Legacy queued Windows
    files can have CRLF, whereas Git stores LF in committed text blobs.
    """
    return payload.replace(b"\r\n", b"\n")


def sync_pending(data=DATA, attempts=4):
    """Retry immutable uploads to a dedicated local branch, never cloud ledgers.

    A separate GitHub Action imports these files into the canonical ledger with
    the shared Actions concurrency lock. Lost acknowledgements are idempotent.
    """
    data = Path(data)
    queue = sorted((data / "pending").glob("*.json"))
    if not queue:
        return 0
    folder = init_upload(data)
    for attempt in range(attempts):
        try:
            refresh_upload(folder)
            added = []
            for src in queue:
                payload = canonical_json_bytes(src.read_bytes())
                event = json.loads(payload.decode("utf-8"))
                day = event["cycle"][:10]
                ident = event["event_id"]
                worker = event["worker"]
                if worker not in WORKERS or not ident.isalnum() or len(ident) != 32:
                    raise ValueError("BAD_QUEUED_EVENT")
                target = folder / RELATIVE / day / (worker + "_" + ident + ".json")
                target.parent.mkdir(parents=True, exist_ok=True)
                if target.exists():
                    if canonical_json_bytes(target.read_bytes()) != payload:
                        raise ValueError("IMMUTABLE_EVENT_CONFLICT")
                else:
                    target.write_bytes(payload)
                    added.append(target.relative_to(folder).as_posix())
            if added:
                git("add", "--", *added, cwd=folder)
                git("-c", "user.name=arena-local[bot]",
                    "-c", "user.email=arena-local@users.noreply.github.com",
                    "commit", "--quiet", "-m", "Add immutable overnight Ollama research", cwd=folder)
                git("push", "--quiet", "origin", "HEAD:refs/heads/arena-local-research", cwd=folder)
            # Confirm commit is visible remotely before clearing durable queue.
            git("fetch", "--quiet", "--depth", "1", "origin", "arena-local-research", cwd=folder)
            for src in queue:
                event = json.loads(src.read_text(encoding="utf-8"))
                path = (RELATIVE / event["cycle"][:10] /
                        (event["worker"] + "_" + event["event_id"] + ".json")).as_posix()
                remote = subprocess.run(["git","show","FETCH_HEAD:"+path], cwd=folder,
                                        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                        timeout=30, check=False)
                if remote.returncode or canonical_json_bytes(remote.stdout) != canonical_json_bytes(src.read_bytes()):
                    raise RuntimeError("REMOTE_EVENT_NOT_CONFIRMED")
            archived = data / "sent"
            archived.mkdir(exist_ok=True, parents=True)
            for src in queue:
                os.replace(src, archived / src.name)
            return len(queue)
        except (RuntimeError, subprocess.TimeoutExpired) as exc:
            # Report only a bounded error category, never raw Git credentials,
            # URLs, stdout, stderr, or untrusted remote content.
            code = str(exc)
            allowed = {"GIT_UNAVAILABLE_OR_TIMED_OUT", "GIT_COMMAND_FAILED",
                       "REMOTE_EVENT_NOT_CONFIRMED"}
            category = code if code in allowed else "GIT_SYNC_TIMEOUT_OR_ERROR"
            print("Research upload attempt", attempt + 1, "of", attempts,
                  "not confirmed:", category, flush=True)
            time.sleep(2)
            continue
    return 0


def write_summary(data, stats):
    rows = ["# Arena local overnight research", "",
            "Updated: " + dt.datetime.now(UTC).isoformat(),
            "Research-only. No cloud AI bills, virtual orders, or real orders.",
            "", "| Worker | Research ideas | Needs data/revision | Failed |",
            "|---|---:|---:|---:|"]
    for w in WORKERS:
        x = stats.get(w, {})
        rows.append("| {} | {} | {} | {} |".format(
            w, x.get("researched",0), x.get("needs_data",0), x.get("failed",0)))
    rows += ["", "Last diagnostic codes (no credentials or provider text):"]
    for w in WORKERS:
        if stats.get(w, {}).get("last_error"):
            rows.append("- " + w + ": " + str(stats[w]["last_error"])[:32])
    rows += ["", "Pending GitHub sync: " + str(len(list((Path(data)/"pending").glob("*.json")))),
             "Details: ~/.trading-arena/sent/ (one immutable JSON record per turn).", ""]
    try:
        metrics=json.loads((Path(data)/"model_runtime.json").read_text(encoding="utf-8"))
        history=[x for x in metrics.get("records",[]) if isinstance(x,dict)]
        models=sorted(set(x.get("model") for x in history if isinstance(x.get("model"),str)))
        model_report={"models":{m:score([x for x in history if x.get("model")==m][-30:])
                                for m in models},
                      "last_selected":history[-1].get("model") if history else "None",
                      "last_switch_reason":"See model_runtime.json for chronological selection",
                      "hardware_snapshot":hardware()}
        rows.append(format_report(model_report))
    except (OSError,ValueError,TypeError):
        pass
    (Path(data)/"MORNING_REPORT.md").write_text("\n".join(rows), encoding="utf-8")


def smoke(model):
    names = available_models()
    if model not in names:
        raise RuntimeError("OLLAMA_MODEL_NOT_INSTALLED_OR_SERVICE_OFFLINE")
    result = OllamaResearch(model, timeout=240)(
        "You are an independent trading research scientist.",
        {"worker":"S07","research_personality":{"name":"Patient Trend Pilot"},
         "supported_backtest_rules":["trend","reversion","breakout","momentum"],
         "eligible_symbols":{},"research_history":[],"untrusted_search_results":[]})
    # Smoke tests only local API connectivity, valid JSON and enforced HOLD.
    # A 3B model may omit a research field on a single sample; never interpret
    # that as a Windows/GitHub installation failure. Full research runs still
    # enforce the independent deterministic validation gates.
    if not isinstance(result, dict) or not result:
        raise RuntimeError("OLLAMA_SMOKE_EMPTY_JSON")
    if result.get("action") != "HOLD" or result.get("symbol") is not None:
        raise RuntimeError("OLLAMA_SMOKE_UNSAFE_ACTION")
    if not isinstance(result.get("research_topic"), str) or not result["research_topic"].strip():
        print("Ollama API smoke passed, but the sample omitted research_topic; "
              "idea quality must be assessed from overnight research.")
    print("Ollama local smoke test succeeded; no trades or GitHub changes.")


def run_round(data, model, stats, allow_outside_window=False, now_fn=None, parallel=1, workers=None, model_selector=None, on_result=None):
    """Run up to two independent researchers at once; serialize disk/Git writes.

    All account copies are worker-private and model output is research-only.
    A single Ollama daemon may still queue inference unless its NUM_PARALLEL
    is configured and the RAM/VRAM is sufficient.
    """
    if type(parallel) is not int or not 1 <= parallel <= 2:
        raise ValueError("PARALLEL_RESEARCH_LANES_MUST_BE_ONE_OR_TWO")
    selected = WORKERS if workers is None else tuple(workers)
    if not selected or len(selected) > len(WORKERS) or len(set(selected)) != len(selected):
        raise ValueError("INVALID_TRIAL_WORKERS")
    if any(worker not in WORKERS for worker in selected):
        raise ValueError("UNKNOWN_TRIAL_WORKER")
    now_fn = now_fn or (lambda: dt.datetime.now(UTC))
    source = init_ledger(data)
    try:
        refresh_ledger(source)
    except RuntimeError:
        if not (source / "records/arena/ai_state.json").exists():
            raise
        print("GitHub unavailable: using prior read-only research snapshot.")
    if shutil.disk_usage(data).free < MIN_DISK_FREE:
        raise RuntimeError("LOW_DISK_SPACE")
    feed = market(now_fn())
    if not feed:
        print("Public market feed unavailable; no fictional historical tests.")
        return 0

    def research_one(worker):
        if not allow_outside_window and not within_window(now_fn()):
            return None
        # Never share a mutable account record, an LLM adapter or Git objects
        # between concurrent workers. Files are written by the main thread.
        accounts = research_account(source, Path(data) / "pending", worker)
        record = accounts[worker]
        original = len(record.get("groq_experiments", []))
        chosen = model_selector(worker) if model_selector is not None else model
        chosen = local_model_name(chosen)
        provider = OllamaResearch(chosen, timeout=300)
        event = one_turn(accounts, feed, provider, now_fn(), worker_id=worker)
        event["provider"] = "LOCAL_OLLAMA"
        event["source"] = "Local Ollama research-only"
        event["model"] = chosen
        event["generation_index"] = record.get("generation_index",0)
        event["local_metrics"] = getattr(provider,"last_metrics",{})
        event["research_only"] = True
        experiment = (record.get("groq_experiments", [])[-1]
                      if len(record.get("groq_experiments", [])) > original else {})
        return event, experiment

    processed = 0
    print("Local research lanes:", parallel, "model:", model, flush=True)
    with ThreadPoolExecutor(max_workers=parallel, thread_name_prefix="arena-local") as pool:
        futures = {pool.submit(research_one, worker): worker for worker in selected}
        for future in as_completed(futures):
            worker = futures[future]
            try:
                result = future.result()
                if result is None:
                    continue
                event, experiment = result
                status = event.get("status", "")
                bucket = ("researched" if status == "RESEARCHED" else
                          "needs_data" if status.startswith("RESEARCH_IDEA_NEEDS_")
                          else "failed")
                # Main-thread-only mutation and append-only durable recording.
                stats.setdefault(worker, {})[bucket] = (
                    stats.setdefault(worker, {}).get(bucket, 0) + 1)
                if status == "AI_UNAVAILABLE":
                    stats[worker]["last_error"] = event.get("safe_error", "PROVIDER_ERROR")
                if on_result is not None:
                    try:
                        on_result(event)
                    except (OSError,ValueError,TypeError):
                        print(worker,"MODEL_TELEMETRY_UNAVAILABLE",flush=True)
                queue_record(data, worker, event, experiment, event.get("model",model))
                processed += 1
                print(worker, status, stats[worker].get("last_error", ""),
                      "research-only", flush=True)
            except (ValueError, RuntimeError, OSError, KeyError, TypeError):
                stats.setdefault(worker, {})["failed"] = (
                    stats.setdefault(worker, {}).get("failed", 0) + 1)
                print(worker, "local research failure (safe hold)", flush=True)
    synced = sync_pending(data)
    pending_count = len(list((Path(data) / "pending").glob("*.json")))
    print("Confirmed GitHub sync:", synced,
          "; pending local records:", pending_count, flush=True)
    return processed


def process_running(pid):
    """Inspect a lock owner's status without signalling/killing it on Windows.

    On Windows, os.kill(pid, 0) calls TerminateProcess and can terminate the
    running overnight worker. Query the exit status via a read-only WinAPI
    process handle instead. Unknown/access-denied states fail safely.
    """
    if os.name == "nt":
        import ctypes
        from ctypes import wintypes
        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        kernel32.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
        kernel32.OpenProcess.restype = wintypes.HANDLE
        kernel32.GetExitCodeProcess.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD)]
        kernel32.GetExitCodeProcess.restype = wintypes.BOOL
        kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
        kernel32.CloseHandle.restype = wintypes.BOOL
        handle = kernel32.OpenProcess(0x1000, False, pid)  # PROCESS_QUERY_LIMITED_INFORMATION
        if not handle:
            if ctypes.get_last_error() == 87:  # ERROR_INVALID_PARAMETER: PID no longer exists
                return False
            raise PermissionError("CANNOT_INSPECT_LOCK_OWNER")
        try:
            code = wintypes.DWORD()
            if not kernel32.GetExitCodeProcess(handle, ctypes.byref(code)):
                raise OSError("CANNOT_INSPECT_LOCK_OWNER")
            return code.value == 259  # STILL_ACTIVE
        finally:
            kernel32.CloseHandle(handle)
    try:
        os.kill(pid, 0)  # POSIX only: probes without signalling
        return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True  # Be conservative if the lock's owner cannot be inspected.


def lock_acquire(data):
    lock = Path(data) / "overnight.lock"
    for _ in range(2):
        try:
            fd = os.open(lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            with os.fdopen(fd,"w",encoding="utf-8") as f:
                f.write(str(os.getpid()))
            return lock
        except FileExistsError:
            try:
                pid=int(lock.read_text(encoding="utf-8").strip())
                if process_running(pid):
                    raise RuntimeError("ANOTHER_RUN_ALREADY_ACTIVE") from None
                lock.unlink(missing_ok=True)   # dead process; queue is durable
            except (PermissionError,ValueError,OSError):
                raise RuntimeError("ANOTHER_RUN_OR_STALE_LOCK") from None
    raise RuntimeError("CANNOT_ACQUIRE_RESEARCH_LOCK")


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default=os.getenv("ARENA_OLLAMA_MODEL","qwen3:4b-instruct"),
                        help="Installed local model, or auto for measured 4B/8B switching")
    parser.add_argument("--parallel",type=int,choices=(1,2),default=1,
                        help="Parallel research lanes (2 only when RAM/VRAM allows)")
    parser.add_argument("--smoke", action="store_true",
                        help="One local-only model response, no market/GitHub writes")
    parser.add_argument("--once", action="store_true",
                        help="One research pass, any hour, useful for testing")
    parser.add_argument("--trial", action="store_true",
                        help="Two-worker real inference + paper-only GitHub sync trial")
    parser.add_argument("--sync-only", action="store_true",
                        help="Recover pending append-only GitHub uploads, no AI inference")
    parser.add_argument("--scheduled", action="store_true",
                        help="Task Scheduler watchdog; exit quietly outside local research window")
    parser.add_argument("--data-dir", type=Path, default=DATA)
    args=parser.parse_args(argv)
    if args.scheduled:
        if args.trial or args.once or args.smoke or args.sync_only:
            parser.error("--scheduled cannot run manual test modes")
        # This guard also protects a morning report created by the completed
        # overnight session from being overwritten by daytime watchdog checks.
        if not within_window(dt.datetime.now(UTC)):
            return 0
    automated=(args.model=="auto")
    model=local_model_name("qwen3:4b-instruct" if automated else args.model)
    data=args.data_dir.expanduser()
    data.mkdir(parents=True, exist_ok=True)
    if args.smoke:
        smoke(model)
        return 0
    if sum(bool(v) for v in (args.trial,args.once,args.sync_only))>1:
        parser.error("Choose --trial OR --once OR --sync-only")
    router=None
    if automated and not args.sync_only:
        if args.parallel != 1:
            raise RuntimeError("ADAPTIVE_ROUTING_REQUIRES_ONE_INFERENCE_LANE")
        router=AdaptiveRouter(data,available_models())
        model=router.preferred
    if not args.sync_only and model not in available_models():
        raise RuntimeError("OLLAMA_MODEL_NOT_INSTALLED_OR_SERVICE_OFFLINE")
    lock=lock_acquire(data)
    stats={}
    try:
        if args.sync_only:
            confirmed = sync_pending(data)
            pending = len(list((data / "pending").glob("*.json")))
            print("Confirmed GitHub sync:", confirmed, "; pending local records:", pending)
            return 0 if pending == 0 else 2
        if args.trial:
            # Exactly two researchers to prove genuine parallelism, market
            # data integration and append-only upload before a full night.
            selected=WORKERS[:2]
            run_round(data, model, stats, allow_outside_window=True,
                      parallel=args.parallel, workers=selected,
                      model_selector=router.choose if router else None,
                      on_result=router.record if router else None)
        elif args.once:
            # Manual one-pass run is allowed outside the overnight window.
            run_round(data, model, stats, allow_outside_window=True, parallel=args.parallel,
                      model_selector=router.choose if router else None,
                      on_result=router.record if router else None)
        else:
            while within_window(dt.datetime.now(UTC)):
                run_round(data,model,stats,parallel=args.parallel,
                          model_selector=router.choose if router else None,
                          on_result=router.record if router else None)
                write_summary(data,stats)
                # At most one round per 40 min; no burst retries, up to two lanes.
                for _ in range(40):
                    if not within_window(dt.datetime.now(UTC)):
                        break
                    time.sleep(60)
            if any((data/"pending").glob("*.json")):
                sync_pending(data)
        write_summary(data,stats)
    finally:
        lock.unlink(missing_ok=True)
    return 0


if __name__=="__main__":
    if "--log" in sys.argv:
        sys.argv.remove("--log")
        # Repeat every fifteen minutes in Task Scheduler to survive DST and
        # missed midnight triggers. Outside the research window this must be
        # a true no-op: no log spam, Ollama calls, Git I/O or report writes.
        if "--scheduled" in sys.argv and not within_window(dt.datetime.now(UTC)):
            sys.exit(0)
        DATA.mkdir(parents=True,exist_ok=True)
        stream=(DATA/"overnight.log").open("a",encoding="utf-8",buffering=1)
        sys.stdout=stream
        sys.stderr=stream
        print("Overnight task started",dt.datetime.now(UTC).isoformat())
    try:
        sys.exit(main())
    except (RuntimeError,ValueError,OSError) as error:
        print("Overnight arena stopped safely:",str(error),file=sys.stderr)
        sys.exit(2)
