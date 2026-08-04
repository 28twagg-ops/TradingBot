# Ledger health — 2026-08-04

_Generated 2026-08-04T14:31:18.013495_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN |
| Missing exit records (post) |   398 | WARN |
| State/ledger mismatches     |    21 | WARN |
| Total open lots             |   208 | INFO |
| Total closed lots           |   747 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (398 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `10db07a6929b`
- `1fad73c5bd2e`
- `4a4c70b87132`
- `569727d8d096`
- `6298d22f4b19`
- `68bdcedb58bf`
- `6a620ea1b5c4`
- `73452d4fd996`
- `8223917270ff`
- `8ee0d51f85ea`
- `9904d193bdc7`
- `a1454a513022`
- `cfe874780e99`
- `d0f74d60de78`
- `dc93f1bb26fb`
- `edbee006e808`
- `eea58313d5b0`
- `ef182507a898`
- `f0deab08c6cf`
- `f750daf33a54`
- `fbb330ec2ca3`
