# Ledger health — 2026-08-06

_Generated 2026-08-06T10:58:51.202708_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN |
| Orphaned lots (post-stable) |   440 | WARN |
| Missing exit records (post) |   437 | WARN |
| State/ledger mismatches     |    24 | WARN |
| Total open lots             |   156 | INFO |
| Total closed lots           |  1146 | INFO |
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

- `0d4a66abab8e`
- `12dc9ff32024`
- `1edd9129c6f0`
- `3990bdd54575`
- `53e410b0bd58`
- `6d0fd9acb73d`
- `73329dd73b59`
- `7478afa6cf76`
- `79c3fa94dee8`
- `79dcdbc2c65a`
- `7e8e8c467922`
- `8b358f144f76`
- `9284453de217`
- `a1fc98d9835a`
- `bc9ed069a924`
- `c57c3e700d0e`
- `c62285dbc991`
- `c750268030a8`
- `d465a8c7b174`
- `d4db12c7dd33`
- `e229c2b7c969`
- `ed3c151a1305`
- `ee08eb0595dc`
- `f5363f91b2ab`
