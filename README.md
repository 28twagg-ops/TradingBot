# TradingBot

This repository includes a live stock-trading system, existing options research/paper workflows, and a **separate, experimental, virtual-only AI research Arena**. Those systems are distinct: Arena research does **not** place Alpaca brokerage orders or authorize live deployment.

## Start here: project handoff for the next ChatGPT conversation

**[Read the complete TradingBot Arena transfer and engineering handoff](docs/ARENA_PROJECT_HANDOFF.md)**

The handoff contains the original project goals and constraints, architecture, exact repository/workflow paths, independent S01–S10 / J01–J03 design, AI vs. rule-based virtual ledgers, Groq/Gemini orchestration, quota limits, historical performance caveats, outstanding bugs, test instructions and an ordered development plan.

### Arena quick links

- [Arena research source](research/trading-arena/)
- [Current Arena research logs and accounts](https://github.com/28twagg-ops/TradingBot/tree/arena-ledger/records/arena)
- [Live GitHub Actions runs](../../actions)
- [Groq automated research workflow](.github/workflows/groq-research.yml)
- [Rule-based and fallback virtual workflow](.github/workflows/arena-paper.yml)

**Important:** The first section of the older [Arena README](research/trading-arena/README.md) is historical and has stale “not deployed” language. The linked handoff and current GitHub workflows/ledger should be used for up-to-date status.

The user's intended Arena is ten independent, source-agnostic strategy researchers that test ideas against suitable historical data before any **virtual** paper trading. Freedom to investigate any public source does not imply verified access to its full contents or permission to execute untrusted source code. No automatic real-money strategy promotion, secret sharing or paid API fallback.
