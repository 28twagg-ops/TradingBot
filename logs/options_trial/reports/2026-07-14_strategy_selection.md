# Options strategy selection report — 2026-07-14

_Generated 2026-07-14T16:01:21.692913_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **2**
- Drop: **3**

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S173 (MomReversal long call) | drop | 94 | 47.9 | +0.00 | +43.37 | -69.67 | +107.24 | $-27.36 | 7 | 27.7% | non-positive median return |
| S165 (GapDown long call 3 DTE) | drop | 55 | 47.3 | -2.70 | +20.09 | -50.18 | +80.39 | $+62.22 | 6 | 47.3% | non-positive median return |
| S174 (RubberBand long call EOD) | drop | 97 | 44.3 | -21.74 | -15.29 | -89.66 | +37.37 | $-909.19 | 6 | 47.4% | manually paused — excluded from new entries & reflected P&L |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (p10), and symbol diversification.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
