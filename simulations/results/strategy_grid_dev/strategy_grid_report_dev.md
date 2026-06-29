# Options Strategy Grid — Leaderboard (Phase 3 dry-run)

_DEVELOPMENT ONLY - NOT FOR TRADING DECISIONS_

Generated: 2026-06-28
Engine: `simulations/options_strategy_simulator.py` (Gate 2A validated).
Data: SYNTHETIC development dataset (Black-Scholes + adversarial spread model). NOT real edge — swap in Alpaca 1-min data for the production run.
Signals per variant: 1000.

## Grid summary

- Total variants: 2700
- MAIN (>=50 filled): 1800
- SECONDARY (30-49 filled): 260
- EXCLUDED (<30 filled): 640
- **Survived all 7 viability thresholds: 85**

## Section 7 viability thresholds applied

1. Expected P&L/signal > $0  2. Fill rate >= 40%  3. Sample >= 50  4. Avg spread <= 20%  5. Cost <= $75  6. Holds in BOTH periods  7. Profit factor >= 1.2

## MAIN leaderboard — top 15 (>=50 filled, ranked by Exp P&L/signal)

| Rank | Variant | ExpP&L/sig | Fill | Win | PF | Spread | Survives |
|---|---|---|---|---|---|---|---|
| 1 | A3_GapUpPut|ATM|1DTE|1000-1100|3day|widen | $+35.77 | 49% | 52% | 4.88 | 17% | YES |
| 2 | A4_MorningRevCall|ATM|1DTE|1100-1200|3day|hold | $+33.83 | 53% | 50% | 4.41 | 17% | YES |
| 3 | A3_GapUpPut|ATM|1DTE|1000-1100|3day|hold | $+29.43 | 55% | 46% | 3.39 | 17% | YES |
| 4 | A8_ORBCall|ATM|1DTE|0930-1000|3day|hold | $+28.95 | 50% | 48% | 3.92 | 18% | YES |
| 5 | A1_GapDownCall|ATM|1DTE|1000-1100|3day|hold | $+27.50 | 54% | 49% | 3.50 | 17% | YES |
| 6 | A3_GapUpPut|ATM|1DTE|0930-1000|3day|widen | $+26.78 | 50% | 48% | 3.97 | 18% | YES |
| 7 | A1_GapDownCall|ATM|1DTE|0930-1000|3day|widen | $+26.38 | 50% | 41% | 3.61 | 18% | YES |
| 8 | A1_GapDownCall|ATM|1DTE|1100-1200|3day|widen | $+25.12 | 50% | 42% | 3.34 | 18% | YES |
| 9 | A3_GapUpPut|ATM|1DTE|1100-1200|3day|cancel | $+24.94 | 33% | 43% | 4.38 | 17% | no |
| 10 | A4_MorningRevCall|ATM|1DTE|0930-1000|3day|widen | $+24.62 | 53% | 43% | 3.03 | 18% | YES |
| 11 | A4_MorningRevCall|ATM|1DTE|1100-1200|3day|widen | $+24.16 | 52% | 48% | 3.42 | 17% | YES |
| 12 | A1_GapDownCall|ATM|1DTE|1000-1100|3day|widen | $+23.68 | 47% | 45% | 3.14 | 17% | YES |
| 13 | A8_ORBCall|ATM|1DTE|0930-1000|3day|widen | $+23.49 | 49% | 44% | 3.15 | 17% | YES |
| 14 | A4_MorningRevCall|ATM|1DTE|1000-1100|3day|widen | $+23.13 | 50% | 44% | 3.24 | 18% | YES |
| 15 | A7_VWAPRejPut|ATM|1DTE|1000-1100|3day|hold | $+22.67 | 52% | 43% | 2.97 | 17% | YES |

## Survivors (all 7 thresholds): 85

| Variant | ExpP&L/sig | Fill | PF | A | B |
|---|---|---|---|---|---|
| A3_GapUpPut|ATM|1DTE|1000-1100|3day|widen | $+35.77 | 49% | 4.88 | $+29.25 | $+42.10 |
| A4_MorningRevCall|ATM|1DTE|1100-1200|3day|hold | $+33.83 | 53% | 4.41 | $+33.91 | $+33.77 |
| A3_GapUpPut|ATM|1DTE|1000-1100|3day|hold | $+29.43 | 55% | 3.39 | $+34.64 | $+24.72 |
| A8_ORBCall|ATM|1DTE|0930-1000|3day|hold | $+28.95 | 50% | 3.92 | $+28.49 | $+29.37 |
| A1_GapDownCall|ATM|1DTE|1000-1100|3day|hold | $+27.50 | 54% | 3.50 | $+31.75 | $+22.79 |
| A3_GapUpPut|ATM|1DTE|0930-1000|3day|widen | $+26.78 | 50% | 3.97 | $+26.27 | $+27.32 |
| A1_GapDownCall|ATM|1DTE|0930-1000|3day|widen | $+26.38 | 50% | 3.61 | $+21.91 | $+30.71 |
| A1_GapDownCall|ATM|1DTE|1100-1200|3day|widen | $+25.12 | 50% | 3.34 | $+31.11 | $+18.87 |
| A4_MorningRevCall|ATM|1DTE|0930-1000|3day|widen | $+24.62 | 53% | 3.03 | $+22.38 | $+27.06 |
| A4_MorningRevCall|ATM|1DTE|1100-1200|3day|widen | $+24.16 | 52% | 3.42 | $+13.19 | $+35.98 |
| A1_GapDownCall|ATM|1DTE|1000-1100|3day|widen | $+23.68 | 47% | 3.14 | $+14.88 | $+32.40 |
| A8_ORBCall|ATM|1DTE|0930-1000|3day|widen | $+23.49 | 49% | 3.15 | $+35.29 | $+10.61 |
| A4_MorningRevCall|ATM|1DTE|1000-1100|3day|widen | $+23.13 | 50% | 3.24 | $+27.87 | $+18.56 |
| A7_VWAPRejPut|ATM|1DTE|1000-1100|3day|hold | $+22.67 | 52% | 2.97 | $+20.82 | $+24.53 |
| A1_GapDownCall|ATM|1DTE|0930-1000|3day|hold | $+22.27 | 48% | 2.95 | $+10.02 | $+33.70 |
| A3_GapUpPut|ATM|1DTE|0930-1000|3day|hold | $+21.66 | 53% | 2.89 | $+16.60 | $+27.36 |
| A3_GapUpPut|OTM1|3DTE|1100-1200|3day|hold | $+21.58 | 47% | 2.78 | $+22.19 | $+21.10 |
| A8_ORBCall|ATM|1DTE|1000-1100|3day|widen | $+20.59 | 57% | 2.50 | $+24.03 | $+17.27 |
| A4_MorningRevCall|ATM|1DTE|0930-1000|3day|hold | $+20.36 | 51% | 2.62 | $+26.58 | $+14.14 |
| A7_VWAPRejPut|ATM|1DTE|1100-1200|3day|widen | $+20.30 | 51% | 2.90 | $+10.34 | $+28.82 |
| A4_MorningRevCall|ATM|1DTE|0930-1000|3day|cancel | $+19.98 | 40% | 3.15 | $+19.30 | $+20.73 |
| A4_MorningRevCall|OTM1|3DTE|1000-1100|3day|widen | $+19.77 | 47% | 2.58 | $+15.78 | $+23.59 |
| A7_VWAPRejPut|ATM|1DTE|1100-1200|3day|hold | $+19.74 | 54% | 2.74 | $+13.11 | $+26.43 |
| A8_ORBCall|ATM|1DTE|1100-1200|3day|hold | $+17.99 | 53% | 2.32 | $+20.44 | $+15.70 |
| A4_MorningRevCall|ATM|1DTE|1000-1100|3day|hold | $+17.65 | 48% | 2.34 | $+9.77 | $+25.98 |

## Hold-period recommendation per mechanic (mean Exp P&L/signal)

| Mechanic | intraday | EOD | 1day | 3day | BEST |
|---|---|---|---|---|---|
| A1_GapDownCall | $-2.41 | $-3.03 | $-2.47 | $+1.06 | 3day |
| A4_MorningRevCall | $-2.84 | $-2.37 | $-2.16 | $+0.51 | 3day |
| A8_ORBCall | $-2.80 | $-2.43 | $-0.58 | $+1.78 | 3day |
| A3_GapUpPut | $-2.50 | $-2.53 | $-2.09 | $+3.53 | 3day |
| A7_VWAPRejPut | $-2.50 | $-1.97 | $-1.46 | $+1.47 | 3day |

## Fill-behavior recommendation per mechanic (mean Exp P&L/signal)

| Mechanic | cancel | widen | hold | BEST |
|---|---|---|---|---|
| A1_GapDownCall | $-0.99 | $-1.59 | $-2.57 | cancel |
| A4_MorningRevCall | $-1.15 | $-1.79 | $-2.21 | cancel |
| A8_ORBCall | $-0.21 | $-1.84 | $-0.98 | cancel |
| A3_GapUpPut | $-0.16 | $-0.80 | $-1.72 | cancel |
| A7_VWAPRejPut | $-0.35 | $-1.19 | $-1.80 | cancel |

_Note: these two tables average Exp P&L/signal across ALL parameter combinations for each mechanic, so they are dominated by the many negative-edge (short-hold) combos — that is why `cancel` (trade less) tends to win the MEAN. Among the positive-edge variants on the leaderboard the opposite holds: higher-fill modes (`widen`/`hold`) compound a real edge and rank at the top. On real data, read the per-variant leaderboard, not just these marginal means._

## What this proves (and does not)

- PROVES: the Phase 3 grid machinery works end-to-end — it sweeps every axis, applies the adversarial engine, computes the Section 4 key metric, enforces the Section 7 thresholds, and produces ranked leaderboards + hold-period / fill-behavior recommendations.
- DOES NOT PROVE: any real strategy edge. Synthetic drifts are arbitrary. The production leaderboard requires ~4 weeks of Alpaca 1-min data via `load_alpaca_dataset(...)`; only then are rankings meaningful.
- DEVELOPMENT ONLY - NOT FOR TRADING DECISIONS