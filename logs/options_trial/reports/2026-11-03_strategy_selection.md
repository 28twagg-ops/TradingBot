# Options strategy selection report — 2026-11-03

_Generated 2026-11-03T10:52:57.865564_

## Summary

- Strategies analyzed: **108**
- Keep: **0**
- Watch: **70**
- Drop: **38**

## Attribution health

- Total exits: **3867**
- Orphan exits (b0/orphan_reconcile): **422**
- Orphan rate: **10.9%** (warn if >10%)
- **ALERT:** orphan_rate > 10% — check client_order_id tagging / fill attribution before trusting strategy P&L.

## Strategy scoreboard

| strategy | DTE | rec | exits | win% | med% | p10% | p25% | p90% | days live | ent 5d | exit 5d | realized $ | top share | rationale |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S409 (RubberBand_ATM) | 3d | watch | 2 | 100.0 | +81.94 | +79.72 | +80.56 | +84.17 | 40 | 0 | 0 | $+118.00 | 100.0% | insufficient sample (<8 exits) |
| S410 (RubberBand_OTM1) | 3d | watch | 11 | 63.6 | +65.28 | -68.49 | -58.43 | +101.49 | 89 | 0 | 0 | $+192.00 | 72.7% | building sample (8-19 exits) |
| S166 (GapDown strong call) | 3d ATM strong | watch | 18 | 61.1 | +60.78 | -67.83 | -49.76 | +142.86 | 105 | 2 | 2 | $+394.00 | 27.8% | building sample (8-19 exits) |
| S396 (GapDown_ITM2) | 3d | watch | 14 | 64.3 | +55.64 | -55.79 | -50.51 | +95.00 | 89 | 1 | 1 | $+257.00 | 78.6% | building sample (8-19 exits) |
| S357 (GapDown_21DTE) | 21d | watch | 31 | 71.0 | +52.94 | -74.47 | -48.25 | +73.68 | 95 | 0 | 1 | $+475.00 | 32.3% | fat left tail (p10 < -45%) |
| S397 (GapDown_ITM1) | 3d | watch | 53 | 62.3 | +51.39 | -64.56 | -52.38 | +116.19 | 95 | 1 | 1 | $+1,108.00 | 17.0% | fat left tail (p10 < -45%) |
| S403 (Any_MA50_Touch) | 3d | watch | 80 | 61.2 | +50.88 | -64.85 | -50.00 | +172.15 | 95 | 0 | 0 | $+1,265.00 | 15.0% | fat left tail (p10 < -45%) |
| S362 (RubberBand_3DTE) | 3d | watch | 67 | 64.2 | +50.00 | -61.56 | -50.84 | +315.24 | 95 | 1 | 2 | $+1,367.00 | 19.4% | fat left tail (p10 < -45%) |
| S406 (RubberBand_ITM3) | 3d | watch | 156 | 53.2 | +40.97 | -59.55 | -47.45 | +207.89 | 95 | 4 | 2 | $+3,063.00 | 10.3% | fat left tail (p10 < -45%) |
| S218 (BB_Lower_Touch) | 3d ATM BB lower touch | watch | 109 | 50.5 | +22.22 | -71.43 | -50.00 | +146.00 | 99 | 0 | 0 | $+1,086.00 | 27.5% | fat left tail (p10 < -45%) |
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
| S402 (Any_High_Volume) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S413 (BBSqueeze_ITM3) | 0d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S414 (BBSqueeze_ITM2) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S415 (BBSqueeze_ITM1) | 7d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S416 (BBSqueeze_ATM) | 0d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S417 (BBSqueeze_OTM1) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S418 (BBSqueeze_OTM2) | 7d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S419 (BBSqueeze_OTM3) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S431 (DayTrader_RS) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S432 (DayTrader_ORB_RS) | 3d | watch | 11 | 36.4 | -37.50 | -50.00 | -45.16 | +72.73 | 18 | 2 | 2 | $-26.00 | 9.1% | early sample with non-positive median |
| S430 (DayTrader_ORB) | 3d | watch | 11 | 27.3 | -40.00 | -42.55 | -40.34 | +67.57 | 18 | 3 | 2 | $-76.00 | 18.2% | early sample with non-positive median |
| S367 (RubberBand_30DTE) | 30d | watch | 3 | 0.0 | -48.89 | -50.89 | -50.14 | -29.78 | 91 | 0 | 0 | $-77.00 | 66.7% | insufficient sample (<8 exits) |
| S400 (Any_Green_Close) | 3d | watch | 6 | 16.7 | -50.00 | -66.67 | -62.50 | +14.93 | 95 | 0 | 0 | $-5.00 | 83.3% | insufficient sample (<8 exits) |
| S358 (GapDown_30DTE) | 30d | watch | 5 | 40.0 | -50.00 | -51.39 | -51.39 | +54.28 | 91 | 0 | 0 | $-49.00 | 40.0% | insufficient sample (<8 exits) |
| S209 (GapDown_Recovery) | 3d ATM gap-recovery | watch | 7 | 0.0 | -64.71 | -80.40 | -68.79 | -50.75 | 97 | 0 | 0 | $-212.00 | 71.4% | insufficient sample (<8 exits) |
| S395 (GapDown_ITM3) | 3d | watch | 1 | 0.0 | -68.75 | -68.75 | -68.75 | -68.75 | 20 | 0 | 0 | $-44.00 | 100.0% | insufficient sample (<8 exits) |
| S401 (Any_Gap_Down_Small) | 3d | drop | 135 | 49.6 | +0.00 | -84.10 | -51.33 | +230.91 | 95 | 0 | 0 | $+928.00 | 23.7% | non-positive median return |
| S350 (GapDown_0DTE) | 0d | drop | 56 | 48.2 | +0.00 | -66.67 | -50.34 | +176.97 | 95 | 2 | 2 | $+753.00 | 26.8% | non-positive median return |
| S365 (RubberBand_14DTE) | 14d | drop | 39 | 48.7 | +0.00 | -64.65 | -52.00 | +68.61 | 95 | 1 | 1 | $-11.00 | 35.9% | non-positive median return |
| S412 (RubberBand_OTM3) | 3d | drop | 68 | 44.1 | -3.57 | -58.23 | -50.00 | +125.40 | 95 | 0 | 0 | $+184.00 | 17.6% | non-positive median return |
| S364 (RubberBand_7DTE) | 7d | drop | 72 | 48.6 | -4.41 | -85.27 | -59.66 | +82.88 | 95 | 1 | 2 | $+28.00 | 36.1% | non-positive median return |
| S408 (RubberBand_ITM1) | 3d | drop | 67 | 43.3 | -6.25 | -81.48 | -59.63 | +573.13 | 92 | 0 | 0 | $+1,137.00 | 17.9% | manually paused — excluded from new entries & reflected P&L |
| S210 (MA_Cross_8_21) | 3d ATM MA cross 8/21 | drop | 112 | 46.4 | -6.38 | -70.87 | -51.75 | +82.83 | 99 | 1 | 0 | $+26.00 | 16.1% | non-positive median return |
| S361 (RubberBand_2DTE) | 2d | drop | 71 | 46.5 | -8.33 | -68.52 | -53.52 | +261.11 | 95 | 1 | 1 | $+85.00 | 18.3% | non-positive median return |
| S404 (GapDown_OTM2) | 3d | drop | 103 | 49.5 | -10.00 | -66.28 | -49.58 | +98.31 | 95 | 4 | 5 | $+835.00 | 9.7% | non-positive median return |
| S398 (GapDown_ATM) | 3d | drop | 65 | 47.7 | -18.42 | -68.25 | -55.56 | +168.45 | 95 | 0 | 0 | $+765.00 | 24.6% | non-positive median return |
| S356 (GapDown_14DTE) | 14d | drop | 35 | 48.6 | -18.92 | -51.33 | -48.95 | +58.62 | 95 | 1 | 1 | $+110.00 | 40.0% | non-positive median return |
| S174 (RubberBand long call EOD) | RubberBand (dropped) | drop | 119 | 36.1 | -25.00 | -89.83 | -71.19 | +36.67 | 120 | 0 | 0 | $-1,658.19 | 50.4% | non-positive median return |
| S411 (RubberBand_OTM2) | 3d | drop | 65 | 47.7 | -28.57 | -58.21 | -52.17 | +60.83 | 92 | 1 | 1 | $-223.00 | 15.4% | non-positive median return |
| S173 (MomReversal long call) | MomRev | drop | 415 | 37.1 | -31.51 | -77.18 | -62.95 | +101.90 | 120 | 0 | 0 | $+62.64 | 27.5% | non-positive median return |
| S165 (GapDown long call 3 DTE) | 3d ATM | drop | 255 | 32.2 | -35.29 | -63.24 | -53.42 | +93.89 | 120 | 0 | 0 | $-1,276.78 | 25.9% | non-positive median return |
| S355 (GapDown_7DTE) | 7d | drop | 71 | 45.1 | -37.50 | -77.08 | -63.70 | +138.64 | 95 | 0 | 0 | $+367.00 | 38.0% | manually paused — excluded from new entries & reflected P&L |
| S352 (GapDown_2DTE) | 2d | drop | 67 | 44.8 | -38.24 | -72.86 | -52.34 | +302.85 | 95 | 2 | 1 | $+226.00 | 16.4% | non-positive median return |
| S359 (RubberBand_0DTE) | 0d | drop | 50 | 42.0 | -41.86 | -71.43 | -62.96 | +164.28 | 92 | 1 | 1 | $+47.00 | 20.0% | non-positive median return |
| S405 (GapDown_OTM3) | 3d | drop | 56 | 33.9 | -42.86 | -83.93 | -65.20 | +103.47 | 95 | 0 | 0 | $-118.00 | 26.8% | manually paused — excluded from new entries & reflected P&L |
| S211 (MA_Cross_21_50) | 3d ATM MA cross 21/50 | drop | 56 | 23.2 | -43.65 | -86.66 | -54.73 | +95.51 | 99 | 0 | 0 | $-401.00 | 26.8% | manually paused — excluded from new entries & reflected P&L |
| S167 (GapDown long call 3 DTE 1-OTM — P2C) | 3d 1-OTM | drop | 27 | 48.1 | -45.00 | -71.88 | -55.46 | +325.71 | 105 | 3 | 2 | $+351.00 | 25.9% | non-positive median return |
| S353 (GapDown_3DTE) | 3d | drop | 45 | 42.2 | -46.15 | -82.61 | -69.70 | +264.21 | 95 | 0 | 0 | $+125.00 | 22.2% | non-positive median return |
| S207 (GapDown_AtSupport) | 3d ATM gap-support | drop | 37 | 5.4 | -47.06 | -63.64 | -55.71 | -6.06 | 99 | 0 | 0 | $-822.00 | 43.2% | manually paused — excluded from new entries & reflected P&L |
| S407 (RubberBand_ITM2) | 3d | drop | 38 | 28.9 | -47.73 | -83.88 | -61.54 | +266.42 | 95 | 0 | 0 | $+33.00 | 26.3% | manually paused — excluded from new entries & reflected P&L |
| S163 (A1 GapDown ATM call EOD) | 7d ATM | drop | 41 | 48.8 | -48.65 | -74.47 | -60.00 | +85.92 | 105 | 3 | 3 | $+239.00 | 36.6% | non-positive median return |
| S164 (GapDown ATM 1-DTE — P2B arm) | 1d ATM | drop | 45 | 42.2 | -48.89 | -88.89 | -53.57 | +180.00 | 105 | 2 | 2 | $+307.00 | 15.6% | non-positive median return |
| S366 (RubberBand_21DTE) | 21d | drop | 21 | 42.9 | -49.12 | -56.92 | -53.45 | +94.34 | 91 | 0 | 0 | $-63.00 | 42.9% | manually paused — excluded from new entries & reflected P&L |
| S217 (RSI_25_Bounce) | 3d ATM RSI<25 bounce | drop | 75 | 33.3 | -49.18 | -79.00 | -60.00 | +99.05 | 99 | 0 | 0 | $+158.00 | 40.0% | manually paused — excluded from new entries & reflected P&L |
| S351 (GapDown_1DTE) | 1d | drop | 75 | 37.3 | -50.00 | -75.68 | -62.03 | +264.88 | 95 | 0 | 0 | $+414.00 | 17.3% | manually paused — excluded from new entries & reflected P&L |
| S168 (GapDown ATM 5-DTE — P2B arm) | 5d ATM | drop | 36 | 41.7 | -50.00 | -74.73 | -54.97 | +229.62 | 105 | 3 | 4 | $+184.00 | 38.9% | non-positive median return |
| S399 (GapDown_OTM1) | 3d | drop | 80 | 38.8 | -50.72 | -83.55 | -66.67 | +141.00 | 95 | 0 | 0 | $-170.00 | 20.0% | non-positive median return |
| S354 (GapDown_5DTE) | 5d | drop | 66 | 36.4 | -51.96 | -84.87 | -75.26 | +135.12 | 95 | 0 | 0 | $+23.00 | 30.3% | manually paused — excluded from new entries & reflected P&L |
| S216 (RSI_Oversold_Cross) | 3d ATM RSI x30 | drop | 70 | 20.0 | -51.97 | -82.35 | -70.00 | +66.98 | 99 | 0 | 0 | $-1,020.00 | 22.9% | manually paused — excluded from new entries & reflected P&L |
| S203 (GapUp_Fade) | 3d ATM gap-up fade (put) | drop | 40 | 10.0 | -55.91 | -78.77 | -67.43 | -3.10 | 99 | 0 | 0 | $-797.00 | 35.0% | manually paused — excluded from new entries & reflected P&L |
| S360 (RubberBand_1DTE) | 1d | drop | 49 | 10.2 | -56.41 | -81.50 | -70.37 | -6.89 | 95 | 0 | 0 | $-913.00 | 22.4% | manually paused — excluded from new entries & reflected P&L |
| S202 (GapDown_Monster) | 3d ATM gap-monster | drop | 14 | 0.0 | -60.53 | -80.50 | -72.44 | -39.53 | 98 | 0 | 0 | $-237.00 | 28.6% | manually paused — excluded from new entries & reflected P&L |
| S363 (RubberBand_5DTE) | 5d | drop | 41 | 39.0 | -65.38 | -92.31 | -85.11 | +90.62 | 92 | 0 | 0 | $-739.00 | 31.7% | manually paused — excluded from new entries & reflected P&L |
| S212 (MA_Bounce_50) | 3d ATM MA bounce 50 | drop | 83 | 13.3 | -68.09 | -98.15 | -81.35 | +51.47 | 99 | 0 | 0 | $-2,246.00 | 34.9% | manually paused — excluded from new entries & reflected P&L |

## Comparison groups

Experiment arms grouped for side-by-side decisions. INSUFFICIENT if any arm has n<10 exits.

### GapDown DTE comparison

- Status: **OK** | Best median: **S165** (-35.29%) | Best p10: **S165** (-63.24%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S163 | 7d ATM | 41 | -48.65 | -74.47 | -60.00 | 3 | 3 |
| S164 | 1d ATM | 45 | -48.89 | -88.89 | -53.57 | 2 | 2 |
| S165 | 3d ATM | 255 | -35.29 | -63.24 | -53.42 | 0 | 0 |
| S168 | 5d ATM | 36 | -50.00 | -74.73 | -54.97 | 3 | 4 |

### GapDown Strike comparison

- Status: **OK** | Best median: **S165** (-35.29%) | Best p10: **S165** (-63.24%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S165 | 3d ATM | 255 | -35.29 | -63.24 | -53.42 | 0 | 0 |
| S167 | 3d 1-OTM | 27 | -45.00 | -71.88 | -55.46 | 3 | 2 |

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
| S210 | 3d ATM MA cross 8/21 | 112 | -6.38 | -70.87 | -51.75 | 1 | 0 |
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

_Pipeline evaluation as of 2026-11-03. Auto-kill thresholds: median<-25% at n>=15, p10<-85%, WR<15% at n>=25. Promote: n>=30 median>0%._

| Strategy | Signal | n | Median% | WR% | Status | Days |
|----------|--------|---|---------|-----|--------|------|
| S163 | A1 GapDown ATM call EO | 41 | -48.65% | 49% | INSUFFICIENT | 105 |
| S164 | GapDown ATM 1-DTE — P2 | 45 | -48.89% | 42% | INSUFFICIENT | 105 |
| S165 | GapDown long call 3 DT | 255 | -35.29% | 32% | INSUFFICIENT | 120 |
| S166 | GapDown strong call | 18 | +60.78% | 61% | INSUFFICIENT | 105 |
| S167 | GapDown long call 3 DT | 27 | -45.00% | 48% | INSUFFICIENT | 105 |
| S168 | GapDown ATM 5-DTE — P2 | 36 | -50.00% | 42% | INSUFFICIENT | 105 |
| S169 | BB Squeeze Breakout ca | 0 | — | — | NEW | 0 |
| S170 | Golden Pocket call 3 D | 0 | — | — | NEW | 0 |
| S171 | VWAP Reclaim call 3 DT | 0 | — | — | NEW | 0 |
| S172 | Trend Resumption call  | 0 | — | — | NEW | 0 |
| S173 | MomReversal long call | 415 | -31.51% | 37% | INSUFFICIENT | 120 |
| S174 | RubberBand long call E | 119 | -25.00% | 36% | INSUFFICIENT | 120 |
| S175 | Earnings Drift call 3  | 0 | — | — | NEW | 0 |
| S200 | GapDown_Aggressive | 0 | — | — | NEW | 0 |
| S201 | GapDown_Mild | 0 | — | — | NEW | 0 |
| S202 | GapDown_Monster | 14 | -60.53% | 0% | WATCH | 98 |
| S203 | GapUp_Fade | 40 | -55.91% | 10% | INSUFFICIENT | 99 |
| S204 | GapUp_Continuation | 0 | — | — | NEW | 0 |
| S205 | GapDown_HighVol | 0 | — | — | NEW | 0 |
| S206 | GapDown_WithTrend | 0 | — | — | NEW | 0 |
| S207 | GapDown_AtSupport | 37 | -47.06% | 5% | INSUFFICIENT | 99 |
| S208 | GapDown_AboveMA200 | 0 | — | — | NEW | 0 |
| S209 | GapDown_Recovery | 7 | -64.71% | 0% | WATCH | 97 |
| S210 | MA_Cross_8_21 | 112 | -6.38% | 46% | INSUFFICIENT | 99 |
| S211 | MA_Cross_21_50 | 56 | -43.65% | 23% | INSUFFICIENT | 99 |
| S212 | MA_Bounce_50 | 83 | -68.09% | 13% | INSUFFICIENT | 99 |
| S213 | MA_Bounce_200 | 0 | — | — | NEW | 0 |
| S214 | MA_Death_Cross | 0 | — | — | NEW | 0 |
| S215 | MA_Reclaim_200 | 0 | — | — | NEW | 0 |
| S216 | RSI_Oversold_Cross | 70 | -51.97% | 20% | INSUFFICIENT | 99 |
| S217 | RSI_25_Bounce | 75 | -49.18% | 33% | INSUFFICIENT | 99 |
| S218 | BB_Lower_Touch | 109 | +22.22% | 50% | INSUFFICIENT | 99 |
| S219 | Volume_Climax_Up | 0 | — | — | NEW | 0 |
| S220 | Pullback50 | 0 | — | — | NEW | 0 |
| S221 | GoldenPocket | 0 | — | — | NEW | 0 |
| S350 | GapDown_0DTE | 56 | +0.00% | 48% | INSUFFICIENT | 95 |
| S351 | GapDown_1DTE | 75 | -50.00% | 37% | INSUFFICIENT | 95 |
| S352 | GapDown_2DTE | 67 | -38.24% | 45% | INSUFFICIENT | 95 |
| S353 | GapDown_3DTE | 45 | -46.15% | 42% | INSUFFICIENT | 95 |
| S354 | GapDown_5DTE | 66 | -51.96% | 36% | INSUFFICIENT | 95 |
| S355 | GapDown_7DTE | 71 | -37.50% | 45% | INSUFFICIENT | 95 |
| S356 | GapDown_14DTE | 35 | -18.92% | 49% | INSUFFICIENT | 95 |
| S357 | GapDown_21DTE | 31 | +52.94% | 71% | INSUFFICIENT | 95 |
| S358 | GapDown_30DTE | 5 | -50.00% | 40% | WATCH | 91 |
| S359 | RubberBand_0DTE | 50 | -41.86% | 42% | INSUFFICIENT | 92 |
| S360 | RubberBand_1DTE | 49 | -56.41% | 10% | INSUFFICIENT | 95 |
| S361 | RubberBand_2DTE | 71 | -8.33% | 46% | INSUFFICIENT | 95 |
| S362 | RubberBand_3DTE | 67 | +50.00% | 64% | INSUFFICIENT | 95 |
| S363 | RubberBand_5DTE | 41 | -65.38% | 39% | INSUFFICIENT | 92 |
| S364 | RubberBand_7DTE | 72 | -4.41% | 49% | INSUFFICIENT | 95 |
| S365 | RubberBand_14DTE | 39 | +0.00% | 49% | INSUFFICIENT | 95 |
| S366 | RubberBand_21DTE | 21 | -49.12% | 43% | INSUFFICIENT | 91 |
| S367 | RubberBand_30DTE | 3 | -48.89% | 0% | WATCH | 91 |
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
| S395 | GapDown_ITM3 | 1 | -68.75% | 0% | WATCH | 20 |
| S396 | GapDown_ITM2 | 14 | +55.64% | 64% | WATCH | 89 |
| S397 | GapDown_ITM1 | 53 | +51.39% | 62% | INSUFFICIENT | 95 |
| S398 | GapDown_ATM | 65 | -18.42% | 48% | INSUFFICIENT | 95 |
| S399 | GapDown_OTM1 | 80 | -50.72% | 39% | INSUFFICIENT | 95 |
| S400 | Any_Green_Close | 6 | -50.00% | 17% | WATCH | 95 |
| S401 | Any_Gap_Down_Small | 135 | +0.00% | 50% | INSUFFICIENT | 95 |
| S402 | Any_High_Volume | 0 | — | — | NEW | 0 |
| S403 | Any_MA50_Touch | 80 | +50.88% | 61% | INSUFFICIENT | 95 |
| S404 | GapDown_OTM2 | 103 | -10.00% | 50% | INSUFFICIENT | 95 |
| S405 | GapDown_OTM3 | 56 | -42.86% | 34% | INSUFFICIENT | 95 |
| S406 | RubberBand_ITM3 | 156 | +40.97% | 53% | INSUFFICIENT | 95 |
| S407 | RubberBand_ITM2 | 38 | -47.73% | 29% | INSUFFICIENT | 95 |
| S408 | RubberBand_ITM1 | 67 | -6.25% | 43% | INSUFFICIENT | 92 |
| S409 | RubberBand_ATM | 2 | +81.94% | 100% | WATCH | 40 |
| S410 | RubberBand_OTM1 | 11 | +65.28% | 64% | WATCH | 89 |
| S411 | RubberBand_OTM2 | 65 | -28.57% | 48% | INSUFFICIENT | 92 |
| S412 | RubberBand_OTM3 | 68 | -3.57% | 44% | INSUFFICIENT | 95 |
| S413 | BBSqueeze_ITM3 | 0 | — | — | NEW | 0 |
| S414 | BBSqueeze_ITM2 | 0 | — | — | NEW | 0 |
| S415 | BBSqueeze_ITM1 | 0 | — | — | NEW | 0 |
| S416 | BBSqueeze_ATM | 0 | — | — | NEW | 0 |
| S417 | BBSqueeze_OTM1 | 0 | — | — | NEW | 0 |
| S418 | BBSqueeze_OTM2 | 0 | — | — | NEW | 0 |
| S419 | BBSqueeze_OTM3 | 0 | — | — | NEW | 0 |
| S430 | DayTrader_ORB | 11 | -40.00% | 27% | WATCH | 18 |
| S431 | DayTrader_RS | 0 | — | — | NEW | 0 |
| S432 | DayTrader_ORB_RS | 11 | -37.50% | 36% | WATCH | 18 |

## Auto-Kill Log

| Date | Strategy | Reason | n | Median% |
|------|----------|--------|---|---------|
| — | — | (no kills yet) | — | — |

## Promote Candidates (n>=30, median>0%)

| Strategy | n | Median% | WR% | Recommendation |
|----------|---|---------|-----|----------------|
| S357 | 31 | +52.94% | 71% | Tyler review |
| S397 | 53 | +51.39% | 62% | Tyler review |
| S403 | 80 | +50.88% | 61% | Tyler review |
| S362 | 67 | +50.00% | 64% | Tyler review |
| S406 | 156 | +40.97% | 53% | Tyler review |
| S218 | 109 | +22.22% | 50% | Tyler review |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- **p25** sits between p10 and median for mid-tail visibility.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
- Active paper strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419, S430, S431, S432.
