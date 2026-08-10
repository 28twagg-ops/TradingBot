# Options strategy selection report — 2026-08-10

_Generated 2026-08-10T11:07:28.287776_

## Summary

- Strategies analyzed: **105**
- Keep: **0**
- Watch: **85**
- Drop: **20**

## Attribution health

- Total exits: **2159**
- Orphan exits (b0/orphan_reconcile): **232**
- Orphan rate: **10.8%** (warn if >10%)
- **ALERT:** orphan_rate > 10% — check client_order_id tagging / fill attribution before trusting strategy P&L.

## Strategy scoreboard

| strategy | DTE | rec | exits | win% | med% | p10% | p25% | p90% | days live | ent 5d | exit 5d | realized $ | top share | rationale |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S406 (RubberBand_ITM3) | 3d | watch | 50 | 60.0 | +66.13 | -63.62 | -50.91 | +965.79 | 10 | 35 | 3 | $+2,859.00 | 26.0% | fat left tail (p10 < -45%) |
| S364 (RubberBand_7DTE) | 7d | watch | 29 | 62.1 | +56.00 | -75.64 | -44.23 | +188.89 | 10 | 26 | 6 | $+297.00 | 41.4% | fat left tail (p10 < -45%) |
| S357 (GapDown_21DTE) | 21d | watch | 18 | 77.8 | +55.07 | -67.86 | +47.06 | +73.68 | 10 | 0 | 6 | $+323.00 | 44.4% | building sample (8-19 exits) |
| S403 (Any_MA50_Touch) | 3d | watch | 21 | 61.9 | +50.00 | -80.36 | -56.00 | +316.00 | 10 | 16 | 7 | $+291.00 | 42.9% | fat left tail (p10 < -45%) |
| S218 (BB_Lower_Touch) | 3d ATM BB lower touch | watch | 52 | 63.5 | +48.91 | -73.54 | -52.61 | +166.67 | 14 | 28 | 7 | $+977.00 | 46.2% | fat left tail (p10 < -45%) |
| S397 (GapDown_ITM1) | 3d | watch | 12 | 75.0 | +47.52 | -88.28 | +14.51 | +116.23 | 10 | 9 | 3 | $+304.00 | 58.3% | building sample (8-19 exits) |
| S408 (RubberBand_ITM1) | 3d | watch | 37 | 54.1 | +41.94 | -69.06 | -50.00 | +865.82 | 7 | 28 | 3 | $+1,255.00 | 27.0% | fat left tail (p10 < -45%) |
| S404 (GapDown_OTM2) | 3d | watch | 17 | 58.8 | +38.60 | -98.18 | -91.67 | +113.61 | 10 | 6 | 7 | $+113.00 | 52.9% | building sample (8-19 exits) |
| S362 (RubberBand_3DTE) | 3d | watch | 31 | 77.4 | +38.24 | -57.89 | +8.70 | +114.29 | 10 | 6 | 3 | $+1,178.00 | 41.9% | fat left tail (p10 < -45%) |
| S350 (GapDown_0DTE) | 0d | watch | 30 | 60.0 | +35.49 | -60.98 | -44.56 | +198.29 | 10 | 11 | 4 | $+584.00 | 43.3% | fat left tail (p10 < -45%) |
| S398 (GapDown_ATM) | 3d | watch | 36 | 55.6 | +26.15 | -61.92 | -43.54 | +156.67 | 10 | 18 | 8 | $+737.00 | 41.7% | fat left tail (p10 < -45%) |
| S401 (Any_Gap_Down_Small) | 3d | watch | 59 | 59.3 | +23.68 | -94.35 | -42.04 | +236.43 | 10 | 40 | 16 | $+1,063.00 | 35.6% | fat left tail (p10 < -45%) |
| S352 (GapDown_2DTE) | 2d | watch | 27 | 55.6 | +13.04 | -64.86 | -51.53 | +119.81 | 10 | 24 | 14 | $+203.00 | 25.9% | fat left tail (p10 < -45%) |
| S210 (MA_Cross_8_21) | 3d ATM MA cross 8/21 | watch | 50 | 56.0 | +10.79 | -72.07 | -43.86 | +78.70 | 14 | 27 | 14 | $+25.00 | 30.0% | fat left tail (p10 < -45%) |
| S356 (GapDown_14DTE) | 14d | watch | 8 | 50.0 | +9.24 | -47.41 | -30.32 | +58.62 | 10 | 2 | 4 | $+44.00 | 75.0% | building sample (8-19 exits) |
| S411 (RubberBand_OTM2) | 3d | watch | 27 | 55.6 | +7.69 | -57.32 | -52.50 | +41.00 | 7 | 13 | 11 | $-190.00 | 33.3% | fat left tail (p10 < -45%) |
| S163 (A1 GapDown ATM call EOD) | 7d ATM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 20 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | 3d ATM strong | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 20 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S167 (GapDown long call 3 DTE 1-OTM — P2C) | 3d 1-OTM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 20 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S168 (GapDown ATM 5-DTE — P2B arm) | 5d ATM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 20 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
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
| S353 (GapDown_3DTE) | 3d | watch | 19 | 36.8 | -34.69 | -86.52 | -77.44 | +123.68 | 10 | 6 | 5 | $-105.00 | 47.4% | early sample with non-positive median |
| S367 (RubberBand_30DTE) | 30d | watch | 2 | 0.0 | -38.20 | -48.75 | -44.79 | -27.64 | 6 | 0 | 2 | $-55.00 | 100.0% | insufficient sample (<8 exits) |
| S400 (Any_Green_Close) | 3d | watch | 5 | 0.0 | -50.00 | -66.67 | -66.67 | -33.33 | 10 | 0 | 0 | $-30.00 | 100.0% | insufficient sample (<8 exits) |
| S358 (GapDown_30DTE) | 30d | watch | 2 | 0.0 | -51.39 | -51.39 | -51.39 | -51.39 | 6 | 0 | 2 | $-74.00 | 100.0% | insufficient sample (<8 exits) |
| S365 (RubberBand_14DTE) | 14d | watch | 7 | 28.6 | -51.61 | -83.58 | -73.45 | +120.90 | 10 | 4 | 7 | $-63.00 | 42.9% | insufficient sample (<8 exits) |
| S366 (RubberBand_21DTE) | 21d | watch | 8 | 0.0 | -55.19 | -58.31 | -56.92 | -49.12 | 6 | 0 | 8 | $-268.00 | 100.0% | early sample with non-positive median |
| S209 (GapDown_Recovery) | 3d ATM gap-recovery | watch | 6 | 0.0 | -61.46 | -82.78 | -69.36 | -50.75 | 12 | 24 | 6 | $-210.00 | 83.3% | insufficient sample (<8 exits) |
| S202 (GapDown_Monster) | 3d ATM gap-monster | watch | 6 | 0.0 | -64.75 | -70.52 | -66.39 | -44.87 | 13 | 4 | 0 | $-133.00 | 66.7% | insufficient sample (<8 exits) |
| S164 (GapDown ATM 1-DTE — P2B arm) | 1d ATM | watch | 6 | 0.0 | -65.67 | -88.89 | -86.11 | -50.00 | 20 | 0 | 0 | $-59.00 | 83.3% | insufficient sample (<8 exits) |
| S410 (RubberBand_OTM1) | 3d | watch | 3 | 33.3 | -68.49 | -76.16 | -73.28 | +67.49 | 4 | 18 | 3 | $-39.00 | 66.7% | insufficient sample (<8 exits) |
| S396 (GapDown_ITM2) | 3d | watch | 1 | 0.0 | -82.19 | -82.19 | -82.19 | -82.19 | 4 | 6 | 1 | $-60.00 | 100.0% | insufficient sample (<8 exits) |
| S355 (GapDown_7DTE) | 7d | drop | 34 | 50.0 | -1.23 | -68.13 | -61.88 | +172.84 | 10 | 15 | 9 | $+457.00 | 32.4% | non-positive median return |
| S412 (RubberBand_OTM3) | 3d | drop | 26 | 42.3 | -3.57 | -47.62 | -14.40 | +88.94 | 10 | 18 | 4 | $+101.00 | 23.1% | non-positive median return |
| S361 (RubberBand_2DTE) | 2d | drop | 30 | 46.7 | -7.50 | -72.72 | -54.85 | +118.39 | 10 | 15 | 7 | $-72.00 | 36.7% | non-positive median return |
| S405 (GapDown_OTM3) | 3d | drop | 41 | 43.9 | -22.50 | -64.71 | -54.29 | +106.94 | 10 | 18 | 6 | $+257.00 | 36.6% | non-positive median return |
| S363 (RubberBand_5DTE) | 5d | drop | 22 | 50.0 | -23.36 | -87.87 | -77.04 | +63.93 | 7 | 24 | 11 | $-291.00 | 36.4% | non-positive median return |
| S211 (MA_Cross_21_50) | 3d ATM MA cross 21/50 | drop | 22 | 22.7 | -24.36 | -93.23 | -48.08 | +102.51 | 14 | 4 | 4 | $-143.00 | 68.2% | non-positive median return |
| S174 (RubberBand long call EOD) | RubberBand (dropped) | drop | 119 | 36.1 | -25.00 | -89.83 | -71.19 | +36.67 | 35 | 0 | 0 | $-1,658.19 | 50.4% | manually paused — excluded from new entries & reflected P&L |
| S173 (MomReversal long call) | MomRev | drop | 415 | 37.1 | -31.51 | -77.18 | -62.95 | +101.90 | 35 | 0 | 0 | $+62.64 | 27.5% | manually paused — excluded from new entries & reflected P&L |
| S165 (GapDown long call 3 DTE) | 3d ATM | drop | 245 | 29.8 | -38.18 | -63.39 | -54.55 | +81.82 | 35 | 0 | 0 | $-1,828.78 | 26.1% | non-positive median return |
| S354 (GapDown_5DTE) | 5d | drop | 34 | 41.2 | -43.75 | -80.48 | -72.88 | +141.82 | 10 | 26 | 7 | $+361.00 | 35.3% | non-positive median return |
| S217 (RSI_25_Bounce) | 3d ATM RSI<25 bounce | drop | 31 | 45.2 | -43.75 | -68.75 | -57.19 | +206.67 | 14 | 16 | 3 | $+502.00 | 67.7% | non-positive median return |
| S399 (GapDown_OTM1) | 3d | drop | 39 | 46.2 | -46.15 | -78.76 | -66.67 | +142.00 | 10 | 18 | 6 | $+64.00 | 41.0% | non-positive median return |
| S359 (RubberBand_0DTE) | 0d | drop | 23 | 17.4 | -46.67 | -71.43 | -70.37 | +61.82 | 7 | 10 | 0 | $-323.00 | 43.5% | non-positive median return |
| S207 (GapDown_AtSupport) | 3d ATM gap-support | drop | 37 | 5.4 | -47.06 | -63.64 | -55.71 | -6.06 | 14 | 0 | 0 | $-822.00 | 43.2% | non-positive median return |
| S407 (RubberBand_ITM2) | 3d | drop | 31 | 35.5 | -51.43 | -86.49 | -61.54 | +353.33 | 10 | 16 | 8 | $+154.00 | 29.0% | non-positive median return |
| S351 (GapDown_1DTE) | 1d | drop | 43 | 23.3 | -52.94 | -75.68 | -62.50 | +171.88 | 10 | 26 | 10 | $-76.00 | 30.2% | non-positive median return |
| S203 (GapUp_Fade) | 3d ATM gap-up fade (put) | drop | 33 | 12.1 | -54.00 | -79.08 | -74.42 | +38.86 | 14 | 14 | 5 | $-717.00 | 42.4% | non-positive median return |
| S360 (RubberBand_1DTE) | 1d | drop | 36 | 8.3 | -55.16 | -81.62 | -70.56 | -33.33 | 10 | 22 | 9 | $-650.00 | 30.6% | non-positive median return |
| S216 (RSI_Oversold_Cross) | 3d ATM RSI x30 | drop | 31 | 9.7 | -56.25 | -87.10 | -75.81 | -36.96 | 14 | 34 | 10 | $-759.00 | 51.6% | non-positive median return |
| S212 (MA_Bounce_50) | 3d ATM MA bounce 50 | drop | 66 | 7.6 | -70.59 | -98.30 | -84.48 | -43.77 | 14 | 43 | 16 | $-2,205.00 | 40.9% | non-positive median return |

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
| S202 | 3d ATM gap-monster | 6 | -64.75 | -70.52 | -66.39 | 4 | 0 |
| S204 | 3d ATM gap-up cont | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S205 | 3d ATM gap-highvol | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S206 | 3d ATM gap-trend | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S207 | 3d ATM gap-support | 37 | -47.06 | -63.64 | -55.71 | 0 | 0 |
| S208 | 3d ATM gap-ma200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S209 | 3d ATM gap-recovery | 6 | -61.46 | -82.78 | -69.36 | 24 | 6 |

### Phase-1 Bearish Gap & MA

- Status: **INSUFFICIENT** | Best median: **S214** (+0.00%) | Best p10: **S214** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S203 | 3d ATM gap-up fade (put) | 33 | -54.00 | -79.08 | -74.42 | 14 | 5 |
| S214 | 3d ATM death cross (put) | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 MA family

- Status: **INSUFFICIENT** | Best median: **S210** (+10.79%) | Best p10: **S213** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S210 | 3d ATM MA cross 8/21 | 50 | +10.79 | -72.07 | -43.86 | 27 | 14 |
| S211 | 3d ATM MA cross 21/50 | 22 | -24.36 | -93.23 | -48.08 | 4 | 4 |
| S212 | 3d ATM MA bounce 50 | 66 | -70.59 | -98.30 | -84.48 | 43 | 16 |
| S213 | 3d ATM MA bounce 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S215 | 3d ATM MA reclaim 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 RSI/BB/Vol

- Status: **INSUFFICIENT** | Best median: **S218** (+48.91%) | Best p10: **S219** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S216 | 3d ATM RSI x30 | 31 | -56.25 | -87.10 | -75.81 | 34 | 10 |
| S217 | 3d ATM RSI<25 bounce | 31 | -43.75 | -68.75 | -57.19 | 16 | 3 |
| S218 | 3d ATM BB lower touch | 52 | +48.91 | -73.54 | -52.61 | 28 | 7 |
| S219 | 3d ATM vol climax up | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Other

- Status: **OK** | Best median: **S173** (-31.51%) | Best p10: **S173** (-77.18%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S173 | MomRev | 415 | -31.51 | -77.18 | -62.95 | 0 | 0 |

## Strategy Pipeline Status

_Pipeline evaluation as of 2026-08-10. Auto-kill thresholds: median<-25% at n>=15, p10<-85%, WR<15% at n>=25. Promote: n>=30 median>0%._

| Strategy | Signal | n | Median% | WR% | Status | Days |
|----------|--------|---|---------|-----|--------|------|
| S163 | A1 GapDown ATM call EO | 0 | — | — | NEW | 20 |
| S164 | GapDown ATM 1-DTE — P2 | 6 | -65.67% | 0% | WATCH | 20 |
| S165 | GapDown long call 3 DT | 245 | -38.18% | 30% | INSUFFICIENT | 35 |
| S166 | GapDown strong call | 0 | — | — | NEW | 20 |
| S167 | GapDown long call 3 DT | 0 | — | — | NEW | 20 |
| S168 | GapDown ATM 5-DTE — P2 | 0 | — | — | NEW | 20 |
| S169 | BB Squeeze Breakout ca | 0 | — | — | NEW | 0 |
| S170 | Golden Pocket call 3 D | 0 | — | — | NEW | 0 |
| S171 | VWAP Reclaim call 3 DT | 0 | — | — | NEW | 0 |
| S172 | Trend Resumption call  | 0 | — | — | NEW | 0 |
| S173 | MomReversal long call | 415 | -31.51% | 37% | INSUFFICIENT | 35 |
| S174 | RubberBand long call E | 119 | -25.00% | 36% | INSUFFICIENT | 35 |
| S175 | Earnings Drift call 3  | 0 | — | — | NEW | 0 |
| S200 | GapDown_Aggressive | 0 | — | — | NEW | 0 |
| S201 | GapDown_Mild | 0 | — | — | NEW | 0 |
| S202 | GapDown_Monster | 6 | -64.75% | 0% | WATCH | 13 |
| S203 | GapUp_Fade | 33 | -54.00% | 12% | INSUFFICIENT | 14 |
| S204 | GapUp_Continuation | 0 | — | — | NEW | 0 |
| S205 | GapDown_HighVol | 0 | — | — | NEW | 0 |
| S206 | GapDown_WithTrend | 0 | — | — | NEW | 0 |
| S207 | GapDown_AtSupport | 37 | -47.06% | 5% | INSUFFICIENT | 14 |
| S208 | GapDown_AboveMA200 | 0 | — | — | NEW | 0 |
| S209 | GapDown_Recovery | 6 | -61.46% | 0% | WATCH | 12 |
| S210 | MA_Cross_8_21 | 50 | +10.79% | 56% | INSUFFICIENT | 14 |
| S211 | MA_Cross_21_50 | 22 | -24.36% | 23% | INSUFFICIENT | 14 |
| S212 | MA_Bounce_50 | 66 | -70.59% | 8% | INSUFFICIENT | 14 |
| S213 | MA_Bounce_200 | 0 | — | — | NEW | 0 |
| S214 | MA_Death_Cross | 0 | — | — | NEW | 0 |
| S215 | MA_Reclaim_200 | 0 | — | — | NEW | 0 |
| S216 | RSI_Oversold_Cross | 31 | -56.25% | 10% | INSUFFICIENT | 14 |
| S217 | RSI_25_Bounce | 31 | -43.75% | 45% | INSUFFICIENT | 14 |
| S218 | BB_Lower_Touch | 52 | +48.91% | 63% | INSUFFICIENT | 14 |
| S219 | Volume_Climax_Up | 0 | — | — | NEW | 0 |
| S220 | Pullback50 | 0 | — | — | NEW | 0 |
| S221 | GoldenPocket | 0 | — | — | NEW | 0 |
| S350 | GapDown_0DTE | 30 | +35.49% | 60% | INSUFFICIENT | 10 |
| S351 | GapDown_1DTE | 43 | -52.94% | 23% | INSUFFICIENT | 10 |
| S352 | GapDown_2DTE | 27 | +13.04% | 56% | INSUFFICIENT | 10 |
| S353 | GapDown_3DTE | 19 | -34.69% | 37% | INSUFFICIENT | 10 |
| S354 | GapDown_5DTE | 34 | -43.75% | 41% | INSUFFICIENT | 10 |
| S355 | GapDown_7DTE | 34 | -1.23% | 50% | INSUFFICIENT | 10 |
| S356 | GapDown_14DTE | 8 | +9.24% | 50% | WATCH | 10 |
| S357 | GapDown_21DTE | 18 | +55.07% | 78% | INSUFFICIENT | 10 |
| S358 | GapDown_30DTE | 2 | -51.39% | 0% | WATCH | 6 |
| S359 | RubberBand_0DTE | 23 | -46.67% | 17% | INSUFFICIENT | 7 |
| S360 | RubberBand_1DTE | 36 | -55.16% | 8% | INSUFFICIENT | 10 |
| S361 | RubberBand_2DTE | 30 | -7.50% | 47% | INSUFFICIENT | 10 |
| S362 | RubberBand_3DTE | 31 | +38.24% | 77% | INSUFFICIENT | 10 |
| S363 | RubberBand_5DTE | 22 | -23.36% | 50% | INSUFFICIENT | 7 |
| S364 | RubberBand_7DTE | 29 | +56.00% | 62% | INSUFFICIENT | 10 |
| S365 | RubberBand_14DTE | 7 | -51.61% | 29% | WATCH | 10 |
| S366 | RubberBand_21DTE | 8 | -55.19% | 0% | WATCH | 6 |
| S367 | RubberBand_30DTE | 2 | -38.20% | 0% | WATCH | 6 |
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
| S396 | GapDown_ITM2 | 1 | -82.19% | 0% | WATCH | 4 |
| S397 | GapDown_ITM1 | 12 | +47.52% | 75% | WATCH | 10 |
| S398 | GapDown_ATM | 36 | +26.15% | 56% | INSUFFICIENT | 10 |
| S399 | GapDown_OTM1 | 39 | -46.15% | 46% | INSUFFICIENT | 10 |
| S400 | Any_Green_Close | 5 | -50.00% | 0% | WATCH | 10 |
| S401 | Any_Gap_Down_Small | 59 | +23.68% | 59% | INSUFFICIENT | 10 |
| S402 | Any_High_Volume | 0 | — | — | NEW | 0 |
| S403 | Any_MA50_Touch | 21 | +50.00% | 62% | INSUFFICIENT | 10 |
| S404 | GapDown_OTM2 | 17 | +38.60% | 59% | INSUFFICIENT | 10 |
| S405 | GapDown_OTM3 | 41 | -22.50% | 44% | INSUFFICIENT | 10 |
| S406 | RubberBand_ITM3 | 50 | +66.13% | 60% | INSUFFICIENT | 10 |
| S407 | RubberBand_ITM2 | 31 | -51.43% | 35% | INSUFFICIENT | 10 |
| S408 | RubberBand_ITM1 | 37 | +41.94% | 54% | INSUFFICIENT | 7 |
| S409 | RubberBand_ATM | 0 | — | — | NEW | 0 |
| S410 | RubberBand_OTM1 | 3 | -68.49% | 33% | WATCH | 4 |
| S411 | RubberBand_OTM2 | 27 | +7.69% | 56% | INSUFFICIENT | 7 |
| S412 | RubberBand_OTM3 | 26 | -3.57% | 42% | INSUFFICIENT | 10 |
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
| S406 | 50 | +66.13% | 60% | Tyler review |
| S218 | 52 | +48.91% | 63% | Tyler review |
| S408 | 37 | +41.94% | 54% | Tyler review |
| S362 | 31 | +38.24% | 77% | Tyler review |
| S350 | 30 | +35.49% | 60% | Tyler review |
| S398 | 36 | +26.15% | 56% | Tyler review |
| S401 | 59 | +23.68% | 59% | Tyler review |
| S210 | 50 | +10.79% | 56% | Tyler review |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- **p25** sits between p10 and median for mid-tail visibility.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
- Active paper strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419.
