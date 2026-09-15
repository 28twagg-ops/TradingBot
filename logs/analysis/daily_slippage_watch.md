# Daily Slippage Watch
*Updated: 2026-09-15 14:04 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-09-15 | 2 | -1.06% | -0.57pp | 1/2 | -0.0338% | **WATCH** |
| 2026-09-14 | 1 | -0.58% | -0.08pp | 1/1 | -0.0338% | **OK** |
| 2026-09-11 | 1 | -0.73% | -0.23pp | 1/1 | -0.0338% | **OK** |
| 2026-09-10 | 4 | -0.97% | -0.47pp | 2/4 | -0.0338% | **WATCH** |
| 2026-09-09 | 3 | -0.88% | -0.38pp | 2/3 | -0.0338% | **OK** |
| 2026-09-08 | 3 | -0.55% | -0.05pp | 3/3 | -0.0338% | **OK** |
| 2026-09-04 | 1 | -0.61% | -0.11pp | 1/1 | -0.0338% | **OK** |
| 2026-09-03 | 1 | -0.70% | -0.20pp | 1/1 | -0.0338% | **OK** |
| 2026-09-02 | 3 | -1.34% | -0.84pp | 2/3 | -0.0338% | **ALERT** |

## Today (2026-09-15) detail

- Stop count: **2**
- Mean stop P&L: **-1.06%** (overshoot -0.57pp)
- Within -1.0%: 1/2
- Worst: ROL -1.6%, AAL -0.5%
- Stop execution methods:
  - `market_urgent_full`: 2

## Historical baseline (all logs)
- Stop samples: 473
- Mean stop P&L: -1.35%
- Mean overshoot: -0.85pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
