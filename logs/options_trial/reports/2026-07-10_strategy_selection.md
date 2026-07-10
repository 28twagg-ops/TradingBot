# Options strategy selection report — 2026-07-10

_Generated 2026-07-10T15:39:26.676598_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **5**
- Drop: **0**

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S173 (MomReversal long call) | watch | 12 | 83.3 | +54.23 | +46.09 | +3.13 | +70.78 | $+531.64 | 3 | 75.0% | building sample (8-19 exits) |
| S165 (GapDown long call 3 DTE) | watch | 5 | 100.0 | +47.73 | +48.14 | +35.34 | +59.09 | $+107.22 | 2 | 80.0% | insufficient sample (<8 exits) |
| S174 (RubberBand long call EOD) | watch | 41 | 82.9 | +30.14 | +21.43 | -49.32 | +37.50 | $+614.81 | 5 | 53.7% | fat left tail (p10 < -45%) |
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (p10), and symbol diversification.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
