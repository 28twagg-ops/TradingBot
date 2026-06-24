# Daily Slippage Watch
*Updated: 2026-06-24 14:00 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-06-24 | 17 | -1.74% | -1.24pp | 5/17 | -0.0470% | **ALERT** |
| 2026-06-23 | 2 | -0.85% | -0.36pp | 2/2 | -0.0470% | **OK** |
| 2026-06-22 | 71 | -0.87% | -0.37pp | 53/71 | -0.0470% | **OK** |
| 2026-06-18 | 4 | -0.75% | -0.25pp | 3/4 | -0.0470% | **OK** |
| 2026-06-17 | 34 | -0.83% | -0.33pp | 26/34 | -0.0470% | **OK** |
| 2026-06-16 | 30 | -1.56% | -1.06pp | 9/30 | -0.0436% | **ALERT** |
| 2026-06-15 | 27 | -2.03% | -1.53pp | 9/27 | -0.0470% | **ALERT** |
| 2026-06-12 | 27 | -1.39% | -0.89pp | 10/27 | -0.0408% | **ALERT** |
| 2026-06-11 | 12 | -4.16% | -3.66pp | 1/12 | -0.0393% | **ALERT** |

## Today (2026-06-24) detail

- Stop count: **17**
- Mean stop P&L: **-1.74%** (overshoot -1.24pp)
- Within -1.0%: 5/17
- Worst: FLS -4.1%, AMKR -3.6%, SYNA -3.4%, PBF -2.5%, COIN -2.3%
- Stop execution methods:
  - `market_urgent_full`: 17

## Historical baseline (all logs)
- Stop samples: 339
- Mean stop P&L: -1.50%
- Mean overshoot: -1.00pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
