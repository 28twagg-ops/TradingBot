# Options strategy selection report — 2026-07-14

_Generated 2026-07-14T10:16:21.064904_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **4**
- Drop: **1**

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S173 (MomReversal long call) | watch | 75 | 54.7 | +20.00 | +59.56 | -69.23 | +152.73 | $+358.64 | 7 | 34.7% | fat left tail (p10 < -45%) |
| S165 (GapDown long call 3 DTE) | watch | 37 | 51.4 | +1.35 | -3.00 | -51.39 | +47.73 | $-115.78 | 4 | 70.3% | fat left tail (p10 < -45%) |
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S174 (RubberBand long call EOD) | drop | 97 | 44.3 | -21.74 | -15.29 | -89.66 | +37.37 | $-909.19 | 6 | 47.4% | manually paused — excluded from new entries & reflected P&L |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (p10), and symbol diversification.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
