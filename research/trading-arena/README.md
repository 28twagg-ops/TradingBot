# TradingBot Arena — autonomous paper-research foundation

**Status: development branch only. Not live, not deployed.** This repository contains a live-money stock bot, so Arena must have *zero* access to production Alpaca API keys, live workflows, or live account state.

## Desired architecture

- **10 Strategists** (S01–S10): isolated paper accounts starting at **$100 each**. Every worker can propose buys/sells for U.S. stocks, BTC, ETH, and long options, subject to cash, whole-contract limits, market/data eligibility, and account permissions. Unlimited notional or naked options positions are forbidden.
- **3 Council judges** (Accounting, Evidence, Risk): independently audit a worker's reports and trades, compare against independently sourced observations, and publish evidence for disagreements. A 2-of-3 vote can prioritize further *paper* research; **votes never override failed hard accounting/data-integrity checks**. The foundation includes three deterministic reviewers plus an **optional** three-call hosted-AI advisory council, not yet wired to the scheduled job.
- **AI research director** (future integration): searches published studies and generates versioned, testable strategy proposals, with budget constraints, a restricted strategy language, and an isolated testing environment. It never executes unreviewed arbitrary LLM-generated Python.
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
