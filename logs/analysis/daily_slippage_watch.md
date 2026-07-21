# Daily Slippage Watch
*Updated: 2026-07-21 13:55 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-07-21 | 3 | -0.78% | -0.28pp | 2/3 | -0.0389% | **OK** |
| 2026-07-20 | 3 | -0.59% | -0.09pp | 3/3 | -0.0389% | **OK** |
| 2026-07-17 | 3 | -0.72% | -0.22pp | 3/3 | -0.0389% | **OK** |
| 2026-07-16 | 2 | -0.66% | -0.16pp | 2/2 | -0.0389% | **OK** |
| 2026-07-14 | 3 | -0.56% | -0.06pp | 3/3 | -0.0389% | **OK** |
| 2026-07-13 | 6 | -0.64% | -0.14pp | 6/6 | -0.0389% | **OK** |
| 2026-07-10 | 1 | -0.54% | -0.04pp | 1/1 | -0.0389% | **OK** |
| 2026-07-08 | 2 | -1.44% | -0.94pp | 1/2 | -0.0389% | **ALERT** |

## Today (2026-07-21) detail

- Stop count: **3**
- Mean stop P&L: **-0.78%** (overshoot -0.28pp)
- Within -1.0%: 2/3
- Worst: WMB -1.1%, IEX -0.7%, MAA -0.6%
- Stop execution methods:
  - `market_urgent_full`: 3

## Historical baseline (all logs)
- Stop samples: 384
- Mean stop P&L: -1.43%
- Mean overshoot: -0.93pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
