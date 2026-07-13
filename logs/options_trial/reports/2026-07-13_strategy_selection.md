# Options strategy selection report — 2026-07-13

_Generated 2026-07-13T09:44:28.655883_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **5**
- Drop: **0**

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S173 (MomReversal long call) | watch | 24 | 75.0 | +33.33 | +31.18 | -8.75 | +70.78 | $+584.64 | 3 | 58.3% | promising mid-sample — need more exits |
| S174 (RubberBand long call EOD) | watch | 62 | 64.5 | +30.14 | +3.99 | -53.15 | +39.44 | $+193.81 | 5 | 35.5% | fat left tail (p10 < -45%) |
| S165 (GapDown long call 3 DTE) | watch | 12 | 75.0 | +27.08 | +24.48 | -2.70 | +57.95 | $+132.22 | 2 | 66.7% | building sample (8-19 exits) |
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (p10), and symbol diversification.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
