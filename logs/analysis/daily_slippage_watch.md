# Daily Slippage Watch
*Updated: 2026-08-26 15:03 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-08-26 | 2 | -0.84% | -0.34pp | 1/2 | -0.0362% | **OK** |
| 2026-08-25 | 3 | -0.67% | -0.17pp | 3/3 | -0.0362% | **OK** |
| 2026-08-24 | 1 | -0.59% | -0.09pp | 1/1 | -0.0362% | **OK** |
| 2026-08-21 | 1 | -0.65% | -0.15pp | 1/1 | -0.0362% | **OK** |
| 2026-08-19 | 1 | -0.54% | -0.04pp | 1/1 | -0.0362% | **OK** |
| 2026-08-18 | 4 | -0.54% | -0.04pp | 4/4 | -0.0362% | **OK** |
| 2026-08-17 | 2 | -0.54% | -0.04pp | 2/2 | -0.0362% | **OK** |
| 2026-08-14 | 1 | -0.56% | -0.06pp | 1/1 | -0.0362% | **OK** |

## Today (2026-08-26) detail

- Stop count: **2**
- Mean stop P&L: **-0.84%** (overshoot -0.34pp)
- Within -1.0%: 1/2
- Worst: NKE -1.2%, AME -0.5%
- Stop execution methods:
  - `market_urgent_full`: 2

## Historical baseline (all logs)
- Stop samples: 441
- Mean stop P&L: -1.38%
- Mean overshoot: -0.88pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
