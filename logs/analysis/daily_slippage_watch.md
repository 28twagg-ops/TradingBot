# Daily Slippage Watch
*Updated: 2026-11-20 16:48 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-11-20 | 2 | -0.67% | -0.17pp | 2/2 | -0.0287% | **OK** |
| 2026-11-19 | 4 | -1.15% | -0.65pp | 2/4 | -0.0287% | **WATCH** |
| 2026-11-18 | 2 | -0.57% | -0.08pp | 2/2 | -0.0287% | **OK** |
| 2026-11-17 | 3 | -0.57% | -0.07pp | 3/3 | -0.0287% | **OK** |
| 2026-11-13 | 3 | -0.71% | -0.21pp | 2/3 | -0.0287% | **OK** |
| 2026-11-12 | 2 | -0.56% | -0.07pp | 2/2 | -0.0287% | **OK** |
| 2026-11-10 | 2 | -0.92% | -0.42pp | 1/2 | -0.0287% | **WATCH** |

## Today (2026-11-20) detail

- Stop count: **2**
- Mean stop P&L: **-0.67%** (overshoot -0.17pp)
- Within -1.0%: 2/2
- Worst: ARES -0.8%, EOG -0.6%
- Stop execution methods:
  - `market_urgent_full`: 2

## Historical baseline (all logs)
- Stop samples: 555
- Mean stop P&L: -1.28%
- Mean overshoot: -0.78pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
