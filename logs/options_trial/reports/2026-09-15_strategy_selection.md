# Options strategy selection report — 2026-09-15

_Generated 2026-09-15T11:12:37.283067_

## Summary

- Strategies analyzed: **105**
- Keep: **0**
- Watch: **81**
- Drop: **24**

## Attribution health

- Total exits: **3055**
- Orphan exits (b0/orphan_reconcile): **376**
- Orphan rate: **12.3%** (warn if >10%)
- **ALERT:** orphan_rate > 10% — check client_order_id tagging / fill attribution before trusting strategy P&L.

## Strategy scoreboard

| strategy | DTE | rec | exits | win% | med% | p10% | p25% | p90% | days live | ent 5d | exit 5d | realized $ | top share | rationale |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S168 (GapDown ATM 5-DTE — P2B arm) | 5d ATM | watch | 14 | 71.4 | +109.46 | -72.32 | -37.05 | +253.46 | 56 | 4 | 0 | $+462.00 | 42.9% | building sample (8-19 exits) |
| S396 (GapDown_ITM2) | 3d | watch | 6 | 83.3 | +89.03 | -3.80 | +77.19 | +106.25 | 40 | 2 | 2 | $+241.00 | 100.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | 3d ATM strong | watch | 8 | 100.0 | +75.23 | +63.34 | +67.08 | +194.50 | 56 | 0 | 0 | $+436.00 | 62.5% | building sample (8-19 exits) |
| S163 (A1 GapDown ATM call EOD) | 7d ATM | watch | 15 | 86.7 | +74.60 | -7.32 | +66.03 | +171.25 | 56 | 2 | 0 | $+514.00 | 33.3% | building sample (8-19 exits) |
| S406 (RubberBand_ITM3) | 3d | watch | 78 | 70.5 | +72.48 | -60.06 | -6.38 | +965.79 | 46 | 7 | 0 | $+3,400.00 | 19.2% | fat left tail (p10 < -45%) |
| S410 (RubberBand_OTM1) | 3d | watch | 9 | 66.7 | +65.28 | -70.41 | -48.44 | +101.53 | 40 | 2 | 1 | $+181.00 | 88.9% | building sample (8-19 exits) |
| S357 (GapDown_21DTE) | 21d | watch | 25 | 80.0 | +57.14 | -74.18 | +47.06 | +78.22 | 46 | 0 | 1 | $+532.00 | 32.0% | fat left tail (p10 < -45%) |
| S362 (RubberBand_3DTE) | 3d | watch | 47 | 72.3 | +55.56 | -59.14 | -30.43 | +662.86 | 46 | 4 | 2 | $+1,382.00 | 27.7% | fat left tail (p10 < -45%) |
| S397 (GapDown_ITM1) | 3d | watch | 32 | 71.9 | +54.46 | -72.49 | -56.38 | +115.32 | 46 | 6 | 0 | $+743.00 | 21.9% | fat left tail (p10 < -45%) |
| S403 (Any_MA50_Touch) | 3d | watch | 54 | 68.5 | +50.93 | -54.96 | -47.87 | +185.67 | 46 | 8 | 4 | $+1,050.00 | 22.2% | fat left tail (p10 < -45%) |
| S218 (BB_Lower_Touch) | 3d ATM BB lower touch | watch | 80 | 58.8 | +48.91 | -67.15 | -45.00 | +154.55 | 50 | 7 | 2 | $+1,352.00 | 31.2% | fat left tail (p10 < -45%) |
| S365 (RubberBand_14DTE) | 14d | watch | 23 | 56.5 | +48.00 | -61.14 | -49.56 | +72.51 | 46 | 4 | 4 | $+113.00 | 39.1% | fat left tail (p10 < -45%) |
| S404 (GapDown_OTM2) | 3d | watch | 52 | 59.6 | +45.14 | -91.67 | -49.78 | +111.04 | 46 | 7 | 0 | $+710.00 | 17.3% | fat left tail (p10 < -45%) |
| S356 (GapDown_14DTE) | 14d | watch | 27 | 51.9 | +36.00 | -51.16 | -35.65 | +66.60 | 46 | 2 | 4 | $+123.00 | 37.0% | fat left tail (p10 < -45%) |
| S167 (GapDown long call 3 DTE 1-OTM — P2C) | 3d 1-OTM | watch | 8 | 50.0 | +25.32 | -71.88 | -59.49 | +516.85 | 56 | 4 | 0 | $+206.00 | 25.0% | building sample (8-19 exits) |
| S364 (RubberBand_7DTE) | 7d | watch | 54 | 51.9 | +23.90 | -85.29 | -56.92 | +159.41 | 46 | 2 | 3 | $+87.00 | 38.9% | fat left tail (p10 < -45%) |
| S401 (Any_Gap_Down_Small) | 3d | watch | 102 | 52.9 | +12.70 | -74.00 | -48.39 | +268.50 | 46 | 6 | 3 | $+1,308.00 | 31.4% | fat left tail (p10 < -45%) |
| S350 (GapDown_0DTE) | 0d | watch | 43 | 51.2 | +11.76 | -65.89 | -52.76 | +246.29 | 46 | 4 | 0 | $+658.00 | 30.2% | fat left tail (p10 < -45%) |
| S355 (GapDown_7DTE) | 7d | watch | 60 | 50.0 | +4.26 | -69.12 | -60.62 | +188.13 | 46 | 0 | 1 | $+582.00 | 30.0% | fat left tail (p10 < -45%) |
| S361 (RubberBand_2DTE) | 2d | watch | 49 | 51.0 | +1.85 | -67.04 | -50.00 | +194.67 | 46 | 4 | 2 | $+160.00 | 22.4% | fat left tail (p10 < -45%) |
| S358 (GapDown_30DTE) | 30d | watch | 4 | 50.0 | +0.84 | -51.39 | -51.39 | +54.49 | 42 | 0 | 0 | $-21.00 | 50.0% | insufficient sample (<8 exits) |
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
| S367 (RubberBand_30DTE) | 30d | watch | 2 | 0.0 | -38.20 | -48.75 | -44.79 | -27.64 | 42 | 2 | 0 | $-55.00 | 100.0% | insufficient sample (<8 exits) |
| S366 (RubberBand_21DTE) | 21d | watch | 13 | 38.5 | -49.12 | -56.92 | -56.92 | +95.73 | 42 | 0 | 1 | $-52.00 | 61.5% | early sample with non-positive median |
| S400 (Any_Green_Close) | 3d | watch | 6 | 16.7 | -50.00 | -66.67 | -62.50 | +14.93 | 46 | 0 | 0 | $-5.00 | 83.3% | insufficient sample (<8 exits) |
| S164 (GapDown ATM 1-DTE — P2B arm) | 1d ATM | watch | 16 | 25.0 | -51.78 | -96.88 | -88.89 | +343.79 | 56 | 4 | 2 | $+81.00 | 31.2% | early sample with non-positive median |
| S202 (GapDown_Monster) | 3d ATM gap-monster | watch | 12 | 0.0 | -56.77 | -73.59 | -65.84 | -38.58 | 49 | 0 | 0 | $-208.00 | 33.3% | early sample with non-positive median |
| S209 (GapDown_Recovery) | 3d ATM gap-recovery | watch | 6 | 0.0 | -61.46 | -82.78 | -69.36 | -50.75 | 48 | 0 | 0 | $-210.00 | 83.3% | insufficient sample (<8 exits) |
| S411 (RubberBand_OTM2) | 3d | drop | 43 | 48.8 | +0.00 | -57.37 | -51.92 | +56.10 | 43 | 6 | 3 | $-328.00 | 20.9% | non-positive median return |
| S412 (RubberBand_OTM3) | 3d | drop | 48 | 43.8 | -3.57 | -52.91 | -47.99 | +113.49 | 46 | 6 | 0 | $+19.00 | 16.7% | non-positive median return |
| S210 (MA_Cross_8_21) | 3d ATM MA cross 8/21 | drop | 84 | 47.6 | -6.25 | -74.98 | -51.22 | +71.78 | 50 | 0 | 0 | $-121.00 | 17.9% | non-positive median return |
| S408 (RubberBand_ITM1) | 3d | drop | 53 | 41.5 | -6.25 | -79.39 | -59.26 | +628.08 | 43 | 6 | 2 | $+1,013.00 | 18.9% | non-positive median return |
| S398 (GapDown_ATM) | 3d | drop | 51 | 49.0 | -11.43 | -68.29 | -55.00 | +155.56 | 46 | 4 | 0 | $+670.00 | 31.4% | non-positive median return |
| S174 (RubberBand long call EOD) | RubberBand (dropped) | drop | 119 | 36.1 | -25.00 | -89.83 | -71.19 | +36.67 | 71 | 0 | 0 | $-1,658.19 | 50.4% | non-positive median return |
| S353 (GapDown_3DTE) | 3d | drop | 32 | 46.9 | -26.32 | -84.12 | -72.79 | +206.62 | 46 | 4 | 0 | $+55.00 | 28.1% | non-positive median return |
| S352 (GapDown_2DTE) | 2d | drop | 46 | 45.7 | -27.95 | -73.22 | -51.84 | +313.69 | 46 | 4 | 0 | $+43.00 | 23.9% | non-positive median return |
| S173 (MomReversal long call) | MomRev | drop | 415 | 37.1 | -31.51 | -77.18 | -62.95 | +101.90 | 71 | 0 | 0 | $+62.64 | 27.5% | non-positive median return |
| S165 (GapDown long call 3 DTE) | 3d ATM | drop | 250 | 30.8 | -38.09 | -63.27 | -53.52 | +84.61 | 71 | 4 | 0 | $-1,558.78 | 26.4% | non-positive median return |
| S211 (MA_Cross_21_50) | 3d ATM MA cross 21/50 | drop | 44 | 27.3 | -40.48 | -80.36 | -54.73 | +100.38 | 50 | 0 | 0 | $-245.00 | 34.1% | non-positive median return |
| S405 (GapDown_OTM3) | 3d | drop | 56 | 33.9 | -42.86 | -83.93 | -65.20 | +103.47 | 46 | 0 | 0 | $-118.00 | 26.8% | manually paused — excluded from new entries & reflected P&L |
| S217 (RSI_25_Bounce) | 3d ATM RSI<25 bounce | drop | 58 | 41.4 | -45.08 | -78.25 | -55.42 | +131.17 | 50 | 2 | 1 | $+471.00 | 51.7% | non-positive median return |
| S359 (RubberBand_0DTE) | 0d | drop | 32 | 31.2 | -45.55 | -71.40 | -67.11 | +155.71 | 43 | 4 | 1 | $-180.00 | 31.2% | non-positive median return |
| S207 (GapDown_AtSupport) | 3d ATM gap-support | drop | 37 | 5.4 | -47.06 | -63.64 | -55.71 | -6.06 | 50 | 0 | 0 | $-822.00 | 43.2% | manually paused — excluded from new entries & reflected P&L |
| S407 (RubberBand_ITM2) | 3d | drop | 38 | 28.9 | -47.73 | -83.88 | -61.54 | +266.42 | 46 | 0 | 0 | $+33.00 | 26.3% | manually paused — excluded from new entries & reflected P&L |
| S399 (GapDown_OTM1) | 3d | drop | 62 | 43.5 | -48.34 | -85.27 | -67.67 | +177.00 | 46 | 6 | 0 | $-19.00 | 25.8% | non-positive median return |
| S354 (GapDown_5DTE) | 5d | drop | 51 | 41.2 | -50.77 | -92.16 | -75.99 | +137.78 | 46 | 0 | 0 | $+220.00 | 27.5% | non-positive median return |
| S351 (GapDown_1DTE) | 1d | drop | 60 | 25.0 | -52.09 | -76.28 | -63.84 | +210.63 | 46 | 4 | 0 | $+4.00 | 21.7% | non-positive median return |
| S216 (RSI_Oversold_Cross) | 3d ATM RSI x30 | drop | 49 | 18.4 | -52.63 | -88.61 | -75.81 | +72.73 | 50 | 2 | 1 | $-752.00 | 32.7% | non-positive median return |
| S203 (GapUp_Fade) | 3d ATM gap-up fade (put) | drop | 40 | 10.0 | -55.91 | -78.77 | -67.43 | -3.10 | 50 | 0 | 0 | $-797.00 | 35.0% | manually paused — excluded from new entries & reflected P&L |
| S360 (RubberBand_1DTE) | 1d | drop | 49 | 10.2 | -56.41 | -81.50 | -70.37 | -6.89 | 46 | 0 | 0 | $-913.00 | 22.4% | manually paused — excluded from new entries & reflected P&L |
| S363 (RubberBand_5DTE) | 5d | drop | 34 | 38.2 | -64.23 | -92.31 | -86.98 | +82.72 | 43 | 0 | 0 | $-726.00 | 32.4% | non-positive median return |
| S212 (MA_Bounce_50) | 3d ATM MA bounce 50 | drop | 83 | 13.3 | -68.09 | -98.15 | -81.35 | +51.47 | 50 | 0 | 0 | $-2,246.00 | 34.9% | manually paused — excluded from new entries & reflected P&L |

## Comparison groups

Experiment arms grouped for side-by-side decisions. INSUFFICIENT if any arm has n<10 exits.

### GapDown DTE comparison

- Status: **OK** | Best median: **S168** (+109.46%) | Best p10: **S163** (-7.32%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S163 | 7d ATM | 15 | +74.60 | -7.32 | +66.03 | 2 | 0 |
| S164 | 1d ATM | 16 | -51.78 | -96.88 | -88.89 | 4 | 2 |
| S165 | 3d ATM | 250 | -38.09 | -63.27 | -53.52 | 4 | 0 |
| S168 | 5d ATM | 14 | +109.46 | -72.32 | -37.05 | 4 | 0 |

### GapDown Strike comparison

- Status: **INSUFFICIENT** | Best median: **S167** (+25.32%) | Best p10: **S165** (-63.27%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S165 | 3d ATM | 250 | -38.09 | -63.27 | -53.52 | 4 | 0 |
| S167 | 3d 1-OTM | 8 | +25.32 | -71.88 | -59.49 | 4 | 0 |

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
| S202 | 3d ATM gap-monster | 12 | -56.77 | -73.59 | -65.84 | 0 | 0 |
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
| S210 | 3d ATM MA cross 8/21 | 84 | -6.25 | -74.98 | -51.22 | 0 | 0 |
| S211 | 3d ATM MA cross 21/50 | 44 | -40.48 | -80.36 | -54.73 | 0 | 0 |
| S212 | 3d ATM MA bounce 50 | 83 | -68.09 | -98.15 | -81.35 | 0 | 0 |
| S213 | 3d ATM MA bounce 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S215 | 3d ATM MA reclaim 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 RSI/BB/Vol

- Status: **INSUFFICIENT** | Best median: **S218** (+48.91%) | Best p10: **S219** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S216 | 3d ATM RSI x30 | 49 | -52.63 | -88.61 | -75.81 | 2 | 1 |
| S217 | 3d ATM RSI<25 bounce | 58 | -45.08 | -78.25 | -55.42 | 2 | 1 |
| S218 | 3d ATM BB lower touch | 80 | +48.91 | -67.15 | -45.00 | 7 | 2 |
| S219 | 3d ATM vol climax up | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Other

- Status: **OK** | Best median: **S173** (-31.51%) | Best p10: **S173** (-77.18%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S173 | MomRev | 415 | -31.51 | -77.18 | -62.95 | 0 | 0 |

## Strategy Pipeline Status

_Pipeline evaluation as of 2026-09-15. Auto-kill thresholds: median<-25% at n>=15, p10<-85%, WR<15% at n>=25. Promote: n>=30 median>0%._

| Strategy | Signal | n | Median% | WR% | Status | Days |
|----------|--------|---|---------|-----|--------|------|
| S163 | A1 GapDown ATM call EO | 15 | +74.60% | 87% | INSUFFICIENT | 56 |
| S164 | GapDown ATM 1-DTE — P2 | 16 | -51.78% | 25% | INSUFFICIENT | 56 |
| S165 | GapDown long call 3 DT | 250 | -38.09% | 31% | INSUFFICIENT | 71 |
| S166 | GapDown strong call | 8 | +75.23% | 100% | WATCH | 56 |
| S167 | GapDown long call 3 DT | 8 | +25.32% | 50% | WATCH | 56 |
| S168 | GapDown ATM 5-DTE — P2 | 14 | +109.46% | 71% | WATCH | 56 |
| S169 | BB Squeeze Breakout ca | 0 | — | — | NEW | 0 |
| S170 | Golden Pocket call 3 D | 0 | — | — | NEW | 0 |
| S171 | VWAP Reclaim call 3 DT | 0 | — | — | NEW | 0 |
| S172 | Trend Resumption call  | 0 | — | — | NEW | 0 |
| S173 | MomReversal long call | 415 | -31.51% | 37% | INSUFFICIENT | 71 |
| S174 | RubberBand long call E | 119 | -25.00% | 36% | INSUFFICIENT | 71 |
| S175 | Earnings Drift call 3  | 0 | — | — | NEW | 0 |
| S200 | GapDown_Aggressive | 0 | — | — | NEW | 0 |
| S201 | GapDown_Mild | 0 | — | — | NEW | 0 |
| S202 | GapDown_Monster | 12 | -56.77% | 0% | WATCH | 49 |
| S203 | GapUp_Fade | 40 | -55.91% | 10% | INSUFFICIENT | 50 |
| S204 | GapUp_Continuation | 0 | — | — | NEW | 0 |
| S205 | GapDown_HighVol | 0 | — | — | NEW | 0 |
| S206 | GapDown_WithTrend | 0 | — | — | NEW | 0 |
| S207 | GapDown_AtSupport | 37 | -47.06% | 5% | INSUFFICIENT | 50 |
| S208 | GapDown_AboveMA200 | 0 | — | — | NEW | 0 |
| S209 | GapDown_Recovery | 6 | -61.46% | 0% | WATCH | 48 |
| S210 | MA_Cross_8_21 | 84 | -6.25% | 48% | INSUFFICIENT | 50 |
| S211 | MA_Cross_21_50 | 44 | -40.48% | 27% | INSUFFICIENT | 50 |
| S212 | MA_Bounce_50 | 83 | -68.09% | 13% | INSUFFICIENT | 50 |
| S213 | MA_Bounce_200 | 0 | — | — | NEW | 0 |
| S214 | MA_Death_Cross | 0 | — | — | NEW | 0 |
| S215 | MA_Reclaim_200 | 0 | — | — | NEW | 0 |
| S216 | RSI_Oversold_Cross | 49 | -52.63% | 18% | INSUFFICIENT | 50 |
| S217 | RSI_25_Bounce | 58 | -45.08% | 41% | INSUFFICIENT | 50 |
| S218 | BB_Lower_Touch | 80 | +48.91% | 59% | INSUFFICIENT | 50 |
| S219 | Volume_Climax_Up | 0 | — | — | NEW | 0 |
| S220 | Pullback50 | 0 | — | — | NEW | 0 |
| S221 | GoldenPocket | 0 | — | — | NEW | 0 |
| S350 | GapDown_0DTE | 43 | +11.76% | 51% | INSUFFICIENT | 46 |
| S351 | GapDown_1DTE | 60 | -52.09% | 25% | INSUFFICIENT | 46 |
| S352 | GapDown_2DTE | 46 | -27.95% | 46% | INSUFFICIENT | 46 |
| S353 | GapDown_3DTE | 32 | -26.32% | 47% | INSUFFICIENT | 46 |
| S354 | GapDown_5DTE | 51 | -50.77% | 41% | INSUFFICIENT | 46 |
| S355 | GapDown_7DTE | 60 | +4.26% | 50% | INSUFFICIENT | 46 |
| S356 | GapDown_14DTE | 27 | +36.00% | 52% | INSUFFICIENT | 46 |
| S357 | GapDown_21DTE | 25 | +57.14% | 80% | INSUFFICIENT | 46 |
| S358 | GapDown_30DTE | 4 | +0.84% | 50% | WATCH | 42 |
| S359 | RubberBand_0DTE | 32 | -45.55% | 31% | INSUFFICIENT | 43 |
| S360 | RubberBand_1DTE | 49 | -56.41% | 10% | INSUFFICIENT | 46 |
| S361 | RubberBand_2DTE | 49 | +1.85% | 51% | INSUFFICIENT | 46 |
| S362 | RubberBand_3DTE | 47 | +55.56% | 72% | INSUFFICIENT | 46 |
| S363 | RubberBand_5DTE | 34 | -64.23% | 38% | INSUFFICIENT | 43 |
| S364 | RubberBand_7DTE | 54 | +23.90% | 52% | INSUFFICIENT | 46 |
| S365 | RubberBand_14DTE | 23 | +48.00% | 57% | INSUFFICIENT | 46 |
| S366 | RubberBand_21DTE | 13 | -49.12% | 38% | WATCH | 42 |
| S367 | RubberBand_30DTE | 2 | -38.20% | 0% | WATCH | 42 |
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
| S396 | GapDown_ITM2 | 6 | +89.03% | 83% | WATCH | 40 |
| S397 | GapDown_ITM1 | 32 | +54.46% | 72% | INSUFFICIENT | 46 |
| S398 | GapDown_ATM | 51 | -11.43% | 49% | INSUFFICIENT | 46 |
| S399 | GapDown_OTM1 | 62 | -48.34% | 44% | INSUFFICIENT | 46 |
| S400 | Any_Green_Close | 6 | -50.00% | 17% | WATCH | 46 |
| S401 | Any_Gap_Down_Small | 102 | +12.70% | 53% | INSUFFICIENT | 46 |
| S402 | Any_High_Volume | 0 | — | — | NEW | 0 |
| S403 | Any_MA50_Touch | 54 | +50.93% | 69% | INSUFFICIENT | 46 |
| S404 | GapDown_OTM2 | 52 | +45.14% | 60% | INSUFFICIENT | 46 |
| S405 | GapDown_OTM3 | 56 | -42.86% | 34% | INSUFFICIENT | 46 |
| S406 | RubberBand_ITM3 | 78 | +72.48% | 71% | INSUFFICIENT | 46 |
| S407 | RubberBand_ITM2 | 38 | -47.73% | 29% | INSUFFICIENT | 46 |
| S408 | RubberBand_ITM1 | 53 | -6.25% | 42% | INSUFFICIENT | 43 |
| S409 | RubberBand_ATM | 0 | — | — | NEW | 0 |
| S410 | RubberBand_OTM1 | 9 | +65.28% | 67% | WATCH | 40 |
| S411 | RubberBand_OTM2 | 43 | +0.00% | 49% | INSUFFICIENT | 43 |
| S412 | RubberBand_OTM3 | 48 | -3.57% | 44% | INSUFFICIENT | 46 |
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
| S406 | 78 | +72.48% | 71% | Tyler review |
| S362 | 47 | +55.56% | 72% | Tyler review |
| S397 | 32 | +54.46% | 72% | Tyler review |
| S403 | 54 | +50.93% | 69% | Tyler review |
| S218 | 80 | +48.91% | 59% | Tyler review |
| S404 | 52 | +45.14% | 60% | Tyler review |
| S364 | 54 | +23.90% | 52% | Tyler review |
| S401 | 102 | +12.70% | 53% | Tyler review |
| S350 | 43 | +11.76% | 51% | Tyler review |
| S355 | 60 | +4.26% | 50% | Tyler review |
| S361 | 49 | +1.85% | 51% | Tyler review |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- **p25** sits between p10 and median for mid-tail visibility.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
- Active paper strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419.
