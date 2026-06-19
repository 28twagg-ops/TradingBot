# Live Validation Log (replaces Phase E paper trading — 2026-06-19)

Minimum 10 trading days on live ~$500 Alpaca account before any forbidden-list parameter changes.
Rollback trigger: revert to `checkpoint-pdt-removal-2026-06-18` on crash, missed exit, buy spike >2x avg, or deprecated PDT API error.

| Date | Runs OK | Buys | Sells | Errors | Notes |
|------|---------|------|-------|--------|-------|

## Daily checklist

- [ ] `logs/runs.csv` — bot ran on schedule
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
