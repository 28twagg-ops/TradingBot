# Options strategy selection report — 2026-09-01

_Generated 2026-09-01T15:40:27.450472_

## Summary

- Strategies analyzed: **105**
- Keep: **0**
- Watch: **79**
- Drop: **26**

## Attribution health

- Total exits: **2594**
- Orphan exits (b0/orphan_reconcile): **345**
- Orphan rate: **13.3%** (warn if >10%)
- **ALERT:** orphan_rate > 10% — check client_order_id tagging / fill attribution before trusting strategy P&L.

## Strategy scoreboard

| strategy | DTE | rec | exits | win% | med% | p10% | p25% | p90% | days live | ent 5d | exit 5d | realized $ | top share | rationale |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S406 (RubberBand_ITM3) | 3d | watch | 61 | 65.6 | +63.64 | -63.41 | -50.00 | +965.79 | 32 | 3 | 1 | $+3,092.00 | 23.0% | fat left tail (p10 < -45%) |
| S397 (GapDown_ITM1) | 3d | watch | 22 | 86.4 | +59.72 | -50.06 | +41.18 | +116.29 | 32 | 4 | 0 | $+733.00 | 31.8% | fat left tail (p10 < -45%) |
| S357 (GapDown_21DTE) | 21d | watch | 18 | 77.8 | +55.07 | -67.86 | +47.06 | +73.68 | 32 | 2 | 0 | $+323.00 | 44.4% | building sample (8-19 exits) |
| S404 (GapDown_OTM2) | 3d | watch | 32 | 71.9 | +50.39 | -91.67 | -11.75 | +122.93 | 32 | 5 | 0 | $+661.00 | 28.1% | fat left tail (p10 < -45%) |
| S403 (Any_MA50_Touch) | 3d | watch | 32 | 53.1 | +49.12 | -76.32 | -51.61 | +310.23 | 32 | 4 | 0 | $+373.00 | 28.1% | fat left tail (p10 < -45%) |
| S218 (BB_Lower_Touch) | 3d ATM BB lower touch | watch | 61 | 57.4 | +36.36 | -71.43 | -48.48 | +166.67 | 36 | 6 | 1 | $+944.00 | 41.0% | fat left tail (p10 < -45%) |
| S362 (RubberBand_3DTE) | 3d | watch | 35 | 68.6 | +25.45 | -67.00 | -42.02 | +111.91 | 32 | 4 | 0 | $+1,036.00 | 37.1% | fat left tail (p10 < -45%) |
| S350 (GapDown_0DTE) | 0d | watch | 35 | 51.4 | +11.76 | -65.10 | -54.17 | +179.86 | 32 | 0 | 0 | $+446.00 | 37.1% | fat left tail (p10 < -45%) |
| S411 (RubberBand_OTM2) | 3d | watch | 29 | 55.2 | +7.69 | -57.02 | -51.67 | +39.66 | 29 | 4 | 0 | $-210.00 | 31.0% | fat left tail (p10 < -45%) |
| S401 (Any_Gap_Down_Small) | 3d | watch | 92 | 50.0 | +3.47 | -91.89 | -49.27 | +227.27 | 32 | 2 | 0 | $+894.00 | 34.8% | fat left tail (p10 < -45%) |
| S358 (GapDown_30DTE) | 30d | watch | 4 | 50.0 | +0.84 | -51.39 | -51.39 | +54.49 | 28 | 0 | 0 | $-21.00 | 50.0% | insufficient sample (<8 exits) |
| S163 (A1 GapDown ATM call EOD) | 7d ATM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 42 | 4 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | 3d ATM strong | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 42 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S167 (GapDown long call 3 DTE 1-OTM — P2C) | 3d 1-OTM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 42 | 2 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S168 (GapDown ATM 5-DTE — P2B arm) | 5d ATM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 42 | 2 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
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
| S356 (GapDown_14DTE) | 14d | watch | 17 | 23.5 | -25.00 | -52.49 | -50.00 | +46.21 | 32 | 2 | 0 | $-151.00 | 35.3% | early sample with non-positive median |
| S367 (RubberBand_30DTE) | 30d | watch | 2 | 0.0 | -38.20 | -48.75 | -44.79 | -27.64 | 28 | 0 | 0 | $-55.00 | 100.0% | insufficient sample (<8 exits) |
| S365 (RubberBand_14DTE) | 14d | watch | 12 | 16.7 | -49.56 | -81.56 | -55.12 | +49.36 | 32 | 4 | 0 | $-186.00 | 50.0% | early sample with non-positive median |
| S400 (Any_Green_Close) | 3d | watch | 6 | 16.7 | -50.00 | -66.67 | -62.50 | +14.93 | 32 | 0 | 0 | $-5.00 | 83.3% | insufficient sample (<8 exits) |
| S164 (GapDown ATM 1-DTE — P2B arm) | 1d ATM | watch | 7 | 0.0 | -53.57 | -88.89 | -83.34 | -49.23 | 42 | 2 | 1 | $-84.00 | 71.4% | insufficient sample (<8 exits) |
| S366 (RubberBand_21DTE) | 21d | watch | 8 | 0.0 | -55.19 | -58.31 | -56.92 | -49.12 | 28 | 2 | 0 | $-268.00 | 100.0% | early sample with non-positive median |
| S410 (RubberBand_OTM1) | 3d | watch | 4 | 25.0 | -58.46 | -75.20 | -70.89 | +56.51 | 26 | 0 | 0 | $-70.00 | 75.0% | insufficient sample (<8 exits) |
| S202 (GapDown_Monster) | 3d ATM gap-monster | watch | 10 | 0.0 | -60.53 | -74.54 | -66.39 | -37.62 | 35 | 0 | 0 | $-171.00 | 40.0% | early sample with non-positive median |
| S209 (GapDown_Recovery) | 3d ATM gap-recovery | watch | 6 | 0.0 | -61.46 | -82.78 | -69.36 | -50.75 | 34 | 0 | 0 | $-210.00 | 83.3% | insufficient sample (<8 exits) |
| S396 (GapDown_ITM2) | 3d | watch | 1 | 0.0 | -82.19 | -82.19 | -82.19 | -82.19 | 26 | 2 | 0 | $-60.00 | 100.0% | insufficient sample (<8 exits) |
| S408 (RubberBand_ITM1) | 3d | drop | 43 | 46.5 | +0.00 | -69.93 | -55.56 | +776.45 | 29 | 4 | 0 | $+1,095.00 | 23.3% | non-positive median return |
| S412 (RubberBand_OTM3) | 3d | drop | 31 | 41.9 | -3.57 | -51.79 | -23.26 | +85.29 | 32 | 4 | 2 | $+34.00 | 25.8% | non-positive median return |
| S398 (GapDown_ATM) | 3d | drop | 42 | 50.0 | -4.05 | -68.29 | -57.35 | +157.56 | 32 | 2 | 0 | $+649.00 | 35.7% | non-positive median return |
| S210 (MA_Cross_8_21) | 3d ATM MA cross 8/21 | drop | 68 | 48.5 | -5.30 | -82.21 | -51.32 | +68.78 | 36 | 0 | 0 | $-140.00 | 22.1% | non-positive median return |
| S361 (RubberBand_2DTE) | 2d | drop | 35 | 48.6 | -6.67 | -70.41 | -53.62 | +109.68 | 32 | 2 | 1 | $-64.00 | 31.4% | non-positive median return |
| S174 (RubberBand long call EOD) | RubberBand (dropped) | drop | 119 | 36.1 | -25.00 | -89.83 | -71.19 | +36.67 | 57 | 0 | 0 | $-1,658.19 | 50.4% | non-positive median return |
| S352 (GapDown_2DTE) | 2d | drop | 34 | 44.1 | -27.95 | -83.88 | -55.35 | +105.83 | 32 | 4 | 2 | $-73.00 | 32.4% | non-positive median return |
| S173 (MomReversal long call) | MomRev | drop | 415 | 37.1 | -31.51 | -77.18 | -62.95 | +101.90 | 57 | 0 | 0 | $+62.64 | 27.5% | non-positive median return |
| S211 (MA_Cross_21_50) | 3d ATM MA cross 21/50 | drop | 41 | 29.3 | -31.58 | -81.13 | -51.47 | +107.69 | 36 | 0 | 0 | $-203.00 | 36.6% | non-positive median return |
| S353 (GapDown_3DTE) | 3d | drop | 20 | 40.0 | -34.69 | -85.57 | -76.88 | +124.42 | 32 | 4 | 0 | $-46.00 | 45.0% | non-positive median return |
| S165 (GapDown long call 3 DTE) | 3d ATM | drop | 245 | 29.8 | -38.18 | -63.39 | -54.55 | +81.82 | 57 | 2 | 0 | $-1,828.78 | 26.1% | non-positive median return |
| S364 (RubberBand_7DTE) | 7d | drop | 43 | 44.2 | -42.31 | -90.75 | -63.64 | +77.78 | 32 | 2 | 1 | $-209.00 | 30.2% | non-positive median return |
| S405 (GapDown_OTM3) | 3d | drop | 56 | 33.9 | -42.86 | -83.93 | -65.20 | +103.47 | 32 | 0 | 0 | $-118.00 | 26.8% | manually paused — excluded from new entries & reflected P&L |
| S399 (GapDown_OTM1) | 3d | drop | 43 | 44.2 | -46.67 | -84.92 | -67.34 | +138.80 | 32 | 4 | 0 | $-64.00 | 37.2% | non-positive median return |
| S359 (RubberBand_0DTE) | 0d | drop | 23 | 17.4 | -46.67 | -71.43 | -70.37 | +61.82 | 29 | 0 | 0 | $-323.00 | 43.5% | non-positive median return |
| S207 (GapDown_AtSupport) | 3d ATM gap-support | drop | 37 | 5.4 | -47.06 | -63.64 | -55.71 | -6.06 | 36 | 0 | 0 | $-822.00 | 43.2% | manually paused — excluded from new entries & reflected P&L |
| S407 (RubberBand_ITM2) | 3d | drop | 38 | 28.9 | -47.73 | -83.88 | -61.54 | +266.42 | 32 | 0 | 0 | $+33.00 | 26.3% | manually paused — excluded from new entries & reflected P&L |
| S217 (RSI_25_Bounce) | 3d ATM RSI<25 bounce | drop | 40 | 35.0 | -48.08 | -80.50 | -60.38 | +169.51 | 36 | 2 | 0 | $+284.00 | 75.0% | non-positive median return |
| S355 (GapDown_7DTE) | 7d | drop | 49 | 38.8 | -48.57 | -74.48 | -63.41 | +134.39 | 32 | 4 | 0 | $+105.00 | 24.5% | non-positive median return |
| S354 (GapDown_5DTE) | 5d | drop | 45 | 33.3 | -52.31 | -92.16 | -76.47 | +138.30 | 32 | 0 | 0 | $-7.00 | 31.1% | non-positive median return |
| S216 (RSI_Oversold_Cross) | 3d ATM RSI x30 | drop | 35 | 20.0 | -52.63 | -84.46 | -71.24 | +168.86 | 36 | 0 | 0 | $-511.00 | 45.7% | non-positive median return |
| S351 (GapDown_1DTE) | 1d | drop | 51 | 21.6 | -53.85 | -81.63 | -69.68 | +171.88 | 32 | 2 | 1 | $-274.00 | 25.5% | non-positive median return |
| S203 (GapUp_Fade) | 3d ATM gap-up fade (put) | drop | 40 | 10.0 | -55.91 | -78.77 | -67.43 | -3.10 | 36 | 2 | 1 | $-797.00 | 35.0% | manually paused — excluded from new entries & reflected P&L |
| S360 (RubberBand_1DTE) | 1d | drop | 49 | 10.2 | -56.41 | -81.50 | -70.37 | -6.89 | 32 | 0 | 0 | $-913.00 | 22.4% | manually paused — excluded from new entries & reflected P&L |
| S212 (MA_Bounce_50) | 3d ATM MA bounce 50 | drop | 83 | 13.3 | -68.09 | -98.15 | -81.35 | +51.47 | 36 | 0 | 0 | $-2,246.00 | 34.9% | manually paused — excluded from new entries & reflected P&L |
| S363 (RubberBand_5DTE) | 5d | drop | 30 | 36.7 | -73.91 | -92.82 | -89.90 | +61.07 | 29 | 2 | 0 | $-735.00 | 36.7% | non-positive median return |

## Comparison groups

Experiment arms grouped for side-by-side decisions. INSUFFICIENT if any arm has n<10 exits.

### GapDown DTE comparison

- Status: **INSUFFICIENT** | Best median: **S163** (+0.00%) | Best p10: **S163** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S163 | 7d ATM | 0 | +0.00 | +0.00 | +0.00 | 4 | 0 |
| S164 | 1d ATM | 7 | -53.57 | -88.89 | -83.34 | 2 | 1 |
| S165 | 3d ATM | 245 | -38.18 | -63.39 | -54.55 | 2 | 0 |
| S168 | 5d ATM | 0 | +0.00 | +0.00 | +0.00 | 2 | 0 |

### GapDown Strike comparison

- Status: **INSUFFICIENT** | Best median: **S167** (+0.00%) | Best p10: **S167** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S165 | 3d ATM | 245 | -38.18 | -63.39 | -54.55 | 2 | 0 |
| S167 | 3d 1-OTM | 0 | +0.00 | +0.00 | +0.00 | 2 | 0 |

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
| S202 | 3d ATM gap-monster | 10 | -60.53 | -74.54 | -66.39 | 0 | 0 |
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
| S203 | 3d ATM gap-up fade (put) | 40 | -55.91 | -78.77 | -67.43 | 2 | 1 |
| S214 | 3d ATM death cross (put) | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 MA family

- Status: **INSUFFICIENT** | Best median: **S213** (+0.00%) | Best p10: **S213** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S210 | 3d ATM MA cross 8/21 | 68 | -5.30 | -82.21 | -51.32 | 0 | 0 |
| S211 | 3d ATM MA cross 21/50 | 41 | -31.58 | -81.13 | -51.47 | 0 | 0 |
| S212 | 3d ATM MA bounce 50 | 83 | -68.09 | -98.15 | -81.35 | 0 | 0 |
| S213 | 3d ATM MA bounce 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S215 | 3d ATM MA reclaim 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 RSI/BB/Vol

- Status: **INSUFFICIENT** | Best median: **S218** (+36.36%) | Best p10: **S219** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S216 | 3d ATM RSI x30 | 35 | -52.63 | -84.46 | -71.24 | 0 | 0 |
| S217 | 3d ATM RSI<25 bounce | 40 | -48.08 | -80.50 | -60.38 | 2 | 0 |
| S218 | 3d ATM BB lower touch | 61 | +36.36 | -71.43 | -48.48 | 6 | 1 |
| S219 | 3d ATM vol climax up | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Other

- Status: **OK** | Best median: **S173** (-31.51%) | Best p10: **S173** (-77.18%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S173 | MomRev | 415 | -31.51 | -77.18 | -62.95 | 0 | 0 |

## Strategy Pipeline Status

_Pipeline evaluation as of 2026-09-01. Auto-kill thresholds: median<-25% at n>=15, p10<-85%, WR<15% at n>=25. Promote: n>=30 median>0%._

| Strategy | Signal | n | Median% | WR% | Status | Days |
|----------|--------|---|---------|-----|--------|------|
| S163 | A1 GapDown ATM call EO | 0 | — | — | NEW | 42 |
| S164 | GapDown ATM 1-DTE — P2 | 7 | -53.57% | 0% | WATCH | 42 |
| S165 | GapDown long call 3 DT | 245 | -38.18% | 30% | INSUFFICIENT | 57 |
| S166 | GapDown strong call | 0 | — | — | NEW | 42 |
| S167 | GapDown long call 3 DT | 0 | — | — | NEW | 42 |
| S168 | GapDown ATM 5-DTE — P2 | 0 | — | — | NEW | 42 |
| S169 | BB Squeeze Breakout ca | 0 | — | — | NEW | 0 |
| S170 | Golden Pocket call 3 D | 0 | — | — | NEW | 0 |
| S171 | VWAP Reclaim call 3 DT | 0 | — | — | NEW | 0 |
| S172 | Trend Resumption call  | 0 | — | — | NEW | 0 |
| S173 | MomReversal long call | 415 | -31.51% | 37% | INSUFFICIENT | 57 |
| S174 | RubberBand long call E | 119 | -25.00% | 36% | INSUFFICIENT | 57 |
| S175 | Earnings Drift call 3  | 0 | — | — | NEW | 0 |
| S200 | GapDown_Aggressive | 0 | — | — | NEW | 0 |
| S201 | GapDown_Mild | 0 | — | — | NEW | 0 |
| S202 | GapDown_Monster | 10 | -60.53% | 0% | WATCH | 35 |
| S203 | GapUp_Fade | 40 | -55.91% | 10% | INSUFFICIENT | 36 |
| S204 | GapUp_Continuation | 0 | — | — | NEW | 0 |
| S205 | GapDown_HighVol | 0 | — | — | NEW | 0 |
| S206 | GapDown_WithTrend | 0 | — | — | NEW | 0 |
| S207 | GapDown_AtSupport | 37 | -47.06% | 5% | INSUFFICIENT | 36 |
| S208 | GapDown_AboveMA200 | 0 | — | — | NEW | 0 |
| S209 | GapDown_Recovery | 6 | -61.46% | 0% | WATCH | 34 |
| S210 | MA_Cross_8_21 | 68 | -5.30% | 49% | INSUFFICIENT | 36 |
| S211 | MA_Cross_21_50 | 41 | -31.58% | 29% | INSUFFICIENT | 36 |
| S212 | MA_Bounce_50 | 83 | -68.09% | 13% | INSUFFICIENT | 36 |
| S213 | MA_Bounce_200 | 0 | — | — | NEW | 0 |
| S214 | MA_Death_Cross | 0 | — | — | NEW | 0 |
| S215 | MA_Reclaim_200 | 0 | — | — | NEW | 0 |
| S216 | RSI_Oversold_Cross | 35 | -52.63% | 20% | INSUFFICIENT | 36 |
| S217 | RSI_25_Bounce | 40 | -48.08% | 35% | INSUFFICIENT | 36 |
| S218 | BB_Lower_Touch | 61 | +36.36% | 57% | INSUFFICIENT | 36 |
| S219 | Volume_Climax_Up | 0 | — | — | NEW | 0 |
| S220 | Pullback50 | 0 | — | — | NEW | 0 |
| S221 | GoldenPocket | 0 | — | — | NEW | 0 |
| S350 | GapDown_0DTE | 35 | +11.76% | 51% | INSUFFICIENT | 32 |
| S351 | GapDown_1DTE | 51 | -53.85% | 22% | INSUFFICIENT | 32 |
| S352 | GapDown_2DTE | 34 | -27.95% | 44% | INSUFFICIENT | 32 |
| S353 | GapDown_3DTE | 20 | -34.69% | 40% | INSUFFICIENT | 32 |
| S354 | GapDown_5DTE | 45 | -52.31% | 33% | INSUFFICIENT | 32 |
| S355 | GapDown_7DTE | 49 | -48.57% | 39% | INSUFFICIENT | 32 |
| S356 | GapDown_14DTE | 17 | -25.00% | 24% | INSUFFICIENT | 32 |
| S357 | GapDown_21DTE | 18 | +55.07% | 78% | INSUFFICIENT | 32 |
| S358 | GapDown_30DTE | 4 | +0.84% | 50% | WATCH | 28 |
| S359 | RubberBand_0DTE | 23 | -46.67% | 17% | INSUFFICIENT | 29 |
| S360 | RubberBand_1DTE | 49 | -56.41% | 10% | INSUFFICIENT | 32 |
| S361 | RubberBand_2DTE | 35 | -6.67% | 49% | INSUFFICIENT | 32 |
| S362 | RubberBand_3DTE | 35 | +25.45% | 69% | INSUFFICIENT | 32 |
| S363 | RubberBand_5DTE | 30 | -73.91% | 37% | INSUFFICIENT | 29 |
| S364 | RubberBand_7DTE | 43 | -42.31% | 44% | INSUFFICIENT | 32 |
| S365 | RubberBand_14DTE | 12 | -49.56% | 17% | WATCH | 32 |
| S366 | RubberBand_21DTE | 8 | -55.19% | 0% | WATCH | 28 |
| S367 | RubberBand_30DTE | 2 | -38.20% | 0% | WATCH | 28 |
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
| S396 | GapDown_ITM2 | 1 | -82.19% | 0% | WATCH | 26 |
| S397 | GapDown_ITM1 | 22 | +59.72% | 86% | INSUFFICIENT | 32 |
| S398 | GapDown_ATM | 42 | -4.05% | 50% | INSUFFICIENT | 32 |
| S399 | GapDown_OTM1 | 43 | -46.67% | 44% | INSUFFICIENT | 32 |
| S400 | Any_Green_Close | 6 | -50.00% | 17% | WATCH | 32 |
| S401 | Any_Gap_Down_Small | 92 | +3.47% | 50% | INSUFFICIENT | 32 |
| S402 | Any_High_Volume | 0 | — | — | NEW | 0 |
| S403 | Any_MA50_Touch | 32 | +49.12% | 53% | INSUFFICIENT | 32 |
| S404 | GapDown_OTM2 | 32 | +50.39% | 72% | INSUFFICIENT | 32 |
| S405 | GapDown_OTM3 | 56 | -42.86% | 34% | INSUFFICIENT | 32 |
| S406 | RubberBand_ITM3 | 61 | +63.64% | 66% | INSUFFICIENT | 32 |
| S407 | RubberBand_ITM2 | 38 | -47.73% | 29% | INSUFFICIENT | 32 |
| S408 | RubberBand_ITM1 | 43 | +0.00% | 47% | INSUFFICIENT | 29 |
| S409 | RubberBand_ATM | 0 | — | — | NEW | 0 |
| S410 | RubberBand_OTM1 | 4 | -58.46% | 25% | WATCH | 26 |
| S411 | RubberBand_OTM2 | 29 | +7.69% | 55% | INSUFFICIENT | 29 |
| S412 | RubberBand_OTM3 | 31 | -3.57% | 42% | INSUFFICIENT | 32 |
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
| S406 | 61 | +63.64% | 66% | Tyler review |
| S404 | 32 | +50.39% | 72% | Tyler review |
| S403 | 32 | +49.12% | 53% | Tyler review |
| S218 | 61 | +36.36% | 57% | Tyler review |
| S362 | 35 | +25.45% | 69% | Tyler review |
| S350 | 35 | +11.76% | 51% | Tyler review |
| S401 | 92 | +3.47% | 50% | Tyler review |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- **p25** sits between p10 and median for mid-tail visibility.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
- Active paper strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419.
