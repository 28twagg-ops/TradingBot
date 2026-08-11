# Options strategy selection report — 2026-08-11

_Generated 2026-08-11T15:34:35.924219_

## Summary

- Strategies analyzed: **105**
- Keep: **0**
- Watch: **80**
- Drop: **25**

## Attribution health

- Total exits: **2410**
- Orphan exits (b0/orphan_reconcile): **292**
- Orphan rate: **12.1%** (warn if >10%)
- **ALERT:** orphan_rate > 10% — check client_order_id tagging / fill attribution before trusting strategy P&L.

## Strategy scoreboard

| strategy | DTE | rec | exits | win% | med% | p10% | p25% | p90% | days live | ent 5d | exit 5d | realized $ | top share | rationale |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S406 (RubberBand_ITM3) | 3d | watch | 58 | 65.5 | +67.65 | -63.41 | -50.00 | +976.05 | 11 | 33 | 10 | $+3,081.00 | 22.4% | fat left tail (p10 < -45%) |
| S357 (GapDown_21DTE) | 21d | watch | 18 | 77.8 | +55.07 | -67.86 | +47.06 | +73.68 | 11 | 0 | 4 | $+323.00 | 44.4% | building sample (8-19 exits) |
| S397 (GapDown_ITM1) | 3d | watch | 16 | 81.2 | +54.46 | -74.71 | +39.91 | +115.57 | 11 | 18 | 4 | $+494.00 | 43.8% | building sample (8-19 exits) |
| S403 (Any_MA50_Touch) | 3d | watch | 24 | 66.7 | +50.88 | -79.49 | -53.41 | +316.00 | 11 | 28 | 10 | $+464.00 | 37.5% | fat left tail (p10 < -45%) |
| S404 (GapDown_OTM2) | 3d | watch | 24 | 70.8 | +48.14 | -96.23 | -91.67 | +102.05 | 11 | 18 | 7 | $+407.00 | 37.5% | fat left tail (p10 < -45%) |
| S218 (BB_Lower_Touch) | 3d ATM BB lower touch | watch | 57 | 59.6 | +45.71 | -72.37 | -52.50 | +166.67 | 15 | 28 | 10 | $+960.00 | 43.9% | fat left tail (p10 < -45%) |
| S362 (RubberBand_3DTE) | 3d | watch | 35 | 68.6 | +25.45 | -67.00 | -42.02 | +111.91 | 11 | 20 | 7 | $+1,036.00 | 37.1% | fat left tail (p10 < -45%) |
| S350 (GapDown_0DTE) | 0d | watch | 34 | 52.9 | +13.38 | -65.49 | -54.17 | +182.75 | 11 | 12 | 2 | $+447.00 | 38.2% | fat left tail (p10 < -45%) |
| S401 (Any_Gap_Down_Small) | 3d | watch | 80 | 52.5 | +8.97 | -93.89 | -50.24 | +166.73 | 11 | 52 | 34 | $+991.00 | 40.0% | fat left tail (p10 < -45%) |
| S210 (MA_Cross_8_21) | 3d ATM MA cross 8/21 | watch | 59 | 54.2 | +7.69 | -84.44 | -44.44 | +79.13 | 15 | 35 | 23 | $+34.00 | 25.4% | fat left tail (p10 < -45%) |
| S411 (RubberBand_OTM2) | 3d | watch | 28 | 57.1 | +7.69 | -57.17 | -52.08 | +40.33 | 8 | 10 | 1 | $-187.00 | 32.1% | fat left tail (p10 < -45%) |
| S163 (A1 GapDown ATM call EOD) | 7d ATM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 21 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | 3d ATM strong | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 21 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S167 (GapDown long call 3 DTE 1-OTM — P2C) | 3d 1-OTM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 21 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S168 (GapDown ATM 5-DTE — P2B arm) | 5d ATM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 21 | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
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
| S356 (GapDown_14DTE) | 14d | watch | 15 | 26.7 | -25.00 | -52.91 | -50.41 | +50.34 | 11 | 4 | 11 | $-136.00 | 40.0% | early sample with non-positive median |
| S367 (RubberBand_30DTE) | 30d | watch | 2 | 0.0 | -38.20 | -48.75 | -44.79 | -27.64 | 7 | 0 | 2 | $-55.00 | 100.0% | insufficient sample (<8 exits) |
| S365 (RubberBand_14DTE) | 14d | watch | 12 | 16.7 | -49.56 | -81.56 | -55.12 | +49.36 | 11 | 6 | 10 | $-186.00 | 50.0% | early sample with non-positive median |
| S400 (Any_Green_Close) | 3d | watch | 5 | 0.0 | -50.00 | -66.67 | -66.67 | -33.33 | 11 | 0 | 0 | $-30.00 | 100.0% | insufficient sample (<8 exits) |
| S358 (GapDown_30DTE) | 30d | watch | 3 | 33.3 | -51.39 | -51.39 | -51.39 | +33.80 | 7 | 4 | 3 | $-47.00 | 66.7% | insufficient sample (<8 exits) |
| S366 (RubberBand_21DTE) | 21d | watch | 8 | 0.0 | -55.19 | -58.31 | -56.92 | -49.12 | 7 | 0 | 8 | $-268.00 | 100.0% | early sample with non-positive median |
| S202 (GapDown_Monster) | 3d ATM gap-monster | watch | 10 | 0.0 | -60.53 | -74.54 | -66.39 | -37.62 | 14 | 10 | 4 | $-171.00 | 40.0% | early sample with non-positive median |
| S209 (GapDown_Recovery) | 3d ATM gap-recovery | watch | 6 | 0.0 | -61.46 | -82.78 | -69.36 | -50.75 | 13 | 0 | 2 | $-210.00 | 83.3% | insufficient sample (<8 exits) |
| S164 (GapDown ATM 1-DTE — P2B arm) | 1d ATM | watch | 6 | 0.0 | -65.67 | -88.89 | -86.11 | -50.00 | 21 | 0 | 0 | $-59.00 | 83.3% | insufficient sample (<8 exits) |
| S410 (RubberBand_OTM1) | 3d | watch | 3 | 33.3 | -68.49 | -76.16 | -73.28 | +67.49 | 5 | 0 | 3 | $-39.00 | 66.7% | insufficient sample (<8 exits) |
| S396 (GapDown_ITM2) | 3d | watch | 1 | 0.0 | -82.19 | -82.19 | -82.19 | -82.19 | 5 | 0 | 1 | $-60.00 | 100.0% | insufficient sample (<8 exits) |
| S408 (RubberBand_ITM1) | 3d | drop | 43 | 46.5 | +0.00 | -69.93 | -55.56 | +776.45 | 8 | 20 | 7 | $+1,095.00 | 23.3% | non-positive median return |
| S352 (GapDown_2DTE) | 2d | drop | 30 | 50.0 | -2.30 | -71.79 | -51.85 | +111.20 | 11 | 20 | 4 | $+85.00 | 30.0% | non-positive median return |
| S412 (RubberBand_OTM3) | 3d | drop | 29 | 37.9 | -3.57 | -52.51 | -23.26 | +86.75 | 11 | 21 | 3 | $-13.00 | 20.7% | non-positive median return |
| S398 (GapDown_ATM) | 3d | drop | 40 | 50.0 | -4.05 | -69.08 | -56.25 | +155.78 | 11 | 20 | 8 | $+645.00 | 37.5% | non-positive median return |
| S361 (RubberBand_2DTE) | 2d | drop | 34 | 47.1 | -7.50 | -70.72 | -53.62 | +110.15 | 11 | 20 | 0 | $-76.00 | 32.4% | non-positive median return |
| S174 (RubberBand long call EOD) | RubberBand (dropped) | drop | 119 | 36.1 | -25.00 | -89.83 | -71.19 | +36.67 | 36 | 0 | 0 | $-1,658.19 | 50.4% | manually paused — excluded from new entries & reflected P&L |
| S173 (MomReversal long call) | MomRev | drop | 415 | 37.1 | -31.51 | -77.18 | -62.95 | +101.90 | 36 | 0 | 0 | $+62.64 | 27.5% | manually paused — excluded from new entries & reflected P&L |
| S353 (GapDown_3DTE) | 3d | drop | 20 | 40.0 | -34.69 | -85.57 | -76.88 | +124.42 | 11 | 20 | 0 | $-46.00 | 45.0% | non-positive median return |
| S355 (GapDown_7DTE) | 7d | drop | 40 | 47.5 | -37.14 | -66.88 | -55.63 | +143.53 | 11 | 20 | 6 | $+369.00 | 27.5% | non-positive median return |
| S211 (MA_Cross_21_50) | 3d ATM MA cross 21/50 | drop | 29 | 24.1 | -38.10 | -96.36 | -51.47 | +88.20 | 15 | 20 | 9 | $-198.00 | 51.7% | non-positive median return |
| S165 (GapDown long call 3 DTE) | 3d ATM | drop | 245 | 29.8 | -38.18 | -63.39 | -54.55 | +81.82 | 36 | 0 | 0 | $-1,828.78 | 26.1% | non-positive median return |
| S405 (GapDown_OTM3) | 3d | drop | 49 | 36.7 | -41.46 | -80.03 | -58.46 | +101.39 | 11 | 20 | 11 | $+57.00 | 30.6% | non-positive median return |
| S364 (RubberBand_7DTE) | 7d | drop | 37 | 48.6 | -42.31 | -92.11 | -63.64 | +122.22 | 11 | 20 | 14 | $-70.00 | 32.4% | non-positive median return |
| S407 (RubberBand_ITM2) | 3d | drop | 36 | 30.6 | -45.45 | -76.58 | -61.54 | +291.25 | 11 | 28 | 3 | $+129.00 | 25.0% | non-positive median return |
| S399 (GapDown_OTM1) | 3d | drop | 40 | 45.0 | -46.41 | -83.51 | -66.67 | +141.00 | 11 | 20 | 0 | $+4.00 | 40.0% | non-positive median return |
| S359 (RubberBand_0DTE) | 0d | drop | 23 | 17.4 | -46.67 | -71.43 | -70.37 | +61.82 | 8 | 12 | 0 | $-323.00 | 43.5% | non-positive median return |
| S207 (GapDown_AtSupport) | 3d ATM gap-support | drop | 37 | 5.4 | -47.06 | -63.64 | -55.71 | -6.06 | 15 | 0 | 0 | $-822.00 | 43.2% | non-positive median return |
| S217 (RSI_25_Bounce) | 3d ATM RSI<25 bounce | drop | 37 | 37.8 | -50.00 | -80.50 | -60.00 | +181.90 | 15 | 16 | 9 | $+352.00 | 73.0% | non-positive median return |
| S216 (RSI_Oversold_Cross) | 3d ATM RSI x30 | drop | 35 | 20.0 | -52.63 | -84.46 | -71.24 | +168.86 | 15 | 28 | 7 | $-511.00 | 45.7% | non-positive median return |
| S203 (GapUp_Fade) | 3d ATM gap-up fade (put) | drop | 35 | 11.4 | -54.00 | -78.99 | -70.26 | +26.87 | 15 | 20 | 4 | $-743.00 | 40.0% | non-positive median return |
| S351 (GapDown_1DTE) | 1d | drop | 48 | 20.8 | -56.57 | -81.63 | -70.30 | +171.88 | 11 | 20 | 9 | $-268.00 | 27.1% | non-positive median return |
| S360 (RubberBand_1DTE) | 1d | drop | 44 | 9.1 | -56.77 | -81.55 | -70.37 | -25.00 | 11 | 30 | 8 | $-821.00 | 25.0% | non-positive median return |
| S354 (GapDown_5DTE) | 5d | drop | 43 | 32.6 | -63.89 | -92.16 | -76.47 | +138.47 | 11 | 17 | 16 | $+19.00 | 30.2% | non-positive median return |
| S212 (MA_Bounce_50) | 3d ATM MA bounce 50 | drop | 77 | 13.0 | -68.09 | -98.18 | -80.88 | +51.47 | 15 | 41 | 19 | $-2,159.00 | 37.7% | non-positive median return |
| S363 (RubberBand_5DTE) | 5d | drop | 29 | 37.9 | -72.31 | -92.31 | -88.46 | +61.43 | 8 | 18 | 18 | $-669.00 | 34.5% | non-positive median return |

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
| S202 | 3d ATM gap-monster | 10 | -60.53 | -74.54 | -66.39 | 10 | 4 |
| S204 | 3d ATM gap-up cont | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S205 | 3d ATM gap-highvol | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S206 | 3d ATM gap-trend | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S207 | 3d ATM gap-support | 37 | -47.06 | -63.64 | -55.71 | 0 | 0 |
| S208 | 3d ATM gap-ma200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S209 | 3d ATM gap-recovery | 6 | -61.46 | -82.78 | -69.36 | 0 | 2 |

### Phase-1 Bearish Gap & MA

- Status: **INSUFFICIENT** | Best median: **S214** (+0.00%) | Best p10: **S214** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S203 | 3d ATM gap-up fade (put) | 35 | -54.00 | -78.99 | -70.26 | 20 | 4 |
| S214 | 3d ATM death cross (put) | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 MA family

- Status: **INSUFFICIENT** | Best median: **S210** (+7.69%) | Best p10: **S213** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S210 | 3d ATM MA cross 8/21 | 59 | +7.69 | -84.44 | -44.44 | 35 | 23 |
| S211 | 3d ATM MA cross 21/50 | 29 | -38.10 | -96.36 | -51.47 | 20 | 9 |
| S212 | 3d ATM MA bounce 50 | 77 | -68.09 | -98.18 | -80.88 | 41 | 19 |
| S213 | 3d ATM MA bounce 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S215 | 3d ATM MA reclaim 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 RSI/BB/Vol

- Status: **INSUFFICIENT** | Best median: **S218** (+45.71%) | Best p10: **S219** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S216 | 3d ATM RSI x30 | 35 | -52.63 | -84.46 | -71.24 | 28 | 7 |
| S217 | 3d ATM RSI<25 bounce | 37 | -50.00 | -80.50 | -60.00 | 16 | 9 |
| S218 | 3d ATM BB lower touch | 57 | +45.71 | -72.37 | -52.50 | 28 | 10 |
| S219 | 3d ATM vol climax up | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Other

- Status: **OK** | Best median: **S173** (-31.51%) | Best p10: **S173** (-77.18%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S173 | MomRev | 415 | -31.51 | -77.18 | -62.95 | 0 | 0 |

## Strategy Pipeline Status

_Pipeline evaluation as of 2026-08-11. Auto-kill thresholds: median<-25% at n>=15, p10<-85%, WR<15% at n>=25. Promote: n>=30 median>0%._

| Strategy | Signal | n | Median% | WR% | Status | Days |
|----------|--------|---|---------|-----|--------|------|
| S163 | A1 GapDown ATM call EO | 0 | — | — | NEW | 21 |
| S164 | GapDown ATM 1-DTE — P2 | 6 | -65.67% | 0% | WATCH | 21 |
| S165 | GapDown long call 3 DT | 245 | -38.18% | 30% | INSUFFICIENT | 36 |
| S166 | GapDown strong call | 0 | — | — | NEW | 21 |
| S167 | GapDown long call 3 DT | 0 | — | — | NEW | 21 |
| S168 | GapDown ATM 5-DTE — P2 | 0 | — | — | NEW | 21 |
| S169 | BB Squeeze Breakout ca | 0 | — | — | NEW | 0 |
| S170 | Golden Pocket call 3 D | 0 | — | — | NEW | 0 |
| S171 | VWAP Reclaim call 3 DT | 0 | — | — | NEW | 0 |
| S172 | Trend Resumption call  | 0 | — | — | NEW | 0 |
| S173 | MomReversal long call | 415 | -31.51% | 37% | INSUFFICIENT | 36 |
| S174 | RubberBand long call E | 119 | -25.00% | 36% | INSUFFICIENT | 36 |
| S175 | Earnings Drift call 3  | 0 | — | — | NEW | 0 |
| S200 | GapDown_Aggressive | 0 | — | — | NEW | 0 |
| S201 | GapDown_Mild | 0 | — | — | NEW | 0 |
| S202 | GapDown_Monster | 10 | -60.53% | 0% | WATCH | 14 |
| S203 | GapUp_Fade | 35 | -54.00% | 11% | INSUFFICIENT | 15 |
| S204 | GapUp_Continuation | 0 | — | — | NEW | 0 |
| S205 | GapDown_HighVol | 0 | — | — | NEW | 0 |
| S206 | GapDown_WithTrend | 0 | — | — | NEW | 0 |
| S207 | GapDown_AtSupport | 37 | -47.06% | 5% | INSUFFICIENT | 15 |
| S208 | GapDown_AboveMA200 | 0 | — | — | NEW | 0 |
| S209 | GapDown_Recovery | 6 | -61.46% | 0% | WATCH | 13 |
| S210 | MA_Cross_8_21 | 59 | +7.69% | 54% | INSUFFICIENT | 15 |
| S211 | MA_Cross_21_50 | 29 | -38.10% | 24% | INSUFFICIENT | 15 |
| S212 | MA_Bounce_50 | 77 | -68.09% | 13% | INSUFFICIENT | 15 |
| S213 | MA_Bounce_200 | 0 | — | — | NEW | 0 |
| S214 | MA_Death_Cross | 0 | — | — | NEW | 0 |
| S215 | MA_Reclaim_200 | 0 | — | — | NEW | 0 |
| S216 | RSI_Oversold_Cross | 35 | -52.63% | 20% | INSUFFICIENT | 15 |
| S217 | RSI_25_Bounce | 37 | -50.00% | 38% | INSUFFICIENT | 15 |
| S218 | BB_Lower_Touch | 57 | +45.71% | 60% | INSUFFICIENT | 15 |
| S219 | Volume_Climax_Up | 0 | — | — | NEW | 0 |
| S220 | Pullback50 | 0 | — | — | NEW | 0 |
| S221 | GoldenPocket | 0 | — | — | NEW | 0 |
| S350 | GapDown_0DTE | 34 | +13.38% | 53% | INSUFFICIENT | 11 |
| S351 | GapDown_1DTE | 48 | -56.57% | 21% | INSUFFICIENT | 11 |
| S352 | GapDown_2DTE | 30 | -2.30% | 50% | INSUFFICIENT | 11 |
| S353 | GapDown_3DTE | 20 | -34.69% | 40% | INSUFFICIENT | 11 |
| S354 | GapDown_5DTE | 43 | -63.89% | 33% | INSUFFICIENT | 11 |
| S355 | GapDown_7DTE | 40 | -37.14% | 48% | INSUFFICIENT | 11 |
| S356 | GapDown_14DTE | 15 | -25.00% | 27% | INSUFFICIENT | 11 |
| S357 | GapDown_21DTE | 18 | +55.07% | 78% | INSUFFICIENT | 11 |
| S358 | GapDown_30DTE | 3 | -51.39% | 33% | WATCH | 7 |
| S359 | RubberBand_0DTE | 23 | -46.67% | 17% | INSUFFICIENT | 8 |
| S360 | RubberBand_1DTE | 44 | -56.77% | 9% | INSUFFICIENT | 11 |
| S361 | RubberBand_2DTE | 34 | -7.50% | 47% | INSUFFICIENT | 11 |
| S362 | RubberBand_3DTE | 35 | +25.45% | 69% | INSUFFICIENT | 11 |
| S363 | RubberBand_5DTE | 29 | -72.31% | 38% | INSUFFICIENT | 8 |
| S364 | RubberBand_7DTE | 37 | -42.31% | 49% | INSUFFICIENT | 11 |
| S365 | RubberBand_14DTE | 12 | -49.56% | 17% | WATCH | 11 |
| S366 | RubberBand_21DTE | 8 | -55.19% | 0% | WATCH | 7 |
| S367 | RubberBand_30DTE | 2 | -38.20% | 0% | WATCH | 7 |
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
| S396 | GapDown_ITM2 | 1 | -82.19% | 0% | WATCH | 5 |
| S397 | GapDown_ITM1 | 16 | +54.46% | 81% | INSUFFICIENT | 11 |
| S398 | GapDown_ATM | 40 | -4.05% | 50% | INSUFFICIENT | 11 |
| S399 | GapDown_OTM1 | 40 | -46.41% | 45% | INSUFFICIENT | 11 |
| S400 | Any_Green_Close | 5 | -50.00% | 0% | WATCH | 11 |
| S401 | Any_Gap_Down_Small | 80 | +8.97% | 52% | INSUFFICIENT | 11 |
| S402 | Any_High_Volume | 0 | — | — | NEW | 0 |
| S403 | Any_MA50_Touch | 24 | +50.88% | 67% | INSUFFICIENT | 11 |
| S404 | GapDown_OTM2 | 24 | +48.14% | 71% | INSUFFICIENT | 11 |
| S405 | GapDown_OTM3 | 49 | -41.46% | 37% | INSUFFICIENT | 11 |
| S406 | RubberBand_ITM3 | 58 | +67.65% | 66% | INSUFFICIENT | 11 |
| S407 | RubberBand_ITM2 | 36 | -45.45% | 31% | INSUFFICIENT | 11 |
| S408 | RubberBand_ITM1 | 43 | +0.00% | 47% | INSUFFICIENT | 8 |
| S409 | RubberBand_ATM | 0 | — | — | NEW | 0 |
| S410 | RubberBand_OTM1 | 3 | -68.49% | 33% | WATCH | 5 |
| S411 | RubberBand_OTM2 | 28 | +7.69% | 57% | INSUFFICIENT | 8 |
| S412 | RubberBand_OTM3 | 29 | -3.57% | 38% | INSUFFICIENT | 11 |
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
| S406 | 58 | +67.65% | 66% | Tyler review |
| S218 | 57 | +45.71% | 60% | Tyler review |
| S362 | 35 | +25.45% | 69% | Tyler review |
| S350 | 34 | +13.38% | 53% | Tyler review |
| S401 | 80 | +8.97% | 52% | Tyler review |
| S210 | 59 | +7.69% | 54% | Tyler review |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- **p25** sits between p10 and median for mid-tail visibility.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
- Active paper strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419.
