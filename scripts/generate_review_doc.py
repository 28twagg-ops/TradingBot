"""
generate_review_doc.py — Build a single self-contained checkpoint review .txt.

Assembles ALL code + live results for an independent reviewer (Claude/ChatGPT)
to check the work for a given checkpoint. Embeds each source file verbatim and
captures live output from the simulator (integrity suite + Step A-E walkthrough).

Run:
    python scripts/generate_review_doc.py

Output:
    docs/handoff/REVIEW_CHECKPOINT_OPTIONS_PHASE1-2_<date>.txt

Reusable: edit CHECKPOINT, SECTIONS, and LIVE_COMMANDS for future checkpoints.
"""

from __future__ import annotations

import subprocess
import sys
from datetime import date
from pathlib import Path

GIT_ROOT = Path(__file__).resolve().parent.parent          # TradingBot-git
LOCAL_ROOT = GIT_ROOT.parent / "TradingBot"                # Desktop/TradingBot
TODAY = date.today().isoformat()

CHECKPOINT = "Options Expansion — Phase 1 (Data Infra) + Phase 2 (Sim Engine / Gate 2A)"
OUT_PATH = GIT_ROOT / "docs" / "handoff" / f"REVIEW_CHECKPOINT_OPTIONS_PHASE1-2_{TODAY}.txt"

# (Section title, absolute path, language hint)
SECTIONS: list[tuple[str, Path, str]] = [
    ("PHASE 2 — Simulation engine (Steps A-E + Gate 2A integrity checks)",
     LOCAL_ROOT / "simulations" / "options_strategy_simulator.py", "python"),
    ("PHASE 2 — Integrity report (RESULT artifact)",
     LOCAL_ROOT / "simulations" / "results" / "sim_integrity_report.md", "markdown"),
    ("PHASE 1 — Universe helper",
     GIT_ROOT / "scripts" / "options_universe.py", "python"),
    ("PHASE 1 — Open-interest helper (Trading API contracts endpoint)",
     GIT_ROOT / "scripts" / "options_oi.py", "python"),
    ("PHASE 1 — Task 1.1 API probe",
     GIT_ROOT / "scripts" / "api_probe_options.py", "python"),
    ("PHASE 1 — Task 1.2 First-hour collector",
     GIT_ROOT / "scripts" / "first_hour_collector.py", "python"),
    ("PHASE 1 — Task 1.3 Full-day options+stock collector",
     GIT_ROOT / "scripts" / "options_data_collector.py", "python"),
    ("PHASE 1 — Task 1.5 Data quality monitor",
     GIT_ROOT / "scripts" / "data_quality_monitor.py", "python"),
    ("PHASE 1 — Task 1.4 Workflow: first_hour_collector.yml (DRAFT/DISABLED)",
     GIT_ROOT / ".github" / "workflows" / "first_hour_collector.yml", "yaml"),
    ("PHASE 1 — Task 1.4 Workflow: options_collector.yml (DRAFT/DISABLED)",
     GIT_ROOT / ".github" / "workflows" / "options_collector.yml", "yaml"),
    ("PHASE 1 — Task 1.3 Parquet schemas (SCHEMA.md)",
     GIT_ROOT / "data" / "SCHEMA.md", "markdown"),
    ("SECTION 9 — Data source evaluations",
     GIT_ROOT / "data" / "data_source_evaluations.md", "markdown"),
]

# (Label, command list, working directory)
LIVE_COMMANDS: list[tuple[str, list[str], Path]] = [
    ("python simulations/options_strategy_simulator.py --integrity",
     [sys.executable, "simulations/options_strategy_simulator.py", "--integrity"], LOCAL_ROOT),
    ("python simulations/options_strategy_simulator.py --steps",
     [sys.executable, "simulations/options_strategy_simulator.py", "--steps"], LOCAL_ROOT),
]

BAR = "=" * 80
SUB = "-" * 80


def run_cmd(cmd: list[str], cwd: Path) -> str:
    try:
        proc = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, timeout=600)
        out = proc.stdout
        if proc.stderr.strip():
            out += "\n[stderr]\n" + proc.stderr
        out += f"\n[exit code: {proc.returncode}]"
        return out
    except Exception as exc:
        return f"[could not run: {exc}]"


def main() -> None:
    parts: list[str] = []
    parts.append(BAR)
    parts.append(f"INDEPENDENT REVIEW PACKET — {CHECKPOINT}")
    parts.append(f"Generated: {TODAY}")
    parts.append(BAR)
    parts.append("")
    parts.append("PURPOSE")
    parts.append("  This document showcases ALL work for this checkpoint so an")
    parts.append("  independent reviewer can verify it. It contains: (1) live run")
    parts.append("  results captured at generation time, and (2) every source file")
    parts.append("  verbatim. Regenerate anytime with: python scripts/generate_review_doc.py")
    parts.append("")
    parts.append("CRITICAL CONTEXT FOR THE REVIEWER")
    parts.append("  - No Alpaca API keys exist in the build environment, and the market")
    parts.append("    was closed, so Phase 1 collectors/probe are CODE ONLY (not yet run")
    parts.append("    against the live API). Phase 2 was built + run on a SYNTHETIC")
    parts.append("    development dataset (Black-Scholes + the plan's adversarial spread")
    parts.append("    model). The integrity checks validate ENGINE CORRECTNESS, not")
    parts.append("    strategy edge. Real edge requires Phase 3 on collected Alpaca data.")
    parts.append("  - Nothing was committed/pushed. The equity bot (rubber_band_bot.py)")
    parts.append("    and run_bot.yml were NOT modified. The two new workflows are")
    parts.append("    disabled by default (schedule commented + `if: false`).")
    parts.append("")
    parts.append("KNOWN OPEN ITEMS TO SCRUTINISE")
    parts.append("  1. Open interest: Alpaca OptionsSnapshot has no OI field. Collectors")
    parts.append("     log OI=None (marked TODO). Resolution: Trading API")
    parts.append("     GET /v2/options/contracts/{symbol_or_id} (1-2 day OCC lag).")
    parts.append("  2. pyarrow must be added to requirements.txt.")
    parts.append("  3. Synthetic dev data is calibrated to exercise the checks; confirm")
    parts.append("     the calibration is not hiding a real bug (see generate_dev_signals).")
    parts.append("")
    parts.append("REVIEW QUESTIONS")
    parts.append("  Q1. Is the Black-Scholes pricing + spread model correct & arbitrage-sane?")
    parts.append("  Q2. Are the adversarial fill assumptions (buy@ask, sell@bid, ask-$0.01")
    parts.append("      limit, one-window cancel) realistic, or too optimistic/pessimistic?")
    parts.append("  Q3. Does the compounding curve truly size against RUNNING equity?")
    parts.append("  Q4. Do the 6 integrity checks actually catch the bug classes they claim")
    parts.append("      (esp. the -191% sizing bug, fee mis-application, impossible fills)?")
    parts.append("  Q5. Are the Phase 1 collectors correct in their Alpaca API usage?")
    parts.append("  Q6. Anything in the workflows that could disrupt the live equity bot?")
    parts.append("")

    # ---- Live results ----
    parts.append(BAR)
    parts.append("PART 1 — LIVE RUN RESULTS (captured at generation time)")
    parts.append(BAR)
    for label, cmd, cwd in LIVE_COMMANDS:
        parts.append("")
        parts.append(SUB)
        parts.append(f"$ {label}")
        parts.append(SUB)
        parts.append(run_cmd(cmd, cwd))
    parts.append("")

    # ---- Source files ----
    parts.append(BAR)
    parts.append("PART 2 — SOURCE FILES (verbatim)")
    parts.append(BAR)
    for title, path, lang in SECTIONS:
        parts.append("")
        parts.append(BAR)
        parts.append(f"FILE: {title}")
        try:
            rel = path.relative_to(GIT_ROOT.parent)
        except ValueError:
            rel = path
        parts.append(f"PATH: {rel}")
        parts.append(f"LANG: {lang}")
        parts.append(BAR)
        if path.exists():
            parts.append(path.read_text(encoding="utf-8"))
        else:
            parts.append(f"[MISSING FILE: {path}]")
    parts.append("")
    parts.append(BAR)
    parts.append("END OF REVIEW PACKET")
    parts.append(BAR)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({OUT_PATH.stat().st_size/1024:.1f} KB)")


if __name__ == "__main__":
    main()
