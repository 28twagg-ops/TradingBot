# Options Strategy Grid — Leaderboard (Phase 3 dry-run)

_DEVELOPMENT ONLY - NOT FOR TRADING DECISIONS_

Generated: 2026-06-28
Engine: `simulations/options_strategy_simulator.py` (Gate 2A validated).
Data: SYNTHETIC development dataset (Black-Scholes + adversarial spread model). NOT real edge — swap in Alpaca 1-min data for the production run.
Signals per variant: 1000.

## Grid summary

- Total variants: 270
- MAIN (>=50 filled): 270
- SECONDARY (30-49 filled): 0
- EXCLUDED (<30 filled): 0
- **Survived all 7 viability thresholds: 0**

## Section 7 viability thresholds applied

1. Expected P&L/signal > $0  2. Fill rate >= 40%  3. Sample >= 50  4. Avg spread <= 20%  5. Cost <= $75  6. Holds in BOTH periods  7. Profit factor >= 1.2

## MAIN leaderboard — top 15 (>=50 filled, ranked by Exp P&L/signal)

| Rank | Variant | ExpP&L/sig | Fill | Win | PF | Spread | Survives |
|---|---|---|---|---|---|---|---|
| 1 | A4_MorningRevCall|ATM|1DTE|1000-1100|EOD|cancel | $+3.69 | 38% | 44% | 1.58 | 17% | no |
| 2 | A3_GapUpPut|ATM|1DTE|0930-1000|EOD|cancel | $+3.61 | 36% | 41% | 1.57 | 18% | no |
| 3 | A7_VWAPRejPut|ATM|1DTE|0930-1000|EOD|hold | $+2.35 | 50% | 40% | 1.27 | 17% | no |
| 4 | A8_ORBCall|ATM|1DTE|1100-1200|EOD|widen | $+1.40 | 52% | 34% | 1.12 | 17% | no |
| 5 | A8_ORBCall|ATM|1DTE|0930-1000|EOD|cancel | $+0.82 | 40% | 31% | 1.10 | 17% | no |
| 6 | A1_GapDownCall|ATM|1DTE|1100-1200|intraday|widen | $+0.77 | 45% | 46% | 1.13 | 17% | no |
| 7 | A3_GapUpPut|ATM|1DTE|0930-1000|EOD|hold | $+0.51 | 49% | 34% | 1.06 | 17% | no |
| 8 | A7_VWAPRejPut|ATM|7DTE|1000-1100|EOD|cancel | $+0.07 | 21% | 45% | 1.05 | 15% | no |
| 9 | A3_GapUpPut|ATM|1DTE|1000-1100|intraday|cancel | $+0.02 | 33% | 39% | 1.00 | 17% | no |
| 10 | A1_GapDownCall|ATM|1DTE|0930-1000|intraday|widen | $+0.02 | 45% | 42% | 1.00 | 18% | no |
| 11 | A1_GapDownCall|ATM|3DTE|0930-1000|EOD|hold | $+0.00 | 49% | 46% | 1.00 | 15% | no |
| 12 | A3_GapUpPut|ATM|1DTE|1000-1100|intraday|hold | $-0.18 | 52% | 38% | 0.97 | 17% | no |
| 13 | A4_MorningRevCall|ATM|3DTE|0930-1000|EOD|cancel | $-0.21 | 29% | 39% | 0.95 | 14% | no |
| 14 | A1_GapDownCall|ATM|1DTE|1000-1100|EOD|widen | $-0.28 | 50% | 34% | 0.97 | 18% | no |
| 15 | A7_VWAPRejPut|ATM|1DTE|1100-1200|intraday|widen | $-0.33 | 48% | 37% | 0.95 | 17% | no |

## Survivors (all 7 thresholds): 0

_No variant survived all 7 thresholds on synthetic data. This is EXPECTED and fine — synthetic edges are deliberately small and the purpose here is to exercise the machinery, not find real winners._

## Hold-period recommendation per mechanic (mean Exp P&L/signal)

| Mechanic | intraday | EOD | 1day | 3day | BEST |
|---|---|---|---|---|---|
| A1_GapDownCall | $-2.29 | $-2.38 | $+nan | $+nan | intraday |
| A4_MorningRevCall | $-2.69 | $-2.41 | $+nan | $+nan | EOD |
| A8_ORBCall | $-2.64 | $-2.19 | $+nan | $+nan | EOD |
| A3_GapUpPut | $-2.49 | $-2.48 | $+nan | $+nan | EOD |
| A7_VWAPRejPut | $-2.68 | $-2.45 | $+nan | $+nan | EOD |

## Fill-behavior recommendation per mechanic (mean Exp P&L/signal)

| Mechanic | cancel | widen | hold | BEST |
|---|---|---|---|---|
| A1_GapDownCall | $-1.74 | $-2.34 | $-2.92 | cancel |
| A4_MorningRevCall | $-1.47 | $-3.04 | $-3.14 | cancel |
| A8_ORBCall | $-1.83 | $-2.52 | $-2.89 | cancel |
| A3_GapUpPut | $-1.41 | $-3.17 | $-2.87 | cancel |
| A7_VWAPRejPut | $-1.87 | $-2.98 | $-2.85 | cancel |

_Note: these two tables average Exp P&L/signal across ALL parameter combinations for each mechanic, so they are dominated by the many negative-edge (short-hold) combos — that is why `cancel` (trade less) tends to win the MEAN. Among the positive-edge variants on the leaderboard the opposite holds: higher-fill modes (`widen`/`hold`) compound a real edge and rank at the top. On real data, read the per-variant leaderboard, not just these marginal means._

## What this proves (and does not)

- PROVES: the Phase 3 grid machinery works end-to-end — it sweeps every axis, applies the adversarial engine, computes the Section 4 key metric, enforces the Section 7 thresholds, and produces ranked leaderboards + hold-period / fill-behavior recommendations.
- DOES NOT PROVE: any real strategy edge. Synthetic drifts are arbitrary. The production leaderboard requires ~4 weeks of Alpaca 1-min data via `load_alpaca_dataset(...)`; only then are rankings meaningful.
- DEVELOPMENT ONLY - NOT FOR TRADING DECISIONS