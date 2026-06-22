# Daily Slippage Watch
*Updated: 2026-06-22 13:36 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-06-22 | 17 | -0.85% | -0.35pp | 12/17 | -0.0460% | **OK** |
| 2026-06-18 | 4 | -0.75% | -0.25pp | 3/4 | -0.0460% | **OK** |
| 2026-06-17 | 34 | -0.83% | -0.33pp | 26/34 | -0.0460% | **OK** |
| 2026-06-16 | 30 | -1.56% | -1.06pp | 9/30 | -0.0419% | **ALERT** |
| 2026-06-15 | 27 | -2.03% | -1.53pp | 9/27 | -0.0460% | **ALERT** |
| 2026-06-12 | 27 | -1.39% | -0.89pp | 10/27 | -0.0386% | **ALERT** |
| 2026-06-11 | 12 | -4.16% | -3.66pp | 1/12 | -0.0368% | **ALERT** |
| 2026-06-10 | 8 | -3.63% | -3.13pp | 2/8 | -0.0432% | **ALERT** |
| 2026-06-09 | 17 | -1.04% | -0.54pp | 11/17 | -0.0460% | **WATCH** |

## Today (2026-06-22) detail

- Stop count: **17**
- Mean stop P&L: **-0.85%** (overshoot -0.35pp)
- Within -1.0%: 12/17
- Worst: GEF -1.7%, FOUR -1.3%, ALB -1.3%, POOL -1.1%, SIGI -1.0%
- Stop execution methods:
  - `market_urgent_full`: 17

## Historical baseline (all logs)
- Stop samples: 266
- Mean stop P&L: -1.62%
- Mean overshoot: -1.12pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
