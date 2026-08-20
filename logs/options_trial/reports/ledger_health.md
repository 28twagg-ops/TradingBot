# Ledger health — 2026-08-20

_Generated 2026-08-20T13:38:43.721532_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    35 | WARN |
| Orphaned lots (post-stable) |   975 | WARN |
| Missing exit records (post) |   945 | WARN |
| State/ledger mismatches     |     5 | WARN |
| Total open lots             |    35 | INFO |
| Total closed lots           |  1770 | INFO |
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
| 349a32a6ea4c | S397 | MARA | 2026-08-14 | 6 |
| ff2feacfbc00 | S354 | MARA | 2026-08-14 | 6 |
| 4d6324cf6582 | ORPHAN | MARA | 2026-08-14 | 6 |
| 66dc0774d3d2 | S405 | MARA | 2026-08-14 | 6 |
| aec70c804923 | S398 | MARA | 2026-08-14 | 6 |
| f2e7db50f3b5 | S398 | MARA | 2026-08-14 | 6 |
| 686007220181 | S355 | MARA | 2026-08-14 | 6 |
| 65e523c0c9ec | S355 | MARA | 2026-08-14 | 6 |
| 352005ef0531 | S354 | MARA | 2026-08-14 | 6 |
| 4eb7e5bbb15d | S354 | MARA | 2026-08-14 | 6 |
| b44296e3fde1 | S405 | MARA | 2026-08-14 | 6 |
| 3cc2c732ed20 | S404 | MSTR | 2026-08-14 | 6 |
| f7b69a3229cb | S404 | MSTR | 2026-08-14 | 6 |
| 7871a4bbc7a4 | S399 | MSTR | 2026-08-14 | 6 |
| 3ebbf6bfdaa4 | S397 | MSTR | 2026-08-14 | 6 |
| f7fdfc0bbe84 | ORPHAN | MSTR | 2026-08-14 | 6 |
| b8799cfc5b7f | ORPHAN | MSTR | 2026-08-14 | 6 |
| 46bcb0b9d47c | S398 | MARA | 2026-08-14 | 6 |
| cb36a28c96ca | S398 | MARA | 2026-08-14 | 6 |
| 6904664a979b | S355 | MARA | 2026-08-14 | 6 |
| cc24e69c9b18 | S354 | MARA | 2026-08-14 | 6 |
| 58a1795b826c | S354 | MARA | 2026-08-14 | 6 |
| 69fd8c48f5a2 | S405 | MARA | 2026-08-14 | 6 |
| 13380b8dcbd2 | S405 | MARA | 2026-08-14 | 6 |
| 3b54aec80f34 | S399 | MSTR | 2026-08-14 | 6 |
| 8f8ceee22bf2 | S397 | MSTR | 2026-08-14 | 6 |
| 31d5712b7b5e | ORPHAN | MSTR | 2026-08-14 | 6 |
| abb064b00a91 | S401 | PFE | 2026-08-14 | 6 |
| 642173cb4f06 | S401 | PFE | 2026-08-14 | 6 |
| bae5933aa2e2 | S398 | MARA | 2026-08-14 | 6 |
| a66aef8afd56 | ORPHAN | MARA | 2026-08-14 | 6 |
| 5705f37d21d2 | S396 | MARA | 2026-08-14 | 6 |
| c3ecef2ec2c4 | S396 | MARA | 2026-08-14 | 6 |
| c40290b649a3 | S212 | MCD | 2026-08-14 | 6 |
| 76b7c973f2d9 | S212 | MCD | 2026-08-14 | 6 |

_Orphaned ledger detail omitted (975 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `31d5712b7b5e`
- `4d6324cf6582`
- `a66aef8afd56`
- `b8799cfc5b7f`
- `f7fdfc0bbe84`
