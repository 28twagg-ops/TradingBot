# Options strategy selection report — 2026-07-10

_Generated 2026-07-10T15:20:52.704655_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **5**
- Drop: **0**

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S173 (MomReversal long call) | watch | 10 | 90.0 | +70.78 | +52.19 | +32.33 | +70.78 | $+526.64 | 2 | 90.0% | building sample (8-19 exits) |
| S165 (GapDown long call 3 DTE) | watch | 4 | 100.0 | +53.41 | +53.41 | +47.73 | +59.09 | $+94.22 | 1 | 100.0% | insufficient sample (<8 exits) |
| S174 (RubberBand long call EOD) | watch | 39 | 82.1 | +30.14 | +21.16 | -49.32 | +40.32 | $+600.81 | 3 | 56.4% | fat left tail (p10 < -45%) |
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (p10), and symbol diversification.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
