# Options strategy selection report — 2026-09-25

_Generated 2026-09-25T18:31:23.680293_

## Summary

- Strategies analyzed: **105**
- Keep: **0**
- Watch: **84**
- Drop: **21**

## Attribution health

- Total exits: **3416**
- Orphan exits (b0/orphan_reconcile): **410**
- Orphan rate: **12.0%** (warn if >10%)
- **ALERT:** orphan_rate > 10% — check client_order_id tagging / fill attribution before trusting strategy P&L.

## Strategy scoreboard

| strategy | DTE | rec | exits | win% | med% | p10% | p25% | p90% | days live | ent 5d | exit 5d | realized $ | top share | rationale |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S167 (GapDown long call 3 DTE 1-OTM — P2C) | 3d 1-OTM | watch | 14 | 71.4 | +134.06 | -66.92 | -15.02 | +455.94 | 66 | 11 | 2 | $+503.00 | 42.9% | building sample (8-19 exits) |
| S396 (GapDown_ITM2) | 3d | watch | 7 | 85.7 | +87.50 | +11.87 | +79.79 | +104.17 | 50 | 2 | 1 | $+304.00 | 85.7% | insufficient sample (<8 exits) |
| S409 (RubberBand_ATM) | 3d | watch | 2 | 100.0 | +81.94 | +79.72 | +80.56 | +84.17 | 1 | 2 | 2 | $+118.00 | 100.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | 3d ATM strong | watch | 8 | 100.0 | +75.23 | +63.34 | +67.08 | +194.50 | 66 | 0 | 0 | $+436.00 | 62.5% | building sample (8-19 exits) |
| S410 (RubberBand_OTM1) | 3d | watch | 10 | 70.0 | +67.85 | -69.45 | -23.48 | +101.51 | 50 | 4 | 1 | $+231.00 | 80.0% | building sample (8-19 exits) |
| S397 (GapDown_ITM1) | 3d | watch | 39 | 74.4 | +66.67 | -66.59 | -17.41 | +126.10 | 56 | 18 | 2 | $+1,237.00 | 20.5% | fat left tail (p10 < -45%) |
| S168 (GapDown ATM 5-DTE — P2B arm) | 5d ATM | watch | 22 | 63.6 | +66.12 | -74.26 | -62.57 | +247.92 | 66 | 10 | 2 | $+517.00 | 54.5% | fat left tail (p10 < -45%) |
| S163 (A1 GapDown ATM call EOD) | 7d ATM | watch | 23 | 65.2 | +64.86 | -74.16 | -63.09 | +120.43 | 66 | 10 | 2 | $+388.00 | 47.8% | fat left tail (p10 < -45%) |
| S406 (RubberBand_ITM3) | 3d | watch | 98 | 67.3 | +63.40 | -56.79 | -43.89 | +874.50 | 56 | 20 | 9 | $+3,531.00 | 15.3% | fat left tail (p10 < -45%) |
| S362 (RubberBand_3DTE) | 3d | watch | 53 | 75.5 | +60.47 | -58.43 | +8.70 | +544.76 | 56 | 4 | 2 | $+1,679.00 | 24.5% | fat left tail (p10 < -45%) |
| S357 (GapDown_21DTE) | 21d | watch | 25 | 80.0 | +57.14 | -74.18 | +47.06 | +78.22 | 56 | 0 | 0 | $+532.00 | 32.0% | fat left tail (p10 < -45%) |
| S404 (GapDown_OTM2) | 3d | watch | 68 | 64.7 | +51.58 | -81.79 | -41.42 | +114.54 | 56 | 21 | 4 | $+1,328.00 | 14.7% | fat left tail (p10 < -45%) |
| S403 (Any_MA50_Touch) | 3d | watch | 64 | 67.2 | +51.19 | -62.10 | -48.04 | +179.60 | 56 | 18 | 9 | $+1,253.00 | 18.8% | fat left tail (p10 < -45%) |
| S353 (GapDown_3DTE) | 3d | watch | 37 | 51.4 | +48.98 | -81.60 | -69.70 | +313.33 | 56 | 0 | 0 | $+247.00 | 27.0% | fat left tail (p10 < -45%) |
| S365 (RubberBand_14DTE) | 14d | watch | 28 | 53.6 | +43.23 | -63.87 | -51.00 | +75.35 | 56 | 6 | 2 | $+95.00 | 46.4% | fat left tail (p10 < -45%) |
| S356 (GapDown_14DTE) | 14d | watch | 27 | 51.9 | +36.00 | -51.16 | -35.65 | +66.60 | 56 | 2 | 0 | $+123.00 | 37.0% | fat left tail (p10 < -45%) |
| S361 (RubberBand_2DTE) | 2d | watch | 56 | 53.6 | +31.30 | -67.59 | -50.00 | +291.66 | 56 | 14 | 1 | $+343.00 | 23.2% | fat left tail (p10 < -45%) |
| S218 (BB_Lower_Touch) | 3d ATM BB lower touch | watch | 106 | 51.9 | +29.29 | -69.05 | -49.77 | +147.50 | 60 | 26 | 15 | $+1,195.00 | 28.3% | fat left tail (p10 < -45%) |
| S412 (RubberBand_OTM3) | 3d | watch | 60 | 50.0 | +15.91 | -52.20 | -47.53 | +138.93 | 56 | 14 | 4 | $+363.00 | 20.0% | fat left tail (p10 < -45%) |
| S350 (GapDown_0DTE) | 0d | watch | 45 | 53.3 | +15.00 | -65.10 | -51.35 | +232.57 | 56 | 6 | 0 | $+714.00 | 28.9% | fat left tail (p10 < -45%) |
| S352 (GapDown_2DTE) | 2d | watch | 52 | 51.9 | +13.04 | -70.77 | -51.36 | +337.15 | 56 | 6 | 2 | $+341.00 | 21.2% | fat left tail (p10 < -45%) |
| S401 (Any_Gap_Down_Small) | 3d | watch | 131 | 51.1 | +8.33 | -84.29 | -50.88 | +233.33 | 56 | 26 | 16 | $+1,090.00 | 24.4% | fat left tail (p10 < -45%) |
| S364 (RubberBand_7DTE) | 7d | watch | 63 | 50.8 | +8.33 | -85.29 | -63.64 | +89.11 | 56 | 8 | 4 | $+69.00 | 39.7% | fat left tail (p10 < -45%) |
| S411 (RubberBand_OTM2) | 3d | watch | 50 | 56.0 | +7.90 | -56.80 | -51.32 | +65.60 | 53 | 12 | 4 | $+1.00 | 18.0% | fat left tail (p10 < -45%) |
| S398 (GapDown_ATM) | 3d | watch | 59 | 52.5 | +3.33 | -68.29 | -53.70 | +176.24 | 56 | 10 | 2 | $+884.00 | 27.1% | fat left tail (p10 < -45%) |
| S358 (GapDown_30DTE) | 30d | watch | 4 | 50.0 | +0.84 | -51.39 | -51.39 | +54.49 | 52 | 0 | 0 | $-21.00 | 50.0% | insufficient sample (<8 exits) |
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
| S367 (RubberBand_30DTE) | 30d | watch | 3 | 0.0 | -48.89 | -50.89 | -50.14 | -29.78 | 52 | 0 | 0 | $-77.00 | 66.7% | insufficient sample (<8 exits) |
| S366 (RubberBand_21DTE) | 21d | watch | 17 | 47.1 | -49.12 | -56.92 | -53.45 | +95.04 | 52 | 2 | 4 | $+5.00 | 52.9% | early sample with non-positive median |
| S400 (Any_Green_Close) | 3d | watch | 6 | 16.7 | -50.00 | -66.67 | -62.50 | +14.93 | 56 | 0 | 0 | $-5.00 | 83.3% | insufficient sample (<8 exits) |
| S202 (GapDown_Monster) | 3d ATM gap-monster | watch | 12 | 0.0 | -56.77 | -73.59 | -65.84 | -38.58 | 59 | 0 | 0 | $-208.00 | 33.3% | early sample with non-positive median |
| S209 (GapDown_Recovery) | 3d ATM gap-recovery | watch | 7 | 0.0 | -64.71 | -80.40 | -68.79 | -50.75 | 58 | 6 | 1 | $-212.00 | 71.4% | insufficient sample (<8 exits) |
| S164 (GapDown ATM 1-DTE — P2B arm) | 1d ATM | drop | 24 | 50.0 | -2.42 | -94.48 | -62.30 | +337.14 | 66 | 14 | 4 | $+433.00 | 25.0% | non-positive median return |
| S210 (MA_Cross_8_21) | 3d ATM MA cross 8/21 | drop | 95 | 48.4 | -6.25 | -71.05 | -51.41 | +82.76 | 60 | 19 | 11 | $-6.00 | 17.9% | non-positive median return |
| S408 (RubberBand_ITM1) | 3d | drop | 62 | 41.9 | -19.79 | -81.48 | -59.81 | +518.18 | 53 | 18 | 4 | $+1,060.00 | 16.1% | non-positive median return |
| S174 (RubberBand long call EOD) | RubberBand (dropped) | drop | 119 | 36.1 | -25.00 | -89.83 | -71.19 | +36.67 | 81 | 0 | 0 | $-1,658.19 | 50.4% | non-positive median return |
| S173 (MomReversal long call) | MomRev | drop | 415 | 37.1 | -31.51 | -77.18 | -62.95 | +101.90 | 81 | 0 | 0 | $+62.64 | 27.5% | non-positive median return |
| S165 (GapDown long call 3 DTE) | 3d ATM | drop | 255 | 32.2 | -35.29 | -63.24 | -53.42 | +93.89 | 81 | 12 | 1 | $-1,276.78 | 25.9% | non-positive median return |
| S355 (GapDown_7DTE) | 7d | drop | 70 | 45.7 | -37.32 | -77.65 | -63.85 | +143.53 | 56 | 12 | 3 | $+389.00 | 37.1% | non-positive median return |
| S405 (GapDown_OTM3) | 3d | drop | 56 | 33.9 | -42.86 | -83.93 | -65.20 | +103.47 | 56 | 0 | 0 | $-118.00 | 26.8% | manually paused — excluded from new entries & reflected P&L |
| S211 (MA_Cross_21_50) | 3d ATM MA cross 21/50 | drop | 56 | 23.2 | -43.65 | -86.66 | -54.73 | +95.51 | 60 | 12 | 7 | $-401.00 | 26.8% | non-positive median return |
| S359 (RubberBand_0DTE) | 0d | drop | 37 | 37.8 | -44.44 | -71.43 | -66.67 | +241.59 | 53 | 10 | 2 | $-95.00 | 27.0% | non-positive median return |
| S207 (GapDown_AtSupport) | 3d ATM gap-support | drop | 37 | 5.4 | -47.06 | -63.64 | -55.71 | -6.06 | 60 | 0 | 0 | $-822.00 | 43.2% | manually paused — excluded from new entries & reflected P&L |
| S217 (RSI_25_Bounce) | 3d ATM RSI<25 bounce | drop | 68 | 35.3 | -47.08 | -78.25 | -59.12 | +112.16 | 60 | 17 | 7 | $+301.00 | 44.1% | non-positive median return |
| S407 (RubberBand_ITM2) | 3d | drop | 38 | 28.9 | -47.73 | -83.88 | -61.54 | +266.42 | 56 | 0 | 0 | $+33.00 | 26.3% | manually paused — excluded from new entries & reflected P&L |
| S351 (GapDown_1DTE) | 1d | drop | 69 | 34.8 | -50.00 | -75.68 | -62.16 | +312.62 | 56 | 12 | 5 | $+310.00 | 18.8% | non-positive median return |
| S399 (GapDown_OTM1) | 3d | drop | 76 | 40.8 | -50.72 | -83.01 | -66.67 | +145.00 | 56 | 14 | 6 | $-90.00 | 21.1% | non-positive median return |
| S354 (GapDown_5DTE) | 5d | drop | 59 | 39.0 | -51.61 | -86.52 | -75.99 | +137.09 | 56 | 11 | 2 | $+85.00 | 33.9% | non-positive median return |
| S216 (RSI_Oversold_Cross) | 3d ATM RSI x30 | drop | 63 | 22.2 | -51.67 | -86.04 | -68.93 | +69.15 | 60 | 13 | 6 | $-784.00 | 25.4% | non-positive median return |
| S203 (GapUp_Fade) | 3d ATM gap-up fade (put) | drop | 40 | 10.0 | -55.91 | -78.77 | -67.43 | -3.10 | 60 | 0 | 0 | $-797.00 | 35.0% | manually paused — excluded from new entries & reflected P&L |
| S360 (RubberBand_1DTE) | 1d | drop | 49 | 10.2 | -56.41 | -81.50 | -70.37 | -6.89 | 56 | 0 | 0 | $-913.00 | 22.4% | manually paused — excluded from new entries & reflected P&L |
| S212 (MA_Bounce_50) | 3d ATM MA bounce 50 | drop | 83 | 13.3 | -68.09 | -98.15 | -81.35 | +51.47 | 60 | 0 | 0 | $-2,246.00 | 34.9% | manually paused — excluded from new entries & reflected P&L |
| S363 (RubberBand_5DTE) | 5d | drop | 39 | 35.9 | -72.31 | -92.31 | -86.78 | +90.80 | 53 | 6 | 1 | $-827.00 | 33.3% | non-positive median return |

## Comparison groups

Experiment arms grouped for side-by-side decisions. INSUFFICIENT if any arm has n<10 exits.

### GapDown DTE comparison

- Status: **OK** | Best median: **S168** (+66.12%) | Best p10: **S165** (-63.24%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S163 | 7d ATM | 23 | +64.86 | -74.16 | -63.09 | 10 | 2 |
| S164 | 1d ATM | 24 | -2.42 | -94.48 | -62.30 | 14 | 4 |
| S165 | 3d ATM | 255 | -35.29 | -63.24 | -53.42 | 12 | 1 |
| S168 | 5d ATM | 22 | +66.12 | -74.26 | -62.57 | 10 | 2 |

### GapDown Strike comparison

- Status: **OK** | Best median: **S167** (+134.06%) | Best p10: **S165** (-63.24%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S165 | 3d ATM | 255 | -35.29 | -63.24 | -53.42 | 12 | 1 |
| S167 | 3d 1-OTM | 14 | +134.06 | -66.92 | -15.02 | 11 | 2 |

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
| S209 | 3d ATM gap-recovery | 7 | -64.71 | -80.40 | -68.79 | 6 | 1 |

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
| S210 | 3d ATM MA cross 8/21 | 95 | -6.25 | -71.05 | -51.41 | 19 | 11 |
| S211 | 3d ATM MA cross 21/50 | 56 | -43.65 | -86.66 | -54.73 | 12 | 7 |
| S212 | 3d ATM MA bounce 50 | 83 | -68.09 | -98.15 | -81.35 | 0 | 0 |
| S213 | 3d ATM MA bounce 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S215 | 3d ATM MA reclaim 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 RSI/BB/Vol

- Status: **INSUFFICIENT** | Best median: **S218** (+29.29%) | Best p10: **S219** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S216 | 3d ATM RSI x30 | 63 | -51.67 | -86.04 | -68.93 | 13 | 6 |
| S217 | 3d ATM RSI<25 bounce | 68 | -47.08 | -78.25 | -59.12 | 17 | 7 |
| S218 | 3d ATM BB lower touch | 106 | +29.29 | -69.05 | -49.77 | 26 | 15 |
| S219 | 3d ATM vol climax up | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Other

- Status: **OK** | Best median: **S173** (-31.51%) | Best p10: **S173** (-77.18%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S173 | MomRev | 415 | -31.51 | -77.18 | -62.95 | 0 | 0 |

## Strategy Pipeline Status

_Pipeline evaluation as of 2026-09-25. Auto-kill thresholds: median<-25% at n>=15, p10<-85%, WR<15% at n>=25. Promote: n>=30 median>0%._

| Strategy | Signal | n | Median% | WR% | Status | Days |
|----------|--------|---|---------|-----|--------|------|
| S163 | A1 GapDown ATM call EO | 23 | +64.86% | 65% | INSUFFICIENT | 66 |
| S164 | GapDown ATM 1-DTE — P2 | 24 | -2.42% | 50% | INSUFFICIENT | 66 |
| S165 | GapDown long call 3 DT | 255 | -35.29% | 32% | INSUFFICIENT | 81 |
| S166 | GapDown strong call | 8 | +75.23% | 100% | WATCH | 66 |
| S167 | GapDown long call 3 DT | 14 | +134.06% | 71% | WATCH | 66 |
| S168 | GapDown ATM 5-DTE — P2 | 22 | +66.12% | 64% | INSUFFICIENT | 66 |
| S169 | BB Squeeze Breakout ca | 0 | — | — | NEW | 0 |
| S170 | Golden Pocket call 3 D | 0 | — | — | NEW | 0 |
| S171 | VWAP Reclaim call 3 DT | 0 | — | — | NEW | 0 |
| S172 | Trend Resumption call  | 0 | — | — | NEW | 0 |
| S173 | MomReversal long call | 415 | -31.51% | 37% | INSUFFICIENT | 81 |
| S174 | RubberBand long call E | 119 | -25.00% | 36% | INSUFFICIENT | 81 |
| S175 | Earnings Drift call 3  | 0 | — | — | NEW | 0 |
| S200 | GapDown_Aggressive | 0 | — | — | NEW | 0 |
| S201 | GapDown_Mild | 0 | — | — | NEW | 0 |
| S202 | GapDown_Monster | 12 | -56.77% | 0% | WATCH | 59 |
| S203 | GapUp_Fade | 40 | -55.91% | 10% | INSUFFICIENT | 60 |
| S204 | GapUp_Continuation | 0 | — | — | NEW | 0 |
| S205 | GapDown_HighVol | 0 | — | — | NEW | 0 |
| S206 | GapDown_WithTrend | 0 | — | — | NEW | 0 |
| S207 | GapDown_AtSupport | 37 | -47.06% | 5% | INSUFFICIENT | 60 |
| S208 | GapDown_AboveMA200 | 0 | — | — | NEW | 0 |
| S209 | GapDown_Recovery | 7 | -64.71% | 0% | WATCH | 58 |
| S210 | MA_Cross_8_21 | 95 | -6.25% | 48% | INSUFFICIENT | 60 |
| S211 | MA_Cross_21_50 | 56 | -43.65% | 23% | INSUFFICIENT | 60 |
| S212 | MA_Bounce_50 | 83 | -68.09% | 13% | INSUFFICIENT | 60 |
| S213 | MA_Bounce_200 | 0 | — | — | NEW | 0 |
| S214 | MA_Death_Cross | 0 | — | — | NEW | 0 |
| S215 | MA_Reclaim_200 | 0 | — | — | NEW | 0 |
| S216 | RSI_Oversold_Cross | 63 | -51.67% | 22% | INSUFFICIENT | 60 |
| S217 | RSI_25_Bounce | 68 | -47.08% | 35% | INSUFFICIENT | 60 |
| S218 | BB_Lower_Touch | 106 | +29.29% | 52% | INSUFFICIENT | 60 |
| S219 | Volume_Climax_Up | 0 | — | — | NEW | 0 |
| S220 | Pullback50 | 0 | — | — | NEW | 0 |
| S221 | GoldenPocket | 0 | — | — | NEW | 0 |
| S350 | GapDown_0DTE | 45 | +15.00% | 53% | INSUFFICIENT | 56 |
| S351 | GapDown_1DTE | 69 | -50.00% | 35% | INSUFFICIENT | 56 |
| S352 | GapDown_2DTE | 52 | +13.04% | 52% | INSUFFICIENT | 56 |
| S353 | GapDown_3DTE | 37 | +48.98% | 51% | INSUFFICIENT | 56 |
| S354 | GapDown_5DTE | 59 | -51.61% | 39% | INSUFFICIENT | 56 |
| S355 | GapDown_7DTE | 70 | -37.32% | 46% | INSUFFICIENT | 56 |
| S356 | GapDown_14DTE | 27 | +36.00% | 52% | INSUFFICIENT | 56 |
| S357 | GapDown_21DTE | 25 | +57.14% | 80% | INSUFFICIENT | 56 |
| S358 | GapDown_30DTE | 4 | +0.84% | 50% | WATCH | 52 |
| S359 | RubberBand_0DTE | 37 | -44.44% | 38% | INSUFFICIENT | 53 |
| S360 | RubberBand_1DTE | 49 | -56.41% | 10% | INSUFFICIENT | 56 |
| S361 | RubberBand_2DTE | 56 | +31.30% | 54% | INSUFFICIENT | 56 |
| S362 | RubberBand_3DTE | 53 | +60.47% | 75% | INSUFFICIENT | 56 |
| S363 | RubberBand_5DTE | 39 | -72.31% | 36% | INSUFFICIENT | 53 |
| S364 | RubberBand_7DTE | 63 | +8.33% | 51% | INSUFFICIENT | 56 |
| S365 | RubberBand_14DTE | 28 | +43.23% | 54% | INSUFFICIENT | 56 |
| S366 | RubberBand_21DTE | 17 | -49.12% | 47% | INSUFFICIENT | 52 |
| S367 | RubberBand_30DTE | 3 | -48.89% | 0% | WATCH | 52 |
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
| S396 | GapDown_ITM2 | 7 | +87.50% | 86% | WATCH | 50 |
| S397 | GapDown_ITM1 | 39 | +66.67% | 74% | INSUFFICIENT | 56 |
| S398 | GapDown_ATM | 59 | +3.33% | 53% | INSUFFICIENT | 56 |
| S399 | GapDown_OTM1 | 76 | -50.72% | 41% | INSUFFICIENT | 56 |
| S400 | Any_Green_Close | 6 | -50.00% | 17% | WATCH | 56 |
| S401 | Any_Gap_Down_Small | 131 | +8.33% | 51% | INSUFFICIENT | 56 |
| S402 | Any_High_Volume | 0 | — | — | NEW | 0 |
| S403 | Any_MA50_Touch | 64 | +51.19% | 67% | INSUFFICIENT | 56 |
| S404 | GapDown_OTM2 | 68 | +51.58% | 65% | INSUFFICIENT | 56 |
| S405 | GapDown_OTM3 | 56 | -42.86% | 34% | INSUFFICIENT | 56 |
| S406 | RubberBand_ITM3 | 98 | +63.40% | 67% | INSUFFICIENT | 56 |
| S407 | RubberBand_ITM2 | 38 | -47.73% | 29% | INSUFFICIENT | 56 |
| S408 | RubberBand_ITM1 | 62 | -19.79% | 42% | INSUFFICIENT | 53 |
| S409 | RubberBand_ATM | 2 | +81.94% | 100% | WATCH | 1 |
| S410 | RubberBand_OTM1 | 10 | +67.85% | 70% | WATCH | 50 |
| S411 | RubberBand_OTM2 | 50 | +7.90% | 56% | INSUFFICIENT | 53 |
| S412 | RubberBand_OTM3 | 60 | +15.91% | 50% | INSUFFICIENT | 56 |
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
| S397 | 39 | +66.67% | 74% | Tyler review |
| S406 | 98 | +63.40% | 67% | Tyler review |
| S362 | 53 | +60.47% | 75% | Tyler review |
| S404 | 68 | +51.58% | 65% | Tyler review |
| S403 | 64 | +51.19% | 67% | Tyler review |
| S353 | 37 | +48.98% | 51% | Tyler review |
| S361 | 56 | +31.30% | 54% | Tyler review |
| S218 | 106 | +29.29% | 52% | Tyler review |
| S412 | 60 | +15.91% | 50% | Tyler review |
| S350 | 45 | +15.00% | 53% | Tyler review |
| S352 | 52 | +13.04% | 52% | Tyler review |
| S401 | 131 | +8.33% | 51% | Tyler review |
| S364 | 63 | +8.33% | 51% | Tyler review |
| S411 | 50 | +7.90% | 56% | Tyler review |
| S398 | 59 | +3.33% | 53% | Tyler review |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- **p25** sits between p10 and median for mid-tail visibility.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
- Active paper strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419.
