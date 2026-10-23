# Myers Backtest — Strategy F — Simple Reference

Model: `1.1.0` · Profile: `simple_reference` · Mode: **EXPLORATORY**

## Limitation

EXPLORATORY MODE: prices are point-in-time; yfinance fundamentals are NOT filing-date accurate and may look ahead. Universe is a modern survivor list (survivorship bias). Results are experimental, not validated historical performance. Live trading disabled.

## Performance (daily mark-to-market)

| Metric | Strategy | SPY buy-hold (same calendar) |
|---|---:|---:|
| start_value | $100,000 | $100,000 |
| end_value | $183,062 | $194,585 |
| cumulative_return | 83.1% | 94.6% |
| cagr | 12.9% | 14.3% |
| max_drawdown | -10.0% | -33.7% |
| volatility | 9.0% | 21.0% |
| sharpe | 1.40 | 0.74 |
| sortino | 1.90 | 0.91 |
| best_calendar_year | 19.7% | 30.5% |
| worst_calendar_year | 2.6% | -18.6% |

Trades: **10** (simulated)
Avg cash allocation: **38.8%**
Avg invested: **61.2%**
Decision rows: **200**

## Independent SPY audit (window start→end)

```json
{
  "terminal": 194584.9117285071,
  "start_value": 100000.0,
  "end_value": 194584.9117285071,
  "cumulative_return": 0.9458491172850712,
  "cagr": 0.14251375232543473,
  "max_drawdown": -0.33717275321149764,
  "volatility": 0.20997311851727063,
  "sharpe": 0.7412314206590958,
  "sortino": 0.907102914445937,
  "best_calendar_year": 0.3050545609120128,
  "worst_calendar_year": -0.1864641504440968,
  "n_obs": 1258.0,
  "first_date": "2020-01-02",
  "last_date": "2024-12-31",
  "first_price": 295.3918151855469,
  "last_price": 574.7879028320312,
  "price_return": 0.9458491172850712
}
```

## Screening diagnostics

```json
{
  "n_evaluated": 200,
  "n_buy_candidate": 144,
  "buy_rate": 0.72,
  "rejection_category_counts": {},
  "score_median": NaN,
  "mos_median": NaN,
  "would_pass_mos_15": 0,
  "would_pass_quality_fair": 0,
  "would_pass_deep_value": 0,
  "closest_to_qualifying": []
}
```

Live trading: **DISABLED**
