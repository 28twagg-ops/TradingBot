# Daily Slippage Watch
*Updated: 2026-08-28 14:07 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-08-28 | 1 | -0.98% | -0.48pp | 1/1 | -0.0357% | **WATCH** |
| 2026-08-27 | 2 | -0.55% | -0.05pp | 2/2 | -0.0357% | **OK** |
| 2026-08-26 | 3 | -0.77% | -0.27pp | 2/3 | -0.0357% | **OK** |
| 2026-08-25 | 3 | -0.67% | -0.17pp | 3/3 | -0.0357% | **OK** |
| 2026-08-24 | 1 | -0.59% | -0.09pp | 1/1 | -0.0357% | **OK** |
| 2026-08-21 | 1 | -0.65% | -0.15pp | 1/1 | -0.0357% | **OK** |
| 2026-08-19 | 1 | -0.54% | -0.04pp | 1/1 | -0.0357% | **OK** |
| 2026-08-18 | 4 | -0.54% | -0.04pp | 4/4 | -0.0357% | **OK** |
| 2026-08-17 | 2 | -0.54% | -0.04pp | 2/2 | -0.0357% | **OK** |

## Today (2026-08-28) detail

- Stop count: **1**
- Mean stop P&L: **-0.98%** (overshoot -0.48pp)
- Within -1.0%: 1/1
- Worst: WSO -1.0%
- Stop execution methods:
  - `market_urgent_full`: 1

## Historical baseline (all logs)
- Stop samples: 445
- Mean stop P&L: -1.38%
- Mean overshoot: -0.88pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
