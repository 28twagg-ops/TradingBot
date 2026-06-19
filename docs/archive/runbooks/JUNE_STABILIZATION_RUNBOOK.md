# June Stabilization Runbook

This is the execution playbook for June so we can separate code/execution issues from true strategy degradation.

## 1) Baseline Confirmation (Completed)

Verified in `rubber_band_bot.py`:

- `EXIT_STOP_LOSS = -0.005`
- `EXIT_DAYS_MAX = 3`
- `SEASONAL_SIZE_PCT = 0.20`
- `OFFSCHEDULE_SIZE_PCT = 0.20`
- `CASH_RESERVE_PCT = 0.05`
- June schedule is `GapDown + VolumeSpike` (`SCHEDULE[6]`)

Verified workflow state in `.github/workflows`:

- Live workflow: `run_bot.yml`
- No duplicate `bot.yml` in this GitHub-linked repo

## 2) Daily June Audit Pipeline (Implemented)

Script: `tools/june_audit.py`

Outputs:

- `logs/analysis/june_audit_latest.md`

Daily command:

```powershell
py -3 tools/june_audit.py --out logs/analysis/june_audit_latest.md
```

With Alpaca export reconciliation:

```powershell
py -3 tools/june_audit.py --broker-csv "alpaca_orders_export.csv" --out logs/analysis/june_audit_latest.md
```

Audit checks performed:

- Duplicate same-day sell rows
- June daily-log mismatch (`No trades today` vs tx rows)
- `runs.csv` exits vs `transactions.csv` sell count mismatch by date
- Stop-loss overshoot rate (`stop_loss` with `pnl_pct <= -3.0%`) vs May baseline
- Optional broker-fill matching (date+ticker sell key)

## 3) June Simulation Alignment + Results (Completed)

Simulation schedule was aligned to live behavior (RubberBand in Apr/May/Nov) in:

- `c:\Users\28twa\Desktop\TradingBot\simulations\validation_sim.py`

Executed:

```powershell
py -3 simulations\validation_sim.py --tests 5 20 22 24 27 28 29 --years 20 --refresh-trades
```

Report:

- `c:\Users\28twa\Desktop\TradingBot\simulations\results\test_5_20_22_24_27_28_29.txt`

Key June metrics from that run:

- Test 5: June `GapDown + VolumeSpike` => `KEEP LIVE`
- Test 20 (June row):
  - `OLD +208.2%`, `NEW +290.4%`, `GAP +121.1%`
  - GAP win rate `49.6%`
- Test 27 (per-trade EV, GAP model):
  - `GapDown(Jun) EV +1.069%`
  - `VolumeSpike(Jun) EV +0.214%`
- Test 28 (execution lag risk):
  - `GapDown(Jun)` same-bar premium `+96.6pp`
  - `VolumeSpike(Jun)` same-bar premium `+144.5pp`
- Test 22 (spread sensitivity, full strategy):
  - at `0.10%` round-trip spread: ann `+30.4%`, WR `45.2%`
- Test 24 (stress): all-night gap model is severe (`-77.4%` total over sample)

## 4) June Expectation Bands + Decision Gates

Use these bands for weekly evaluation:

- `Optimistic`: Test 20 NEW June profile (`~+290%` monthly equivalent in sim context)
- `Realistic`: Test 20 GAP June profile (`~+121%` monthly equivalent, WR near `~50%`)
- `Stressed`: include Test 22 + Test 24 drag and Test 28 lag penalties (expect material degradation if fill timing slips)

Go/No-Go gates:

1. **Execution gate** (must pass first):
   - duplicate sells = `0`
   - June daily mismatch = `0`
   - run-vs-tx mismatch = `0`
   - June overshoot rate not worse than May baseline
2. **Broker reconciliation gate**:
   - Alpaca export supplied and all June sell rows matched
3. **Strategy gate** (only after execution+broker gates):
   - June sells >= `20`
   - June sell win rate >= `45.0%`
   - June avg P&L per sell >= `-0.10%`

If execution gates fail, treat performance as non-diagnostic and fix plumbing first.
If execution gates pass but strategy gate fails by month-end, treat as true edge degradation and move to schedule/entry redesign.
