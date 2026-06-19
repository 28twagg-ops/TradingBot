# Stop Exit Overshoot — Multi-Agent Investigation Plan

**Pushed:** pipeline + `merge_bot_logs.py` (commit `b04c7f5`).  
**Problem:** Stop threshold is **-0.5%** (`EXIT_STOP_LOSS = -0.005`) but realized stop sells are often **-1% to -14%** (208/211 stop sells worse than -0.5%; worst ORCL **-13.9%** on 2026-06-11).

---

## Root-cause hypotheses (agents must falsify/confirm)

| ID | Hypothesis | Evidence so far |
|----|------------|-----------------|
| H1 | **PDT same-day block** — buys at 9:45 can't exit until next day; intraday bleed logged in `stop_losses_to_look_into.txt` | 100% of look-into entries say "PDT guard deferred" |
| H2 | **Fractional positions** — ~$14–20 notional → `stop_qty < 1` → no GTC stop; only 15-min software checks | `ensure_stop` skips fractional |
| H3 | **Check interval lag** — price crosses -0.5% between cron runs; exit at next poll | Many exits at -0.6% to -1.5% |
| H4 | **Overnight gap** — unprotected fractional or stale entry-based stop; open far below stop | Worst losses often next-morning sells |
| H5 | **Slippage on market fallback** — `do_sell` limit timeout → market in fast moves | `execution_audit.csv` slippage on stop exits |
| H6 | **PnL reporting** — `exit_reason` uses Alpaca unrealized % at sell time, not trigger at -0.5% | Stop label shows actual exit % |

---

## Agent roster (run in parallel, then synthesize)

### Agent 1 — Forensics & timeline
- **Input:** `transactions.csv`, `execution_audit.csv`, `stop_losses_to_look_into.txt`, daily logs Jun 1–16
- **Tasks:** Per overshoot > -2%: entry date, first breach timestamp, sell timestamp, hold path, PDT deferred?, fractional?
- **Output:** `logs/analysis/stop_overshoot_timelines.md` + CSV of worst 50 exits

### Agent 2 — Broker / stop-order audit
- **Input:** Alpaca positions, open orders API (paper/live), `fractional_watch.json` after deploy
- **Tasks:** For each open position: whole-share qty, live GTC stop?, stop price vs entry vs current
- **Output:** Gap report — % positions without broker stop protection

### Agent 3 — Execution path review (read-only code)
- **Scope:** `do_sell`, `ensure_stop`, `run_exits`, `run_scan` exit loops — **no strategy changes**
- **Tasks:** Map every path from breach detection to fill; time spent waiting; when PDT skips
- **Output:** Flow diagram + list of fixable execution gaps (not signal changes)

### Agent 4 — Simulation / counterfactual
- **Input:** June transaction tape, sim harness if available
- **Tasks:** Counterfactual: same-day stop allowed on paper; 5-min vs 15-min check; mandatory fractional software exit
- **Output:** Estimated P&L delta vs actual (analysis only unless user approves code)

### Agent 5 — Synthesis & fix proposal (no implementation until approved)
- Merge Agent 1–4; rank fixes by impact vs risk
- **Proposed fix buckets (execution only):**
  1. Paper: `STRICT_SAME_DAY_EXIT = False` for stop-only exits (already wired for paper)
  2. Fractional: aggressive software stop every exits cron when `pnl <= EXIT_STOP_LOSS`
  3. Tighter urgent sells: reduce limit wait for stop exits
  4. EOD: refresh stops + ext_exits for fractional watch list
  5. Optional: intraday exits cron every 5 min during market hours (workflow only)
- **Explicitly out of scope:** changing `EXIT_STOP_LOSS`, signals, schedule, universe

---

## Success metrics (after fixes deployed)

- % stop sells with `pnl_pct` worse than **-1.0%** drops below 10% (from ~99% today)
- `stop_losses_to_look_into.txt` PDT-deferred rate drops on paper
- No regression in midline/max-hold exits or win rate on midline sells

---

## Immediate actions (today)

1. ✅ Push pipeline + log merge fix — next Actions run should not fail on `runs.csv` conflict
2. Re-run failed workflow or wait for next cron; confirm `duration_s` / `cache_hit` in `runs.csv`
3. Launch Agents 1–3 in parallel (readonly); Agent 4 if sim env available
4. User decision: live account still has `STRICT_SAME_DAY_EXIT=True` — same-day stops remain blocked on live until explicitly changed
