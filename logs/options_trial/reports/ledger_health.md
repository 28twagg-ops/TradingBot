# Ledger health — 2026-08-04

_Generated 2026-08-04T10:57:45.668387_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN |
| Missing exit records (post) |   398 | WARN |
| State/ledger mismatches     |    23 | WARN |
| Total open lots             |   171 | INFO |
| Total closed lots           |   666 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (398 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `02870fdbe3cc`
- `07fa43b3866a`
- `098ad5484a47`
- `1161c297dbfb`
- `1954a5edb17c`
- `19ebe810b50a`
- `40f46c5f6dea`
- `417d8592df6d`
- `4789d4f5ed60`
- `74e317c0f6d7`
- `7a91f71a0efa`
- `81a90ff6b881`
- `8bbc05f2da28`
- `91bee9a87674`
- `9904d193bdc7`
- `9ede8657b083`
- `a23b6ed99f4e`
- `a8ea143cb3c1`
- `b9fbd7007e5b`
- `c6df1ed90b93`
- `cfe874780e99`
- `dc93f1bb26fb`
- `e6593cb65d2a`
