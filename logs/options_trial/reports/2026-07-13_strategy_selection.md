# Options strategy selection report — 2026-07-13

_Generated 2026-07-13T09:34:54.379811_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **5**
- Drop: **0**

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S173 (MomReversal long call) | watch | 20 | 80.0 | +35.41 | +32.18 | -12.84 | +70.78 | $+553.64 | 3 | 50.0% | promising mid-sample — need more exits |
| S174 (RubberBand long call EOD) | watch | 51 | 72.5 | +30.14 | +12.41 | -49.32 | +37.50 | $+459.81 | 5 | 43.1% | fat left tail (p10 < -45%) |
| S165 (GapDown long call 3 DTE) | watch | 9 | 77.8 | +27.08 | +29.31 | -2.70 | +59.09 | $+117.22 | 2 | 55.6% | building sample (8-19 exits) |
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (p10), and symbol diversification.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
