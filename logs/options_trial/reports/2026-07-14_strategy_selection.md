# Options strategy selection report — 2026-07-14

_Generated 2026-07-14T10:36:14.371622_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **3**
- Drop: **2**

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S173 (MomReversal long call) | watch | 77 | 55.8 | +20.69 | +59.96 | -69.23 | +151.82 | $+391.64 | 7 | 33.8% | fat left tail (p10 < -45%) |
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S165 (GapDown long call 3 DTE) | drop | 38 | 50.0 | -0.68 | -4.50 | -52.53 | +47.73 | $-157.78 | 5 | 68.4% | non-positive median return |
| S174 (RubberBand long call EOD) | drop | 97 | 44.3 | -21.74 | -15.29 | -89.66 | +37.37 | $-909.19 | 6 | 47.4% | manually paused — excluded from new entries & reflected P&L |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (p10), and symbol diversification.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
