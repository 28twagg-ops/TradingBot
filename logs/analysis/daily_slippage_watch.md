# Daily Slippage Watch
*Updated: 2026-10-16 23:12 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-10-16 | 2 | -0.73% | -0.23pp | 2/2 | -0.0303% | **OK** |
| 2026-10-15 | 1 | -1.40% | -0.90pp | 0/1 | -0.0303% | **ALERT** |
| 2026-10-14 | 2 | -0.59% | -0.09pp | 2/2 | -0.0303% | **OK** |
| 2026-10-13 | 1 | -1.21% | -0.71pp | 0/1 | -0.0303% | **ALERT** |
| 2026-10-09 | 1 | -0.51% | -0.01pp | 1/1 | -0.0303% | **OK** |
| 2026-10-08 | 1 | -0.83% | -0.33pp | 1/1 | -0.0303% | **OK** |
| 2026-10-05 | 2 | -0.57% | -0.07pp | 2/2 | -0.0303% | **OK** |

## Today (2026-10-16) detail

- Stop count: **2**
- Mean stop P&L: **-0.73%** (overshoot -0.23pp)
- Within -1.0%: 2/2
- Worst: ALLE -0.7%, AMCR -0.7%
- Stop execution methods:
  - `market_urgent_full`: 2

## Historical baseline (all logs)
- Stop samples: 513
- Mean stop P&L: -1.31%
- Mean overshoot: -0.81pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
