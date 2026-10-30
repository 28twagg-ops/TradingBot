# TradingBot / Arena — Comprehensive Chat Transfer & Engineering Handoff

**Last verified:** 2026-10-30, based on the current GitHub `main` branch and `arena-ledger` records (ledger latest research timestamp checked: **2026-10-30 19:28 UTC**).  
**Primary repo:** [28twagg-ops/TradingBot](https://github.com/28twagg-ops/TradingBot)  
**Status:** Arena research workflows are deployed, actively running at scheduled opportunities, and still experimental. **No profitable AI strategy has been independently validated.**  
**Audience:** A new ChatGPT/Codex/engineering session taking over the project without the previous conversation.

> **Read this document first.** This is a transfer of the owner's goals, the verified repository layout and operational state, plus a prioritized work plan. It is not an instruction to turn on real-money trading, increase API spending, or treat research output as financial advice. Recheck live GitHub state before changing anything.

## 0. Exactly what the owner wants — the most important part

Build a self-directed **TradingBot Arena** where **ten independent AI research agents (S01–S10)** tirelessly investigate *any* trading ideas they want, and **three independent reviewers (J01–J03)** scrutinize evidence and accounting. Each starts with **$100 of separate, fictional virtual capital**. These are *not* ten copies of the same canned strategy.

The owner has repeated these requirements emphatically:

1. **True scientific autonomy.** Each bot chooses its own market, hypothesis, source, research direction, test and later revisions. No imposed split such as “three crypto, three stocks, two options.” If all independently decide crypto offers the most promising hypotheses, that is fine, provided they have evidence rather than just convenient data access.
2. **Source freedom.** A bot can look at a research paper, an obscure five-year-old strategy blog, Reddit, TikTok, YouTube, GitHub, public forums, social media or independent ideas. **Do not prohibit an idea based on perceived prestige of the source.** Provenance and trustworthiness matter when evaluating *claims*, not when determining whether an idea is allowed to be investigated. A dubious source is a research lead, not an instruction or trading authorization.
3. **Evidence before simulated risk.** Translate ideas into executable rules; obtain suitable historical data; verify no lookahead, survivorship/selection leakage or fabricated price/fill data; backtest with transaction fees/slippage and meaningful sample sizes; test a genuinely later validation period; only *then* allow a candidate to forward paper trade. A hypothesis unsupported by the current data/engine should remain in a research queue rather than receive a fake backtest or an unjustified virtual buy.
4. **Use available free hosted inference efficiently and fairly.** Research should run unattended, including overnight. Spread requests across the day instead of burning the allowance in bursts. **Agents that missed research because of rate limiting, API errors, invalid outputs or scheduler gaps should get priority when capacity returns.** Aim to use available free quota responsibly, observing actual provider request/token limits and backoff. The user does *not* want tedious manual GitHub steps.
5. **Keep researchers independent.** Ten separate accounts, histories, hypotheses, and future searches. A lightweight scheduler can allocate capacity; it must not act as a central research director that dictates markets/strategies.
6. **Use Gemini sparingly** for special or weekly high-value reviews; Groq's free tier is the everyday inference worker. No automatic paid-provider fallback, no new paid API spending, and **a ChatGPT Plus subscription is not an OpenAI API quota**.
7. **Production live trading is out of scope.** Do **not** alter, route orders from, disable or promote strategies into the existing live stock/options bots as part of Arena work. All Arena purchases/sales remain fictional ledger events. Separate explicit owner approval and professionally validated safeguards are required for any real trading deployment.
8. **Don't confuse “AI generated an idea” with “AI tested it” or “AI made money.”** Report operation health, accepted ideas, backtest outcomes, paper portfolio performance and real-money performance *separately*.

**North-star behavior:** Discover any idea → inspect source and counterevidence → state exact falsifiable trade rules → obtain correct historical data → run a credible historical test → pass holdout/robustness gates → begin **virtual-only** forward paper tracking → revisit hypothesis based on accumulating evidence → request independent review. Bots retain freedom to change course.

## 1. Orientation and actual current state

**Default branch:** `main`.  
**Persistent virtual-account state branch:** `arena-ledger`.  
**Developer branch history:** older feature/fix branches remain visible even when their PRs were merged; do not infer that a branch is active work just because it exists.

### Latest snapshot (verified 2026-10-30)

Read [the raw research records](https://github.com/28twagg-ops/TradingBot/blob/arena-ledger/records/arena/groq_research.json) before quoting today's statistics.

- `records/arena/groq_research.json` had **193 recorded Groq events**, broken into **70 `RESEARCHED`**, **58 `RESEARCH_IDEA_NEEDS_DATA`**, **40 `AI_UNAVAILABLE`** and **25 `REJECTED_INVALID_MODEL_EXPERIMENT`**. These are status categories, not 70 verified profitable strategies.
- All ten agents have participated; the individual `groq_experiments` arrays currently range from about **7** (S07) to **15** (S06). Uneven results and repeated hypotheses remain issues.
- The last saved research events observed were at **2026-10-30 19:28 UTC**. Several recent `GROQ_HTTP_400_unknown` provider errors and invalid experiments occurred; successful jobs are not evidence that every inference succeeded.
- `records/arena/groq_quota.json` exposed a local cap of **72 requests/day**, plus a provider header snapshot showing **991 remaining out of 1000 daily requests** and **5440 remaining out of 8000 minute tokens** at **2026-10-30 19:28 UTC**. This is a historical provider-header snapshot, *not* guaranteed current entitlement or permission to increase spending. Check Groq's exact live free-plan quotas, which can vary by model/organization/TPD, before raising throughput. Its `pending_worker_priority` was `[]` at this snapshot; verify why (all workers can be within their 40-minute spacing gate).
- `records/arena/ai_state.json` is the **separate AI researcher account ledger**. At that snapshot S04 had fictional cash **$80.17328667** with **0.000249 BTC/USD**; S06 had fictional cash **$90.07922002** with **0.098527 SOL/USD**; the other eight were at **$100 cash** without positions. These are historical close-proxy virtual trades, **not independently marked-to-market brokerage performance**.
- `records/arena/DASHBOARD.md` is the **separate rule-based virtual competition**, updated **2026-10-30 19:26 UTC**. Its S04 was ~$100.60, S03 ~$98.19, S09 ~$97.39, etc. **Do not attribute those profits or losses to the Groq AI agents**. Each of the ten rule-based accounts also started with $100.
- No independently proven positive, realistic, reproducible out-of-sample trading edge has been identified. Historical validation trades that occurred during earlier snapshots were negative. “0 trades, 0% return” is not an economically successful backtest.
- The first Gemini ten-worker/three-reviewer research report was from Oct 26; J01/J02 rejected unsupported profitability claims, J03 was quota-limited. **No** `records/arena/gemini_special.json` existed at the most recent inspection, so do not claim that the weekly specialist cycle has successfully run.

### Direct status links

- [Arena rule-based dashboard](https://github.com/28twagg-ops/TradingBot/blob/arena-ledger/records/arena/DASHBOARD.md)
- [Groq research summary](https://github.com/28twagg-ops/TradingBot/blob/arena-ledger/records/arena/GROQ_RESEARCH.md)
- [Groq structured research history](https://github.com/28twagg-ops/TradingBot/blob/arena-ledger/records/arena/groq_research.json)
- [Groq quota state](https://github.com/28twagg-ops/TradingBot/blob/arena-ledger/records/arena/groq_quota.json)
- [AI account ledger](https://github.com/28twagg-ops/TradingBot/blob/arena-ledger/records/arena/ai_state.json)
- [Rule-based account ledger](https://github.com/28twagg-ops/TradingBot/blob/arena-ledger/records/arena/state.json)
- [Original Gemini review](https://github.com/28twagg-ops/TradingBot/blob/arena-ledger/records/arena/AI_COUNCIL.md)
- [GitHub Actions history](https://github.com/28twagg-ops/TradingBot/actions)

## 2. Repository map: exact current paths

The repository is large (tens of thousands of stored data/research files) and contains multiple older live/options projects. **Do not move, rewrite or clean up that historical content while working on Arena.** The key paths:

```text
TradingBot/
├── README.md                          # Repository homepage; links to this handoff
├── .github/
│   └── workflows/
│       ├── groq-research.yml          # Routine hourly free Groq research and ledger push
│       ├── arena-paper.yml            # Every-2h RULE-BASED virtual sim, research fallback, Sunday Gemini
│       ├── arena-ai-ci.yml            # Isolated Arena unit tests on PRs
│       ├── run_bot.yml                # EXISTING live stock + live options workflow; DO NOT ALTER
│       ├── options_morning_bot.yml    # Separate PAPER options workflow
│       ├── options_collector.yml      # Older options data collection
│       └── first_hour_collector.yml   # Older data collection
├── research/
│   └── trading-arena/
│       ├── README.md                  # Long historical design narrative; portions are STALE
│       ├── config.json                # S01–S10; J01–J03; virtual risk caps
│       ├── arena.py                   # PaperAccount ledger, accounting, council hard checks
│       ├── run_virtual.py             # Distinct zero-AI RULE-BASED 10-account simulator
│       ├── groq_research.py           # LLM schema, hypotheses, simplified backtesting, AI virtual turns
│       ├── quota_scheduler.py         # UTC pace, fairness, cooldown, provider header decoding
│       ├── open_research.py           # Public search-index snippets/repo metadata
│       ├── research_sources.py        # Labeled context from selected historical repo files
│       ├── groq_probe.py              # Groq model-access probe
│       ├── gemini_cycle.py            # Initial Gemini independent-worker cycle + J01-J03
│       ├── gemini_special.py          # Scheduled weekly special reviewer (verify actual output)
│       ├── council_ai.py              # Additional advisory council implementation
│       └── tests/
│           ├── test_arena.py
│           ├── test_virtual.py
│           ├── test_groq_research.py
│           ├── test_quota_scheduler.py
│           ├── test_open_research.py
│           ├── test_gemini_cycle.py
│           └── test_gemini_special.py
├── docs/
│   ├── ARENA_PROJECT_HANDOFF.md       # THIS FILE
│   ├── ESCALATION_PROTOCOL.md         # Earlier options research; historical/not live authorization
│   └── CLAUDE_TRANSFER_2026-07-26.txt # Older independent project handoff
├── rubber_band_bot.py                 # EXISTING real-money stock bot, not Arena
├── scripts/
│   ├── options_morning_bot.py         # EXISTING paper options logic, not Arena
│   ├── options_live_micro.py          # EXISTING live options logic, not Arena
│   ├── options_strategy_lab.py        # Historic options paper research, not a clean holdout
│   ├── historical_data_fetcher.py     # Other historical data infrastructure
│   ├── options_data_collector.py
│   └── [many other helpers]
├── simulations/
│   ├── historical_backtest.py
│   ├── options_strategy_simulator.py
│   ├── options_robustness_tests.py
│   └── results/                     # Historic outputs; inspect quality/taint before reuse
├── data/                              # Historic equity parquet and other data
└── logs/                              # Existing operational/live/options logs
```

### Persistent ledger branch (NOT the default branch's source files)

```text
arena-ledger:
└── records/
    └── arena/
        ├── ai_state.json             # 10 AI virtual accounts; histories/positions
        ├── groq_research.json        # Groq research event feed
        ├── groq_quota.json           # Provider quota/cooldown/fairness metadata
        ├── GROQ_RESEARCH.md          # Human-readable Groq event table
        ├── state.json                # Separate rule-based account positions
        ├── DASHBOARD.md              # Separate rule-based scoreboard
        ├── ai_report.json            # Initial Gemini proposals and council
        ├── AI_COUNCIL.md             # Initial Gemini council text report
        └── [additional reports/artifacts, if created by subsequent runs]
```

**Critical:** `main` contains production code and workflows. `arena-ledger` contains persistent research evidence. Checking `main/records/arena/` instead of `arena-ledger/records/arena/` can yield missing or misleading data.

## 3. How the current Arena works

### 3.1 Worker identities and reviewers

From `research/trading-arena/config.json`:

| Worker | Original starting specialty (NOT a binding assignment) |
|---|---|
| S01 | Intraday VWAP/noise |
| S02 | Long-only noise |
| S03 | Mean reversion |
| S04 | Gap-down quality |
| S05 | Opening-range breakout |
| S06 | Relative strength |
| S07 | Trend-following |
| S08 | Volatility compression |
| S09 | BTC/ETH trend |
| S10 | Long-option risk-defined theory |

The ten names represent ten independent memory and virtual account identities. **None should be restricted to its original specialty.** J01 = accounting; J02 = evidence/methodology; J03 = risk. The initial Gemini reviews are advisory; no council can override a hard integrity failure or authorize a production trade.

`config.json` sets initial virtual balance `$100`, no margin, no shorting, no naked options, and no automatic real-money promotion. Its paper account class can represent long options for accounting, but **options pricing/historical chain evaluation and autonomous options paper execution are not implemented here**.

### 3.2 Two separate mechanisms, intentionally not the same

**A. RULE-BASED virtual simulator (separate from the AI):**

- `run_virtual.py` uses Yahoo Finance via `yfinance` to request up to roughly 30 days of **hourly historical price bars** for `SPY, QQQ, AAPL, MSFT, BTC-USD, ETH-USD, SOL-USD`; drops incomplete/unusable bars.
- It has ten deterministic signal paths using indicator/price thresholds indexed by worker ID, records hash-chained virtual buys/sells with fees and indicative close prices.
- Writes `state.json` and `DASHBOARD.md`. These are not genuine independently validated tradable fills or the PnL of LLM proposals.

**B. AI-driven virtual research:**

- `groq_research.py` calls Groq's `openai/gpt-oss-20b` using a JSON-schema response. Model text is never executed as Python.
- Each agent receives its own recent research history, available eligible symbols and selected public source-search snippets, then proposes a hypothesis, data requirements, test/falsification design, a possible bounded rule and the sources/next search direction.
- `open_research.py` performs bounded queries of **Bing RSS-style public search metadata** for public web/social platforms and GitHub repository search metadata. The bot can request web, Reddit, YouTube, TikTok, academic, forum or blog sources and a specific domain. **This does not actually watch TikTok/YouTube videos, read entire articles, sign into social accounts, access paid sites or execute someone else's GitHub code.** Citations should describe what was retrieved, not overclaim.
- The only executable built-in deterministic historical rule families currently are `trend`, `reversion`, `breakout` and `momentum`, normally with lookback 5–80 and threshold 0–0.12. They are evaluated from **single-asset hourly closes**, with 25-basis-point fees each way and next-hour-close entry approximations. A 5-minute order-book theory is *not* actually tested by an hourly close-only breakout.
- Agent declares timeframe, data requirements and whether it believes its idea matches the bounded DSL. An extra heuristic rejects certain claims requiring unavailable inputs (VWAP, order book, cross-asset relationships, options, minute bars, etc.). Ideas that cannot be properly tested get `RESEARCH_IDEA_NEEDS_DATA` and `RESEARCH_ONLY_NEEDS_DATA` instead of fictitious backtest results.
- Paper buys for supported rules require historical activity and positive retrospective validation results plus a current entry signal; this remains **far short of proof of market edge**. Earlier historical S04 BTC virtual entry occurred before the stricter guard and should be treated as legacy experimental evidence, not proof.
- These AI results are stored independently in `ai_state.json` and `groq_research.json`. A paper-only trade is represented with Yahoo close proxies; **no Alpaca brokerage paper order is placed**.

### 3.3 Per-agent research memory

An AI experiment can store:

```json
{
  "cycle": "UTC timestamp",
  "topic": "free-form idea",
  "hypothesis": "falsifiable idea",
  "candidate": {"family":"...", "lookback":20, "threshold":0.01},
  "symbol": "studied symbol or null",
  "test": {"status":"HISTORICAL_PROXY_ONLY or PENDING_PROPER_HISTORICAL_DATA"},
  "paper_action": "HOLD or research-only/other safe result",
  "falsification_test": "what could refute the claim",
  "source_search": {"query":"...", "attempted":["..."], "matches":4},
  "source_leads": [],
  "next_search_query": "bot-chosen follow-up question",
  "preferred_sources": ["web","reddit","github"],
  "site_domain": null,
  "research_data_requirements": ["hourly_close"],
  "hypothesis_timeframe": "hourly",
  "rule_expressible_as_candidate": false
}
```

The model output is not always valid. Some logs have `source_search.matches > 0` but `source_leads: []` because the agent selected no source indices. That is a provenance weakness: it did not demonstrate that a source was actually used. An idea may still be original; do not invent citations.

## 4. Automation and free API quota — deployed, but needs tuning

### 4.1 Current GitHub Actions design

**Routine Groq:** [`.github/workflows/groq-research.yml`](../.github/workflows/groq-research.yml)

- Triggers `workflow_dispatch`, relevant code changes on `main`, and UTC cron **`13 * * * *`** (hourly at :13), plus backup **`43 3,7,11 * * *`**.
- Tests source, sets up Python, installs public-data packages if the Groq secret exists, checks out the Arena source separate from ledger state, and runs `groq_research.py --dir ledger/records/arena --batch 5`.
- Writes *only research evidence* into `arena-ledger`, using a shared concurrency group.
- Model access probe runs only on manual dispatch; a successful workflow can still contain `AI_UNAVAILABLE`/`REJECTED_INVALID_MODEL_EXPERIMENT` events.

**Baseline + fallback:** [`.github/workflows/arena-paper.yml`](../.github/workflows/arena-paper.yml)

- Cron **`17 */2 * * *`** every two hours UTC; Sunday specialist **`17 19 * * 0`**; manual dispatch available.
- Runs Arena tests, updates all ten **rule-based** virtual accounts, invokes the same Groq research scheduler if time-paced credit remains, runs Sunday Gemini specialist when eligible, and pushes updates to `arena-ledger`.
- Both workflows share `concurrency.group: paper-arena-ledger-writes` with `cancel-in-progress: false` to reduce branch-write races. Verify actual push and persisted records rather than trusting a green check alone. GitHub cron is best-effort, may skip or delay executions.

**CI:** [`.github/workflows/arena-ai-ci.yml`](../.github/workflows/arena-ai-ci.yml) runs Python unit tests on Arena PRs, not real-provider account integration tests.

### 4.2 Current quota implementation

See `research/trading-arena/quota_scheduler.py` and `groq_research.py`:

- `DAILY_REQUEST_TARGET = 72` = **local** ceiling, not Groq entitlement.
- `MAX_BATCH = 5`; `MIN_INTERVAL_MINUTES = 40` per worker.
- `remaining_time_paced_credit(...)` releases quota progressively across the UTC day, allowing backlog catch-up if GitHub misses schedules.
- `eligible_worker_order(...)` sorts workers by **fewest successful research sessions today**, then attempts and historical successful work, then recency. An API failure is not a successful turn; `RESEARCH_IDEA_NEEDS_DATA` *is* treated as an accepted research session even though it is not a successful historical test.
- `read_provider_headers(...)` attempts to read sanitized numerical request/day and token/minute limits/remaining values and reset windows. `cooldown_deadline(...)` respects 403/429 / Retry-After / daily-reset signals; `spacing_seconds(...)` enforces at least ~40 seconds between requests, extending under token pressure.
- The state is persisted in `groq_quota.json`. Legacy 429 requests are conservatively counted toward local API usage even if incorrectly marked `ai_requests=0`.
- Free access is *not unlimited*. The user wants efficient utilization of **actual available free quotas**, not artificial under-use. Do not blindly replace 72 with 1000 because provider limits may differ by model, tokens/day, request/min, concurrency or billing status. Start by measuring actual live 429/400 patterns and quota reset behavior. No new paid billing/fallback.

### 4.3 Most recent quota observations

Last saved quota snapshot listed **1000/day provider request limit** and **8000/min token limit**, despite the local 72/day ceiling. This suggests significant unused reported RPD capacity, but the system also had repeated `GROQ_HTTP_400_unknown` and `REJECTED_INVALID_MODEL_EXPERIMENT` failures. The next engineer should investigate **why** those model failures occur (structured schema, prompt truncation, content/validation, provider mode), not simply increase inference volume.

**Urgent fairness concern:** At the snapshot, S07 has around 7 accepted experiment records versus S06's ~15. Compare accepted research, *valid historical tests* and actual inference attempts separately. Worker credit should be fair without privileging repeated untestable ideas over genuine completed experiments.

### 4.4 GitHub secret names — names only, never values

- `GROQ_API_KEY`: routine AI research, currently used by both relevant Arena workflows.
- `Gemini_API_Key`: referenced by Sunday reviewer workflow (case-sensitive name as currently written); initial Gemini tooling uses `GEMINI_API_KEY` as an environment variable.
- Production and older paper-options workflows have distinct Alpaca secrets. **Do not copy/expose/passthrough those credentials to Arena.** Never paste API tokens, private account IDs, personal details or secret values into this public documentation.

## 5. Safety boundaries and how to avoid confusing performance

**Three independent ledgers/concerns:**

| Purpose | Location | What it proves |
|---|---|---|
| Rule-based Arena virtual portfolios | `arena-ledger:records/arena/state.json` and `DASHBOARD.md` | Deterministic indicator-rule simulated holdings, not LLM strategy success |
| AI researcher virtual portfolios and experiments | `arena-ledger:records/arena/ai_state.json` + `groq_research.json` | AI hypotheses, proxy backtests and occasional fictional buys, not brokerage fills |
| Existing real-money stock / options / historical research | Production root code, `logs/`, `data/`, `scripts/` and other workflows | Separate operational systems. **Never use these as Arena performance or permissions** |

There is *no* automatic switch that promotes a winning Arena researcher into real-money orders. The earlier `docs/ESCALATION_PROTOCOL.md` belongs to historical options development, not a grant of live trading permissions.

**Minimum appropriate evidence standard before a bot may begin forward virtual paper tracking:** exact executable rule and data requirements; sufficient clean historical sample; chronological training/validation windows; fees/slippage and corporate-action effects where applicable; no lookahead/data leakage; plausible signal frequency; multiple market regimes; sensible benchmark comparisons; worst drawdown and tail losses; repeated family testing adjustments; reproducible results. Only later can it request independent judges' audits.

**Never claim:** “profitable strategy” just because a virtual balance is above $100, a Google/GitHub Actions job passed, model output contains an impressive claim, a public article says it works, or a zero-trade backtest reports 0% losses.

## 6. Major completed PR milestones and what is still incomplete

The current `main` incorporates the following **merged** pull requests:

- [#2 — basic isolated Arena foundation](https://github.com/28twagg-ops/TradingBot/pull/2), merged Oct 25.
- [#4 — 10 independent Gemini researchers + 3 reviewers](https://github.com/28twagg-ops/TradingBot/pull/4), merged Oct 26.
- [#5 — rotating Groq inference and Sunday Gemini special](https://github.com/28twagg-ops/TradingBot/pull/5), merged Oct 26.
- [#6 — five-agent batches and overnight scheduling fallback](https://github.com/28twagg-ops/TradingBot/pull/6), merged Oct 26.
- [#7 — public-source discovery and proper-data gate for open-ended research](https://github.com/28twagg-ops/TradingBot/pull/7), merged Oct 27.
- [#8 — fair quota/priority and response-header pacing](https://github.com/28twagg-ops/TradingBot/pull/8), merged Oct 28.
- [#9 — additional fair scheduling/quota PR](https://github.com/28twagg-ops/TradingBot/pull/9), merged Oct 29.

**Important correction for the new chat:** Earlier conversations may describe the quota scheduler as “unfinished, on an unmerged branch.” That information is obsolete. **PR #8 and #9 are both merged into `main`**, as verified Oct 30.

**Other open PRs must not be casually merged into Arena:**

- [#1 — whole-repo reorganization](https://github.com/28twagg-ops/TradingBot/pull/1), open; broad structural changes.
- [#3 — live safety/strategy-research fixes](https://github.com/28twagg-ops/TradingBot/pull/3), open; touches separate production concerns.

### Existing documentation caveat

`research/trading-arena/README.md` is a chronologically appended design history and contains introductory text such as **“development branch only / not deployed.”** That introductory claim is stale: Arena workflows *are* merged and scheduled. Use **this newly dated handoff** and actual workflow/ledger state for operational truth; do not erase historical records without a reason.

## 7. Known technical limitations, bugs and unresolved design problems

1. **Research freedom is broader than execution freedom.** The agents can choose topics/sources, but only an hourly single-asset four-family DSL is backtestable. Most interesting multi-asset, volume, options, news and sub-hour hypotheses remain queued. This creates repetitive “Bitcoin breakout” output and excessive `RESEARCH_IDEA_NEEDS_DATA`.
2. **Source discovery is metadata, not reading.** TikTok, YouTube and Reddit queries produce public index snippets if available; there is no credible full-video transcript pipeline or per-page verification. Search matches with zero selected leads are often not useful source evidence.
3. **Historical data is shallow for the AI path.** `run_virtual.market` loads about 30 days of hourly Yahoo closes for seven symbols, whereas the large `data/historical/stocks/` collection is a separate older archive, mainly daily OHLC data. Do not claim 12-month historical backtests from the 30-day hourly feed.
4. **No true flexible strategy executor.** Models cannot yet express multi-asset decisions, stop/exit policies, position sizing, minutes/options in an audited intermediate language; avoid running arbitrary model-generated Python or cloned repository code with secrets.
5. **Provider failures may be overrepresented.** `GROQ_HTTP_400_unknown` and invalid structured outputs increased by Oct 30. Diagnose provider/schema compatibility, max tokens, output parsing, field constraint mismatch, prompt length, and response handling with sanitized logs and tests. Do not log full credentials or potentially sensitive raw provider responses.
6. **Quota under-utilization vs safety.** Provider headers show a much higher nominal request/day cap than the local 72, but real token/request throttles and failure rates matter. Build a dynamic conservative budget optimizer, measure actual successful inference throughput and whether the scheduler is still prematurely idle.
7. **Unfair research throughput.** Some workers have far more retained experiments than others, and repeated invalid/unsupported ideas are not the same as validated progress. Fairness should consider last *actual successful research turn*, useful work/accepted result, and recent attempts. Guarantee no starvation without repeatedly paying for broken proposals.
8. **GitHub schedule is unreliable.** GitHub Actions cron can miss or delay; preserve sufficient catch-up state. Test actual persistence and concurrency against the `arena-ledger` branch after every scheduler change.
9. **Judge coverage incomplete.** Verify Sunday Gemini specialist saved report, current config/model validity, quota and whether J01/J02/J03 truly independently audit actual experimental evidence.
10. **Quote-close virtual fills are not genuine execution evidence.** Include stale/missing data, market hours, spreads/slippage, partial fills and transaction fees for credible simulations.
11. **No independent long-term forward trial yet.** Never equate reusing the same 30-day rolling price history for multiple studies with a clean, previously unseen holdout.
12. **Rule-based vs AI dashboards remain easy to confuse.** A unified dashboard should show two explicitly labeled cohorts and separate performance/provenance metrics.

## 8. Recommended work plan for the NEXT chat

**Do not ask the user to re-explain the requirements or re-enter API keys.** Use the connected GitHub repository and work in small reviewed increments. The most valuable next sequence:

### Priority A — Fix quota use, fairness and repeated provider errors without adding costs

- Confirm latest `main` commit, both Arena workflows, actual latest GitHub scheduled run logs, `groq_quota.json` and successful agent turns from `arena-ledger`.
- Parse recent `400` / `429` frequency and time windows. Distinguish RPM/TPM/RPD/TPD and provider model support; investigate malformed-schema or Groq JSON response errors. Avoid blind retries of 400s.
- Create a dashboard of **per-bot successful inference sessions** (accepted hypotheses vs historically tested candidates), **failed calls**, **next eligible time**, **provider remaining budgets**, and a rolling 24-hour attempt ledger.
- If actual free quota safely exceeds the current 72/day, propose an adaptive local cap informed by measured provider limits, token burn and rate-limit feedback; no automatic paid tier or secret rotation.
- Enforce fairness: least-served bots prioritized *when capacity returns*, with per-bot retry cooldown, one-attempt-per-pass fairness and a breaker for persistent invalid model outputs.
- Maintain serialized ledger writes and anti-duplication of research/trades. Verify actual saved evidence in branch, not only green actions status.

### Priority B — Make source autonomy *real* rather than just search queries

- Add permitted text-page and public document retrieval with provenance, publication date, bounded size, URL allow/deny checks and prompt-injection isolation.
- Integrate source verification and source usefulness feedback; track when a bot merely saw an index snippet, when it read the underlying article, and what the source actually claimed.
- Support Reddit/GitHub and other public APIs where feasible, video transcripts where accessible and permitted; accept that some sites block scraping. Never fabricate access or use prohibited bypasses.
- Preserve total subject freedom: no list of preapproved strategies, topics or media outlets. Separate “can investigate” from “can run a paper trade.”

### Priority C — Give them a genuinely flexible scientific backtesting lab

- Define a safe intermediate strategy language (e.g. composable technical indicators, multi-symbol features, rule graphs, signal-to-order transitions, stop/exit/size logic) and a **deterministic interpreter** in an isolated historical simulator.
- Provide appropriately timestamped and license-compliant hourly/minute/daily OHLCV, volume, multi-asset, fees/commissions, corporate action metadata and, if possible, verified options chains / costs. No fabricated data or evaluation of minute claims on hourly close-only series.
- Require every proposed rule to carry exact asset universe, unit/timeframe, data dependencies, signal definition, execution assumptions, risk management and falsification test.
- Automate a first sanity gate, proper historical backtest, chronological holdout, walk-forward sensitivity, and only then queue a separate forward virtual portfolio experiment.
- Implement metrics: trade count, gross/net return, drawdown, profit factor, turnover, sample coverage, benchmark excess, confidence uncertainty, regime robustness, feature availability.

### Priority D — Independent reviews, status and researcher accountability

- Test and repair Gemini weekly special cycle. Save judge input evidentiary references and structured verdicts in the virtual ledger; make J01/J02/J03 disagree transparently. Judge recommendations never override hard vetoes.
- Publish a clear per-bot scoreboard: current unique idea, verified source, historical passes/fails, next test, skipped/delayed reason, API usage, position changes. Include a separate rule-based performance tab and clear “not real trading.”
- Give the user concise daily updates: who successfully researched, who was starved/429-limited, ideas with genuine historical data, best *credible* results, portfolio changes and remaining blockers.

## 9. Verification, GitHub workflow and useful commands

1. Read exact current paths before editing; use GitHub connector or repository clone, not stale chat paraphrases.
2. Make a **small feature branch + pull request** for changes affecting scheduled workflows or strategy interpretation, and review diff/CI. Do not change the live `run_bot.yml` as a convenience.
3. Test offline first:

```bash
python -m unittest discover -s research/trading-arena/tests -v
```

4. Run a pure mocked research turn (no live API) and test edge cases: quota 0, rate header formats, consecutive 429, persisted cooldown across GitHub runs, reset at UTC midnight, worker starvation after a long outage, malformed model JSON, conflicting ledger pushes, no lookahead, 0-trade gating, a source snippet containing malicious commands, invalid/stale market data.
5. Once CI is green, merge an appropriately scoped PR; inspect resulting scheduled/manual GitHub Actions *logs*, saved `records/arena/groq_research.json` and `groq_quota.json`, and compare before/after fairness. Manual dispatch may use a real Groq free API call; check budget first.
6. The repo is connected to the user’s GitHub account in ChatGPT. Use the connector for read/write PRs when available. Do not require the user to click a dozen GitHub screens or copy secrets. Never include secret values in issue/PR logs or this document.
7. Observe the protection of `arena-ledger`: atomic account recording and concurrency are essential because the AI job and baseline job can both write to the same branch.
8. Keep research activity independent of production; decline any automatic real-money promotions.

### Important GitHub pages

- [Repository homepage](https://github.com/28twagg-ops/TradingBot)
- [Arena code directory](https://github.com/28twagg-ops/TradingBot/tree/main/research/trading-arena)
- [Arena unit tests](https://github.com/28twagg-ops/TradingBot/tree/main/research/trading-arena/tests)
- [Groq workflow definition](https://github.com/28twagg-ops/TradingBot/blob/main/.github/workflows/groq-research.yml)
- [Rule-based + fallback workflow](https://github.com/28twagg-ops/TradingBot/blob/main/.github/workflows/arena-paper.yml)
- [All GitHub Actions](https://github.com/28twagg-ops/TradingBot/actions)
- [Paper ledger branch](https://github.com/28twagg-ops/TradingBot/tree/arena-ledger/records/arena)

## 10. Paste this starter request into the NEXT ChatGPT conversation

> You are taking over the GitHub repository https://github.com/28twagg-ops/TradingBot. First read the full transfer document at docs/ARENA_PROJECT_HANDOFF.md on main, then inspect the current main code, Arena GitHub workflows, last successful/failed run logs, and the arena-ledger branch. The primary objective is 10 truly independent AI strategy researchers with complete freedom of subjects/sources (including Reddit, TikTok, YouTube, GitHub and obscure sources); correct historical data and robust backtesting *before* virtual forward paper trading; fair, free-tier, provider-aware inference utilization throughout the day, prioritizing bots that have not successfully researched recently; and 3 independent Gemini evidence judges. Do not conflate the AI virtual accounts with the deterministic rule-based virtual dashboard. Do not touch the existing live stock/options trading workflows or enable paid API fallback. First identify the highest-impact current blocker based on actual evidence, propose the smallest safe fix, implement it on a branch, run tests, and verify saved run results. Do not ask me to repeat these requirements.

---

**End of handoff.** Keep this file updated when the architecture, quotas, functionality or validation status materially changes. There are no API keys or personal secrets in this document.
