# Stop Overshoot Forensics
Generated: 2026-06-16 23:17 UTC

## Summary
- Total stop-loss sells: **211**
- Worse than -0.5% threshold: **208** (98.6%)
- Fractional sells (<$25): **208** / 208
- Same-day (hold 0d): **3** / 208
- Look-into file entries: **172** (PDT deferred: **170**)
- Rough extra loss vs -0.5% cap (overshoot × size): **$41.93**

## Overshoot severity buckets

| Bucket | Count |
|--------|------:|
| -0.5_to_-1% | 70 |
| -1_to_-2% | 77 |
| -2_to_-5% | 48 |
| -5_plus% | 13 |

## Worst 50 stop exits

| Date | Ticker | P&L% | Hold | $Size | Sell method |
|------|--------|------|------|-------|-------------|
| 2026-06-11 | ORCL | -13.91% | 1d | $17.26 |  |
| 2026-06-12 | SATS | -6.95% | 1d | $9.15 |  |
| 2026-05-27 | APA | -6.86% | 1d | $19.48 |  |
| 2026-06-10 | NOW | -5.98% | 1d | $19.07 |  |
| 2026-06-10 | COIN | -5.95% | 1d | $19.11 |  |
| 2026-06-11 | AA | -5.93% | 1d | $18.97 |  |
| 2026-06-11 | BILL | -5.73% | 1d | $19.01 |  |
| 2026-06-15 | MUR | -5.69% | 3d | $2.84 |  |
| 2026-06-15 | PBF | -5.17% | 3d | $15.42 |  |
| 2026-06-15 | OVV | -5.11% | 3d | $2.85 |  |
| 2026-05-27 | OXY | -5.08% | 1d | $19.96 |  |
| 2026-06-10 | AVGO | -5.04% | 1d | $19.28 |  |
| 2026-06-15 | EOG | -5.04% | 3d | $2.83 |  |
| 2026-06-10 | ABNB | -4.96% | 1d | $19.31 |  |
| 2026-06-11 | PEGA | -4.70% | 1d | $19.22 |  |
| 2026-06-08 | GWRE | -4.66% | 3d | $19.64 |  |
| 2026-05-27 | CVX | -4.36% | 1d | $20.00 |  |
| 2026-06-15 | CVX | -4.22% | 3d | $2.85 |  |
| 2026-06-01 | JCI | -4.05% | 3d | $19.93 |  |
| 2026-06-15 | HAL | -3.89% | 3d | $2.88 |  |
| 2026-06-10 | EME | -3.87% | 1d | $19.53 |  |
| 2026-05-27 | AZO | -3.86% | 1d | $20.22 |  |
| 2026-06-05 | INTC | -3.83% | 1d | $19.79 |  |
| 2026-05-27 | XOM | -3.73% | 1d | $20.12 |  |
| 2026-06-11 | GLW | -3.68% | 1d | $19.43 |  |
| 2026-05-28 | AMCR | -3.66% | 1d | $20.00 |  |
| 2026-06-11 | NEM | -3.54% | 1d | $19.46 |  |
| 2026-06-03 | OKTA | -3.29% | 1d | $20.42 |  |
| 2026-06-05 | LRCX | -3.25% | 1d | $19.89 |  |
| 2026-06-16 | APA | -3.22% | 1d | $7.80 |  |
| 2026-06-02 | INTC | -3.14% | 1d | $19.98 |  |
| 2026-06-03 | PANW | -3.10% | 1d | $19.50 |  |
| 2026-06-11 | MU | -2.88% | 1d | $19.65 |  |
| 2026-06-16 | VAL | -2.83% | 1d | $7.88 |  |
| 2026-06-16 | FISV | -2.80% | 1d | $7.88 |  |
| 2026-06-15 | KMI | -2.77% | 3d | $2.94 |  |
| 2026-06-16 | TPL | -2.74% | 1d | $7.83 |  |
| 2026-06-16 | TRGP | -2.71% | 1d | $7.89 |  |
| 2026-06-05 | GNRC | -2.70% | 1d | $20.01 |  |
| 2026-06-01 | AMCR | -2.69% | 3d | $20.01 |  |
| 2026-06-02 | DGX | -2.69% | 1d | $19.95 |  |
| 2026-06-11 | SNPS | -2.69% | 1d | $19.61 |  |
| 2026-06-11 | HL | -2.63% | 1d | $5.55 |  |
| 2026-06-03 | APPF | -2.62% | 1d | $20.68 |  |
| 2026-06-16 | AGCO | -2.62% | 1d | $7.83 |  |
| 2026-06-01 | FAST | -2.61% | 3d | $20.21 |  |
| 2026-06-16 | DVN | -2.54% | 1d | $7.85 |  |
| 2026-06-15 | AM | -2.53% | 3d | $2.93 |  |
| 2026-06-12 | NWE | -2.45% | 1d | $7.21 |  |
| 2026-06-01 | CASY | -2.42% | 3d | $20.19 |  |

## Execution audit (stop sells)

| Date | Ticker | Slippage% | Method |
|------|--------|-----------|--------|
| 2026-06-12 | FOUR | -1.7713 | market_fallback |
| 2026-06-15 | CHH | -0.6501 | market_fallback |
| 2026-06-16 | PBF | -0.3823 | market_fallback |
| 2026-06-15 | ED | -0.2986 | market_fallback |
| 2026-06-15 | SWX | -0.2927 | market_fallback |
| 2026-06-16 | OKE | -0.2303 | market_fallback |
| 2026-06-12 | AEE | -0.2157 | market_fallback |
| 2026-06-16 | TRGP | -0.1943 | limit_fill_position_check |
| 2026-06-16 | AGCO | -0.1908 | limit_fill_position_check |
| 2026-06-16 | GLPI | -0.1835 | limit_fill_position_check |
| 2026-06-11 | SNPS | -0.1815 | limit_fill_position_check |
| 2026-06-11 | FCX | -0.1554 | limit_fill_position_check |
| 2026-06-16 | DINO | -0.1506 | limit_fill_position_check |
| 2026-06-16 | MTDR | -0.1461 | limit_fill_position_check |
| 2026-06-15 | DUK | -0.1355 | limit_fill_position_check |
| 2026-06-16 | OVV | -0.1327 | limit_fill_position_check |
| 2026-06-16 | VAL | -0.1327 | limit_fill_position_check |
| 2026-06-11 | BILL | -0.1252 | market_fallback |
| 2026-06-15 | MUR | -0.1138 | limit_fill_position_check |
| 2026-06-12 | AM | -0.1127 | limit_fill_position_check |
| 2026-06-15 | AEE | -0.1108 | limit_fill_position_check |
| 2026-06-16 | TPL | -0.1073 | limit_fill_position_check |
| 2026-06-10 | ABNB | -0.1041 | market_fallback |
| 2026-06-11 | ORCL | -0.1014 | limit_fill_position_check |
| 2026-06-12 | ED | -0.0998 | limit_fill_position_check |
| 2026-06-12 | ETR | -0.0998 | limit_fill_position_check |
| 2026-06-15 | OVV | -0.0991 | limit_fill_position_check |
| 2026-06-16 | VTR | -0.093 | limit_fill_position_check |
| 2026-06-15 | FE | -0.0899 | limit_fill_position_check |
| 2026-06-12 | SO | -0.0896 | limit_fill_position_check |