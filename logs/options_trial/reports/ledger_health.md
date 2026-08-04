# Ledger health — 2026-08-04

_Generated 2026-08-04T10:42:11.438250_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN |
| Missing exit records (post) |   398 | WARN |
| State/ledger mismatches     |    22 | WARN |
| Total open lots             |   141 | INFO |
| Total closed lots           |   657 | INFO |
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
- `08077b694b05`
- `098ad5484a47`
- `1161c297dbfb`
- `1954a5edb17c`
- `19ebe810b50a`
- `2a58900fb3d5`
- `40f46c5f6dea`
- `66b29fe16dc9`
- `6b7a77057810`
- `74e317c0f6d7`
- `7a91f71a0efa`
- `8bbc05f2da28`
- `91bee9a87674`
- `9ede8657b083`
- `a8ea143cb3c1`
- `b9fbd7007e5b`
- `c6df1ed90b93`
- `c9b2ac431e10`
- `e6593cb65d2a`
- `f39886287555`
