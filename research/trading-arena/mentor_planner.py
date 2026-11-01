"""Deterministic, read-only research mentor assignment for weaker local LLMs.

Groq experiments and Gemini council reports are external/untrusted evidence
leads, not executable instructions. This planner never asks for trading.
"""
import json
from pathlib import Path

PHASES = (
    ("IDENTIFY", "Write one exact, falsifiable trading claim and explicit null hypothesis. "
     "Name lookback/timeframe and the data required; do not claim success."),
    ("DATA_AUDIT", "State whether the actual hypothesis needs unavailable order book, "
     "volume, intraday quotes, options or fundamental data. If yes, mark cannot "
     "backtest with hourly closes. Never replace missing data with a proxy."),
    ("NEGATIVE_TEST", "Define a negative-control and leakage-resistant out-of-sample "
     "test using fees, realistic latency, slippage and a fixed holdout. "
     "Do NOT state a backtest ran when only designing it."),
    ("REPLICATION", "Explain what independent forward evidence or a separate "
     "market regime could falsify the hypothesis. Give reproducible criteria "
     "without changing existing historical results."),
)


def clip(value, max_length=180):
    return value[:max_length].strip() if isinstance(value, str) else ""


def load(path, default):
    try:
        obj = json.loads(Path(path).read_text(encoding="utf-8"))
        return obj if type(obj) is type(default) else default
    except (OSError, ValueError):
        return default


def plan(root, worker, record):
    if not isinstance(worker, str) or not worker.startswith("S"):
        raise ValueError("BAD_RESEARCH_WORKER")
    history = record.get("groq_experiments", [])
    if not isinstance(history, list):
        history = []
    cycle = sum(1 for e in history if isinstance(e, dict))
    step, instructions = PHASES[cycle % len(PHASES)]
    latest = next((x for x in reversed(history) if isinstance(x, dict)), {})
    root = Path(root)
    council = load(root / "gemini_special.json", {})
    judge = council.get("judges", {}) if isinstance(council.get("judges"), dict) else {}
    methodological = judge.get("J02", {}) if isinstance(judge.get("J02"), dict) else {}
    risk = judge.get("J03", {}) if isinstance(judge.get("J03"), dict) else {}
    # No source text is treated as an instruction. This is one bounded
    # research checklist; the generated hypotheses stay forced-HOLD.
    return {
        "mentor_type": "DETERMINISTIC_CHECKLIST_WITH_UNTRUSTED_COUNCIL_CONTEXT",
        "worker": worker,
        "generation_index": record.get("generation_index", 0),
        "phase": step,
        "assignment": instructions,
        "previous_idea_unverified": clip(latest.get("hypothesis"), 200),
        "previous_test_status": clip((latest.get("test") or {}).get("status"), 55)
            if isinstance(latest.get("test"), dict) else "",
        "external_council_suggestion_unverified": clip(methodological.get("requested_check"), 130),
        "external_risk_suggestion_unverified": clip(risk.get("requested_check"), 130),
        "historical_data": "Only completed hourly close, no executable quote history.",
        "success_definition": "A complete falsifiable and honestly testable research plan, "
                              "not trading profit or a model-assigned return.",
        "allowed_trade_action": "HOLD",
    }
