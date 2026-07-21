# Options strategy selection report — 2026-07-21

_Generated 2026-07-21T13:20:43.712965_

## Summary

- Strategies analyzed: **8**
- Keep: **0**
- Watch: **5**
- Drop: **3**

## Attribution health

- Total exits: **762**
- Orphan exits (b0/orphan_reconcile): **22**
- Orphan rate: **2.9%** (warn if >10%)
- Orphan rate OK (attribution looks healthy).

## Strategy scoreboard

| strategy | DTE | rec | exits | win% | med% | p10% | p25% | p90% | days live | ent 5d | exit 5d | realized $ | top share | rationale |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S163 (A1 GapDown ATM call EOD) | 7d ATM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 0 | 15 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S164 (GapDown ATM 1-DTE — P2B arm) | 1d ATM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 0 | 20 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S166 (GapDown strong call) | 3d ATM strong | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 0 | 15 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S167 (GapDown long call 3 DTE 1-OTM — P2C) | 3d 1-OTM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 0 | 20 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S168 (GapDown ATM 5-DTE — P2B arm) | 5d ATM | watch | 0 | 0.0 | +0.00 | +0.00 | +0.00 | +0.00 | 0 | 20 | 0 | $+0.00 | 0.0% | insufficient sample (<8 exits) |
| S174 (RubberBand long call EOD) | RubberBand (dropped) | drop | 119 | 36.1 | -25.00 | -89.83 | -71.19 | +36.67 | 15 | 0 | 0 | $-1,658.19 | 50.4% | manually paused — excluded from new entries & reflected P&L |
| S173 (MomReversal long call) | MomRev | drop | 385 | 35.6 | -32.31 | -78.45 | -63.16 | +100.00 | 15 | 65 | 66 | $-1,186.36 | 28.1% | manually paused — excluded from new entries & reflected P&L |
| S165 (GapDown long call 3 DTE) | 3d ATM | drop | 236 | 30.9 | -34.31 | -61.76 | -52.73 | +81.82 | 15 | 60 | 24 | $-1,493.78 | 27.1% | non-positive median return |

## Comparison groups

Experiment arms grouped for side-by-side decisions. INSUFFICIENT if any arm has n<10 exits.

### GapDown DTE comparison

- Status: **INSUFFICIENT** | Best median: **S163** (+0.00%) | Best p10: **S163** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S163 | 7d ATM | 0 | +0.00 | +0.00 | +0.00 | 15 | 0 |
| S164 | 1d ATM | 0 | +0.00 | +0.00 | +0.00 | 20 | 0 |
| S165 | 3d ATM | 236 | -34.31 | -61.76 | -52.73 | 60 | 24 |
| S168 | 5d ATM | 0 | +0.00 | +0.00 | +0.00 | 20 | 0 |

### GapDown Strike comparison

- Status: **INSUFFICIENT** | Best median: **S167** (+0.00%) | Best p10: **S167** (+0.00%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S165 | 3d ATM | 236 | -34.31 | -61.76 | -52.73 | 60 | 24 |
| S167 | 3d 1-OTM | 0 | +0.00 | +0.00 | +0.00 | 20 | 0 |

### Other

- Status: **OK** | Best median: **S173** (-32.31%) | Best p10: **S173** (-78.45%)

| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |
|---|---|---:|---:|---:|---:|---:|---:|
| S173 | MomRev | 385 | -32.31 | -78.45 | -63.16 | 65 | 66 |

## Notes

- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.
- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.
- **p25** sits between p10 and median for mid-tail visibility.
- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.
- `watch` means potentially viable but still sample-limited or risk-concentrated.
- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).
- Orphan rate = orphan_exits / total_exits; alert if >10% (attribution failure, not edge).
- Active paper strategies: S165, S164, S168, S167, S166, S163.
