# Agent 5: Stop Overshoot Synthesis

**Date:** 2026-06-16  
**Agents 1–3 complete.** Agent 4 (sim) deferred — log-based counterfactual below.

---

## Verdict

Stops are not "misconfigured" at -0.5%. They are **not enforced in time** for your account shape (~$14–20 positions, live PDT guard, 15-min polls).

| Confirmed cause | Share of problem | Confidence |
|-----------------|------------------|------------|
| PDT blocks same-day software exit | **~80%** of look-into items (170/170 PDT) | High |
| Fractional → no GTC stop | **~100%** of positions at this size | High |
| 15-min check interval | Moderate (-0.6% to -1.5% slips) | Medium |
| Sell slippage / market fallback | Minor vs delay | Medium |
| Overnight gap on unprotected | Worst tail (-5% to -14%) | High |

**Rough extra loss from overshoot beyond -0.5% cap:** ~**$42** across all bad stop sells in logs (Agent 1).

---

## Ranked fix plan (execution only — approve before coding)

### Tier 0 — Do first (high impact, no strategy drift)

1. **Stop-only same-day exit exception**  
   Change PDT guard: block same-day **midline/max-hold** only; if `pnl_frac <= EXIT_STOP_LOSS`, **allow sell** even if `entered_today`.  
   *Addresses afternoon bleed on names like EME, NOV, ORCL.*

2. **Mandatory fractional software stop**  
   In every `exits` / `ext_exits` / scan exit loop: if `pnl <= EXIT_STOP_LOSS`, **always attempt `do_sell`** regardless of fractional / watch state.

3. **Deploy pipeline already pushed** — ensure cron includes prep + execute; monitor `cache_hit` / `duration_s`.

### Tier 1 — Next

4. Urgent stop sells: skip limit wait → market immediately when stop breached  
5. `ext_exits` (4–8pm ET): treat stop breach same as regular hours (currently skips midline only — verify stops attempted for fractional)  
6. Cron: exits every **5 min** during 10:00–16:00 ET (workflow/cron-job.org)

### Tier 2 — Optional / live account policy

7. Live: separate flag `ALLOW_SAME_DAY_STOP_EXIT = True` (default True after Tier 0)  
8. Paper: already relaxes via `STRICT_SAME_DAY_EXIT = not PAPER_TRADING`  
9. Broker: increase position size to ≥1 whole share on highest-vol names (sizing — discuss before changing)

---

## Agent 4 counterfactual (log-based, not full sim)

If every stop sell had exited at **-0.5%** instead of actual:

- June overshoot sells: ~171 cases  
- Estimated savings vs actual: **~$25–35** of the ~$42 total extra loss figure (remainder is positions that never got a stop sell at all until catastrophic)

---

## Recommended next step

**Tier 0 items 1–2 implemented** in `rubber_band_bot.py` (`_pdt_blocks_exit` — same-day stop exits allowed on live). Monitor 3 trading days and re-run `scripts/analyze_stop_overshoots.py`.

---

## Artifacts

| File | Agent |
|------|-------|
| `logs/analysis/stop_overshoot_timelines.md` | 1 |
| `logs/analysis/stop_overshoot_worst50.csv` | 1 |
| `logs/analysis/execution_path_review.md` | 3 |
| `docs/stop_exit_agent_plan.md` | Plan |
