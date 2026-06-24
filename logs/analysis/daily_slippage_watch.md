# Daily Slippage Watch
*Updated: 2026-06-24 15:15 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-06-24 | 18 | -1.69% | -1.19pp | 6/18 | -0.0468% | **ALERT** |
| 2026-06-23 | 2 | -0.85% | -0.36pp | 2/2 | -0.0468% | **OK** |
| 2026-06-22 | 71 | -0.87% | -0.37pp | 53/71 | -0.0468% | **OK** |
| 2026-06-18 | 4 | -0.75% | -0.25pp | 3/4 | -0.0468% | **OK** |
| 2026-06-17 | 34 | -0.83% | -0.33pp | 26/34 | -0.0468% | **OK** |
| 2026-06-16 | 30 | -1.56% | -1.06pp | 9/30 | -0.0435% | **ALERT** |
| 2026-06-15 | 27 | -2.03% | -1.53pp | 9/27 | -0.0468% | **ALERT** |
| 2026-06-12 | 27 | -1.39% | -0.89pp | 10/27 | -0.0407% | **ALERT** |
| 2026-06-11 | 12 | -4.16% | -3.66pp | 1/12 | -0.0392% | **ALERT** |

## Today (2026-06-24) detail

- Stop count: **18**
- Mean stop P&L: **-1.69%** (overshoot -1.19pp)
- Within -1.0%: 6/18
- Worst: FLS -4.1%, AMKR -3.6%, SYNA -3.4%, PBF -2.5%, COIN -2.3%
- Stop execution methods:
  - `market_urgent_full`: 18

## Historical baseline (all logs)
- Stop samples: 340
- Mean stop P&L: -1.50%
- Mean overshoot: -1.00pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
