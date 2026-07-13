# Daily Slippage Watch
*Updated: 2026-07-13 14:46 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-07-13 | 2 | -0.69% | -0.19pp | 2/2 | -0.0413% | **OK** |
| 2026-07-10 | 1 | -0.54% | -0.04pp | 1/1 | -0.0413% | **OK** |
| 2026-07-08 | 2 | -1.44% | -0.94pp | 1/2 | -0.0413% | **ALERT** |
| 2026-07-07 | 2 | -1.92% | -1.42pp | 0/2 | -0.0413% | **ALERT** |
| 2026-07-02 | 3 | -0.54% | -0.04pp | 3/3 | -0.0413% | **OK** |
| 2026-07-01 | 1 | -0.56% | -0.06pp | 1/1 | -0.0413% | **OK** |
| 2026-06-30 | 1 | -0.95% | -0.45pp | 1/1 | -0.0413% | **WATCH** |

## Today (2026-07-13) detail

- Stop count: **2**
- Mean stop P&L: **-0.69%** (overshoot -0.19pp)
- Within -1.0%: 2/2
- Worst: CMI -0.8%, DOV -0.6%
- Stop execution methods:
  - `market_urgent_full`: 2

## Historical baseline (all logs)
- Stop samples: 366
- Mean stop P&L: -1.46%
- Mean overshoot: -0.96pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
