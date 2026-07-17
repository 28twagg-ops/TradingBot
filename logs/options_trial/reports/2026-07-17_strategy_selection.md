# Options strategy selection report — 2026-07-17

_Generated 2026-07-17T09:54:57.466438_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **2**
- Drop: **3**

## Attribution health

- Total exits: **437**
- Orphan exits (b0/orphan_reconcile): **22**
- Orphan rate: **5.0%** (warn if >10%)
- Orphan rate OK (attribution looks healthy).

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S165 (GapDown long call 3 DTE) | drop | 119 | 37.0 | -10.00 | +3.76 | -56.42 | +78.40 | $-581.78 | 8 | 34.5% | non-positive median return |
| S174 (RubberBand long call EOD) | drop | 107 | 40.2 | -23.29 | -19.11 | -89.73 | +37.29 | $-1,230.19 | 6 | 48.6% | manually paused — excluded from new entries & reflected P&L |
| S173 (MomReversal long call) | drop | 189 | 33.9 | -31.51 | +12.74 | -79.42 | +93.81 | $-2,029.36 | 11 | 20.1% | non-positive median return |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
