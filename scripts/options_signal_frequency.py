"""
options_signal_frequency.py — Daily ENTRY counts per strategy from options run logs.

Outputs:
  logs/options_trial/reports/signal_frequency.md

Usage:
  python scripts/options_signal_frequency.py
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_lab import TRIAL_ROOT, ensure_trial_layout

STRATEGIES = ["S163", "S165", "S166", "S173", "S174"]
EXIT_RATE_PROXY = 0.60  # rough: fraction of entries that become exits
TARGET_EXITS = 30

# ENTRY [b20|c020_s173_w1_0928_1005_r2|S173] BUY 1x AAL...
_RE_ENTRY_BRACKET = re.compile(
    r"ENTRY\s*\[[^\]]*\|(S\d{3})\]",
    re.IGNORECASE,
)
# ENTRY S165 | AVGO ...  OR  ENTRY S165 BUY ...
_RE_ENTRY_PLAIN = re.compile(
    r"\bENTRY\b[^\n]{0,80}?\b(S\d{3})\b",
    re.IGNORECASE,
)
# options entry: strategy=S165 symbol=AVGO
_RE_STRATEGY_EQ = re.compile(
    r"(?:strategy[_ ]?id|strategy)\s*[=:]\s*(S\d{3})",
    re.IGNORECASE,
)
# pending id=... for dedupe within a day file
_RE_PENDING_ID = re.compile(r"pending\s+id=([0-9a-fA-F\-]{8,})", re.IGNORECASE)
_RE_ORDER_ID = re.compile(r"\bid=([0-9a-fA-F\-]{8,})", re.IGNORECASE)


def _extract_strategy(line: str) -> str | None:
    if "ENTRY" not in line.upper() and "signal" not in line.lower():
        # Prefer ENTRY; also allow explicit strategy= on signal lines with S###.
        m = _RE_STRATEGY_EQ.search(line)
        if m and "signal" in line.lower():
            sid = m.group(1).upper()
            return sid if sid in STRATEGIES else None
        return None

    for rx in (_RE_ENTRY_BRACKET, _RE_STRATEGY_EQ, _RE_ENTRY_PLAIN):
        m = rx.search(line)
        if m:
            sid = m.group(1).upper()
            if sid in STRATEGIES:
                return sid
    return None


def _dedupe_key(line: str, sid: str, day: str) -> str:
    m = _RE_PENDING_ID.search(line) or _RE_ORDER_ID.search(line)
    if m:
        return f"{day}|{sid}|{m.group(1)}"
    # Fallback: normalize whitespace
    return f"{day}|{sid}|{re.sub(r'\s+', ' ', line.strip())[:160]}"


def collect_counts() -> tuple[dict[str, dict[str, int]], dict[str, int]]:
    """Return (counts[day][sid], totals[sid])."""
    ensure_trial_layout()
    runs_dir = TRIAL_ROOT / "runs"
    counts: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    seen: set[str] = set()
    totals: dict[str, int] = defaultdict(int)

    if not runs_dir.exists():
        return {}, {s: 0 for s in STRATEGIES}

    for path in sorted(runs_dir.glob("*.log")):
        day = path.stem  # YYYY-MM-DD
        if not re.match(r"\d{4}-\d{2}-\d{2}$", day):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            print(f"WARN: could not read {path}: {e}")
            continue
        for line in text.splitlines():
            if "ENTRY" not in line.upper():
                continue
            sid = _extract_strategy(line)
            if not sid:
                continue
            key = _dedupe_key(line, sid, day)
            if key in seen:
                continue
            seen.add(key)
            counts[day][sid] += 1
            totals[sid] += 1

    return dict(counts), {s: int(totals.get(s, 0)) for s in STRATEGIES}


def _est_days_to_n30(total_entries: int, active_days: int, avg_per_active: float) -> str:
    if avg_per_active <= 0 or active_days <= 0:
        if total_entries == 0:
            return "inf (no entries yet)"
        return "n/a"
    exits_est = total_entries * EXIT_RATE_PROXY
    if exits_est >= TARGET_EXITS:
        return "0 (proxy already >=30 exits)"
    need = TARGET_EXITS - exits_est
    # expected exits per active day
    exits_per_active = avg_per_active * EXIT_RATE_PROXY
    if exits_per_active <= 0:
        return "inf"
    # active days are sparse — scale by observed active-day frequency if possible
    days_needed = need / exits_per_active
    return f"~{days_needed:.0f} active signal-days (~{days_needed * 2:.0f} calendar trading days @ ~50% hit rate)"


def build_report(counts: dict[str, dict[str, int]], totals: dict[str, int]) -> str:
    days = sorted(counts.keys())
    lines = [
        f"# Options signal frequency",
        "",
        f"_Generated {datetime.now().isoformat()}_",
        "",
        "Counts are unique ENTRY events from `logs/options_trial/runs/*.log` "
        "(deduped by pending/order id when present).",
        "",
        "| Date       | S163 | S165 | S166 | S173 | S174 | Total |",
        "|------------|-----:|-----:|-----:|-----:|-----:|------:|",
    ]
    for day in days:
        row = counts[day]
        vals = [int(row.get(s, 0)) for s in STRATEGIES]
        lines.append(
            f"| {day} | {vals[0]:4d} | {vals[1]:4d} | {vals[2]:4d} | "
            f"{vals[3]:4d} | {vals[4]:4d} | {sum(vals):5d} |"
        )
    if not days:
        lines.append("| _(no run logs)_ | 0 | 0 | 0 | 0 | 0 | 0 |")

    lines.extend(["", "## Per-strategy summary", ""])
    lines.append("| Strategy | Total entries | Active days | Avg / active day | Est. days to n=30 exits* |")
    lines.append("|----------|--------------:|------------:|-----------------:|--------------------------|")

    for sid in STRATEGIES:
        total = totals.get(sid, 0)
        active = sum(1 for d in days if counts[d].get(sid, 0) > 0)
        avg = (total / active) if active else 0.0
        est = _est_days_to_n30(total, active, avg)
        lines.append(
            f"| {sid} | {total} | {active} | {avg:.1f} | {est} |"
        )

    lines.extend(
        [
            "",
            f"\\* Proxy assumes {EXIT_RATE_PROXY:.0%} of entries become exits; "
            f"target = {TARGET_EXITS} exits. Update when real exit rates are known.",
            "",
            "## Notes",
            "",
            "- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 "
            "were starved by one-hit-per-symbol priority — expect zeros until fix is live.",
            "- Controlled layout places one ENTRY per matching bucket×strategy, so "
            "a single gap-down symbol can produce many ENTRY rows for S165 (etc.).",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    try:
        counts, totals = collect_counts()
        md = build_report(counts, totals)
        out_dir = TRIAL_ROOT / "reports"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "signal_frequency.md"
        out_path.write_text(md, encoding="utf-8")
        print(md.encode("utf-8", errors="replace").decode(sys.stdout.encoding or "utf-8", errors="replace"))
        print(f"\nWrote {out_path}")
    except Exception as e:
        print(f"signal_frequency report failed (non-fatal): {e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
