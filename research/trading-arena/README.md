# TradingBot Arena — autonomous paper-research foundation

**Status: development branch only. Not live, not deployed.** This repository contains a live-money stock bot, so Arena must have *zero* access to production Alpaca API keys, live workflows, or live account state.

## Desired architecture

- **10 Strategists** (S01–S10): isolated paper accounts starting at **$100 each**. Every worker can propose buys/sells for U.S. stocks, BTC, ETH, and long options, subject to cash, whole-contract limits, market/data eligibility, and account permissions. Unlimited notional or naked options positions are forbidden.
- **3 Council judges** (Accounting, Evidence, Risk): independently audit a worker's reports and trades, compare against independently sourced observations, and publish evidence for disagreements. A 2-of-3 vote can prioritize further *paper* research; **votes never override failed hard accounting/data-integrity checks**. The foundation includes three deterministic reviewers plus an **optional** three-call hosted-AI advisory council, not yet wired to the scheduled job.
- **No central AI Research Director**: workers research independently; a simple scheduler wakes them.
- **Historical research**: workers can consult existing paper/live research **only as labeled, untrusted prior evidence**, never ground truth. Judges use independently reconstructed trade/market records. Do not claim old data is a clean holdout.
- **Promotion**: only increases *virtual research budget*, subject to independent forward evidence. Live deployment requires separate explicit human authorization.

## Foundation available in this branch

- \`config.json\` declares the ten $100 worker accounts and the three judge roles.
- \`arena.py\` provides a **self-contained virtual paper order ledger**. Paper stocks and crypto may use fractional units; long options require whole contracts and use an explicit 100-share multiplier. Each worker's account is isolated; orders exceeding available cash or sells exceeding held quantity are rejected.
- \`tests/test_arena.py\` validates isolation, options affordability, oversells, tamper detection, and voting.
- \`.github/workflows/arena-paper.yml\` runs the unit suite on a schedule and manual dispatch **only after merged to the default branch**. Its permission is read-only, and it passes no brokerage credentials.

**Not implemented yet:** real market data collection, autonomous strategy execution, actual Alpaca PAPER order routing, independent paper account reconciliation, hosted AI idea generation, scheduling of the optional AI council, long-term append-only storage, a historical full-stack backtest, and the human-audited live release mechanism. Neither this branch nor a scheduled test runner is a fully autonomous 10-bot trading operation. Those are next phases, and must be implemented and tested before any claimed performance is reported.

## Using prior research responsibly

Examples from the existing repository (do not move or mutate them):
- \`logs/options_trial/reports/*_strategy_selection.md\` — exploratory strategy selection. CLEAN vs TAINTED and survivor-selection cautions.
- \`logs/options_trial/reports/*_data_quality.md\` — material attribution debt (e.g., orphan exits).
- \`logs/rubber_band_report.md\` and \`logs/dashboard.md\` — real-money stock bot results, separate from options paper returns.
- \`docs/ESCALATION_PROTOCOL.md\` and \`simulations/results/\` — prior designs, methodology, and historical failures.

An AI worker may *reference* these in hypothesis design, but must not quote their outcomes as its own. Each research claim stores original source ID, timestamp, category, and verification status. Holdouts exposed to earlier selections are never relabeled "untouched."

## Run locally (stdlib-only foundation)

\`\`\`bash
python -m unittest discover -s research/trading-arena/tests -v
python research/trading-arena/arena.py --demo
\`\`\`

The \`--demo\` command uses **clearly synthetic test observations** to demonstrate virtual trades, never actual returns. No market data is fetched and **no paper broker orders are placed**.

## Safeguards

- No API key or secret in source code or generated artifacts.
- Council cannot authorize production trades or rewrite submitted ledger events.
- Evidence first: a split council vote does not establish whether a report is true.
- If a worker is marked suspicious, it may be suspended and its entire history retained.
- The existing live workflow \`.github/workflows/run_bot.yml\` is untouched.

## Deployed free research mode (current scope)

- 10 autonomous **RULE-BASED** strategies currently execute virtual-only research; they are not 10 independently reasoning LLM instances. A model API (separate service and budget) is necessary for novel web/TikTok idea invention.
- The scheduled runner is `run_virtual.py`, using completed hourly Yahoo bars for a limited list of stocks, BTC/USD, ETH/USD, SOL/USD. This can run without any Alpaca credentials or expenditure. Its fill prices are *indicative*; no actual Alpaca PAPER order is sent.
- A separate `arena-ledger` Git branch stores state and virtual scoreboards, and cannot reset your production stock or options ledgers. All workers start with $100 virtual; risk is capped to about $40 per new position, no margin or shorting.
- Options contracts and the full Alpaca asset catalog are **not yet traded**. The accounting engine can represent whole long options contracts if under the worker's $100 limit, but requires genuine point-in-time option quotes, approval/eligibility validation and broker-paper account isolation before activation.
- Three deterministic council validators run after virtual trades. `council_ai.py` has optional code for three independent hosted-AI advisory reviewers, which cannot run without a paid or otherwise authorized model API. Missing executable-price corroboration keeps evidence REVIEW_REQUIRED.
- Free hosted GitHub Models inference was retired in July 2026. No model fees or new AI secrets have been authorized or configured here.
- Workflow `arena-paper.yml` runs every two hours, and once upon changes merged to main; GitHub scheduled runs can be delayed. GitHub Actions's standard runner use for public repositories is ordinarily free.
- Virtual scoreboard after first successful job: https://github.com/28twagg-ops/TradingBot/blob/arena-ledger/records/arena/DASHBOARD.md


## Optional FREE Gemini research agents (October 2026)

There is no Research Director agent. Exactly ten individually prompted strategists and three independent council reviewers use Google's Gemini Developer API when explicitly enabled.

- The gemini_cycle.py script makes at most 13 model requests per day: one per strategist and one per judge. It runs at 19:17 UTC on scheduled days. Existing rule-based virtual monitoring continues every two hours. If Google returns 429/403, it stops requesting AI calls. With no Gemini key, the cycle simply skips.
- Default model: gemini-2.5-flash-lite. Use a Google AI Studio Free Tier project with **no billing attached**, subject to Google's variable free allowances. A key from a paid project CAN incur charges; this software cannot guarantee $0 billing for a paid project.
- Each strategist independently receives its specialty, recent observed hourly price bars, curated descriptions of historical studies, and public Crossref academic-paper metadata. Each invents a testable hypothesis and chooses one BUY, SELL or HOLD virtual action.
- The deterministic order validator accepts only quote-supported symbols, a maximum 40% of remaining cash and $40 per opening order, no margin, shorts or leveraged instruments. These orders are local virtual-paper accounting, not real Alpaca PAPER brokerage orders.
- Three AI reviewers independently evaluate accounting, evidence and risk, but their votes cannot establish authentic market fills. No worker is promoted to real money or certified profitable by the AI council.
- No live brokerage keys or transaction records are sent to Gemini. The summarized historical research is tagged exploratory or mixed-quality, and is not treated as an untouched holdout. Google free-tier API input may be used to improve Google's products.
- Crossref scholarly metadata is the currently implemented live external research source. TikTok and other login-gated websites are NOT automatically scraped. Do not treat model-supplied references as verified sources.

### Required one-time credential setup — user controls Google authorization

1. Open https://aistudio.google.com/apikey and get an API key in a Free Tier project with **billing disabled**.
2. Open https://github.com/28twagg-ops/TradingBot/settings/secrets/actions and choose New repository secret. Set name Gemini_API_Key (exact capitalization), paste its value, and save. The workflow maps this existing GitHub secret to the internal GEMINI_API_KEY environment variable.

Never paste a key into ChatGPT, the repository, or a source file. Once configured, the following scheduled job at 19:17 UTC will attempt AI research without repeated prompting.

### Status and capabilities

- Core virtual dashboard: https://github.com/28twagg-ops/TradingBot/blob/arena-ledger/records/arena/DASHBOARD.md
- Gemini council results (after first successful Gemini cycle): https://github.com/28twagg-ops/TradingBot/blob/arena-ledger/records/arena/AI_COUNCIL.md
- Machine-readable AI research: https://github.com/28twagg-ops/TradingBot/blob/arena-ledger/records/arena/ai_report.json

Not yet present: executable autonomous AI-designed backtest variants, all Alpaca supported assets, genuine options-chain fills, Alpaca PAPER-only brokerage routing, independently verified execution quotes, live trading, private social-media browsing or guaranteed profitability. The Council must not claim research proposals are independently verified trading returns. Existing records, paper ledgers and live-bot workflow must remain untouched.


## 2026-10: Rotating independent research (Groq daily + Gemini weekly)

This project has **NO AI Research Director**. The 10 paper researchers are allowed
to change research direction over time and propose original candidate rules.
The code enforces a safe experiment language, independent-account cash rules,
and separate historic-vs-forward evidence grades.

### Groq: inexpensive everyday reasoning, free-plan opt-in

- Workflow: .github/workflows/groq-research.yml; one rotating researcher per
  half-hour (approximately 48 total researcher calls/day). Each of 10 workers
  gets approximately 4-5 research slots per day, provided GitHub scheduling
  and Groq rate limits permit. This is NOT an always-on process.
- Model: openai/gpt-oss-20b via Groq's free API plan, no billing required.
  Groq publishes limits around 1,000 requests/day and 200,000 tokens/day
  on this model as of October 2026; exact account limits can be lower.
  We impose an additional rate cap by scheduling only one call/slot.
- Each researcher picks its own topic, proposes a hypothesis and parameters
  (trend, breakout, mean reversion or momentum), runs deterministic
  chronological next-hour-close historical PROXY tests, and may propose a
  spot-market virtual buy/sell within its OWN initial $100 account.
- Experimental variants and fail outcomes are recorded in
  records/arena/groq_research.json and records/arena/GROQ_RESEARCH.md,
  committed to arena-ledger. Prior experiments inform subsequent prompts.
- Source code from LLM output is NEVER executed. The final dispatcher validates
  quote-supported asset symbols and cash constraints; unsupported options
  or unavailable symbols can be researched, but not virtually traded.
- **This is a bounded strategy research DSL, not truly unlimited AI agency.**
  More research families, online-source retrievers and point-in-time option
  data remain to be built. Historical proxy backtests do not prove profitability.

**One-time user-only setup:** Create a GroqCloud *Free* account at
https://console.groq.com/keys ; do not upgrade to paid. Add its key to GitHub
repository Actions secrets under name GROQ_API_KEY. Do NOT paste it into
chat, a commit or an issue. Without a key, all Groq jobs simply skip their
AI calls, and the original scheduled virtual algorithm remains functional.

### Gemini: reserve stronger free-tier review capacity

The original 10-per-day Gemini research cycle is NO LONGER scheduled.
Instead, the verified existing Gemini_API_Key secret powers up to **three**
independent weekly council-research reviews at Sunday 19:17 UTC.
The model's rate cap can still interrupt any review. These advisors
never certify indicative Yahoo fills or enable live trading. Reports go
to records/arena/GEMINI_SPECIAL.md and gemini_special.json.

### Practical free-tier boundaries

- Groq free plans remain rate-limited; the 48-call/day routine target is not a
  guarantee. A Groq 429 halts that cycle without spending money or calling
  paid providers. Model memory is persisted as explicit per-agent research
  history, not hidden language-model training.
- Open-source Ollama models can run without metered cloud API usage on a
  computer you operate, but that requires local hardware and power.
- GitHub Actions scheduled jobs can be delayed or skipped; there is no
  continuously running cloud instance supplied by the subscription.
- The repo is PUBLIC. Research snapshots are visible, so do not pass private
  financial records, personal data, brokerage credentials or confidential
  documents to either external provider or into commit history.
- Nothing can transfer to live trading without a separate explicit approval
  and production-only code review.


## Overnight scheduling reliability improvement (October 26, 2026)

GitHub Actions had been configured for twice-hourly Groq research, but the real
GitHub schedule history showed only one successful overnight *scheduled* Groq
run. The old worker selection was tied to the hour's time slot, leaving many
strategists without any chance to research when cron runs slipped or dropped.

The revised Groq workflow now attempts **five different, overdue strategists
per job**, fairly selected by recorded actual research attempts, and gives
another set the next time it runs. Its dedicated schedule is every two hours
at :23 UTC, plus extra overnight attempts at **03:53, 07:53 and 11:53 UTC**.
The independent two-hour paper workflow, at :17 UTC, also makes a fallback
research attempt if no Groq research event has been recorded for 70 minutes.
This is useful redundancy, not a guarantee: GitHub's `schedule` events may
still be delayed or dropped under load.

Groq usage is conservatively capped at 40 recorded research attempts per UTC
day, maximum five per job. Provider 403/429 errors halt the current batch;
there are no retries to a paid provider. A provider's lower token/rate quota
may restrict throughput further. Do not attach paid billing if the goal is
zero additional charges.

The model can invent and backtest bounded declarative strategies only.
Positions remain **virtual**, independent of production credentials. These
checks do not replace proper quote-level fills or a truly untouched forward
validation set.


## Open-ended investigator autonomy — public-source prototype (October 2026)

**The investigation scope belongs to each researcher, not a centrally assigned
market or source whitelist.** The 10 Groq researchers may change research subjects
at each turn and individually choose their NEXT search query, source categories,
and even a specific public website. Research leads can come from TikTok,
YouTube, Reddit, GitHub, blogs, forums, academic papers, or any indexed public
site. All source leads are logged with URLs and whether only a snippet/metadata
was actually retrieved, so claimed source provenance can be audited.

**What works:** agent-chosen next-search plans are persisted independently in
each worker's groq_experiments history; the following run performs up to
three bounded searches using that plan before the researcher chooses its next
idea. General/custom/social search uses the publicly reachable Bing RSS search
index (an unofficial, best-effort interface); GitHub repositories use public
GitHub search metadata. Only fixed provider endpoints are contacted. Linked
content is not downloaded or run. Untrusted search snippets are never
instructions. Missing sources remain explicitly missing; no citations are
invented. No subscription or platform account is bypassed.

**What does NOT yet work:** watching TikTok/YouTube videos, transcribing audio,
reading arbitrary sites beyond indexed snippets, opening private/subscription
pages, researching all derivative instruments with real historical chains,
or generating/executing arbitrary strategy code. Some sources may be missing or
blocked by the index. To support those capabilities, additional permitted
provider APIs and historical market data integrations are needed. We never
describe search snippets as whole-video or article research.

A new model output separates the **free-form scientific hypothesis** from
**the executable backtest representation**. All ideas are valid to investigate,
including those not expressible by the current engine. Unsupported hypotheses
(minutes, order books, volume, options, true cross-asset dependencies, etc.)
are recorded as RESEARCH_IDEA_NEEDS_DATA; they are NOT falsely backtested
against an unrelated hourly single-asset close series or paper traded.
The only strategies eligible for paper orders are honestly expressible as
supported single-asset hourly-close rule tests. BUY still requires at least
three historical research entries, two retrospective validation entries and
positive validation P&L with fees. This is NOT a scientific proof of real-world
profit and cannot guarantee a favorable live market.

Model output and online text cannot directly change the source code,
brokerage integrations, security controls or real-money strategies. The existing
rule-based virtual scoreboard is a **separate system** and is not proof of AI
strategy validation. Gemini remains a limited-capacity specialist reviewer.


## Fair 24-hour Groq quota scheduler (October 28, 2026)

Every available scheduled session should give priority to the workers who have
the *fewest successfully accepted research sessions* today, breaking ties by
persistent completed lifetime history. Invalid output, rejected model output,
and Groq 429 responses do **not** falsely count as successes. Each researcher
gets at most one attempt within a 40-minute window, so failures don't
monopolize all available requests or starve other accounts.

The free-tier scheduler no longer tries to use all daily credits immediately
after UTC midnight. It releases its local conservative target of **72 requests
per UTC day** proportionally over the 24 hours, with catch-up capacity for
missed GitHub runs. This is a **safety target, not a statement of the actual
Groq org quota**: the account may have smaller provider-specific RPM, RPD,
TPM, TPD, or concurrent usage limits. API response headers supply request/day
and token/minute availability. The scheduler spaces calls at least 40 seconds
apart, honors Retry-After and provider daily-reset hints after HTTP 429, and
records sanitized metadata (no API keys) in records/arena/groq_quota.json. It
does not spin on exhausted quotas, retry 429 requests in a loop, or switch to
a paid inference provider.

The dedicated workflow now checks hourly, with some extra overnight windows;
the independent two-hour baseline Arena workflow also participates when
time-paced free research credits are left. GitHub schedules are best-effort
and can be delayed. The saved quota report shows which researchers are
next priority. Research remains virtual and is not live brokerage execution.
