# Options strategy selection report — 2026-07-13

_Generated 2026-07-13T10:46:26.994900_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **5**
- Drop: **0**

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S174 (RubberBand long call EOD) | watch | 65 | 63.1 | +30.14 | +3.57 | -67.00 | +39.66 | $+143.81 | 5 | 33.8% | fat left tail (p10 < -45%) |
| S165 (GapDown long call 3 DTE) | watch | 13 | 76.9 | +27.08 | +23.43 | -2.70 | +56.82 | $+139.22 | 2 | 69.2% | building sample (8-19 exits) |
| S173 (MomReversal long call) | watch | 28 | 67.9 | +25.97 | +20.06 | -51.85 | +70.78 | $+465.64 | 4 | 53.6% | fat left tail (p10 < -45%) |
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (p10), and symbol diversification.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
