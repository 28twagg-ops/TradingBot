# Options strategy selection report — 2026-07-29

_Generated 2026-07-29T18:05:49.240451_

## Summary

- Strategies analyzed: **103**
- Keep: **0**
- Watch: **100**
- Drop: **3**

## Attribution health

- Total exits: **811**
- Orphan exits (b0/orphan_reconcile): **22**
- Orphan rate: **2.7%** (warn if >10%)
- Orphan rate OK (attribution looks healthy).

## Strategy scoreboard

| strategy | DTE | rec | exits | win% | med% | p10% | p25% | p90% | days live | ent 5d | exit 5d | realized $ | top share | rationale |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S163 (A1 GapDown ATM call EOD) | 7d ATM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 8 | 18 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | 3d ATM strong | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 8 | 16 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S167 (GapDown long call 3 DTE 1-OTM — P2C) | 3d 1-OTM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 8 | 22 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S168 (GapDown ATM 5-DTE — P2B arm) | 5d ATM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 8 | 18 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S169 (BB Squeeze Breakout call 3 DTE) | 3d ATM BB squeeze | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S170 (Golden Pocket call 3 DTE) | 3d ATM golden pocket | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S171 (VWAP Reclaim call 3 DTE) | 3d ATM VWAP reclaim | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S172 (Trend Resumption call 3 DTE) | 3d ATM trend resume | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S175 (Earnings Drift call 3 DTE) | 3d ATM earnings drift | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S200 (GapDown_Aggressive) | 3d ATM gap-aggr | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S201 (GapDown_Mild) | 3d ATM gap-mild | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S203 (GapUp_Fade) | 3d ATM gap-up fade (put) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 2 | 8 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S204 (GapUp_Continuation) | 3d ATM gap-up cont | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S205 (GapDown_HighVol) | 3d ATM gap-highvol | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S206 (GapDown_WithTrend) | 3d ATM gap-trend | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S207 (GapDown_AtSupport) | 3d ATM gap-support | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 2 | 12 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S208 (GapDown_AboveMA200) | 3d ATM gap-ma200 | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S209 (GapDown_Recovery) | 3d ATM gap-recovery | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 0 | 6 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S210 (MA_Cross_8_21) | 3d ATM MA cross 8/21 | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 2 | 15 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S211 (MA_Cross_21_50) | 3d ATM MA cross 21/50 | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 2 | 10 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S212 (MA_Bounce_50) | 3d ATM MA bounce 50 | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 2 | 18 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S213 (MA_Bounce_200) | 3d ATM MA bounce 200 | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S214 (MA_Death_Cross) | 3d ATM death cross (put) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S215 (MA_Reclaim_200) | 3d ATM MA reclaim 200 | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S216 (RSI_Oversold_Cross) | 3d ATM RSI x30 | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 2 | 20 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S217 (RSI_25_Bounce) | 3d ATM RSI<25 bounce | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 2 | 10 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S219 (Volume_Climax_Up) | 3d ATM vol climax up | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S350 (GapDown_0DTE) | 0d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S351 (GapDown_1DTE) | 1d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S352 (GapDown_2DTE) | 2d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S353 (GapDown_3DTE) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S354 (GapDown_5DTE) | 5d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S355 (GapDown_7DTE) | 7d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S356 (GapDown_14DTE) | 14d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S357 (GapDown_21DTE) | 21d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S358 (GapDown_30DTE) | 30d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S359 (RubberBand_0DTE) | 0d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S360 (RubberBand_1DTE) | 1d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S361 (RubberBand_2DTE) | 2d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S362 (RubberBand_3DTE) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S363 (RubberBand_5DTE) | 5d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S364 (RubberBand_7DTE) | 7d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S365 (RubberBand_14DTE) | 14d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S366 (RubberBand_21DTE) | 21d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S367 (RubberBand_30DTE) | 30d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
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
| S396 (GapDown_ITM2) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S397 (GapDown_ITM1) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S398 (GapDown_ATM) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S399 (GapDown_OTM1) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S400 (Any_Green_Close) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S401 (Any_Gap_Down_Small) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S402 (Any_High_Volume) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S403 (Any_MA50_Touch) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S404 (GapDown_OTM2) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S405 (GapDown_OTM3) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S406 (RubberBand_ITM3) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S407 (RubberBand_ITM2) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S408 (RubberBand_ITM1) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S409 (RubberBand_ATM) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S410 (RubberBand_OTM1) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S411 (RubberBand_OTM2) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S412 (RubberBand_OTM3) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S413 (BBSqueeze_ITM3) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S414 (BBSqueeze_ITM2) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S415 (BBSqueeze_ITM1) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S416 (BBSqueeze_ATM) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S417 (BBSqueeze_OTM1) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S418 (BBSqueeze_OTM2) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S419 (BBSqueeze_OTM3) | 3d | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | — | 0 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S202 (GapDown_Monster) | 3d ATM gap-monster | watch | 2 | 0.0 | -50.00 | -63.34 | -58.33 | -36.66 | 1 | 14 | 2 | $-3.00 | 100.0% | insufficient sample (<8 exits) |
| S218 (BB_Lower_Touch) | 3d ATM BB lower touch | watch | 2 | 0.0 | -50.00 | -63.34 | -58.33 | -36.66 | 2 | 16 | 2 | $-3.00 | 100.0% | insufficient sample (<8 exits) |
| S164 (GapDown ATM 1-DTE — P2B arm) | 1d ATM | watch | 6 | 0.0 | -65.67 | -88.89 | -86.11 | -50.00 | 8 | 21 | 0 | $-59.00 | 83.3% | insufficient sample (<8 exits) |
| S174 (RubberBand long call EOD) | RubberBand (dropped) | drop | 119 | 36.1 | -25.00 | -89.83 | -71.19 | +36.67 | 23 | 0 | 0 | $-1,658.19 | 50.4% | manually paused — excluded from new entries & reflected P&L |
| S173 (MomReversal long call) | MomRev | drop | 415 | 37.1 | -31.51 | -77.18 | -62.95 | +101.90 | 23 | 0 | 0 | $+62.64 | 27.5% | manually paused — excluded from new entries & reflected P&L |
| S165 (GapDown long call 3 DTE) | 3d ATM | drop | 245 | 29.8 | -38.18 | -63.39 | -54.55 | +81.82 | 23 | 26 | 0 | $-1,828.78 | 26.1% | non-positive median return |

## Comparison groups

Experiment arms grouped for side-by-side decisions. INSUFFICIENT if any arm has n<10 exits.

### GapDown DTE comparison

- Status: **INSUFFICIENT** | Best median: **S163** (+0.00%) | Best p10: **S163** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S163 | 7d ATM | 0 | +0.00 | +0.00 | +0.00 | 18 | 0 |
| S164 | 1d ATM | 6 | -65.67 | -88.89 | -86.11 | 21 | 0 |
| S165 | 3d ATM | 245 | -38.18 | -63.39 | -54.55 | 26 | 0 |
| S168 | 5d ATM | 0 | +0.00 | +0.00 | +0.00 | 18 | 0 |

### GapDown Strike comparison

- Status: **INSUFFICIENT** | Best median: **S167** (+0.00%) | Best p10: **S167** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S165 | 3d ATM | 245 | -38.18 | -63.39 | -54.55 | 26 | 0 |
| S167 | 3d 1-OTM | 0 | +0.00 | +0.00 | +0.00 | 22 | 0 |

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
| S202 | 3d ATM gap-monster | 2 | -50.00 | -63.34 | -58.33 | 14 | 2 |
| S204 | 3d ATM gap-up cont | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S205 | 3d ATM gap-highvol | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S206 | 3d ATM gap-trend | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S207 | 3d ATM gap-support | 0 | +0.00 | +0.00 | +0.00 | 12 | 0 |
| S208 | 3d ATM gap-ma200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S209 | 3d ATM gap-recovery | 0 | +0.00 | +0.00 | +0.00 | 6 | 0 |

### Phase-1 Bearish Gap & MA

- Status: **INSUFFICIENT** | Best median: **S203** (+0.00%) | Best p10: **S203** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S203 | 3d ATM gap-up fade (put) | 0 | +0.00 | +0.00 | +0.00 | 8 | 0 |
| S214 | 3d ATM death cross (put) | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 MA family

- Status: **INSUFFICIENT** | Best median: **S210** (+0.00%) | Best p10: **S210** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S210 | 3d ATM MA cross 8/21 | 0 | +0.00 | +0.00 | +0.00 | 15 | 0 |
| S211 | 3d ATM MA cross 21/50 | 0 | +0.00 | +0.00 | +0.00 | 10 | 0 |
| S212 | 3d ATM MA bounce 50 | 0 | +0.00 | +0.00 | +0.00 | 18 | 0 |
| S213 | 3d ATM MA bounce 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |
| S215 | 3d ATM MA reclaim 200 | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Phase-1 RSI/BB/Vol

- Status: **INSUFFICIENT** | Best median: **S216** (+0.00%) | Best p10: **S216** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S216 | 3d ATM RSI x30 | 0 | +0.00 | +0.00 | +0.00 | 20 | 0 |
| S217 | 3d ATM RSI<25 bounce | 0 | +0.00 | +0.00 | +0.00 | 10 | 0 |
| S218 | 3d ATM BB lower touch | 2 | -50.00 | -63.34 | -58.33 | 16 | 2 |
| S219 | 3d ATM vol climax up | 0 | +0.00 | +0.00 | +0.00 | 0 | 0 |

### Other

- Status: **OK** | Best median: **S173** (-31.51%) | Best p10: **S173** (-77.18%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S173 | MomRev | 415 | -31.51 | -77.18 | -62.95 | 0 | 0 |

## Strategy Pipeline Status

_Pipeline evaluation as of 2026-07-29. Auto-kill thresholds: median<-25% at n>=15, p10<-85%, WR<15% at n>=25. Promote: n>=30 median>0%._

| Strategy | Signal | n | Median% | WR% | Status | Days |
|----------|--------|---|---------|-----|--------|------|
| S163 | A1 GapDown ATM call EO | 0 | — | — | NEW | 8 |
| S164 | GapDown ATM 1-DTE — P2 | 6 | -65.67% | 0% | WATCH | 8 |
| S165 | GapDown long call 3 DT | 245 | -38.18% | 30% | INSUFFICIENT | 23 |
| S166 | GapDown strong call | 0 | — | — | NEW | 8 |
| S167 | GapDown long call 3 DT | 0 | — | — | NEW | 8 |
| S168 | GapDown ATM 5-DTE — P2 | 0 | — | — | NEW | 8 |
| S169 | BB Squeeze Breakout ca | 0 | — | — | NEW | 0 |
| S170 | Golden Pocket call 3 D | 0 | — | — | NEW | 0 |
| S171 | VWAP Reclaim call 3 DT | 0 | — | — | NEW | 0 |
| S172 | Trend Resumption call  | 0 | — | — | NEW | 0 |
| S173 | MomReversal long call | 415 | -31.51% | 37% | INSUFFICIENT | 23 |
| S174 | RubberBand long call E | 119 | -25.00% | 36% | INSUFFICIENT | 23 |
| S175 | Earnings Drift call 3  | 0 | — | — | NEW | 0 |
| S200 | GapDown_Aggressive | 0 | — | — | NEW | 0 |
| S201 | GapDown_Mild | 0 | — | — | NEW | 0 |
| S202 | GapDown_Monster | 2 | -50.00% | 0% | WATCH | 1 |
| S203 | GapUp_Fade | 0 | — | — | NEW | 2 |
| S204 | GapUp_Continuation | 0 | — | — | NEW | 0 |
| S205 | GapDown_HighVol | 0 | — | — | NEW | 0 |
| S206 | GapDown_WithTrend | 0 | — | — | NEW | 0 |
| S207 | GapDown_AtSupport | 0 | — | — | NEW | 2 |
| S208 | GapDown_AboveMA200 | 0 | — | — | NEW | 0 |
| S209 | GapDown_Recovery | 0 | — | — | NEW | 0 |
| S210 | MA_Cross_8_21 | 0 | — | — | NEW | 2 |
| S211 | MA_Cross_21_50 | 0 | — | — | NEW | 2 |
| S212 | MA_Bounce_50 | 0 | — | — | NEW | 2 |
| S213 | MA_Bounce_200 | 0 | — | — | NEW | 0 |
| S214 | MA_Death_Cross | 0 | — | — | NEW | 0 |
| S215 | MA_Reclaim_200 | 0 | — | — | NEW | 0 |
| S216 | RSI_Oversold_Cross | 0 | — | — | NEW | 2 |
| S217 | RSI_25_Bounce | 0 | — | — | NEW | 2 |
| S218 | BB_Lower_Touch | 2 | -50.00% | 0% | WATCH | 2 |
| S219 | Volume_Climax_Up | 0 | — | — | NEW | 0 |
| S350 | GapDown_0DTE | 0 | — | — | NEW | 0 |
| S351 | GapDown_1DTE | 0 | — | — | NEW | 0 |
| S352 | GapDown_2DTE | 0 | — | — | NEW | 0 |
| S353 | GapDown_3DTE | 0 | — | — | NEW | 0 |
| S354 | GapDown_5DTE | 0 | — | — | NEW | 0 |
| S355 | GapDown_7DTE | 0 | — | — | NEW | 0 |
| S356 | GapDown_14DTE | 0 | — | — | NEW | 0 |
| S357 | GapDown_21DTE | 0 | — | — | NEW | 0 |
| S358 | GapDown_30DTE | 0 | — | — | NEW | 0 |
| S359 | RubberBand_0DTE | 0 | — | — | NEW | 0 |
| S360 | RubberBand_1DTE | 0 | — | — | NEW | 0 |
| S361 | RubberBand_2DTE | 0 | — | — | NEW | 0 |
| S362 | RubberBand_3DTE | 0 | — | — | NEW | 0 |
| S363 | RubberBand_5DTE | 0 | — | — | NEW | 0 |
| S364 | RubberBand_7DTE | 0 | — | — | NEW | 0 |
| S365 | RubberBand_14DTE | 0 | — | — | NEW | 0 |
| S366 | RubberBand_21DTE | 0 | — | — | NEW | 0 |
| S367 | RubberBand_30DTE | 0 | — | — | NEW | 0 |
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
| S396 | GapDown_ITM2 | 0 | — | — | NEW | 0 |
| S397 | GapDown_ITM1 | 0 | — | — | NEW | 0 |
| S398 | GapDown_ATM | 0 | — | — | NEW | 0 |
| S399 | GapDown_OTM1 | 0 | — | — | NEW | 0 |
| S400 | Any_Green_Close | 0 | — | — | NEW | 0 |
| S401 | Any_Gap_Down_Small | 0 | — | — | NEW | 0 |
| S402 | Any_High_Volume | 0 | — | — | NEW | 0 |
| S403 | Any_MA50_Touch | 0 | — | — | NEW | 0 |
| S404 | GapDown_OTM2 | 0 | — | — | NEW | 0 |
| S405 | GapDown_OTM3 | 0 | — | — | NEW | 0 |
| S406 | RubberBand_ITM3 | 0 | — | — | NEW | 0 |
| S407 | RubberBand_ITM2 | 0 | — | — | NEW | 0 |
| S408 | RubberBand_ITM1 | 0 | — | — | NEW | 0 |
| S409 | RubberBand_ATM | 0 | — | — | NEW | 0 |
| S410 | RubberBand_OTM1 | 0 | — | — | NEW | 0 |
| S411 | RubberBand_OTM2 | 0 | — | — | NEW | 0 |
| S412 | RubberBand_OTM3 | 0 | — | — | NEW | 0 |
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
| — | — | — | — | (none yet — collecting data) |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- **p25** sits between p10 and median for mid-tail visibility.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
- Active paper strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419.
