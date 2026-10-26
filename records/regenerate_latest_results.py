#!/usr/bin/env python3
"""Regenerate records/current/latest-results.md from newest report files."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "records" / "current" / "latest-results.md"

CANDIDATES = [
    ROOT / "logs" / "options_trial" / "reports",
    ROOT / "logs" / "action_runs" / "reports",
    ROOT / "logs" / "options_live_micro",
    ROOT / "logs" / "research",
    ROOT / "records" / "research",
]


def newest(paths: list[Path], patterns: tuple[str, ...]) -> list[tuple[float, Path]]:
    found: list[tuple[float, Path]] = []
    for base in paths:
        if not base.is_dir():
            continue
        for pat in patterns:
            for p in base.rglob(pat):
                if p.is_file():
                    found.append((p.stat().st_mtime, p))
    found.sort(reverse=True)
    return found


def main() -> None:
    lines = [
        "# Latest results (regenerated pointer)",
        "",
        f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "Active ledgers remain under `logs/`. This file only points at recent artifacts.",
        "",
        "## Newest report-like files",
        "",
    ]
    hits = newest(CANDIDATES, ("*.md", "*.csv", "*.json"))
    if not hits:
        lines.append("_No report files found locally._")
    else:
        lines.append("| mtime (UTC) | path |")
        lines.append("|---|---|")
        for mtime, p in hits[:25]:
            ts = datetime.fromtimestamp(mtime, timezone.utc).strftime("%Y-%m-%d %H:%M")
            rel = p.relative_to(ROOT).as_posix()
            lines.append(f"| {ts} | `{rel}` |")
    lines.extend(
        [
            "",
            "## Canonical live pointers",
            "",
            "- Paper selection/DQ: `logs/options_trial/reports/`",
            "- Live micro: `logs/options_live_micro/`",
            "- Rubber Band daily: `logs/daily/`",
            "- Research copies: `records/research/` (+ original `logs/research/`)",
            "",
            "Regenerate: `python records/regenerate_latest_results.py`",
            "",
        ]
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
