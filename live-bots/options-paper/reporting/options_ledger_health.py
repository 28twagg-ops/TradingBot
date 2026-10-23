"""
options_ledger_health.py — Cross-check master ledger vs lab_state for stuck lots.

Outputs:
  logs/options_trial/reports/ledger_health.md

Always exits 0 (non-fatal for GHA).
"""
from __future__ import annotations

import csv
import json
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_lab import (
    LEDGER_PATH,
    ORPHAN_PROFILE,
    ORPHAN_STRATEGY,
    STATE_PATH,
    TRIAL_ROOT,
    ensure_trial_layout,
)

EXIT_DAYS_MAX = 3
STUCK_BUFFER_DAYS = 2  # weekend/holiday → stuck if age > EXIT_DAYS_MAX+2
# Fill-attribution / OrderStatus.value fix era started ~2026-07-06.
BASELINE_CUTOFF = date.fromisoformat("2026-07-06")
# Ledger lot_id pairing was still noisy through 2026-07-14 (optimistic logging /
# reconcile churn on Jul 13-14). WARN only on unmatched entries AFTER this
# inclusive date so the daily monitor stays actionable (pre/transition debt = INFO).
STABLE_AFTER = date.fromisoformat("2026-07-21")  # advanced 25B: covers S173 last entries 2026-07-20


def _f(v, d=0.0) -> float:
    try:
        return float(v)
    except (TypeError, ValueError):
        return d


def _day(ts: str, fallback: str = "") -> str:
    s = str(ts or "")
    if len(s) >= 10 and s[4] == "-" and s[7] == "-":
        return s[:10]
    return str(fallback or "")[:10]


def _parse_day(d: str) -> date | None:
    try:
        return date.fromisoformat(d[:10])
    except ValueError:
        return None


def _is_orphan_attr(r: dict) -> bool:
    sid = str(r.get("strategy_id") or "")
    profile = str(r.get("profile") or "")
    return sid == ORPHAN_STRATEGY or profile == ORPHAN_PROFILE


def _load_ledger() -> list[dict]:
    if not LEDGER_PATH.exists():
        return []
    with LEDGER_PATH.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def _load_state() -> dict | None:
    if not STATE_PATH.exists():
        print(f"WARN: state file missing: {STATE_PATH}")
        return None
    try:
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"WARN: corrupt/unreadable state file: {e}")
        return None


def analyze(as_of: date | None = None) -> dict:
    as_of = as_of or date.today()
    stuck_after = EXIT_DAYS_MAX + STUCK_BUFFER_DAYS
    rows = _load_ledger()

    # Deduplicate entries by (bucket, strategy, occ, entry_day) — historical
    # ledgers often re-logged the same fill under new lot_ids.
    entries_by_key: dict[str, dict] = {}
    entries_by_lot: dict[str, dict] = {}
    exits_by_lot: dict[str, list[dict]] = {}
    exits_by_key: dict[str, list[dict]] = {}

    for r in rows:
        if _is_orphan_attr(r):
            continue
        lot_id = str(r.get("lot_id") or "").strip()
        ev = r.get("event")
        day = _day(r.get("ts", ""), r.get("date", ""))
        key = f"{r.get('bucket_id')}|{r.get('strategy_id')}|{r.get('occ') or r.get('symbol')}|{day}"

        if ev == "entry":
            if lot_id:
                prev = entries_by_lot.get(lot_id)
                if prev is None or day < _day(prev.get("ts", "")):
                    entries_by_lot[lot_id] = r
            prev_k = entries_by_key.get(key)
            if prev_k is None or day <= _day(prev_k.get("ts", "")):
                entries_by_key[key] = r
        elif ev == "exit":
            if lot_id:
                exits_by_lot.setdefault(lot_id, []).append(r)
            # Exit key uses exit day — also index by occ/bucket/strategy without day
            soft = f"{r.get('bucket_id')}|{r.get('strategy_id')}|{r.get('occ') or r.get('symbol')}"
            exits_by_key.setdefault(soft, []).append(r)

    def has_exit_for_entry(ent: dict) -> bool:
        lot_id = str(ent.get("lot_id") or "")
        if lot_id and lot_id in exits_by_lot:
            return True
        soft = f"{ent.get('bucket_id')}|{ent.get('strategy_id')}|{ent.get('occ') or ent.get('symbol')}"
        ed = _parse_day(_day(ent.get("ts", ""), ent.get("date", "")))
        for ex in exits_by_key.get(soft, []):
            xd = _parse_day(_day(ex.get("ts", ""), ex.get("date", "")))
            if ed is None or xd is None:
                return True
            if xd >= ed:
                return True
        return False

    orphaned_lots: list[dict] = []
    pre_cutoff_debt: list[dict] = []
    transition_debt: list[dict] = []
    for key, ent in entries_by_key.items():
        if has_exit_for_entry(ent):
            continue
        ed = _parse_day(_day(ent.get("ts", ""), ent.get("date", "")))
        if ed is None:
            continue
        age = (as_of - ed).days
        if age <= stuck_after:
            continue
        row = {
            "lot_id": ent.get("lot_id") or "?",
            "strategy_id": ent.get("strategy_id") or "?",
            "symbol": ent.get("symbol") or ent.get("occ") or "?",
            "entry_day": ed.isoformat(),
            "age_days": age,
            "key": key,
        }
        if ed < BASELINE_CUTOFF:
            pre_cutoff_debt.append(row)
        elif ed <= STABLE_AFTER:
            transition_debt.append(row)
        else:
            orphaned_lots.append(row)

    state = _load_state()
    state_open: list[dict] = []
    if state is not None:
        for lot in state.get("lots") or []:
            qty = int(_f(lot.get("qty"), 0))
            if qty > 0:
                state_open.append(lot)

    state_open_ids = {str(l.get("lot_id") or "") for l in state_open if l.get("lot_id")}

    # State open lot with no matching ledger entry at all
    state_missing_entry = sorted(
        lid for lid in state_open_ids
        if lid and lid not in entries_by_lot
    )
    # State still open but ledger already has an exit for that lot_id
    state_open_but_exited = sorted(
        lid for lid in state_open_ids if lid in exits_by_lot
    )
    # Current stuck: open in state AND entry age > stuck_after
    current_stuck: list[dict] = []
    for lot in state_open:
        lid = str(lot.get("lot_id") or "")
        ed = _parse_day(str(lot.get("entry_date") or "")[:10])
        if ed is None and lid in entries_by_lot:
            ed = _parse_day(_day(entries_by_lot[lid].get("ts", "")))
        if ed is None:
            continue
        age = (as_of - ed).days
        if age > stuck_after:
            current_stuck.append(
                {
                    "lot_id": lid,
                    "strategy_id": lot.get("strategy_id") or "?",
                    "symbol": lot.get("underlying") or lot.get("occ_symbol") or "?",
                    "entry_day": ed.isoformat(),
                    "age_days": age,
                }
            )

    # Missing exit: post-cutoff deduped entry, no exit, not in state, older than stuck buffer
    missing_exit_records = [
        o for o in orphaned_lots
        if o.get("lot_id") not in state_open_ids
    ]

    closed_lots = sum(1 for lid in entries_by_lot if lid in exits_by_lot)

    return {
        "as_of": as_of.isoformat(),
        "baseline_cutoff": BASELINE_CUTOFF.isoformat(),
        "stable_after": STABLE_AFTER.isoformat(),
        "orphaned_lots": orphaned_lots,
        "orphaned_count": len(orphaned_lots),
        "pre_cutoff_debt": pre_cutoff_debt,
        "pre_cutoff_debt_count": len(pre_cutoff_debt),
        "transition_debt": transition_debt,
        "transition_debt_count": len(transition_debt),
        "current_stuck": current_stuck,
        "current_stuck_count": len(current_stuck),
        "state_ledger_mismatch": state_missing_entry + state_open_but_exited,
        "state_mismatch_count": len(state_missing_entry) + len(state_open_but_exited),
        "missing_exit_records": missing_exit_records,
        "missing_exit_count": len(missing_exit_records),
        "total_open_lots": len(state_open) if state is not None else 0,
        "total_closed_lots": closed_lots,
        "stuck_after_days": stuck_after,
        "state_available": state is not None,
        "generated_at": datetime.now().isoformat(),
    }


def write_report(result: dict) -> Path:
    out_dir = TRIAL_ROOT / "reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "ledger_health.md"

    def st(count: int) -> str:
        return "WARN" if count > 0 else "OK"

    lines = [
        f"# Ledger health — {result['as_of']}",
        "",
        f"_Generated {result['generated_at']}_",
        "",
        f"Stuck threshold: **>{result['stuck_after_days']}** days "
        f"(EXIT_DAYS_MAX={EXIT_DAYS_MAX} + buffer={STUCK_BUFFER_DAYS}).",
        "",
        f"Baseline cutoff: **{result.get('baseline_cutoff', BASELINE_CUTOFF.isoformat())}** "
        "(attribution fix start). "
        f"WARN only after **{result.get('stable_after', STABLE_AFTER.isoformat())}** "
        "(ledger pairing stabilized); earlier unmatched entries = INFO debt.",
        "",
        f"State file: {'OK' if result['state_available'] else 'MISSING/UNREADABLE'}",
        "",
        "| Check                       | Count | Status |",
        "|-----------------------------|------:|--------|",
        f"| Current stuck (state)       | {result['current_stuck_count']:5d} | "
        f"{st(result['current_stuck_count'])} |",
        f"| Orphaned lots (post-stable) | {result['orphaned_count']:5d} | "
        f"{st(result['orphaned_count'])} |",
        f"| Missing exit records (post) | {result['missing_exit_count']:5d} | "
        f"{st(result['missing_exit_count'])} |",
        f"| State/ledger mismatches     | {result['state_mismatch_count']:5d} | "
        f"{st(result['state_mismatch_count'])} |",
        f"| Total open lots             | {result['total_open_lots']:5d} | INFO |",
        f"| Total closed lots           | {result['total_closed_lots']:5d} | INFO |",
        f"| Pre-cutoff audit debt       | {result.get('pre_cutoff_debt_count', 0):5d} | INFO |",
        f"| Transition audit debt       | {result.get('transition_debt_count', 0):5d} | INFO |",
        "",
        "Notes:",
        "- **Current stuck** = open in `lab_state.json` and older than stuck threshold "
        "(actionable).",
        f"- **Post-stable orphaned / missing exits** = actionable WARN "
        f"(entry_date > {STABLE_AFTER.isoformat()}).",
        f"- **Pre-cutoff debt** = entry_date < {BASELINE_CUTOFF.isoformat()} (INFO).",
        f"- **Transition debt** = {BASELINE_CUTOFF.isoformat()}..{STABLE_AFTER.isoformat()} "
        "lot_id churn after attribution fix (INFO, not WARN).",
        "",
    ]

    if result["current_stuck"]:
        lines.append("## Current stuck lots")
        lines.append("")
        lines.append("| lot_id | strategy | symbol | entry_day | age_days |")
        lines.append("|--------|----------|--------|-----------|---------:|")
        for o in result["current_stuck"][:40]:
            lines.append(
                f"| {o['lot_id']} | {o['strategy_id']} | {o['symbol']} | "
                f"{o['entry_day']} | {o['age_days']} |"
            )
        lines.append("")

    if result["orphaned_lots"] and result["orphaned_count"] <= 50:
        lines.append("## Orphaned ledger entries (detail)")
        lines.append("")
        lines.append("| lot_id | strategy | symbol | entry_day | age_days |")
        lines.append("|--------|----------|--------|-----------|---------:|")
        for o in result["orphaned_lots"][:50]:
            lines.append(
                f"| {o['lot_id']} | {o['strategy_id']} | {o['symbol']} | "
                f"{o['entry_day']} | {o['age_days']} |"
            )
        lines.append("")
    elif result["orphaned_count"] > 50:
        lines.append(
            f"_Orphaned ledger detail omitted ({result['orphaned_count']} rows) — "
            "see note above on historical lot_id churn._"
        )
        lines.append("")

    if result["state_ledger_mismatch"]:
        lines.append("## State/ledger mismatches")
        lines.append("")
        for lid in result["state_ledger_mismatch"][:30]:
            lines.append(f"- `{lid}`")
        lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    try:
        ensure_trial_layout()
        result = analyze()
        path = write_report(result)
        print(f"## Ledger health — {result['as_of']}")
        rows = [
            ("Current stuck (state)", result["current_stuck_count"], True),
            ("Orphaned lots (post-stable)", result["orphaned_count"], True),
            ("Missing exit records (post)", result["missing_exit_count"], True),
            ("State/ledger mismatches", result["state_mismatch_count"], True),
            ("Total open lots", result["total_open_lots"], False),
            ("Total closed lots", result["total_closed_lots"], False),
            ("Pre-cutoff audit debt", result.get("pre_cutoff_debt_count", 0), False),
            ("Transition audit debt", result.get("transition_debt_count", 0), False),
        ]
        print("| Check                       | Count | Status |")
        print("|-----------------------------|------:|--------|")
        for name, n, warnable in rows:
            if not warnable:
                st = "INFO"
            else:
                st = "WARN" if n > 0 else "OK"
            mark = " <<<" if st == "WARN" else ""
            print(f"| {name:<27} | {n:5d} | {st} |{mark}")
        print(f"\nWrote {path}")
    except Exception as e:
        print(f"ledger_health failed (non-fatal): {e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
