# Daily Slippage Watch
*Updated: 2026-10-27 22:37 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-10-27 | 2 | -0.53% | -0.03pp | 2/2 | -0.0297% | **OK** |
| 2026-10-23 | 3 | -0.84% | -0.34pp | 2/3 | -0.0297% | **OK** |
| 2026-10-22 | 1 | -0.60% | -0.10pp | 1/1 | -0.0297% | **OK** |
| 2026-10-21 | 3 | -0.62% | -0.12pp | 3/3 | -0.0297% | **OK** |
| 2026-10-19 | 3 | -0.77% | -0.27pp | 2/3 | -0.0297% | **OK** |
| 2026-10-16 | 2 | -0.73% | -0.23pp | 2/2 | -0.0297% | **OK** |
| 2026-10-15 | 1 | -1.40% | -0.90pp | 0/1 | -0.0297% | **ALERT** |
| 2026-10-14 | 2 | -0.59% | -0.09pp | 2/2 | -0.0297% | **OK** |

## Today (2026-10-27) detail

- Stop count: **2**
- Mean stop P&L: **-0.53%** (overshoot -0.03pp)
- Within -1.0%: 2/2
- Worst: LFUS -0.6%, CPAY -0.5%
- Stop execution methods:
  - `market_urgent_full`: 2

## Historical baseline (all logs)
- Stop samples: 525
- Mean stop P&L: -1.30%
- Mean overshoot: -0.80pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
