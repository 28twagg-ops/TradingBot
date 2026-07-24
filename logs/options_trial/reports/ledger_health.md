# Ledger health — 2026-07-24

_Generated 2026-07-24T11:26:29.879742_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-15** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    18 | WARN |
| Missing exit records (post) |    18 | WARN |
| State/ledger mismatches     |    21 | WARN |
| Total open lots             |    21 | INFO |
| Total closed lots           |   317 | INFO |
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

- `1aa2b1b51a04`
- `211b0bddf535`
- `25201976c071`
- `28d60aa6a5f9`
- `3063590c2bb4`
- `460f91a52e8a`
- `54fec12e2369`
- `7e82e0cace34`
- `9340a11ca774`
- `96f6cc1d25d7`
- `9ea768ebfa98`
- `ab1cc6feba8f`
- `ac80b7f09ff6`
- `ae6794a2be85`
- `bd4db2c0955b`
- `c0260070763f`
- `c13bef6f8d85`
- `d17208d3486f`
- `d6087c930f74`
- `e8d5ddb1c20a`
- `ed80d98325b1`
