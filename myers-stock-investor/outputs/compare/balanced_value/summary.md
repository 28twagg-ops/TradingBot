# Myers Backtest — Strategy B — Balanced Value

Model: `1.1.0` · Profile: `balanced_value` · Mode: **EXPLORATORY**

## Limitation

EXPLORATORY MODE: prices are point-in-time; yfinance fundamentals are NOT filing-date accurate and may look ahead. Universe is a modern survivor list (survivorship bias). Results are experimental, not validated historical performance. Live trading disabled.

## Performance (daily mark-to-market)

| Metric | Strategy | SPY buy-hold (same calendar) |
|---|---:|---:|
| start_value | $100,000 | $100,000 |
| end_value | $118,088 | $194,585 |
| cumulative_return | 18.1% | 94.6% |
| cagr | 3.4% | 14.3% |
| max_drawdown | -3.3% | -33.7% |
| volatility | 3.5% | 21.0% |
| sharpe | 0.97 | 0.74 |
| sortino | 1.42 | 0.91 |
| best_calendar_year | 5.9% | 30.5% |
| worst_calendar_year | -1.2% | -18.6% |

Trades: **2** (simulated)
Avg cash allocation: **83.1%**
Avg invested: **16.9%**
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
  "n_buy_candidate": 11,
  "buy_rate": 0.055,
  "rejection_category_counts": {
    "insufficient_margin_of_safety": 174,
    "excessive_valuation": 164,
    "low_business_quality_or_score": 142
  },
  "score_median": 67.46,
  "mos_median": -0.40099813575285864,
  "would_pass_mos_15": 0,
  "would_pass_quality_fair": 0,
  "would_pass_deep_value": 11,
  "closest_to_qualifying": [
    {
      "ticker": "MRK",
      "date": "2022-09-30",
      "score": 74.6,
      "mos": 0.14382250440635225,
      "categories": [
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "MRK",
      "date": "2022-06-30",
      "score": 74.25,
      "mos": 0.10086537852953356,
      "categories": [
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "PG",
      "date": "2020-03-31",
      "score": 73.73,
      "mos": -0.09165552583132962,
      "categories": [
        "excessive_valuation",
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "MRK",
      "date": "2024-12-31",
      "score": 73.04,
      "mos": -0.05134098820154845,
      "categories": [
        "excessive_valuation",
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "MRK",
      "date": "2023-09-30",
      "score": 73.04,
      "mos": -0.0514914423157946,
      "categories": [
        "excessive_valuation",
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "PG",
      "date": "2020-06-30",
      "score": 72.91,
      "mos": -0.19454336776832337,
      "categories": [
        "excessive_valuation",
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "MRK",
      "date": "2023-03-31",
      "score": 72.87,
      "mos": -0.07210536373271896,
      "categories": [
        "excessive_valuation",
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "AAPL",
      "date": "2020-09-30",
      "score": 72.79,
      "mos": 0.06366887283461486,
      "categories": [
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "MRK",
      "date": "2022-12-31",
      "score": 72.56,
      "mos": -0.11033770101499601,
      "categories": [
        "excessive_valuation",
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "MRK",
      "date": "2023-12-31",
      "score": 72.48,
      "mos": -0.12155063116281783,
      "categories": [
        "excessive_valuation",
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "AAPL",
      "date": "2021-03-31",
      "score": 72.35,
      "mos": 0.009227411584529062,
      "categories": [
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "MRK",
      "date": "2023-06-30",
      "score": 72.08,
      "mos": -0.17056853035125835,
      "categories": [
        "excessive_valuation",
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "JNJ",
      "date": "2020-03-31",
      "score": 72.0,
      "mos": 0.10887292698194387,
      "categories": [
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "MRK",
      "date": "2024-09-30",
      "score": 71.92,
      "mos": -0.19061274129698502,
      "categories": [
        "excessive_valuation",
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "PG",
      "date": "2022-09-30",
      "score": 71.81,
      "mos": -0.33141883787883525,
      "categories": [
        "excessive_valuation",
        "insufficient_margin_of_safety"
      ]
    }
  ]
}
```

Live trading: **DISABLED**
