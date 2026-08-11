# Ledger health — 2026-08-11

_Generated 2026-08-11T13:39:57.440733_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   591 | WARN |
| Missing exit records (post) |   591 | WARN |
| State/ledger mismatches     |    15 | WARN |
| Total open lots             |   112 | INFO |
| Total closed lots           |  1650 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (591 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `06517a8e6efc`
- `2b6df4aef9e1`
- `3425b4d12807`
- `44e4a2352a6e`
- `517cade30593`
- `725402a7cd1c`
- `8524e9215e14`
- `86005b9e6f2d`
- `885b3bf4c7bf`
- `95871676b266`
- `bd3a385ba519`
- `c2e41b290ed2`
- `cff37a88683d`
- `d632d1f22a35`
- `f58e0388cd6c`
