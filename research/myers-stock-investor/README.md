# Myers Stock Investor

Standalone **business-acquirer** investment research, scoring, valuation, and
backtesting spin-off. Kept separate from the options TradingBot.

> Evaluate a stock as an ownership interest in an actual business,
> not merely as a fluctuating ticker symbol.

**Live brokerage trading is disabled.** Research + paper simulation only.

## Install

```bash
cd myers-stock-investor
python -m pip install -r requirements.txt
python -m pytest tests -q
```

## Commands

```bash
# Single-name / multi-name analysis (JSON)
python -m myers analyze AAPL MSFT --out outputs/sample_report.json

# Audited backtest: quarterly decisions, daily mark-to-market vs SPY
python -m myers backtest \
  --start 2020-01-01 --end 2024-12-31 \
  --universe AAPL,MSFT,COST,XOM,JNJ,CAT,UNH,PG,WMT,MRK \
  --profile conservative_acquirer \
  --out outputs/backtest

# Compare experimental profiles under identical assumptions
python -m myers compare \
  --start 2020-01-01 --end 2024-12-31 \
  --universe AAPL,MSFT,COST,XOM,JNJ,CAT,UNH,PG,WMT,MRK \
  --profiles conservative_acquirer,balanced_value,quality_fair_value,simple_reference \
  --out outputs/compare

python -m myers profiles
python -m myers version
```

Dashboard:

```bash
streamlit run dashboard/app.py
```

## Strategy profiles

| Key | Idea |
|---|---|
| `conservative_acquirer` | Score≥70, MOS≥25% (default / Myers-strict) |
| `balanced_value` | Score≥70, MOS≥15% |
| `quality_fair_value` | Score≥80, MOS≥0% |
| `deep_value` | Score≥60, MOS≥30% |
| `quality_value_ranking` | Soft floors + rank by score+MOS |
| `simple_reference` | Equal-weight deploy (no MOS filter) |

Thresholds are **experimental**, not optimized optima.

## Backtesting methodology (v1.1)

1. **Decisions:** quarter-ends (`QE`).
2. **Valuation of portfolio:** **daily** mark-to-market on the SPY trading calendar.
3. **Benchmark:** SPY buy-and-hold on the **same** first/last trading dates (auto-adjusted closes).
4. **Cash:** default 0% yield (`backtest.cash_annual_rate`).
5. **Costs:** commission_bps + slippage_bps on each trade.
6. **Modes:**
   - `exploratory` (default): yfinance fundamentals may look ahead; survivor universe.
   - `validated`: **refuses** until a point-in-time fundamentals provider is configured.

See `outputs/AUDIT_REPORT.md` for the v1.0 → v1.1 calculation audit.

## Corrected smoke results (exploratory)

Window 2020-01-02 → 2024-12-31, 10 mega-caps, conservative profile:

| | Strategy | SPY |
|---|---:|---:|
| Cumulative | +18.1% | **+94.6%** (was misreported +144%) |
| Max DD | -3.3% | **-33.7%** (was -24.5% on quarterly sampling) |
| Trades | 2 | — |
| Avg cash | 83% | — |

Why few trades: median MOS deeply negative on this universe; only COVID-quarter AAPL/MRK cleared 25% MOS. Details in the audit report and `outputs/backtest/rejections.csv`.

## Data providers

| Data | Source | PIT? |
|---|---|---|
| Prices | yfinance adjusted daily | Yes (as-of date) |
| Fundamentals | yfinance statements/info | **No** |
| SEC XBRL helper | `myers/data/sec_edgar.py` | Optional enrichment |

## Layout

```
myers-stock-investor/
  config/strategy.yaml
  myers/           # library
  dashboard/app.py
  tests/
  outputs/         # local runs (gitignored patterns apply)
```

## Philosophy

Think like a business acquirer. Analyze like a financial engineer.
Test like a quantitative researcher. Execute conservatively.
