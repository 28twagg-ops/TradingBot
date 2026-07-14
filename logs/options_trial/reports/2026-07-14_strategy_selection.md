# Options strategy selection report — 2026-07-14

_Generated 2026-07-14T11:50:57.460391_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **3**
- Drop: **2**

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S165 (GapDown long call 3 DTE) | watch | 50 | 52.0 | +3.49 | +23.41 | -51.03 | +85.29 | $+107.22 | 6 | 52.0% | fat left tail (p10 < -45%) |
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S173 (MomReversal long call) | drop | 92 | 48.9 | +0.00 | +45.33 | -69.80 | +109.31 | $+38.64 | 7 | 28.3% | non-positive median return |
| S174 (RubberBand long call EOD) | drop | 97 | 44.3 | -21.74 | -15.29 | -89.66 | +37.37 | $-909.19 | 6 | 47.4% | manually paused — excluded from new entries & reflected P&L |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (p10), and symbol diversification.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
