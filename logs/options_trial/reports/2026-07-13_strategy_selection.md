# Options strategy selection report — 2026-07-13

_Generated 2026-07-13T12:20:50.428204_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **5**
- Drop: **0**

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S173 (MomReversal long call) | watch | 50 | 64.0 | +32.29 | +38.61 | -65.94 | +84.31 | $+469.64 | 6 | 52.0% | fat left tail (p10 < -45%) |
| S174 (RubberBand long call EOD) | watch | 85 | 50.6 | +9.46 | -9.56 | -89.66 | +37.50 | $-536.19 | 6 | 45.9% | fat left tail (p10 < -45%) |
| S165 (GapDown long call 3 DTE) | watch | 20 | 65.0 | +8.20 | +9.31 | -52.25 | +48.87 | $+48.22 | 2 | 80.0% | fat left tail (p10 < -45%) |
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (p10), and symbol diversification.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
