# Options strategy selection report — 2026-07-17

_Generated 2026-07-17T10:11:27.211893_

## Summary

- Strategies analyzed: **5**
- Keep: **0**
- Watch: **2**
- Drop: **3**

## Attribution health

- Total exits: **443**
- Orphan exits (b0/orphan_reconcile): **22**
- Orphan rate: **5.0%** (warn if >10%)
- Orphan rate OK (attribution looks healthy).

## Strategy scoreboard

| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S163 (A1 GapDown ATM call EOD) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | $+0.00 | 0 | 0.0% | insufficient sample (<8 exits) |
| S165 (GapDown long call 3 DTE) | drop | 120 | 36.7 | -13.46 | +3.17 | -56.67 | +78.20 | $-626.78 | 9 | 34.2% | non-positive median return |
| S174 (RubberBand long call EOD) | drop | 108 | 39.8 | -23.29 | -19.78 | -89.83 | +37.29 | $-1,284.19 | 6 | 49.1% | manually paused — excluded from new entries & reflected P&L |
| S173 (MomReversal long call) | drop | 193 | 34.7 | -27.69 | +13.21 | -79.44 | +95.96 | $-1,977.36 | 11 | 19.7% | non-positive median return |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
