# Profitability Research Report

**Generated:** 2026-10-23 16:30 UTC  
**Branch work:** paper research + safety; live entries remain OFF  
**LIVE_OPTIONS_ENTRIES:** fail-closed default `0` (unchanged)  
**LIVE_OPTIONS_MAX_CAP:** hard maximum `$250` (configs above rejected)  

## Data sources (every figure cites these)

- `ledger` → `C:\Users\28twa\Documents\Other Desktop Stuff\TradingBot-git\logs\options_trial\_ledger\master_ledger.csv`
- `selection` → `C:\Users\28twa\Documents\Other Desktop Stuff\TradingBot-git\logs\options_trial\reports\2026-10-23_strategy_selection.md`
- `quality` → `C:\Users\28twa\Documents\Other Desktop Stuff\TradingBot-git\logs\options_trial\reports\2026-10-23_data_quality.md`
- `selection_csv` → `C:\Users\28twa\Documents\Other Desktop Stuff\TradingBot-git\logs\options_trial\reports\2026-10-23_strategy_selection.csv`
- Analysis outputs → `C:/Users/28twa/Documents/Other Desktop Stuff/TradingBot-git/research/options-strategies/results`

---

## A. What Actually Makes Money?

Primary lens is **CLEAN** (natural TP/SL/EOD on non-outage days). ALL includes TAINTED reconcile/outage mass and can invent or destroy dollars.

### CLEAN keepers among priority arms

| Strategy | CLEAN n | WR% | Med% | CLEAN $ | $/trade (after $2 cost) | Status |
|---|---:|---:|---:|---:|---:|---|
| S397 | 35 | 68.6 | +56.1 | $+1,072 | $+28.63 | PROFITABLE IN EXPLORATORY PAPER |
| S166 | 12 | 66.7 | +60.8 | $+314 | $+24.17 | PROMISING BUT UNVALIDATED |
| S167 | 19 | 63.2 | +106.0 | $+450 | $+21.68 | PROMISING BUT UNVALIDATED |
| S404 | 53 | 64.2 | +53.2 | $+1,161 | $+19.91 | PROFITABLE IN EXPLORATORY PAPER |
| S362 | 33 | 66.7 | +57.1 | $+792 | $+22.00 | PROFITABLE IN EXPLORATORY PAPER |
| S406 | 75 | 58.7 | +53.3 | $+930 | $+10.40 | PROFITABLE IN EXPLORATORY PAPER |
| S410 | 10 | 60.0 | +58.3 | $+142 | $+12.20 | PROMISING BUT UNVALIDATED |

### S406 CLEAN vs ALL dollar gap

- CLEAN: n=75, $+930, med +53.3% (source: `C:\Users\28twa\Documents\Other Desktop Stuff\TradingBot-git\logs\options_trial\_ledger\master_ledger.csv` + CLEAN tag rules in `options_data_quality_report.py`)
- ALL: n=143, $+3,191, med +50.0%
- Gap (ALL − CLEAN) = **$+2,261** — extra ALL dollars are mostly TAINTED / reconcile-path outcomes, not proven alpha.
- After $2/contract cost drag: CLEAN net $+780 ($+10.40/trade).

### S404

- CLEAN $+1,161 (n=53, WR 64.2%, med +53.2%) vs ALL $+909 — ALL median collapses when TAINTED days included (ALL med +26.7%).

### Winner vs loser pre-decision traits

Features available at decision time only (cost, spread, exit-reason shares).

| strategy_id   | cohort   |   n |   med_cost | med_spread   |   med_ret_pct |   top_symbol_share |   eod_share |   tp_share |   sl_share |
|:--------------|:---------|----:|-----------:|:-------------|--------------:|-------------------:|------------:|-----------:|-----------:|
| S166          | winner   |  10 |       58.5 |              |        70.045 |           0.5      |           0 |   0.8      |   0        |
| S166          | loser    |   5 |       40   |              |       -50.79  |           0.4      |           0 |   0        |   0.8      |
| S167          | winner   |  12 |       29.5 |              |       142.11  |           0.5      |           0 |   1        |   0        |
| S167          | loser    |  12 |       40.5 |              |       -56.67  |           0.166667 |           0 |   0        |   0.583333 |
| S362          | winner   |  42 |       37   |              |        72.505 |           0.285714 |           0 |   0.52381  |   0        |
| S362          | loser    |  21 |       59   |              |       -54.93  |           0.285714 |           0 |   0        |   0.52381  |
| S397          | winner   |  31 |       66   |              |        73.02  |           0.258065 |           0 |   0.774194 |   0        |
| S397          | loser    |  20 |       58.5 |              |       -58.285 |           0.2      |           0 |   0        |   0.55     |
| S404          | winner   |  48 |       63.5 |              |        65.025 |           0.208333 |           0 |   0.708333 |   0        |
| S404          | loser    |  45 |       57   |              |       -50     |           0.155556 |           0 |   0        |   0.466667 |
| S406          | winner   |  80 |       27.5 |              |        75.365 |           0.175    |           0 |   0.55     |   0        |
| S406          | loser    |  63 |       41   |              |       -50     |           0.174603 |           0 |   0        |   0.492063 |
| S410          | winner   |   7 |       71   |              |        77.78  |           0.714286 |           0 |   0.857143 |   0        |
| S410          | loser    |   4 |       68.5 |              |       -68.455 |           0.75     |           0 |   0        |   1        |
| S430          | winner   |   2 |       41   |              |        63.415 |           1        |           0 |   1        |   0        |
| S430          | loser    |   2 |       44.5 |              |       -43.165 |           0.5      |           0 |   0        |   1        |
| S432          | winner   |   2 |       23.5 |              |        94.46  |           0.5      |           0 |   1        |   0        |
| S432          | loser    |   2 |       38   |              |       -38.015 |           0.5      |           0 |   0        |   1        |

Effects separation (qualitative from ledger structure):

- **Underlying move:** RubberBand/GapDown winners show higher TP share; losers cluster on stop_loss/EOD — consistent with underlying direction, not only IV.
- **Contract choice:** ITM3 (S406) vs OTM2 (S404) vs ITM1 (S397) — CLEAN medians similar (~53–56%) but S404 has better CLEAN $ density; OTM increases left-tail risk on ALL.
- **Timing:** DayTrader S430–S432 still n≤4 — not attributable.
- **Optimistic fills:** paper ask−0.01 + virtual $500 buckets overstate concurrency vs $250 live sleeve (see constrained sim).

---

## B. What Is Losing Money?

| Strategy | CLEAN n | Med% | CLEAN $ | ALL $ | Status |
|---|---:|---:|---:|---:|---|

Book-level drag (from `2026-10-23_data_quality.md`):

- TAINTED exits: n=2036, −$11,713 — ops/reconcile, not strategy alpha.
- Orphan exits: 422 / 3775 = **11.2%** — attribution debt (history preserved; live micro now normalizes OCC + best-effort reclaim).
- CLEAN kill list leaders (S212, S202, S360, …) remain non-attractive; not re-promoted here.

---

## C. Best New Experiments (implemented)

New strategy IDs only (S404/S406 paper twins preserved). **Awaiting forward paper evidence** — no live enablement.

| ID | Name | Hypothesis | Mechanics vs baseline |
|---|---|---|---|
| **S440** | RubberBand_ITM3_StrongGap | Stronger gap (≤−3%) cuts S406 left tail | RB reclaim + GAP_STRONG; strike ITM3 |
| **S441** | GapDown_OTM2_StrongGap | S404 structure + S166 gap quality | Gap ≤−3%, OTM2 |
| **S442** | RubberBand_ITM3_5DTE | DTE neighbor to S362/S406 | ITM3, 5 DTE |
| **S443** | TrueORB_15m | Classical ORB ≠ S430 drive proxy | ≥15m session, stronger drive/high |

Paper buckets (research-only):

- `b92 s406_maxprem40` — S406 scope, max_premium=$40 (left-tail / cost).
- `b93 s440_rb_stronggap` — dedicated S440 sleeve.

Code: `live-bots/options-paper/strategies/options_signals.py` (PROFITABILITY_EXPERIMENT_STRATEGIES), `live-bots/options-paper/lab/options_lab.py` (bucket 92/93 inject).

---

## D. Best Portfolio Combination (constrained sim)

Arms tested: S406 + S404 + S397 + S362 (CLEAN replay).

| Mode | Fills | Skip capital | Skip concurrency | Realized $ | End cash | Max DD |
|---|---:|---:|---:|---:|---:|---:|
| Discovery (unconstrained) | 196 | 0 | 0 | $+3,955 | $4,205 | $-561 |
| Capital-constrained ($250 opts) | 71 | 0 | 125 | $+652 | $902 | $-122 |
| Combo constrained | 36 | 0 | 32 | $+939 | $1,189 | $-136 |

**Minimum practical account (estimate):** $600 — $250 stock reserve + $250 options research sleeve + ~$100 buffer; below ~$600 concurrent 2-contract options + stock reserve is impractical

Correlation (CLEAN daily P&L):

| strategy_id   |   S362 |   S397 |   S404 |   S406 |
|:--------------|-------:|-------:|-------:|-------:|
| S362          |   1    |   0.07 |   0.14 |   0.62 |
| S397          |   0.07 |   1    |   0.91 |   0.13 |
| S404          |   0.14 |   0.91 |   1    |   0.22 |
| S406          |   0.62 |   0.13 |   0.22 |   1    |

**Portfolio read:** Prefer at most one GapDown family (S404 **or** S397) plus one RubberBand family (S406 **or** S362) under a $250 options sleeve — correlation and capital skips make four-arm concurrency unrealistic. **Do not recommend live execution.**

---

## E. Next Steps to Genuine Profitability

1. Keep `LIVE_OPTIONS_ENTRIES=0` until S440/S441 forward n≥20 CLEAN and p10 protocol clears.
2. Collect forward paper on S440–S443 + b92/b93 for 10–15 sessions.
3. Drive orphan rate &lt;10% via OCC-normalized reclaim (shipped) + paper `attribute_vanished_lots` monitoring.
4. Re-run constrained sim monthly; treat discovery $ as upper bound only.
5. Separate Myers research — live trading stays disabled there.
6. No Rubber Band / production live behavior changes without explicit approval.

---

## Safety confirmation

| Control | Status |
|---|---|
| LIVE_OPTIONS_ENTRIES | **0** workflow + fail-closed parser |
| Options hard max | **$250** (reject &gt;250 / NaN / inf) |
| Stock cash reserve | **$250** |
| Broker query fail-closed | Entries abort; manage still runs |
| DayTrader freshness | Same-day disk TTL; no RTH disk pin; incomplete morning grace |
| Main merge | **Not merged** |
