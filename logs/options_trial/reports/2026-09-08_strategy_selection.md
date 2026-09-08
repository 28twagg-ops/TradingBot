# Options strategy selection report — 2026-09-08

_Generated 2026-09-08T10:37:24.718971_

## Summary

- Strategies analyzed: **105**
- Keep: **0**
- Watch: **83**
- Drop: **22**

## Attribution health

- Total exits: **2833**
- Orphan exits (b0/orphan_reconcile): **353**
- Orphan rate: **12.5%** (warn if >10%)
- **ALERT:** orphan_rate > 10% — check client_order_id tagging / fill attribution before trusting strategy P&L.

## Strategy scoreboard

| strategy | DTE | rec | exits | win% | med% | p10% | p25% | p90% | days live | ent 5d | exit 5d | realized $ | top share | rationale |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S167 (GapDown long call 3 DTE 1-OTM — P2C) | 3d 1-OTM | watch | 4 | 100.0 | +318.26 | +112.00 | +121.00 | +525.26 | 49 | 10 | 0 | $+314.00 | 50.0% | insufficient sample (<8 exits) |
| S168 (GapDown ATM 5-DTE — P2B arm) | 5d ATM | watch | 10 | 100.0 | +137.84 | +53.00 | +106.08 | +257.23 | 49 | 11 | 2 | $+584.00 | 60.0% | building sample (8-19 exits) |
| S396 (GapDown_ITM2) | 3d | watch | 4 | 75.0 | +83.82 | -35.16 | +35.39 | +95.00 | 33 | 2 | 0 | $+120.00 | 100.0% | insufficient sample (<8 exits) |
| S163 (A1 GapDown ATM call EOD) | 7d ATM | watch | 9 | 100.0 | +82.76 | +71.35 | +81.08 | +201.14 | 49 | 8 | 0 | $+394.00 | 55.6% | building sample (8-19 exits) |
| S353 (GapDown_3DTE) | 3d | watch | 27 | 55.6 | +78.95 | -81.60 | -71.22 | +246.32 | 39 | 6 | 0 | $+213.00 | 33.3% | fat left tail (p10 < -45%) |
| S166 (GapDown strong call) | 3d ATM strong | watch | 7 | 100.0 | +77.59 | +62.55 | +70.04 | +205.71 | 49 | 5 | 1 | $+394.00 | 71.4% | insufficient sample (<8 exits) |
| S406 (RubberBand_ITM3) | 3d | watch | 69 | 69.6 | +72.55 | -63.41 | -6.38 | +972.63 | 39 | 8 | 0 | $+3,382.00 | 21.7% | fat left tail (p10 < -45%) |
| S397 (GapDown_ITM1) | 3d | watch | 29 | 75.9 | +57.53 | -70.11 | +19.15 | +115.58 | 39 | 10 | 2 | $+757.00 | 24.1% | fat left tail (p10 < -45%) |
| S362 (RubberBand_3DTE) | 3d | watch | 43 | 74.4 | +57.14 | -59.71 | -10.87 | +725.71 | 39 | 4 | 0 | $+1,359.00 | 30.2% | fat left tail (p10 < -45%) |
| S357 (GapDown_21DTE) | 21d | watch | 24 | 79.2 | +55.04 | -76.29 | +47.06 | +78.98 | 39 | 4 | 1 | $+490.00 | 33.3% | fat left tail (p10 < -45%) |
| S403 (Any_MA50_Touch) | 3d | watch | 44 | 65.9 | +50.93 | -63.07 | -49.10 | +236.83 | 39 | 8 | 2 | $+890.00 | 20.5% | fat left tail (p10 < -45%) |
| S404 (GapDown_OTM2) | 3d | watch | 45 | 64.4 | +50.00 | -91.67 | -41.89 | +117.95 | 39 | 13 | 5 | $+789.00 | 20.0% | fat left tail (p10 < -45%) |
| S361 (RubberBand_2DTE) | 2d | watch | 41 | 56.1 | +44.83 | -68.52 | -53.33 | +253.33 | 39 | 4 | 0 | $+212.00 | 26.8% | fat left tail (p10 < -45%) |
| S218 (BB_Lower_Touch) | 3d ATM BB lower touch | watch | 69 | 56.5 | +36.36 | -71.43 | -48.57 | +164.89 | 43 | 6 | 1 | $+1,111.00 | 36.2% | fat left tail (p10 < -45%) |
| S364 (RubberBand_7DTE) | 7d | watch | 50 | 52.0 | +23.90 | -85.97 | -57.98 | +188.89 | 39 | 2 | 0 | $+92.00 | 38.0% | fat left tail (p10 < -45%) |
| S350 (GapDown_0DTE) | 0d | watch | 39 | 56.4 | +17.65 | -63.53 | -52.09 | +260.00 | 39 | 10 | 0 | $+764.00 | 33.3% | fat left tail (p10 < -45%) |
| S352 (GapDown_2DTE) | 2d | watch | 40 | 52.5 | +13.04 | -76.27 | -51.85 | +342.77 | 39 | 6 | 2 | $+176.00 | 27.5% | fat left tail (p10 < -45%) |
| S401 (Any_Gap_Down_Small) | 3d | watch | 96 | 52.1 | +8.97 | -83.94 | -48.74 | +273.08 | 39 | 12 | 2 | $+1,209.00 | 33.3% | fat left tail (p10 < -45%) |
| S410 (RubberBand_OTM1) | 3d | watch | 6 | 50.0 | +8.42 | -73.28 | -63.48 | +89.63 | 33 | 2 | 0 | $+33.00 | 83.3% | insufficient sample (<8 exits) |
| S398 (GapDown_ATM) | 3d | watch | 47 | 53.2 | +3.33 | -68.29 | -55.00 | +156.45 | 39 | 10 | 1 | $+760.00 | 31.9% | fat left tail (p10 < -45%) |
| S358 (GapDown_30DTE) | 30d | watch | 4 | 50.0 | +0.84 | -51.39 | -51.39 | +54.49 | 35 | 0 | 0 | $-21.00 | 50.0% | insufficient sample (<8 exits) |
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
| S356 (GapDown_14DTE) | 14d | watch | 19 | 31.6 | -21.62 | -52.08 | -50.00 | +58.62 | 39 | 9 | 0 | $-81.00 | 31.6% | early sample with non-positive median |
| S365 (RubberBand_14DTE) | 14d | watch | 16 | 37.5 | -24.16 | -73.45 | -51.80 | +65.47 | 39 | 8 | 0 | $-77.00 | 37.5% | early sample with non-positive median |
| S367 (RubberBand_30DTE) | 30d | watch | 2 | 0.0 | -38.20 | -48.75 | -44.79 | -27.64 | 35 | 0 | 0 | $-55.00 | 100.0% | insufficient sample (<8 exits) |
| S164 (GapDown ATM 1-DTE — P2B arm) | 1d ATM | watch | 11 | 36.4 | -50.00 | -88.89 | -65.67 | +531.58 | 49 | 16 | 0 | $+260.00 | 45.5% | early sample with non-positive median |
| S400 (Any_Green_Close) | 3d | watch | 6 | 16.7 | -50.00 | -66.67 | -62.50 | +14.93 | 39 | 0 | 0 | $-5.00 | 83.3% | insufficient sample (<8 exits) |
| S366 (RubberBand_21DTE) | 21d | watch | 12 | 33.3 | -50.42 | -56.92 | -56.92 | +95.91 | 35 | 4 | 2 | $-77.00 | 66.7% | early sample with non-positive median |
| S202 (GapDown_Monster) | 3d ATM gap-monster | watch | 12 | 0.0 | -56.77 | -73.59 | -65.84 | -38.58 | 42 | 6 | 2 | $-208.00 | 33.3% | early sample with non-positive median |
| S209 (GapDown_Recovery) | 3d ATM gap-recovery | watch | 6 | 0.0 | -61.46 | -82.78 | -69.36 | -50.75 | 41 | 0 | 0 | $-210.00 | 83.3% | insufficient sample (<8 exits) |
| S408 (RubberBand_ITM1) | 3d | drop | 47 | 46.8 | +0.00 | -69.06 | -57.13 | +716.00 | 36 | 6 | 2 | $+1,100.00 | 21.3% | non-positive median return |
| S411 (RubberBand_OTM2) | 3d | drop | 33 | 48.5 | +0.00 | -56.72 | -51.67 | +37.88 | 36 | 6 | 0 | $-321.00 | 27.3% | non-positive median return |
| S412 (RubberBand_OTM3) | 3d | drop | 36 | 47.2 | -2.90 | -51.79 | -23.26 | +114.15 | 39 | 6 | 0 | $+110.00 | 22.2% | non-positive median return |
| S210 (MA_Cross_8_21) | 3d ATM MA cross 8/21 | drop | 72 | 48.6 | -5.30 | -80.79 | -50.83 | +63.95 | 43 | 6 | 2 | $-122.00 | 20.8% | non-positive median return |
| S399 (GapDown_OTM1) | 3d | drop | 55 | 49.1 | -17.24 | -84.36 | -66.67 | +183.89 | 39 | 11 | 2 | $+148.00 | 29.1% | non-positive median return |
| S174 (RubberBand long call EOD) | RubberBand (dropped) | drop | 119 | 36.1 | -25.00 | -89.83 | -71.19 | +36.67 | 64 | 0 | 0 | $-1,658.19 | 50.4% | non-positive median return |
| S355 (GapDown_7DTE) | 7d | drop | 58 | 48.3 | -26.38 | -69.85 | -61.88 | +189.38 | 39 | 6 | 1 | $+517.00 | 29.3% | non-positive median return |
| S173 (MomReversal long call) | MomRev | drop | 415 | 37.1 | -31.51 | -77.18 | -62.95 | +101.90 | 64 | 0 | 0 | $+62.64 | 27.5% | non-positive median return |
| S165 (GapDown long call 3 DTE) | 3d ATM | drop | 249 | 30.9 | -38.00 | -63.29 | -53.52 | +84.90 | 64 | 10 | 0 | $-1,526.78 | 26.5% | non-positive median return |
| S211 (MA_Cross_21_50) | 3d ATM MA cross 21/50 | drop | 43 | 27.9 | -38.10 | -80.62 | -55.60 | +102.82 | 43 | 0 | 0 | $-207.00 | 34.9% | non-positive median return |
| S405 (GapDown_OTM3) | 3d | drop | 56 | 33.9 | -42.86 | -83.93 | -65.20 | +103.47 | 39 | 0 | 0 | $-118.00 | 26.8% | manually paused — excluded from new entries & reflected P&L |
| S359 (RubberBand_0DTE) | 0d | drop | 28 | 28.6 | -45.55 | -71.43 | -68.91 | +178.57 | 36 | 8 | 1 | $-178.00 | 35.7% | non-positive median return |
| S217 (RSI_25_Bounce) | 3d ATM RSI<25 bounce | drop | 54 | 38.9 | -46.15 | -79.25 | -58.01 | +133.53 | 43 | 6 | 3 | $+402.00 | 55.6% | non-positive median return |
| S207 (GapDown_AtSupport) | 3d ATM gap-support | drop | 37 | 5.4 | -47.06 | -63.64 | -55.71 | -6.06 | 43 | 0 | 0 | $-822.00 | 43.2% | manually paused — excluded from new entries & reflected P&L |
| S407 (RubberBand_ITM2) | 3d | drop | 38 | 28.9 | -47.73 | -83.88 | -61.54 | +266.42 | 39 | 0 | 0 | $+33.00 | 26.3% | manually paused — excluded from new entries & reflected P&L |
| S354 (GapDown_5DTE) | 5d | drop | 51 | 41.2 | -50.77 | -92.16 | -75.99 | +137.78 | 39 | 6 | 0 | $+220.00 | 27.5% | non-positive median return |
| S351 (GapDown_1DTE) | 1d | drop | 56 | 26.8 | -52.55 | -78.66 | -68.17 | +261.46 | 39 | 16 | 1 | $+101.00 | 23.2% | non-positive median return |
| S216 (RSI_Oversold_Cross) | 3d ATM RSI x30 | drop | 38 | 21.1 | -53.98 | -82.47 | -74.25 | +121.64 | 43 | 4 | 0 | $-517.00 | 42.1% | non-positive median return |
| S203 (GapUp_Fade) | 3d ATM gap-up fade (put) | drop | 40 | 10.0 | -55.91 | -78.77 | -67.43 | -3.10 | 43 | 0 | 0 | $-797.00 | 35.0% | manually paused — excluded from new entries & reflected P&L |
| S360 (RubberBand_1DTE) | 1d | drop | 49 | 10.2 | -56.41 | -81.50 | -70.37 | -6.89 | 39 | 0 | 0 | $-913.00 | 22.4% | manually paused — excluded from new entries & reflected P&L |
| S212 (MA_Bounce_50) | 3d ATM MA bounce 50 | drop | 83 | 13.3 | -68.09 | -98.15 | -81.35 | +51.47 | 43 | 0 | 0 | $-2,246.00 | 34.9% | manually paused — excluded from new entries & reflected P&L |
| S363 (RubberBand_5DTE) | 5d | drop | 32 | 40.6 | -68.84 | -92.31 | -88.94 | +87.99 | 36 | 2 | 0 | $-671.00 | 34.4% | non-positive median return |

## Comparison groups

Experiment arms grouped for side-by-side decisions. INSUFFICIENT if any arm has n<10 exits.

### GapDown DTE comparison

- Status: **INSUFFICIENT** | Best median: **S168** (+137.84%) | Best p10: **S163** (+71.35%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S163 | 7d ATM | 9 | +82.76 | +71.35 | +81.08 | 8 | 0 |
| S164 | 1d ATM | 11 | -50.00 | -88.89 | -65.67 | 16 | 0 |
| S165 | 3d ATM | 249 | -38.00 | -63.29 | -53.52 | 10 | 0 |
| S168 | 5d ATM | 10 | +137.84 | +53.00 | +106.08 | 11 | 2 |

### GapDown Strike comparison

- Status: **INSUFFICIENT** | Best median: **S167** (+318.26%) | Best p10: **S167** (+112.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S165 | 3d ATM | 249 | -38.00 | -63.29 | -53.52 | 10 | 0 |
| S167 | 3d 1-OTM | 4 | +318.26 | +112.00 | +121.00 | 10 | 0 |

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
| S210 | 3d ATM MA cross 8/21 | 72 | -5.30 | -80.79 | -50.83 | 6 | 2 |
| S211 | 3d ATM MA cross 21/50 | 43 | -38.10 | -80.62 | -55.60 | 0 | 0 |
| S212 | 3d ATM MA bounce 50 | 83 | -68.09 | -98.15 | -81.35 | 0 | 0 |
| S213 | 3d ATM MA bounce 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S215 | 3d ATM MA reclaim 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 RSI/BB/Vol

- Status: **INSUFFICIENT** | Best median: **S218** (+36.36%) | Best p10: **S219** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S216 | 3d ATM RSI x30 | 38 | -53.98 | -82.47 | -74.25 | 4 | 0 |
| S217 | 3d ATM RSI<25 bounce | 54 | -46.15 | -79.25 | -58.01 | 6 | 3 |
| S218 | 3d ATM BB lower touch | 69 | +36.36 | -71.43 | -48.57 | 6 | 1 |
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
| S163 | A1 GapDown ATM call EO | 9 | +82.76% | 100% | WATCH | 49 |
| S164 | GapDown ATM 1-DTE — P2 | 11 | -50.00% | 36% | WATCH | 49 |
| S165 | GapDown long call 3 DT | 249 | -38.00% | 31% | INSUFFICIENT | 64 |
| S166 | GapDown strong call | 7 | +77.59% | 100% | WATCH | 49 |
| S167 | GapDown long call 3 DT | 4 | +318.26% | 100% | WATCH | 49 |
| S168 | GapDown ATM 5-DTE — P2 | 10 | +137.84% | 100% | WATCH | 49 |
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
| S210 | MA_Cross_8_21 | 72 | -5.30% | 49% | INSUFFICIENT | 43 |
| S211 | MA_Cross_21_50 | 43 | -38.10% | 28% | INSUFFICIENT | 43 |
| S212 | MA_Bounce_50 | 83 | -68.09% | 13% | INSUFFICIENT | 43 |
| S213 | MA_Bounce_200 | 0 | — | — | NEW | 0 |
| S214 | MA_Death_Cross | 0 | — | — | NEW | 0 |
| S215 | MA_Reclaim_200 | 0 | — | — | NEW | 0 |
| S216 | RSI_Oversold_Cross | 38 | -53.98% | 21% | INSUFFICIENT | 43 |
| S217 | RSI_25_Bounce | 54 | -46.15% | 39% | INSUFFICIENT | 43 |
| S218 | BB_Lower_Touch | 69 | +36.36% | 57% | INSUFFICIENT | 43 |
| S219 | Volume_Climax_Up | 0 | — | — | NEW | 0 |
| S220 | Pullback50 | 0 | — | — | NEW | 0 |
| S221 | GoldenPocket | 0 | — | — | NEW | 0 |
| S350 | GapDown_0DTE | 39 | +17.65% | 56% | INSUFFICIENT | 39 |
| S351 | GapDown_1DTE | 56 | -52.55% | 27% | INSUFFICIENT | 39 |
| S352 | GapDown_2DTE | 40 | +13.04% | 52% | INSUFFICIENT | 39 |
| S353 | GapDown_3DTE | 27 | +78.95% | 56% | INSUFFICIENT | 39 |
| S354 | GapDown_5DTE | 51 | -50.77% | 41% | INSUFFICIENT | 39 |
| S355 | GapDown_7DTE | 58 | -26.38% | 48% | INSUFFICIENT | 39 |
| S356 | GapDown_14DTE | 19 | -21.62% | 32% | INSUFFICIENT | 39 |
| S357 | GapDown_21DTE | 24 | +55.04% | 79% | INSUFFICIENT | 39 |
| S358 | GapDown_30DTE | 4 | +0.84% | 50% | WATCH | 35 |
| S359 | RubberBand_0DTE | 28 | -45.55% | 29% | INSUFFICIENT | 36 |
| S360 | RubberBand_1DTE | 49 | -56.41% | 10% | INSUFFICIENT | 39 |
| S361 | RubberBand_2DTE | 41 | +44.83% | 56% | INSUFFICIENT | 39 |
| S362 | RubberBand_3DTE | 43 | +57.14% | 74% | INSUFFICIENT | 39 |
| S363 | RubberBand_5DTE | 32 | -68.84% | 41% | INSUFFICIENT | 36 |
| S364 | RubberBand_7DTE | 50 | +23.90% | 52% | INSUFFICIENT | 39 |
| S365 | RubberBand_14DTE | 16 | -24.16% | 38% | INSUFFICIENT | 39 |
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
| S398 | GapDown_ATM | 47 | +3.33% | 53% | INSUFFICIENT | 39 |
| S399 | GapDown_OTM1 | 55 | -17.24% | 49% | INSUFFICIENT | 39 |
| S400 | Any_Green_Close | 6 | -50.00% | 17% | WATCH | 39 |
| S401 | Any_Gap_Down_Small | 96 | +8.97% | 52% | INSUFFICIENT | 39 |
| S402 | Any_High_Volume | 0 | — | — | NEW | 0 |
| S403 | Any_MA50_Touch | 44 | +50.93% | 66% | INSUFFICIENT | 39 |
| S404 | GapDown_OTM2 | 45 | +50.00% | 64% | INSUFFICIENT | 39 |
| S405 | GapDown_OTM3 | 56 | -42.86% | 34% | INSUFFICIENT | 39 |
| S406 | RubberBand_ITM3 | 69 | +72.55% | 70% | INSUFFICIENT | 39 |
| S407 | RubberBand_ITM2 | 38 | -47.73% | 29% | INSUFFICIENT | 39 |
| S408 | RubberBand_ITM1 | 47 | +0.00% | 47% | INSUFFICIENT | 36 |
| S409 | RubberBand_ATM | 0 | — | — | NEW | 0 |
| S410 | RubberBand_OTM1 | 6 | +8.42% | 50% | WATCH | 33 |
| S411 | RubberBand_OTM2 | 33 | +0.00% | 48% | INSUFFICIENT | 36 |
| S412 | RubberBand_OTM3 | 36 | -2.90% | 47% | INSUFFICIENT | 39 |
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
| S406 | 69 | +72.55% | 70% | Tyler review |
| S362 | 43 | +57.14% | 74% | Tyler review |
| S403 | 44 | +50.93% | 66% | Tyler review |
| S404 | 45 | +50.00% | 64% | Tyler review |
| S361 | 41 | +44.83% | 56% | Tyler review |
| S218 | 69 | +36.36% | 57% | Tyler review |
| S364 | 50 | +23.90% | 52% | Tyler review |
| S350 | 39 | +17.65% | 56% | Tyler review |
| S352 | 40 | +13.04% | 52% | Tyler review |
| S401 | 96 | +8.97% | 52% | Tyler review |
| S398 | 47 | +3.33% | 53% | Tyler review |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- **p25** sits between p10 and median for mid-tail visibility.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
- Active paper strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419.
