"""Scheduled midnight-to-7 local Ollama research with safe, append-only GitHub sync.

This program is NOT a GitHub self-hosted runner, a broker or a trading executor.
It never edits the canonical Arena account ledgers. The immutable local research
records can be consumed/reviewed later without cloud-writer state conflicts.
"""
import argparse
import copy
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
        with temp.open("w", encoding="utf-8") as f:
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


def event_paths(folder, pending):
    # Immutable records only; never read or stage production data.
    for path in (folder / RELATIVE).glob("*/*.json"):
        if path.is_file():
            yield path
    for path in Path(pending).glob("*.json"):
        if path.is_file():
            yield path


def read_history(folder, pending, worker, max_items=12):
    rows = {}
    for path in event_paths(folder, pending):
        try:
            x = json.loads(path.read_text(encoding="utf-8"))
            if x.get("worker") != worker:
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
    history.extend(x["experiment"] for x in read_history(folder, pending, worker))
    # Local experimental history is private to the research identity; account
    # positions/real ledger events remain untouched. Only history is appended.
    record["groq_experiments"] = history
    return {worker: record}


def within_window(when):
    here = when.astimezone(LOCAL_TZ)
    return 0 <= here.hour < 7


def queue_record(data, worker, event, experiment, model):
    if worker not in WORKERS:
        raise ValueError("UNKNOWN_WORKER")
    identifier = uuid.uuid4().hex
    cycle = str(event.get("cycle", ""))[:20]
    record = {"schema_version":1,"kind":"local_research_only",
              "event_id":identifier,"worker":worker,"cycle":cycle,
              "model":model,"research_only":True,"live_trading":False,
              "event":event,"experiment":experiment}
    path = Path(data) / "pending" / (cycle[:10] + "_" + worker + "_" + identifier + ".json")
    json_atomic(path, record)
    return path


def sync_pending(data=DATA, attempts=4):
    """Rebase by re-materializing only unique files after every fetch.

    This does not mutate ai_state, state.json or other cloud-managed records.
    Recover safely if a previous push succeeded but the acknowledgement failed.
    """
    data = Path(data)
    queue = sorted((data / "pending").glob("*.json"))
    if not queue:
        return 0
    folder = init_ledger(data)
    for _ in range(attempts):
        try:
            refresh_ledger(folder)
            added = []
            for src in queue:
                payload = src.read_bytes()
                event = json.loads(payload.decode("utf-8"))
                day = event["cycle"][:10]
                ident = event["event_id"]
                worker = event["worker"]
                if worker not in WORKERS or not ident.isalnum() or len(ident) != 32:
                    raise ValueError("BAD_QUEUED_EVENT")
                target = folder / RELATIVE / day / (worker + "_" + ident + ".json")
                target.parent.mkdir(parents=True, exist_ok=True)
                if target.exists():
                    if target.read_bytes() != payload:
                        raise ValueError("IMMUTABLE_EVENT_CONFLICT")
                else:
                    target.write_bytes(payload)
                    added.append(target.relative_to(folder).as_posix())
            if added:
                git("add", "--", *added, cwd=folder)
                git("-c", "user.name=arena-local[bot]",
                    "-c", "user.email=arena-local@users.noreply.github.com",
                    "commit", "--quiet", "-m", "Add immutable overnight Ollama research", cwd=folder)
                git("push", "--quiet", "origin", "HEAD:refs/heads/arena-ledger", cwd=folder)
            # Confirm commit is visible remotely before clearing durable queue.
            git("fetch", "--quiet", "--depth", "1", "origin", "arena-ledger", cwd=folder)
            for src in queue:
                event = json.loads(src.read_text(encoding="utf-8"))
                path = (RELATIVE / event["cycle"][:10] /
                        (event["worker"] + "_" + event["event_id"] + ".json")).as_posix()
                remote = subprocess.run(["git","show","FETCH_HEAD:"+path], cwd=folder,
                                        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                        timeout=30, check=False)
                if remote.returncode or remote.stdout != src.read_bytes():
                    raise RuntimeError("REMOTE_EVENT_NOT_CONFIRMED")
            archived = data / "sent"
            archived.mkdir(exist_ok=True, parents=True)
            for src in queue:
                os.replace(src, archived / src.name)
            return len(queue)
        except (RuntimeError, subprocess.TimeoutExpired):
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
    rows += ["", "Pending GitHub sync: " + str(len(list((Path(data)/"pending").glob("*.json")))),
             "Details: ~/.trading-arena/sent/ (one immutable JSON record per turn).", ""]
    (Path(data)/"MORNING_REPORT.md").write_text("\n".join(rows), encoding="utf-8")


def smoke(model):
    names = available_models()
    if model not in names:
        raise RuntimeError("OLLAMA_MODEL_NOT_INSTALLED_OR_SERVICE_OFFLINE")
    result = OllamaResearch(model, timeout=120)(
        "You are an independent trading research scientist.",
        {"worker":"S07","research_personality":{"name":"Patient Trend Pilot"},
         "supported_backtest_rules":["trend","reversion","breakout","momentum"],
         "eligible_symbols":{},"research_history":[],"untrusted_search_results":[]})
    if not isinstance(result.get("research_topic"), str):
        raise RuntimeError("OLLAMA_SMOKE_JSON_FIELDS_MISSING")
    print("Ollama local smoke test succeeded; no trades or GitHub changes.")


def run_round(data, model, stats, allow_outside_window=False, now_fn=None):
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
    provider = OllamaResearch(model)
    processed = 0
    for worker in WORKERS:
        if not allow_outside_window and not within_window(now_fn()):
            break
        try:
            accounts = research_account(source, Path(data)/"pending", worker)
            record = accounts[worker]
            original = len(record.get("groq_experiments", []))
            event = one_turn(accounts,feed,provider,now_fn(),worker_id=worker)
            event["provider"] = "LOCAL_OLLAMA"
            event["model"] = model
            event["research_only"] = True
            status = event.get("status", "")
            bucket = "researched" if status=="RESEARCHED" else (
                "needs_data" if status.startswith("RESEARCH_IDEA_NEEDS_") else "failed")
            stats.setdefault(worker,{})[bucket] = stats.setdefault(worker,{}).get(bucket,0)+1
            experiment = record.get("groq_experiments",[])[-1] if (
                len(record.get("groq_experiments",[])) > original) else None
            queue_record(data, worker, event, experiment or {}, model)
            processed += 1
            print(worker, status, "research-only", flush=True)
        except (ValueError,RuntimeError,OSError,KeyError,TypeError):
            stats.setdefault(worker,{})["failed"]=stats.setdefault(worker,{}).get("failed",0)+1
            print(worker, "local research failure (safe hold)", flush=True)
        time.sleep(3)
    synced = sync_pending(data)
    print("Synced immutable events:",synced,"; pending saved locally", flush=True)
    return processed


def lock_acquire(data):
    lock = Path(data) / "overnight.lock"
    try:
        fd = os.open(lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        # A previous hard power loss may leave a stale marker; never start a
        # second concurrent runner automatically. User can remove it when off.
        raise RuntimeError("ANOTHER_RUN_OR_STALE_LOCK") from None
    os.close(fd)
    return lock


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default=os.getenv("ARENA_OLLAMA_MODEL","llama3.2:3b"))
    parser.add_argument("--smoke", action="store_true",
                        help="One local-only model response, no market/GitHub writes")
    parser.add_argument("--once", action="store_true",
                        help="One research pass, any hour, useful for testing")
    parser.add_argument("--data-dir", type=Path, default=DATA)
    args=parser.parse_args(argv)
    model=local_model_name(args.model)
    data=args.data_dir.expanduser()
    data.mkdir(parents=True, exist_ok=True)
    if args.smoke:
        smoke(model)
        return 0
    if model not in available_models():
        raise RuntimeError("OLLAMA_MODEL_NOT_INSTALLED_OR_SERVICE_OFFLINE")
    lock=lock_acquire(data)
    stats={}
    try:
        if args.once:
            # Manual one-pass run is allowed outside the overnight window.
            run_round(data, model, stats, allow_outside_window=True)
        else:
            while within_window(dt.datetime.now(UTC)):
                run_round(data,model,stats)
                write_summary(data,stats)
                # At most one round per 40 min; no burst retries, sequential bots.
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
    try:
        sys.exit(main())
    except (RuntimeError,ValueError,OSError) as error:
        print("Overnight arena stopped safely:",str(error),file=sys.stderr)
        sys.exit(2)
