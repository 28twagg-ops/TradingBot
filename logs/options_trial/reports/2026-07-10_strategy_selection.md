# Options strategy selection report — 2026-07-10

_Generated 2026-07-10T15:49:45.349503_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **5**
- Drop: **0**

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S165 (GapDown long call 3 DTE) | watch | 6 | 83.3 | +47.73 | +39.67 | +12.19 | +59.09 | $+105.22 | 2 | 66.7% | insufficient sample (<8 exits) |
| S173 (MomReversal long call) | watch | 16 | 87.5 | +37.69 | +40.54 | +2.38 | +70.78 | $+551.64 | 3 | 56.2% | building sample (8-19 exits) |
| S174 (RubberBand long call EOD) | watch | 42 | 83.3 | +30.14 | +21.22 | -46.72 | +37.40 | $+623.81 | 5 | 52.4% | fat left tail (p10 < -45%) |
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (p10), and symbol diversification.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
