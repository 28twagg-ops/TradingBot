# Daily Slippage Watch
*Updated: 2026-09-01 13:49 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-09-01 | 2 | -0.91% | -0.41pp | 1/2 | -0.0353% | **WATCH** |
| 2026-08-31 | 5 | -1.05% | -0.55pp | 3/5 | -0.0353% | **WATCH** |
| 2026-08-28 | 2 | -0.75% | -0.25pp | 2/2 | -0.0353% | **OK** |
| 2026-08-27 | 2 | -0.55% | -0.05pp | 2/2 | -0.0353% | **OK** |
| 2026-08-26 | 3 | -0.77% | -0.27pp | 2/3 | -0.0353% | **OK** |
| 2026-08-25 | 3 | -0.67% | -0.17pp | 3/3 | -0.0353% | **OK** |
| 2026-08-24 | 1 | -0.59% | -0.09pp | 1/1 | -0.0353% | **OK** |
| 2026-08-21 | 1 | -0.65% | -0.15pp | 1/1 | -0.0353% | **OK** |
| 2026-08-19 | 1 | -0.54% | -0.04pp | 1/1 | -0.0353% | **OK** |

## Today (2026-09-01) detail

- Stop count: **2**
- Mean stop P&L: **-0.91%** (overshoot -0.41pp)
- Within -1.0%: 1/2
- Worst: NVT -1.3%, DLR -0.5%
- Stop execution methods:
  - `market_urgent_full`: 2

## Historical baseline (all logs)
- Stop samples: 453
- Mean stop P&L: -1.37%
- Mean overshoot: -0.87pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
