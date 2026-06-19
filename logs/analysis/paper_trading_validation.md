# Live Validation Log (replaces Phase E paper trading — 2026-06-19)

Minimum 10 trading days on live ~$500 Alpaca account before any forbidden-list parameter changes.
Rollback trigger: revert to `checkpoint-pdt-removal-2026-06-18` on crash, missed exit, buy spike >2x avg, or deprecated PDT API error.

**Holiday rule:** Non-trading days (NYSE holidays, weekends) do NOT count toward the 10-day window and are NOT missed runs.

| Date | Runs OK | Buys | Sells | Errors | Notes |
|------|---------|------|-------|--------|-------|
| 2026-06-19 | N/A | — | — | — | **Market Holiday — Juneteenth (NYSE/Nasdaq closed). No trading expected. Does not count toward 10-day window.** |

## Daily checklist

- [ ] `logs/runs.csv` — bot ran on schedule (skip on market holidays)
- [ ] `logs/analysis/daily_slippage_watch.md` — stop overshoot vs Jun 17 baseline (-0.33pp)
- [ ] `logs/daily/[date].md` — same-day midline/max-hold exits firing post-PDT removal
- [ ] Position count trending toward MAX_OPEN_POSITIONS=5
- [ ] GitHub Actions — no KeyError/AttributeError on account fields

## Pass criteria

- [ ] Zero crashes in 10 trading days
- [ ] Zero KeyError on account API fields
- [ ] Same-day midline exits observed (not just deferred)
- [ ] Stop exits via market_urgent_full
- [ ] No buy spike >2x normal daily count
- [ ] Slippage watch daily OK
- [ ] Daily reconcile OK

## Calendar notes

- **2026-06-19 (Fri):** Juneteenth — market closed. Resume monitoring **Mon 2026-06-22**.
- **Bot holiday awareness:** `detect_mode()` uses weekday only (`dow >= 5` → weekly). It does **not** check NYSE holiday calendar. If cron fires on Jun 19, the bot may attempt runs (likely no fills if market closed). Treat quiet holiday as non-event; do not flag as missed run.
