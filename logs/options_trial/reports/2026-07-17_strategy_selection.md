# Options strategy selection report — 2026-07-17

_Generated 2026-07-17T12:45:41.962547_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **2**
- Drop: **3**

## Attribution health

- Total exits: **599**
- Orphan exits (b0/orphan_reconcile): **22**
- Orphan rate: **3.7%** (warn if >10%)
- Orphan rate OK (attribution looks healthy).

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S174 (RubberBand long call EOD) | drop | 113 | 38.1 | -23.29 | -21.39 | -89.83 | +37.13 | $-1,444.19 | 6 | 49.6% | manually paused — excluded from new entries & reflected P&L |
| S165 (GapDown long call 3 DTE) | drop | 187 | 33.7 | -24.24 | +1.05 | -60.00 | +85.49 | $-650.78 | 9 | 28.3% | non-positive median return |
| S173 (MomReversal long call) | drop | 277 | 33.6 | -33.93 | +11.39 | -79.43 | +98.00 | $-1,968.36 | 11 | 32.5% | non-positive median return |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
