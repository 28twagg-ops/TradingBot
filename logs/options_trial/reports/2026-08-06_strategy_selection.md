# Options strategy selection report — 2026-08-06

_Generated 2026-08-06T19:30:54.863424_

## Summary

- Strategies analyzed: **105**
- Keep: **0**
- Watch: **91**
- Drop: **14**

## Attribution health

- Total exits: **1857**
- Orphan exits (b0/orphan_reconcile): **149**
- Orphan rate: **8.0%** (warn if >10%)
- Orphan rate OK (attribution looks healthy).

## Strategy scoreboard

| strategy | DTE | rec | exits | win% | med% | p10% | p25% | p90% | days live | ent 5d | exit 5d | realized $ | top share | rationale |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S354 (GapDown_5DTE) | 5d | watch | 27 | 51.9 | +93.62 | -70.80 | -64.16 | +155.91 | 6 | 30 | 13 | $+665.00 | 29.6% | fat left tail (p10 < -45%) |
| S364 (RubberBand_7DTE) | 7d | watch | 22 | 81.8 | +63.64 | -44.04 | +42.10 | +188.89 | 6 | 46 | 18 | $+547.00 | 54.5% | promising but needs larger sample |
| S406 (RubberBand_ITM3) | 3d | watch | 46 | 58.7 | +62.47 | -64.47 | -50.91 | +965.79 | 6 | 71 | 42 | $+2,746.00 | 28.3% | fat left tail (p10 < -45%) |
| S357 (GapDown_21DTE) | 21d | watch | 13 | 100.0 | +59.68 | +47.06 | +47.06 | +73.68 | 6 | 24 | 11 | $+472.00 | 53.8% | building sample (8-19 exits) |
| S350 (GapDown_0DTE) | 0d | watch | 28 | 64.3 | +57.34 | -61.37 | -28.26 | +212.00 | 6 | 48 | 22 | $+609.00 | 46.4% | fat left tail (p10 < -45%) |
| S362 (RubberBand_3DTE) | 3d | watch | 28 | 85.7 | +56.55 | -56.05 | +13.04 | +116.86 | 6 | 67 | 28 | $+1,274.00 | 42.9% | fat left tail (p10 < -45%) |
| S365 (RubberBand_14DTE) | 14d | watch | 1 | 100.0 | +54.84 | +54.84 | +54.84 | +54.84 | 6 | 24 | 1 | $+34.00 | 100.0% | insufficient sample (<8 exits) |
| S403 (Any_MA50_Touch) | 3d | watch | 12 | 58.3 | +53.79 | -76.32 | -58.52 | +319.60 | 6 | 20 | 12 | $+216.00 | 41.7% | building sample (8-19 exits) |
| S363 (RubberBand_5DTE) | 5d | watch | 11 | 100.0 | +52.94 | +7.14 | +9.52 | +103.23 | 3 | 36 | 11 | $+167.00 | 54.5% | building sample (8-19 exits) |
| S217 (RSI_25_Bounce) | 3d ATM RSI<25 bounce | watch | 26 | 53.8 | +52.45 | -59.41 | -53.95 | +221.81 | 10 | 46 | 25 | $+650.00 | 61.5% | fat left tail (p10 < -45%) |
| S397 (GapDown_ITM1) | 3d | watch | 11 | 81.8 | +51.39 | -91.67 | +39.48 | +116.39 | 6 | 39 | 2 | $+345.00 | 63.6% | building sample (8-19 exits) |
| S218 (BB_Lower_Touch) | 3d ATM BB lower touch | watch | 42 | 69.0 | +50.00 | -73.54 | -48.04 | +228.81 | 10 | 64 | 40 | $+927.00 | 35.7% | fat left tail (p10 < -45%) |
| S398 (GapDown_ATM) | 3d | watch | 31 | 64.5 | +50.00 | -54.29 | -21.41 | +157.78 | 6 | 50 | 17 | $+860.00 | 38.7% | fat left tail (p10 < -45%) |
| S352 (GapDown_2DTE) | 2d | watch | 18 | 61.1 | +50.00 | -59.02 | -51.39 | +154.26 | 6 | 50 | 11 | $+238.00 | 33.3% | building sample (8-19 exits) |
| S356 (GapDown_14DTE) | 14d | watch | 4 | 100.0 | +48.27 | +37.93 | +37.93 | +58.62 | 6 | 24 | 2 | $+112.00 | 100.0% | insufficient sample (<8 exits) |
| S408 (RubberBand_ITM1) | 3d | watch | 31 | 58.1 | +45.16 | -55.56 | -24.55 | +954.55 | 3 | 66 | 31 | $+1,320.00 | 32.3% | fat left tail (p10 < -45%) |
| S355 (GapDown_7DTE) | 7d | watch | 27 | 51.9 | +43.48 | -64.71 | -56.75 | +190.00 | 6 | 33 | 17 | $+546.00 | 40.7% | fat left tail (p10 < -45%) |
| S404 (GapDown_OTM2) | 3d | watch | 16 | 62.5 | +41.84 | -94.93 | -91.67 | +115.38 | 6 | 40 | 6 | $+167.00 | 50.0% | building sample (8-19 exits) |
| S401 (Any_Gap_Down_Small) | 3d | watch | 42 | 59.5 | +22.37 | -96.23 | -35.07 | +261.77 | 6 | 63 | 40 | $+797.00 | 28.6% | fat left tail (p10 < -45%) |
| S412 (RubberBand_OTM3) | 3d | watch | 22 | 50.0 | +15.91 | -47.62 | -11.86 | +91.86 | 6 | 59 | 22 | $+123.00 | 27.3% | fat left tail (p10 < -45%) |
| S210 (MA_Cross_8_21) | 3d ATM MA cross 8/21 | watch | 34 | 64.7 | +13.89 | -50.51 | -8.51 | +52.50 | 10 | 68 | 34 | $+40.00 | 44.1% | fat left tail (p10 < -45%) |
| S411 (RubberBand_OTM2) | 3d | watch | 21 | 61.9 | +10.45 | -53.73 | -48.61 | +45.00 | 3 | 61 | 21 | $-43.00 | 42.9% | fat left tail (p10 < -45%) |
| S361 (RubberBand_2DTE) | 2d | watch | 27 | 51.9 | +1.85 | -75.89 | -54.44 | +138.92 | 6 | 63 | 27 | $-7.00 | 40.7% | fat left tail (p10 < -45%) |
| S163 (A1 GapDown ATM call EOD) | 7d ATM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 16 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | 3d ATM strong | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 16 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S167 (GapDown long call 3 DTE 1-OTM — P2C) | 3d 1-OTM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 16 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S168 (GapDown ATM 5-DTE — P2B arm) | 5d ATM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 16 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
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
| S358 (GapDown_30DTE) | 30d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 2 | 8 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S366 (RubberBand_21DTE) | 21d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 2 | 30 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S367 (RubberBand_30DTE) | 30d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 2 | 8 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
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
| S396 (GapDown_ITM2) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 0 | 2 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S402 (Any_High_Volume) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S409 (RubberBand_ATM) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S410 (RubberBand_OTM1) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 0 | 7 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S413 (BBSqueeze_ITM3) | 0d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S414 (BBSqueeze_ITM2) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S415 (BBSqueeze_ITM1) | 7d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S416 (BBSqueeze_ATM) | 0d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S417 (BBSqueeze_OTM1) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S418 (BBSqueeze_OTM2) | 7d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S419 (BBSqueeze_OTM3) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S353 (GapDown_3DTE) | 3d | watch | 18 | 33.3 | -42.73 | -87.47 | -78.01 | +104.69 | 6 | 38 | 14 | $-164.00 | 50.0% | early sample with non-positive median |
| S400 (Any_Green_Close) | 3d | watch | 5 | 0.0 | -50.00 | -66.67 | -66.67 | -33.33 | 6 | 0 | 0 | $-30.00 | 100.0% | insufficient sample (<8 exits) |
| S209 (GapDown_Recovery) | 3d ATM gap-recovery | watch | 3 | 0.0 | -58.21 | -63.41 | -61.46 | -52.24 | 8 | 10 | 3 | $-84.00 | 66.7% | insufficient sample (<8 exits) |
| S202 (GapDown_Monster) | 3d ATM gap-monster | watch | 6 | 0.0 | -64.75 | -70.52 | -66.39 | -44.87 | 9 | 0 | 2 | $-133.00 | 66.7% | insufficient sample (<8 exits) |
| S164 (GapDown ATM 1-DTE — P2B arm) | 1d ATM | watch | 6 | 0.0 | -65.67 | -88.89 | -86.11 | -50.00 | 16 | 0 | 0 | $-59.00 | 83.3% | insufficient sample (<8 exits) |
| S405 (GapDown_OTM3) | 3d | drop | 36 | 50.0 | -8.80 | -57.52 | -43.35 | +114.58 | 6 | 53 | 22 | $+392.00 | 33.3% | non-positive median return |
| S399 (GapDown_OTM1) | 3d | drop | 37 | 48.6 | -17.24 | -70.71 | -66.67 | +144.00 | 6 | 77 | 25 | $+179.00 | 43.2% | non-positive median return |
| S211 (MA_Cross_21_50) | 3d ATM MA cross 21/50 | drop | 20 | 20.0 | -24.36 | -61.35 | -46.79 | +109.42 | 10 | 64 | 20 | $-127.00 | 70.0% | non-positive median return |
| S174 (RubberBand long call EOD) | RubberBand (dropped) | drop | 119 | 36.1 | -25.00 | -89.83 | -71.19 | +36.67 | 31 | 0 | 0 | $-1,658.19 | 50.4% | manually paused — excluded from new entries & reflected P&L |
| S173 (MomReversal long call) | MomRev | drop | 415 | 37.1 | -31.51 | -77.18 | -62.95 | +101.90 | 31 | 0 | 0 | $+62.64 | 27.5% | manually paused — excluded from new entries & reflected P&L |
| S165 (GapDown long call 3 DTE) | 3d ATM | drop | 245 | 29.8 | -38.18 | -63.39 | -54.55 | +81.82 | 31 | 0 | 0 | $-1,828.78 | 26.1% | non-positive median return |
| S359 (RubberBand_0DTE) | 0d | drop | 23 | 17.4 | -46.67 | -71.43 | -70.37 | +61.82 | 3 | 44 | 23 | $-323.00 | 43.5% | non-positive median return |
| S207 (GapDown_AtSupport) | 3d ATM gap-support | drop | 37 | 5.4 | -47.06 | -63.64 | -55.71 | -6.06 | 10 | 50 | 37 | $-822.00 | 43.2% | non-positive median return |
| S407 (RubberBand_ITM2) | 3d | drop | 27 | 40.7 | -51.43 | -90.26 | -61.54 | +381.23 | 6 | 58 | 23 | $+184.00 | 33.3% | non-positive median return |
| S351 (GapDown_1DTE) | 1d | drop | 36 | 27.8 | -51.76 | -83.68 | -64.44 | +171.88 | 6 | 80 | 25 | $+42.00 | 36.1% | non-positive median return |
| S203 (GapUp_Fade) | 3d ATM gap-up fade (put) | drop | 29 | 13.8 | -53.33 | -79.25 | -66.10 | +53.62 | 10 | 47 | 25 | $-625.00 | 48.3% | non-positive median return |
| S360 (RubberBand_1DTE) | 1d | drop | 31 | 9.7 | -54.76 | -81.58 | -70.76 | -33.33 | 6 | 57 | 27 | $-525.00 | 35.5% | non-positive median return |
| S216 (RSI_Oversold_Cross) | 3d ATM RSI x30 | drop | 22 | 0.0 | -57.12 | -86.44 | -79.32 | -36.96 | 10 | 44 | 22 | $-693.00 | 63.6% | non-positive median return |
| S212 (MA_Bounce_50) | 3d ATM MA bounce 50 | drop | 53 | 3.8 | -71.43 | -98.51 | -97.96 | -46.55 | 10 | 61 | 53 | $-2,084.00 | 41.5% | non-positive median return |

## Comparison groups

Experiment arms grouped for side-by-side decisions. INSUFFICIENT if any arm has n<10 exits.

### GapDown DTE comparison

- Status: **INSUFFICIENT** | Best median: **S163** (+0.00%) | Best p10: **S163** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S163 | 7d ATM | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S164 | 1d ATM | 6 | -65.67 | -88.89 | -86.11 | 0 | 0 |
| S165 | 3d ATM | 245 | -38.18 | -63.39 | -54.55 | 0 | 0 |
| S168 | 5d ATM | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### GapDown Strike comparison

- Status: **INSUFFICIENT** | Best median: **S167** (+0.00%) | Best p10: **S167** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S165 | 3d ATM | 245 | -38.18 | -63.39 | -54.55 | 0 | 0 |
| S167 | 3d 1-OTM | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

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
| S202 | 3d ATM gap-monster | 6 | -64.75 | -70.52 | -66.39 | 0 | 2 |
| S204 | 3d ATM gap-up cont | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S205 | 3d ATM gap-highvol | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S206 | 3d ATM gap-trend | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S207 | 3d ATM gap-support | 37 | -47.06 | -63.64 | -55.71 | 50 | 37 |
| S208 | 3d ATM gap-ma200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S209 | 3d ATM gap-recovery | 3 | -58.21 | -63.41 | -61.46 | 10 | 3 |

### Phase-1 Bearish Gap & MA

- Status: **INSUFFICIENT** | Best median: **S214** (+0.00%) | Best p10: **S214** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S203 | 3d ATM gap-up fade (put) | 29 | -53.33 | -79.25 | -66.10 | 47 | 25 |
| S214 | 3d ATM death cross (put) | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 MA family

- Status: **INSUFFICIENT** | Best median: **S210** (+13.89%) | Best p10: **S213** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S210 | 3d ATM MA cross 8/21 | 34 | +13.89 | -50.51 | -8.51 | 68 | 34 |
| S211 | 3d ATM MA cross 21/50 | 20 | -24.36 | -61.35 | -46.79 | 64 | 20 |
| S212 | 3d ATM MA bounce 50 | 53 | -71.43 | -98.51 | -97.96 | 61 | 53 |
| S213 | 3d ATM MA bounce 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S215 | 3d ATM MA reclaim 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 RSI/BB/Vol

- Status: **INSUFFICIENT** | Best median: **S217** (+52.45%) | Best p10: **S219** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S216 | 3d ATM RSI x30 | 22 | -57.12 | -86.44 | -79.32 | 44 | 22 |
| S217 | 3d ATM RSI<25 bounce | 26 | +52.45 | -59.41 | -53.95 | 46 | 25 |
| S218 | 3d ATM BB lower touch | 42 | +50.00 | -73.54 | -48.04 | 64 | 40 |
| S219 | 3d ATM vol climax up | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Other

- Status: **OK** | Best median: **S173** (-31.51%) | Best p10: **S173** (-77.18%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S173 | MomRev | 415 | -31.51 | -77.18 | -62.95 | 0 | 0 |

## Strategy Pipeline Status

_Pipeline evaluation as of 2026-08-06. Auto-kill thresholds: median<-25% at n>=15, p10<-85%, WR<15% at n>=25. Promote: n>=30 median>0%._

| Strategy | Signal | n | Median% | WR% | Status | Days |
|----------|--------|---|---------|-----|--------|------|
| S163 | A1 GapDown ATM call EO | 0 | — | — | NEW | 16 |
| S164 | GapDown ATM 1-DTE — P2 | 6 | -65.67% | 0% | WATCH | 16 |
| S165 | GapDown long call 3 DT | 245 | -38.18% | 30% | INSUFFICIENT | 31 |
| S166 | GapDown strong call | 0 | — | — | NEW | 16 |
| S167 | GapDown long call 3 DT | 0 | — | — | NEW | 16 |
| S168 | GapDown ATM 5-DTE — P2 | 0 | — | — | NEW | 16 |
| S169 | BB Squeeze Breakout ca | 0 | — | — | NEW | 0 |
| S170 | Golden Pocket call 3 D | 0 | — | — | NEW | 0 |
| S171 | VWAP Reclaim call 3 DT | 0 | — | — | NEW | 0 |
| S172 | Trend Resumption call  | 0 | — | — | NEW | 0 |
| S173 | MomReversal long call | 415 | -31.51% | 37% | INSUFFICIENT | 31 |
| S174 | RubberBand long call E | 119 | -25.00% | 36% | INSUFFICIENT | 31 |
| S175 | Earnings Drift call 3  | 0 | — | — | NEW | 0 |
| S200 | GapDown_Aggressive | 0 | — | — | NEW | 0 |
| S201 | GapDown_Mild | 0 | — | — | NEW | 0 |
| S202 | GapDown_Monster | 6 | -64.75% | 0% | WATCH | 9 |
| S203 | GapUp_Fade | 29 | -53.33% | 14% | INSUFFICIENT | 10 |
| S204 | GapUp_Continuation | 0 | — | — | NEW | 0 |
| S205 | GapDown_HighVol | 0 | — | — | NEW | 0 |
| S206 | GapDown_WithTrend | 0 | — | — | NEW | 0 |
| S207 | GapDown_AtSupport | 37 | -47.06% | 5% | INSUFFICIENT | 10 |
| S208 | GapDown_AboveMA200 | 0 | — | — | NEW | 0 |
| S209 | GapDown_Recovery | 3 | -58.21% | 0% | WATCH | 8 |
| S210 | MA_Cross_8_21 | 34 | +13.89% | 65% | INSUFFICIENT | 10 |
| S211 | MA_Cross_21_50 | 20 | -24.36% | 20% | INSUFFICIENT | 10 |
| S212 | MA_Bounce_50 | 53 | -71.43% | 4% | INSUFFICIENT | 10 |
| S213 | MA_Bounce_200 | 0 | — | — | NEW | 0 |
| S214 | MA_Death_Cross | 0 | — | — | NEW | 0 |
| S215 | MA_Reclaim_200 | 0 | — | — | NEW | 0 |
| S216 | RSI_Oversold_Cross | 22 | -57.12% | 0% | INSUFFICIENT | 10 |
| S217 | RSI_25_Bounce | 26 | +52.45% | 54% | INSUFFICIENT | 10 |
| S218 | BB_Lower_Touch | 42 | +50.00% | 69% | INSUFFICIENT | 10 |
| S219 | Volume_Climax_Up | 0 | — | — | NEW | 0 |
| S220 | Pullback50 | 0 | — | — | NEW | 0 |
| S221 | GoldenPocket | 0 | — | — | NEW | 0 |
| S350 | GapDown_0DTE | 28 | +57.34% | 64% | INSUFFICIENT | 6 |
| S351 | GapDown_1DTE | 36 | -51.76% | 28% | INSUFFICIENT | 6 |
| S352 | GapDown_2DTE | 18 | +50.00% | 61% | INSUFFICIENT | 6 |
| S353 | GapDown_3DTE | 18 | -42.73% | 33% | INSUFFICIENT | 6 |
| S354 | GapDown_5DTE | 27 | +93.62% | 52% | INSUFFICIENT | 6 |
| S355 | GapDown_7DTE | 27 | +43.48% | 52% | INSUFFICIENT | 6 |
| S356 | GapDown_14DTE | 4 | +48.27% | 100% | WATCH | 6 |
| S357 | GapDown_21DTE | 13 | +59.68% | 100% | WATCH | 6 |
| S358 | GapDown_30DTE | 0 | — | — | NEW | 2 |
| S359 | RubberBand_0DTE | 23 | -46.67% | 17% | INSUFFICIENT | 3 |
| S360 | RubberBand_1DTE | 31 | -54.76% | 10% | INSUFFICIENT | 6 |
| S361 | RubberBand_2DTE | 27 | +1.85% | 52% | INSUFFICIENT | 6 |
| S362 | RubberBand_3DTE | 28 | +56.55% | 86% | INSUFFICIENT | 6 |
| S363 | RubberBand_5DTE | 11 | +52.94% | 100% | WATCH | 3 |
| S364 | RubberBand_7DTE | 22 | +63.64% | 82% | INSUFFICIENT | 6 |
| S365 | RubberBand_14DTE | 1 | +54.84% | 100% | WATCH | 6 |
| S366 | RubberBand_21DTE | 0 | — | — | NEW | 2 |
| S367 | RubberBand_30DTE | 0 | — | — | NEW | 2 |
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
| S396 | GapDown_ITM2 | 0 | — | — | NEW | 0 |
| S397 | GapDown_ITM1 | 11 | +51.39% | 82% | WATCH | 6 |
| S398 | GapDown_ATM | 31 | +50.00% | 65% | INSUFFICIENT | 6 |
| S399 | GapDown_OTM1 | 37 | -17.24% | 49% | INSUFFICIENT | 6 |
| S400 | Any_Green_Close | 5 | -50.00% | 0% | WATCH | 6 |
| S401 | Any_Gap_Down_Small | 42 | +22.37% | 60% | INSUFFICIENT | 6 |
| S402 | Any_High_Volume | 0 | — | — | NEW | 0 |
| S403 | Any_MA50_Touch | 12 | +53.79% | 58% | WATCH | 6 |
| S404 | GapDown_OTM2 | 16 | +41.84% | 62% | INSUFFICIENT | 6 |
| S405 | GapDown_OTM3 | 36 | -8.80% | 50% | INSUFFICIENT | 6 |
| S406 | RubberBand_ITM3 | 46 | +62.47% | 59% | INSUFFICIENT | 6 |
| S407 | RubberBand_ITM2 | 27 | -51.43% | 41% | INSUFFICIENT | 6 |
| S408 | RubberBand_ITM1 | 31 | +45.16% | 58% | INSUFFICIENT | 3 |
| S409 | RubberBand_ATM | 0 | — | — | NEW | 0 |
| S410 | RubberBand_OTM1 | 0 | — | — | NEW | 0 |
| S411 | RubberBand_OTM2 | 21 | +10.45% | 62% | INSUFFICIENT | 3 |
| S412 | RubberBand_OTM3 | 22 | +15.91% | 50% | INSUFFICIENT | 6 |
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
| S406 | 46 | +62.47% | 59% | Tyler review |
| S218 | 42 | +50.00% | 69% | Tyler review |
| S398 | 31 | +50.00% | 65% | Tyler review |
| S408 | 31 | +45.16% | 58% | Tyler review |
| S401 | 42 | +22.37% | 60% | Tyler review |
| S210 | 34 | +13.89% | 65% | Tyler review |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- **p25** sits between p10 and median for mid-tail visibility.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
- Active paper strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419.
