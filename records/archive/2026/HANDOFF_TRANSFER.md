# TradingBot + Myers — Comprehensive Handoff Transfer Document

**Purpose:** Paste this into a new AI chat so it can understand the full project: what we built, why, results, failures, and what to do next — without rediscovering context.

**Document date:** 2026-10-21  
**Repo:** [https://github.com/28twagg-ops/TradingBot](https://github.com/28twagg-ops/TradingBot)  
**Authoritative workspace root (git):**  
`C:\Users\28twa\Documents\Other Desktop Stuff\TradingBot-git`  

**Also opens as:** `C:\Users\28twa\Desktop\TradingBot-git` (Windows junction/symlink to the Documents path — same tree).

**Honesty rule:** Numbers below are from files on disk or `origin/main` as of this write. Uncertain items are marked. Do **not** invent fills, P&L, or commits.

---

## 0. Executive snapshot (read first)

| System | What it is | Live trading? | Current posture |
|---|---|---|---|
| **TradingBot options** | Morning paper lab + paused live micro-sleeve | Live **entries OFF** (`LIVE_OPTIONS_ENTRIES=0`); manage/orphans only; **$250 cap** | Paper: promising cohort ≥75 unique + one bucket/strategy + S404/S406 twins. DayTrader S430–S432 additive. |
| **Rubber Band stock bot** | Equity overnight/pullback live bot (`rubber_band_bot.py`) | LIVE (small account historically ~$480–500) | Separate account/truth from options. Do not mix. |
| **Myers Stock Investor** | Business-acquirer research/backtest spin-off under `myers-stock-investor/` | **Disabled** (`live_trading_enabled: false`) | v1.1 audited engine; exploratory only; cash-heavy underperformance vs SPY under strict rules. |
| **Rainbow BTC/ETH research** | Walk-forward log-regression bands | N/A (research) | Buy-hold crushed band timing; both in band 3 Accumulate (~2026-10-16). |

**Standing rules (non-negotiable):**

1. **Two bots, two accounts, two truths** — Rubber Band LIVE ≠ Options PAPER ≠ Myers research.
2. **+16,719% options historical chart is NOT real edge** — Black-Scholes / synthetic ranking artifact only.
3. **Do not merge Myers into the options bot.**
4. **Do not re-enable live options entries** without twin/paper edge review and explicit human approval.
5. **Day Trader Analytics buckets are additive only** — do not rewrite KEEP/twin arms to “make room.”

---

## 1. Repo / dual-path / git context

### 1.1 Remote

- **GitHub:** `28twagg-ops/TradingBot`
- **Remote URL:** `https://github.com/28twagg-ops/TradingBot.git`
- Default branch: `main`
- GitHub Actions workflow for the combined morning/day run: `.github/workflows/run_bot.yml`
- Bot runs **commit logs/results back to `main`** frequently (`bot run YYYY-MM-DD HH:MM UTC`). Local clones are often **behind** `origin/main`.

### 1.2 Local vs origin (as of 2026-10-21 inspection)

| Fact | Value |
|---|---|
| Local HEAD | `b397c7118e` — *Add Day Trader Analytics buckets (S430-S432)…* (2026-10-15) |
| Local vs `origin/main` | **Behind by ~341 commits** (almost all bot-run commits) |
| Latest `origin/main` tip (sample) | `2a258b8532 bot run 2026-10-20 19:27 UTC` |
| Untracked / local-only work commonly present | `myers-stock-investor/`, `scripts/crypto_rainbow_backtest.py`, `scripts/midcap_*.py`, `logs/research/*` |

**Implication for next agent:** Pull or `git show origin/main:…` when you need newest paper reports (e.g. `logs/options_trial/reports/2026-10-20_*`). Local may stop at 2026-10-15 report files even though remote has 2026-10-20.

### 1.3 Desktop vs Documents path quirk

- Cursor workspace may show `c:\Users\28twa\Desktop\TradingBot-git`.
- `git rev-parse --show-toplevel` resolves to  
  `C:/Users/28twa/Documents/Other Desktop Stuff/TradingBot-git`.
- Desktop path is a **junction** to the Documents tree — edits land in one place. Prefer the Documents path for absolute commands if confused.

### 1.4 Separate trees — do not mix

```
TradingBot-git/                    ← options paper/live + rubber band + research scripts
  rubber_band_bot.py
  scripts/options_*.py
  .github/workflows/run_bot.yml
  logs/options_trial/…
  logs/research/…                  ← rainbow, midcap research outputs
  myers-stock-investor/            ← SPIN-OFF (own package, own outputs, no shared orders)
```

Myers must **not** share Alpaca keys, bucket ledgers, strategy IDs, or GHA steps with the options lab.

---

## 2. TradingBot — what it is

### 2.1 Architecture (options)

| Layer | Role | Key files |
|---|---|---|
| Signals | Scan universe → strategy hits | `scripts/options_signals.py` |
| Morning bot | Paper scan/place/manage windows | `scripts/options_morning_bot.py` |
| Lab / buckets | Virtual $500 buckets, cohort, twins, shared-OCC block | `scripts/options_lab.py` |
| Strategy lab | Registry, auto-kill evaluate, bucket generation | `scripts/options_strategy_lab.py` |
| Live micro | Tiny LIVE options sleeve | `scripts/options_live_micro.py` |
| Reports | Selection, DQ CLEAN/TAINTED/KEEP, buckets | `scripts/options_strategy_selection_report.py`, data-quality / daily bucket reports |
| Orchestration | GHA weekday runs | `.github/workflows/run_bot.yml` |

Older transfer packets (superseded for strategy lists but still useful for rules):

- `docs/CLAUDE_TRANSFER_2026-07-26.txt`
- `docs/ESCALATION_PROTOCOL.md`
- Session logs under `docs/SESSION_WORK_LOG_*.txt`

### 2.2 Live options micro-sleeve (PAUSED entries)

From `.github/workflows/run_bot.yml` (current local/workflow values):

| Env | Value | Meaning |
|---|---|---|
| `LIVE_OPTIONS_ENTRIES` | `0` | **No new buys** — manage / orphan adopt only |
| `LIVE_OPTIONS_MAX_CAP` | `250` | Hard dollar firewall |
| `LIVE_STOCK_CASH_RESERVE` | `250` | Protect stock half of account |
| `LIVE_OPTIONS_SHARE` | `0.25` | Soft share of equity |
| `LIVE_OPTIONS_ALLOW` | `S404,S406` | Allowed live strategies (S218 removed — CLEAN-KILL) |
| `LIVE_OPTIONS_MIN_COST` | `20` | Lottery-ticket filter (min premium) |

**Status:** Live options is a **risk-managed parking/manage path**, not an active entry engine. Paper twins exist to decide if/when entries could reopen.

### 2.3 Paper lab — current operating mode

Workflow paper env (abbreviated):

| Flag | Value | Intent |
|---|---|---|
| `OPTIONS_PAPER_UNLIMITED` | `1` | Not constrained by tiny paper equity |
| `OPTIONS_MIRROR_LIVE` | `1` | Run live 1:1 twin buckets |
| `OPTIONS_VARIATION_STUDY` | `1` | Cohort study alongside twins |
| `OPTIONS_CONTROLLED_LAYOUT` | `1` | Lab-generated controlled buckets |
| `OPTIONS_PROMISING_COHORT` | `1` | Auto-build ≥N unique strategies |
| `OPTIONS_PROMISING_MIN` | `75` | Target ≥75 unique |
| `OPTIONS_ONE_BUCKET_PER_STRATEGY` | `1` | One dedicated bucket per strategy (not window×rep spam) |
| `OPTIONS_MIRROR_STRATEGIES` | `S404,S406` | Twin arms |
| `OPTIONS_BLOCK_SHARED_OCC` | `1` | Refuse new entry on OCC already held/pending |
| `OPTIONS_BLOCK_KILL_STRATEGIES` | `1` | Block dynamic CLEAN kill list |
| `OPTIONS_BUCKET_COUNT` | `1800` | Capacity for large cohort |
| `OPTIONS_MAX_NEW_ENTRIES_PER_RUN` | `200` | Cap burst entries |

**Twins in code (`options_lab.py`):**

- Bucket **90** / name `live_1to1` — mirror of live allow set
- Bucket **91** / name `s406_only` — S406-only twin

### 2.4 KEEP vs KILL / CLEAN vs TAINTED / orphans / shared-OCC

| Concept | Meaning |
|---|---|
| **CLEAN** | Natural TP/SL/EOD exits on healthy runtime days |
| **TAINTED** | `reconcile_fill`, broker-missing, known outage days (e.g. 2026-08-01, 2026-08-06) |
| **KEEP-only** | CLEAN exits from strategies with n≥10, med≥0%, win≥50% (optimistic lens) |
| **KILL (CLEAN kill list)** | n≥10 & med≤−20% on CLEAN — used to block new entries when `OPTIONS_BLOCK_KILL_STRATEGIES=1` |
| **Orphans** | Exits attributed to `b0` / `orphan_reconcile` / `ORPHAN` — attribution failures, not alpha |
| **Shared-OCC block** | Prevents multiple lab lots stacking the same OCC |

**Auto-kill thresholds** (strategy lab / selection pipeline — still the standing design):

- KILL: median < −25% at n≥15 **or** p10 < −85% **or** WR < 15% at n≥25  
- KEEP (pipeline sense): median > −10% at n≥30  
- PROMOTE: median > 0% at n≥30  
- Fat left tail note: p10 < −45% flags risk even when median is green

---

## 3. Day Trader Analytics (S430–S432)

### 3.1 Why added

User wanted **day-trader style ORB / relative-strength** paper arms **without** disturbing existing KEEP / twin machinery. Solution: **additive** strategies + dedicated named buckets.

### 3.2 Commit

- **`b397c7118e`** — *Add Day Trader Analytics buckets (S430-S432) for paper ORB/RS arms.*  
- AuthorDate: 2026-10-15  
- Touched: `scripts/options_signals.py`, `options_lab.py`, `options_morning_bot.py`, `.github/workflows/run_bot.yml`  
- Reported as **pushed** to origin (DayTrader code is on the lineage that remote continued from).

### 3.3 Spec

| ID | Name | Idea |
|---|---|---|
| **S430** | `DayTrader_ORB` | Opening-drive / ORB proxy on session bar (gap floor, drive ≥0.4%, high ≥ open×1.003, close > open) |
| **S431** | `DayTrader_RS` | Relative strength vs SPY (stock day-ret > 0, RS ≥ 0.6%, near MA20, VZ≥0); needs SPY context |
| **S432** | `DayTrader_ORB_RS` | S430 AND RS ≥ 0.4% vs SPY |

- Bucket profile names: `day_trader_analytics_s430` / `_s431` / `_s432`
- Buy window: **10:05–10:45** ET (morning)
- Always injected into promising cohort; IDs collide-check against existing paper strategies
- DTE window in StrategyConfig: 3 / 1 / 7 (same pattern as many paper arms)

### 3.4 Latest known paper status (~2026-10-20 on `origin/main`)

From `origin/main:logs/options_trial/reports/2026-10-20_strategy_selection.md`:

| ID | Exits | Win% | Med% | Realized $ | Pipeline | Notes |
|---|---:|---:|---:|---:|---|---|
| **S430** | 3 | 33% | −40.38% | −$17 | **WATCH** | Slightly red; tiny n |
| **S431** | 0 | — | — | $0 | **NEW / silent** | No exits yet |
| **S432** | 2 | 50% | +14.84% | −$18 | **WATCH** | Mixed; tiny n |

**Verdict:** Insufficient sample. Do not promote or kill. Keep collecting.

---

## 4. Paper performance snapshot (latest known)

### 4.1 Data quality — 2026-10-15 (local report)

Source: `logs/options_trial/reports/2026-10-15_data_quality.md`

| Slice | n | Win% | Med% | Realized $ |
|---|---:|---:|---:|---:|
| ALL | 3687 | 39.7 | −38.5 | +$7,701 |
| CLEAN | 1685 | 48.4 | −25.0 | +$18,645 |
| TAINTED | 2002 | 32.4 | −40.4 | −$10,944 |
| **KEEP-only** | **826** | **61.0** | **+51.0** | **+$12,816** |

≈ **$12.8k KEEP-only**, ~61% win, ~+51% median — **full book diluted** by TAINTED/orphans/losers.

### 4.2 Data quality — 2026-10-20 (`origin/main`)

| Slice | n | Win% | Med% | Realized $ |
|---|---:|---:|---:|---:|
| ALL | 3719 | 39.7 | −39.0 | +$7,457 |
| CLEAN | 1711 | 48.3 | −26.2 | +$18,555 |
| TAINTED | 2008 | 32.3 | −40.6 | −$11,098 |
| **KEEP-only** | **847** | **60.6** | **+50.9** | **+$12,761** |

### 4.3 Twins / promote candidates (2026-10-20 selection, origin)

| Strategy | Exits | Win% | Med% | p10% | Note |
|---|---:|---:|---:|---:|---|
| **S406** RubberBand_ITM3 | 132 | 60.6 | +52.98 | −58.54 | Promote-list / Tyler review; **fat left tail** |
| **S404** GapDown_OTM2 | 87 | 55.2 | +45.07 | −68.57 | Promote-list / Tyler review; **fat left tail** |
| S218 BB_Lower_Touch | 109 | 50.5 | +22.22 | −71.43 | Was live-allowed historically; **CLEAN-KILL**; not in `LIVE_OPTIONS_ALLOW` / mirror |

**Not live-ready:** positive medians with p10 ≪ −45% fail escalation left-tail spirit. Entries stay paused.

### 4.4 Attribution health

- Orphan rate **~11.3–11.5%** (alert threshold 10%) as of mid/late Oct reports  
- Silent / zero-exit strategies remain **common** (many S200-series, BBSqueeze/VolClimax grids, pattern arms still at n=0)

### 4.5 CLEAN KEEP list examples (2026-10-15 DQ)

Includes (among others): S167, S168, S166, S350, S164, S361, S410, S163, S397, S362, S359, **S406**, S357, **S404**, S364, S365, S173, S210, S403, S356, S352, S174, S411, S398 — with the caveat that KEEP-only is an optimistic CLEAN lens and pipeline “Keep: 0” can still show Watch/Drop taxonomy separately.

---

## 5. Rainbow BTC/ETH research

### 5.1 Script & method

- **Script:** `scripts/crypto_rainbow_backtest.py`
- **Outputs:** `logs/research/rainbow_*`
  - `rainbow_btc_eth_summary.md`
  - `rainbow_btc_bands.csv` / `rainbow_eth_bands.csv`
  - `rainbow_btc_eth_equity.csv`
- **Model:** walk-forward OLS `log10(price) = a · ln(days_since_origin) + b`, nine parallel bands (log10 offsets −0.4…+0.4), fit through **prior close only** (~730-day warmup)
- **Costs:** 0.1% round-trip; full capital long-only
- **Origins:** BTC 2009-01-03; ETH 2015-08-07

### 5.2 Rules tested

| Rule | Entry | Exit |
|---|---|---|
| buy_hold | first valid day | end |
| deep_value | band ≤ 2 | band ≥ 8 |
| accumulate_distribute | band ≤ 3 | band ≥ 7 |
| center_fade | band < 6 | band ≥ 6 |

### 5.3 Result (generated 2026-10-16)

**Buy-and-hold crushed every band-timing rule** on terminal wealth for both assets.

| Asset | BH terminal | Best alternate | Now (as of report) |
|---|---:|---|---|
| BTC-USD | **133.86×** | deep_value 23.17× (−82.7% vs BH) | **Band 3 — Accumulate** (~$81.3k) |
| ETH-USD | **13.13×** | accumulate_distribute 7.08× (−46.1% vs BH) | **Band 3 — Accumulate** (~$2.43k) |

**Usefulness:** risk/regime dashboard, **not** an alpha engine. Do not build a live crypto timer from this without a new thesis.

### 5.4 Related exploratory research (local)

- `scripts/midcap_yoy_analysis.py` / `midcap_longterm_analysis.py`
- Outputs: `logs/research/midcap_*.json|csv` (cohort case studies; not production signals)

---

## 6. Myers Stock Investor — full section

### 6.1 Location & philosophy

- **Path:** `myers-stock-investor/` (standalone package; largely **untracked** vs git as of 2026-10-21)
- **Philosophy:** Evaluate equities as **ownership of a business**, not ticker speculation.
- **Live trading:** **DISABLED** (`config/strategy.yaml` → `live_trading_enabled: false`)
- **Model version:** `1.1.0`

### 6.2 Stack

| Piece | Tech |
|---|---|
| Prices | yfinance daily (as-of) |
| Fundamentals | yfinance statements/info — **NOT full PIT** |
| Optional SEC | `myers/data/sec_edgar.py` |
| Config | `config/strategy.yaml` + Pydantic |
| CLI | `python -m myers …` |
| UI | Streamlit `dashboard/app.py` (Overview / Screener / Company / Diagnostics / Backtest / Data Audit) |
| Tests | pytest — **14 tests collected** |

### 6.3 CLI commands

```text
analyze   — multi-ticker research JSON
backtest  — quarterly decisions, daily MTM vs SPY
compare   — profiles A–F under identical window
profiles  — list profile keys
version   — model + live flag + research_mode
```

### 6.4 Strategy profiles A–F

| Key | Letter | Rules (summary) |
|---|---|---|
| `conservative_acquirer` | A | Score≥70, MOS≥25% (default Myers-strict) |
| `balanced_value` | B | Score≥70, MOS≥15% |
| `quality_fair_value` | C | Score≥80, MOS≥0% |
| `deep_value` | D | Score≥60, MOS≥30% |
| `quality_value_ranking` | E | Soft floors score≥55 / MOS≥5%; ranking mode |
| `simple_reference` | F | Equal-weight deploy; no MOS filter (reference) |

### 6.5 ORIGINAL buggy backtest (v1.0 narrative — DO NOT TRUST)

Reported roughly:

| | Strategy | SPY |
|---|---:|---:|
| Cum | +18% | **+144%** |
| Max DD | −2.4% | −24.5% |
| Trades | 2 | — |

#### Bugs explained (confirmed; fixed in v1.1)

1. **SPY +144% inflation**  
   Metrics started at the **first quarter-end** (2020-03-31, post-COVID trough) instead of window start 2020-01-02. Measuring SPY from the trough → Dec 2024 ≈ +144%. True window buy-hold ≈ **+94.6%**.

2. **Strategy DD understated**  
   Equity recorded only at quarter-ends then **ffill** — no intra-quarter MTM → DD looked like −2.4%. Daily MTM → strategy DD ≈ **−3.3%** (still small due to cash), SPY DD ≈ **−33.7%**.

Internal inconsistency clue: SPY terminal ~$194,585 on $100k start is already ~+94.6%, not +144%.

### 6.6 CORRECTED audit run (conservative, 10 names, 2020–2024)

**Universe (smoke):**  
`AAPL,MSFT,COST,XOM,JNJ,CAT,UNH,PG,WMT,MRK`  
**Profile:** `conservative_acquirer`  
**Mode:** EXPLORATORY  
**Sources:** `outputs/backtest/summary.md`, `metrics.json`, `outputs/AUDIT_REPORT.md`

| Metric | Strategy | SPY (same calendar) |
|---|---:|---:|
| Start → end | $100,000 → $118,088 | $100,000 → $194,585 |
| Cumulative | **+18.1%** | **+94.6%** |
| CAGR | 3.4% | 14.3% |
| Max DD | **−3.3%** | **−33.7%** |
| Sharpe | 0.97 | 0.74 |
| Trades | **2** | — |
| Avg cash | **83.1%** | 0% |
| Avg invested | 16.9% | — |

**Trades (simulated):** 2020-03-31 BUY MRK ~$5,005; BUY AAPL ~$5,005; held (no sells through end).

### 6.7 Why only 2 trades

Not a broken ticket. On expensive mega-caps, **score≥70 + MOS≥25%** rarely clears.

- Dominant rejections: insufficient MOS, excessive valuation, low score  
- Closest near-miss often **MRK** with MOS ~15–20% (fails 25% gate)  
- Later BUY_CANDIDATE rows for held names skipped (`already_held`)  
- Result: **cash drag** → low volatility / high Sharpe optics / large underperformance vs SPY

### 6.8 Compare outputs (filesystem as of 2026-10-21)

`outputs/compare/comparison.md` contains **A, B, C, F only**:

| Profile | Cum | MaxDD | Trades | Avg Cash |
|---|---:|---:|---:|---:|
| conservative_acquirer | 18.1% | −3.3% | 2 | 83.1% |
| balanced_value | 18.1% | −3.3% | 2 | 83.1% |
| quality_fair_value | 0.0% | 0.0% | 0 | 100% |
| simple_reference | **83.1%** | −10.0% | 10 | 38.8% |
| SPY | **94.6%** | −33.7% | — | — |

**Missing on disk:** `outputs/compare/deep_value/` and `quality_value_ranking/` — full A–F compare was **not completed** (or interrupted / subsetted). Profiles exist in code (`myers/strategy/profiles.py`).

### 6.9 What was implemented in the upgrade

- Daily MTM backtest engine + cash/invested curves  
- Independent `spy_total_return_audit()`  
- Rejection diagnostics (`rejections.csv`, category tallies, closest-to-qualifying)  
- Reverse DCF fields on valuation  
- Profiles A–F + `myers compare`  
- Streamlit dashboard tabs  
- `research_mode: exploratory | validated` (validated refuses without PIT provider)  
- Tests: **14 collected** (audit, backtesting helpers, metrics, reverse DCF)  
- Docs: `outputs/AUDIT_REPORT.md`, refreshed `README.md`  
- Buy-count diagnostic fix in engine: `n_buy_candidate` counted from decision log `BUY_CANDIDATE` (rejection list alone undercounted buys). **Note:** older `outputs/backtest/metrics.json` may still show `n_buy_candidate: 0` until re-run; compare conservative summary shows `n_buy_candidate: 10`.

### 6.10 Incomplete / honesty checklist (filesystem)

| Item | Status (2026-10-21) |
|---|---|
| Daily MTM + SPY audit | **Done** |
| `outputs/AUDIT_REPORT.md` | **Present** |
| README refresh | **Present** |
| Buy-count diagnostic in code | **Fixed in engine.py** |
| Re-run backtest outputs after fix | **May be stale** — re-run to refresh `outputs/backtest/*` |
| Full A–F compare dirs | **Incomplete** (D & E missing) |
| PIT / validated mode usable | **Not available** (no PIT vendor wired) |
| Live trading | **Disabled** |
| Package committed to GitHub | **Typically untracked locally** — confirm before assuming remote has Myers |

### 6.11 Exploratory vs validated + bias disclosure

Every Myers report should carry:

> EXPLORATORY MODE: prices are point-in-time; yfinance fundamentals are NOT filing-date accurate and may look ahead. Universe is a modern survivor list (survivorship bias). Results are experimental, not validated historical performance. Live trading disabled.

**Do not treat exploratory Myers results as validated alpha.**

### 6.12 Package layout (high level)

```
myers-stock-investor/
  config/strategy.yaml
  dashboard/app.py
  myers/
    analysis/metrics.py
    backtesting/{engine,performance}.py
    data/{fundamentals,market,sec_edgar}.py
    intelligence/thesis.py          # optional LLM stub
    portfolio/paper.py
    strategy/{engine,scoring,signals,eligibility,diagnostics,profiles}.py
    valuation/engine.py
    cli.py
  outputs/{backtest,compare,AUDIT_REPORT.md,sample_report.json}
  tests/
  requirements.txt
  README.md
```

---

## 7. Failures / lessons / open risks

| Area | Lesson / risk |
|---|---|
| **Silent scanners** | Many paper strategies sit at n=0 for weeks/months — signal too rare or broken for daily bars |
| **Orphan stacking / attribution** | Orphan rate >10% pollutes strategy P&L; fix tagging before trusting rankings |
| **TAINTED days** | Outages/reconciles create fake “strategy” losses — always prefer CLEAN |
| **Fat left tails** | S404/S406 green medians with p10 ~−60% — not Stage-3 ready |
| **Live options** | Entries paused; reopening without twin edge is reckless |
| **S218** | Was twin/live candidate; became CLEAN-KILL — removed from live allow/mirror |
| **Historical BS backtests** | Useful for ranking hypotheses only — not fill truth |
| **Rainbow timing** | No edge vs buy-hold in walk-forward test |
| **Myers cash drag** | Strict MOS on mega-caps ≈ T-bill proxy with tiny equity sleeve; loses to SPY |
| **Myers metric bugs** | Wrong SPY window + quarterly ffill nearly published false +144% / −2.4% DD story |
| **PIT data gap** | Cannot claim validated historical fundamentals performance on yfinance |
| **Survivorship** | Modern mega-cap list biases long-only quality tests |
| **Interrupted compare** | D/E profiles not in `outputs/compare/` |
| **Local behind remote** | 300+ bot commits — always check `origin/main` for latest paper reports |
| **Dual-path confusion** | Desktop junction vs Documents — same repo, don’t clone twice and diverge |
| **Mixing systems** | Wiring Myers into options GHA would corrupt both missions |

---

## 8. How to run (copy-paste)

### 8.1 TradingBot — paper cohort flags (local dry conceptual)

Typical paper env (matches GHA intent):

```bash
# From repo root (Documents or Desktop junction)
export OPTIONS_PAPER_UNLIMITED=1
export OPTIONS_MIRROR_LIVE=1
export OPTIONS_VARIATION_STUDY=1
export OPTIONS_CONTROLLED_LAYOUT=1
export OPTIONS_PROMISING_COHORT=1
export OPTIONS_PROMISING_MIN=75
export OPTIONS_ONE_BUCKET_PER_STRATEGY=1
export OPTIONS_MIRROR_STRATEGIES=S404,S406
export OPTIONS_BLOCK_SHARED_OCC=1
export OPTIONS_BLOCK_KILL_STRATEGIES=1
export OPTIONS_BUCKET_COUNT=1800
export OPTIONS_MAX_NEW_ENTRIES_PER_RUN=200
# Requires ALPACA_PAPER_KEY / ALPACA_PAPER_SECRET
python scripts/options_morning_bot.py
```

PowerShell equivalents use `$env:OPTIONS_PROMISING_COHORT="1"` etc.

Live micro (entries paused — do not flip without approval):

```bash
export LIVE_OPTIONS_ENTRIES=0
export LIVE_OPTIONS_MAX_CAP=250
export LIVE_STOCK_CASH_RESERVE=250
export LIVE_OPTIONS_ALLOW=S404,S406
export LIVE_OPTIONS_MIN_COST=20
python scripts/options_live_micro.py
```

Reports (after ledgers exist):

```bash
python scripts/options_strategy_lab.py --evaluate
# plus selection / data-quality / bucket report scripts used in GHA
```

Sync newest bot artifacts:

```bash
git fetch origin
git log HEAD..origin/main --oneline | head
# Prefer reading: git show origin/main:logs/options_trial/reports/YYYY-MM-DD_strategy_selection.md
```

### 8.2 Myers

```bash
cd myers-stock-investor
python -m pip install -r requirements.txt
python -m pytest tests -q

python -m myers analyze AAPL MSFT --out outputs/sample_report.json

python -m myers backtest \
  --start 2020-01-01 --end 2024-12-31 \
  --universe AAPL,MSFT,COST,XOM,JNJ,CAT,UNH,PG,WMT,MRK \
  --profile conservative_acquirer \
  --out outputs/backtest

python -m myers compare \
  --start 2020-01-01 --end 2024-12-31 \
  --universe AAPL,MSFT,COST,XOM,JNJ,CAT,UNH,PG,WMT,MRK \
  --profiles conservative_acquirer,balanced_value,quality_fair_value,deep_value,quality_value_ranking,simple_reference \
  --out outputs/compare

python -m myers profiles
streamlit run dashboard/app.py
```

### 8.3 Rainbow research

```bash
# From repo root
python scripts/crypto_rainbow_backtest.py
# Reads: logs/research/rainbow_btc_eth_summary.md
```

---

## 9. Key decisions / do-nots

1. **Do not enable live options entries** (`LIVE_OPTIONS_ENTRIES=1`) without: twin paper confirmation, left-tail review (p10), and explicit human (Tyler) approval.  
2. **Do not merge Myers into the options bot** (no shared ledgers, keys, or workflow jobs).  
3. **Do not treat exploratory Myers as validated alpha** or market-beating proof.  
4. **Day trader buckets stay additive** — never gut KEEP/twins to free slots.  
5. **Do not optimize toward the +16,719% BS chart.**  
6. **Prefer CLEAN / KEEP-only lenses** over ALL for promotion; treat orphans as infrastructure debt.  
7. **S218 stays off live allow** unless CLEAN status reverses with adequate sample.  
8. **Rainbow band timing is not a trade engine** given current results.  
9. **When local is behind origin**, don’t conclude paper “stopped” — check remote reports.  
10. **Cash earns 0% in Myers default** — don’t confuse high Sharpe + cash pile with alpha.

---

## 10. Suggested next steps for the next agent

### Priority A — Myers (continue 1→6 style backlog)

| Pri | Work | Why |
|---|---|---|
| **1** | Re-run `myers backtest` after buy-count fix; confirm `n_buy_candidate` ≈ 10 and docs match | Stale outputs can confuse audits |
| **2** | Finish **full A–F compare** (add `deep_value`, `quality_value_ranking` to `outputs/compare/`) | Incomplete experimental matrix |
| **3** | Expand universe beyond mega-caps (mid-cap cash compounders; reuse midcap research ideas carefully) | Strict MOS never fires on expensive leaders |
| **4** | Design/wire **PIT fundamentals** path → real `validated` mode | Without PIT, no production claim |
| **5** | Cyclical earnings normalization + peer EV/EBITDA bands | Reduce DCF MOS false negatives/positives |
| **6** | Optional SEC major-customer / key-person extraction; decide whether to **commit** Myers tree to git | Completeness + reproducibility |

Also keep `outputs/AUDIT_REPORT.md` and README consistent with any new numbers.

### Priority B — TradingBot paper monitoring

1. `git fetch` and read latest `logs/options_trial/reports/*_strategy_selection.md` + `*_data_quality.md` (esp. post–2026-10-20).  
2. Track **S430 / S431 / S432** until n≥15–30 before any KEEP/KILL call.  
3. Watch **orphan rate** — still >10%; attribution work before trusting $ rankings.  
4. Re-evaluate **S404/S406** left tails (p10) vs escalation protocol before any live entry discussion.  
5. Keep live **ENTRIES=0** and **$250** firewall unless human overrides.  
6. Do not add large new strategy grids until silent/broken scanners are understood.

### Priority C — Research hygiene

1. Treat rainbow as closed negative result unless new methodology.  
2. Midcap scripts are exploratory case studies — not wired to live.  
3. If committing handoff/docs: `docs/` is traditionally local-ish — confirm with user before pushing secrets or large ledgers.

---

## 11. Quick file index for the next chat

| Need | Path |
|---|---|
| This handoff | `docs/HANDOFF_TRANSFER.md` |
| Options signals + DayTrader | `scripts/options_signals.py` |
| Paper lab / cohort / twins | `scripts/options_lab.py` |
| Morning bot | `scripts/options_morning_bot.py` |
| Live micro | `scripts/options_live_micro.py` |
| GHA | `.github/workflows/run_bot.yml` |
| Oct 15 DQ (local) | `logs/options_trial/reports/2026-10-15_data_quality.md` |
| Oct 20 reports | `origin/main:logs/options_trial/reports/2026-10-20_*` |
| Rainbow summary | `logs/research/rainbow_btc_eth_summary.md` |
| Myers audit | `myers-stock-investor/outputs/AUDIT_REPORT.md` |
| Myers corrected backtest | `myers-stock-investor/outputs/backtest/summary.md` |
| Myers compare | `myers-stock-investor/outputs/compare/comparison.md` |
| Older options transfer | `docs/CLAUDE_TRANSFER_2026-07-26.txt` |
| Escalation stages | `docs/ESCALATION_PROTOCOL.md` |

---

## 12. One-paragraph brief for the next model

You are inheriting a dual-track repo: (1) an Alpaca **options paper laboratory** with paused **$250 live micro** entries, promising-cohort paper (≥75 unique, one bucket each), S404/S406 twins, and new additive DayTrader arms S430–S432 that still lack sample; KEEP-only paper looks ~+$12.8k / ~61% / ~+51% med but the full book and orphans dilute trust, and twins are not live-ready due to fat left tails; (2) a separate **Myers Stock Investor** spin-off that thinks like a business acquirer, with a **fixed** backtest engine after SPY-window and quarterly-ffill bugs, showing conservative ~+18% vs SPY ~+94.6% (2020–2024) on 2 trades / ~83% cash — exploratory only, not PIT-validated. Rainbow BTC/ETH band timing lost to buy-hold. Local `main` is often hundreds of commits behind `origin/main` because of bot-run commits. Do not mix systems, do not enable live options entries casually, and continue Myers universe/PIT/compare work while monitoring paper DayTrader + twin tails.

---

*End of HANDOFF_TRANSFER.md — generated 2026-10-21 from filesystem + git inspection.*
