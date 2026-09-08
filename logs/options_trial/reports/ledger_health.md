# Ledger health — 2026-09-08

_Generated 2026-09-08T17:06:20.908515_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN |
| Orphaned lots (post-stable) |  1052 | WARN |
| Missing exit records (post) |  1050 | WARN |
| State/ledger mismatches     |     4 | WARN |
| Total open lots             |   102 | INFO |
| Total closed lots           |  2067 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

## Current stuck lots

| lot_id | strategy | symbol | entry_day | age_days |
|--------|----------|--------|-----------|---------:|
| 561eb75525f7 | S366 | NKE | 2026-09-01 | 7 |
| 2a2bf12135d0 | S366 | NKE | 2026-09-01 | 7 |

_Orphaned ledger detail omitted (1052 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `1dd70207ec04`
- `aec42dbdd398`
- `b83861379190`
- `ca6c25d8b04c`
