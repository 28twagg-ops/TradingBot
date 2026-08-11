# Ledger health — 2026-08-11

_Generated 2026-08-11T11:17:19.936918_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   591 | WARN |
| Missing exit records (post) |   591 | WARN |
| State/ledger mismatches     |    22 | WARN |
| Total open lots             |   127 | INFO |
| Total closed lots           |  1620 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (591 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `08d10d697291`
- `0dfc7d4dddd9`
- `2c150104d8a9`
- `310b2a365ad3`
- `3624bdf6ef0e`
- `56412425e8a9`
- `6047a02bc306`
- `69c0f18b57d0`
- `6ec840bfb4b6`
- `773104f3e5d5`
- `7c4bd63574a0`
- `87a3ffaebd0c`
- `8c0e68b87645`
- `96478e14b0db`
- `9f071b59a24a`
- `a2286f081cc4`
- `ccd35b7494ad`
- `cdf30b192b2f`
- `da7bd04265c7`
- `ef428d55abd6`
- `ef5d694f4fe3`
- `f82900bab9e3`
