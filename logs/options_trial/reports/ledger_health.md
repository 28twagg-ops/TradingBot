# Ledger health — 2026-07-20

_Generated 2026-07-20T12:35:44.332498_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-10** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN |
| Missing exit records (post) |    27 | WARN |
| State/ledger mismatches     |     9 | WARN |
| Total open lots             |    14 | INFO |
| Total closed lots           |   272 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-10).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-10 lot_id churn after attribution fix (INFO, not WARN).

## Orphaned ledger entries (detail)

| lot_id | strategy | symbol | entry_day | age_days |
|--------|----------|--------|-----------|---------:|
| 69035bbe54ed | S165 | INTC | 2026-07-13 | 7 |
| acd35e3d9d37 | S165 | INTC | 2026-07-13 | 7 |
| 7e3efbcbee4d | S165 | INTC | 2026-07-13 | 7 |
| 315408291e9d | S173 | SMCI | 2026-07-13 | 7 |
| 81cbb1d143b4 | S173 | SMCI | 2026-07-13 | 7 |
| c7c921ac55b3 | S173 | SMCI | 2026-07-13 | 7 |
| 9499278895a8 | S173 | SMCI | 2026-07-13 | 7 |
| 7a915749c7e3 | S173 | AMD | 2026-07-13 | 7 |
| e5e4a424e123 | S173 | AMD | 2026-07-13 | 7 |
| 9ab08bd47c31 | S174 | AVGO | 2026-07-13 | 7 |
| 0299cfa5bb54 | S165 | HL | 2026-07-13 | 7 |
| 5e6fb2e3314a | S165 | HL | 2026-07-13 | 7 |
| 1a9aa13a72c1 | S173 | AMD | 2026-07-13 | 7 |
| 174fad3a5c93 | S173 | AMD | 2026-07-13 | 7 |
| 82b23daf2111 | S173 | AMD | 2026-07-13 | 7 |
| 43108024132f | S173 | AMD | 2026-07-13 | 7 |
| 8e079ecd2e01 | S173 | AMD | 2026-07-13 | 7 |
| 2920355fb151 | S174 | INTC | 2026-07-13 | 7 |
| 11796ab3d72d | S165 | MSFT | 2026-07-14 | 6 |
| 135cee9ff4b0 | S165 | MSFT | 2026-07-14 | 6 |
| 8b2091753041 | S165 | MSFT | 2026-07-14 | 6 |
| 6f7835a223cc | S173 | C | 2026-07-14 | 6 |
| e229674c717d | S165 | BSX | 2026-07-14 | 6 |
| c2de9fef4808 | S173 | ADBE | 2026-07-14 | 6 |
| 3c43a209d835 | S173 | C | 2026-07-14 | 6 |
| 55a88a33b549 | S173 | ADBE | 2026-07-14 | 6 |
| 8c19f86893e9 | S173 | ADBE | 2026-07-14 | 6 |

## State/ledger mismatches

- `20d644c8e972`
- `2dcba6f79273`
- `486b1eb6d22e`
- `5b7d6a634930`
- `79ff86ea5f4e`
- `a5ae36cde254`
- `b5f619f67e1d`
- `e60117a0df51`
- `faa77572aad3`
