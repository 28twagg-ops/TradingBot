# Ledger health — 2026-08-04

_Generated 2026-08-04T11:56:18.196244_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN |
| Missing exit records (post) |   398 | WARN |
| State/ledger mismatches     |    18 | WARN |
| Total open lots             |   225 | INFO |
| Total closed lots           |   712 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (398 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `10db07a6929b`
- `1fad73c5bd2e`
- `60573ace2ade`
- `6a620ea1b5c4`
- `8223917270ff`
- `9904d193bdc7`
- `a61f8143b499`
- `a8ea143cb3c1`
- `b9fbd7007e5b`
- `c3b3c141129b`
- `c6df1ed90b93`
- `cfe874780e99`
- `d0f74d60de78`
- `dc93f1bb26fb`
- `eea58313d5b0`
- `f0deab08c6cf`
- `fbb330ec2ca3`
- `fbcec519485c`
