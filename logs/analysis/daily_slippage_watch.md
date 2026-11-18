# Daily Slippage Watch
*Updated: 2026-11-18 00:12 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-11-17 | 3 | -0.57% | -0.07pp | 3/3 | -0.0292% | **OK** |
| 2026-11-13 | 3 | -0.71% | -0.21pp | 2/3 | -0.0292% | **OK** |
| 2026-11-12 | 2 | -0.56% | -0.07pp | 2/2 | -0.0292% | **OK** |
| 2026-11-10 | 2 | -0.92% | -0.42pp | 1/2 | -0.0292% | **WATCH** |
| 2026-11-05 | 5 | -2.02% | -1.52pp | 4/5 | -0.0292% | **ALERT** |

## Today (2026-11-18) detail

_No stop losses recorded today._

## Historical baseline (all logs)
- Stop samples: 547
- Mean stop P&L: -1.28%
- Mean overshoot: -0.78pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
