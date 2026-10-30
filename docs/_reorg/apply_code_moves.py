#!/usr/bin/env python3
"""Apply Phase C code moves + thin compatibility wrappers. Idempotent-ish."""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

WRAPPER_TMPL = '''\
"""Compatibility wrapper — canonical module: {rel_target}

Do not edit trading logic here. GHA and local tools may still invoke this path.
"""
from __future__ import annotations

import runpy
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[{parents}]
_SEARCH = [
{search_paths}
]
for _p in _SEARCH:
    _s = str(_p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

_TARGET = _ROOT / {target_parts}
if not _TARGET.is_file():
    raise SystemExit(f"wrapper target missing: {{_TARGET}}")

if __name__ == "__main__":
    sys.argv[0] = str(_TARGET)
    runpy.run_path(str(_TARGET), run_name="__main__")
else:
    # Import-time: load real module into this namespace for `import options_lab` style.
    _mod = runpy.run_path(str(_TARGET), run_name=__name__)
    globals().update({{k: v for k, v in _mod.items() if not k.startswith("__")}})
    globals()["__file__"] = str(_TARGET)
'''

# (src_relative, dest_relative)
MOVES: list[tuple[str, str]] = [
    # Rubber Band
    ("rubber_band_bot.py", "live-bots/rubber-band/rubber_band_bot.py"),
    # options-paper lab
    ("scripts/options_lab.py", "live-bots/options-paper/lab/options_lab.py"),
    ("scripts/options_universe.py", "live-bots/options-paper/lab/options_universe.py"),
    ("scripts/options_oi.py", "live-bots/options-paper/lab/options_oi.py"),
    # strategies
    ("scripts/options_signals.py", "live-bots/options-paper/strategies/options_signals.py"),
    ("scripts/options_strategy_lab.py", "live-bots/options-paper/strategies/options_strategy_lab.py"),
    ("scripts/strategy_registry.json", "live-bots/options-paper/strategies/strategy_registry.json"),
    # bot
    ("scripts/options_morning_bot.py", "live-bots/options-paper/bot/options_morning_bot.py"),
    ("scripts/options_reconcile.py", "live-bots/options-paper/bot/options_reconcile.py"),
    ("scripts/init_options_trial.py", "live-bots/options-paper/bot/init_options_trial.py"),
    ("scripts/options_paper_probe.py", "live-bots/options-paper/bot/options_paper_probe.py"),
    # reporting
    ("scripts/options_daily_bucket_report.py", "live-bots/options-paper/reporting/options_daily_bucket_report.py"),
    ("scripts/options_strategy_selection_report.py", "live-bots/options-paper/reporting/options_strategy_selection_report.py"),
    ("scripts/options_data_quality_report.py", "live-bots/options-paper/reporting/options_data_quality_report.py"),
    ("scripts/options_ledger_health.py", "live-bots/options-paper/reporting/options_ledger_health.py"),
    ("scripts/options_signal_frequency.py", "live-bots/options-paper/reporting/options_signal_frequency.py"),
    ("scripts/options_lab_report.py", "live-bots/options-paper/reporting/options_lab_report.py"),
    ("scripts/generate_dashboard.py", "live-bots/options-paper/reporting/generate_dashboard.py"),
    ("scripts/generate_review_doc.py", "live-bots/options-paper/reporting/generate_review_doc.py"),
    ("scripts/rubber_band_report.py", "live-bots/options-paper/reporting/rubber_band_report.py"),
    # options-micro
    ("scripts/options_live_micro.py", "live-bots/options-micro/options_live_micro.py"),
    ("scripts/test_options_live_micro_safety.py", "live-bots/options-micro/test_options_live_micro_safety.py"),
    # shared runtime helpers / collectors
    ("scripts/merge_bot_logs.py", "live-bots/shared/merge_bot_logs.py"),
    ("scripts/reconcile_daily_logs.py", "live-bots/shared/reconcile_daily_logs.py"),
    ("scripts/daily_slippage_watch.py", "live-bots/shared/daily_slippage_watch.py"),
    ("scripts/append_action_run_review.py", "live-bots/shared/append_action_run_review.py"),
    ("scripts/options_data_collector.py", "live-bots/shared/options_data_collector.py"),
    ("scripts/first_hour_collector.py", "live-bots/shared/first_hour_collector.py"),
    ("scripts/data_quality_monitor.py", "live-bots/shared/data_quality_monitor.py"),
    ("scripts/test_day_trader_data_validity.py", "live-bots/shared/test_day_trader_data_validity.py"),
    ("scripts/test_options_chain_cache.py", "live-bots/shared/test_options_chain_cache.py"),
    ("scripts/api_probe_options.py", "live-bots/shared/api_probe_options.py"),
    ("scripts/options_microlive_sim.py", "live-bots/shared/options_microlive_sim.py"),
    ("scripts/benchmark_run.py", "live-bots/shared/benchmark_run.py"),
    ("scripts/local_docs.py", "live-bots/shared/local_docs.py"),
    # research market
    ("scripts/crypto_rainbow_backtest.py", "research/market-research/crypto_rainbow_backtest.py"),
    ("scripts/midcap_longterm_analysis.py", "research/market-research/midcap_longterm_analysis.py"),
    ("scripts/midcap_yoy_analysis.py", "research/market-research/midcap_yoy_analysis.py"),
    # research other
    ("scripts/analyze_stop_overshoots.py", "research/other-studies/analyze_stop_overshoots.py"),
    ("scripts/generate_june10_report.py", "research/other-studies/generate_june10_report.py"),
    ("scripts/historical_data_fetcher.py", "research/other-studies/historical_data_fetcher.py"),
    ("scripts/pdt_removal_verify.py", "research/other-studies/pdt_removal_verify.py"),
    ("scripts/run_enrich_parallel.py", "research/other-studies/run_enrich_parallel.py"),
    ("scripts/run_full_research.py", "research/other-studies/run_full_research.py"),
    ("scripts/run_historical_parallel.py", "research/other-studies/run_historical_parallel.py"),
    ("scripts/run_options_research.py", "research/other-studies/run_options_research.py"),
    ("scripts/run_rank_top5_parallel.py", "research/other-studies/run_rank_top5_parallel.py"),
    ("scripts/sim_pdt_schedule.py", "research/other-studies/sim_pdt_schedule.py"),
    ("scripts/strategy_parity_check.py", "research/other-studies/strategy_parity_check.py"),
]

# Paths that need wrappers at the OLD location after move
WRAPPER_AT_OLD = {src for src, _ in MOVES}


def git_mv(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if not src.exists():
        if dst.exists():
            print(f"skip (already moved): {src} -> {dst}")
            return
        raise FileNotFoundError(src)
    if dst.exists():
        print(f"skip (dest exists): {dst}")
        return
    # Prefer git mv when tracked
    tracked = subprocess.run(
        ["git", "ls-files", "--error-unmatch", str(src)],
        cwd=ROOT,
        capture_output=True,
    ).returncode == 0
    if tracked:
        subprocess.check_call(["git", "mv", str(src), str(dst)], cwd=ROOT)
    else:
        shutil.move(str(src), str(dst))
        subprocess.run(["git", "add", "-f", str(dst)], cwd=ROOT, check=False)
    print(f"moved: {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")


def search_paths_for(dest_rel: str) -> list[str]:
    """sys.path entries relative to repo root as Path expressions for wrapper."""
    bases = [
        "live-bots/options-paper/lab",
        "live-bots/options-paper/strategies",
        "live-bots/options-paper/bot",
        "live-bots/options-paper/reporting",
        "live-bots/options-micro",
        "live-bots/shared",
        "live-bots/rubber-band",
        "research/market-research",
        "research/other-studies",
        "research/options-strategies/backtests",
        "research/options-strategies/experiments",
    ]
    return bases


def write_wrapper(old_rel: str, dest_rel: str) -> None:
    old = ROOT / old_rel
    parents = len(Path(old_rel).parts) - 1
    if parents < 1:
        parents = 0
    # For root rubber_band_bot.py, parents=0 → Path(__file__).resolve().parents[0] is file's dir = root. Good.
    # Actually Path(__file__).parents[0] == parent of file. For root file, parents[0] is ROOT. We need ROOT.
    # parents[0] for /repo/rubber_band_bot.py is /repo. Good when parents=0... wait
    # Path.parents[0] is the direct parent. So parents index should be 0 for root files → _ROOT = parent of file = repo root.
    # For scripts/foo.py, we need parents[1] to get repo root. So parents = len(parts)-1. scripts/foo → 1. Good.

    search = search_paths_for(dest_rel)
    search_lines = ",\n".join(f'    _ROOT / "{p}"' for p in search)
    parts = " / ".join(f'"{p}"' for p in Path(dest_rel).parts)
    content = WRAPPER_TMPL.format(
        rel_target=dest_rel.replace("\\", "/"),
        parents=parents if parents > 0 else 0,
        search_paths=search_lines,
        target_parts=parts,
    )
    # Fix root case: parents[0] works. For parents=0 we used parents[0] which is correct.
    old.parent.mkdir(parents=True, exist_ok=True)
    old.write_text(content, encoding="utf-8", newline="\n")
    print(f"wrapper: {old_rel}")


def move_myers() -> None:
    src = ROOT / "myers-stock-investor"
    dst = ROOT / "research" / "myers-stock-investor"
    if dst.exists():
        print("myers already at research/myers-stock-investor")
        return
    if not src.exists():
        print("myers source missing")
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dst))
    print("moved myers-stock-investor -> research/myers-stock-investor")


def move_simulations() -> None:
    src = ROOT / "simulations"
    dst = ROOT / "research" / "options-strategies" / "backtests"
    if not src.exists():
        print("simulations missing")
        return
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        if item.name == "__pycache__":
            continue
        target = dst / item.name
        if target.exists():
            print(f"skip exists: {target.relative_to(ROOT)}")
            continue
        if item.is_dir() or item.is_file():
            # git mv if possible
            tracked = subprocess.run(
                ["git", "ls-files", "--error-unmatch", str(item)],
                cwd=ROOT,
                capture_output=True,
            ).returncode == 0
            # For directories, use shutil + git add
            shutil.move(str(item), str(target))
            print(f"moved sim: {item.name} -> {target.relative_to(ROOT)}")
    # leave simulations/ as pointer README + optional thin note
    readme = src / "README.md"
    if not any(src.iterdir()) if src.exists() else True:
        src.mkdir(exist_ok=True)
    readme.write_text(
        "# Moved\n\nCanonical path: `research/options-strategies/backtests/`\n",
        encoding="utf-8",
    )


def move_docs_strategy() -> None:
    mapping = [
        ("docs/STRATEGY_RESEARCH_2026-10-23.md", "research/options-strategies/STRATEGY_RESEARCH_2026-10-23.md"),
        ("docs/HANDOFF_TRANSFER.md", "docs/HANDOFF_TRANSFER.md"),  # keep
    ]
    src = ROOT / "docs" / "STRATEGY_RESEARCH_2026-10-23.md"
    dst = ROOT / "research" / "options-strategies" / "STRATEGY_RESEARCH_2026-10-23.md"
    if src.exists() and not dst.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)  # copy then keep original until wrappers/docs settle
        print(f"copied strategy research -> {dst.relative_to(ROOT)}")


def main() -> None:
    for src_rel, dst_rel in MOVES:
        git_mv(ROOT / src_rel, ROOT / dst_rel)
        if src_rel.endswith(".py"):
            write_wrapper(src_rel, dst_rel)

    move_myers()
    move_simulations()
    move_docs_strategy()

    # Package markers
    for pkg in [
        "live-bots",
        "live-bots/rubber-band",
        "live-bots/options-micro",
        "live-bots/options-paper",
        "live-bots/options-paper/lab",
        "live-bots/options-paper/strategies",
        "live-bots/options-paper/bot",
        "live-bots/options-paper/reporting",
        "live-bots/shared",
        "research",
        "research/market-research",
        "research/other-studies",
        "research/options-strategies",
    ]:
        init = ROOT / pkg / "__init__.py"
        if not init.exists():
            init.write_text('"""TradingBot package namespace marker."""\n', encoding="utf-8")

    print("DONE Phase C moves")


if __name__ == "__main__":
    main()
