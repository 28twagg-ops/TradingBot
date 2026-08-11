# Ledger health — 2026-08-11

_Generated 2026-08-11T12:01:21.141347_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   591 | WARN |
| Missing exit records (post) |   591 | WARN |
| State/ledger mismatches     |    19 | WARN |
| Total open lots             |   127 | INFO |
| Total closed lots           |  1638 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (591 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `0dfc7d4dddd9`
- `3624bdf6ef0e`
- `44e4a2352a6e`
- `56412425e8a9`
- `6047a02bc306`
- `69c0f18b57d0`
- `6ec840bfb4b6`
- `7c4bd63574a0`
- `86005b9e6f2d`
- `87a3ffaebd0c`
- `885b3bf4c7bf`
- `95871676b266`
- `9f071b59a24a`
- `a2286f081cc4`
- `a229a689915f`
- `cdf30b192b2f`
- `d632d1f22a35`
- `da7bd04265c7`
- `f82900bab9e3`
