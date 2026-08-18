"""
Append one GitHub Actions run into the daily comprehensive review + run index.

Slim review sections (tail of logs + links to full per-run files) avoid multi-MB
markdown growth and bash heredoc failures in CI.
"""
from __future__ import annotations

import csv
import os
import sys
from pathlib import Path

TAIL_LINES = int(os.getenv("REVIEW_LOG_TAIL_LINES", "80"))
RUN_INDEX_FIELDS = [
    "run_stamp",
    "run_number",
    "run_id",
    "live_exit",
    "live_options_exit",
    "options_exit",
    "live_duration_s",
    "live_options_duration_s",
    "options_duration_s",
    "event_type",
]


def _tail(path: Path, n: int) -> str:
    if not path.exists():
        return f"(missing {path.as_posix()})"
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as exc:
        return f"(read error {path.name}: {exc})"
    if len(lines) <= n:
        return "\n".join(lines)
    omitted = len(lines) - n
    body = "\n".join(lines[-n:])
    return f"... ({omitted} earlier lines - see full log file)\n{body}"


def _ensure_review_header(path: Path, run_day: str) -> None:
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"# Daily Comprehensive Action Review - {run_day}\n\n"
        "_Auto-generated from GitHub Actions run output. "
        "Each run appends a summary; full stdout is in linked per-run log files._\n",
        encoding="utf-8",
    )


def _append_review_section(
    path: Path,
    *,
    run_stamp: str,
    run_day: str,
    run_number: str,
    run_id: str,
    repo: str,
    live_exit: str,
    live_options_exit: str,
    options_exit: str,
    live_duration_s: str,
    live_options_duration_s: str,
    options_duration_s: str,
    live_log: Path,
    live_options_log: Path,
    options_log: Path,
    paper_enabled: bool,
) -> None:
    _ensure_review_header(path, run_day)
    header = f"## Run {run_stamp}"
    existing = path.read_text(encoding="utf-8", errors="replace")
    if header in existing:
        print(f"Review section already present for {run_stamp}; skip duplicate append")
        return

    lines = [
        header,
        "",
        f"- UTC timestamp: `{run_stamp}`",
        f"- GitHub run: [#{run_number}](https://github.com/{repo}/actions/runs/{run_id})",
        f"- Run id: `{run_id}`",
        f"- Live bot: exit=`{live_exit}`, duration=`{live_duration_s}s`",
        f"- Live options: exit=`{live_options_exit}`, duration=`{live_options_duration_s}s`",
        f"- Paper options: exit=`{options_exit}`, duration=`{options_duration_s}s`",
        f"- Full logs: `{live_log.as_posix()}`, `{live_options_log.as_posix()}`, `{options_log.as_posix()}`",
        "",
    ]

    if paper_enabled:
        dq = Path("logs/options_trial/reports/latest_data_quality_snippet.md")
        if dq.exists():
            lines.extend(["", dq.read_text(encoding="utf-8", errors="replace").strip(), ""])
        runs_jsonl = Path("logs/options_trial/runs.jsonl")
        if runs_jsonl.exists():
            last = runs_jsonl.read_text(encoding="utf-8", errors="replace").splitlines()
            if last:
                lines.extend(["- Options structured summary (latest JSON):", "```json", last[-1], "```", ""])

    for title, log_path in (
        ("Live bot (tail)", live_log),
        ("Live options micro (tail)", live_options_log),
        ("Paper options bot (tail)", options_log),
    ):
        lines.extend([
            f"### {title}",
            "",
            "```text",
            _tail(log_path, TAIL_LINES),
            "```",
            "",
        ])

    lines.extend(["---", ""])
    with path.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines))


def _read_run_index(path: Path) -> tuple[list[str], list[dict]]:
    if not path.exists():
        return RUN_INDEX_FIELDS, []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = list(reader.fieldnames or RUN_INDEX_FIELDS)
        rows = list(reader)
    return fields, rows


def _normalize_row(row: dict) -> dict:
    """Map legacy / misaligned rows onto the canonical 10-column schema."""
    out = {k: str(row.get(k) or "").strip() for k in RUN_INDEX_FIELDS}
    ev = out.get("event_type", "")
    if ev.isdigit():
        out["live_options_duration_s"] = ev
        out["options_duration_s"] = "0"
        out["event_type"] = "workflow_dispatch"
        out["live_duration_s"] = str(row.get("options_duration_s") or out.get("live_duration_s") or "0")
        out["live_options_exit"] = "0"
    elif "live_options_exit" not in (row.keys() or []):
        out["live_options_exit"] = "0"
        out["live_options_duration_s"] = str(row.get("options_duration_s") or "0")
        out["options_duration_s"] = "0"
    if not out.get("event_type"):
        out["event_type"] = "workflow_dispatch"
    for k in ("run_stamp", "run_number", "run_id", "live_exit", "options_exit"):
        if row.get(k) not in (None, ""):
            out[k] = str(row[k]).strip()
    return out


def _append_run_index(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    _, rows = _read_run_index(path)
    norm = _normalize_row(row)
    stamp = norm.get("run_stamp", "")
    if not stamp:
        print("WARN: run_stamp missing; skip run index append")
        return
    merged = [_normalize_row(r) for r in rows if str(r.get("run_stamp", "")).strip()]
    if any(r.get("run_stamp") == stamp for r in merged):
        print(f"Run index already has {stamp}; skip duplicate")
    else:
        merged.append(norm)
    merged.sort(key=lambda r: str(r.get("run_stamp", "")))
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=RUN_INDEX_FIELDS, extrasaction="ignore")
        w.writeheader()
        for r in merged:
            w.writerow(r)


def main() -> int:
    run_day = os.environ.get("RUN_DAY", "")
    run_stamp = os.environ.get("RUN_STAMP", "")
    if not run_day or not run_stamp:
        print("ERROR: RUN_DAY and RUN_STAMP must be set", file=sys.stderr)
        return 1

    review_doc = Path(os.environ.get(
        "DAY_REVIEW_DOC",
        f"logs/action_runs/reports/{run_day}_comprehensive_review.md",
    ))
    run_index = Path(os.environ.get(
        "DAY_RUN_INDEX",
        f"logs/action_runs/reports/{run_day}_run_index.csv",
    ))
    live_log = Path(os.environ.get("LIVE_LOG", ""))
    live_options_log = Path(os.environ.get("LIVE_OPTIONS_LOG", ""))
    options_log = Path(os.environ.get("OPTIONS_LOG", ""))

    try:
        _append_review_section(
            review_doc,
            run_stamp=run_stamp,
            run_day=run_day,
            run_number=os.environ.get("RUN_NUMBER", "?"),
            run_id=os.environ.get("RUN_ID", "?"),
            repo=os.environ.get("GITHUB_REPOSITORY", "unknown/unknown"),
            live_exit=os.environ.get("LIVE_BOT_EXIT", "0"),
            live_options_exit=os.environ.get("LIVE_OPTIONS_EXIT", "0"),
            options_exit=os.environ.get("OPTIONS_BOT_EXIT", "0"),
            live_duration_s=os.environ.get("LIVE_BOT_DURATION_S", "0"),
            live_options_duration_s=os.environ.get("LIVE_OPTIONS_DURATION_S", "0"),
            options_duration_s=os.environ.get("OPTIONS_BOT_DURATION_S", "0"),
            live_log=live_log,
            live_options_log=live_options_log,
            options_log=options_log,
            paper_enabled=os.environ.get("OPTIONS_PAPER_ENABLED", "0") == "1",
        )
        _append_run_index(run_index, {
            "run_stamp": run_stamp,
            "run_number": os.environ.get("RUN_NUMBER", ""),
            "run_id": os.environ.get("RUN_ID", ""),
            "live_exit": os.environ.get("LIVE_BOT_EXIT", "0"),
            "live_options_exit": os.environ.get("LIVE_OPTIONS_EXIT", "0"),
            "options_exit": os.environ.get("OPTIONS_BOT_EXIT", "0"),
            "live_duration_s": os.environ.get("LIVE_BOT_DURATION_S", "0"),
            "live_options_duration_s": os.environ.get("LIVE_OPTIONS_DURATION_S", "0"),
            "options_duration_s": os.environ.get("OPTIONS_BOT_DURATION_S", "0"),
            "event_type": os.environ.get("GITHUB_EVENT_NAME", "workflow_dispatch"),
        })
    except Exception as exc:
        print(f"ERROR appending action run review: {exc}", file=sys.stderr)
        return 1

    print(f"Appended review for {run_stamp} -> {review_doc}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
