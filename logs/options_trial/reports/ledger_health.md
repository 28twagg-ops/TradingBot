# Ledger health — 2026-08-06

_Generated 2026-08-06T10:18:22.233901_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN |
| Orphaned lots (post-stable) |   441 | WARN |
| Missing exit records (post) |   438 | WARN |
| State/ledger mismatches     |    17 | WARN |
| Total open lots             |   154 | INFO |
| Total closed lots           |  1083 | INFO |
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

_Orphaned ledger detail omitted (441 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `07adba66b2b4`
- `124baaf9707f`
- `15328f5d4806`
- `24ce6f816b8c`
- `42a43e96eb70`
- `533439b4af09`
- `5922a38a0135`
- `70284995a788`
- `8975f7420163`
- `9284453de217`
- `b4c693e6c725`
- `bb06c1517733`
- `d438b640fa62`
- `d6fe853b1f7d`
- `ed3c151a1305`
- `f43b00eb93ab`
- `f7cfc7c642c8`
