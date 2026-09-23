# Daily Slippage Watch
*Updated: 2026-09-23 22:56 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-09-23 | 2 | -1.97% | -1.47pp | 1/2 | -0.0324% | **ALERT** |
| 2026-09-22 | 2 | -1.32% | -0.82pp | 1/2 | -0.0324% | **ALERT** |
| 2026-09-21 | 3 | -0.66% | -0.16pp | 3/3 | -0.0324% | **OK** |
| 2026-09-18 | 2 | -1.53% | -1.03pp | 1/2 | -0.0324% | **ALERT** |
| 2026-09-17 | 2 | -0.69% | -0.19pp | 2/2 | -0.0324% | **OK** |
| 2026-09-16 | 5 | -0.62% | -0.12pp | 5/5 | -0.0324% | **OK** |
| 2026-09-15 | 4 | -0.85% | -0.35pp | 3/4 | -0.0324% | **OK** |
| 2026-09-14 | 1 | -0.58% | -0.08pp | 1/1 | -0.0324% | **OK** |
| 2026-09-11 | 1 | -0.73% | -0.23pp | 1/1 | -0.0324% | **OK** |
| 2026-09-10 | 4 | -0.97% | -0.47pp | 2/4 | -0.0324% | **WATCH** |

## Today (2026-09-23) detail

- Stop count: **2**
- Mean stop P&L: **-1.97%** (overshoot -1.47pp)
- Within -1.0%: 1/2
- Worst: CCL -3.2%, ADM -0.8%
- Stop execution methods:
  - `market_urgent_full`: 2

## Historical baseline (all logs)
- Stop samples: 491
- Mean stop P&L: -1.34%
- Mean overshoot: -0.84pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
