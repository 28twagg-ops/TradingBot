# Options strategy selection report — 2026-08-04

_Generated 2026-08-04T17:01:04.703177_

## Summary

- Strategies analyzed: **105**
- Keep: **0**
- Watch: **101**
- Drop: **4**

## Attribution health

- Total exits: **1267**
- Orphan exits (b0/orphan_reconcile): **47**
- Orphan rate: **3.7%** (warn if >10%)
- Orphan rate OK (attribution looks healthy).

## Strategy scoreboard

| strategy | DTE | rec | exits | win% | med% | p10% | p25% | p90% | days live | ent 5d | exit 5d | realized $ | top share | rationale |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S355 (GapDown_7DTE) | 7d | watch | 10 | 100.0 | +135.99 | +90.51 | +92.48 | +296.43 | 4 | 20 | 10 | $+731.00 | 80.0% | building sample (8-19 exits) |
| S354 (GapDown_5DTE) | 5d | watch | 16 | 87.5 | +130.56 | +21.43 | +102.31 | +197.92 | 4 | 32 | 16 | $+998.00 | 43.8% | building sample (8-19 exits) |
| S407 (RubberBand_ITM2) | 3d | watch | 13 | 69.2 | +125.00 | -95.92 | -66.67 | +441.54 | 4 | 34 | 13 | $+229.00 | 53.8% | building sample (8-19 exits) |
| S361 (RubberBand_2DTE) | 2d | watch | 10 | 90.0 | +94.83 | +33.68 | +62.37 | +187.33 | 4 | 35 | 10 | $+229.00 | 70.0% | building sample (8-19 exits) |
| S352 (GapDown_2DTE) | 2d | watch | 9 | 100.0 | +93.75 | +45.87 | +52.38 | +223.89 | 4 | 28 | 9 | $+314.00 | 55.6% | building sample (8-19 exits) |
| S399 (GapDown_OTM1) | 3d | watch | 17 | 76.5 | +92.00 | -67.20 | +52.63 | +144.00 | 4 | 50 | 17 | $+397.00 | 52.9% | building sample (8-19 exits) |
| S217 (RSI_25_Bounce) | 3d ATM RSI<25 bounce | watch | 15 | 86.7 | +77.78 | -12.58 | +59.91 | +626.21 | 8 | 36 | 15 | $+779.00 | 53.3% | building sample (8-19 exits) |
| S412 (RubberBand_OTM3) | 3d | watch | 10 | 100.0 | +76.69 | +37.15 | +46.75 | +95.10 | 4 | 35 | 10 | $+246.00 | 60.0% | building sample (8-19 exits) |
| S406 (RubberBand_ITM3) | 3d | watch | 17 | 82.4 | +73.08 | -23.83 | +63.64 | +169.48 | 4 | 34 | 17 | $+347.00 | 70.6% | building sample (8-19 exits) |
| S398 (GapDown_ATM) | 3d | watch | 16 | 87.5 | +71.60 | -0.51 | +49.74 | +243.73 | 4 | 39 | 16 | $+864.00 | 50.0% | building sample (8-19 exits) |
| S364 (RubberBand_7DTE) | 7d | watch | 16 | 100.0 | +68.12 | +56.79 | +62.73 | +211.11 | 4 | 32 | 16 | $+626.00 | 75.0% | building sample (8-19 exits) |
| S218 (BB_Lower_Touch) | 3d ATM BB lower touch | watch | 16 | 81.2 | +67.97 | -16.66 | +43.05 | +570.31 | 8 | 28 | 14 | $+684.00 | 56.2% | building sample (8-19 exits) |
| S403 (Any_MA50_Touch) | 3d | watch | 5 | 100.0 | +65.38 | +53.03 | +57.58 | +318.40 | 4 | 20 | 5 | $+257.00 | 60.0% | insufficient sample (<8 exits) |
| S350 (GapDown_0DTE) | 0d | watch | 22 | 63.6 | +64.90 | -62.55 | -21.20 | +253.14 | 4 | 32 | 22 | $+516.00 | 54.5% | fat left tail (p10 < -45%) |
| S397 (GapDown_ITM1) | 3d | watch | 9 | 100.0 | +61.90 | +40.00 | +43.66 | +123.43 | 4 | 30 | 9 | $+433.00 | 77.8% | building sample (8-19 exits) |
| S404 (GapDown_OTM2) | 3d | watch | 10 | 100.0 | +55.86 | +37.90 | +45.37 | +126.29 | 4 | 30 | 10 | $+460.00 | 80.0% | building sample (8-19 exits) |
| S405 (GapDown_OTM3) | 3d | watch | 17 | 82.4 | +55.71 | -47.65 | +42.86 | +182.48 | 4 | 41 | 17 | $+629.00 | 47.1% | building sample (8-19 exits) |
| S401 (Any_Gap_Down_Small) | 3d | watch | 20 | 90.0 | +53.66 | +3.91 | +23.02 | +171.31 | 4 | 40 | 20 | $+548.00 | 55.0% | promising mid-sample — need more exits |
| S363 (RubberBand_5DTE) | 5d | watch | 10 | 100.0 | +52.94 | +7.14 | +9.52 | +103.55 | 1 | 22 | 10 | $+150.00 | 60.0% | building sample (8-19 exits) |
| S210 (MA_Cross_8_21) | 3d ATM MA cross 8/21 | watch | 9 | 100.0 | +50.00 | +38.64 | +48.28 | +79.13 | 8 | 30 | 9 | $+128.00 | 88.9% | building sample (8-19 exits) |
| S356 (GapDown_14DTE) | 14d | watch | 4 | 100.0 | +48.27 | +37.93 | +37.93 | +58.62 | 4 | 22 | 4 | $+112.00 | 100.0% | insufficient sample (<8 exits) |
| S357 (GapDown_21DTE) | 21d | watch | 5 | 100.0 | +47.06 | +47.06 | +47.06 | +53.66 | 4 | 20 | 5 | $+164.00 | 100.0% | insufficient sample (<8 exits) |
| S362 (RubberBand_3DTE) | 3d | watch | 16 | 100.0 | +45.44 | +10.87 | +21.02 | +111.31 | 4 | 42 | 16 | $+382.00 | 37.5% | building sample (8-19 exits) |
| S408 (RubberBand_ITM1) | 3d | watch | 9 | 66.7 | +45.16 | -1.25 | +0.00 | +100.00 | 1 | 26 | 9 | $+78.00 | 66.7% | building sample (8-19 exits) |
| S411 (RubberBand_OTM2) | 3d | watch | 8 | 100.0 | +37.20 | +12.31 | +13.35 | +58.73 | 1 | 26 | 8 | $+152.00 | 50.0% | building sample (8-19 exits) |
| S163 (A1 GapDown ATM call EOD) | 7d ATM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 14 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | 3d ATM strong | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 14 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S167 (GapDown long call 3 DTE 1-OTM — P2C) | 3d 1-OTM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 14 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S168 (GapDown ATM 5-DTE — P2B arm) | 5d ATM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 14 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
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
| S209 (GapDown_Recovery) | 3d ATM gap-recovery | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 6 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S213 (MA_Bounce_200) | 3d ATM MA bounce 200 | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S214 (MA_Death_Cross) | 3d ATM death cross (put) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S215 (MA_Reclaim_200) | 3d ATM MA reclaim 200 | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S219 (Volume_Climax_Up) | 3d ATM vol climax up | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S220 (Pullback50) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S221 (GoldenPocket) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S358 (GapDown_30DTE) | 30d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 0 | 2 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S365 (RubberBand_14DTE) | 14d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 4 | 14 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S366 (RubberBand_21DTE) | 21d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 0 | 12 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S367 (RubberBand_30DTE) | 30d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 0 | 2 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
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
| S396 (GapDown_ITM2) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S402 (Any_High_Volume) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S409 (RubberBand_ATM) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S410 (RubberBand_OTM1) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S413 (BBSqueeze_ITM3) | 0d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S414 (BBSqueeze_ITM2) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S415 (BBSqueeze_ITM1) | 7d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S416 (BBSqueeze_ATM) | 0d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S417 (BBSqueeze_OTM1) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S418 (BBSqueeze_OTM2) | 7d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S419 (BBSqueeze_OTM3) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S211 (MA_Cross_21_50) | 3d ATM MA cross 21/50 | watch | 14 | 14.3 | -17.14 | -49.87 | -42.85 | +35.27 | 8 | 34 | 14 | $-101.00 | 71.4% | early sample with non-positive median |
| S359 (RubberBand_0DTE) | 0d | watch | 10 | 40.0 | -33.33 | -46.67 | -39.29 | +151.43 | 1 | 20 | 10 | $+11.00 | 60.0% | early sample with non-positive median |
| S360 (RubberBand_1DTE) | 1d | watch | 14 | 21.4 | -35.19 | -55.32 | -50.00 | +39.85 | 4 | 30 | 14 | $-100.00 | 57.1% | early sample with non-positive median |
| S207 (GapDown_AtSupport) | 3d ATM gap-support | watch | 13 | 15.4 | -49.15 | -58.95 | -55.71 | +11.01 | 8 | 26 | 13 | $-305.00 | 76.9% | early sample with non-positive median |
| S400 (Any_Green_Close) | 3d | watch | 5 | 0.0 | -50.00 | -66.67 | -66.67 | -33.33 | 4 | 12 | 5 | $-30.00 | 100.0% | insufficient sample (<8 exits) |
| S203 (GapUp_Fade) | 3d ATM gap-up fade (put) | watch | 15 | 0.0 | -53.33 | -64.74 | -59.48 | -49.02 | 8 | 35 | 15 | $-426.00 | 60.0% | early sample with non-positive median |
| S202 (GapDown_Monster) | 3d ATM gap-monster | watch | 6 | 0.0 | -64.75 | -70.52 | -66.39 | -44.87 | 7 | 16 | 4 | $-133.00 | 66.7% | insufficient sample (<8 exits) |
| S212 (MA_Bounce_50) | 3d ATM MA bounce 50 | watch | 14 | 0.0 | -64.90 | -73.84 | -72.11 | -45.97 | 8 | 33 | 14 | $-471.00 | 64.3% | early sample with non-positive median |
| S164 (GapDown ATM 1-DTE — P2B arm) | 1d ATM | watch | 6 | 0.0 | -65.67 | -88.89 | -86.11 | -50.00 | 14 | 0 | 0 | $-59.00 | 83.3% | insufficient sample (<8 exits) |
| S353 (GapDown_3DTE) | 3d | watch | 11 | 36.4 | -69.70 | -79.59 | -77.44 | +123.68 | 4 | 31 | 11 | $-82.00 | 45.5% | early sample with non-positive median |
| S216 (RSI_Oversold_Cross) | 3d ATM RSI x30 | watch | 3 | 0.0 | -80.49 | -80.49 | -80.49 | -80.49 | 8 | 12 | 3 | $-99.00 | 100.0% | insufficient sample (<8 exits) |
| S174 (RubberBand long call EOD) | RubberBand (dropped) | drop | 119 | 36.1 | -25.00 | -89.83 | -71.19 | +36.67 | 29 | 0 | 0 | $-1,658.19 | 50.4% | manually paused — excluded from new entries & reflected P&L |
| S173 (MomReversal long call) | MomRev | drop | 415 | 37.1 | -31.51 | -77.18 | -62.95 | +101.90 | 29 | 0 | 0 | $+62.64 | 27.5% | manually paused — excluded from new entries & reflected P&L |
| S165 (GapDown long call 3 DTE) | 3d ATM | drop | 245 | 29.8 | -38.18 | -63.39 | -54.55 | +81.82 | 29 | 0 | 0 | $-1,828.78 | 26.1% | non-positive median return |
| S351 (GapDown_1DTE) | 1d | drop | 21 | 33.3 | -43.75 | -92.31 | -62.50 | +197.92 | 4 | 48 | 21 | $+152.00 | 42.9% | non-positive median return |

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
| S202 | 3d ATM gap-monster | 6 | -64.75 | -70.52 | -66.39 | 16 | 4 |
| S204 | 3d ATM gap-up cont | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S205 | 3d ATM gap-highvol | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S206 | 3d ATM gap-trend | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S207 | 3d ATM gap-support | 13 | -49.15 | -58.95 | -55.71 | 26 | 13 |
| S208 | 3d ATM gap-ma200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S209 | 3d ATM gap-recovery | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 Bearish Gap & MA

- Status: **INSUFFICIENT** | Best median: **S214** (+0.00%) | Best p10: **S214** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S203 | 3d ATM gap-up fade (put) | 15 | -53.33 | -64.74 | -59.48 | 35 | 15 |
| S214 | 3d ATM death cross (put) | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 MA family

- Status: **INSUFFICIENT** | Best median: **S210** (+50.00%) | Best p10: **S210** (+38.64%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S210 | 3d ATM MA cross 8/21 | 9 | +50.00 | +38.64 | +48.28 | 30 | 9 |
| S211 | 3d ATM MA cross 21/50 | 14 | -17.14 | -49.87 | -42.85 | 34 | 14 |
| S212 | 3d ATM MA bounce 50 | 14 | -64.90 | -73.84 | -72.11 | 33 | 14 |
| S213 | 3d ATM MA bounce 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S215 | 3d ATM MA reclaim 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 RSI/BB/Vol

- Status: **INSUFFICIENT** | Best median: **S217** (+77.78%) | Best p10: **S219** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S216 | 3d ATM RSI x30 | 3 | -80.49 | -80.49 | -80.49 | 12 | 3 |
| S217 | 3d ATM RSI<25 bounce | 15 | +77.78 | -12.58 | +59.91 | 36 | 15 |
| S218 | 3d ATM BB lower touch | 16 | +67.97 | -16.66 | +43.05 | 28 | 14 |
| S219 | 3d ATM vol climax up | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Other

- Status: **OK** | Best median: **S173** (-31.51%) | Best p10: **S173** (-77.18%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S173 | MomRev | 415 | -31.51 | -77.18 | -62.95 | 0 | 0 |

## Strategy Pipeline Status

_Pipeline evaluation as of 2026-08-04. Auto-kill thresholds: median<-25% at n>=15, p10<-85%, WR<15% at n>=25. Promote: n>=30 median>0%._

| Strategy | Signal | n | Median% | WR% | Status | Days |
|----------|--------|---|---------|-----|--------|------|
| S163 | A1 GapDown ATM call EO | 0 | — | — | NEW | 14 |
| S164 | GapDown ATM 1-DTE — P2 | 6 | -65.67% | 0% | WATCH | 14 |
| S165 | GapDown long call 3 DT | 245 | -38.18% | 30% | INSUFFICIENT | 29 |
| S166 | GapDown strong call | 0 | — | — | NEW | 14 |
| S167 | GapDown long call 3 DT | 0 | — | — | NEW | 14 |
| S168 | GapDown ATM 5-DTE — P2 | 0 | — | — | NEW | 14 |
| S169 | BB Squeeze Breakout ca | 0 | — | — | NEW | 0 |
| S170 | Golden Pocket call 3 D | 0 | — | — | NEW | 0 |
| S171 | VWAP Reclaim call 3 DT | 0 | — | — | NEW | 0 |
| S172 | Trend Resumption call  | 0 | — | — | NEW | 0 |
| S173 | MomReversal long call | 415 | -31.51% | 37% | INSUFFICIENT | 29 |
| S174 | RubberBand long call E | 119 | -25.00% | 36% | INSUFFICIENT | 29 |
| S175 | Earnings Drift call 3  | 0 | — | — | NEW | 0 |
| S200 | GapDown_Aggressive | 0 | — | — | NEW | 0 |
| S201 | GapDown_Mild | 0 | — | — | NEW | 0 |
| S202 | GapDown_Monster | 6 | -64.75% | 0% | WATCH | 7 |
| S203 | GapUp_Fade | 15 | -53.33% | 0% | INSUFFICIENT | 8 |
| S204 | GapUp_Continuation | 0 | — | — | NEW | 0 |
| S205 | GapDown_HighVol | 0 | — | — | NEW | 0 |
| S206 | GapDown_WithTrend | 0 | — | — | NEW | 0 |
| S207 | GapDown_AtSupport | 13 | -49.15% | 15% | WATCH | 8 |
| S208 | GapDown_AboveMA200 | 0 | — | — | NEW | 0 |
| S209 | GapDown_Recovery | 0 | — | — | NEW | 6 |
| S210 | MA_Cross_8_21 | 9 | +50.00% | 100% | WATCH | 8 |
| S211 | MA_Cross_21_50 | 14 | -17.14% | 14% | WATCH | 8 |
| S212 | MA_Bounce_50 | 14 | -64.90% | 0% | WATCH | 8 |
| S213 | MA_Bounce_200 | 0 | — | — | NEW | 0 |
| S214 | MA_Death_Cross | 0 | — | — | NEW | 0 |
| S215 | MA_Reclaim_200 | 0 | — | — | NEW | 0 |
| S216 | RSI_Oversold_Cross | 3 | -80.49% | 0% | WATCH | 8 |
| S217 | RSI_25_Bounce | 15 | +77.78% | 87% | INSUFFICIENT | 8 |
| S218 | BB_Lower_Touch | 16 | +67.97% | 81% | INSUFFICIENT | 8 |
| S219 | Volume_Climax_Up | 0 | — | — | NEW | 0 |
| S220 | Pullback50 | 0 | — | — | NEW | 0 |
| S221 | GoldenPocket | 0 | — | — | NEW | 0 |
| S350 | GapDown_0DTE | 22 | +64.90% | 64% | INSUFFICIENT | 4 |
| S351 | GapDown_1DTE | 21 | -43.75% | 33% | INSUFFICIENT | 4 |
| S352 | GapDown_2DTE | 9 | +93.75% | 100% | WATCH | 4 |
| S353 | GapDown_3DTE | 11 | -69.70% | 36% | WATCH | 4 |
| S354 | GapDown_5DTE | 16 | +130.56% | 88% | INSUFFICIENT | 4 |
| S355 | GapDown_7DTE | 10 | +135.99% | 100% | WATCH | 4 |
| S356 | GapDown_14DTE | 4 | +48.27% | 100% | WATCH | 4 |
| S357 | GapDown_21DTE | 5 | +47.06% | 100% | WATCH | 4 |
| S358 | GapDown_30DTE | 0 | — | — | NEW | 0 |
| S359 | RubberBand_0DTE | 10 | -33.33% | 40% | WATCH | 1 |
| S360 | RubberBand_1DTE | 14 | -35.19% | 21% | WATCH | 4 |
| S361 | RubberBand_2DTE | 10 | +94.83% | 90% | WATCH | 4 |
| S362 | RubberBand_3DTE | 16 | +45.44% | 100% | INSUFFICIENT | 4 |
| S363 | RubberBand_5DTE | 10 | +52.94% | 100% | WATCH | 1 |
| S364 | RubberBand_7DTE | 16 | +68.12% | 100% | INSUFFICIENT | 4 |
| S365 | RubberBand_14DTE | 0 | — | — | NEW | 4 |
| S366 | RubberBand_21DTE | 0 | — | — | NEW | 0 |
| S367 | RubberBand_30DTE | 0 | — | — | NEW | 0 |
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
| S397 | GapDown_ITM1 | 9 | +61.90% | 100% | WATCH | 4 |
| S398 | GapDown_ATM | 16 | +71.60% | 88% | INSUFFICIENT | 4 |
| S399 | GapDown_OTM1 | 17 | +92.00% | 76% | INSUFFICIENT | 4 |
| S400 | Any_Green_Close | 5 | -50.00% | 0% | WATCH | 4 |
| S401 | Any_Gap_Down_Small | 20 | +53.66% | 90% | INSUFFICIENT | 4 |
| S402 | Any_High_Volume | 0 | — | — | NEW | 0 |
| S403 | Any_MA50_Touch | 5 | +65.38% | 100% | WATCH | 4 |
| S404 | GapDown_OTM2 | 10 | +55.86% | 100% | WATCH | 4 |
| S405 | GapDown_OTM3 | 17 | +55.71% | 82% | INSUFFICIENT | 4 |
| S406 | RubberBand_ITM3 | 17 | +73.08% | 82% | INSUFFICIENT | 4 |
| S407 | RubberBand_ITM2 | 13 | +125.00% | 69% | WATCH | 4 |
| S408 | RubberBand_ITM1 | 9 | +45.16% | 67% | WATCH | 1 |
| S409 | RubberBand_ATM | 0 | — | — | NEW | 0 |
| S410 | RubberBand_OTM1 | 0 | — | — | NEW | 0 |
| S411 | RubberBand_OTM2 | 8 | +37.20% | 100% | WATCH | 1 |
| S412 | RubberBand_OTM3 | 10 | +76.69% | 100% | WATCH | 4 |
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
| — | — | — | — | (none yet — collecting data) |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- **p25** sits between p10 and median for mid-tail visibility.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
- Active paper strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419.
