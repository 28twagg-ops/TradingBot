# Profitability Research Dashboard

_Generated 2026-10-23T16:30:42.963019+00:00_

## Data sources

- **ledger**: `C:\Users\28twa\Documents\Other Desktop Stuff\TradingBot-git\logs\options_trial\_ledger\master_ledger.csv`
- **selection**: `C:\Users\28twa\Documents\Other Desktop Stuff\TradingBot-git\logs\options_trial\reports\2026-10-23_strategy_selection.md`
- **quality**: `C:\Users\28twa\Documents\Other Desktop Stuff\TradingBot-git\logs\options_trial\reports\2026-10-23_data_quality.md`
- **selection_csv**: `C:\Users\28twa\Documents\Other Desktop Stuff\TradingBot-git\logs\options_trial\reports\2026-10-23_strategy_selection.csv`

## Strategy scorecard (CLEAN lens primary)

| sid | status | clean n | clean med% | clean $ | clean $/trade | ALL $ | $ gap | score |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| S397 | PROFITABLE IN EXPLORATORY PAPER | 35 | +56.1 | $+1,072 | $+28.63 | $+1,021 | $-51 | 107.4 |
| S166 | PROMISING BUT UNVALIDATED | 12 | +60.8 | $+314 | $+24.17 | $+397 | $+83 | 98.7 |
| S167 | PROMISING BUT UNVALIDATED | 19 | +106.0 | $+450 | $+21.68 | $+370 | $-80 | 92.7 |
| S404 | PROFITABLE IN EXPLORATORY PAPER | 53 | +53.2 | $+1,161 | $+19.91 | $+909 | $-252 | 90.6 |
| S362 | PROFITABLE IN EXPLORATORY PAPER | 33 | +57.1 | $+792 | $+22.00 | $+1,432 | $+640 | 90.0 |
| S406 | PROFITABLE IN EXPLORATORY PAPER | 75 | +53.3 | $+930 | $+10.40 | $+3,191 | $+2,261 | 67.0 |
| S410 | PROMISING BUT UNVALIDATED | 10 | +58.3 | $+142 | $+12.20 | $+192 | $+50 | 57.5 |
| S432 | NEEDS MORE DATA | 4 | +17.1 | $+21 | $+3.25 | $+21 | $+0 | 41.3 |
| S430 | NEEDS MORE DATA | 4 | +5.4 | $+14 | $+1.50 | $+14 | $+0 | 33.7 |
| S431 | NEEDS MORE DATA | 0 | +0.0 | $+0 | $+0.00 | $+0 | $+0 | 0.0 |

## Portfolio simulations

### Mode: `discovery`

- Starting options cash: $250
- Stock reserve (untouched): $250
- Fills / skip_capital / skip_simultaneous: 196 / 0 / 0
- Realized P&L: $+3,955.00
- Ending options cash: $4205.00
- Max DD (options sleeve): $-561.00
- Max simultaneous: 4
- Note: DISCOVERY / exploratory paper — no capital or concurrency constraints

### Mode: `capital_constrained`

- Starting options cash: $250
- Stock reserve (untouched): $250
- Fills / skip_capital / skip_simultaneous: 71 / 0 / 125
- Realized P&L: $+652.00
- Ending options cash: $902.00
- Max DD (options sleeve): $-122.00
- Max simultaneous: 2
- Note: Whole contracts; premium locked until exit; max 2 simultaneous; stock reserve $250 untouched

### Mode: `combo_constrained`

- Starting options cash: $250
- Stock reserve (untouched): $250
- Fills / skip_capital / skip_simultaneous: 36 / 0 / 32
- Realized P&L: $+939.00
- Ending options cash: $1189.00
- Max DD (options sleeve): $-136.00
- Max simultaneous: 2
- Note: Whole contracts; premium locked until exit; max 2 simultaneous; stock reserve $250 untouched | arms=['S397', 'S362']

## CLEAN daily P&L correlation

| strategy_id   |   S362 |   S397 |   S404 |   S406 |
|:--------------|-------:|-------:|-------:|-------:|
| S362          |   1    |   0.07 |   0.14 |   0.62 |
| S397          |   0.07 |   1    |   0.91 |   0.13 |
| S404          |   0.14 |   0.91 |   1    |   0.22 |
| S406          |   0.62 |   0.13 |   0.22 |   1    |
