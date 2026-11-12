# Daily Slippage Watch
*Updated: 2026-11-12 21:12 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-11-12 | 2 | -0.56% | -0.07pp | 2/2 | -0.0293% | **OK** |
| 2026-11-10 | 2 | -0.92% | -0.42pp | 1/2 | -0.0293% | **WATCH** |
| 2026-11-05 | 5 | -2.02% | -1.52pp | 4/5 | -0.0293% | **ALERT** |
| 2026-11-03 | 1 | -0.70% | -0.20pp | 1/1 | -0.0293% | **OK** |
| 2026-11-02 | 2 | -0.35% | +0.15pp | 2/2 | -0.0293% | **OK** |
| 2026-10-30 | 1 | -0.54% | -0.04pp | 1/1 | -0.0293% | **OK** |

## Today (2026-11-12) detail

- Stop count: **2**
- Mean stop P&L: **-0.56%** (overshoot -0.07pp)
- Within -1.0%: 2/2
- Worst: MSFT -0.6%, SMCI -0.5%
- Stop execution methods:
  - `market_urgent_full`: 2

## Historical baseline (all logs)
- Stop samples: 541
- Mean stop P&L: -1.29%
- Mean overshoot: -0.79pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
