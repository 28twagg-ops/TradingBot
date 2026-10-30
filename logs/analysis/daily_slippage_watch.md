# Daily Slippage Watch
*Updated: 2026-10-30 20:22 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-10-30 | 1 | -0.54% | -0.04pp | 1/1 | -0.0296% | **OK** |
| 2026-10-29 | 1 | -1.44% | -0.94pp | 0/1 | -0.0296% | **ALERT** |
| 2026-10-28 | 2 | -0.71% | -0.21pp | 2/2 | -0.0296% | **OK** |
| 2026-10-27 | 2 | -0.53% | -0.03pp | 2/2 | -0.0296% | **OK** |
| 2026-10-23 | 3 | -0.84% | -0.34pp | 2/3 | -0.0296% | **OK** |
| 2026-10-22 | 1 | -0.60% | -0.10pp | 1/1 | -0.0296% | **OK** |
| 2026-10-21 | 3 | -0.62% | -0.12pp | 3/3 | -0.0296% | **OK** |
| 2026-10-19 | 3 | -0.77% | -0.27pp | 2/3 | -0.0296% | **OK** |

## Today (2026-10-30) detail

- Stop count: **1**
- Mean stop P&L: **-0.54%** (overshoot -0.04pp)
- Within -1.0%: 1/1
- Worst: ADBE -0.5%
- Stop execution methods:
  - `market_urgent_full`: 1

## Historical baseline (all logs)
- Stop samples: 529
- Mean stop P&L: -1.29%
- Mean overshoot: -0.79pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
