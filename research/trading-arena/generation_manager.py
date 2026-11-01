"""Versioned paper Arena generation registry. No broker calls or real orders."""
import argparse
import copy
import datetime as dt
import hashlib
import json
import math
from pathlib import Path
from arena import PaperAccount, council
from run_virtual import CONFIG, UTC, initial

WORKERS = tuple(w["id"] for w in CONFIG["workers"])
MIN_AGE_DAYS = 28
MIN_SNAPSHOTS = 60
MIN_MARK_DAYS = 14
MIN_SELLS = 6
FINAL_FIVE = frozenset(("S09", "S02", "S07", "S10", "S06"))
FINAL_START = dt.datetime(2026, 11, 2, 5, 30, tzinfo=UTC)
FINAL_END = dt.datetime(2026, 11, 3, 5, 30, tzinfo=UTC)


def suffix(n):
    """a ... z, aa ... az, ba ... never reuse an identity."""
    if type(n) is not int or n < 0:
        raise ValueError("BAD_GENERATION_INDEX")
    result = ""
    while True:
        result = chr(97 + n % 26) + result
        n = n // 26 - 1
        if n < 0:
            return result


def alias(wid, n):
    if wid not in WORKERS:
        raise ValueError("UNKNOWN_WORKER")
    return wid + suffix(n)


def read(path, default):
    return json.loads(Path(path).read_text(encoding="utf-8")) if Path(path).exists() else copy.deepcopy(default)


def write(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def when(stamp):
    try:
        x = dt.datetime.fromisoformat(str(stamp).replace("Z", "+00:00"))
        return x.astimezone(UTC) if x.tzinfo else None
    except (TypeError, ValueError, OverflowError):
        return None


def registry_for(root, state, now):
    if set(state) != set(WORKERS):
        raise ValueError("BAD_WORKER_ROSTER")
    reg = read(Path(root) / "generation_registry.json", {"schema": 1, "workers": {}})
    if reg.get("schema") != 1 or not isinstance(reg.get("workers"), dict):
        raise ValueError("BAD_GENERATION_REGISTRY")
    for wid in WORKERS:
        if wid not in reg["workers"]:
            first = [when(x.get("timestamp")) for x in state[wid].get("events", [])
                     if isinstance(x, dict)]
            starts = [x for x in first if x and x <= now]
            index = state[wid].get("generation_index", 0)
            reg["workers"][wid] = {
                "index": index, "active": alias(wid, index),
                "started_at": (min(starts) if starts else now).isoformat(),
                "history": []}
        slot = reg["workers"][wid]
        idx = slot["index"]
        if slot.get("active") != alias(wid, idx) or state[wid].get("generation_index", idx) != idx:
            raise ValueError("GENERATION_IDENTITY_MISMATCH")
    return reg


def marks_for(rows, wid, name):
    result = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        item = row.get("workers", {}).get(wid)
        stamp = when(row.get("timestamp"))
        if stamp and isinstance(item, dict) and item.get("generation") == name:
            result.append((stamp, item))
    return sorted(result, key=lambda x: x[0])


def record_snapshot(root):
    root = Path(root)
    last = read(root / "last_run.json", {})
    stamp = when(last.get("timestamp"))
    result = last.get("results")
    if stamp is None or not isinstance(result, dict) or set(result) != set(WORKERS):
        raise ValueError("INVALID_LAST_RUN")
    state = read(root / "state.json", {})
    reg = registry_for(root, state, stamp)
    rows = read(root / "generation_observations.json", [])
    if not isinstance(rows, list):
        raise ValueError("BAD_MARK_HISTORY")
    if any(x.get("timestamp") == stamp.isoformat() for x in rows if isinstance(x, dict)):
        return False
    values = {}
    for wid in WORKERS:
        r = result[wid]
        equity = r.get("equity")
        if equity is not None and (type(equity) not in (int, float) or
                                   not math.isfinite(equity) or equity < 0):
            raise ValueError("INVALID_PRICE_MARK")
        values[wid] = {
            "generation": reg["workers"][wid]["active"],
            "equity": equity,
            "ledger_events": r.get("ledger_events"),
            "action": str(r.get("action", ""))[:60],
            "missing_quotes": bool(r.get("missing_quotes")),
            "council": str(r.get("council", ""))[:50]}
    rows.append({"timestamp": stamp.isoformat(), "workers": values,
                 "basis": "INDICATIVE_YAHOO_HOURLY_NOT_EXECUTABLE"})
    write(root / "generation_registry.json", reg)
    write(root / "generation_observations.json", rows)
    render(root, reg, rows)
    return True


def audited(worker, record):
    """Both rule-based and AI books must pass replay and hard-veto checks."""
    acc = PaperAccount(worker)
    for event in record["events"]:
        replay = acc.trade(timestamp=event["timestamp"], asset_class=event["asset_class"],
                           symbol=event["symbol"], side=event["side"], qty=event["qty"],
                           price=event["price"], fee=event["fee"], source_id=event["source_id"])
        if replay != event:
            raise ValueError("LEDGER_REPLAY_MISMATCH")
    if acc.holdings != record["positions"] or abs(acc.cash - record["cash"]) > 1e-6:
        raise ValueError("LEDGER_BALANCE_MISMATCH")
    report = council(acc.statement())
    if report["status"] == "REJECT_AND_QUARANTINE":
        raise ValueError("COUNCIL_HARD_VETO")
    return report


def decision(record, slot, marks, now, final=False):
    start = when(slot["started_at"])
    if start is None or start > now:
        return "DEFER_BAD_START"
    if not marks or marks[-1][1].get("equity") is None:
        return "DEFER_MISSING_EQUITY"
    latest = marks[-1][1]
    if (latest.get("missing_quotes") or latest.get("action") == "QUARANTINED"
            or now - marks[-1][0] > dt.timedelta(hours=8)):
        return "DEFER_STALE_OR_BAD_EQUITY"
    if final:
        # User-authorized one-off elimination, NOT a statistically proven loss.
        # No successor inherits any claimed historical profit.
        return "ROTATE_FINAL_CHANCE_UNPROVEN"
    age = (now - start).total_seconds() / 86400
    if age < MIN_AGE_DAYS:
        return "DEFER_MINIMUM_28_DAYS"
    valid = [(t, r) for t, r in marks if t >= start and r.get("equity") is not None
             and not r.get("missing_quotes") and r.get("action") != "QUARANTINED"]
    if len(valid) < MIN_SNAPSHOTS or len({t.date() for t, _ in valid}) < MIN_MARK_DAYS:
        return "DEFER_NOT_ENOUGH_FORWARD_MARKS"
    sells = sum(e.get("side") == "SELL" for e in record.get("events", []))
    if latest["equity"] < 99 and (sells >= MIN_SELLS or age >= 56):
        return "ROTATE_PERSISTENT_PAPER_LOSS"
    if age >= 56 and not record.get("events"):
        return "ROTATE_NO_TRADING_ACTIVITY"
    return "RETAIN_NO_PROVEN_EDGE"


def audit_and_rotate(root, now=None):
    root = Path(root)
    now = now or dt.datetime.now(UTC)
    if now.tzinfo is None:
        raise ValueError("NAIVE_REVIEW_TIME")
    now = now.astimezone(UTC)
    state = read(root / "state.json", {})
    ai = read(root / "ai_state.json", initial())
    if set(ai) != set(WORKERS):
        raise ValueError("BAD_AI_ROSTER")
    reg = registry_for(root, state, now)
    rows = read(root / "generation_observations.json", [])
    if not isinstance(rows, list):
        raise ValueError("BAD_MARK_HISTORY")
    advisory = read(root / "gemini_special.json", {})
    findings = []
    changes = 0
    for wid in WORKERS:
        slot = reg["workers"][wid]
        old = slot["active"]
        marks = marks_for(rows, wid, old)
        final = wid in FINAL_FIVE and slot["index"] == 0 and FINAL_START <= now < FINAL_END
        try:
            rules_review = audited(wid, state[wid])
            ai_review = audited(wid, ai[wid])
            verdict = decision(state[wid], slot, marks, now, final)
        except (ValueError, KeyError, TypeError, AttributeError, OverflowError):
            verdict = "QUARANTINE_NO_RESET"
            rules_review = None
            ai_review = None
        item = {"generation": old, "decision": verdict,
                "equity": marks[-1][1].get("equity") if marks else None,
                "observations": len(marks),
                "closed_trades": sum(x.get("side") == "SELL"
                                     for x in state[wid].get("events", []))}
        if verdict.startswith("ROTATE_"):
            path = root / "generations" / (old + ".json")
            if path.exists():
                item["decision"] = "QUARANTINE_DUPLICATE_ARCHIVE"
            else:
                archived = {
                    "schema": 1, "generation": old,
                    "started_at": slot["started_at"], "closed_at": now.isoformat(),
                    "decision": verdict, "last_indicative_equity": item["equity"],
                    "includes_open_paper_positions_without_fictitious_closing": True,
                    "real_money_trades": False,
                    "rule_book": copy.deepcopy(state[wid]),
                    "ai_book": copy.deepcopy(ai[wid]),
                    "paper_observations": [{"timestamp": t.isoformat(), **v}
                                           for t, v in marks],
                    "deterministic_council": {"rules": rules_review, "ai": ai_review},
                    "gemini_advisory": copy.deepcopy(advisory),
                    "ollama_source_branch": "arena-local-research"}
                checksum = hashlib.sha256(json.dumps(
                    archived, sort_keys=True, allow_nan=False).encode()).hexdigest()
                archived["sha256_content"] = checksum
                write(path, archived)
                slot["history"].append({
                    "generation": old, "archive": "generations/" + old + ".json",
                    "sha256": checksum, "equity": item["equity"],
                    "closed_at": now.isoformat(), "decision": verdict})
                successor_number = slot["index"] + 1
                new_name = alias(wid, successor_number)
                lesson = {
                    "previous_generation": old,
                    "previous_equity": item["equity"],
                    "review_reason": verdict,
                    "warning": "Prior paper performance is not forward proof.",
                    "topics": [str(e.get("topic", ""))[:100] for e in
                               ai[wid].get("groq_experiments", [])[-3:]
                               if isinstance(e, dict)]}
                state[wid] = initial()[wid]
                ai[wid] = initial()[wid]
                state[wid]["generation_index"] = successor_number
                ai[wid]["generation_index"] = successor_number
                ai[wid]["previous_generation_context"] = lesson
                slot.update({"index": successor_number, "active": new_name,
                             "started_at": now.isoformat()})
                item["successor"] = new_name
                changes += 1
        findings.append(item)
    if changes:
        write(root / "state.json", state)
        write(root / "ai_state.json", ai)
    write(root / "generation_registry.json", reg)
    output = {"timestamp": now.isoformat(), "rotations": changes,
              "monthly_minimum_days": MIN_AGE_DAYS,
              "no_live_trading": True, "results": findings}
    write(root / "generation_review.json", output)
    render(root, reg, rows, findings)
    return output


def render(root, reg, rows, findings=()):
    table = ["# Trading Arena — versioned paper generations", "",
             "Each generation begins a separate virtual $100 trial. Retired losses",
             "are never erased or counted as profit for a successor. Yahoo hourly",
             "prices are INDICATIVE, not executable. No live trading.", "",
             "| Active | Latest indicative equity | Marks | Archived versions |",
             "|---|---:|---:|---|"]
    for wid in WORKERS:
        slot = reg["workers"][wid]
        marks = marks_for(rows, wid, slot["active"])
        eq = next((r["equity"] for _, r in reversed(marks)
                   if r.get("equity") is not None), None)
        old = ", ".join(x["generation"] for x in slot["history"]) or "—"
        table.append("| {} | {} | {} | {} |".format(
            slot["active"], "New trial" if eq is None else "$" + format(eq, ".2f"),
            len(marks), old))
    if findings:
        table += ["", "## Council decisions", "",
                  "| Generation | Result | New bot |", "|---|---|---|"]
        for f in findings:
            table.append("| {} | {} | {} |".format(
                f["generation"], f["decision"], f.get("successor", "—")))
    table += ["", "Archived books and evidence: records/arena/generations/",
              "Immutable local Llama ideas: arena-local-research branch.",
              "Missing independently executable quotes prevent profit certification."]
    (Path(root) / "GENERATIONS.md").write_text("\n".join(table) + "\n", encoding="utf-8")


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--dir", required=True)
    x = p.add_mutually_exclusive_group(required=True)
    x.add_argument("--record", action="store_true")
    x.add_argument("--review", action="store_true")
    args = p.parse_args(argv)
    if args.record:
        print("Recorded new generation observations:", record_snapshot(args.dir))
    else:
        v = audit_and_rotate(args.dir)
        print("Council rotation check complete:", v["rotations"], "new paper generations")


if __name__ == "__main__":
    main()
