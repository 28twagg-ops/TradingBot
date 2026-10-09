# Options strategy selection report — 2026-10-09

_Generated 2026-10-09T13:51:26.085682_

## Summary

- Strategies analyzed: **105**
- Keep: **0**
- Watch: **74**
- Drop: **31**

## Attribution health

- Total exits: **3626**
- Orphan exits (b0/orphan_reconcile): **422**
- Orphan rate: **11.6%** (warn if >10%)
- **ALERT:** orphan_rate > 10% — check client_order_id tagging / fill attribution before trusting strategy P&L.

## Strategy scoreboard

| strategy | DTE | rec | exits | win% | med% | p10% | p25% | p90% | days live | ent 5d | exit 5d | realized $ | top share | rationale |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S167 (GapDown long call 3 DTE 1-OTM — P2C) | 3d 1-OTM | watch | 18 | 61.1 | +113.53 | -62.01 | -55.36 | +383.16 | 80 | 2 | 2 | $+469.00 | 33.3% | building sample (8-19 exits) |
| S396 (GapDown_ITM2) | 3d | watch | 8 | 75.0 | +86.25 | -61.50 | +42.78 | +102.08 | 64 | 1 | 1 | $+274.00 | 87.5% | building sample (8-19 exits) |
| S409 (RubberBand_ATM) | 3d | watch | 2 | 100.0 | +81.94 | +79.72 | +80.56 | +84.17 | 15 | 0 | 0 | $+118.00 | 100.0% | insufficient sample (<8 exits) |
| S410 (RubberBand_OTM1) | 3d | watch | 10 | 70.0 | +67.85 | -69.45 | -23.48 | +101.51 | 64 | 0 | 0 | $+231.00 | 80.0% | building sample (8-19 exits) |
| S166 (GapDown strong call) | 3d ATM strong | watch | 11 | 72.7 | +67.21 | -88.24 | +2.78 | +160.87 | 80 | 1 | 1 | $+386.00 | 45.5% | building sample (8-19 exits) |
| S163 (A1 GapDown ATM call EOD) | 7d ATM | watch | 30 | 60.0 | +57.91 | -74.86 | -61.42 | +93.51 | 80 | 3 | 3 | $+415.00 | 40.0% | fat left tail (p10 < -45%) |
| S406 (RubberBand_ITM3) | 3d | watch | 116 | 64.7 | +55.75 | -55.78 | -44.06 | +528.57 | 70 | 10 | 10 | $+3,609.00 | 12.9% | fat left tail (p10 < -45%) |
| S168 (GapDown ATM 5-DTE — P2B arm) | 5d ATM | watch | 26 | 57.7 | +55.23 | -73.41 | -54.82 | +245.34 | 80 | 3 | 3 | $+482.00 | 50.0% | fat left tail (p10 < -45%) |
| S357 (GapDown_21DTE) | 21d | watch | 27 | 77.8 | +52.94 | -69.97 | +47.06 | +76.71 | 70 | 1 | 2 | $+539.00 | 29.6% | fat left tail (p10 < -45%) |
| S362 (RubberBand_3DTE) | 3d | watch | 61 | 67.2 | +52.63 | -60.00 | -50.82 | +323.81 | 70 | 2 | 2 | $+1,441.00 | 21.3% | fat left tail (p10 < -45%) |
| S397 (GapDown_ITM1) | 3d | watch | 45 | 64.4 | +51.39 | -65.28 | -53.97 | +118.39 | 70 | 2 | 2 | $+1,092.00 | 20.0% | fat left tail (p10 < -45%) |
| S403 (Any_MA50_Touch) | 3d | watch | 75 | 62.7 | +50.88 | -61.50 | -50.00 | +178.36 | 70 | 4 | 3 | $+1,301.00 | 16.0% | fat left tail (p10 < -45%) |
| S404 (GapDown_OTM2) | 3d | watch | 79 | 57.0 | +45.21 | -72.65 | -48.26 | +108.66 | 70 | 6 | 6 | $+1,128.00 | 12.7% | fat left tail (p10 < -45%) |
| S218 (BB_Lower_Touch) | 3d ATM BB lower touch | watch | 109 | 50.5 | +22.22 | -71.43 | -50.00 | +146.00 | 74 | 0 | 0 | $+1,086.00 | 27.5% | fat left tail (p10 < -45%) |
| S350 (GapDown_0DTE) | 0d | watch | 49 | 53.1 | +15.00 | -63.53 | -50.00 | +205.14 | 70 | 2 | 2 | $+849.00 | 26.5% | fat left tail (p10 < -45%) |
| S356 (GapDown_14DTE) | 14d | watch | 30 | 50.0 | +8.54 | -51.88 | -47.45 | +60.62 | 70 | 2 | 2 | $+110.00 | 36.7% | fat left tail (p10 < -45%) |
| S411 (RubberBand_OTM2) | 3d | watch | 53 | 54.7 | +7.69 | -57.37 | -51.39 | +64.52 | 67 | 2 | 2 | $-16.00 | 17.0% | fat left tail (p10 < -45%) |
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
| S413 (BBSqueeze_ITM3) | 0d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S414 (BBSqueeze_ITM2) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S415 (BBSqueeze_ITM1) | 7d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S416 (BBSqueeze_ATM) | 0d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S417 (BBSqueeze_OTM1) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S418 (BBSqueeze_OTM2) | 7d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S419 (BBSqueeze_OTM3) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S367 (RubberBand_30DTE) | 30d | watch | 3 | 0.0 | -48.89 | -50.89 | -50.14 | -29.78 | 66 | 0 | 0 | $-77.00 | 66.7% | insufficient sample (<8 exits) |
| S400 (Any_Green_Close) | 3d | watch | 6 | 16.7 | -50.00 | -66.67 | -62.50 | +14.93 | 70 | 0 | 0 | $-5.00 | 83.3% | insufficient sample (<8 exits) |
| S358 (GapDown_30DTE) | 30d | watch | 5 | 40.0 | -50.00 | -51.39 | -51.39 | +54.28 | 66 | 1 | 1 | $-49.00 | 40.0% | insufficient sample (<8 exits) |
| S209 (GapDown_Recovery) | 3d ATM gap-recovery | watch | 7 | 0.0 | -64.71 | -80.40 | -68.79 | -50.75 | 72 | 0 | 0 | $-212.00 | 71.4% | insufficient sample (<8 exits) |
| S401 (Any_Gap_Down_Small) | 3d | drop | 135 | 49.6 | +0.00 | -84.10 | -51.33 | +230.91 | 70 | 0 | 0 | $+928.00 | 23.7% | non-positive median return |
| S365 (RubberBand_14DTE) | 14d | drop | 35 | 48.6 | +0.00 | -64.10 | -52.00 | +71.21 | 70 | 1 | 2 | $+7.00 | 37.1% | non-positive median return |
| S210 (MA_Cross_8_21) | 3d ATM MA cross 8/21 | drop | 100 | 50.0 | -1.35 | -71.05 | -51.22 | +83.32 | 74 | 3 | 3 | $+180.00 | 17.0% | non-positive median return |
| S364 (RubberBand_7DTE) | 7d | drop | 65 | 49.2 | -2.94 | -85.29 | -63.64 | +87.59 | 70 | 2 | 2 | $+41.00 | 38.5% | non-positive median return |
| S412 (RubberBand_OTM3) | 3d | drop | 66 | 45.5 | -3.57 | -56.15 | -49.13 | +125.66 | 70 | 1 | 1 | $+200.00 | 18.2% | non-positive median return |
| S361 (RubberBand_2DTE) | 2d | drop | 63 | 49.2 | -4.26 | -66.67 | -53.52 | +278.89 | 70 | 1 | 1 | $+136.00 | 20.6% | non-positive median return |
| S408 (RubberBand_ITM1) | 3d | drop | 67 | 43.3 | -6.25 | -81.48 | -59.63 | +573.13 | 67 | 0 | 0 | $+1,137.00 | 17.9% | manually paused — excluded from new entries & reflected P&L |
| S398 (GapDown_ATM) | 3d | drop | 63 | 49.2 | -11.43 | -68.27 | -55.56 | +172.00 | 70 | 1 | 1 | $+796.00 | 25.4% | non-positive median return |
| S174 (RubberBand long call EOD) | RubberBand (dropped) | drop | 119 | 36.1 | -25.00 | -89.83 | -71.19 | +36.67 | 95 | 0 | 0 | $-1,658.19 | 50.4% | non-positive median return |
| S352 (GapDown_2DTE) | 2d | drop | 62 | 46.8 | -27.95 | -74.64 | -52.59 | +324.28 | 70 | 2 | 2 | $+255.00 | 17.7% | non-positive median return |
| S173 (MomReversal long call) | MomRev | drop | 415 | 37.1 | -31.51 | -77.18 | -62.95 | +101.90 | 95 | 0 | 0 | $+62.64 | 27.5% | non-positive median return |
| S165 (GapDown long call 3 DTE) | 3d ATM | drop | 255 | 32.2 | -35.29 | -63.24 | -53.42 | +93.89 | 95 | 0 | 0 | $-1,276.78 | 25.9% | non-positive median return |
| S355 (GapDown_7DTE) | 7d | drop | 71 | 45.1 | -37.50 | -77.08 | -63.70 | +138.64 | 70 | 0 | 0 | $+367.00 | 38.0% | manually paused — excluded from new entries & reflected P&L |
| S359 (RubberBand_0DTE) | 0d | drop | 41 | 43.9 | -39.29 | -71.43 | -63.16 | +228.57 | 67 | 2 | 2 | $+49.00 | 24.4% | non-positive median return |
| S405 (GapDown_OTM3) | 3d | drop | 56 | 33.9 | -42.86 | -83.93 | -65.20 | +103.47 | 70 | 0 | 0 | $-118.00 | 26.8% | manually paused — excluded from new entries & reflected P&L |
| S211 (MA_Cross_21_50) | 3d ATM MA cross 21/50 | drop | 56 | 23.2 | -43.65 | -86.66 | -54.73 | +95.51 | 74 | 0 | 0 | $-401.00 | 26.8% | manually paused — excluded from new entries & reflected P&L |
| S353 (GapDown_3DTE) | 3d | drop | 45 | 42.2 | -46.15 | -82.61 | -69.70 | +264.21 | 70 | 0 | 0 | $+125.00 | 22.2% | non-positive median return |
| S207 (GapDown_AtSupport) | 3d ATM gap-support | drop | 37 | 5.4 | -47.06 | -63.64 | -55.71 | -6.06 | 74 | 0 | 0 | $-822.00 | 43.2% | manually paused — excluded from new entries & reflected P&L |
| S407 (RubberBand_ITM2) | 3d | drop | 38 | 28.9 | -47.73 | -83.88 | -61.54 | +266.42 | 70 | 0 | 0 | $+33.00 | 26.3% | manually paused — excluded from new entries & reflected P&L |
| S164 (GapDown ATM 1-DTE — P2B arm) | 1d ATM | drop | 31 | 45.2 | -48.08 | -88.89 | -53.71 | +323.81 | 80 | 2 | 2 | $+411.00 | 19.4% | non-positive median return |
| S366 (RubberBand_21DTE) | 21d | drop | 21 | 42.9 | -49.12 | -56.92 | -53.45 | +94.34 | 66 | 0 | 0 | $-63.00 | 42.9% | manually paused — excluded from new entries & reflected P&L |
| S217 (RSI_25_Bounce) | 3d ATM RSI<25 bounce | drop | 75 | 33.3 | -49.18 | -79.00 | -60.00 | +99.05 | 74 | 0 | 0 | $+158.00 | 40.0% | manually paused — excluded from new entries & reflected P&L |
| S351 (GapDown_1DTE) | 1d | drop | 75 | 37.3 | -50.00 | -75.68 | -62.03 | +264.88 | 70 | 0 | 0 | $+414.00 | 17.3% | manually paused — excluded from new entries & reflected P&L |
| S399 (GapDown_OTM1) | 3d | drop | 80 | 38.8 | -50.72 | -83.55 | -66.67 | +141.00 | 70 | 0 | 0 | $-170.00 | 20.0% | non-positive median return |
| S354 (GapDown_5DTE) | 5d | drop | 66 | 36.4 | -51.96 | -84.87 | -75.26 | +135.12 | 70 | 0 | 0 | $+23.00 | 30.3% | manually paused — excluded from new entries & reflected P&L |
| S216 (RSI_Oversold_Cross) | 3d ATM RSI x30 | drop | 70 | 20.0 | -51.97 | -82.35 | -70.00 | +66.98 | 74 | 0 | 0 | $-1,020.00 | 22.9% | manually paused — excluded from new entries & reflected P&L |
| S203 (GapUp_Fade) | 3d ATM gap-up fade (put) | drop | 40 | 10.0 | -55.91 | -78.77 | -67.43 | -3.10 | 74 | 0 | 0 | $-797.00 | 35.0% | manually paused — excluded from new entries & reflected P&L |
| S360 (RubberBand_1DTE) | 1d | drop | 49 | 10.2 | -56.41 | -81.50 | -70.37 | -6.89 | 70 | 0 | 0 | $-913.00 | 22.4% | manually paused — excluded from new entries & reflected P&L |
| S202 (GapDown_Monster) | 3d ATM gap-monster | drop | 14 | 0.0 | -60.53 | -80.50 | -72.44 | -39.53 | 73 | 0 | 0 | $-237.00 | 28.6% | manually paused — excluded from new entries & reflected P&L |
| S363 (RubberBand_5DTE) | 5d | drop | 41 | 39.0 | -65.38 | -92.31 | -85.11 | +90.62 | 67 | 0 | 0 | $-739.00 | 31.7% | manually paused — excluded from new entries & reflected P&L |
| S212 (MA_Bounce_50) | 3d ATM MA bounce 50 | drop | 83 | 13.3 | -68.09 | -98.15 | -81.35 | +51.47 | 74 | 0 | 0 | $-2,246.00 | 34.9% | manually paused — excluded from new entries & reflected P&L |

## Comparison groups

Experiment arms grouped for side-by-side decisions. INSUFFICIENT if any arm has n<10 exits.

### GapDown DTE comparison

- Status: **OK** | Best median: **S163** (+57.91%) | Best p10: **S165** (-63.24%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S163 | 7d ATM | 30 | +57.91 | -74.86 | -61.42 | 3 | 3 |
| S164 | 1d ATM | 31 | -48.08 | -88.89 | -53.71 | 2 | 2 |
| S165 | 3d ATM | 255 | -35.29 | -63.24 | -53.42 | 0 | 0 |
| S168 | 5d ATM | 26 | +55.23 | -73.41 | -54.82 | 3 | 3 |

### GapDown Strike comparison

- Status: **OK** | Best median: **S167** (+113.53%) | Best p10: **S167** (-62.01%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S165 | 3d ATM | 255 | -35.29 | -63.24 | -53.42 | 0 | 0 |
| S167 | 3d 1-OTM | 18 | +113.53 | -62.01 | -55.36 | 2 | 2 |

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
| S202 | 3d ATM gap-monster | 14 | -60.53 | -80.50 | -72.44 | 0 | 0 |
| S204 | 3d ATM gap-up cont | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S205 | 3d ATM gap-highvol | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S206 | 3d ATM gap-trend | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S207 | 3d ATM gap-support | 37 | -47.06 | -63.64 | -55.71 | 0 | 0 |
| S208 | 3d ATM gap-ma200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S209 | 3d ATM gap-recovery | 7 | -64.71 | -80.40 | -68.79 | 0 | 0 |

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
| S210 | 3d ATM MA cross 8/21 | 100 | -1.35 | -71.05 | -51.22 | 3 | 3 |
| S211 | 3d ATM MA cross 21/50 | 56 | -43.65 | -86.66 | -54.73 | 0 | 0 |
| S212 | 3d ATM MA bounce 50 | 83 | -68.09 | -98.15 | -81.35 | 0 | 0 |
| S213 | 3d ATM MA bounce 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S215 | 3d ATM MA reclaim 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 RSI/BB/Vol

- Status: **INSUFFICIENT** | Best median: **S218** (+22.22%) | Best p10: **S219** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S216 | 3d ATM RSI x30 | 70 | -51.97 | -82.35 | -70.00 | 0 | 0 |
| S217 | 3d ATM RSI<25 bounce | 75 | -49.18 | -79.00 | -60.00 | 0 | 0 |
| S218 | 3d ATM BB lower touch | 109 | +22.22 | -71.43 | -50.00 | 0 | 0 |
| S219 | 3d ATM vol climax up | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Other

- Status: **OK** | Best median: **S173** (-31.51%) | Best p10: **S173** (-77.18%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S173 | MomRev | 415 | -31.51 | -77.18 | -62.95 | 0 | 0 |

## Strategy Pipeline Status

_Pipeline evaluation as of 2026-10-09. Auto-kill thresholds: median<-25% at n>=15, p10<-85%, WR<15% at n>=25. Promote: n>=30 median>0%._

| Strategy | Signal | n | Median% | WR% | Status | Days |
|----------|--------|---|---------|-----|--------|------|
| S163 | A1 GapDown ATM call EO | 30 | +57.91% | 60% | INSUFFICIENT | 80 |
| S164 | GapDown ATM 1-DTE — P2 | 31 | -48.08% | 45% | INSUFFICIENT | 80 |
| S165 | GapDown long call 3 DT | 255 | -35.29% | 32% | INSUFFICIENT | 95 |
| S166 | GapDown strong call | 11 | +67.21% | 73% | WATCH | 80 |
| S167 | GapDown long call 3 DT | 18 | +113.53% | 61% | INSUFFICIENT | 80 |
| S168 | GapDown ATM 5-DTE — P2 | 26 | +55.23% | 58% | INSUFFICIENT | 80 |
| S169 | BB Squeeze Breakout ca | 0 | — | — | NEW | 0 |
| S170 | Golden Pocket call 3 D | 0 | — | — | NEW | 0 |
| S171 | VWAP Reclaim call 3 DT | 0 | — | — | NEW | 0 |
| S172 | Trend Resumption call  | 0 | — | — | NEW | 0 |
| S173 | MomReversal long call | 415 | -31.51% | 37% | INSUFFICIENT | 95 |
| S174 | RubberBand long call E | 119 | -25.00% | 36% | INSUFFICIENT | 95 |
| S175 | Earnings Drift call 3  | 0 | — | — | NEW | 0 |
| S200 | GapDown_Aggressive | 0 | — | — | NEW | 0 |
| S201 | GapDown_Mild | 0 | — | — | NEW | 0 |
| S202 | GapDown_Monster | 14 | -60.53% | 0% | WATCH | 73 |
| S203 | GapUp_Fade | 40 | -55.91% | 10% | INSUFFICIENT | 74 |
| S204 | GapUp_Continuation | 0 | — | — | NEW | 0 |
| S205 | GapDown_HighVol | 0 | — | — | NEW | 0 |
| S206 | GapDown_WithTrend | 0 | — | — | NEW | 0 |
| S207 | GapDown_AtSupport | 37 | -47.06% | 5% | INSUFFICIENT | 74 |
| S208 | GapDown_AboveMA200 | 0 | — | — | NEW | 0 |
| S209 | GapDown_Recovery | 7 | -64.71% | 0% | WATCH | 72 |
| S210 | MA_Cross_8_21 | 100 | -1.35% | 50% | INSUFFICIENT | 74 |
| S211 | MA_Cross_21_50 | 56 | -43.65% | 23% | INSUFFICIENT | 74 |
| S212 | MA_Bounce_50 | 83 | -68.09% | 13% | INSUFFICIENT | 74 |
| S213 | MA_Bounce_200 | 0 | — | — | NEW | 0 |
| S214 | MA_Death_Cross | 0 | — | — | NEW | 0 |
| S215 | MA_Reclaim_200 | 0 | — | — | NEW | 0 |
| S216 | RSI_Oversold_Cross | 70 | -51.97% | 20% | INSUFFICIENT | 74 |
| S217 | RSI_25_Bounce | 75 | -49.18% | 33% | INSUFFICIENT | 74 |
| S218 | BB_Lower_Touch | 109 | +22.22% | 50% | INSUFFICIENT | 74 |
| S219 | Volume_Climax_Up | 0 | — | — | NEW | 0 |
| S220 | Pullback50 | 0 | — | — | NEW | 0 |
| S221 | GoldenPocket | 0 | — | — | NEW | 0 |
| S350 | GapDown_0DTE | 49 | +15.00% | 53% | INSUFFICIENT | 70 |
| S351 | GapDown_1DTE | 75 | -50.00% | 37% | INSUFFICIENT | 70 |
| S352 | GapDown_2DTE | 62 | -27.95% | 47% | INSUFFICIENT | 70 |
| S353 | GapDown_3DTE | 45 | -46.15% | 42% | INSUFFICIENT | 70 |
| S354 | GapDown_5DTE | 66 | -51.96% | 36% | INSUFFICIENT | 70 |
| S355 | GapDown_7DTE | 71 | -37.50% | 45% | INSUFFICIENT | 70 |
| S356 | GapDown_14DTE | 30 | +8.54% | 50% | INSUFFICIENT | 70 |
| S357 | GapDown_21DTE | 27 | +52.94% | 78% | INSUFFICIENT | 70 |
| S358 | GapDown_30DTE | 5 | -50.00% | 40% | WATCH | 66 |
| S359 | RubberBand_0DTE | 41 | -39.29% | 44% | INSUFFICIENT | 67 |
| S360 | RubberBand_1DTE | 49 | -56.41% | 10% | INSUFFICIENT | 70 |
| S361 | RubberBand_2DTE | 63 | -4.26% | 49% | INSUFFICIENT | 70 |
| S362 | RubberBand_3DTE | 61 | +52.63% | 67% | INSUFFICIENT | 70 |
| S363 | RubberBand_5DTE | 41 | -65.38% | 39% | INSUFFICIENT | 67 |
| S364 | RubberBand_7DTE | 65 | -2.94% | 49% | INSUFFICIENT | 70 |
| S365 | RubberBand_14DTE | 35 | +0.00% | 49% | INSUFFICIENT | 70 |
| S366 | RubberBand_21DTE | 21 | -49.12% | 43% | INSUFFICIENT | 66 |
| S367 | RubberBand_30DTE | 3 | -48.89% | 0% | WATCH | 66 |
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
| S396 | GapDown_ITM2 | 8 | +86.25% | 75% | WATCH | 64 |
| S397 | GapDown_ITM1 | 45 | +51.39% | 64% | INSUFFICIENT | 70 |
| S398 | GapDown_ATM | 63 | -11.43% | 49% | INSUFFICIENT | 70 |
| S399 | GapDown_OTM1 | 80 | -50.72% | 39% | INSUFFICIENT | 70 |
| S400 | Any_Green_Close | 6 | -50.00% | 17% | WATCH | 70 |
| S401 | Any_Gap_Down_Small | 135 | +0.00% | 50% | INSUFFICIENT | 70 |
| S402 | Any_High_Volume | 0 | — | — | NEW | 0 |
| S403 | Any_MA50_Touch | 75 | +50.88% | 63% | INSUFFICIENT | 70 |
| S404 | GapDown_OTM2 | 79 | +45.21% | 57% | INSUFFICIENT | 70 |
| S405 | GapDown_OTM3 | 56 | -42.86% | 34% | INSUFFICIENT | 70 |
| S406 | RubberBand_ITM3 | 116 | +55.75% | 65% | INSUFFICIENT | 70 |
| S407 | RubberBand_ITM2 | 38 | -47.73% | 29% | INSUFFICIENT | 70 |
| S408 | RubberBand_ITM1 | 67 | -6.25% | 43% | INSUFFICIENT | 67 |
| S409 | RubberBand_ATM | 2 | +81.94% | 100% | WATCH | 15 |
| S410 | RubberBand_OTM1 | 10 | +67.85% | 70% | WATCH | 64 |
| S411 | RubberBand_OTM2 | 53 | +7.69% | 55% | INSUFFICIENT | 67 |
| S412 | RubberBand_OTM3 | 66 | -3.57% | 45% | INSUFFICIENT | 70 |
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
| S163 | 30 | +57.91% | 60% | Tyler review |
| S406 | 116 | +55.75% | 65% | Tyler review |
| S362 | 61 | +52.63% | 67% | Tyler review |
| S397 | 45 | +51.39% | 64% | Tyler review |
| S403 | 75 | +50.88% | 63% | Tyler review |
| S404 | 79 | +45.21% | 57% | Tyler review |
| S218 | 109 | +22.22% | 50% | Tyler review |
| S350 | 49 | +15.00% | 53% | Tyler review |
| S356 | 30 | +8.54% | 50% | Tyler review |
| S411 | 53 | +7.69% | 55% | Tyler review |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- **p25** sits between p10 and median for mid-tail visibility.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
- Active paper strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419.
