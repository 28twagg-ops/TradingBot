# Options strategy selection report — 2026-07-13

_Generated 2026-07-13T11:06:16.271954_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **5**
- Drop: **0**

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S173 (MomReversal long call) | watch | 40 | 65.0 | +25.97 | +45.58 | -64.09 | +80.58 | $+523.64 | 6 | 50.0% | fat left tail (p10 < -45%) |
| S174 (RubberBand long call EOD) | watch | 81 | 53.1 | +15.71 | -6.69 | -84.51 | +37.50 | $-344.19 | 6 | 43.2% | fat left tail (p10 < -45%) |
| S165 (GapDown long call 3 DTE) | watch | 17 | 76.5 | +10.77 | +20.31 | -2.70 | +52.27 | $+161.22 | 2 | 76.5% | building sample (8-19 exits) |
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (p10), and symbol diversification.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
