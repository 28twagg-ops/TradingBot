# Daily Slippage Watch
*Updated: 2026-11-23 21:27 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-11-23 | 5 | -1.13% | -0.63pp | 3/5 | -0.0286% | **WATCH** |
| 2026-11-20 | 4 | -0.67% | -0.17pp | 4/4 | -0.0286% | **OK** |
| 2026-11-19 | 4 | -1.15% | -0.65pp | 2/4 | -0.0286% | **WATCH** |
| 2026-11-18 | 2 | -0.57% | -0.08pp | 2/2 | -0.0286% | **OK** |
| 2026-11-17 | 3 | -0.57% | -0.07pp | 3/3 | -0.0286% | **OK** |
| 2026-11-13 | 3 | -0.71% | -0.21pp | 2/3 | -0.0286% | **OK** |
| 2026-11-12 | 2 | -0.56% | -0.07pp | 2/2 | -0.0286% | **OK** |
| 2026-11-10 | 2 | -0.92% | -0.42pp | 1/2 | -0.0286% | **WATCH** |

## Today (2026-11-23) detail

- Stop count: **5**
- Mean stop P&L: **-1.13%** (overshoot -0.63pp)
- Within -1.0%: 3/5
- Worst: TTWO -2.4%, EOG -1.0%, DELL -0.8%, NVDA -0.7%, MU -0.7%
- Stop execution methods:
  - `market_urgent_full`: 5

## Historical baseline (all logs)
- Stop samples: 562
- Mean stop P&L: -1.27%
- Mean overshoot: -0.77pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
