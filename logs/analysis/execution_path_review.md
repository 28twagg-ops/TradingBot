# Agent 3: Execution Path Review (Stop Exits)

Read-only review of `rubber_band_bot.py` — no strategy logic touched.

## Stop detection paths

| Path | When | Data source | Can sell same day? |
|------|------|-------------|-------------------|
| `run_exits` / `ext_exits` | Every 15 min | Alpaca `pnl_pct` | **No** if `STRICT_SAME_DAY_EXIT` (live) |
| `run_scan` exit loop | 9:45 / 3:45 | Same + yfinance midline | **No** if entered today (live) |
| `ensure_stop` GTC | After buys, start of exits | Entry × 0.995 | Broker — **skipped if qty < 1 share** |
| `place_eod_stops` | End of evening scan | Current × 0.995 | Broker — **skipped fractional** |

## Failure chain (confirmed)

```
Morning buy (~$14–20 notional)
  → fractional qty (< 1 whole share)
  → ensure_stop SKIPPED
  → STRICT_SAME_DAY_EXIT blocks software sell
  → logged to stop_losses_to_look_into (PDT deferred)
  → price drifts -2% to -14% until next session
  → do_sell at market/limit with 5–20s polls
  → log_tx shows large stop_loss % (actual exit, not trigger)
```

## `do_sell` timing (stop exits use urgency=`urgent` → 1×5s poll)

- Limit sell at ~0.2% below market, wait **5s once**, then market fallback
- Extended hours: limit only, **no market fallback**, may stay pending
- Not the main overshoot driver — **late trigger** is

## Gaps fixable without strategy changes

| Priority | Fix | File / function |
|----------|-----|-----------------|
| P0 | Allow **stop-only** same-day exits on live (block same-day midline only) | `run_exits`, `run_scan` PDT guard |
| P0 | **Never skip** software stop for fractional when `pnl <= EXIT_STOP_LOSS` | exit loops |
| P1 | Register fractional in watch + **priority sort** (already partial) | `ensure_stop`, exit loops |
| P1 | `ext_exits` must attempt stop for all breached fractional same day | `run_exits(extended_hours=True)` |
| P2 | Urgent sells: 0 polls + immediate market for stop breach | `do_sell(urgency="urgent")` |
| P2 | More frequent exits cron (5 min) — workflow only | `run_bot.yml` / cron-job.org |

## What NOT to change

- `EXIT_STOP_LOSS` (-0.5%), `get_signals`, `SCHEDULE`, entry sizing
