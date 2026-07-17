# Options strategy selection report — 2026-07-17

_Generated 2026-07-17T12:40:43.976181_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **2**
- Drop: **3**

## Attribution health

- Total exits: **593**
- Orphan exits (b0/orphan_reconcile): **22**
- Orphan rate: **3.7%** (warn if >10%)
- Orphan rate OK (attribution looks healthy).

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S174 (RubberBand long call EOD) | drop | 111 | 38.7 | -23.29 | -20.94 | -89.83 | +37.29 | $-1,392.19 | 6 | 49.5% | manually paused — excluded from new entries & reflected P&L |
| S165 (GapDown long call 3 DTE) | drop | 186 | 33.3 | -25.63 | +0.73 | -60.00 | +85.79 | $-684.78 | 9 | 28.5% | non-positive median return |
| S173 (MomReversal long call) | drop | 274 | 33.2 | -33.93 | +11.30 | -79.44 | +99.00 | $-1,965.36 | 11 | 32.8% | non-positive median return |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
