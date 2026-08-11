# Ledger health — 2026-08-11

_Generated 2026-08-11T19:56:02.010408_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   591 | WARN |
| Missing exit records (post) |   591 | WARN |
| State/ledger mismatches     |    13 | WARN |
| Total open lots             |   108 | INFO |
| Total closed lots           |  1652 | INFO |
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
- `2463c820ab36`
- `2a5f26b32177`
- `44e4a2352a6e`
- `6c779d79cdac`
- `7eff478f64e3`
- `86005b9e6f2d`
- `885b3bf4c7bf`
- `95871676b266`
- `c081a3ca8cd6`
- `cff37a88683d`
- `dbaeb02d7c97`
- `f58e0388cd6c`
