# Options strategy selection report — 2026-08-07

_Generated 2026-08-07T16:06:00.933811_

## Summary

- Strategies analyzed: **105**
- Keep: **0**
- Watch: **86**
- Drop: **19**

## Attribution health

- Total exits: **2014**
- Orphan exits (b0/orphan_reconcile): **192**
- Orphan rate: **9.5%** (warn if >10%)
- Orphan rate OK (attribution looks healthy).

## Strategy scoreboard

| strategy | DTE | rec | exits | win% | med% | p10% | p25% | p90% | days live | ent 5d | exit 5d | realized $ | top share | rationale |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S406 (RubberBand_ITM3) | 3d | watch | 46 | 58.7 | +62.47 | -64.47 | -50.91 | +965.79 | 7 | 83 | 42 | $+2,746.00 | 28.3% | fat left tail (p10 < -45%) |
| S364 (RubberBand_7DTE) | 7d | watch | 25 | 72.0 | +60.00 | -47.69 | -42.31 | +188.89 | 7 | 55 | 21 | $+461.00 | 48.0% | fat left tail (p10 < -45%) |
| S357 (GapDown_21DTE) | 21d | watch | 16 | 87.5 | +58.87 | -17.77 | +47.06 | +73.68 | 7 | 28 | 14 | $+400.00 | 50.0% | building sample (8-19 exits) |
| S350 (GapDown_0DTE) | 0d | watch | 28 | 64.3 | +57.34 | -61.37 | -28.26 | +212.00 | 7 | 51 | 22 | $+609.00 | 46.4% | fat left tail (p10 < -45%) |
| S362 (RubberBand_3DTE) | 3d | watch | 29 | 82.8 | +52.63 | -55.79 | +13.04 | +116.00 | 7 | 67 | 29 | $+1,237.00 | 44.8% | fat left tail (p10 < -45%) |
| S397 (GapDown_ITM1) | 3d | watch | 11 | 81.8 | +51.39 | -91.67 | +39.48 | +116.39 | 7 | 40 | 2 | $+345.00 | 63.6% | building sample (8-19 exits) |
| S218 (BB_Lower_Touch) | 3d ATM BB lower touch | watch | 48 | 66.7 | +50.00 | -73.77 | -53.45 | +187.38 | 11 | 78 | 46 | $+961.00 | 43.8% | fat left tail (p10 < -45%) |
| S403 (Any_MA50_Touch) | 3d | watch | 18 | 55.6 | +49.56 | -80.36 | -63.57 | +317.20 | 7 | 28 | 18 | $+199.00 | 33.3% | building sample (8-19 exits) |
| S398 (GapDown_ATM) | 3d | watch | 34 | 58.8 | +48.98 | -57.24 | -39.29 | +157.11 | 7 | 59 | 20 | $+799.00 | 44.1% | fat left tail (p10 < -45%) |
| S408 (RubberBand_ITM1) | 3d | watch | 36 | 55.6 | +43.55 | -64.09 | -50.00 | +880.61 | 4 | 74 | 36 | $+1,282.00 | 27.8% | fat left tail (p10 < -45%) |
| S352 (GapDown_2DTE) | 2d | watch | 22 | 59.1 | +39.01 | -64.86 | -51.85 | +134.17 | 7 | 58 | 15 | $+221.00 | 27.3% | fat left tail (p10 < -45%) |
| S404 (GapDown_OTM2) | 3d | watch | 17 | 58.8 | +38.60 | -98.18 | -91.67 | +113.61 | 7 | 40 | 7 | $+113.00 | 52.9% | building sample (8-19 exits) |
| S356 (GapDown_14DTE) | 14d | watch | 6 | 66.7 | +37.93 | -48.15 | -25.24 | +58.62 | 7 | 24 | 4 | $+60.00 | 100.0% | insufficient sample (<8 exits) |
| S401 (Any_Gap_Down_Small) | 3d | watch | 52 | 59.6 | +26.95 | -92.80 | -31.46 | +160.00 | 7 | 81 | 50 | $+970.00 | 32.7% | fat left tail (p10 < -45%) |
| S210 (MA_Cross_8_21) | 3d ATM MA cross 8/21 | watch | 43 | 60.5 | +13.89 | -56.39 | -25.31 | +74.04 | 11 | 80 | 43 | $+54.00 | 34.9% | fat left tail (p10 < -45%) |
| S363 (RubberBand_5DTE) | 5d | watch | 15 | 73.3 | +9.52 | -71.46 | -23.36 | +87.65 | 4 | 42 | 15 | $+30.00 | 40.0% | building sample (8-19 exits) |
| S411 (RubberBand_OTM2) | 3d | watch | 24 | 54.2 | +6.57 | -57.76 | -52.08 | +43.00 | 4 | 66 | 24 | $-156.00 | 37.5% | fat left tail (p10 < -45%) |
| S163 (A1 GapDown ATM call EOD) | 7d ATM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 17 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | 3d ATM strong | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 17 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S167 (GapDown long call 3 DTE 1-OTM — P2C) | 3d 1-OTM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 17 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S168 (GapDown ATM 5-DTE — P2B arm) | 5d ATM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 17 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
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
| S358 (GapDown_30DTE) | 30d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 3 | 8 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S366 (RubberBand_21DTE) | 21d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 3 | 30 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
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
| S367 (RubberBand_30DTE) | 30d | watch | 1 | 0.0 | -25.00 | -25.00 | -25.00 | -25.00 | 3 | 8 | 1 | $-18.00 | 100.0% | insufficient sample (<8 exits) |
| S353 (GapDown_3DTE) | 3d | watch | 18 | 33.3 | -42.73 | -87.47 | -78.01 | +104.69 | 7 | 40 | 14 | $-164.00 | 50.0% | early sample with non-positive median |
| S400 (Any_Green_Close) | 3d | watch | 5 | 0.0 | -50.00 | -66.67 | -66.67 | -33.33 | 7 | 0 | 0 | $-30.00 | 100.0% | insufficient sample (<8 exits) |
| S365 (RubberBand_14DTE) | 14d | watch | 6 | 33.3 | -57.47 | -83.58 | -78.52 | +137.42 | 7 | 26 | 6 | $-63.00 | 33.3% | insufficient sample (<8 exits) |
| S209 (GapDown_Recovery) | 3d ATM gap-recovery | watch | 6 | 0.0 | -61.46 | -82.78 | -69.36 | -50.75 | 9 | 18 | 6 | $-210.00 | 83.3% | insufficient sample (<8 exits) |
| S202 (GapDown_Monster) | 3d ATM gap-monster | watch | 6 | 0.0 | -64.75 | -70.52 | -66.39 | -44.87 | 10 | 0 | 2 | $-133.00 | 66.7% | insufficient sample (<8 exits) |
| S164 (GapDown ATM 1-DTE — P2B arm) | 1d ATM | watch | 6 | 0.0 | -65.67 | -88.89 | -86.11 | -50.00 | 17 | 0 | 0 | $-59.00 | 83.3% | insufficient sample (<8 exits) |
| S410 (RubberBand_OTM1) | 3d | watch | 3 | 33.3 | -68.49 | -76.16 | -73.28 | +67.49 | 1 | 12 | 3 | $-39.00 | 66.7% | insufficient sample (<8 exits) |
| S396 (GapDown_ITM2) | 3d | watch | 1 | 0.0 | -82.19 | -82.19 | -82.19 | -82.19 | 1 | 4 | 1 | $-60.00 | 100.0% | insufficient sample (<8 exits) |
| S355 (GapDown_7DTE) | 7d | drop | 30 | 50.0 | -1.23 | -66.67 | -58.54 | +188.13 | 7 | 43 | 20 | $+504.00 | 36.7% | non-positive median return |
| S361 (RubberBand_2DTE) | 2d | drop | 28 | 50.0 | -2.41 | -74.83 | -56.45 | +132.08 | 7 | 68 | 28 | $-44.00 | 39.3% | non-positive median return |
| S412 (RubberBand_OTM3) | 3d | drop | 24 | 45.8 | -2.90 | -47.62 | -11.86 | +90.40 | 7 | 65 | 24 | $+121.00 | 25.0% | non-positive median return |
| S217 (RSI_25_Bounce) | 3d ATM RSI<25 bounce | drop | 29 | 48.3 | -10.00 | -61.75 | -55.00 | +212.73 | 11 | 50 | 28 | $+593.00 | 65.5% | non-positive median return |
| S399 (GapDown_OTM1) | 3d | drop | 37 | 48.6 | -17.24 | -70.71 | -66.67 | +144.00 | 7 | 84 | 25 | $+179.00 | 43.2% | non-positive median return |
| S405 (GapDown_OTM3) | 3d | drop | 39 | 46.2 | -21.05 | -58.92 | -47.41 | +110.00 | 7 | 61 | 25 | $+324.00 | 38.5% | non-positive median return |
| S174 (RubberBand long call EOD) | RubberBand (dropped) | drop | 119 | 36.1 | -25.00 | -89.83 | -71.19 | +36.67 | 32 | 0 | 0 | $-1,658.19 | 50.4% | manually paused — excluded from new entries & reflected P&L |
| S173 (MomReversal long call) | MomRev | drop | 415 | 37.1 | -31.51 | -77.18 | -62.95 | +101.90 | 32 | 0 | 0 | $+62.64 | 27.5% | manually paused — excluded from new entries & reflected P&L |
| S211 (MA_Cross_21_50) | 3d ATM MA cross 21/50 | drop | 21 | 19.0 | -31.58 | -97.22 | -48.72 | +107.69 | 11 | 64 | 21 | $-162.00 | 71.4% | non-positive median return |
| S354 (GapDown_5DTE) | 5d | drop | 29 | 48.3 | -33.33 | -73.68 | -66.67 | +149.54 | 7 | 36 | 15 | $+592.00 | 31.0% | non-positive median return |
| S165 (GapDown long call 3 DTE) | 3d ATM | drop | 245 | 29.8 | -38.18 | -63.39 | -54.55 | +81.82 | 32 | 0 | 0 | $-1,828.78 | 26.1% | non-positive median return |
| S359 (RubberBand_0DTE) | 0d | drop | 23 | 17.4 | -46.67 | -71.43 | -70.37 | +61.82 | 4 | 48 | 23 | $-323.00 | 43.5% | non-positive median return |
| S207 (GapDown_AtSupport) | 3d ATM gap-support | drop | 37 | 5.4 | -47.06 | -63.64 | -55.71 | -6.06 | 11 | 50 | 37 | $-822.00 | 43.2% | non-positive median return |
| S351 (GapDown_1DTE) | 1d | drop | 38 | 26.3 | -52.55 | -80.48 | -66.52 | +171.88 | 7 | 90 | 27 | $+7.00 | 34.2% | non-positive median return |
| S203 (GapUp_Fade) | 3d ATM gap-up fade (put) | drop | 33 | 12.1 | -54.00 | -79.08 | -74.42 | +38.86 | 11 | 55 | 29 | $-717.00 | 42.4% | non-positive median return |
| S407 (RubberBand_ITM2) | 3d | drop | 29 | 37.9 | -54.05 | -88.38 | -61.54 | +367.28 | 7 | 62 | 25 | $+161.00 | 31.0% | non-positive median return |
| S360 (RubberBand_1DTE) | 1d | drop | 34 | 8.8 | -55.16 | -81.64 | -70.96 | -33.33 | 7 | 64 | 30 | $-612.00 | 32.4% | non-positive median return |
| S216 (RSI_Oversold_Cross) | 3d ATM RSI x30 | drop | 30 | 10.0 | -56.25 | -87.23 | -75.81 | -27.09 | 11 | 62 | 30 | $-733.00 | 53.3% | non-positive median return |
| S212 (MA_Bounce_50) | 3d ATM MA bounce 50 | drop | 60 | 5.0 | -71.01 | -98.42 | -97.89 | -46.36 | 11 | 79 | 60 | $-2,176.00 | 40.0% | non-positive median return |

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
| S209 | 3d ATM gap-recovery | 6 | -61.46 | -82.78 | -69.36 | 18 | 6 |

### Phase-1 Bearish Gap & MA

- Status: **INSUFFICIENT** | Best median: **S214** (+0.00%) | Best p10: **S214** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S203 | 3d ATM gap-up fade (put) | 33 | -54.00 | -79.08 | -74.42 | 55 | 29 |
| S214 | 3d ATM death cross (put) | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 MA family

- Status: **INSUFFICIENT** | Best median: **S210** (+13.89%) | Best p10: **S213** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S210 | 3d ATM MA cross 8/21 | 43 | +13.89 | -56.39 | -25.31 | 80 | 43 |
| S211 | 3d ATM MA cross 21/50 | 21 | -31.58 | -97.22 | -48.72 | 64 | 21 |
| S212 | 3d ATM MA bounce 50 | 60 | -71.01 | -98.42 | -97.89 | 79 | 60 |
| S213 | 3d ATM MA bounce 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S215 | 3d ATM MA reclaim 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 RSI/BB/Vol

- Status: **INSUFFICIENT** | Best median: **S218** (+50.00%) | Best p10: **S219** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S216 | 3d ATM RSI x30 | 30 | -56.25 | -87.23 | -75.81 | 62 | 30 |
| S217 | 3d ATM RSI<25 bounce | 29 | -10.00 | -61.75 | -55.00 | 50 | 28 |
| S218 | 3d ATM BB lower touch | 48 | +50.00 | -73.77 | -53.45 | 78 | 46 |
| S219 | 3d ATM vol climax up | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Other

- Status: **OK** | Best median: **S173** (-31.51%) | Best p10: **S173** (-77.18%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S173 | MomRev | 415 | -31.51 | -77.18 | -62.95 | 0 | 0 |

## Strategy Pipeline Status

_Pipeline evaluation as of 2026-08-07. Auto-kill thresholds: median<-25% at n>=15, p10<-85%, WR<15% at n>=25. Promote: n>=30 median>0%._

| Strategy | Signal | n | Median% | WR% | Status | Days |
|----------|--------|---|---------|-----|--------|------|
| S163 | A1 GapDown ATM call EO | 0 | — | — | NEW | 17 |
| S164 | GapDown ATM 1-DTE — P2 | 6 | -65.67% | 0% | WATCH | 17 |
| S165 | GapDown long call 3 DT | 245 | -38.18% | 30% | INSUFFICIENT | 32 |
| S166 | GapDown strong call | 0 | — | — | NEW | 17 |
| S167 | GapDown long call 3 DT | 0 | — | — | NEW | 17 |
| S168 | GapDown ATM 5-DTE — P2 | 0 | — | — | NEW | 17 |
| S169 | BB Squeeze Breakout ca | 0 | — | — | NEW | 0 |
| S170 | Golden Pocket call 3 D | 0 | — | — | NEW | 0 |
| S171 | VWAP Reclaim call 3 DT | 0 | — | — | NEW | 0 |
| S172 | Trend Resumption call  | 0 | — | — | NEW | 0 |
| S173 | MomReversal long call | 415 | -31.51% | 37% | INSUFFICIENT | 32 |
| S174 | RubberBand long call E | 119 | -25.00% | 36% | INSUFFICIENT | 32 |
| S175 | Earnings Drift call 3  | 0 | — | — | NEW | 0 |
| S200 | GapDown_Aggressive | 0 | — | — | NEW | 0 |
| S201 | GapDown_Mild | 0 | — | — | NEW | 0 |
| S202 | GapDown_Monster | 6 | -64.75% | 0% | WATCH | 10 |
| S203 | GapUp_Fade | 33 | -54.00% | 12% | INSUFFICIENT | 11 |
| S204 | GapUp_Continuation | 0 | — | — | NEW | 0 |
| S205 | GapDown_HighVol | 0 | — | — | NEW | 0 |
| S206 | GapDown_WithTrend | 0 | — | — | NEW | 0 |
| S207 | GapDown_AtSupport | 37 | -47.06% | 5% | INSUFFICIENT | 11 |
| S208 | GapDown_AboveMA200 | 0 | — | — | NEW | 0 |
| S209 | GapDown_Recovery | 6 | -61.46% | 0% | WATCH | 9 |
| S210 | MA_Cross_8_21 | 43 | +13.89% | 60% | INSUFFICIENT | 11 |
| S211 | MA_Cross_21_50 | 21 | -31.58% | 19% | INSUFFICIENT | 11 |
| S212 | MA_Bounce_50 | 60 | -71.01% | 5% | INSUFFICIENT | 11 |
| S213 | MA_Bounce_200 | 0 | — | — | NEW | 0 |
| S214 | MA_Death_Cross | 0 | — | — | NEW | 0 |
| S215 | MA_Reclaim_200 | 0 | — | — | NEW | 0 |
| S216 | RSI_Oversold_Cross | 30 | -56.25% | 10% | INSUFFICIENT | 11 |
| S217 | RSI_25_Bounce | 29 | -10.00% | 48% | INSUFFICIENT | 11 |
| S218 | BB_Lower_Touch | 48 | +50.00% | 67% | INSUFFICIENT | 11 |
| S219 | Volume_Climax_Up | 0 | — | — | NEW | 0 |
| S220 | Pullback50 | 0 | — | — | NEW | 0 |
| S221 | GoldenPocket | 0 | — | — | NEW | 0 |
| S350 | GapDown_0DTE | 28 | +57.34% | 64% | INSUFFICIENT | 7 |
| S351 | GapDown_1DTE | 38 | -52.55% | 26% | INSUFFICIENT | 7 |
| S352 | GapDown_2DTE | 22 | +39.01% | 59% | INSUFFICIENT | 7 |
| S353 | GapDown_3DTE | 18 | -42.73% | 33% | INSUFFICIENT | 7 |
| S354 | GapDown_5DTE | 29 | -33.33% | 48% | INSUFFICIENT | 7 |
| S355 | GapDown_7DTE | 30 | -1.23% | 50% | INSUFFICIENT | 7 |
| S356 | GapDown_14DTE | 6 | +37.93% | 67% | WATCH | 7 |
| S357 | GapDown_21DTE | 16 | +58.87% | 88% | INSUFFICIENT | 7 |
| S358 | GapDown_30DTE | 0 | — | — | NEW | 3 |
| S359 | RubberBand_0DTE | 23 | -46.67% | 17% | INSUFFICIENT | 4 |
| S360 | RubberBand_1DTE | 34 | -55.16% | 9% | INSUFFICIENT | 7 |
| S361 | RubberBand_2DTE | 28 | -2.41% | 50% | INSUFFICIENT | 7 |
| S362 | RubberBand_3DTE | 29 | +52.63% | 83% | INSUFFICIENT | 7 |
| S363 | RubberBand_5DTE | 15 | +9.52% | 73% | INSUFFICIENT | 4 |
| S364 | RubberBand_7DTE | 25 | +60.00% | 72% | INSUFFICIENT | 7 |
| S365 | RubberBand_14DTE | 6 | -57.47% | 33% | WATCH | 7 |
| S366 | RubberBand_21DTE | 0 | — | — | NEW | 3 |
| S367 | RubberBand_30DTE | 1 | -25.00% | 0% | WATCH | 3 |
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
| S396 | GapDown_ITM2 | 1 | -82.19% | 0% | WATCH | 1 |
| S397 | GapDown_ITM1 | 11 | +51.39% | 82% | WATCH | 7 |
| S398 | GapDown_ATM | 34 | +48.98% | 59% | INSUFFICIENT | 7 |
| S399 | GapDown_OTM1 | 37 | -17.24% | 49% | INSUFFICIENT | 7 |
| S400 | Any_Green_Close | 5 | -50.00% | 0% | WATCH | 7 |
| S401 | Any_Gap_Down_Small | 52 | +26.95% | 60% | INSUFFICIENT | 7 |
| S402 | Any_High_Volume | 0 | — | — | NEW | 0 |
| S403 | Any_MA50_Touch | 18 | +49.56% | 56% | INSUFFICIENT | 7 |
| S404 | GapDown_OTM2 | 17 | +38.60% | 59% | INSUFFICIENT | 7 |
| S405 | GapDown_OTM3 | 39 | -21.05% | 46% | INSUFFICIENT | 7 |
| S406 | RubberBand_ITM3 | 46 | +62.47% | 59% | INSUFFICIENT | 7 |
| S407 | RubberBand_ITM2 | 29 | -54.05% | 38% | INSUFFICIENT | 7 |
| S408 | RubberBand_ITM1 | 36 | +43.55% | 56% | INSUFFICIENT | 4 |
| S409 | RubberBand_ATM | 0 | — | — | NEW | 0 |
| S410 | RubberBand_OTM1 | 3 | -68.49% | 33% | WATCH | 1 |
| S411 | RubberBand_OTM2 | 24 | +6.57% | 54% | INSUFFICIENT | 4 |
| S412 | RubberBand_OTM3 | 24 | -2.90% | 46% | INSUFFICIENT | 7 |
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
| S218 | 48 | +50.00% | 67% | Tyler review |
| S398 | 34 | +48.98% | 59% | Tyler review |
| S408 | 36 | +43.55% | 56% | Tyler review |
| S401 | 52 | +26.95% | 60% | Tyler review |
| S210 | 43 | +13.89% | 60% | Tyler review |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- **p25** sits between p10 and median for mid-tail visibility.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
- Active paper strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419.
