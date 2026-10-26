"""
options_signal_frequency.py — Daily ENTRY counts per strategy from options run logs.

Headline metric: unique (strategy_id, underlying_symbol, date).
Raw log-line counts kept as a secondary debug table.

Outputs:
  logs/options_trial/reports/signal_frequency.md

Usage:
  python scripts/options_signal_frequency.py
"""
from __future__ import annotations

import math
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_lab import TRIAL_ROOT, ensure_trial_layout

STRATEGIES = [
    "S163", "S164", "S165", "S166", "S167", "S168",
    "S169", "S170", "S171", "S172", "S175",
    "S173", "S174",
]
EXIT_RATE_PROXY = 0.80  # rough: fraction of unique entries that become exits
TARGET_EXITS = 30

# ENTRY [b20|c020_s173_w1_0928_1005_r2|S173] BUY 1x AAL260717C00015000 ...
_RE_ENTRY_BRACKET = re.compile(
    r"ENTRY\s*\[[^\]]*\|(S\d{3})\]",
    re.IGNORECASE,
)
_RE_ENTRY_PLAIN = re.compile(
    r"\bENTRY\b[^\n]{0,80}?\b(S\d{3})\b",
    re.IGNORECASE,
)
_RE_STRATEGY_EQ = re.compile(
    r"(?:strategy[_ ]?id|strategy)\s*[=:]\s*(S\d{3})",
    re.IGNORECASE,
)
# Window tag from controlled-layout profile name: ..._w2_1005_1045_r1
# Note: do not use \b before w — underscore is a word char in Python.
_RE_WINDOW = re.compile(r"(?<![A-Za-z0-9])(w[1-4])_\d{4}_\d{4}", re.IGNORECASE)
# Underlying from OCC: AAL260717C00015000 or "BUY 1x AAL260717..."
_RE_OCC = re.compile(
    r"\b([A-Z]{1,6})\d{6}[CP]\d{8}\b",
)
_RE_SYMBOL_EQ = re.compile(
    r"(?:underlying|symbol)\s*[=:]\s*([A-Z]{1,6})\b",
    re.IGNORECASE,
)
_RE_PENDING_ID = re.compile(r"pending\s+id=([0-9a-fA-F\-]{8,})", re.IGNORECASE)
_RE_ORDER_ID = re.compile(r"\bid=([0-9a-fA-F\-]{8,})", re.IGNORECASE)

WINDOWS = ["w1", "w2", "w3", "w4"]


def _extract_window(line: str) -> str | None:
    """Extract w1–w4 from controlled-layout profile tag in ENTRY line."""
    m = _RE_WINDOW.search(line)
    if m:
        return m.group(1).lower()
    return None


def _extract_strategy(line: str) -> str | None:
    if "ENTRY" not in line.upper():
        return None
    for rx in (_RE_ENTRY_BRACKET, _RE_STRATEGY_EQ, _RE_ENTRY_PLAIN):
        m = rx.search(line)
        if m:
            sid = m.group(1).upper()
            if sid in STRATEGIES:
                return sid
    return None


def _extract_underlying(line: str) -> str | None:
    m = _RE_OCC.search(line.upper())
    if m:
        return m.group(1)
    m = _RE_SYMBOL_EQ.search(line)
    if m:
        return m.group(1).upper()
    return None


def _raw_line_key(line: str, sid: str, day: str) -> str:
    m = _RE_PENDING_ID.search(line) or _RE_ORDER_ID.search(line)
    if m:
        return f"{day}|{sid}|{m.group(1)}"
    # Precompute — older Python forbids backslashes inside f-string expressions.
    compact = re.sub(r"\s+", " ", line.strip())[:160]
    return f"{day}|{sid}|{compact}"


def collect_counts() -> tuple[
    dict[str, dict[str, int]],
    dict[str, dict[str, int]],
    dict[str, int],
    dict[str, int],
    dict[str, dict[str, int]],
]:
    """Return unique_counts, raw_counts, unique_totals, raw_totals, window_unique.

    window_unique[window][sid] = unique (strategy, underlying, date) in that window.
    """
    ensure_trial_layout()
    runs_dir = TRIAL_ROOT / "runs"
    unique_counts: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    raw_counts: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    window_unique: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    unique_seen: set[str] = set()
    raw_seen: set[str] = set()
    window_seen: set[str] = set()
    unique_totals: dict[str, int] = defaultdict(int)
    raw_totals: dict[str, int] = defaultdict(int)

    if not runs_dir.exists():
        z = {s: 0 for s in STRATEGIES}
        return {}, {}, z, z, {}

    for path in sorted(runs_dir.glob("*.log")):
        day = path.stem
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

            raw_key = _raw_line_key(line, sid, day)
            if raw_key not in raw_seen:
                raw_seen.add(raw_key)
                raw_counts[day][sid] += 1
                raw_totals[sid] += 1

            sym = _extract_underlying(line)
            if not sym:
                continue
            ukey = f"{day}|{sid}|{sym}"
            if ukey not in unique_seen:
                unique_seen.add(ukey)
                unique_counts[day][sid] += 1
                unique_totals[sid] += 1

            win = _extract_window(line)
            if win:
                wkey = f"{day}|{sid}|{sym}|{win}"
                if wkey not in window_seen:
                    window_seen.add(wkey)
                    window_unique[win][sid] += 1

    return (
        dict(unique_counts),
        dict(raw_counts),
        {s: int(unique_totals.get(s, 0)) for s in STRATEGIES},
        {s: int(raw_totals.get(s, 0)) for s in STRATEGIES},
        {w: dict(window_unique.get(w, {})) for w in WINDOWS},
    )


def _est_days_to_n30(avg_unique_per_active: float) -> str:
    if avg_unique_per_active <= 0:
        return "inf (no unique entries yet)"
    # ceil(30 / (avg * 0.80))
    denom = avg_unique_per_active * EXIT_RATE_PROXY
    if denom <= 0:
        return "inf"
    days = math.ceil(TARGET_EXITS / denom)
    return f"~{days} active signal-days"


def _md_table(counts: dict[str, dict[str, int]], title: str) -> list[str]:
    days = sorted(counts.keys())
    hdr = "| Date       | " + " | ".join(STRATEGIES) + " | Total |"
    sep = "|------------|" + "|".join(["-----:" for _ in STRATEGIES]) + "|------:|"
    lines = [
        f"### {title}",
        "",
        hdr,
        sep,
    ]
    for day in days:
        row = counts[day]
        vals = [int(row.get(s, 0)) for s in STRATEGIES]
        cells = " | ".join(f"{v:4d}" for v in vals)
        lines.append(f"| {day} | {cells} | {sum(vals):5d} |")
    if not days:
        zeros = " | ".join(["   0" for _ in STRATEGIES])
        lines.append(f"| _(no run logs)_ | {zeros} |     0 |")
    lines.append("")
    return lines


def build_report(
    unique_counts: dict[str, dict[str, int]],
    raw_counts: dict[str, dict[str, int]],
    unique_totals: dict[str, int],
    raw_totals: dict[str, int],
    window_unique: dict[str, dict[str, int]] | None = None,
) -> str:
    days = sorted(set(unique_counts.keys()) | set(raw_counts.keys()))
    lines = [
        "# Options signal frequency",
        "",
        f"_Generated {datetime.now().isoformat()}_",
        "",
        "Headline counts are **unique (strategy, underlying, date)** from "
        "`ENTRY` lines in `logs/options_trial/runs/*.log`.",
        "Raw log-line counts (multi-bucket duplicates) are shown below for debug.",
        "",
    ]
    lines.extend(_md_table(unique_counts, "Unique underlying symbols per day (headline)"))

    lines.extend(["## Per-strategy summary (unique underlyings)", ""])
    lines.append(
        "| Strategy | Unique entries | Active days | Avg unique / active day | "
        "Est. active days to n=30 exits* |"
    )
    lines.append(
        "|----------|---------------:|------------:|------------------------:|"
        "--------------------------------|"
    )
    for sid in STRATEGIES:
        total = unique_totals.get(sid, 0)
        active = sum(1 for d in days if unique_counts.get(d, {}).get(sid, 0) > 0)
        avg = (total / active) if active else 0.0
        est = _est_days_to_n30(avg)
        if total * EXIT_RATE_PROXY >= TARGET_EXITS:
            est = "0 (proxy already >=30 exits)"
        lines.append(f"| {sid} | {total} | {active} | {avg:.1f} | {est} |")

    lines.extend(
        [
            "",
            f"\\* Formula: `ceil({TARGET_EXITS} / (avg_unique_per_active_day * "
            f"{EXIT_RATE_PROXY:.0%}))`. Update when real exit rates are known.",
            "",
            "## Signal frequency by window (all time, unique strategy×symbol×date×window)",
            "",
            "| Window | " + " | ".join(STRATEGIES) + " | Total |",
            "|--------|" + "|".join(["-----:" for _ in STRATEGIES]) + "|------:|",
        ]
    )
    wu = window_unique or {}
    for win in WINDOWS:
        row = wu.get(win, {})
        vals = [int(row.get(s, 0)) for s in STRATEGIES]
        cells = " | ".join(f"{v:4d}" for v in vals)
        lines.append(f"| {win}     | {cells} | {sum(vals):5d} |")
    if not any(wu.get(w) for w in WINDOWS):
        lines.extend(
            [
                "",
                "_No window tags found in ENTRY lines "
                "(expected profile tag like `w2_1005_1045`)._",
            ]
        )
    else:
        lines.extend(
            [
                "",
                "Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · "
                "w3 10:45–11:20 · w4 11:20–11:35. "
                "Parsed from controlled-layout profile names in ENTRY log lines.",
            ]
        )

    lines.extend(
        [
            "",
            "## Raw vs unique totals",
            "",
            "| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |",
            "|----------|-------------------------------------------------:|--------------------------:|",
        ]
    )
    for sid in STRATEGIES:
        lines.append(
            f"| {sid} | {raw_totals.get(sid, 0)} | {unique_totals.get(sid, 0)} |"
        )
    lines.append("")
    lines.extend(_md_table(raw_counts, "Raw log lines per day (debug / multi-bucket)"))

    lines.extend(
        [
            "## Notes",
            "",
            "- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 "
            "were starved — expect zeros until a post-fix entry-window gap-down day.",
            "- Controlled layout places one ENTRY per matching bucket×strategy; "
            "raw counts inflate, unique underlyings do not.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    try:
        unique_counts, raw_counts, unique_totals, raw_totals, window_unique = (
            collect_counts()
        )
        md = build_report(
            unique_counts, raw_counts, unique_totals, raw_totals, window_unique
        )
        out_dir = TRIAL_ROOT / "reports"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "signal_frequency.md"
        out_path.write_text(md, encoding="utf-8")
        enc = sys.stdout.encoding or "utf-8"
        print(md.encode("utf-8", errors="replace").decode(enc, errors="replace"))
        print(f"\nWrote {out_path}")
    except Exception as e:
        print(f"signal_frequency report failed (non-fatal): {e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
