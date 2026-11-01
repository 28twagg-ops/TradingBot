"""Bounded, read-only handoff of local Llama ideas to cloud research reviewers.

Input files are untrusted records, not commands, executable code, or evidence of
profit. Never loads trading credentials or changes any virtual/live account.
"""
import json
from pathlib import Path

WORKERS = {f"S{i:02d}" for i in range(1, 11)}
ALLOWED_STATUSES = {
    "RESEARCHED", "RESEARCH_IDEA_NEEDS_DATA", "RESEARCH_IDEA_NEEDS_REVISION",
    "REJECTED_INVALID_MODEL_EXPERIMENT",
}


def _short(value, maximum=200):
    return value.strip()[:maximum] if isinstance(value, str) else ""


def read_local_ideas(root, worker=None, limit=3):
    """Expose only bounded, labeled hypotheses from imported immutable events.

    Files must have passed the independent importer; this second read still
    validates essential safety properties because the content is untrusted.
    """
    if worker is not None and worker not in WORKERS:
        raise ValueError("UNKNOWN_WORKER")
    limit = max(0, min(int(limit), 15))
    if not limit:
        return []
    folder = Path(root) / "local_research"
    if not folder.exists():
        return []
    # Finite read, sorted newest date first. Files within a day can arrive
    # in any order; sort on the validated recorded cycle below.
    paths = sorted(folder.glob("*/*.json"), reverse=True)[:300]
    collected = []
    for path in paths:
        try:
            if path.stat().st_size > 100_000:
                continue
            item = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(item, dict):
                continue
            wid = item.get("worker")
            if wid not in WORKERS or (worker is not None and wid != worker):
                continue
            if (item.get("kind") != "local_research_only"
                    or item.get("research_only") is not True
                    or item.get("live_trading") is not False):
                continue
            if not path.name.startswith(wid + "_") or not path.name.endswith(".json"):
                continue
            if len(path.stem[4:]) != 32 or item.get("event_id") != path.stem[4:]:
                continue
            if str(item.get("cycle", ""))[:10] != path.parent.name:
                continue
            event, experiment = item.get("event"), item.get("experiment")
            if not isinstance(event, dict) or not isinstance(experiment, dict):
                continue
            if event.get("status") not in ALLOWED_STATUSES:
                continue
            action = event.get("action", "HOLD")
            if not isinstance(action, str) or not action.startswith(("HOLD", "RESEARCH_ONLY")):
                continue
            topic = _short(experiment.get("topic"), 100)
            hypothesis = _short(experiment.get("hypothesis"), 220)
            if not topic and not hypothesis:
                continue
            test = experiment.get("test")
            test_status = (_short(test.get("status"), 55)
                           if isinstance(test, dict) else "")
            requirements = experiment.get("research_data_requirements")
            requirements = ([x[:30] for x in requirements[:5] if isinstance(x, str)]
                            if isinstance(requirements, list) else [])
            collected.append({
                "source": "UNVERIFIED_LOCAL_LLAMA_RESEARCH_ONLY",
                "worker": wid,
                "cycle": _short(item.get("cycle"), 30),
                "model": _short(item.get("model"), 65),
                "status": event["status"],
                "topic": topic,
                "hypothesis": hypothesis,
                "test_status": test_status,
                "data_requirements": requirements,
                "falsification_test": _short(experiment.get("falsification_test"), 180),
            })
        except (OSError, ValueError, UnicodeError, TypeError):
            continue
    collected.sort(key=lambda x: x["cycle"], reverse=True)
    return collected[:limit]
