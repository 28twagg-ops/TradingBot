# Daily Slippage Watch
*Updated: 2026-06-22 18:30 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-06-22 | 67 | -0.89% | -0.39pp | 49/67 | -0.0430% | **OK** |
| 2026-06-18 | 4 | -0.75% | -0.25pp | 3/4 | -0.0430% | **OK** |
| 2026-06-17 | 34 | -0.83% | -0.33pp | 26/34 | -0.0430% | **OK** |
| 2026-06-16 | 30 | -1.56% | -1.06pp | 9/30 | -0.0397% | **ALERT** |
| 2026-06-15 | 27 | -2.03% | -1.53pp | 9/27 | -0.0430% | **ALERT** |
| 2026-06-12 | 27 | -1.39% | -0.89pp | 10/27 | -0.0370% | **ALERT** |
| 2026-06-11 | 12 | -4.16% | -3.66pp | 1/12 | -0.0355% | **ALERT** |
| 2026-06-10 | 8 | -3.63% | -3.13pp | 2/8 | -0.0408% | **ALERT** |
| 2026-06-09 | 17 | -1.04% | -0.54pp | 11/17 | -0.0430% | **WATCH** |

## Today (2026-06-22) detail

- Stop count: **67**
- Mean stop P&L: **-0.89%** (overshoot -0.39pp)
- Within -1.0%: 49/67
- Worst: DPZ -4.1%, AVGO -3.4%, GEF -1.7%, CW -1.5%, DT -1.3%
- Stop execution methods:
  - `market_urgent_full`: 67

## Historical baseline (all logs)
- Stop samples: 316
- Mean stop P&L: -1.50%
- Mean overshoot: -1.00pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
