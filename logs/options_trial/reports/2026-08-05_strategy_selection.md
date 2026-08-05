# Options strategy selection report — 2026-08-05

_Generated 2026-08-05T11:12:36.791673_

## Summary

- Strategies analyzed: **105**
- Keep: **0**
- Watch: **97**
- Drop: **8**

## Attribution health

- Total exits: **1462**
- Orphan exits (b0/orphan_reconcile): **70**
- Orphan rate: **4.8%** (warn if >10%)
- Orphan rate OK (attribution looks healthy).

## Strategy scoreboard

| strategy | DTE | rec | exits | win% | med% | p10% | p25% | p90% | days live | ent 5d | exit 5d | realized $ | top share | rationale |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S354 (GapDown_5DTE) | 5d | watch | 20 | 70.0 | +116.67 | -64.66 | -51.16 | +179.58 | 5 | 20 | 6 | $+861.00 | 40.0% | fat left tail (p10 < -45%) |
| S355 (GapDown_7DTE) | 7d | watch | 13 | 76.9 | +95.45 | -65.34 | +85.11 | +273.04 | 5 | 12 | 3 | $+644.00 | 61.5% | building sample (8-19 exits) |
| S352 (GapDown_2DTE) | 2d | watch | 11 | 81.8 | +90.00 | -64.86 | +43.25 | +194.44 | 5 | 28 | 4 | $+266.00 | 54.5% | building sample (8-19 exits) |
| S361 (RubberBand_2DTE) | 2d | watch | 15 | 80.0 | +82.76 | -43.33 | +31.30 | +180.00 | 5 | 43 | 15 | $+259.00 | 66.7% | building sample (8-19 exits) |
| S350 (GapDown_0DTE) | 0d | watch | 25 | 68.0 | +76.47 | -61.96 | +0.00 | +232.57 | 5 | 37 | 19 | $+613.00 | 48.0% | fat left tail (p10 < -45%) |
| S406 (RubberBand_ITM3) | 3d | watch | 25 | 68.0 | +72.41 | -55.82 | -6.38 | +178.95 | 5 | 43 | 21 | $+1,084.00 | 52.0% | fat left tail (p10 < -45%) |
| S217 (RSI_25_Bounce) | 3d ATM RSI<25 bounce | watch | 20 | 70.0 | +71.45 | -55.89 | -46.05 | +301.84 | 9 | 38 | 19 | $+738.00 | 50.0% | fat left tail (p10 < -45%) |
| S364 (RubberBand_7DTE) | 7d | watch | 16 | 100.0 | +68.12 | +56.79 | +62.73 | +211.11 | 5 | 32 | 12 | $+626.00 | 75.0% | building sample (8-19 exits) |
| S398 (GapDown_ATM) | 3d | watch | 18 | 77.8 | +65.89 | -32.07 | +48.98 | +216.46 | 5 | 35 | 4 | $+847.00 | 44.4% | building sample (8-19 exits) |
| S399 (GapDown_OTM1) | 3d | watch | 24 | 58.3 | +62.07 | -67.60 | -64.40 | +138.20 | 5 | 53 | 12 | $+322.00 | 45.8% | fat left tail (p10 < -45%) |
| S397 (GapDown_ITM1) | 3d | watch | 9 | 100.0 | +61.90 | +40.00 | +43.66 | +123.43 | 5 | 28 | 0 | $+433.00 | 77.8% | building sample (8-19 exits) |
| S362 (RubberBand_3DTE) | 3d | watch | 23 | 100.0 | +60.47 | +13.04 | +29.28 | +121.15 | 5 | 51 | 23 | $+1,390.00 | 43.5% | promising mid-sample — need more exits |
| S403 (Any_MA50_Touch) | 3d | watch | 11 | 63.6 | +57.58 | -77.46 | -59.32 | +320.00 | 5 | 16 | 11 | $+230.00 | 36.4% | building sample (8-19 exits) |
| S412 (RubberBand_OTM3) | 3d | watch | 14 | 78.6 | +57.45 | -11.52 | +34.91 | +92.59 | 5 | 44 | 14 | $+253.00 | 42.9% | building sample (8-19 exits) |
| S404 (GapDown_OTM2) | 3d | watch | 10 | 100.0 | +55.86 | +37.90 | +45.37 | +126.29 | 5 | 28 | 0 | $+460.00 | 80.0% | building sample (8-19 exits) |
| S363 (RubberBand_5DTE) | 5d | watch | 10 | 100.0 | +52.94 | +7.14 | +9.52 | +103.55 | 2 | 26 | 10 | $+150.00 | 60.0% | building sample (8-19 exits) |
| S408 (RubberBand_ITM1) | 3d | watch | 15 | 66.7 | +52.63 | -6.25 | +0.00 | +1036.00 | 2 | 40 | 15 | $+631.00 | 53.3% | building sample (8-19 exits) |
| S401 (Any_Gap_Down_Small) | 3d | watch | 27 | 74.1 | +50.00 | -45.79 | +0.14 | +205.23 | 5 | 36 | 25 | $+645.00 | 44.4% | fat left tail (p10 < -45%) |
| S218 (BB_Lower_Touch) | 3d ATM BB lower touch | watch | 25 | 68.0 | +50.00 | -65.89 | -33.33 | +369.37 | 9 | 36 | 23 | $+606.00 | 56.0% | fat left tail (p10 < -45%) |
| S356 (GapDown_14DTE) | 14d | watch | 4 | 100.0 | +48.27 | +37.93 | +37.93 | +58.62 | 5 | 16 | 2 | $+112.00 | 100.0% | insufficient sample (<8 exits) |
| S357 (GapDown_21DTE) | 21d | watch | 7 | 100.0 | +47.06 | +47.06 | +47.06 | +64.58 | 5 | 14 | 5 | $+242.00 | 85.7% | insufficient sample (<8 exits) |
| S405 (GapDown_OTM3) | 3d | watch | 23 | 60.9 | +46.94 | -57.10 | -41.46 | +138.22 | 5 | 38 | 9 | $+473.00 | 47.8% | fat left tail (p10 < -45%) |
| S407 (RubberBand_ITM2) | 3d | watch | 17 | 58.8 | +44.90 | -95.92 | -61.54 | +432.31 | 5 | 44 | 13 | $+248.00 | 41.2% | building sample (8-19 exits) |
| S411 (RubberBand_OTM2) | 3d | watch | 14 | 92.9 | +18.66 | +5.03 | +11.11 | +53.72 | 2 | 44 | 14 | $+206.00 | 42.9% | building sample (8-19 exits) |
| S210 (MA_Cross_8_21) | 3d ATM MA cross 8/21 | watch | 21 | 81.0 | +16.67 | -8.51 | +7.69 | +57.14 | 9 | 45 | 21 | $+116.00 | 38.1% | promising mid-sample — need more exits |
| S163 (A1 GapDown ATM call EOD) | 7d ATM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 15 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | 3d ATM strong | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 15 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S167 (GapDown long call 3 DTE 1-OTM — P2C) | 3d 1-OTM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 15 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S168 (GapDown ATM 5-DTE — P2B arm) | 5d ATM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 15 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
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
| S209 (GapDown_Recovery) | 3d ATM gap-recovery | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 7 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S213 (MA_Bounce_200) | 3d ATM MA bounce 200 | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S214 (MA_Death_Cross) | 3d ATM death cross (put) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S215 (MA_Reclaim_200) | 3d ATM MA reclaim 200 | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S219 (Volume_Climax_Up) | 3d ATM vol climax up | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S220 (Pullback50) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S221 (GoldenPocket) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S358 (GapDown_30DTE) | 30d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 1 | 4 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S365 (RubberBand_14DTE) | 14d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 5 | 18 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S366 (RubberBand_21DTE) | 21d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 1 | 22 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S367 (RubberBand_30DTE) | 30d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 1 | 4 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
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
| S211 (MA_Cross_21_50) | 3d ATM MA cross 21/50 | watch | 18 | 22.2 | -17.14 | -49.54 | -44.44 | +112.88 | 9 | 48 | 18 | $-49.00 | 66.7% | early sample with non-positive median |
| S359 (RubberBand_0DTE) | 0d | watch | 16 | 25.0 | -42.98 | -71.29 | -68.91 | +103.25 | 2 | 28 | 16 | $-182.00 | 50.0% | early sample with non-positive median |
| S400 (Any_Green_Close) | 3d | watch | 5 | 0.0 | -50.00 | -66.67 | -66.67 | -33.33 | 5 | 0 | 0 | $-30.00 | 100.0% | insufficient sample (<8 exits) |
| S353 (GapDown_3DTE) | 3d | watch | 12 | 33.3 | -60.23 | -79.49 | -76.88 | +119.21 | 5 | 26 | 8 | $-99.00 | 50.0% | early sample with non-positive median |
| S202 (GapDown_Monster) | 3d ATM gap-monster | watch | 6 | 0.0 | -64.75 | -70.52 | -66.39 | -44.87 | 8 | 0 | 2 | $-133.00 | 66.7% | insufficient sample (<8 exits) |
| S164 (GapDown ATM 1-DTE — P2B arm) | 1d ATM | watch | 6 | 0.0 | -65.67 | -88.89 | -86.11 | -50.00 | 15 | 0 | 0 | $-59.00 | 83.3% | insufficient sample (<8 exits) |
| S216 (RSI_Oversold_Cross) | 3d ATM RSI x30 | watch | 10 | 0.0 | -69.61 | -81.15 | -80.49 | -51.67 | 9 | 18 | 10 | $-338.00 | 50.0% | early sample with non-positive median |
| S174 (RubberBand long call EOD) | RubberBand (dropped) | drop | 119 | 36.1 | -25.00 | -89.83 | -71.19 | +36.67 | 30 | 0 | 0 | $-1,658.19 | 50.4% | manually paused — excluded from new entries & reflected P&L |
| S173 (MomReversal long call) | MomRev | drop | 415 | 37.1 | -31.51 | -77.18 | -62.95 | +101.90 | 30 | 0 | 0 | $+62.64 | 27.5% | manually paused — excluded from new entries & reflected P&L |
| S165 (GapDown long call 3 DTE) | 3d ATM | drop | 245 | 29.8 | -38.18 | -63.39 | -54.55 | +81.82 | 30 | 0 | 0 | $-1,828.78 | 26.1% | non-positive median return |
| S351 (GapDown_1DTE) | 1d | drop | 27 | 29.6 | -48.72 | -91.93 | -68.75 | +182.30 | 5 | 56 | 16 | $+81.00 | 40.7% | non-positive median return |
| S207 (GapDown_AtSupport) | 3d ATM gap-support | drop | 26 | 7.7 | -49.15 | -62.64 | -55.84 | -6.06 | 9 | 36 | 26 | $-632.00 | 61.5% | non-positive median return |
| S360 (RubberBand_1DTE) | 1d | drop | 22 | 13.6 | -50.00 | -81.11 | -68.80 | +1.67 | 5 | 35 | 18 | $-322.00 | 45.5% | non-positive median return |
| S203 (GapUp_Fade) | 3d ATM gap-up fade (put) | drop | 20 | 0.0 | -54.79 | -76.94 | -66.10 | -49.02 | 9 | 35 | 16 | $-591.00 | 70.0% | non-positive median return |
| S212 (MA_Bounce_50) | 3d ATM MA bounce 50 | drop | 28 | 0.0 | -71.01 | -98.03 | -75.78 | -52.56 | 9 | 33 | 28 | $-1,112.00 | 57.1% | non-positive median return |

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
| S207 | 3d ATM gap-support | 26 | -49.15 | -62.64 | -55.84 | 36 | 26 |
| S208 | 3d ATM gap-ma200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S209 | 3d ATM gap-recovery | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 Bearish Gap & MA

- Status: **INSUFFICIENT** | Best median: **S214** (+0.00%) | Best p10: **S214** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S203 | 3d ATM gap-up fade (put) | 20 | -54.79 | -76.94 | -66.10 | 35 | 16 |
| S214 | 3d ATM death cross (put) | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 MA family

- Status: **INSUFFICIENT** | Best median: **S210** (+16.67%) | Best p10: **S213** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S210 | 3d ATM MA cross 8/21 | 21 | +16.67 | -8.51 | +7.69 | 45 | 21 |
| S211 | 3d ATM MA cross 21/50 | 18 | -17.14 | -49.54 | -44.44 | 48 | 18 |
| S212 | 3d ATM MA bounce 50 | 28 | -71.01 | -98.03 | -75.78 | 33 | 28 |
| S213 | 3d ATM MA bounce 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S215 | 3d ATM MA reclaim 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 RSI/BB/Vol

- Status: **INSUFFICIENT** | Best median: **S217** (+71.45%) | Best p10: **S219** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S216 | 3d ATM RSI x30 | 10 | -69.61 | -81.15 | -80.49 | 18 | 10 |
| S217 | 3d ATM RSI<25 bounce | 20 | +71.45 | -55.89 | -46.05 | 38 | 19 |
| S218 | 3d ATM BB lower touch | 25 | +50.00 | -65.89 | -33.33 | 36 | 23 |
| S219 | 3d ATM vol climax up | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Other

- Status: **OK** | Best median: **S173** (-31.51%) | Best p10: **S173** (-77.18%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S173 | MomRev | 415 | -31.51 | -77.18 | -62.95 | 0 | 0 |

## Strategy Pipeline Status

_Pipeline evaluation as of 2026-08-05. Auto-kill thresholds: median<-25% at n>=15, p10<-85%, WR<15% at n>=25. Promote: n>=30 median>0%._

| Strategy | Signal | n | Median% | WR% | Status | Days |
|----------|--------|---|---------|-----|--------|------|
| S163 | A1 GapDown ATM call EO | 0 | — | — | NEW | 15 |
| S164 | GapDown ATM 1-DTE — P2 | 6 | -65.67% | 0% | WATCH | 15 |
| S165 | GapDown long call 3 DT | 245 | -38.18% | 30% | INSUFFICIENT | 30 |
| S166 | GapDown strong call | 0 | — | — | NEW | 15 |
| S167 | GapDown long call 3 DT | 0 | — | — | NEW | 15 |
| S168 | GapDown ATM 5-DTE — P2 | 0 | — | — | NEW | 15 |
| S169 | BB Squeeze Breakout ca | 0 | — | — | NEW | 0 |
| S170 | Golden Pocket call 3 D | 0 | — | — | NEW | 0 |
| S171 | VWAP Reclaim call 3 DT | 0 | — | — | NEW | 0 |
| S172 | Trend Resumption call  | 0 | — | — | NEW | 0 |
| S173 | MomReversal long call | 415 | -31.51% | 37% | INSUFFICIENT | 30 |
| S174 | RubberBand long call E | 119 | -25.00% | 36% | INSUFFICIENT | 30 |
| S175 | Earnings Drift call 3  | 0 | — | — | NEW | 0 |
| S200 | GapDown_Aggressive | 0 | — | — | NEW | 0 |
| S201 | GapDown_Mild | 0 | — | — | NEW | 0 |
| S202 | GapDown_Monster | 6 | -64.75% | 0% | WATCH | 8 |
| S203 | GapUp_Fade | 20 | -54.79% | 0% | INSUFFICIENT | 9 |
| S204 | GapUp_Continuation | 0 | — | — | NEW | 0 |
| S205 | GapDown_HighVol | 0 | — | — | NEW | 0 |
| S206 | GapDown_WithTrend | 0 | — | — | NEW | 0 |
| S207 | GapDown_AtSupport | 26 | -49.15% | 8% | INSUFFICIENT | 9 |
| S208 | GapDown_AboveMA200 | 0 | — | — | NEW | 0 |
| S209 | GapDown_Recovery | 0 | — | — | NEW | 7 |
| S210 | MA_Cross_8_21 | 21 | +16.67% | 81% | INSUFFICIENT | 9 |
| S211 | MA_Cross_21_50 | 18 | -17.14% | 22% | INSUFFICIENT | 9 |
| S212 | MA_Bounce_50 | 28 | -71.01% | 0% | INSUFFICIENT | 9 |
| S213 | MA_Bounce_200 | 0 | — | — | NEW | 0 |
| S214 | MA_Death_Cross | 0 | — | — | NEW | 0 |
| S215 | MA_Reclaim_200 | 0 | — | — | NEW | 0 |
| S216 | RSI_Oversold_Cross | 10 | -69.61% | 0% | WATCH | 9 |
| S217 | RSI_25_Bounce | 20 | +71.45% | 70% | INSUFFICIENT | 9 |
| S218 | BB_Lower_Touch | 25 | +50.00% | 68% | INSUFFICIENT | 9 |
| S219 | Volume_Climax_Up | 0 | — | — | NEW | 0 |
| S220 | Pullback50 | 0 | — | — | NEW | 0 |
| S221 | GoldenPocket | 0 | — | — | NEW | 0 |
| S350 | GapDown_0DTE | 25 | +76.47% | 68% | INSUFFICIENT | 5 |
| S351 | GapDown_1DTE | 27 | -48.72% | 30% | INSUFFICIENT | 5 |
| S352 | GapDown_2DTE | 11 | +90.00% | 82% | WATCH | 5 |
| S353 | GapDown_3DTE | 12 | -60.23% | 33% | WATCH | 5 |
| S354 | GapDown_5DTE | 20 | +116.67% | 70% | INSUFFICIENT | 5 |
| S355 | GapDown_7DTE | 13 | +95.45% | 77% | WATCH | 5 |
| S356 | GapDown_14DTE | 4 | +48.27% | 100% | WATCH | 5 |
| S357 | GapDown_21DTE | 7 | +47.06% | 100% | WATCH | 5 |
| S358 | GapDown_30DTE | 0 | — | — | NEW | 1 |
| S359 | RubberBand_0DTE | 16 | -42.98% | 25% | INSUFFICIENT | 2 |
| S360 | RubberBand_1DTE | 22 | -50.00% | 14% | INSUFFICIENT | 5 |
| S361 | RubberBand_2DTE | 15 | +82.76% | 80% | INSUFFICIENT | 5 |
| S362 | RubberBand_3DTE | 23 | +60.47% | 100% | INSUFFICIENT | 5 |
| S363 | RubberBand_5DTE | 10 | +52.94% | 100% | WATCH | 2 |
| S364 | RubberBand_7DTE | 16 | +68.12% | 100% | INSUFFICIENT | 5 |
| S365 | RubberBand_14DTE | 0 | — | — | NEW | 5 |
| S366 | RubberBand_21DTE | 0 | — | — | NEW | 1 |
| S367 | RubberBand_30DTE | 0 | — | — | NEW | 1 |
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
| S397 | GapDown_ITM1 | 9 | +61.90% | 100% | WATCH | 5 |
| S398 | GapDown_ATM | 18 | +65.89% | 78% | INSUFFICIENT | 5 |
| S399 | GapDown_OTM1 | 24 | +62.07% | 58% | INSUFFICIENT | 5 |
| S400 | Any_Green_Close | 5 | -50.00% | 0% | WATCH | 5 |
| S401 | Any_Gap_Down_Small | 27 | +50.00% | 74% | INSUFFICIENT | 5 |
| S402 | Any_High_Volume | 0 | — | — | NEW | 0 |
| S403 | Any_MA50_Touch | 11 | +57.58% | 64% | WATCH | 5 |
| S404 | GapDown_OTM2 | 10 | +55.86% | 100% | WATCH | 5 |
| S405 | GapDown_OTM3 | 23 | +46.94% | 61% | INSUFFICIENT | 5 |
| S406 | RubberBand_ITM3 | 25 | +72.41% | 68% | INSUFFICIENT | 5 |
| S407 | RubberBand_ITM2 | 17 | +44.90% | 59% | INSUFFICIENT | 5 |
| S408 | RubberBand_ITM1 | 15 | +52.63% | 67% | INSUFFICIENT | 2 |
| S409 | RubberBand_ATM | 0 | — | — | NEW | 0 |
| S410 | RubberBand_OTM1 | 0 | — | — | NEW | 0 |
| S411 | RubberBand_OTM2 | 14 | +18.66% | 93% | WATCH | 2 |
| S412 | RubberBand_OTM3 | 14 | +57.45% | 79% | WATCH | 5 |
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
