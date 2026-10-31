"""Append-only import of laptop research from isolated inbox to canonical Arena.

Called only by a GitHub Actions job sharing the Arena ledger-write lock.
NEVER edits ai_state.json, state.json, orders, strategy files or production.
"""
import argparse
import collections
import datetime as dt
import json
from pathlib import Path
import re
import sys

VALID_FILE=re.compile(r"^S(0[1-9]|10)_[a-f0-9]{32}\.json$")
VALID_DAY=re.compile(r"^\d{4}-\d{2}-\d{2}$")
WORKERS=[f"S{i:02d}" for i in range(1,11)]


def verified_event(src):
    if not VALID_DAY.fullmatch(src.parent.name):
        raise ValueError("INVALID_EVENT_DAY")
    if not VALID_FILE.fullmatch(src.name):
        raise ValueError("INVALID_EVENT_FILENAME")
    payload=src.read_bytes()
    if len(payload)>100_000:
        raise ValueError("EXCESSIVE_EVENT_SIZE")
    event=json.loads(payload.decode("utf-8"))
    wid=event.get("worker")
    if wid not in WORKERS or wid!=src.name[:3]:
        raise ValueError("INVALID_WORKER_IDENTITY")
    if event.get("kind")!="local_research_only" or event.get("research_only") is not True:
        raise ValueError("NON_RESEARCH_EVENT_REFUSED")
    if event.get("live_trading") is not False:
        raise ValueError("LIVE_TRADING_REFUSED")
    if event.get("event_id")!=src.stem[4:]:
        raise ValueError("EVENT_ID_MISMATCH")
    if str(event.get("cycle",""))[:10]!=src.parent.name:
        raise ValueError("EVENT_DATE_MISMATCH")
    action=event.get("event",{}).get("action","HOLD")
    if action is not None and not str(action).startswith(("HOLD","RESEARCH_ONLY")):
        raise ValueError("TRADE_ACTION_REFUSED")
    return payload,event


def import_records(inbox,ledger):
    inbox=Path(inbox)
    ledger=Path(ledger)
    if not inbox.exists():
        return 0
    destination=ledger/"local_research"
    incoming=sorted(inbox.glob("*/*.json"))
    if len(incoming)>10000:
        raise ValueError("TOO_MANY_IMPORT_FILES")
    added=0
    for src in incoming:
        payload,_=verified_event(src)
        dst=destination/src.parent.name/src.name
        if dst.exists():
            if dst.read_bytes()!=payload:
                raise ValueError("IMMUTABLE_EVENT_CONFLICT")
            continue
        dst.parent.mkdir(parents=True,exist_ok=True)
        # This only writes immutable research artifacts, never account ledgers.
        dst.write_bytes(payload)
        added+=1
    write_report(ledger)
    return added


def write_report(ledger):
    rows=[]
    for file in (Path(ledger)/"local_research").glob("*/*.json"):
        try:
            _,item=verified_event(file)
            rows.append(item)
        except (ValueError,KeyError,TypeError,OSError):
            continue
    count=collections.Counter(x.get("worker") for x in rows)
    valid=collections.Counter(x.get("worker") for x in rows
                              if x.get("event",{}).get("status")=="RESEARCHED")
    failures=collections.Counter(x.get("worker") for x in rows
                                 if x.get("event",{}).get("status") in
                                 ("AI_UNAVAILABLE","REJECTED_INVALID_MODEL_EXPERIMENT"))
    lines=["# Overnight local Ollama research — paper-only", "",
           "Updated: "+dt.datetime.now(dt.timezone.utc).isoformat(), "",
           "**Separate local Llama research; not rule-based balances or validated profits.**",
           "No model-generated orders; no live trading.", "",
           "| Bot | Research attempts | Supported proxy ideas | Errors |",
           "|---|---:|---:|---:|"]
    for worker in WORKERS:
        lines.append(f"| {worker} | {count[worker]} | {valid[worker]} | {failures[worker]} |")
    lines.extend(["",f"Total accepted immutable local events: {len(rows)}",""])
    (Path(ledger)/"LOCAL_NIGHTLY.md").write_text(
        "\n".join(lines),encoding="utf-8")


def main(argv=None):
    p=argparse.ArgumentParser()
    p.add_argument("--inbox",type=Path,required=True)
    p.add_argument("--ledger",type=Path,required=True)
    a=p.parse_args(argv)
    print("Imported",import_records(a.inbox,a.ledger),
          "new isolated local research records")


if __name__=="__main__":
    try:
        main()
    except (ValueError,OSError,TypeError,KeyError) as exc:
        print("Local research import stopped safely:",type(exc).__name__,
              file=sys.stderr)
        sys.exit(2)
