# Ledger health — 2026-08-14

_Generated 2026-08-14T12:42:04.062157_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN |
| Missing exit records (post) |   678 | WARN |
| State/ledger mismatches     |     8 | WARN |
| Total open lots             |    63 | INFO |
| Total closed lots           |  1769 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (678 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `168e2036bf09`
- `31d5712b7b5e`
- `4d6324cf6582`
- `5c5bca0143e1`
- `a66aef8afd56`
- `b8799cfc5b7f`
- `d903b82b8523`
- `f7fdfc0bbe84`
