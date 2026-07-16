# Options strategy selection report — 2026-07-16

_Generated 2026-07-16T13:20:44.962021_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **2**
- Drop: **3**

## Attribution health

- Total exits: **382**
- Orphan exits (b0/orphan_reconcile): **22**
- Orphan rate: **5.8%** (warn if >10%)
- Orphan rate OK (attribution looks healthy).

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S165 (GapDown long call 3 DTE) | drop | 100 | 37.0 | -7.69 | +7.24 | -56.04 | +78.38 | $-408.78 | 7 | 31.0% | non-positive median return |
| S174 (RubberBand long call EOD) | drop | 103 | 41.7 | -23.29 | -18.01 | -89.80 | +37.29 | $-1,123.19 | 6 | 48.5% | manually paused — excluded from new entries & reflected P&L |
| S173 (MomReversal long call) | drop | 157 | 33.8 | -26.23 | +18.92 | -77.41 | +100.00 | $-1,535.36 | 10 | 21.7% | non-positive median return |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
