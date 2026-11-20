"""Fail-closed evidence gate for paper-generation replacement.

Evidence is produced by an independent historical backtester, not by an LLM.
No broker calls and no automatic candidate certification.
"""
import datetime as dt
import json
import math
from pathlib import Path

REQUIRED = ("candidate_id", "worker", "validated", "data_provenance",
            "no_lookahead", "point_in_time_universe", "next_bar_execution",
            "costs_included", "out_of_sample_trades", "out_of_sample_days",
            "candidate_net_return_pct", "baseline_net_return_pct",
            "candidate_max_drawdown_pct", "baseline_max_drawdown_pct",
            "evaluated_at")

def evaluate(root, worker, candidate_id, now):
    """Return (approved, reason). Missing, stale, or malformed proof is rejected."""
    path = Path(root) / "candidate_evidence" / (candidate_id + ".json")
    if not path.is_file():
        return False, "NO_INDEPENDENT_BACKTEST"
    try:
        e = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(e, dict) or any(k not in e for k in REQUIRED):
            return False, "INCOMPLETE_BACKTEST_EVIDENCE"
        if e["worker"] != worker or e["candidate_id"] != candidate_id:
            return False, "BACKTEST_IDENTITY_MISMATCH"
        if any(e[k] is not True for k in ("validated", "no_lookahead",
                "point_in_time_universe", "next_bar_execution", "costs_included")):
            return False, "BACKTEST_METHOD_NOT_CERTIFIED"
        if not isinstance(e["data_provenance"], str) or not e["data_provenance"].strip():
            return False, "NO_DATA_PROVENANCE"
        stamp = dt.datetime.fromisoformat(e["evaluated_at"].replace("Z", "+00:00"))
        if stamp.tzinfo is None or stamp > now or now-stamp > dt.timedelta(days=30):
            return False, "STALE_BACKTEST"
        for k in ("out_of_sample_trades", "out_of_sample_days"):
            if type(e[k]) is not int:
                return False, "INVALID_SAMPLE_SIZE"
        if e["out_of_sample_trades"] < 30 or e["out_of_sample_days"] < 90:
            return False, "INSUFFICIENT_OUT_OF_SAMPLE"
        keys = ("candidate_net_return_pct", "baseline_net_return_pct",
                "candidate_max_drawdown_pct", "baseline_max_drawdown_pct")
        if any(type(e[k]) not in (int, float) or not math.isfinite(e[k]) for k in keys):
            return False, "INVALID_BACKTEST_METRICS"
        if (e["candidate_net_return_pct"] <= 0 or
                e["candidate_net_return_pct"] <= e["baseline_net_return_pct"] or
                e["candidate_max_drawdown_pct"] < 0 or
                e["baseline_max_drawdown_pct"] < 0 or
                e["candidate_max_drawdown_pct"] > e["baseline_max_drawdown_pct"]):
            return False, "CANDIDATE_FAILED_COMPARISON"
        return False, "TRUSTED_PORTFOLIO_VERIFIER_NOT_CONFIGURED"
    except (OSError, ValueError, TypeError, OverflowError, AttributeError):
        return False, "INVALID_BACKTEST_EVIDENCE"
