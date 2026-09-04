# Options strategy selection report — 2026-09-04

_Generated 2026-09-04T18:06:07.895978_

## Summary

- Strategies analyzed: **105**
- Keep: **0**
- Watch: **83**
- Drop: **22**

## Attribution health

- Total exits: **2820**
- Orphan exits (b0/orphan_reconcile): **353**
- Orphan rate: **12.5%** (warn if >10%)
- **ALERT:** orphan_rate > 10% — check client_order_id tagging / fill attribution before trusting strategy P&L.

## Strategy scoreboard

| strategy | DTE | rec | exits | win% | med% | p10% | p25% | p90% | days live | ent 5d | exit 5d | realized $ | top share | rationale |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S167 (GapDown long call 3 DTE 1-OTM — P2C) | 3d 1-OTM | watch | 4 | 100.0 | +318.26 | +112.00 | +121.00 | +525.26 | 45 | 12 | 4 | $+314.00 | 50.0% | insufficient sample (<8 exits) |
| S168 (GapDown ATM 5-DTE — P2B arm) | 5d ATM | watch | 8 | 100.0 | +186.95 | +52.33 | +102.52 | +260.56 | 45 | 19 | 8 | $+503.00 | 75.0% | building sample (8-19 exits) |
| S396 (GapDown_ITM2) | 3d | watch | 4 | 75.0 | +83.82 | -35.16 | +35.39 | +95.00 | 29 | 6 | 3 | $+120.00 | 100.0% | insufficient sample (<8 exits) |
| S163 (A1 GapDown ATM call EOD) | 7d ATM | watch | 9 | 100.0 | +82.76 | +71.35 | +81.08 | +201.14 | 45 | 18 | 9 | $+394.00 | 55.6% | building sample (8-19 exits) |
| S353 (GapDown_3DTE) | 3d | watch | 27 | 55.6 | +78.95 | -81.60 | -71.22 | +246.32 | 35 | 12 | 7 | $+213.00 | 33.3% | fat left tail (p10 < -45%) |
| S166 (GapDown strong call) | 3d ATM strong | watch | 6 | 100.0 | +75.23 | +61.38 | +68.63 | +148.00 | 45 | 13 | 6 | $+293.00 | 66.7% | insufficient sample (<8 exits) |
| S406 (RubberBand_ITM3) | 3d | watch | 69 | 69.6 | +72.55 | -63.41 | -6.38 | +972.63 | 35 | 17 | 9 | $+3,382.00 | 21.7% | fat left tail (p10 < -45%) |
| S397 (GapDown_ITM1) | 3d | watch | 27 | 81.5 | +61.90 | -71.66 | +39.48 | +115.78 | 35 | 16 | 5 | $+830.00 | 25.9% | fat left tail (p10 < -45%) |
| S362 (RubberBand_3DTE) | 3d | watch | 43 | 74.4 | +57.14 | -59.71 | -10.87 | +725.71 | 35 | 10 | 8 | $+1,359.00 | 30.2% | fat left tail (p10 < -45%) |
| S357 (GapDown_21DTE) | 21d | watch | 23 | 82.6 | +57.14 | -60.62 | +47.06 | +79.74 | 35 | 10 | 5 | $+530.00 | 34.8% | fat left tail (p10 < -45%) |
| S404 (GapDown_OTM2) | 3d | watch | 42 | 69.0 | +52.00 | -91.67 | -35.14 | +121.15 | 35 | 19 | 10 | $+878.00 | 21.4% | fat left tail (p10 < -45%) |
| S403 (Any_MA50_Touch) | 3d | watch | 44 | 65.9 | +50.93 | -63.07 | -49.10 | +236.83 | 35 | 16 | 12 | $+890.00 | 20.5% | fat left tail (p10 < -45%) |
| S361 (RubberBand_2DTE) | 2d | watch | 41 | 56.1 | +44.83 | -68.52 | -53.33 | +253.33 | 35 | 8 | 7 | $+212.00 | 26.8% | fat left tail (p10 < -45%) |
| S218 (BB_Lower_Touch) | 3d ATM BB lower touch | watch | 69 | 56.5 | +36.36 | -71.43 | -48.57 | +164.89 | 39 | 15 | 9 | $+1,111.00 | 36.2% | fat left tail (p10 < -45%) |
| S398 (GapDown_ATM) | 3d | watch | 46 | 54.3 | +26.15 | -68.29 | -55.35 | +156.67 | 35 | 12 | 4 | $+788.00 | 32.6% | fat left tail (p10 < -45%) |
| S364 (RubberBand_7DTE) | 7d | watch | 50 | 52.0 | +23.90 | -85.97 | -57.98 | +188.89 | 35 | 10 | 8 | $+92.00 | 38.0% | fat left tail (p10 < -45%) |
| S350 (GapDown_0DTE) | 0d | watch | 39 | 56.4 | +17.65 | -63.53 | -52.09 | +260.00 | 35 | 10 | 4 | $+764.00 | 33.3% | fat left tail (p10 < -45%) |
| S352 (GapDown_2DTE) | 2d | watch | 40 | 52.5 | +13.04 | -76.27 | -51.85 | +342.77 | 35 | 12 | 8 | $+176.00 | 27.5% | fat left tail (p10 < -45%) |
| S410 (RubberBand_OTM1) | 3d | watch | 6 | 50.0 | +8.42 | -73.28 | -63.48 | +89.63 | 29 | 4 | 2 | $+33.00 | 83.3% | insufficient sample (<8 exits) |
| S401 (Any_Gap_Down_Small) | 3d | watch | 95 | 51.6 | +8.33 | -85.93 | -48.84 | +273.08 | 35 | 16 | 3 | $+1,178.00 | 33.7% | fat left tail (p10 < -45%) |
| S358 (GapDown_30DTE) | 30d | watch | 4 | 50.0 | +0.84 | -51.39 | -51.39 | +54.49 | 31 | 0 | 0 | $-21.00 | 50.0% | insufficient sample (<8 exits) |
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
| S356 (GapDown_14DTE) | 14d | watch | 19 | 31.6 | -21.62 | -52.08 | -50.00 | +58.62 | 35 | 11 | 2 | $-81.00 | 31.6% | early sample with non-positive median |
| S365 (RubberBand_14DTE) | 14d | watch | 16 | 37.5 | -24.16 | -73.45 | -51.80 | +65.47 | 35 | 14 | 4 | $-77.00 | 37.5% | early sample with non-positive median |
| S367 (RubberBand_30DTE) | 30d | watch | 2 | 0.0 | -38.20 | -48.75 | -44.79 | -27.64 | 31 | 0 | 0 | $-55.00 | 100.0% | insufficient sample (<8 exits) |
| S164 (GapDown ATM 1-DTE — P2B arm) | 1d ATM | watch | 11 | 36.4 | -50.00 | -88.89 | -65.67 | +531.58 | 45 | 18 | 5 | $+260.00 | 45.5% | early sample with non-positive median |
| S400 (Any_Green_Close) | 3d | watch | 6 | 16.7 | -50.00 | -66.67 | -62.50 | +14.93 | 35 | 0 | 0 | $-5.00 | 83.3% | insufficient sample (<8 exits) |
| S366 (RubberBand_21DTE) | 21d | watch | 12 | 33.3 | -50.42 | -56.92 | -56.92 | +95.91 | 31 | 10 | 4 | $-77.00 | 66.7% | early sample with non-positive median |
| S202 (GapDown_Monster) | 3d ATM gap-monster | watch | 12 | 0.0 | -56.77 | -73.59 | -65.84 | -38.58 | 38 | 6 | 2 | $-208.00 | 33.3% | early sample with non-positive median |
| S209 (GapDown_Recovery) | 3d ATM gap-recovery | watch | 6 | 0.0 | -61.46 | -82.78 | -69.36 | -50.75 | 37 | 0 | 0 | $-210.00 | 83.3% | insufficient sample (<8 exits) |
| S408 (RubberBand_ITM1) | 3d | drop | 45 | 48.9 | +0.00 | -69.49 | -55.56 | +746.23 | 32 | 6 | 2 | $+1,104.00 | 22.2% | non-positive median return |
| S411 (RubberBand_OTM2) | 3d | drop | 33 | 48.5 | +0.00 | -56.72 | -51.67 | +37.88 | 32 | 12 | 4 | $-321.00 | 27.3% | non-positive median return |
| S412 (RubberBand_OTM3) | 3d | drop | 36 | 47.2 | -2.90 | -51.79 | -23.26 | +114.15 | 35 | 12 | 7 | $+110.00 | 22.2% | non-positive median return |
| S210 (MA_Cross_8_21) | 3d ATM MA cross 8/21 | drop | 72 | 48.6 | -5.30 | -80.79 | -50.83 | +63.95 | 39 | 14 | 4 | $-122.00 | 20.8% | non-positive median return |
| S399 (GapDown_OTM1) | 3d | drop | 55 | 49.1 | -17.24 | -84.36 | -66.67 | +183.89 | 35 | 22 | 12 | $+148.00 | 29.1% | non-positive median return |
| S174 (RubberBand long call EOD) | RubberBand (dropped) | drop | 119 | 36.1 | -25.00 | -89.83 | -71.19 | +36.67 | 60 | 0 | 0 | $-1,658.19 | 50.4% | non-positive median return |
| S355 (GapDown_7DTE) | 7d | drop | 58 | 48.3 | -26.38 | -69.85 | -61.88 | +189.38 | 35 | 15 | 9 | $+517.00 | 29.3% | non-positive median return |
| S173 (MomReversal long call) | MomRev | drop | 415 | 37.1 | -31.51 | -77.18 | -62.95 | +101.90 | 60 | 0 | 0 | $+62.64 | 27.5% | non-positive median return |
| S165 (GapDown long call 3 DTE) | 3d ATM | drop | 249 | 30.9 | -38.00 | -63.29 | -53.52 | +84.90 | 60 | 12 | 4 | $-1,526.78 | 26.5% | non-positive median return |
| S211 (MA_Cross_21_50) | 3d ATM MA cross 21/50 | drop | 43 | 27.9 | -38.10 | -80.62 | -55.60 | +102.82 | 39 | 4 | 2 | $-207.00 | 34.9% | non-positive median return |
| S405 (GapDown_OTM3) | 3d | drop | 56 | 33.9 | -42.86 | -83.93 | -65.20 | +103.47 | 35 | 0 | 0 | $-118.00 | 26.8% | manually paused — excluded from new entries & reflected P&L |
| S359 (RubberBand_0DTE) | 0d | drop | 28 | 28.6 | -45.55 | -71.43 | -68.91 | +178.57 | 32 | 8 | 5 | $-178.00 | 35.7% | non-positive median return |
| S217 (RSI_25_Bounce) | 3d ATM RSI<25 bounce | drop | 54 | 38.9 | -46.15 | -79.25 | -58.01 | +133.53 | 39 | 20 | 14 | $+402.00 | 55.6% | non-positive median return |
| S207 (GapDown_AtSupport) | 3d ATM gap-support | drop | 37 | 5.4 | -47.06 | -63.64 | -55.71 | -6.06 | 39 | 0 | 0 | $-822.00 | 43.2% | manually paused — excluded from new entries & reflected P&L |
| S407 (RubberBand_ITM2) | 3d | drop | 38 | 28.9 | -47.73 | -83.88 | -61.54 | +266.42 | 35 | 0 | 0 | $+33.00 | 26.3% | manually paused — excluded from new entries & reflected P&L |
| S354 (GapDown_5DTE) | 5d | drop | 51 | 41.2 | -50.77 | -92.16 | -75.99 | +137.78 | 35 | 12 | 6 | $+220.00 | 27.5% | non-positive median return |
| S351 (GapDown_1DTE) | 1d | drop | 56 | 26.8 | -52.55 | -78.66 | -68.17 | +261.46 | 35 | 18 | 6 | $+101.00 | 23.2% | non-positive median return |
| S216 (RSI_Oversold_Cross) | 3d ATM RSI x30 | drop | 38 | 21.1 | -53.98 | -82.47 | -74.25 | +121.64 | 39 | 6 | 3 | $-517.00 | 42.1% | non-positive median return |
| S203 (GapUp_Fade) | 3d ATM gap-up fade (put) | drop | 40 | 10.0 | -55.91 | -78.77 | -67.43 | -3.10 | 39 | 2 | 1 | $-797.00 | 35.0% | manually paused — excluded from new entries & reflected P&L |
| S360 (RubberBand_1DTE) | 1d | drop | 49 | 10.2 | -56.41 | -81.50 | -70.37 | -6.89 | 35 | 0 | 0 | $-913.00 | 22.4% | manually paused — excluded from new entries & reflected P&L |
| S212 (MA_Bounce_50) | 3d ATM MA bounce 50 | drop | 83 | 13.3 | -68.09 | -98.15 | -81.35 | +51.47 | 39 | 0 | 0 | $-2,246.00 | 34.9% | manually paused — excluded from new entries & reflected P&L |
| S363 (RubberBand_5DTE) | 5d | drop | 32 | 40.6 | -68.84 | -92.31 | -88.94 | +87.99 | 32 | 4 | 2 | $-671.00 | 34.4% | non-positive median return |

## Comparison groups

Experiment arms grouped for side-by-side decisions. INSUFFICIENT if any arm has n<10 exits.

### GapDown DTE comparison

- Status: **INSUFFICIENT** | Best median: **S168** (+186.95%) | Best p10: **S163** (+71.35%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S163 | 7d ATM | 9 | +82.76 | +71.35 | +81.08 | 18 | 9 |
| S164 | 1d ATM | 11 | -50.00 | -88.89 | -65.67 | 18 | 5 |
| S165 | 3d ATM | 249 | -38.00 | -63.29 | -53.52 | 12 | 4 |
| S168 | 5d ATM | 8 | +186.95 | +52.33 | +102.52 | 19 | 8 |

### GapDown Strike comparison

- Status: **INSUFFICIENT** | Best median: **S167** (+318.26%) | Best p10: **S167** (+112.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S165 | 3d ATM | 249 | -38.00 | -63.29 | -53.52 | 12 | 4 |
| S167 | 3d 1-OTM | 4 | +318.26 | +112.00 | +121.00 | 12 | 4 |

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
| S203 | 3d ATM gap-up fade (put) | 40 | -55.91 | -78.77 | -67.43 | 2 | 1 |
| S214 | 3d ATM death cross (put) | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 MA family

- Status: **INSUFFICIENT** | Best median: **S213** (+0.00%) | Best p10: **S213** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S210 | 3d ATM MA cross 8/21 | 72 | -5.30 | -80.79 | -50.83 | 14 | 4 |
| S211 | 3d ATM MA cross 21/50 | 43 | -38.10 | -80.62 | -55.60 | 4 | 2 |
| S212 | 3d ATM MA bounce 50 | 83 | -68.09 | -98.15 | -81.35 | 0 | 0 |
| S213 | 3d ATM MA bounce 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S215 | 3d ATM MA reclaim 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 RSI/BB/Vol

- Status: **INSUFFICIENT** | Best median: **S218** (+36.36%) | Best p10: **S219** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S216 | 3d ATM RSI x30 | 38 | -53.98 | -82.47 | -74.25 | 6 | 3 |
| S217 | 3d ATM RSI<25 bounce | 54 | -46.15 | -79.25 | -58.01 | 20 | 14 |
| S218 | 3d ATM BB lower touch | 69 | +36.36 | -71.43 | -48.57 | 15 | 9 |
| S219 | 3d ATM vol climax up | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Other

- Status: **OK** | Best median: **S173** (-31.51%) | Best p10: **S173** (-77.18%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S173 | MomRev | 415 | -31.51 | -77.18 | -62.95 | 0 | 0 |

## Strategy Pipeline Status

_Pipeline evaluation as of 2026-09-04. Auto-kill thresholds: median<-25% at n>=15, p10<-85%, WR<15% at n>=25. Promote: n>=30 median>0%._

| Strategy | Signal | n | Median% | WR% | Status | Days |
|----------|--------|---|---------|-----|--------|------|
| S163 | A1 GapDown ATM call EO | 9 | +82.76% | 100% | WATCH | 45 |
| S164 | GapDown ATM 1-DTE — P2 | 11 | -50.00% | 36% | WATCH | 45 |
| S165 | GapDown long call 3 DT | 249 | -38.00% | 31% | INSUFFICIENT | 60 |
| S166 | GapDown strong call | 6 | +75.23% | 100% | WATCH | 45 |
| S167 | GapDown long call 3 DT | 4 | +318.26% | 100% | WATCH | 45 |
| S168 | GapDown ATM 5-DTE — P2 | 8 | +186.95% | 100% | WATCH | 45 |
| S169 | BB Squeeze Breakout ca | 0 | — | — | NEW | 0 |
| S170 | Golden Pocket call 3 D | 0 | — | — | NEW | 0 |
| S171 | VWAP Reclaim call 3 DT | 0 | — | — | NEW | 0 |
| S172 | Trend Resumption call  | 0 | — | — | NEW | 0 |
| S173 | MomReversal long call | 415 | -31.51% | 37% | INSUFFICIENT | 60 |
| S174 | RubberBand long call E | 119 | -25.00% | 36% | INSUFFICIENT | 60 |
| S175 | Earnings Drift call 3  | 0 | — | — | NEW | 0 |
| S200 | GapDown_Aggressive | 0 | — | — | NEW | 0 |
| S201 | GapDown_Mild | 0 | — | — | NEW | 0 |
| S202 | GapDown_Monster | 12 | -56.77% | 0% | WATCH | 38 |
| S203 | GapUp_Fade | 40 | -55.91% | 10% | INSUFFICIENT | 39 |
| S204 | GapUp_Continuation | 0 | — | — | NEW | 0 |
| S205 | GapDown_HighVol | 0 | — | — | NEW | 0 |
| S206 | GapDown_WithTrend | 0 | — | — | NEW | 0 |
| S207 | GapDown_AtSupport | 37 | -47.06% | 5% | INSUFFICIENT | 39 |
| S208 | GapDown_AboveMA200 | 0 | — | — | NEW | 0 |
| S209 | GapDown_Recovery | 6 | -61.46% | 0% | WATCH | 37 |
| S210 | MA_Cross_8_21 | 72 | -5.30% | 49% | INSUFFICIENT | 39 |
| S211 | MA_Cross_21_50 | 43 | -38.10% | 28% | INSUFFICIENT | 39 |
| S212 | MA_Bounce_50 | 83 | -68.09% | 13% | INSUFFICIENT | 39 |
| S213 | MA_Bounce_200 | 0 | — | — | NEW | 0 |
| S214 | MA_Death_Cross | 0 | — | — | NEW | 0 |
| S215 | MA_Reclaim_200 | 0 | — | — | NEW | 0 |
| S216 | RSI_Oversold_Cross | 38 | -53.98% | 21% | INSUFFICIENT | 39 |
| S217 | RSI_25_Bounce | 54 | -46.15% | 39% | INSUFFICIENT | 39 |
| S218 | BB_Lower_Touch | 69 | +36.36% | 57% | INSUFFICIENT | 39 |
| S219 | Volume_Climax_Up | 0 | — | — | NEW | 0 |
| S220 | Pullback50 | 0 | — | — | NEW | 0 |
| S221 | GoldenPocket | 0 | — | — | NEW | 0 |
| S350 | GapDown_0DTE | 39 | +17.65% | 56% | INSUFFICIENT | 35 |
| S351 | GapDown_1DTE | 56 | -52.55% | 27% | INSUFFICIENT | 35 |
| S352 | GapDown_2DTE | 40 | +13.04% | 52% | INSUFFICIENT | 35 |
| S353 | GapDown_3DTE | 27 | +78.95% | 56% | INSUFFICIENT | 35 |
| S354 | GapDown_5DTE | 51 | -50.77% | 41% | INSUFFICIENT | 35 |
| S355 | GapDown_7DTE | 58 | -26.38% | 48% | INSUFFICIENT | 35 |
| S356 | GapDown_14DTE | 19 | -21.62% | 32% | INSUFFICIENT | 35 |
| S357 | GapDown_21DTE | 23 | +57.14% | 83% | INSUFFICIENT | 35 |
| S358 | GapDown_30DTE | 4 | +0.84% | 50% | WATCH | 31 |
| S359 | RubberBand_0DTE | 28 | -45.55% | 29% | INSUFFICIENT | 32 |
| S360 | RubberBand_1DTE | 49 | -56.41% | 10% | INSUFFICIENT | 35 |
| S361 | RubberBand_2DTE | 41 | +44.83% | 56% | INSUFFICIENT | 35 |
| S362 | RubberBand_3DTE | 43 | +57.14% | 74% | INSUFFICIENT | 35 |
| S363 | RubberBand_5DTE | 32 | -68.84% | 41% | INSUFFICIENT | 32 |
| S364 | RubberBand_7DTE | 50 | +23.90% | 52% | INSUFFICIENT | 35 |
| S365 | RubberBand_14DTE | 16 | -24.16% | 38% | INSUFFICIENT | 35 |
| S366 | RubberBand_21DTE | 12 | -50.42% | 33% | WATCH | 31 |
| S367 | RubberBand_30DTE | 2 | -38.20% | 0% | WATCH | 31 |
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
| S396 | GapDown_ITM2 | 4 | +83.82% | 75% | WATCH | 29 |
| S397 | GapDown_ITM1 | 27 | +61.90% | 81% | INSUFFICIENT | 35 |
| S398 | GapDown_ATM | 46 | +26.15% | 54% | INSUFFICIENT | 35 |
| S399 | GapDown_OTM1 | 55 | -17.24% | 49% | INSUFFICIENT | 35 |
| S400 | Any_Green_Close | 6 | -50.00% | 17% | WATCH | 35 |
| S401 | Any_Gap_Down_Small | 95 | +8.33% | 52% | INSUFFICIENT | 35 |
| S402 | Any_High_Volume | 0 | — | — | NEW | 0 |
| S403 | Any_MA50_Touch | 44 | +50.93% | 66% | INSUFFICIENT | 35 |
| S404 | GapDown_OTM2 | 42 | +52.00% | 69% | INSUFFICIENT | 35 |
| S405 | GapDown_OTM3 | 56 | -42.86% | 34% | INSUFFICIENT | 35 |
| S406 | RubberBand_ITM3 | 69 | +72.55% | 70% | INSUFFICIENT | 35 |
| S407 | RubberBand_ITM2 | 38 | -47.73% | 29% | INSUFFICIENT | 35 |
| S408 | RubberBand_ITM1 | 45 | +0.00% | 49% | INSUFFICIENT | 32 |
| S409 | RubberBand_ATM | 0 | — | — | NEW | 0 |
| S410 | RubberBand_OTM1 | 6 | +8.42% | 50% | WATCH | 29 |
| S411 | RubberBand_OTM2 | 33 | +0.00% | 48% | INSUFFICIENT | 32 |
| S412 | RubberBand_OTM3 | 36 | -2.90% | 47% | INSUFFICIENT | 35 |
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
| S404 | 42 | +52.00% | 69% | Tyler review |
| S403 | 44 | +50.93% | 66% | Tyler review |
| S361 | 41 | +44.83% | 56% | Tyler review |
| S218 | 69 | +36.36% | 57% | Tyler review |
| S398 | 46 | +26.15% | 54% | Tyler review |
| S364 | 50 | +23.90% | 52% | Tyler review |
| S350 | 39 | +17.65% | 56% | Tyler review |
| S352 | 40 | +13.04% | 52% | Tyler review |
| S401 | 95 | +8.33% | 52% | Tyler review |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- **p25** sits between p10 and median for mid-tail visibility.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
- Active paper strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419.
