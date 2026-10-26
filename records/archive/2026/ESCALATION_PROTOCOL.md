# Options Strategy Escalation Protocol
Date: 2026-07-25
Author: Cursor AI (Claude) — LOCAL ONLY, do not commit to GitHub

---

## Overview

This document defines the exact escalation path for options strategies from
initial paper testing to live trading. Tyler reviews on Aug 18 and selects
go-live candidates from the promote pipeline.

---

## STAGE 1: PAPER (current — July 25 to Aug 18)

- Strategy runs in paper lab with 2 reps per window (8 buckets each)
- All entries fill at Alpaca paper prices (realistic slippage simulated)
- Auto-kill conditions evaluated daily:
  - KILL if n >= 15 AND median P&L% < -25%
  - KILL if n >= 15 AND p10 < -85% (catastrophic left tail)
  - KILL if n >= 25 AND WR < 15% (almost never wins)
- WATCH: n >= 15 AND median between -10% and -25%
- KEEP: n >= 30 AND median > -10%
- PROMOTE candidate: n >= 30 AND median > 0%

Running now:
  S163-S175 (11 active strategies, launched Jul 21-22)
  S200-S219 (20 new strategies, launched Jul 26)

Kill/promote check runs daily after market close via GHA:
  python3 scripts/options_strategy_lab.py --evaluate

---

## STAGE 2: TYLER REVIEW (Aug 18)

Tyler reviews all PROMOTE candidates surfaced by the auto-kill system.

Decision criteria for Stage 3 approval:
  - n >= 30 exits (minimum sample size)
  - Median P&L% > 0% (positive expected value)
  - p10 > -50% (acceptable worst 10% case)
  - Win rate > 40% (majority of trades win)
  - Profit factor > 1.1 (wins outweigh losses in dollar terms)
  - Symbol diversification: top symbol < 50% of exits (not single-name dependent)

Target: Select top 3-5 strategies for Stage 3.

If no strategies reach PROMOTE by Aug 18:
  - Review KEEP candidates (median > -10%, n >= 30)
  - Consider running another 2 weeks of paper before any live exposure
  - Do not go live without at least one positive-median strategy at n >= 30

---

## STAGE 3: MICRO LIVE (post-Aug 18)

Conditions: At least one strategy approved by Tyler in Stage 2.

Execution:
  - Run with $25-50 per trade on real options account (1 contract max)
  - Run alongside paper lab simultaneously for 2 weeks
  - Track paper vs live fill comparison:
    - If paper median and live median within 20%: proceed to Stage 4
    - If paper fills significantly better than live: investigate slippage,
      consider tightening limit offset or abandoning the strategy

Risk controls in Stage 3:
  - Never exceed $100 total open options premium on live account
  - Paper account continues running full universe in parallel
  - No changes to entry parameters during Stage 3 (compare apples to apples)

Duration: 2 weeks minimum (Aug 18 - Sep 1)

---

## STAGE 4: SCALE UP

Conditions: Stage 3 live fills within 20% of paper, strategy still positive.

Execution:
  - Gradually increase from $25-50 to $75-100 per trade
  - Never exceed 10% of live account equity per single options trade
  - Monitor fill quality weekly (live vs paper median comparison)
  - Keep paper lab running for new strategy testing always

Scale-up schedule:
  Week 1-2: $25-50 per trade
  Week 3-4: $50-75 per trade (if fills still look good)
  Week 5+:  $75-100 per trade (if strategy stable)

---

## STAGE 5: RETIRE PAPER FOR WINNERS

- Proven winners move fully to live with controlled position sizing
- Paper lab continues testing new combinations indefinitely
- No live strategy ever displaces paper testing — both run in parallel

---

## GUARDRAILS (always in effect)

1. PAPER_TRADING=True until explicit Tyler approval for Stage 3
2. Never exceed 10% of live account per trade
3. Never go live with a strategy showing median < 0% (even positive WR can lose)
4. Always verify paper fills are realistic (check bid/ask spread)
5. Kill system is advisory only — Tyler makes final drop/keep decisions
   (auto-kill flags for review, Tyler can override)

---

## Current Status (2026-07-26)

  Active paper strategies: 31 (S163-S175, S200-S219)
  Days until Tyler returns: 23 (Aug 18, 2026)
  Current promote candidates: 0 (data collecting)
  Expected first decisions: Aug 8-10 (strategies with n>=15)

Target by Aug 11 (final sweep before Tyler returns):
  - Have n >= 15 on all S163-S175 strategies
  - Have n >= 5 on all S200-S219 strategies
  - Kill clear losers, identify top 5 candidates
  - Have at least one PROMOTE candidate emerging

---
END ESCALATION PROTOCOL
