# Ledger health — 2026-07-24

_Generated 2026-07-24T10:02:49.187221_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-15** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    18 | WARN |
| Missing exit records (post) |    18 | WARN |
| State/ledger mismatches     |     8 | WARN |
| Total open lots             |    10 | INFO |
| Total closed lots           |   316 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-15).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-15 lot_id churn after attribution fix (INFO, not WARN).

## Orphaned ledger entries (detail)

| lot_id | strategy | symbol | entry_day | age_days |
|--------|----------|--------|-----------|---------:|
| fe6b46fa00bb | S165 | AVGO | 2026-07-16 | 8 |
| 7385dc02b472 | S173 | UAL | 2026-07-16 | 8 |
| 5b2b4313830f | S173 | UAL | 2026-07-16 | 8 |
| f09b7de85a3f | S173 | AMD | 2026-07-16 | 8 |
| 78970860d223 | S165 | AVGO | 2026-07-16 | 8 |
| cfe20e4c43c8 | S165 | AVGO | 2026-07-16 | 8 |
| 30f0bcea133d | S173 | LULU | 2026-07-16 | 8 |
| 9ecc64bd9c12 | S173 | AMZN | 2026-07-17 | 7 |
| 5d7beb55fe5d | S173 | AMZN | 2026-07-17 | 7 |
| a475367ce58d | S165 | GOOGL | 2026-07-17 | 7 |
| e6ef223ec478 | S165 | META | 2026-07-17 | 7 |
| 7931dfce2f00 | S165 | META | 2026-07-17 | 7 |
| 79be64ae2c62 | S173 | AMD | 2026-07-17 | 7 |
| 436408a3ca7a | S165 | META | 2026-07-17 | 7 |
| 5f3a3db61d3b | S165 | META | 2026-07-17 | 7 |
| 036fd10e9adc | S165 | META | 2026-07-17 | 7 |
| fe4bb2e8483b | S173 | AMD | 2026-07-17 | 7 |
| 768e1ca7158a | S173 | AMD | 2026-07-17 | 7 |

## State/ledger mismatches

- `2d781519f9f4`
- `3830601a325e`
- `3f3e3d0dc0a7`
- `8ebc02f36dd4`
- `a79b6f59c780`
- `a936288ddddd`
- `be2abd19a1df`
- `e7d7bff2a764`
