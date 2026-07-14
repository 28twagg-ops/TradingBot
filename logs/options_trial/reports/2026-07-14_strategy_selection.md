# Options strategy selection report — 2026-07-14

_Generated 2026-07-14T10:11:21.667706_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **4**
- Drop: **1**

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S173 (MomReversal long call) | watch | 73 | 53.4 | +20.00 | +56.52 | -69.23 | +108.27 | $+283.64 | 7 | 35.6% | fat left tail (p10 < -45%) |
| S165 (GapDown long call 3 DTE) | watch | 36 | 52.8 | +3.49 | -1.57 | -50.00 | +47.73 | $-85.78 | 4 | 69.4% | fat left tail (p10 < -45%) |
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S174 (RubberBand long call EOD) | drop | 95 | 45.3 | -19.57 | -13.70 | -87.60 | +37.42 | $-802.19 | 6 | 46.3% | manually paused — excluded from new entries & reflected P&L |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (p10), and symbol diversification.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
