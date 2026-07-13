# Options strategy selection report — 2026-07-13

_Generated 2026-07-13T15:50:18.313497_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **4**
- Drop: **1**

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S173 (MomReversal long call) | watch | 55 | 60.0 | +20.69 | +52.67 | -65.57 | +89.19 | $+450.64 | 6 | 47.3% | fat left tail (p10 < -45%) |
| S165 (GapDown long call 3 DTE) | watch | 25 | 56.0 | +5.63 | +0.99 | -50.90 | +47.73 | $-43.78 | 3 | 80.0% | fat left tail (p10 < -45%) |
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S174 (RubberBand long call EOD) | drop | 90 | 47.8 | -1.41 | -11.83 | -89.66 | +37.50 | $-668.19 | 6 | 45.6% | non-positive median return |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (p10), and symbol diversification.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
