# Options strategy selection report — 2026-07-13

_Generated 2026-07-13T14:35:50.783013_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **4**
- Drop: **1**

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S173 (MomReversal long call) | watch | 50 | 64.0 | +32.29 | +38.61 | -65.94 | +84.31 | $+469.64 | 6 | 52.0% | fat left tail (p10 < -45%) |
| S165 (GapDown long call 3 DTE) | watch | 22 | 59.1 | +5.63 | +4.00 | -51.81 | +47.73 | $-5.78 | 2 | 81.8% | fat left tail (p10 < -45%) |
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S174 (RubberBand long call EOD) | drop | 88 | 48.9 | -1.41 | -10.99 | -89.66 | +37.50 | $-609.19 | 6 | 44.3% | non-positive median return |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (p10), and symbol diversification.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
