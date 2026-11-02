# Rubber Band validation — research gate (2026-11-02)

**Status: NOT VALIDATED / LIVE GATE CLOSED.** Separate branch; no changes to live trading, scheduled jobs, or production strategy.

## Critical pre-existing look-ahead issue
In `simulations/historical_backtest.py`, `_match_signal(..., "rubber_band")` depends on the *current day's Close, High and Low*. `signals_to_events()` then initializes pricing with `S0 = r.S_open` (the *same day's open*). A same-day-open entry cannot know the day's final Close/High/Low. This makes that backtest unsuitable as evidence for live profitability. The new validator uses the completed signal bar and enters at the **next day's opening price**.

## New implementation
- `simulations/validate_rubber_band.py`: reads actual per-symbol daily OHLCV CSVs; flags missing or corrupt data; enforces next-session entries; prevents overlapping positions in the same symbol; handles adverse gap-through-stop fills; creates per-trade CSVs and JSON summary for ideal / realistic / harsh scenarios; divides trades by a fixed out-of-sample boundary; blocks approval for insufficient harsh OOS trades or weak profit factor.
- `tests/test_rubber_band_validation.py`: unittest regressions for temporal ordering, costs, stop-gap behavior and missing-data gating.

## Run
From repo root, on an environment with Python 3.10+:
```bash
python -m unittest discover -s tests -p 'test_rubber_band_validation.py' -v
python simulations/validate_rubber_band.py --data-dir data/validation_csv --split-date 2024-01-01 --hold-bars 3 --stop-pct 0.005
```
Put real, independently sourced **per-symbol** CSV files in `data/validation_csv/`. Each CSV needs `Date,Open,High,Low,Close,Volume` columns. Do **not** use synthesized prices as evidence. Output: `simulations/results/rubber_band_validation/`.

## Strict limitations / next work
1. This is an independent daily-bar **equity-price proxy** for the Rubber Band signal, not a faithful reconstruction of the options execution engine or full live strategy (which may use additional RSI criteria and order logic). An apples-to-apples production-equivalent replay still must be built from timestamped decision logs and true executable quotes.
2. Three scenarios use **assumed** per-side costs: ideal 0bps/$0; realistic 10bps/$1 per share; harsh 30bps/$2 per share. These are deliberately conservative placeholders, not estimates calibrated to your actual execution. Fixed dollar fee is **per share per side** in this one-share proxy.
3. Reported net return is per-share trade return, **not** a compounded capital curve. Cross-symbol capital constraints, short borrow, sector exposure, dividends, split adjustments, portfolio drawdown, Sharpe, and SPY comparison are **not implemented**. Do not infer them.
4. The split date is a single holdout, **not** a complete rolling walk-forward procedure. An independent series of purged walk-forward windows, frozen configuration manifest and confidence intervals is still required.
5. Verify delisted symbols, corporate actions, historical constituent selection, missing-market sessions, and input provenance. This script cannot prove survivorship safety.
6. Missing historical CSVs => no backtest; do not claim returns without the data. The original paper-ledger accounting mismatch also remains a **separate blocking issue**.
7. The validator's `gate=REVIEW_REQUIRED` is **not approval**; only `BLOCK` or `REVIEW_REQUIRED` can be emitted. Do not auto-enable live entries.
