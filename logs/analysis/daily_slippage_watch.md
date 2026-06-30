# Daily Slippage Watch
*Updated: 2026-06-30 23:20 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-06-30 | 1 | -0.95% | -0.45pp | 1/1 | -0.0433% | **WATCH** |
| 2026-06-26 | 6 | -1.37% | -0.87pp | 4/6 | -0.0433% | **ALERT** |
| 2026-06-25 | 2 | -0.67% | -0.17pp | 2/2 | -0.0433% | **OK** |
| 2026-06-24 | 24 | -1.48% | -0.98pp | 11/24 | -0.0433% | **ALERT** |
| 2026-06-23 | 2 | -0.85% | -0.36pp | 2/2 | -0.0433% | **OK** |
| 2026-06-22 | 71 | -0.87% | -0.37pp | 53/71 | -0.0433% | **OK** |
| 2026-06-18 | 4 | -0.75% | -0.25pp | 3/4 | -0.0433% | **OK** |
| 2026-06-17 | 34 | -0.83% | -0.33pp | 26/34 | -0.0433% | **OK** |

## Today (2026-06-30) detail

- Stop count: **1**
- Mean stop P&L: **-0.95%** (overshoot -0.45pp)
- Within -1.0%: 1/1
- Worst: CPAY -0.9%
- Stop execution methods:
  - `market_urgent_full`: 1

## Historical baseline (all logs)
- Stop samples: 355
- Mean stop P&L: -1.48%
- Mean overshoot: -0.98pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
