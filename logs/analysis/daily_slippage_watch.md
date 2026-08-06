# Daily Slippage Watch
*Updated: 2026-08-06 20:31 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-08-06 | 1 | -0.71% | -0.21pp | 1/1 | -0.0370% | **OK** |
| 2026-08-05 | 2 | -0.66% | -0.16pp | 2/2 | -0.0370% | **OK** |
| 2026-08-04 | 1 | -0.66% | -0.16pp | 1/1 | -0.0370% | **OK** |
| 2026-08-03 | 5 | -0.57% | -0.07pp | 5/5 | -0.0370% | **OK** |
| 2026-07-31 | 3 | -0.57% | -0.07pp | 3/3 | -0.0370% | **OK** |
| 2026-07-30 | 4 | -2.35% | -1.85pp | 0/4 | -0.0370% | **ALERT** |
| 2026-07-29 | 4 | -4.71% | -4.21pp | 3/4 | -0.0370% | **ALERT** |
| 2026-07-28 | 2 | -0.59% | -0.09pp | 2/2 | -0.0370% | **OK** |
| 2026-07-27 | 4 | -0.68% | -0.18pp | 4/4 | -0.0370% | **OK** |

## Today (2026-08-06) detail

- Stop count: **1**
- Mean stop P&L: **-0.71%** (overshoot -0.21pp)
- Within -1.0%: 1/1
- Worst: GEV -0.7%
- Stop execution methods:
  - `market_urgent_full`: 1

## Historical baseline (all logs)
- Stop samples: 415
- Mean stop P&L: -1.43%
- Mean overshoot: -0.93pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
