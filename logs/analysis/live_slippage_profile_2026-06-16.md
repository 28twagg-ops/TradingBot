# Live Slippage Profile (2026-06-16)

- Transaction rows: 959
- Execution audit rows: 383
- TX date range: ('2026-04-21', '2026-06-16')
- Audit date range: ('2026-06-10', '2026-06-16')

## Execution audit slippage_pct

- All: mean -0.0314%
- BUY: mean +0.0000%
- SELL: mean -0.0584%

## Stop-loss sells (transactions)

- Count: 279
- Mean P&L: -1.80%
- Overshoot vs -0.5%: mean -1.30%

## Recommended sim parameters

- BUY_SLIPPAGE_PCT: +0.0000
- SELL_SLIPPAGE_PCT: -0.0584
- ROUND_TRIP_SPREAD_PCT: 0.1167
- Stop samples for Test 33: 279

JSON: `live_slippage_profile_2026-06-16.json`