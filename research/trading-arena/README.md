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
