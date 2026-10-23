#!/usr/bin/env python3
"""Fix REPO_ROOT / logs path depth after package nesting."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

FILES = [
    "live-bots/options-paper/bot/options_morning_bot.py",
    "live-bots/options-paper/bot/init_options_trial.py",
    "live-bots/options-paper/bot/options_reconcile.py",
    "live-bots/options-paper/lab/options_lab.py",
    "live-bots/options-paper/lab/options_universe.py",
    "live-bots/options-paper/reporting/generate_dashboard.py",
    "live-bots/options-paper/reporting/generate_review_doc.py",
    "live-bots/options-micro/options_live_micro.py",
    "live-bots/shared/options_data_collector.py",
    "live-bots/shared/data_quality_monitor.py",
    "live-bots/shared/first_hour_collector.py",
    "live-bots/shared/api_probe_options.py",
    "live-bots/shared/local_docs.py",
    "live-bots/shared/benchmark_run.py",
    "research/market-research/crypto_rainbow_backtest.py",
    "research/market-research/midcap_longterm_analysis.py",
    "research/market-research/midcap_yoy_analysis.py",
    "research/other-studies/run_historical_parallel.py",
    "research/other-studies/run_enrich_parallel.py",
    "research/other-studies/run_rank_top5_parallel.py",
    "research/other-studies/run_options_research.py",
    "research/other-studies/historical_data_fetcher.py",
    "research/other-studies/strategy_parity_check.py",
    "research/other-studies/analyze_stop_overshoots.py",
    "research/other-studies/sim_pdt_schedule.py",
    "research/other-studies/generate_june10_report.py",
]

BOOTSTRAP = """\
try:
    from repo_root import find_repo_root
except ImportError:
    import sys as _sys
    from pathlib import Path as _Path
    _sys.path.insert(0, str(_Path(__file__).resolve().parents[{shared_depth}] / "live-bots" / "shared"))
    from repo_root import find_repo_root
"""

ASSIGN_PATTERNS = [
    (
        re.compile(r"^(\s*)REPO_ROOT\s*=\s*Path\(__file__\)\.resolve\(\)\.parent\.parent\s*$", re.M),
        r"\1REPO_ROOT = find_repo_root(Path(__file__))",
    ),
    (
        re.compile(r"^(\s*)REPO\s*=\s*Path\(__file__\)\.resolve\(\)\.parent\.parent\s*$", re.M),
        r"\1REPO = find_repo_root(Path(__file__))",
    ),
    (
        re.compile(r"^(\s*)GIT_ROOT\s*=\s*Path\(__file__\)\.resolve\(\)\.parent\.parent.*$", re.M),
        r"\1GIT_ROOT = find_repo_root(Path(__file__))",
    ),
    (
        re.compile(r"^(\s*)GIT\s*=\s*Path\(__file__\)\.resolve\(\)\.parent\.parent\s*$", re.M),
        r"\1GIT = find_repo_root(Path(__file__))",
    ),
    (
        re.compile(r"^(\s*)GIT_REPO\s*=\s*Path\(__file__\)\.resolve\(\)\.parent\.parent\s*$", re.M),
        r"\1GIT_REPO = find_repo_root(Path(__file__))",
    ),
    (
        re.compile(r"^(\s*)_REPO_ROOT\s*=\s*Path\(__file__\)\.resolve\(\)\.parent\.parent\s*$", re.M),
        r"\1_REPO_ROOT = find_repo_root(Path(__file__))",
    ),
    (
        re.compile(r"^(\s*)ROOT\s*=\s*Path\(__file__\)\.resolve\(\)\.parent\.parent\s*$", re.M),
        r"\1ROOT = find_repo_root(Path(__file__))",
    ),
    (
        re.compile(r"^(\s*)ROOT\s*=\s*Path\(__file__\)\.resolve\(\)\.parents\[1\]\s*$", re.M),
        r"\1ROOT = find_repo_root(Path(__file__))",
    ),
    (
        re.compile(
            r'^(\s*)OUT\s*=\s*Path\(__file__\)\.resolve\(\)\.parent\.parent\s*/\s*"logs"\s*/\s*"research"\s*$',
            re.M,
        ),
        r'\1OUT = find_repo_root(Path(__file__)) / "logs" / "research"',
    ),
    (
        re.compile(
            r'^(\s*)ROOT\s*=\s*Path\(__file__\)\.resolve\(\)\.parent\.parent\s*/\s*"logs"\s*/\s*"options_live_micro"\s*$',
            re.M,
        ),
        r'\1ROOT = find_repo_root(Path(__file__)) / "logs" / "options_live_micro"',
    ),
]

INLINE = [
    (
        re.compile(r'Path\(__file__\)\.resolve\(\)\.parent\.parent\s*/\s*"logs"'),
        'find_repo_root(Path(__file__)) / "logs"',
    ),
]


def ensure_import(text: str, fpath: Path) -> str:
    if "from repo_root import find_repo_root" in text:
        return text
    shared_depth = len(fpath.relative_to(ROOT).parts) - 1
    block = BOOTSTRAP.format(shared_depth=shared_depth).strip() + "\n"
    if text.startswith('"""') or text.startswith("'''"):
        q = text[:3]
        end = text.find(q, 3) + 3
        i = end
        while i < len(text) and text[i] in "\r\n":
            i += 1
        rest = text[i:]
        if rest.startswith("from __future__"):
            nl = rest.find("\n")
            i = i + nl + 1
            if i < len(text) and text[i] == "\n":
                i += 1
        return text[:i] + block + "\n" + text[i:]
    if text.startswith("from __future__"):
        nl = text.find("\n") + 1
        return text[:nl] + "\n" + block + "\n" + text[nl:]
    return block + "\n" + text


def main() -> None:
    changed = []
    for rel in FILES:
        p = ROOT / rel
        if not p.exists():
            print("MISSING", rel)
            continue
        text = p.read_text(encoding="utf-8")
        orig = text
        needs = any(rx.search(text) for rx, _ in ASSIGN_PATTERNS + INLINE)
        if not needs:
            print("no-op", rel)
            continue
        text = ensure_import(text, p)
        for rx, repl in ASSIGN_PATTERNS:
            text = rx.sub(repl, text)
        for rx, repl in INLINE:
            text = rx.sub(repl, text)
        if text != orig:
            p.write_text(text, encoding="utf-8", newline="\n")
            changed.append(rel)
            print("patched", rel)
        else:
            print("unchanged", rel)
    print("TOTAL", len(changed))


if __name__ == "__main__":
    main()
