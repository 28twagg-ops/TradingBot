# Daily Slippage Watch
*Updated: 2026-07-27 17:55 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-07-27 | 2 | -0.71% | -0.21pp | 2/2 | -0.0382% | **OK** |
| 2026-07-23 | 2 | -0.99% | -0.49pp | 1/2 | -0.0382% | **WATCH** |
| 2026-07-22 | 1 | -0.51% | -0.01pp | 1/1 | -0.0382% | **OK** |
| 2026-07-21 | 5 | -0.92% | -0.42pp | 3/5 | -0.0382% | **WATCH** |
| 2026-07-20 | 3 | -0.59% | -0.09pp | 3/3 | -0.0382% | **OK** |
| 2026-07-17 | 3 | -0.72% | -0.22pp | 3/3 | -0.0382% | **OK** |
| 2026-07-16 | 2 | -0.66% | -0.16pp | 2/2 | -0.0382% | **OK** |
| 2026-07-14 | 3 | -0.56% | -0.06pp | 3/3 | -0.0382% | **OK** |

## Today (2026-07-27) detail

- Stop count: **2**
- Mean stop P&L: **-0.71%** (overshoot -0.21pp)
- Within -1.0%: 2/2
- Worst: ALGN -0.9%, CMS -0.5%
- Stop execution methods:
  - `market_urgent_full`: 2

## Historical baseline (all logs)
- Stop samples: 391
- Mean stop P&L: -1.42%
- Mean overshoot: -0.92pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
