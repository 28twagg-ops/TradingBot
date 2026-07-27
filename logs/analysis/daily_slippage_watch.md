# Daily Slippage Watch
*Updated: 2026-07-27 23:30 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-07-27 | 4 | -0.68% | -0.18pp | 4/4 | -0.0380% | **OK** |
| 2026-07-23 | 2 | -0.99% | -0.49pp | 1/2 | -0.0380% | **WATCH** |
| 2026-07-22 | 1 | -0.51% | -0.01pp | 1/1 | -0.0380% | **OK** |
| 2026-07-21 | 5 | -0.92% | -0.42pp | 3/5 | -0.0380% | **WATCH** |
| 2026-07-20 | 3 | -0.59% | -0.09pp | 3/3 | -0.0380% | **OK** |
| 2026-07-17 | 3 | -0.72% | -0.22pp | 3/3 | -0.0380% | **OK** |
| 2026-07-16 | 2 | -0.66% | -0.16pp | 2/2 | -0.0380% | **OK** |
| 2026-07-14 | 3 | -0.56% | -0.06pp | 3/3 | -0.0380% | **OK** |

## Today (2026-07-27) detail

- Stop count: **4**
- Mean stop P&L: **-0.68%** (overshoot -0.18pp)
- Within -1.0%: 4/4
- Worst: ALGN -0.9%, AVB -0.8%, CMS -0.5%, EQR -0.5%
- Stop execution methods:
  - `market_urgent_full`: 4

## Historical baseline (all logs)
- Stop samples: 393
- Mean stop P&L: -1.41%
- Mean overshoot: -0.91pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
