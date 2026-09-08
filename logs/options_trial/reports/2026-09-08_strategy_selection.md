# Options strategy selection report — 2026-09-08

_Generated 2026-09-08T16:46:10.537005_

## Summary

- Strategies analyzed: **105**
- Keep: **0**
- Watch: **83**
- Drop: **22**

## Attribution health

- Total exits: **2891**
- Orphan exits (b0/orphan_reconcile): **357**
- Orphan rate: **12.3%** (warn if >10%)
- **ALERT:** orphan_rate > 10% — check client_order_id tagging / fill attribution before trusting strategy P&L.

## Strategy scoreboard

| strategy | DTE | rec | exits | win% | med% | p10% | p25% | p90% | days live | ent 5d | exit 5d | realized $ | top share | rationale |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S168 (GapDown ATM 5-DTE — P2B arm) | 5d ATM | watch | 12 | 83.3 | +117.57 | -54.46 | +52.50 | +254.86 | 49 | 11 | 4 | $+510.00 | 50.0% | building sample (8-19 exits) |
| S167 (GapDown long call 3 DTE 1-OTM — P2C) | 3d 1-OTM | watch | 6 | 66.7 | +116.00 | -55.36 | -15.02 | +521.06 | 49 | 10 | 2 | $+252.00 | 33.3% | insufficient sample (<8 exits) |
| S396 (GapDown_ITM2) | 3d | watch | 4 | 75.0 | +83.82 | -35.16 | +35.39 | +95.00 | 33 | 2 | 0 | $+120.00 | 100.0% | insufficient sample (<8 exits) |
| S163 (A1 GapDown ATM call EOD) | 7d ATM | watch | 11 | 100.0 | +81.08 | +64.86 | +73.78 | +200.00 | 49 | 8 | 2 | $+478.00 | 45.5% | building sample (8-19 exits) |
| S166 (GapDown strong call) | 3d ATM strong | watch | 8 | 100.0 | +75.23 | +63.34 | +67.08 | +194.50 | 49 | 5 | 2 | $+436.00 | 62.5% | building sample (8-19 exits) |
| S406 (RubberBand_ITM3) | 3d | watch | 74 | 71.6 | +72.81 | -61.97 | -4.79 | +965.79 | 39 | 8 | 5 | $+3,431.00 | 20.3% | fat left tail (p10 < -45%) |
| S353 (GapDown_3DTE) | 3d | watch | 28 | 53.6 | +63.97 | -81.10 | -70.46 | +237.37 | 39 | 6 | 1 | $+191.00 | 32.1% | fat left tail (p10 < -45%) |
| S397 (GapDown_ITM1) | 3d | watch | 29 | 75.9 | +57.53 | -70.11 | +19.15 | +115.58 | 39 | 12 | 2 | $+757.00 | 24.1% | fat left tail (p10 < -45%) |
| S362 (RubberBand_3DTE) | 3d | watch | 45 | 75.6 | +57.14 | -59.43 | +8.70 | +694.28 | 39 | 6 | 2 | $+1,392.00 | 28.9% | fat left tail (p10 < -45%) |
| S357 (GapDown_21DTE) | 21d | watch | 24 | 79.2 | +55.04 | -76.29 | +47.06 | +78.98 | 39 | 4 | 1 | $+490.00 | 33.3% | fat left tail (p10 < -45%) |
| S410 (RubberBand_OTM1) | 3d | watch | 7 | 57.1 | +51.39 | -72.33 | -58.46 | +87.26 | 33 | 2 | 1 | $+70.00 | 85.7% | insufficient sample (<8 exits) |
| S403 (Any_MA50_Touch) | 3d | watch | 46 | 67.4 | +50.88 | -61.05 | -48.23 | +222.50 | 39 | 10 | 4 | $+925.00 | 19.6% | fat left tail (p10 < -45%) |
| S361 (RubberBand_2DTE) | 2d | watch | 42 | 57.1 | +50.36 | -68.33 | -47.61 | +246.00 | 39 | 6 | 1 | $+230.00 | 26.2% | fat left tail (p10 < -45%) |
| S404 (GapDown_OTM2) | 3d | watch | 45 | 64.4 | +50.00 | -91.67 | -41.89 | +117.95 | 39 | 15 | 5 | $+789.00 | 20.0% | fat left tail (p10 < -45%) |
| S218 (BB_Lower_Touch) | 3d ATM BB lower touch | watch | 74 | 56.8 | +41.03 | -70.00 | -47.61 | +161.14 | 43 | 8 | 6 | $+1,214.00 | 33.8% | fat left tail (p10 < -45%) |
| S412 (RubberBand_OTM3) | 3d | watch | 39 | 51.3 | +34.04 | -51.79 | -19.26 | +113.16 | 39 | 8 | 3 | $+168.00 | 20.5% | fat left tail (p10 < -45%) |
| S364 (RubberBand_7DTE) | 7d | watch | 50 | 52.0 | +23.90 | -85.97 | -57.98 | +188.89 | 39 | 2 | 0 | $+92.00 | 38.0% | fat left tail (p10 < -45%) |
| S350 (GapDown_0DTE) | 0d | watch | 41 | 53.7 | +15.00 | -62.75 | -50.00 | +260.00 | 39 | 10 | 2 | $+713.00 | 31.7% | fat left tail (p10 < -45%) |
| S401 (Any_Gap_Down_Small) | 3d | watch | 96 | 52.1 | +8.97 | -83.94 | -48.74 | +273.08 | 39 | 14 | 2 | $+1,209.00 | 33.3% | fat left tail (p10 < -45%) |
| S411 (RubberBand_OTM2) | 3d | watch | 36 | 52.8 | +5.20 | -56.72 | -51.46 | +54.09 | 36 | 10 | 3 | $-200.00 | 25.0% | fat left tail (p10 < -45%) |
| S398 (GapDown_ATM) | 3d | watch | 48 | 52.1 | +3.33 | -68.29 | -54.65 | +156.23 | 39 | 10 | 2 | $+732.00 | 31.2% | fat left tail (p10 < -45%) |
| S358 (GapDown_30DTE) | 30d | watch | 4 | 50.0 | +0.84 | -51.39 | -51.39 | +54.49 | 35 | 0 | 0 | $-21.00 | 50.0% | insufficient sample (<8 exits) |
| S365 (RubberBand_14DTE) | 14d | watch | 19 | 47.4 | +0.00 | -67.38 | -51.20 | +64.37 | 39 | 8 | 3 | $-6.00 | 31.6% | early sample with non-positive median |
| S169 (BB Squeeze Breakout call 3 DTE) | 3d ATM BB squeeze | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S170 (Golden Pocket call 3 DTE) | 3d ATM golden pocket | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S171 (VWAP Reclaim call 3 DTE) | 3d ATM VWAP reclaim | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S172 (Trend Resumption call 3 DTE) | 3d ATM trend resume | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S175 (Earnings Drift call 3 DTE) | 3d ATM earnings drift | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S200 (GapDown_Aggressive) | 3d ATM gap-aggr | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S201 (GapDown_Mild) | 3d ATM gap-mild | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S204 (GapUp_Continuation) | 3d ATM gap-up cont | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S205 (GapDown_HighVol) | 3d ATM gap-highvol | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S206 (GapDown_WithTrend) | 3d ATM gap-trend | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S208 (GapDown_AboveMA200) | 3d ATM gap-ma200 | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S213 (MA_Bounce_200) | 3d ATM MA bounce 200 | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S214 (MA_Death_Cross) | 3d ATM death cross (put) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S215 (MA_Reclaim_200) | 3d ATM MA reclaim 200 | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S219 (Volume_Climax_Up) | 3d ATM vol climax up | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S220 (Pullback50) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S221 (GoldenPocket) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S368 (BBSqueeze_0DTE) | 0d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S369 (BBSqueeze_1DTE) | 1d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S370 (BBSqueeze_2DTE) | 2d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S371 (BBSqueeze_3DTE) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S372 (BBSqueeze_5DTE) | 5d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S373 (BBSqueeze_7DTE) | 7d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S374 (BBSqueeze_14DTE) | 14d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S375 (BBSqueeze_21DTE) | 21d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S376 (BBSqueeze_30DTE) | 30d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S377 (GapDownAggr_0DTE) | 0d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S378 (GapDownAggr_1DTE) | 1d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S379 (GapDownAggr_2DTE) | 2d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S380 (GapDownAggr_3DTE) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S381 (GapDownAggr_5DTE) | 5d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S382 (GapDownAggr_7DTE) | 7d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S383 (GapDownAggr_14DTE) | 14d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S384 (GapDownAggr_21DTE) | 21d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S385 (GapDownAggr_30DTE) | 30d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S386 (VolClimax_0DTE) | 0d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S387 (VolClimax_1DTE) | 1d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S388 (VolClimax_2DTE) | 2d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S389 (VolClimax_3DTE) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S390 (VolClimax_5DTE) | 5d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S391 (VolClimax_7DTE) | 7d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S392 (VolClimax_14DTE) | 14d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S393 (VolClimax_21DTE) | 21d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S394 (VolClimax_30DTE) | 30d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S395 (GapDown_ITM3) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S402 (Any_High_Volume) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S409 (RubberBand_ATM) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S413 (BBSqueeze_ITM3) | 0d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S414 (BBSqueeze_ITM2) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S415 (BBSqueeze_ITM1) | 7d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S416 (BBSqueeze_ATM) | 0d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S417 (BBSqueeze_OTM1) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S418 (BBSqueeze_OTM2) | 7d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S419 (BBSqueeze_OTM3) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S367 (RubberBand_30DTE) | 30d | watch | 2 | 0.0 | -38.20 | -48.75 | -44.79 | -27.64 | 35 | 0 | 0 | $-55.00 | 100.0% | insufficient sample (<8 exits) |
| S164 (GapDown ATM 1-DTE — P2B arm) | 1d ATM | watch | 12 | 33.3 | -50.00 | -87.78 | -62.30 | +494.02 | 49 | 16 | 1 | $+228.00 | 41.7% | early sample with non-positive median |
| S400 (Any_Green_Close) | 3d | watch | 6 | 16.7 | -50.00 | -66.67 | -62.50 | +14.93 | 39 | 0 | 0 | $-5.00 | 83.3% | insufficient sample (<8 exits) |
| S366 (RubberBand_21DTE) | 21d | watch | 12 | 33.3 | -50.42 | -56.92 | -56.92 | +95.91 | 35 | 4 | 2 | $-77.00 | 66.7% | early sample with non-positive median |
| S202 (GapDown_Monster) | 3d ATM gap-monster | watch | 12 | 0.0 | -56.77 | -73.59 | -65.84 | -38.58 | 42 | 6 | 2 | $-208.00 | 33.3% | early sample with non-positive median |
| S209 (GapDown_Recovery) | 3d ATM gap-recovery | watch | 6 | 0.0 | -61.46 | -82.78 | -69.36 | -50.75 | 41 | 0 | 0 | $-210.00 | 83.3% | insufficient sample (<8 exits) |
| S408 (RubberBand_ITM1) | 3d | drop | 47 | 46.8 | +0.00 | -69.06 | -57.13 | +716.00 | 36 | 8 | 2 | $+1,100.00 | 21.3% | non-positive median return |
| S352 (GapDown_2DTE) | 2d | drop | 42 | 50.0 | -2.30 | -74.64 | -51.84 | +336.07 | 39 | 6 | 4 | $+120.00 | 26.2% | non-positive median return |
| S210 (MA_Cross_8_21) | 3d ATM MA cross 8/21 | drop | 75 | 49.3 | -4.35 | -79.42 | -50.96 | +72.84 | 43 | 12 | 5 | $-85.00 | 20.0% | non-positive median return |
| S355 (GapDown_7DTE) | 7d | drop | 59 | 49.2 | -15.62 | -69.48 | -61.25 | +188.75 | 39 | 6 | 2 | $+553.00 | 28.8% | non-positive median return |
| S356 (GapDown_14DTE) | 14d | drop | 21 | 38.1 | -19.44 | -51.67 | -50.00 | +58.62 | 39 | 9 | 2 | $-31.00 | 28.6% | non-positive median return |
| S174 (RubberBand long call EOD) | RubberBand (dropped) | drop | 119 | 36.1 | -25.00 | -89.83 | -71.19 | +36.67 | 64 | 0 | 0 | $-1,658.19 | 50.4% | non-positive median return |
| S173 (MomReversal long call) | MomRev | drop | 415 | 37.1 | -31.51 | -77.18 | -62.95 | +101.90 | 64 | 0 | 0 | $+62.64 | 27.5% | non-positive median return |
| S165 (GapDown long call 3 DTE) | 3d ATM | drop | 249 | 30.9 | -38.00 | -63.29 | -53.52 | +84.90 | 64 | 10 | 0 | $-1,526.78 | 26.5% | non-positive median return |
| S211 (MA_Cross_21_50) | 3d ATM MA cross 21/50 | drop | 43 | 27.9 | -38.10 | -80.62 | -55.60 | +102.82 | 43 | 0 | 0 | $-207.00 | 34.9% | non-positive median return |
| S405 (GapDown_OTM3) | 3d | drop | 56 | 33.9 | -42.86 | -83.93 | -65.20 | +103.47 | 39 | 0 | 0 | $-118.00 | 26.8% | manually paused — excluded from new entries & reflected P&L |
| S359 (RubberBand_0DTE) | 0d | drop | 30 | 33.3 | -44.44 | -71.43 | -67.98 | +164.28 | 36 | 8 | 3 | $-151.00 | 33.3% | non-positive median return |
| S399 (GapDown_OTM1) | 3d | drop | 57 | 47.4 | -46.15 | -84.19 | -66.67 | +182.60 | 39 | 17 | 4 | $+91.00 | 28.1% | non-positive median return |
| S217 (RSI_25_Bounce) | 3d ATM RSI<25 bounce | drop | 56 | 41.1 | -46.15 | -78.75 | -56.38 | +132.35 | 43 | 6 | 5 | $+465.00 | 53.6% | non-positive median return |
| S207 (GapDown_AtSupport) | 3d ATM gap-support | drop | 37 | 5.4 | -47.06 | -63.64 | -55.71 | -6.06 | 43 | 0 | 0 | $-822.00 | 43.2% | manually paused — excluded from new entries & reflected P&L |
| S407 (RubberBand_ITM2) | 3d | drop | 38 | 28.9 | -47.73 | -83.88 | -61.54 | +266.42 | 39 | 0 | 0 | $+33.00 | 26.3% | manually paused — excluded from new entries & reflected P&L |
| S354 (GapDown_5DTE) | 5d | drop | 51 | 41.2 | -50.77 | -92.16 | -75.99 | +137.78 | 39 | 6 | 0 | $+220.00 | 27.5% | non-positive median return |
| S351 (GapDown_1DTE) | 1d | drop | 58 | 25.9 | -52.09 | -77.47 | -66.52 | +236.04 | 39 | 16 | 3 | $+45.00 | 22.4% | non-positive median return |
| S216 (RSI_Oversold_Cross) | 3d ATM RSI x30 | drop | 39 | 20.5 | -52.63 | -81.81 | -72.69 | +105.90 | 43 | 6 | 1 | $-538.00 | 41.0% | non-positive median return |
| S203 (GapUp_Fade) | 3d ATM gap-up fade (put) | drop | 40 | 10.0 | -55.91 | -78.77 | -67.43 | -3.10 | 43 | 0 | 0 | $-797.00 | 35.0% | manually paused — excluded from new entries & reflected P&L |
| S360 (RubberBand_1DTE) | 1d | drop | 49 | 10.2 | -56.41 | -81.50 | -70.37 | -6.89 | 39 | 0 | 0 | $-913.00 | 22.4% | manually paused — excluded from new entries & reflected P&L |
| S212 (MA_Bounce_50) | 3d ATM MA bounce 50 | drop | 83 | 13.3 | -68.09 | -98.15 | -81.35 | +51.47 | 43 | 0 | 0 | $-2,246.00 | 34.9% | manually paused — excluded from new entries & reflected P&L |
| S363 (RubberBand_5DTE) | 5d | drop | 32 | 40.6 | -68.84 | -92.31 | -88.94 | +87.99 | 36 | 2 | 0 | $-671.00 | 34.4% | non-positive median return |

## Comparison groups

Experiment arms grouped for side-by-side decisions. INSUFFICIENT if any arm has n<10 exits.

### GapDown DTE comparison

- Status: **OK** | Best median: **S168** (+117.57%) | Best p10: **S163** (+64.86%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S163 | 7d ATM | 11 | +81.08 | +64.86 | +73.78 | 8 | 2 |
| S164 | 1d ATM | 12 | -50.00 | -87.78 | -62.30 | 16 | 1 |
| S165 | 3d ATM | 249 | -38.00 | -63.29 | -53.52 | 10 | 0 |
| S168 | 5d ATM | 12 | +117.57 | -54.46 | +52.50 | 11 | 4 |

### GapDown Strike comparison

- Status: **INSUFFICIENT** | Best median: **S167** (+116.00%) | Best p10: **S167** (-55.36%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S165 | 3d ATM | 249 | -38.00 | -63.29 | -53.52 | 10 | 0 |
| S167 | 3d 1-OTM | 6 | +116.00 | -55.36 | -15.02 | 10 | 2 |

### New Pattern Strategies — GapDown signal independent

- Status: **INSUFFICIENT** | Best median: **S169** (+0.00%) | Best p10: **S169** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S169 | 3d ATM BB squeeze | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S170 | 3d ATM golden pocket | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S171 | 3d ATM VWAP reclaim | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S172 | 3d ATM trend resume | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S175 | 3d ATM earnings drift | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 Gap family

- Status: **INSUFFICIENT** | Best median: **S200** (+0.00%) | Best p10: **S200** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S200 | 3d ATM gap-aggr | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S201 | 3d ATM gap-mild | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S202 | 3d ATM gap-monster | 12 | -56.77 | -73.59 | -65.84 | 6 | 2 |
| S204 | 3d ATM gap-up cont | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S205 | 3d ATM gap-highvol | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S206 | 3d ATM gap-trend | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S207 | 3d ATM gap-support | 37 | -47.06 | -63.64 | -55.71 | 0 | 0 |
| S208 | 3d ATM gap-ma200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S209 | 3d ATM gap-recovery | 6 | -61.46 | -82.78 | -69.36 | 0 | 0 |

### Phase-1 Bearish Gap & MA

- Status: **INSUFFICIENT** | Best median: **S214** (+0.00%) | Best p10: **S214** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S203 | 3d ATM gap-up fade (put) | 40 | -55.91 | -78.77 | -67.43 | 0 | 0 |
| S214 | 3d ATM death cross (put) | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 MA family

- Status: **INSUFFICIENT** | Best median: **S213** (+0.00%) | Best p10: **S213** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S210 | 3d ATM MA cross 8/21 | 75 | -4.35 | -79.42 | -50.96 | 12 | 5 |
| S211 | 3d ATM MA cross 21/50 | 43 | -38.10 | -80.62 | -55.60 | 0 | 0 |
| S212 | 3d ATM MA bounce 50 | 83 | -68.09 | -98.15 | -81.35 | 0 | 0 |
| S213 | 3d ATM MA bounce 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S215 | 3d ATM MA reclaim 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 RSI/BB/Vol

- Status: **INSUFFICIENT** | Best median: **S218** (+41.03%) | Best p10: **S219** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S216 | 3d ATM RSI x30 | 39 | -52.63 | -81.81 | -72.69 | 6 | 1 |
| S217 | 3d ATM RSI<25 bounce | 56 | -46.15 | -78.75 | -56.38 | 6 | 5 |
| S218 | 3d ATM BB lower touch | 74 | +41.03 | -70.00 | -47.61 | 8 | 6 |
| S219 | 3d ATM vol climax up | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Other

- Status: **OK** | Best median: **S173** (-31.51%) | Best p10: **S173** (-77.18%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S173 | MomRev | 415 | -31.51 | -77.18 | -62.95 | 0 | 0 |

## Strategy Pipeline Status

_Pipeline evaluation as of 2026-09-08. Auto-kill thresholds: median<-25% at n>=15, p10<-85%, WR<15% at n>=25. Promote: n>=30 median>0%._

| Strategy | Signal | n | Median% | WR% | Status | Days |
|----------|--------|---|---------|-----|--------|------|
| S163 | A1 GapDown ATM call EO | 11 | +81.08% | 100% | WATCH | 49 |
| S164 | GapDown ATM 1-DTE — P2 | 12 | -50.00% | 33% | WATCH | 49 |
| S165 | GapDown long call 3 DT | 249 | -38.00% | 31% | INSUFFICIENT | 64 |
| S166 | GapDown strong call | 8 | +75.23% | 100% | WATCH | 49 |
| S167 | GapDown long call 3 DT | 6 | +116.00% | 67% | WATCH | 49 |
| S168 | GapDown ATM 5-DTE — P2 | 12 | +117.57% | 83% | WATCH | 49 |
| S169 | BB Squeeze Breakout ca | 0 | — | — | NEW | 0 |
| S170 | Golden Pocket call 3 D | 0 | — | — | NEW | 0 |
| S171 | VWAP Reclaim call 3 DT | 0 | — | — | NEW | 0 |
| S172 | Trend Resumption call  | 0 | — | — | NEW | 0 |
| S173 | MomReversal long call | 415 | -31.51% | 37% | INSUFFICIENT | 64 |
| S174 | RubberBand long call E | 119 | -25.00% | 36% | INSUFFICIENT | 64 |
| S175 | Earnings Drift call 3  | 0 | — | — | NEW | 0 |
| S200 | GapDown_Aggressive | 0 | — | — | NEW | 0 |
| S201 | GapDown_Mild | 0 | — | — | NEW | 0 |
| S202 | GapDown_Monster | 12 | -56.77% | 0% | WATCH | 42 |
| S203 | GapUp_Fade | 40 | -55.91% | 10% | INSUFFICIENT | 43 |
| S204 | GapUp_Continuation | 0 | — | — | NEW | 0 |
| S205 | GapDown_HighVol | 0 | — | — | NEW | 0 |
| S206 | GapDown_WithTrend | 0 | — | — | NEW | 0 |
| S207 | GapDown_AtSupport | 37 | -47.06% | 5% | INSUFFICIENT | 43 |
| S208 | GapDown_AboveMA200 | 0 | — | — | NEW | 0 |
| S209 | GapDown_Recovery | 6 | -61.46% | 0% | WATCH | 41 |
| S210 | MA_Cross_8_21 | 75 | -4.35% | 49% | INSUFFICIENT | 43 |
| S211 | MA_Cross_21_50 | 43 | -38.10% | 28% | INSUFFICIENT | 43 |
| S212 | MA_Bounce_50 | 83 | -68.09% | 13% | INSUFFICIENT | 43 |
| S213 | MA_Bounce_200 | 0 | — | — | NEW | 0 |
| S214 | MA_Death_Cross | 0 | — | — | NEW | 0 |
| S215 | MA_Reclaim_200 | 0 | — | — | NEW | 0 |
| S216 | RSI_Oversold_Cross | 39 | -52.63% | 21% | INSUFFICIENT | 43 |
| S217 | RSI_25_Bounce | 56 | -46.15% | 41% | INSUFFICIENT | 43 |
| S218 | BB_Lower_Touch | 74 | +41.03% | 57% | INSUFFICIENT | 43 |
| S219 | Volume_Climax_Up | 0 | — | — | NEW | 0 |
| S220 | Pullback50 | 0 | — | — | NEW | 0 |
| S221 | GoldenPocket | 0 | — | — | NEW | 0 |
| S350 | GapDown_0DTE | 41 | +15.00% | 54% | INSUFFICIENT | 39 |
| S351 | GapDown_1DTE | 58 | -52.09% | 26% | INSUFFICIENT | 39 |
| S352 | GapDown_2DTE | 42 | -2.30% | 50% | INSUFFICIENT | 39 |
| S353 | GapDown_3DTE | 28 | +63.97% | 54% | INSUFFICIENT | 39 |
| S354 | GapDown_5DTE | 51 | -50.77% | 41% | INSUFFICIENT | 39 |
| S355 | GapDown_7DTE | 59 | -15.62% | 49% | INSUFFICIENT | 39 |
| S356 | GapDown_14DTE | 21 | -19.44% | 38% | INSUFFICIENT | 39 |
| S357 | GapDown_21DTE | 24 | +55.04% | 79% | INSUFFICIENT | 39 |
| S358 | GapDown_30DTE | 4 | +0.84% | 50% | WATCH | 35 |
| S359 | RubberBand_0DTE | 30 | -44.44% | 33% | INSUFFICIENT | 36 |
| S360 | RubberBand_1DTE | 49 | -56.41% | 10% | INSUFFICIENT | 39 |
| S361 | RubberBand_2DTE | 42 | +50.36% | 57% | INSUFFICIENT | 39 |
| S362 | RubberBand_3DTE | 45 | +57.14% | 76% | INSUFFICIENT | 39 |
| S363 | RubberBand_5DTE | 32 | -68.84% | 41% | INSUFFICIENT | 36 |
| S364 | RubberBand_7DTE | 50 | +23.90% | 52% | INSUFFICIENT | 39 |
| S365 | RubberBand_14DTE | 19 | +0.00% | 47% | INSUFFICIENT | 39 |
| S366 | RubberBand_21DTE | 12 | -50.42% | 33% | WATCH | 35 |
| S367 | RubberBand_30DTE | 2 | -38.20% | 0% | WATCH | 35 |
| S368 | BBSqueeze_0DTE | 0 | — | — | NEW | 0 |
| S369 | BBSqueeze_1DTE | 0 | — | — | NEW | 0 |
| S370 | BBSqueeze_2DTE | 0 | — | — | NEW | 0 |
| S371 | BBSqueeze_3DTE | 0 | — | — | NEW | 0 |
| S372 | BBSqueeze_5DTE | 0 | — | — | NEW | 0 |
| S373 | BBSqueeze_7DTE | 0 | — | — | NEW | 0 |
| S374 | BBSqueeze_14DTE | 0 | — | — | NEW | 0 |
| S375 | BBSqueeze_21DTE | 0 | — | — | NEW | 0 |
| S376 | BBSqueeze_30DTE | 0 | — | — | NEW | 0 |
| S377 | GapDownAggr_0DTE | 0 | — | — | NEW | 0 |
| S378 | GapDownAggr_1DTE | 0 | — | — | NEW | 0 |
| S379 | GapDownAggr_2DTE | 0 | — | — | NEW | 0 |
| S380 | GapDownAggr_3DTE | 0 | — | — | NEW | 0 |
| S381 | GapDownAggr_5DTE | 0 | — | — | NEW | 0 |
| S382 | GapDownAggr_7DTE | 0 | — | — | NEW | 0 |
| S383 | GapDownAggr_14DTE | 0 | — | — | NEW | 0 |
| S384 | GapDownAggr_21DTE | 0 | — | — | NEW | 0 |
| S385 | GapDownAggr_30DTE | 0 | — | — | NEW | 0 |
| S386 | VolClimax_0DTE | 0 | — | — | NEW | 0 |
| S387 | VolClimax_1DTE | 0 | — | — | NEW | 0 |
| S388 | VolClimax_2DTE | 0 | — | — | NEW | 0 |
| S389 | VolClimax_3DTE | 0 | — | — | NEW | 0 |
| S390 | VolClimax_5DTE | 0 | — | — | NEW | 0 |
| S391 | VolClimax_7DTE | 0 | — | — | NEW | 0 |
| S392 | VolClimax_14DTE | 0 | — | — | NEW | 0 |
| S393 | VolClimax_21DTE | 0 | — | — | NEW | 0 |
| S394 | VolClimax_30DTE | 0 | — | — | NEW | 0 |
| S395 | GapDown_ITM3 | 0 | — | — | NEW | 0 |
| S396 | GapDown_ITM2 | 4 | +83.82% | 75% | WATCH | 33 |
| S397 | GapDown_ITM1 | 29 | +57.53% | 76% | INSUFFICIENT | 39 |
| S398 | GapDown_ATM | 48 | +3.33% | 52% | INSUFFICIENT | 39 |
| S399 | GapDown_OTM1 | 57 | -46.15% | 47% | INSUFFICIENT | 39 |
| S400 | Any_Green_Close | 6 | -50.00% | 17% | WATCH | 39 |
| S401 | Any_Gap_Down_Small | 96 | +8.97% | 52% | INSUFFICIENT | 39 |
| S402 | Any_High_Volume | 0 | — | — | NEW | 0 |
| S403 | Any_MA50_Touch | 46 | +50.88% | 67% | INSUFFICIENT | 39 |
| S404 | GapDown_OTM2 | 45 | +50.00% | 64% | INSUFFICIENT | 39 |
| S405 | GapDown_OTM3 | 56 | -42.86% | 34% | INSUFFICIENT | 39 |
| S406 | RubberBand_ITM3 | 74 | +72.81% | 72% | INSUFFICIENT | 39 |
| S407 | RubberBand_ITM2 | 38 | -47.73% | 29% | INSUFFICIENT | 39 |
| S408 | RubberBand_ITM1 | 47 | +0.00% | 47% | INSUFFICIENT | 36 |
| S409 | RubberBand_ATM | 0 | — | — | NEW | 0 |
| S410 | RubberBand_OTM1 | 7 | +51.39% | 57% | WATCH | 33 |
| S411 | RubberBand_OTM2 | 36 | +5.20% | 53% | INSUFFICIENT | 36 |
| S412 | RubberBand_OTM3 | 39 | +34.04% | 51% | INSUFFICIENT | 39 |
| S413 | BBSqueeze_ITM3 | 0 | — | — | NEW | 0 |
| S414 | BBSqueeze_ITM2 | 0 | — | — | NEW | 0 |
| S415 | BBSqueeze_ITM1 | 0 | — | — | NEW | 0 |
| S416 | BBSqueeze_ATM | 0 | — | — | NEW | 0 |
| S417 | BBSqueeze_OTM1 | 0 | — | — | NEW | 0 |
| S418 | BBSqueeze_OTM2 | 0 | — | — | NEW | 0 |
| S419 | BBSqueeze_OTM3 | 0 | — | — | NEW | 0 |

## Auto-Kill Log

| Date | Strategy | Reason | n | Median% |
|------|----------|--------|---|---------|
| — | — | (no kills yet) | — | — |

## Promote Candidates (n>=30, median>0%)

| Strategy | n | Median% | WR% | Recommendation |
|----------|---|---------|-----|----------------|
| S406 | 74 | +72.81% | 72% | Tyler review |
| S362 | 45 | +57.14% | 76% | Tyler review |
| S403 | 46 | +50.88% | 67% | Tyler review |
| S361 | 42 | +50.36% | 57% | Tyler review |
| S404 | 45 | +50.00% | 64% | Tyler review |
| S218 | 74 | +41.03% | 57% | Tyler review |
| S412 | 39 | +34.04% | 51% | Tyler review |
| S364 | 50 | +23.90% | 52% | Tyler review |
| S350 | 41 | +15.00% | 54% | Tyler review |
| S401 | 96 | +8.97% | 52% | Tyler review |
| S411 | 36 | +5.20% | 53% | Tyler review |
| S398 | 48 | +3.33% | 52% | Tyler review |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- **p25** sits between p10 and median for mid-tail visibility.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
- Active paper strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419.
