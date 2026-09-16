# Daily Slippage Watch
*Updated: 2026-09-16 19:06 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-09-16 | 3 | -0.65% | -0.15pp | 3/3 | -0.0334% | **OK** |
| 2026-09-15 | 4 | -0.85% | -0.35pp | 3/4 | -0.0334% | **OK** |
| 2026-09-14 | 1 | -0.58% | -0.08pp | 1/1 | -0.0334% | **OK** |
| 2026-09-11 | 1 | -0.73% | -0.23pp | 1/1 | -0.0334% | **OK** |
| 2026-09-10 | 4 | -0.97% | -0.47pp | 2/4 | -0.0334% | **WATCH** |
| 2026-09-09 | 3 | -0.88% | -0.38pp | 2/3 | -0.0334% | **OK** |
| 2026-09-08 | 3 | -0.55% | -0.05pp | 3/3 | -0.0334% | **OK** |
| 2026-09-04 | 1 | -0.61% | -0.11pp | 1/1 | -0.0334% | **OK** |
| 2026-09-03 | 1 | -0.70% | -0.20pp | 1/1 | -0.0334% | **OK** |

## Today (2026-09-16) detail

- Stop count: **3**
- Mean stop P&L: **-0.65%** (overshoot -0.15pp)
- Within -1.0%: 3/3
- Worst: ALLE -0.7%, AAL -0.6%, ALL -0.6%
- Stop execution methods:
  - `market_urgent_full`: 2
  - `limit_fill_position_check_full`: 1

## Historical baseline (all logs)
- Stop samples: 478
- Mean stop P&L: -1.34%
- Mean overshoot: -0.84pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
