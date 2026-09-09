# Options strategy selection report — 2026-09-09

_Generated 2026-09-09T17:03:34.514680_

## Summary

- Strategies analyzed: **105**
- Keep: **0**
- Watch: **82**
- Drop: **23**

## Attribution health

- Total exits: **2929**
- Orphan exits (b0/orphan_reconcile): **360**
- Orphan rate: **12.3%** (warn if >10%)
- **ALERT:** orphan_rate > 10% — check client_order_id tagging / fill attribution before trusting strategy P&L.

## Strategy scoreboard

| strategy | DTE | rec | exits | win% | med% | p10% | p25% | p90% | days live | ent 5d | exit 5d | realized $ | top share | rationale |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S168 (GapDown ATM 5-DTE — P2B arm) | 5d ATM | watch | 12 | 83.3 | +117.57 | -54.46 | +52.50 | +254.86 | 50 | 4 | 4 | $+510.00 | 50.0% | building sample (8-19 exits) |
| S167 (GapDown long call 3 DTE 1-OTM — P2C) | 3d 1-OTM | watch | 6 | 66.7 | +116.00 | -55.36 | -15.02 | +521.06 | 50 | 4 | 2 | $+252.00 | 33.3% | insufficient sample (<8 exits) |
| S396 (GapDown_ITM2) | 3d | watch | 4 | 75.0 | +83.82 | -35.16 | +35.39 | +95.00 | 34 | 0 | 0 | $+120.00 | 100.0% | insufficient sample (<8 exits) |
| S163 (A1 GapDown ATM call EOD) | 7d ATM | watch | 13 | 100.0 | +81.08 | +65.33 | +70.49 | +185.62 | 50 | 2 | 4 | $+562.00 | 38.5% | building sample (8-19 exits) |
| S166 (GapDown strong call) | 3d ATM strong | watch | 8 | 100.0 | +75.23 | +63.34 | +67.08 | +194.50 | 50 | 0 | 2 | $+436.00 | 62.5% | building sample (8-19 exits) |
| S406 (RubberBand_ITM3) | 3d | watch | 75 | 70.7 | +72.55 | -61.49 | -6.38 | +965.79 | 40 | 1 | 6 | $+3,403.00 | 20.0% | fat left tail (p10 < -45%) |
| S397 (GapDown_ITM1) | 3d | watch | 30 | 76.7 | +59.72 | -67.51 | +24.01 | +115.48 | 40 | 6 | 3 | $+820.00 | 23.3% | fat left tail (p10 < -45%) |
| S362 (RubberBand_3DTE) | 3d | watch | 45 | 75.6 | +57.14 | -59.43 | +8.70 | +694.28 | 40 | 6 | 2 | $+1,392.00 | 28.9% | fat left tail (p10 < -45%) |
| S357 (GapDown_21DTE) | 21d | watch | 24 | 79.2 | +55.04 | -76.29 | +47.06 | +78.98 | 40 | 0 | 1 | $+490.00 | 33.3% | fat left tail (p10 < -45%) |
| S410 (RubberBand_OTM1) | 3d | watch | 7 | 57.1 | +51.39 | -72.33 | -58.46 | +87.26 | 34 | 0 | 1 | $+70.00 | 85.7% | insufficient sample (<8 exits) |
| S403 (Any_MA50_Touch) | 3d | watch | 46 | 67.4 | +50.88 | -61.05 | -48.23 | +222.50 | 40 | 6 | 2 | $+925.00 | 19.6% | fat left tail (p10 < -45%) |
| S361 (RubberBand_2DTE) | 2d | watch | 42 | 57.1 | +50.36 | -68.33 | -47.61 | +246.00 | 40 | 6 | 1 | $+230.00 | 26.2% | fat left tail (p10 < -45%) |
| S404 (GapDown_OTM2) | 3d | watch | 47 | 63.8 | +50.00 | -91.67 | -41.58 | +115.81 | 40 | 7 | 5 | $+817.00 | 19.1% | fat left tail (p10 < -45%) |
| S218 (BB_Lower_Touch) | 3d ATM BB lower touch | watch | 74 | 56.8 | +41.03 | -70.00 | -47.61 | +161.14 | 44 | 10 | 5 | $+1,214.00 | 33.8% | fat left tail (p10 < -45%) |
| S364 (RubberBand_7DTE) | 7d | watch | 50 | 52.0 | +23.90 | -85.97 | -57.98 | +188.89 | 40 | 0 | 0 | $+92.00 | 38.0% | fat left tail (p10 < -45%) |
| S353 (GapDown_3DTE) | 3d | watch | 30 | 50.0 | +15.51 | -85.57 | -72.91 | +219.48 | 40 | 4 | 3 | $+125.00 | 30.0% | fat left tail (p10 < -45%) |
| S350 (GapDown_0DTE) | 0d | watch | 42 | 52.4 | +13.38 | -62.55 | -51.01 | +253.14 | 40 | 4 | 3 | $+694.00 | 31.0% | fat left tail (p10 < -45%) |
| S401 (Any_Gap_Down_Small) | 3d | watch | 97 | 51.5 | +8.33 | -81.95 | -49.02 | +273.08 | 40 | 10 | 1 | $+1,177.00 | 33.0% | fat left tail (p10 < -45%) |
| S398 (GapDown_ATM) | 3d | watch | 48 | 52.1 | +3.33 | -68.29 | -54.65 | +156.23 | 40 | 4 | 2 | $+732.00 | 31.2% | fat left tail (p10 < -45%) |
| S411 (RubberBand_OTM2) | 3d | watch | 38 | 50.0 | +1.35 | -56.72 | -51.60 | +52.74 | 37 | 8 | 5 | $-270.00 | 23.7% | fat left tail (p10 < -45%) |
| S358 (GapDown_30DTE) | 30d | watch | 4 | 50.0 | +0.84 | -51.39 | -51.39 | +54.49 | 36 | 0 | 0 | $-21.00 | 50.0% | insufficient sample (<8 exits) |
| S365 (RubberBand_14DTE) | 14d | watch | 19 | 47.4 | +0.00 | -67.38 | -51.20 | +64.37 | 40 | 0 | 3 | $-6.00 | 31.6% | early sample with non-positive median |
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
| S367 (RubberBand_30DTE) | 30d | watch | 2 | 0.0 | -38.20 | -48.75 | -44.79 | -27.64 | 36 | 0 | 0 | $-55.00 | 100.0% | insufficient sample (<8 exits) |
| S164 (GapDown ATM 1-DTE — P2B arm) | 1d ATM | watch | 13 | 30.8 | -50.00 | -88.89 | -77.78 | +456.46 | 50 | 4 | 2 | $+173.00 | 38.5% | early sample with non-positive median |
| S400 (Any_Green_Close) | 3d | watch | 6 | 16.7 | -50.00 | -66.67 | -62.50 | +14.93 | 40 | 0 | 0 | $-5.00 | 83.3% | insufficient sample (<8 exits) |
| S366 (RubberBand_21DTE) | 21d | watch | 12 | 33.3 | -50.42 | -56.92 | -56.92 | +95.91 | 36 | 0 | 0 | $-77.00 | 66.7% | early sample with non-positive median |
| S202 (GapDown_Monster) | 3d ATM gap-monster | watch | 12 | 0.0 | -56.77 | -73.59 | -65.84 | -38.58 | 43 | 0 | 0 | $-208.00 | 33.3% | early sample with non-positive median |
| S209 (GapDown_Recovery) | 3d ATM gap-recovery | watch | 6 | 0.0 | -61.46 | -82.78 | -69.36 | -50.75 | 42 | 0 | 0 | $-210.00 | 83.3% | insufficient sample (<8 exits) |
| S408 (RubberBand_ITM1) | 3d | drop | 48 | 45.8 | +0.00 | -68.84 | -56.34 | +700.89 | 37 | 6 | 3 | $+1,098.00 | 20.8% | non-positive median return |
| S412 (RubberBand_OTM3) | 3d | drop | 41 | 48.8 | -2.22 | -51.79 | -23.26 | +112.50 | 40 | 6 | 5 | $+130.00 | 19.5% | non-positive median return |
| S210 (MA_Cross_8_21) | 3d ATM MA cross 8/21 | drop | 82 | 48.8 | -5.30 | -76.11 | -51.09 | +72.33 | 44 | 14 | 8 | $-72.00 | 18.3% | non-positive median return |
| S355 (GapDown_7DTE) | 7d | drop | 59 | 49.2 | -15.62 | -69.48 | -61.25 | +188.75 | 40 | 0 | 1 | $+553.00 | 28.8% | non-positive median return |
| S352 (GapDown_2DTE) | 2d | drop | 44 | 47.7 | -17.65 | -73.93 | -51.85 | +324.88 | 40 | 4 | 4 | $+81.00 | 25.0% | non-positive median return |
| S356 (GapDown_14DTE) | 14d | drop | 23 | 43.5 | -19.44 | -51.50 | -48.15 | +57.51 | 40 | 0 | 4 | $+8.00 | 26.1% | non-positive median return |
| S174 (RubberBand long call EOD) | RubberBand (dropped) | drop | 119 | 36.1 | -25.00 | -89.83 | -71.19 | +36.67 | 65 | 0 | 0 | $-1,658.19 | 50.4% | non-positive median return |
| S173 (MomReversal long call) | MomRev | drop | 415 | 37.1 | -31.51 | -77.18 | -62.95 | +101.90 | 65 | 0 | 0 | $+62.64 | 27.5% | non-positive median return |
| S165 (GapDown long call 3 DTE) | 3d ATM | drop | 249 | 30.9 | -38.00 | -63.29 | -53.52 | +84.90 | 65 | 4 | 0 | $-1,526.78 | 26.5% | non-positive median return |
| S211 (MA_Cross_21_50) | 3d ATM MA cross 21/50 | drop | 43 | 27.9 | -38.10 | -80.62 | -55.60 | +102.82 | 44 | 0 | 0 | $-207.00 | 34.9% | non-positive median return |
| S405 (GapDown_OTM3) | 3d | drop | 56 | 33.9 | -42.86 | -83.93 | -65.20 | +103.47 | 40 | 0 | 0 | $-118.00 | 26.8% | manually paused — excluded from new entries & reflected P&L |
| S359 (RubberBand_0DTE) | 0d | drop | 30 | 33.3 | -44.44 | -71.43 | -67.98 | +164.28 | 37 | 4 | 2 | $-151.00 | 33.3% | non-positive median return |
| S217 (RSI_25_Bounce) | 3d ATM RSI<25 bounce | drop | 57 | 42.1 | -46.15 | -78.50 | -55.56 | +131.76 | 44 | 4 | 3 | $+493.00 | 52.6% | non-positive median return |
| S399 (GapDown_OTM1) | 3d | drop | 59 | 45.8 | -46.67 | -85.72 | -66.67 | +181.30 | 40 | 8 | 3 | $+48.00 | 27.1% | non-positive median return |
| S207 (GapDown_AtSupport) | 3d ATM gap-support | drop | 37 | 5.4 | -47.06 | -63.64 | -55.71 | -6.06 | 44 | 0 | 0 | $-822.00 | 43.2% | manually paused — excluded from new entries & reflected P&L |
| S407 (RubberBand_ITM2) | 3d | drop | 38 | 28.9 | -47.73 | -83.88 | -61.54 | +266.42 | 40 | 0 | 0 | $+33.00 | 26.3% | manually paused — excluded from new entries & reflected P&L |
| S354 (GapDown_5DTE) | 5d | drop | 51 | 41.2 | -50.77 | -92.16 | -75.99 | +137.78 | 40 | 0 | 0 | $+220.00 | 27.5% | non-positive median return |
| S351 (GapDown_1DTE) | 1d | drop | 60 | 25.0 | -52.09 | -76.28 | -63.84 | +210.63 | 40 | 4 | 4 | $+4.00 | 21.7% | non-positive median return |
| S216 (RSI_Oversold_Cross) | 3d ATM RSI x30 | drop | 42 | 19.0 | -53.98 | -80.49 | -69.25 | +73.95 | 44 | 11 | 4 | $-630.00 | 38.1% | non-positive median return |
| S203 (GapUp_Fade) | 3d ATM gap-up fade (put) | drop | 40 | 10.0 | -55.91 | -78.77 | -67.43 | -3.10 | 44 | 0 | 0 | $-797.00 | 35.0% | manually paused — excluded from new entries & reflected P&L |
| S360 (RubberBand_1DTE) | 1d | drop | 49 | 10.2 | -56.41 | -81.50 | -70.37 | -6.89 | 40 | 0 | 0 | $-913.00 | 22.4% | manually paused — excluded from new entries & reflected P&L |
| S212 (MA_Bounce_50) | 3d ATM MA bounce 50 | drop | 83 | 13.3 | -68.09 | -98.15 | -81.35 | +51.47 | 44 | 0 | 0 | $-2,246.00 | 34.9% | manually paused — excluded from new entries & reflected P&L |
| S363 (RubberBand_5DTE) | 5d | drop | 32 | 40.6 | -68.84 | -92.31 | -88.94 | +87.99 | 37 | 0 | 0 | $-671.00 | 34.4% | non-positive median return |

## Comparison groups

Experiment arms grouped for side-by-side decisions. INSUFFICIENT if any arm has n<10 exits.

### GapDown DTE comparison

- Status: **OK** | Best median: **S168** (+117.57%) | Best p10: **S163** (+65.33%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S163 | 7d ATM | 13 | +81.08 | +65.33 | +70.49 | 2 | 4 |
| S164 | 1d ATM | 13 | -50.00 | -88.89 | -77.78 | 4 | 2 |
| S165 | 3d ATM | 249 | -38.00 | -63.29 | -53.52 | 4 | 0 |
| S168 | 5d ATM | 12 | +117.57 | -54.46 | +52.50 | 4 | 4 |

### GapDown Strike comparison

- Status: **INSUFFICIENT** | Best median: **S167** (+116.00%) | Best p10: **S167** (-55.36%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S165 | 3d ATM | 249 | -38.00 | -63.29 | -53.52 | 4 | 0 |
| S167 | 3d 1-OTM | 6 | +116.00 | -55.36 | -15.02 | 4 | 2 |

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
| S210 | 3d ATM MA cross 8/21 | 82 | -5.30 | -76.11 | -51.09 | 14 | 8 |
| S211 | 3d ATM MA cross 21/50 | 43 | -38.10 | -80.62 | -55.60 | 0 | 0 |
| S212 | 3d ATM MA bounce 50 | 83 | -68.09 | -98.15 | -81.35 | 0 | 0 |
| S213 | 3d ATM MA bounce 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S215 | 3d ATM MA reclaim 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 RSI/BB/Vol

- Status: **INSUFFICIENT** | Best median: **S218** (+41.03%) | Best p10: **S219** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S216 | 3d ATM RSI x30 | 42 | -53.98 | -80.49 | -69.25 | 11 | 4 |
| S217 | 3d ATM RSI<25 bounce | 57 | -46.15 | -78.50 | -55.56 | 4 | 3 |
| S218 | 3d ATM BB lower touch | 74 | +41.03 | -70.00 | -47.61 | 10 | 5 |
| S219 | 3d ATM vol climax up | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Other

- Status: **OK** | Best median: **S173** (-31.51%) | Best p10: **S173** (-77.18%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S173 | MomRev | 415 | -31.51 | -77.18 | -62.95 | 0 | 0 |

## Strategy Pipeline Status

_Pipeline evaluation as of 2026-09-09. Auto-kill thresholds: median<-25% at n>=15, p10<-85%, WR<15% at n>=25. Promote: n>=30 median>0%._

| Strategy | Signal | n | Median% | WR% | Status | Days |
|----------|--------|---|---------|-----|--------|------|
| S163 | A1 GapDown ATM call EO | 13 | +81.08% | 100% | WATCH | 50 |
| S164 | GapDown ATM 1-DTE — P2 | 13 | -50.00% | 31% | WATCH | 50 |
| S165 | GapDown long call 3 DT | 249 | -38.00% | 31% | INSUFFICIENT | 65 |
| S166 | GapDown strong call | 8 | +75.23% | 100% | WATCH | 50 |
| S167 | GapDown long call 3 DT | 6 | +116.00% | 67% | WATCH | 50 |
| S168 | GapDown ATM 5-DTE — P2 | 12 | +117.57% | 83% | WATCH | 50 |
| S169 | BB Squeeze Breakout ca | 0 | — | — | NEW | 0 |
| S170 | Golden Pocket call 3 D | 0 | — | — | NEW | 0 |
| S171 | VWAP Reclaim call 3 DT | 0 | — | — | NEW | 0 |
| S172 | Trend Resumption call  | 0 | — | — | NEW | 0 |
| S173 | MomReversal long call | 415 | -31.51% | 37% | INSUFFICIENT | 65 |
| S174 | RubberBand long call E | 119 | -25.00% | 36% | INSUFFICIENT | 65 |
| S175 | Earnings Drift call 3  | 0 | — | — | NEW | 0 |
| S200 | GapDown_Aggressive | 0 | — | — | NEW | 0 |
| S201 | GapDown_Mild | 0 | — | — | NEW | 0 |
| S202 | GapDown_Monster | 12 | -56.77% | 0% | WATCH | 43 |
| S203 | GapUp_Fade | 40 | -55.91% | 10% | INSUFFICIENT | 44 |
| S204 | GapUp_Continuation | 0 | — | — | NEW | 0 |
| S205 | GapDown_HighVol | 0 | — | — | NEW | 0 |
| S206 | GapDown_WithTrend | 0 | — | — | NEW | 0 |
| S207 | GapDown_AtSupport | 37 | -47.06% | 5% | INSUFFICIENT | 44 |
| S208 | GapDown_AboveMA200 | 0 | — | — | NEW | 0 |
| S209 | GapDown_Recovery | 6 | -61.46% | 0% | WATCH | 42 |
| S210 | MA_Cross_8_21 | 82 | -5.30% | 49% | INSUFFICIENT | 44 |
| S211 | MA_Cross_21_50 | 43 | -38.10% | 28% | INSUFFICIENT | 44 |
| S212 | MA_Bounce_50 | 83 | -68.09% | 13% | INSUFFICIENT | 44 |
| S213 | MA_Bounce_200 | 0 | — | — | NEW | 0 |
| S214 | MA_Death_Cross | 0 | — | — | NEW | 0 |
| S215 | MA_Reclaim_200 | 0 | — | — | NEW | 0 |
| S216 | RSI_Oversold_Cross | 42 | -53.98% | 19% | INSUFFICIENT | 44 |
| S217 | RSI_25_Bounce | 57 | -46.15% | 42% | INSUFFICIENT | 44 |
| S218 | BB_Lower_Touch | 74 | +41.03% | 57% | INSUFFICIENT | 44 |
| S219 | Volume_Climax_Up | 0 | — | — | NEW | 0 |
| S220 | Pullback50 | 0 | — | — | NEW | 0 |
| S221 | GoldenPocket | 0 | — | — | NEW | 0 |
| S350 | GapDown_0DTE | 42 | +13.38% | 52% | INSUFFICIENT | 40 |
| S351 | GapDown_1DTE | 60 | -52.09% | 25% | INSUFFICIENT | 40 |
| S352 | GapDown_2DTE | 44 | -17.65% | 48% | INSUFFICIENT | 40 |
| S353 | GapDown_3DTE | 30 | +15.51% | 50% | INSUFFICIENT | 40 |
| S354 | GapDown_5DTE | 51 | -50.77% | 41% | INSUFFICIENT | 40 |
| S355 | GapDown_7DTE | 59 | -15.62% | 49% | INSUFFICIENT | 40 |
| S356 | GapDown_14DTE | 23 | -19.44% | 43% | INSUFFICIENT | 40 |
| S357 | GapDown_21DTE | 24 | +55.04% | 79% | INSUFFICIENT | 40 |
| S358 | GapDown_30DTE | 4 | +0.84% | 50% | WATCH | 36 |
| S359 | RubberBand_0DTE | 30 | -44.44% | 33% | INSUFFICIENT | 37 |
| S360 | RubberBand_1DTE | 49 | -56.41% | 10% | INSUFFICIENT | 40 |
| S361 | RubberBand_2DTE | 42 | +50.36% | 57% | INSUFFICIENT | 40 |
| S362 | RubberBand_3DTE | 45 | +57.14% | 76% | INSUFFICIENT | 40 |
| S363 | RubberBand_5DTE | 32 | -68.84% | 41% | INSUFFICIENT | 37 |
| S364 | RubberBand_7DTE | 50 | +23.90% | 52% | INSUFFICIENT | 40 |
| S365 | RubberBand_14DTE | 19 | +0.00% | 47% | INSUFFICIENT | 40 |
| S366 | RubberBand_21DTE | 12 | -50.42% | 33% | WATCH | 36 |
| S367 | RubberBand_30DTE | 2 | -38.20% | 0% | WATCH | 36 |
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
| S396 | GapDown_ITM2 | 4 | +83.82% | 75% | WATCH | 34 |
| S397 | GapDown_ITM1 | 30 | +59.72% | 77% | INSUFFICIENT | 40 |
| S398 | GapDown_ATM | 48 | +3.33% | 52% | INSUFFICIENT | 40 |
| S399 | GapDown_OTM1 | 59 | -46.67% | 46% | INSUFFICIENT | 40 |
| S400 | Any_Green_Close | 6 | -50.00% | 17% | WATCH | 40 |
| S401 | Any_Gap_Down_Small | 97 | +8.33% | 52% | INSUFFICIENT | 40 |
| S402 | Any_High_Volume | 0 | — | — | NEW | 0 |
| S403 | Any_MA50_Touch | 46 | +50.88% | 67% | INSUFFICIENT | 40 |
| S404 | GapDown_OTM2 | 47 | +50.00% | 64% | INSUFFICIENT | 40 |
| S405 | GapDown_OTM3 | 56 | -42.86% | 34% | INSUFFICIENT | 40 |
| S406 | RubberBand_ITM3 | 75 | +72.55% | 71% | INSUFFICIENT | 40 |
| S407 | RubberBand_ITM2 | 38 | -47.73% | 29% | INSUFFICIENT | 40 |
| S408 | RubberBand_ITM1 | 48 | +0.00% | 46% | INSUFFICIENT | 37 |
| S409 | RubberBand_ATM | 0 | — | — | NEW | 0 |
| S410 | RubberBand_OTM1 | 7 | +51.39% | 57% | WATCH | 34 |
| S411 | RubberBand_OTM2 | 38 | +1.35% | 50% | INSUFFICIENT | 37 |
| S412 | RubberBand_OTM3 | 41 | -2.22% | 49% | INSUFFICIENT | 40 |
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
| S406 | 75 | +72.55% | 71% | Tyler review |
| S397 | 30 | +59.72% | 77% | Tyler review |
| S362 | 45 | +57.14% | 76% | Tyler review |
| S403 | 46 | +50.88% | 67% | Tyler review |
| S361 | 42 | +50.36% | 57% | Tyler review |
| S404 | 47 | +50.00% | 64% | Tyler review |
| S218 | 74 | +41.03% | 57% | Tyler review |
| S364 | 50 | +23.90% | 52% | Tyler review |
| S353 | 30 | +15.51% | 50% | Tyler review |
| S350 | 42 | +13.38% | 52% | Tyler review |
| S401 | 97 | +8.33% | 52% | Tyler review |
| S398 | 48 | +3.33% | 52% | Tyler review |
| S411 | 38 | +1.35% | 50% | Tyler review |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- **p25** sits between p10 and median for mid-tail visibility.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
- Active paper strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419.
