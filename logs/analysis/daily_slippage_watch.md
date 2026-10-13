# Daily Slippage Watch
*Updated: 2026-10-13 18:52 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-10-13 | 1 | -1.21% | -0.71pp | 0/1 | -0.0308% | **ALERT** |
| 2026-10-09 | 1 | -0.51% | -0.01pp | 1/1 | -0.0308% | **OK** |
| 2026-10-08 | 1 | -0.83% | -0.33pp | 1/1 | -0.0308% | **OK** |
| 2026-10-05 | 2 | -0.57% | -0.07pp | 2/2 | -0.0308% | **OK** |
| 2026-10-02 | 2 | -0.78% | -0.28pp | 1/2 | -0.0308% | **OK** |
| 2026-10-01 | 1 | -0.54% | -0.04pp | 1/1 | -0.0308% | **OK** |
| 2026-09-30 | 2 | -0.53% | -0.03pp | 2/2 | -0.0308% | **OK** |

## Today (2026-10-13) detail

- Stop count: **1**
- Mean stop P&L: **-1.21%** (overshoot -0.71pp)
- Within -1.0%: 0/1
- Worst: FICO -1.2%
- Stop execution methods:
  - `market_urgent_full`: 1

## Historical baseline (all logs)
- Stop samples: 508
- Mean stop P&L: -1.32%
- Mean overshoot: -0.82pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
