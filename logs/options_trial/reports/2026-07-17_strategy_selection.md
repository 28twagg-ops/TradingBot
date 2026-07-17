# Options strategy selection report — 2026-07-17

_Generated 2026-07-17T12:15:47.308835_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **2**
- Drop: **3**

## Attribution health

- Total exits: **499**
- Orphan exits (b0/orphan_reconcile): **22**
- Orphan rate: **4.4%** (warn if >10%)
- Orphan rate OK (attribution looks healthy).

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S174 (RubberBand long call EOD) | drop | 109 | 39.4 | -23.29 | -20.43 | -89.83 | +37.29 | $-1,337.19 | 6 | 49.5% | manually paused — excluded from new entries & reflected P&L |
| S173 (MomReversal long call) | drop | 226 | 35.8 | -31.51 | +17.75 | -77.05 | +100.00 | $-1,324.36 | 11 | 29.6% | non-positive median return |
| S165 (GapDown long call 3 DTE) | drop | 142 | 31.0 | -35.29 | -6.20 | -60.00 | +61.82 | $-1,436.78 | 9 | 28.9% | non-positive median return |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
