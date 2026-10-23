"""
generate_correlation_review_doc.py
================================================================================
Assembles ONE self-contained weekend-checkpoint review packet (.txt) for an
independent reviewer (e.g. Claude) covering BOTH:
  - Task 2.0  Preliminary Correlation Study (yfinance + BS reconstruction)
  - Task 2.3  Strategy Grid engine (Phase 3 machinery, synthetic dev data)

It embeds, for each task: live run output captured at generation time, the
result artifacts, and the source code verbatim — so the reviewer can verify
everything from this single file.

Output: TradingBot/REVIEW_WEEKEND_OPTIONS_CHECKPOINT_<date>.txt  (LOCAL,
not committed to GitHub). Regenerate anytime:
    python simulations/generate_correlation_review_doc.py
"""

from __future__ import annotations

import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # TradingBot/  (local)
SIM = ROOT / "simulations"
CORR = SIM / "results" / "preliminary_correlation"
GRID = SIM / "results" / "strategy_grid_dev"
GIT = ROOT.parent / "TradingBot-git"                   # pushed repo (code only)
OUT = ROOT / f"REVIEW_WEEKEND_OPTIONS_CHECKPOINT_{date.today()}.txt"

BAR = "=" * 80
SUB = "-" * 80


def rule(title: str) -> str:
    return f"\n{BAR}\n{title}\n{BAR}\n"


def embed_file(path: Path, max_lines: int | None = None) -> str:
    if not path.exists():
        return f"[MISSING: {path}]\n"
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    note = ""
    if max_lines and len(lines) > max_lines:
        note = f"\n[... truncated: showing first {max_lines} of {len(lines)} lines ...]"
        lines = lines[:max_lines]
    return "\n".join(lines) + note + "\n"


def run_capture(cmd: list[str]) -> str:
    try:
        p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=1800)
        out = (p.stdout or "") + (p.stderr or "")
        return out + f"\n[exit code: {p.returncode}]\n"
    except Exception as exc:  # noqa: BLE001
        return f"[failed to run {' '.join(cmd)}: {exc}]\n"


def main() -> int:
    parts: list[str] = []

    parts.append(BAR)
    parts.append("INDEPENDENT REVIEW PACKET — WEEKEND OPTIONS CHECKPOINT")
    parts.append("Task 2.0 (Preliminary Correlation Study) + Task 2.3 (Strategy Grid engine)")
    parts.append(f"Generated: {date.today()}")
    parts.append(BAR)

    parts.append("""
PURPOSE
  One self-contained document so an independent reviewer can verify this
  weekend's work. For each task it contains (1) live run output captured at
  generation time, (2) result artifacts, and (3) source code verbatim.
  Regenerate: python simulations/generate_correlation_review_doc.py

STATUS (lead with this)
  - Task 2.0 — Preliminary Correlation Study: VERDICT B (WEAK/CONDITIONAL),
    PRELIMINARY. Signal edge is real but concentrated INTRADAY (EOD); it
    disappears at 1/3/5-day horizons. Based on yfinance EOD + Black-Scholes
    RECONSTRUCTED option prices — confirm with Alpaca 1-min data.
  - Task 2.3 — Strategy Grid engine: BUILD COMPLETE, DEVELOPMENT ONLY. The
    Phase 3 parameter-grid machinery runs end-to-end on SYNTHETIC dev data
    (2,700 variants in ~40s) with Section 7 thresholds + leaderboards. A
    `--focused` Verdict-B preset (intraday/EOD exits, ATM, short DTE) is
    included. It proves the machinery, NOT any real edge.
  - Task 4.1 — Paper options bot: BUILD COMPLETE, PAPER ONLY, NOT YET RUN.
    Trades the preliminary Verdict-B heuristic (strong gap-down -> ATM call ->
    EOD close, Tier 0). PAPER_TRADING is hard-locked True; it refuses to run
    live. Reviewed here as code only (no live run possible: no keys, market
    closed). First real run is Monday on the paper account.

  Nothing is committed to GitHub. The live equity bot (rubber_band_bot.py) and
  run_bot.yml were NOT modified. The paper bot's workflow is disabled
  (if: false + schedule commented).

  WHAT TO DO NEXT (the plan this packet supports):
    Mon 9:45 ET run scripts/api_probe_options.py (Gate 1A); if it passes, commit
    everything, run the paper bot on Monday's signals, enable the two data-
    collection workflows. The full real grid waits on ~4 weeks of Alpaca data.

GLOBAL CONTEXT
  - The equity bot is LONG-ONLY mean-reversion (BUYs dips expecting a bounce),
    so every BUY is a BULLISH thesis -> analysed as buying a CALL.
  - No scipy in the environment: Task 2.0's Welch t-test + Student-t p-value
    are implemented from scratch (incomplete-beta continued fraction).
  - Task 2.3 reuses the Gate 2A-validated engine (options_strategy_simulator.py).
    A `fill_mode` parameter (cancel/widen/hold) was ADDED to
    simulate_single_trade with default = original behavior; Gate 2A was re-run
    and all 6 integrity checks still PASS (see live run in PART 1c).
""")

    # ============================ TASK 2.0 ============================
    parts.append(rule("##### TASK 2.0 — PRELIMINARY CORRELATION STUDY #####"))

    parts.append("""
WHAT IT ANSWERS
  Do the equity bot's existing BUY signals correlate with options price
  movement? Uses real transactions.csv (358 BUYs, 2026-05-25..06-16, 220
  tickers) + yfinance daily OHLCV + Black-Scholes RECONSTRUCTED option prices
  (since yfinance has no historical option prices). Control group = 3 same-day
  non-signal names per signal (isolates signal effect from market drift).

KEY NUMBERS
  - EOD: signal call return +33.25% vs control +5.75%, diff +27.50%, p<0.001
    (n=358 vs 1074). The ONLY horizon both positive and significant.
  - 1/3/5-day: signal does NOT beat control (diffs negative, p>0.3).
  - Net P&L per signal after adversarial costs: EOD +$115.48 vs +$4.95 control.
  - Strong gaps (<-2%) beat weak gaps at every horizon (EOD +47.0% vs +15.3%).
  - All 5 sanity checks pass.

REVIEW QUESTIONS (Task 2.0)
  Q1. Is the long-only-BUY => CALL interpretation sound, or restrict to GapDown?
  Q2. Is the same-day non-signal control a fair drift control given ~3 weeks data?
  Q3. EOD uses open->close for BOTH groups (symmetric) not the bot's actual
      intraday entry->close. Fair simplification or bias?
  Q4. The +33% EOD return is option leverage on a ~1.5-2% move — anything
      inflating it (strike rounding, sigma=realized-vol proxy, no EOD decay)?
  Q5. Is the from-scratch Welch t-test / Student-t p-value correct?
  Q6. Is Verdict B right (vs A or C)?
""")

    parts.append(rule("PART 1a — TASK 2.0 LIVE RUN OUTPUT (captured now)"))
    parts.append(f"{SUB}\n$ python simulations/preliminary_correlation_study.py\n{SUB}")
    parts.append(run_capture([sys.executable, "simulations/preliminary_correlation_study.py"]))

    parts.append(rule("PART 2a — TASK 2.0 RESULT ARTIFACTS"))
    parts.append(rule("2a-i. preliminary_verdict.md"))
    parts.append(embed_file(CORR / "preliminary_verdict.md"))
    parts.append(rule("2a-ii. correlation_results.csv (Q1-Q5 tables)"))
    parts.append(embed_file(CORR / "correlation_results.csv"))
    parts.append(rule("2a-iii. signal_history.csv (first 30 rows)"))
    parts.append(embed_file(CORR / "signal_history.csv", max_lines=30))
    parts.append(rule("2a-iv. stock_returns.csv (first 30 rows)"))
    parts.append(embed_file(CORR / "stock_returns.csv", max_lines=30))
    parts.append(rule("2a-v. reconstructed_options.csv (first 20 rows)"))
    parts.append(embed_file(CORR / "reconstructed_options.csv", max_lines=20))
    parts.append(rule("2a-vi. control_group.csv (first 20 rows)"))
    parts.append(embed_file(CORR / "control_group.csv", max_lines=20))

    # ============================ TASK 2.3 ============================
    parts.append(rule("##### TASK 2.3 — STRATEGY GRID ENGINE (Phase 3 machinery, DEV) #####"))

    parts.append("""
WHAT IT IS
  The Phase 3 mass-strategy-testing parameter grid, built early on SYNTHETIC
  dev data while real Alpaca 1-min data accumulates (plan Section 3 Task 2.3 /
  Section 10 step 6). Axes (Section 4): mechanic x strike(ATM/OTM1/OTM2) x
  DTE(1/3/7/14/30) x entry-window(3) x exit(intraday/EOD/1day/3day) x
  fill(cancel/widen/hold) = 2,700 variants x 1,000 signals = 2.7M sims (~40s).

  It enforces the Section 7 seven viability thresholds (exp P&L/sig>0,
  fill>=40%, sample>=50, spread<=20%, cost<=$75, holds in BOTH sub-periods,
  PF>=1.2), splits MAIN(>=50)/SECONDARY(30-49)/EXCLUDED(<30), and emits ranked
  leaderboards + hold-period / fill-behavior recommendation tables.

  IMPORTANT: synthetic drifts are arbitrary -> rankings are NOT real edge. This
  validates the machinery only. Phase 3 swaps gen_variant_signals(...) for the
  stubbed load_alpaca_dataset(...); everything downstream is unchanged.

REVIEW QUESTIONS (Task 2.3)
  Q7.  Is the fill_mode model (cancel/widen/hold) a fair abstraction of the
       plan's Option 1/2/3 fill behaviors?
  Q8.  Is using GBM closed-form terminal draws (instead of minute-stepping) a
       valid speedup for the exit price distribution?
  Q9.  Are the Section 7 thresholds implemented correctly, incl. the both-
       sub-periods robustness check (#6)?
  Q10. Is the MAIN/SECONDARY/EXCLUDED split by FILLED-trade count the right
       definition of "sample size"?
  Q11. Does the leaderboard correctly avoid presenting synthetic results as edge?
""")

    parts.append(rule("PART 1b — TASK 2.3 LIVE RUN OUTPUT (full grid, captured now)"))
    parts.append(f"{SUB}\n$ python simulations/options_strategy_grid.py\n{SUB}")
    parts.append(run_capture([sys.executable, "simulations/options_strategy_grid.py"]))

    parts.append(rule("PART 1c — Gate 2A RE-RUN after adding fill_mode (must still be ALL 6 PASS)"))
    parts.append(f"{SUB}\n$ python simulations/options_strategy_simulator.py --integrity\n{SUB}")
    parts.append(run_capture([sys.executable, "simulations/options_strategy_simulator.py",
                              "--integrity"]))

    parts.append(rule("PART 2b — TASK 2.3 RESULT ARTIFACTS"))
    parts.append(rule("2b-i. strategy_grid_report_dev.md (leaderboard + recommendations)"))
    parts.append(embed_file(GRID / "strategy_grid_report_dev.md"))
    parts.append(rule("2b-ii. options_leaderboard_dev.csv (top 40 ranked variants)"))
    parts.append(embed_file(GRID / "options_leaderboard_dev.csv", max_lines=41))
    parts.append(rule("2b-iii. hold_period_reco_dev.csv"))
    parts.append(embed_file(GRID / "hold_period_reco_dev.csv"))
    parts.append(rule("2b-iv. fill_behavior_reco_dev.csv"))
    parts.append(embed_file(GRID / "fill_behavior_reco_dev.csv"))
    parts.append(rule("2b-v. FOCUSED (Verdict-B) grid report — `--focused` preset"))
    parts.append(embed_file(GRID / "focused" / "strategy_grid_report_dev.md"))

    # ============================ TASK 4.1 ============================
    parts.append(rule("##### TASK 4.1 — PAPER OPTIONS BOT (code review only) #####"))

    parts.append("""
WHAT IT IS
  A standalone morning options bot (PAPER account) that trades the preliminary
  Verdict-B finding: on a strong gap-down (gap_pct < -2%) buy an ATM CALL and
  CLOSE SAME DAY. It runs SEPARATELY from rubber_band_bot.py and never touches
  it. PAPER_TRADING is hard-locked True; the bot refuses to run live.

  Per cron run (entry window 9:28-11:35 ET):
    1) cancel still-open option orders from the prior run (Option-1 fill),
    2) manage exits on open option positions (+50% / -50% -> close),
    3) scan the universe for strong gap-downs,
    4) for each new signal: pick ATM call, apply liquidity + Tier-0 sizing,
       place a BUY limit at ask-$0.01.
  EOD (>= 15:30 ET): close ALL option positions (limit at bid; market at 15:50).
  Tier 0 sizing: 1 contract, <= $75 premium, <= 20% of equity in premium.

  STATUS: BUILD COMPLETE; compiles + lints clean; no-keys guard verified. NOT
  yet run (needs paper keys + open market). It trades the PRELIMINARY heuristic,
  NOT a Phase-3-validated variant -> early plumbing validation, not proven edge.
  In paper mode it uses a SEPARATE account from the live equity bot, so the
  shared-account coordination (Task 5.2) is deferred to Phase 5 go-live.

REVIEW QUESTIONS (Task 4.1)
  Q12. Is the order flow correct for Alpaca options (OptionChainRequest ->
       snapshot bid/ask, OCC symbol, LimitOrderRequest qty=contracts)?
  Q13. Are the Tier-0 sizing caps + the 20% account cap enforced correctly
       (size_contracts), and is the entry/exit limit logic sound?
  Q14. Is the EOD sweep safe (limit at bid, market only at 15:50 last resort)?
  Q15. Is the PAPER hard-lock + no-live-coordination stance acceptable, and are
       there any ways this bot could affect the live equity bot? (It should not:
       separate paper account, separate workflow, disabled by default.)
  Q16. Is the gap-down scan (daily bars open vs prior close) a reasonable signal
       proxy for the preliminary paper run until first-hour data is collected?""")

    # ============================ SOURCE ============================
    parts.append(rule("##### PART 3 — SOURCE CODE (verbatim) #####"))
    parts.append(rule("3a. simulations/preliminary_correlation_study.py (Task 2.0)"))
    parts.append(embed_file(SIM / "preliminary_correlation_study.py"))
    parts.append(rule("3b. simulations/options_strategy_grid.py (Task 2.3)"))
    parts.append(embed_file(SIM / "options_strategy_grid.py"))
    parts.append(rule("3c. simulations/options_strategy_simulator.py (Gate 2A engine, "
                      "shared by both — bs_price/bs_delta + fill_mode)"))
    parts.append(embed_file(SIM / "options_strategy_simulator.py"))
    parts.append(rule("3d. TradingBot-git/scripts/options_morning_bot.py (Task 4.1 PAPER bot)"))
    parts.append(embed_file(GIT / "scripts" / "options_morning_bot.py"))
    parts.append(rule("3e. TradingBot-git/.github/workflows/options_morning_bot.yml "
                      "(DISABLED workflow)"))
    parts.append(embed_file(GIT / ".github" / "workflows" / "options_morning_bot.yml"))

    parts.append("\n" + BAR + "\nEND OF WEEKEND REVIEW PACKET\n" + BAR + "\n")

    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
