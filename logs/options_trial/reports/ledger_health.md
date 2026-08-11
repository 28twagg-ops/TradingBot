# Ledger health — 2026-08-11

_Generated 2026-08-11T10:12:16.856083_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   591 | WARN |
| Missing exit records (post) |   591 | WARN |
| State/ledger mismatches     |    21 | WARN |
| Total open lots             |   131 | INFO |
| Total closed lots           |  1586 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (591 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `075adab43582`
- `08d10d697291`
- `30e1a418b4d0`
- `3624bdf6ef0e`
- `6047a02bc306`
- `62718582f724`
- `755c5aa2f481`
- `7a39ae9277a6`
- `7c4bd63574a0`
- `96478e14b0db`
- `9f071b59a24a`
- `a2286f081cc4`
- `a2fa8f3b4dd3`
- `c87a043e6603`
- `cd6f7fb007d7`
- `cdf30b192b2f`
- `da7bd04265c7`
- `e4b3d8271b9e`
- `ef428d55abd6`
- `ef5d694f4fe3`
- `f82900bab9e3`
