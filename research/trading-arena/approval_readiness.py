"""Fail-closed evidence/readiness report, never a broker or execution interface.

Financial research: DSR/PBO caution against repeated-trial selection bias.
A backtest, simulated Yahoo close, or LLM vote cannot certify future profit.
"""
from pathlib import Path
import json
from arena import PaperAccount, council
from run_virtual import CONFIG

MIN_FORWARD_SESSIONS = 60
MIN_COMPLETED_EXITS = 20
MIN_MARKET_DAYS = 30


def readiness(worker, record, marks, council_review=None):
    blockers = []
    exits = sum(e.get("side") == "SELL" for e in record.get("events", []))
    dated = {ts.date() for ts, item in marks if item.get("equity") is not None}
    # Separate per-generation *forward* observations, not recycled backtests.
    valid = [(ts, item) for ts, item in marks if item.get("equity") is not None
             and not item.get("missing_quotes")]
    latest = valid[-1][1]["equity"] if valid else None
    if len(valid) < MIN_FORWARD_SESSIONS:
        blockers.append("LESS_THAN_60_FORWARD_PAPER_MARKS")
    if len(dated) < MIN_MARKET_DAYS:
        blockers.append("LESS_THAN_30_DISTINCT_FORWARD_DAYS")
    if exits < MIN_COMPLETED_EXITS:
        blockers.append("LESS_THAN_20_CLOSED_PAPER_EXITS")
    if latest is None or latest <= 100.0:
        blockers.append("NO_NET_POSITIVE_CUMULATIVE_PAPER_EQUITY")
    if council_review is None or council_review.get("status") != "AUDIT_PASSED":
        blockers.append("INDEPENDENT_COUNCIL_EVIDENCE_NOT_PASSED")
    # The current Yahoo hourly prices are indicative closes, not actual fills.
    # No trusted independent executable bid/ask quote stream is connected.
    blockers.append("NO_VERIFIED_EXECUTABLE_QUOTES_AND_SLIPPAGE")
    blockers.append("NO_UNTOUCHED_OUT_OF_SAMPLE_MULTIPLE_TEST_CORRECTION")
    return {"worker": worker, "status": "NOT_ELIGIBLE_FOR_LIVE_APPROVAL",
            "blockers": blockers, "forward_marks": len(valid),
            "closed_paper_exits": exits, "distinct_mark_days": len(dated),
            "latest_indicative_equity": latest,
            "live_trading_enabled": False, "automatic_real_trading": False,
            "approval_requested": False,
            "note": "No trading method can be proven 100% profitable. "
                    "Do not request approval without new independent "
                    "executable-quote evidence and an untouched forward trial."}


def report(root, registry, states, rows, marks_for):
    evaluations = {}
    for worker in sorted(states):
        slot = registry["workers"][worker]
        # Deterministic independent council uses ledger replay; its evidence
        # role remains UNVERIFIED without external executable observations.
        account = PaperAccount(worker)
        record = states[worker]
        try:
            for e in record["events"]:
                replay = account.trade(timestamp=e["timestamp"], asset_class=e["asset_class"],
                                       symbol=e["symbol"], side=e["side"], qty=e["qty"],
                                       price=e["price"], fee=e["fee"], source_id=e["source_id"])
                if replay != e:
                    raise ValueError("LEDGER_REPLAY_MISMATCH")
            if abs(account.cash-record["cash"]) > 1e-6 or account.holdings != record["positions"]:
                raise ValueError("LEDGER_BALANCE_MISMATCH")
            check = council(account.statement())
        except (ValueError, KeyError, TypeError):
            check = {"status": "REJECT_AND_QUARANTINE"}
        evaluations[slot["active"]] = readiness(
            worker, record, marks_for(rows, worker, slot["active"]), check)
    p = Path(root)
    (p / "approval_readiness.json").write_text(json.dumps(
        {"schema": 1, "council": evaluations,
         "live_order_permissions_unchanged": True, "approval_candidates": []},
        indent=2) + "\n", encoding="utf-8")
    lines = ["# Council — real-money approval readiness", "",
             "No strategy can be guaranteed profitable. No model or council",
             "may enable live trading or approve its own evidence.", "",
             "| Paper generation | Status | Main blocker |",
             "|---|---|---|"]
    for generation, check in evaluations.items():
        lines.append("| {} | {} | {} |".format(
            generation, check["status"], check["blockers"][-2]))
    (p / "APPROVAL_READINESS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return evaluations
