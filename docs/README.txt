TradingBot (GitHub live repo) — documentation index
===================================================

START HERE: docs/TIMELINE.md  (timeline + where to find everything)

ACTIVE (current use)
  docs/handoff/          ChatGPT / independent review exports (2026-06-19)
  docs/ops/              Cron pipeline validation
  logs/transactions.csv  Live trade ledger
  logs/analysis/         paper_trading_validation.md, daily_slippage_watch.md,
                         pdt_removal_audit.md, live_slippage_profile_2026-06-16.*
  logs/ab_test/          A/B concentration test dashboards (when running)
  simulations/           Backtest / PDT removal sim code + results/

ARCHIVE (historical — not deleted)
  docs/archive/          Old handoffs, runbooks, agent plans, incident reports
  logs/analysis/archive/ Old sim exports, validation dumps, June studies

Bot entrypoints: rubber_band_bot.py, generate_dashboard.py
Scripts: scripts/  |  Tools: tools/
