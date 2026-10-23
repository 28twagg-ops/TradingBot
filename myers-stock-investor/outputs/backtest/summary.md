# Myers Backtest — Strategy A — Conservative Acquirer

Model: `1.1.0` · Profile: `conservative_acquirer` · Mode: **EXPLORATORY**

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
  "terminal": 194584.932390947,
  "start_value": 100000.0,
  "end_value": 194584.932390947,
  "cumulative_return": 0.9458493239094701,
  "cagr": 0.1425137766061353,
  "max_drawdown": -0.3371726378600284,
  "volatility": 0.20997295188895113,
  "sharpe": 0.7412319415780925,
  "sortino": 0.9071031384865845,
  "best_calendar_year": 0.30505441706467673,
  "worst_calendar_year": -0.1864640270095459,
  "n_obs": 1258.0,
  "first_date": "2020-01-02",
  "last_date": "2024-12-31",
  "first_price": 295.3918151855469,
  "last_price": 574.7879638671875,
  "price_return": 0.9458493239094701
}
```

## Screening diagnostics

```json
{
  "n_evaluated": 190,
  "n_buy_candidate": 0,
  "buy_rate": 0.0,
  "rejection_category_counts": {
    "insufficient_margin_of_safety": 178,
    "excessive_valuation": 164,
    "low_business_quality_or_score": 142
  },
  "score_median": 67.66,
  "mos_median": -0.3998835957651403,
  "would_pass_mos_15": 1,
  "would_pass_quality_fair": 0,
  "would_pass_deep_value": 11,
  "closest_to_qualifying": [
    {
      "ticker": "MRK",
      "date": "2022-03-31",
      "score": 75.03,
      "mos": 0.1973773380171769,
      "categories": [
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "MRK",
      "date": "2022-09-30",
      "score": 74.6,
      "mos": 0.1438223336298321,
      "categories": [
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "MRK",
      "date": "2022-06-30",
      "score": 74.26,
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
      "mos": -0.051340902813288375,
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
      "mos": -0.07210544912097903,
      "categories": [
        "excessive_valuation",
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "AAPL",
      "date": "2020-09-30",
      "score": 72.79,
      "mos": 0.06366900013154791,
      "categories": [
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "MRK",
      "date": "2022-12-31",
      "score": 72.57,
      "mos": -0.11033753023847587,
      "categories": [
        "excessive_valuation",
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "MRK",
      "date": "2023-12-31",
      "score": 72.48,
      "mos": -0.12155071655107791,
      "categories": [
        "excessive_valuation",
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "AAPL",
      "date": "2021-03-31",
      "score": 72.35,
      "mos": 0.009227347936062533,
      "categories": [
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "MRK",
      "date": "2023-06-30",
      "score": 72.09,
      "mos": -0.17056861573951843,
      "categories": [
        "excessive_valuation",
        "insufficient_margin_of_safety"
      ]
    },
    {
      "ticker": "JNJ",
      "date": "2020-03-31",
      "score": 72.0,
      "mos": 0.10887317489070615,
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
    }
  ]
}
```

Live trading: **DISABLED**
