# Rubber Band Bot — Document Timeline & Map

Quick navigation for humans and AI assistants. **Nothing is deleted** — older material lives under `archive/`.

---

## How to use this repo

| I need… | Go here |
|---------|---------|
| **Live bot code** | `rubber_band_bot.py` |
| **Current ops / cron** | `docs/ops/pipeline_validation.md` |
| **Live trade log** | `logs/transactions.csv` |
| **Live monitoring** | `logs/analysis/paper_trading_validation.md` |
| **Slippage watch** | `logs/analysis/daily_slippage_watch.md` |
| **A/B test (this week)** | `logs/ab_test/dashboard.md`, `week_review.md` |
| **Export for ChatGPT** | `docs/handoff/` (strategy rules + code inspection) |
| **Simulation code** | `simulations/` |
| **Old reports / handoffs** | `docs/archive/` and `logs/analysis/archive/` |

---

## Timeline (major events & documents)

### 2026-05 — Live validation & strategy tuning

| Date | Event / document | Location |
|------|------------------|----------|
| May 2–10 | Validation sim runs; stop -0.5%, hold 3d OOS wins | `simulations/validation_sim.py` |
| May 3 | Schedule regression (RSI vs RubberBand) | validation tests 14–17 |
| May 10 | Position sizing sweep (20%/20% wins) | Test 18 |
| May 13 | Earnings filter study (+16pp CAGR in sim) | `EARNINGS_SKIP_DAYS` in bot |
| May 22+ | Live trading begins (transactions.csv) | `logs/transactions.csv` |

### 2026-05 — June prep & display proposals

| Document | Location |
|----------|----------|
| Bot display / mode naming proposal | `TradingBot/docs/proposals/` (local workspace) |
| Strategy effectiveness reports | `docs/archive/` / local `docs/analysis/` |

### 2026-06-10 — June incident & stabilization

| Date | Event / document | Location |
|------|------------------|----------|
| Jun 10 | Stop-loss / morning-run incident | `docs/archive/incidents/june_10_incident_report.md` |
| Jun 10 | Stabilization runbook | `docs/archive/runbooks/JUNE_STABILIZATION_RUNBOOK.md` |
| Jun 10 | June audit | `logs/analysis/archive/june_audit_latest.md` |

### 2026-06-11 — 18 — Execution & slippage investigation

| Document | Location |
|----------|----------|
| Stop overshoot synthesis | `logs/analysis/archive/stop_overshoot_synthesis.md` |
| Stop timelines / worst 50 | `logs/analysis/archive/stop_overshoot_*.md/csv` |
| Live slippage profile (Jun 16) | `logs/analysis/live_slippage_profile_2026-06-16.md` |
| Daily slippage watch (ongoing) | `logs/analysis/daily_slippage_watch.md` |
| Execution path review | `logs/analysis/archive/execution_path_review.md` |
| Stop/exit agent plan | `docs/archive/agent_plans/stop_exit_agent_plan.md` |

### 2026-06-16 — 17 — Simulation studies

| Study | Location |
|-------|----------|
| Strategy expansion 3yr / 20yr | `logs/analysis/archive/strategy_expansion_*` |
| Overnight PDT validation | `logs/analysis/archive/overnight_pdt_*` |
| Return methodology note | `logs/analysis/archive/return_methodology_report.md` |
| PDT schedule sim (pre-removal suite) | `logs/analysis/archive/pdt_schedule_sim_*` |
| Validation 20yr test exports | `logs/analysis/archive/validation_*` |

### 2026-06-18 — PDT removal checkpoint

| Event | Location |
|-------|----------|
| Git tag `checkpoint-pdt-removal-2026-06-18` | git tags |
| PDT removal audit | `logs/analysis/pdt_removal_audit.md` |
| PDT removal sim suite | `simulations/pdt_removal_suite.py`, `pdt_schedule_engine.py` |
| Stage 1 empirical gate **failed** (-0.8% threshold) | `simulations/results/pdt_removal/OVERNIGHT_RUN_STOPPED_AT_STAGE_1.md` |

### 2026-06-19 — Handoffs & independent review exports

| Document | Location |
|----------|----------|
| Strategy export (rules + history) | `docs/handoff/STRATEGY_EXPORT_FOR_INDEPENDENT_REVIEW.txt` |
| Transactions export | `docs/handoff/transactions_full_export.csv` |
| Code inspection for ChatGPT | `docs/handoff/CODE_INSPECTION_FOR_CHATGPT_2026-06-19.txt` |
| Full situation brief | `docs/archive/briefs/FULL_SITUATION_BRIEF_FOR_REVIEW.txt` |
| Claude next steps (archived copy) | `docs/archive/handoff/CLAUDE_NEXT_STEPS_HANDOFF.txt` |
| Project handoff v9 | `docs/archive/handoff/PROJECT_HANDOFF_V9.txt` |
| Transfer document | `docs/archive/handoff/TRANSFER_DOCUMENT.txt` |

### 2026-06-20+ — A/B concentration test (live)

| Item | Location |
|------|----------|
| Ratio-based A/B sizing in live bot | `rubber_band_bot.py` (`AB_TEST_*` config) |
| A/B dashboard | `logs/ab_test/dashboard.md` |
| Week review report | `logs/ab_test/week_review.md` |
| Sorted trade export | `logs/ab_test/trades_sorted.csv` |

---

## Archive index (combined reference)

See `docs/archive/combined/ARCHIVE_INDEX.txt` for a flat file list of everything in `docs/archive/` and `logs/analysis/archive/`.

---

_Last updated: 2026-06-20_
