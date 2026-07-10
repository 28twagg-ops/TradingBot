# Options strategy selection report — 2026-07-10

_Generated 2026-07-10T18:50:48.969468_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **5**
- Drop: **0**

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S173 (MomReversal long call) | watch | 19 | 78.9 | +37.50 | +32.78 | -13.17 | +70.78 | $+547.64 | 3 | 47.4% | building sample (8-19 exits) |
| S165 (GapDown long call 3 DTE) | watch | 8 | 75.0 | +37.41 | +29.58 | -2.70 | +59.09 | $+104.22 | 2 | 50.0% | building sample (8-19 exits) |
| S174 (RubberBand long call EOD) | watch | 43 | 81.4 | +30.14 | +20.69 | -44.11 | +37.30 | $+622.81 | 5 | 51.2% | promising but needs larger sample |
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (p10), and symbol diversification.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
