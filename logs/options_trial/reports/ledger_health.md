# Ledger health — 2026-08-06

_Generated 2026-08-06T10:50:02.169034_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN |
| Orphaned lots (post-stable) |   440 | WARN |
| Missing exit records (post) |   437 | WARN |
| State/ledger mismatches     |    21 | WARN |
| Total open lots             |   168 | INFO |
| Total closed lots           |  1123 | INFO |
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
| b428605e4e35 | S365 | AAPL | 2026-07-31 | 6 |

_Orphaned ledger detail omitted (440 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `07adba66b2b4`
- `0d4a66abab8e`
- `124baaf9707f`
- `12dc9ff32024`
- `1edd9129c6f0`
- `24ce6f816b8c`
- `3990bdd54575`
- `42a43e96eb70`
- `533439b4af09`
- `6d0fd9acb73d`
- `70284995a788`
- `73329dd73b59`
- `7e8e8c467922`
- `9284453de217`
- `a1fc98d9835a`
- `c750268030a8`
- `d438b640fa62`
- `e229c2b7c969`
- `ed3c151a1305`
- `ee08eb0595dc`
- `f43b00eb93ab`
