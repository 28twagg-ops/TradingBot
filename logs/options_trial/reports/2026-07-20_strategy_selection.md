# Options strategy selection report — 2026-07-20

_Generated 2026-07-20T11:40:45.876657_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **2**
- Drop: **3**

## Attribution health

- Total exits: **611**
- Orphan exits (b0/orphan_reconcile): **22**
- Orphan rate: **3.6%** (warn if >10%)
- Orphan rate OK (attribution looks healthy).

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S174 (RubberBand long call EOD) | drop | 114 | 37.7 | -24.14 | -22.00 | -89.83 | +37.06 | $-1,498.19 | 6 | 50.0% | manually paused — excluded from new entries & reflected P&L |
| S165 (GapDown long call 3 DTE) | drop | 191 | 33.0 | -30.00 | -0.20 | -60.00 | +84.31 | $-788.78 | 9 | 27.7% | non-positive median return |
| S173 (MomReversal long call) | drop | 284 | 34.5 | -33.85 | +11.43 | -79.44 | +95.94 | $-1,914.36 | 12 | 31.7% | non-positive median return |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
