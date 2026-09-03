# Options strategy selection report — 2026-09-03

_Generated 2026-09-03T10:37:22.913062_

## Summary

- Strategies analyzed: **105**
- Keep: **0**
- Watch: **82**
- Drop: **23**

## Attribution health

- Total exits: **2696**
- Orphan exits (b0/orphan_reconcile): **348**
- Orphan rate: **12.9%** (warn if >10%)
- **ALERT:** orphan_rate > 10% — check client_order_id tagging / fill attribution before trusting strategy P&L.

## Strategy scoreboard

| strategy | DTE | rec | exits | win% | med% | p10% | p25% | p90% | days live | ent 5d | exit 5d | realized $ | top share | rationale |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S168 (GapDown ATM 5-DTE — P2B arm) | 5d ATM | watch | 2 | 100.0 | +137.84 | +122.70 | +128.38 | +152.98 | 44 | 10 | 2 | $+102.00 | 100.0% | insufficient sample (<8 exits) |
| S396 (GapDown_ITM2) | 3d | watch | 4 | 75.0 | +83.82 | -35.16 | +35.39 | +95.00 | 28 | 4 | 3 | $+120.00 | 100.0% | insufficient sample (<8 exits) |
| S163 (A1 GapDown ATM call EOD) | 7d ATM | watch | 3 | 100.0 | +81.08 | +81.08 | +81.08 | +118.71 | 44 | 10 | 3 | $+101.00 | 100.0% | insufficient sample (<8 exits) |
| S406 (RubberBand_ITM3) | 3d | watch | 67 | 68.7 | +72.41 | -63.41 | -28.19 | +965.79 | 34 | 10 | 7 | $+3,248.00 | 22.4% | fat left tail (p10 < -45%) |
| S357 (GapDown_21DTE) | 21d | watch | 22 | 81.8 | +55.04 | -61.08 | +47.06 | +73.68 | 34 | 6 | 4 | $+463.00 | 36.4% | fat left tail (p10 < -45%) |
| S397 (GapDown_ITM1) | 3d | watch | 24 | 79.2 | +54.46 | -81.28 | +33.74 | +116.09 | 34 | 10 | 2 | $+663.00 | 29.2% | fat left tail (p10 < -45%) |
| S403 (Any_MA50_Touch) | 3d | watch | 37 | 59.5 | +50.00 | -70.64 | -51.22 | +281.40 | 34 | 8 | 5 | $+586.00 | 24.3% | fat left tail (p10 < -45%) |
| S404 (GapDown_OTM2) | 3d | watch | 35 | 68.6 | +50.00 | -91.67 | -29.10 | +119.13 | 34 | 11 | 3 | $+676.00 | 25.7% | fat left tail (p10 < -45%) |
| S353 (GapDown_3DTE) | 3d | watch | 25 | 52.0 | +48.98 | -82.61 | -72.73 | +155.30 | 34 | 10 | 5 | $+95.00 | 36.0% | fat left tail (p10 < -45%) |
| S218 (BB_Lower_Touch) | 3d ATM BB lower touch | watch | 68 | 57.4 | +41.03 | -71.43 | -49.55 | +165.11 | 38 | 14 | 8 | $+1,130.00 | 36.8% | fat left tail (p10 < -45%) |
| S362 (RubberBand_3DTE) | 3d | watch | 39 | 71.8 | +38.24 | -62.33 | -30.43 | +116.00 | 34 | 10 | 4 | $+1,128.00 | 33.3% | fat left tail (p10 < -45%) |
| S350 (GapDown_0DTE) | 0d | watch | 35 | 51.4 | +11.76 | -65.10 | -54.17 | +179.86 | 34 | 4 | 0 | $+446.00 | 37.1% | fat left tail (p10 < -45%) |
| S410 (RubberBand_OTM1) | 3d | watch | 6 | 50.0 | +8.42 | -73.28 | -63.48 | +89.63 | 28 | 2 | 2 | $+33.00 | 83.3% | insufficient sample (<8 exits) |
| S401 (Any_Gap_Down_Small) | 3d | watch | 93 | 50.5 | +6.94 | -89.90 | -49.02 | +263.92 | 34 | 8 | 1 | $+1,056.00 | 34.4% | fat left tail (p10 < -45%) |
| S398 (GapDown_ATM) | 3d | watch | 44 | 52.3 | +3.33 | -68.29 | -56.25 | +157.11 | 34 | 6 | 2 | $+702.00 | 34.1% | fat left tail (p10 < -45%) |
| S364 (RubberBand_7DTE) | 7d | watch | 48 | 50.0 | +2.70 | -87.34 | -59.66 | +81.63 | 34 | 8 | 6 | $-91.00 | 35.4% | fat left tail (p10 < -45%) |
| S361 (RubberBand_2DTE) | 2d | watch | 37 | 51.4 | +1.85 | -69.78 | -53.62 | +108.76 | 34 | 8 | 3 | $-54.00 | 29.7% | fat left tail (p10 < -45%) |
| S358 (GapDown_30DTE) | 30d | watch | 4 | 50.0 | +0.84 | -51.39 | -51.39 | +54.49 | 30 | 0 | 0 | $-21.00 | 50.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | 3d ATM strong | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 44 | 4 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S167 (GapDown long call 3 DTE 1-OTM — P2C) | 3d 1-OTM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 44 | 6 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
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
| S356 (GapDown_14DTE) | 14d | watch | 18 | 27.8 | -23.31 | -52.29 | -50.00 | +53.99 | 34 | 2 | 1 | $-125.00 | 33.3% | early sample with non-positive median |
| S367 (RubberBand_30DTE) | 30d | watch | 2 | 0.0 | -38.20 | -48.75 | -44.79 | -27.64 | 30 | 0 | 0 | $-55.00 | 100.0% | insufficient sample (<8 exits) |
| S365 (RubberBand_14DTE) | 14d | watch | 15 | 33.3 | -48.33 | -75.48 | -52.00 | +63.64 | 34 | 6 | 3 | $-112.00 | 40.0% | early sample with non-positive median |
| S400 (Any_Green_Close) | 3d | watch | 6 | 16.7 | -50.00 | -66.67 | -62.50 | +14.93 | 34 | 0 | 0 | $-5.00 | 83.3% | insufficient sample (<8 exits) |
| S366 (RubberBand_21DTE) | 21d | watch | 10 | 20.0 | -52.59 | -57.38 | -56.92 | +76.67 | 30 | 6 | 2 | $-181.00 | 80.0% | early sample with non-positive median |
| S164 (GapDown ATM 1-DTE — P2B arm) | 1d ATM | watch | 7 | 0.0 | -53.57 | -88.89 | -83.34 | -49.23 | 44 | 6 | 1 | $-84.00 | 71.4% | insufficient sample (<8 exits) |
| S202 (GapDown_Monster) | 3d ATM gap-monster | watch | 10 | 0.0 | -60.53 | -74.54 | -66.39 | -37.62 | 37 | 0 | 0 | $-171.00 | 40.0% | early sample with non-positive median |
| S209 (GapDown_Recovery) | 3d ATM gap-recovery | watch | 6 | 0.0 | -61.46 | -82.78 | -69.36 | -50.75 | 36 | 0 | 0 | $-210.00 | 83.3% | insufficient sample (<8 exits) |
| S408 (RubberBand_ITM1) | 3d | drop | 45 | 48.9 | +0.00 | -69.49 | -55.56 | +746.23 | 31 | 4 | 2 | $+1,104.00 | 22.2% | non-positive median return |
| S411 (RubberBand_OTM2) | 3d | drop | 33 | 48.5 | +0.00 | -56.72 | -51.67 | +37.88 | 31 | 10 | 4 | $-321.00 | 27.3% | non-positive median return |
| S412 (RubberBand_OTM3) | 3d | drop | 36 | 47.2 | -2.90 | -51.79 | -23.26 | +114.15 | 34 | 10 | 7 | $+110.00 | 22.2% | non-positive median return |
| S210 (MA_Cross_8_21) | 3d ATM MA cross 8/21 | drop | 69 | 47.8 | -6.25 | -81.89 | -51.22 | +67.42 | 38 | 4 | 1 | $-161.00 | 21.7% | non-positive median return |
| S352 (GapDown_2DTE) | 2d | drop | 37 | 48.6 | -17.65 | -80.08 | -51.85 | +189.20 | 34 | 10 | 5 | $+27.00 | 29.7% | non-positive median return |
| S174 (RubberBand long call EOD) | RubberBand (dropped) | drop | 119 | 36.1 | -25.00 | -89.83 | -71.19 | +36.67 | 59 | 0 | 0 | $-1,658.19 | 50.4% | non-positive median return |
| S173 (MomReversal long call) | MomRev | drop | 415 | 37.1 | -31.51 | -77.18 | -62.95 | +101.90 | 59 | 0 | 0 | $+62.64 | 27.5% | non-positive median return |
| S211 (MA_Cross_21_50) | 3d ATM MA cross 21/50 | drop | 41 | 29.3 | -31.58 | -81.13 | -51.47 | +107.69 | 38 | 2 | 0 | $-203.00 | 36.6% | non-positive median return |
| S355 (GapDown_7DTE) | 7d | drop | 54 | 44.4 | -37.32 | -71.31 | -63.18 | +172.84 | 34 | 9 | 5 | $+333.00 | 29.6% | non-positive median return |
| S165 (GapDown long call 3 DTE) | 3d ATM | drop | 245 | 29.8 | -38.18 | -63.39 | -54.55 | +81.82 | 59 | 6 | 0 | $-1,828.78 | 26.1% | non-positive median return |
| S405 (GapDown_OTM3) | 3d | drop | 56 | 33.9 | -42.86 | -83.93 | -65.20 | +103.47 | 34 | 0 | 0 | $-118.00 | 26.8% | manually paused — excluded from new entries & reflected P&L |
| S399 (GapDown_OTM1) | 3d | drop | 46 | 45.7 | -46.41 | -84.09 | -66.67 | +145.00 | 34 | 11 | 3 | $-32.00 | 34.8% | non-positive median return |
| S359 (RubberBand_0DTE) | 0d | drop | 25 | 24.0 | -46.67 | -71.43 | -70.37 | +131.43 | 31 | 4 | 2 | $-304.00 | 40.0% | non-positive median return |
| S207 (GapDown_AtSupport) | 3d ATM gap-support | drop | 37 | 5.4 | -47.06 | -63.64 | -55.71 | -6.06 | 38 | 0 | 0 | $-822.00 | 43.2% | manually paused — excluded from new entries & reflected P&L |
| S407 (RubberBand_ITM2) | 3d | drop | 38 | 28.9 | -47.73 | -83.88 | -61.54 | +266.42 | 34 | 0 | 0 | $+33.00 | 26.3% | manually paused — excluded from new entries & reflected P&L |
| S217 (RSI_25_Bounce) | 3d ATM RSI<25 bounce | drop | 47 | 34.0 | -50.00 | -82.00 | -60.00 | +147.33 | 38 | 12 | 7 | $+237.00 | 63.8% | non-positive median return |
| S354 (GapDown_5DTE) | 5d | drop | 45 | 33.3 | -52.31 | -92.16 | -76.47 | +138.30 | 34 | 4 | 0 | $-7.00 | 31.1% | non-positive median return |
| S351 (GapDown_1DTE) | 1d | drop | 51 | 21.6 | -53.85 | -81.63 | -69.68 | +171.88 | 34 | 6 | 1 | $-274.00 | 25.5% | non-positive median return |
| S216 (RSI_Oversold_Cross) | 3d ATM RSI x30 | drop | 38 | 21.1 | -53.98 | -82.47 | -74.25 | +121.64 | 38 | 6 | 3 | $-517.00 | 42.1% | non-positive median return |
| S203 (GapUp_Fade) | 3d ATM gap-up fade (put) | drop | 40 | 10.0 | -55.91 | -78.77 | -67.43 | -3.10 | 38 | 2 | 1 | $-797.00 | 35.0% | manually paused — excluded from new entries & reflected P&L |
| S360 (RubberBand_1DTE) | 1d | drop | 49 | 10.2 | -56.41 | -81.50 | -70.37 | -6.89 | 34 | 0 | 0 | $-913.00 | 22.4% | manually paused — excluded from new entries & reflected P&L |
| S212 (MA_Bounce_50) | 3d ATM MA bounce 50 | drop | 83 | 13.3 | -68.09 | -98.15 | -81.35 | +51.47 | 38 | 0 | 0 | $-2,246.00 | 34.9% | manually paused — excluded from new entries & reflected P&L |
| S363 (RubberBand_5DTE) | 5d | drop | 32 | 40.6 | -68.84 | -92.31 | -88.94 | +87.99 | 31 | 2 | 2 | $-671.00 | 34.4% | non-positive median return |

## Comparison groups

Experiment arms grouped for side-by-side decisions. INSUFFICIENT if any arm has n<10 exits.

### GapDown DTE comparison

- Status: **INSUFFICIENT** | Best median: **S168** (+137.84%) | Best p10: **S168** (+122.70%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S163 | 7d ATM | 3 | +81.08 | +81.08 | +81.08 | 10 | 3 |
| S164 | 1d ATM | 7 | -53.57 | -88.89 | -83.34 | 6 | 1 |
| S165 | 3d ATM | 245 | -38.18 | -63.39 | -54.55 | 6 | 0 |
| S168 | 5d ATM | 2 | +137.84 | +122.70 | +128.38 | 10 | 2 |

### GapDown Strike comparison

- Status: **INSUFFICIENT** | Best median: **S167** (+0.00%) | Best p10: **S167** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S165 | 3d ATM | 245 | -38.18 | -63.39 | -54.55 | 6 | 0 |
| S167 | 3d 1-OTM | 0 | +0.00 | +0.00 | +0.00 | 6 | 0 |

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
| S210 | 3d ATM MA cross 8/21 | 69 | -6.25 | -81.89 | -51.22 | 4 | 1 |
| S211 | 3d ATM MA cross 21/50 | 41 | -31.58 | -81.13 | -51.47 | 2 | 0 |
| S212 | 3d ATM MA bounce 50 | 83 | -68.09 | -98.15 | -81.35 | 0 | 0 |
| S213 | 3d ATM MA bounce 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S215 | 3d ATM MA reclaim 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 RSI/BB/Vol

- Status: **INSUFFICIENT** | Best median: **S218** (+41.03%) | Best p10: **S219** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S216 | 3d ATM RSI x30 | 38 | -53.98 | -82.47 | -74.25 | 6 | 3 |
| S217 | 3d ATM RSI<25 bounce | 47 | -50.00 | -82.00 | -60.00 | 12 | 7 |
| S218 | 3d ATM BB lower touch | 68 | +41.03 | -71.43 | -49.55 | 14 | 8 |
| S219 | 3d ATM vol climax up | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Other

- Status: **OK** | Best median: **S173** (-31.51%) | Best p10: **S173** (-77.18%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S173 | MomRev | 415 | -31.51 | -77.18 | -62.95 | 0 | 0 |

## Strategy Pipeline Status

_Pipeline evaluation as of 2026-09-03. Auto-kill thresholds: median<-25% at n>=15, p10<-85%, WR<15% at n>=25. Promote: n>=30 median>0%._

| Strategy | Signal | n | Median% | WR% | Status | Days |
|----------|--------|---|---------|-----|--------|------|
| S163 | A1 GapDown ATM call EO | 3 | +81.08% | 100% | WATCH | 44 |
| S164 | GapDown ATM 1-DTE — P2 | 7 | -53.57% | 0% | WATCH | 44 |
| S165 | GapDown long call 3 DT | 245 | -38.18% | 30% | INSUFFICIENT | 59 |
| S166 | GapDown strong call | 0 | — | — | NEW | 44 |
| S167 | GapDown long call 3 DT | 0 | — | — | NEW | 44 |
| S168 | GapDown ATM 5-DTE — P2 | 2 | +137.84% | 100% | WATCH | 44 |
| S169 | BB Squeeze Breakout ca | 0 | — | — | NEW | 0 |
| S170 | Golden Pocket call 3 D | 0 | — | — | NEW | 0 |
| S171 | VWAP Reclaim call 3 DT | 0 | — | — | NEW | 0 |
| S172 | Trend Resumption call  | 0 | — | — | NEW | 0 |
| S173 | MomReversal long call | 415 | -31.51% | 37% | INSUFFICIENT | 59 |
| S174 | RubberBand long call E | 119 | -25.00% | 36% | INSUFFICIENT | 59 |
| S175 | Earnings Drift call 3  | 0 | — | — | NEW | 0 |
| S200 | GapDown_Aggressive | 0 | — | — | NEW | 0 |
| S201 | GapDown_Mild | 0 | — | — | NEW | 0 |
| S202 | GapDown_Monster | 10 | -60.53% | 0% | WATCH | 37 |
| S203 | GapUp_Fade | 40 | -55.91% | 10% | INSUFFICIENT | 38 |
| S204 | GapUp_Continuation | 0 | — | — | NEW | 0 |
| S205 | GapDown_HighVol | 0 | — | — | NEW | 0 |
| S206 | GapDown_WithTrend | 0 | — | — | NEW | 0 |
| S207 | GapDown_AtSupport | 37 | -47.06% | 5% | INSUFFICIENT | 38 |
| S208 | GapDown_AboveMA200 | 0 | — | — | NEW | 0 |
| S209 | GapDown_Recovery | 6 | -61.46% | 0% | WATCH | 36 |
| S210 | MA_Cross_8_21 | 69 | -6.25% | 48% | INSUFFICIENT | 38 |
| S211 | MA_Cross_21_50 | 41 | -31.58% | 29% | INSUFFICIENT | 38 |
| S212 | MA_Bounce_50 | 83 | -68.09% | 13% | INSUFFICIENT | 38 |
| S213 | MA_Bounce_200 | 0 | — | — | NEW | 0 |
| S214 | MA_Death_Cross | 0 | — | — | NEW | 0 |
| S215 | MA_Reclaim_200 | 0 | — | — | NEW | 0 |
| S216 | RSI_Oversold_Cross | 38 | -53.98% | 21% | INSUFFICIENT | 38 |
| S217 | RSI_25_Bounce | 47 | -50.00% | 34% | INSUFFICIENT | 38 |
| S218 | BB_Lower_Touch | 68 | +41.03% | 57% | INSUFFICIENT | 38 |
| S219 | Volume_Climax_Up | 0 | — | — | NEW | 0 |
| S220 | Pullback50 | 0 | — | — | NEW | 0 |
| S221 | GoldenPocket | 0 | — | — | NEW | 0 |
| S350 | GapDown_0DTE | 35 | +11.76% | 51% | INSUFFICIENT | 34 |
| S351 | GapDown_1DTE | 51 | -53.85% | 22% | INSUFFICIENT | 34 |
| S352 | GapDown_2DTE | 37 | -17.65% | 49% | INSUFFICIENT | 34 |
| S353 | GapDown_3DTE | 25 | +48.98% | 52% | INSUFFICIENT | 34 |
| S354 | GapDown_5DTE | 45 | -52.31% | 33% | INSUFFICIENT | 34 |
| S355 | GapDown_7DTE | 54 | -37.32% | 44% | INSUFFICIENT | 34 |
| S356 | GapDown_14DTE | 18 | -23.31% | 28% | INSUFFICIENT | 34 |
| S357 | GapDown_21DTE | 22 | +55.04% | 82% | INSUFFICIENT | 34 |
| S358 | GapDown_30DTE | 4 | +0.84% | 50% | WATCH | 30 |
| S359 | RubberBand_0DTE | 25 | -46.67% | 24% | INSUFFICIENT | 31 |
| S360 | RubberBand_1DTE | 49 | -56.41% | 10% | INSUFFICIENT | 34 |
| S361 | RubberBand_2DTE | 37 | +1.85% | 51% | INSUFFICIENT | 34 |
| S362 | RubberBand_3DTE | 39 | +38.24% | 72% | INSUFFICIENT | 34 |
| S363 | RubberBand_5DTE | 32 | -68.84% | 41% | INSUFFICIENT | 31 |
| S364 | RubberBand_7DTE | 48 | +2.70% | 50% | INSUFFICIENT | 34 |
| S365 | RubberBand_14DTE | 15 | -48.33% | 33% | INSUFFICIENT | 34 |
| S366 | RubberBand_21DTE | 10 | -52.59% | 20% | WATCH | 30 |
| S367 | RubberBand_30DTE | 2 | -38.20% | 0% | WATCH | 30 |
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
| S396 | GapDown_ITM2 | 4 | +83.82% | 75% | WATCH | 28 |
| S397 | GapDown_ITM1 | 24 | +54.46% | 79% | INSUFFICIENT | 34 |
| S398 | GapDown_ATM | 44 | +3.33% | 52% | INSUFFICIENT | 34 |
| S399 | GapDown_OTM1 | 46 | -46.41% | 46% | INSUFFICIENT | 34 |
| S400 | Any_Green_Close | 6 | -50.00% | 17% | WATCH | 34 |
| S401 | Any_Gap_Down_Small | 93 | +6.94% | 51% | INSUFFICIENT | 34 |
| S402 | Any_High_Volume | 0 | — | — | NEW | 0 |
| S403 | Any_MA50_Touch | 37 | +50.00% | 59% | INSUFFICIENT | 34 |
| S404 | GapDown_OTM2 | 35 | +50.00% | 69% | INSUFFICIENT | 34 |
| S405 | GapDown_OTM3 | 56 | -42.86% | 34% | INSUFFICIENT | 34 |
| S406 | RubberBand_ITM3 | 67 | +72.41% | 69% | INSUFFICIENT | 34 |
| S407 | RubberBand_ITM2 | 38 | -47.73% | 29% | INSUFFICIENT | 34 |
| S408 | RubberBand_ITM1 | 45 | +0.00% | 49% | INSUFFICIENT | 31 |
| S409 | RubberBand_ATM | 0 | — | — | NEW | 0 |
| S410 | RubberBand_OTM1 | 6 | +8.42% | 50% | WATCH | 28 |
| S411 | RubberBand_OTM2 | 33 | +0.00% | 48% | INSUFFICIENT | 31 |
| S412 | RubberBand_OTM3 | 36 | -2.90% | 47% | INSUFFICIENT | 34 |
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
| S406 | 67 | +72.41% | 69% | Tyler review |
| S403 | 37 | +50.00% | 59% | Tyler review |
| S404 | 35 | +50.00% | 69% | Tyler review |
| S218 | 68 | +41.03% | 57% | Tyler review |
| S362 | 39 | +38.24% | 72% | Tyler review |
| S350 | 35 | +11.76% | 51% | Tyler review |
| S401 | 93 | +6.94% | 51% | Tyler review |
| S398 | 44 | +3.33% | 52% | Tyler review |
| S364 | 48 | +2.70% | 50% | Tyler review |
| S361 | 37 | +1.85% | 51% | Tyler review |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- **p25** sits between p10 and median for mid-tail visibility.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
- Active paper strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419.
