# Preliminary Correlation Study — Verdict (Task 2.0)

_PRELIMINARY - based on yfinance EOD data, confirm with Alpaca 1-min data once collected_

## STATUS: VERDICT B (PRELIMINARY)

VERDICT B — WEAK/CONDITIONAL (preliminary). Outperformance only at specific horizons/strengths (significant horizons: ['EOD']; net P&L positive: True). -> Proceed but narrow Phase 4 to those conditions.

## Interpretation note

The equity bot is long-only mean-reversion; every BUY is a bullish thesis analysed as an ATM CALL. No GapUp/short signals exist, so PUT analysis is N/A.

## Inputs

- Signals: 358 with options data (GapDown subset: 64)
- Signal types: {'VolumeSpike': 4, 'MomReversal': 5, 'Pullback50': 280, 'GapDown': 64, 'RSIRecovery': 5}
- Date range: 2026-05-25..2026-06-16
- Controls: 1074 (3/signal, non-signal names same day)
- BS: r=0.05, T=7d, sigma=max(realized_vol_30d, 0.15); adversarial entry x1.05, exit x0.95, fee $1.3

## Q1/Q2 — signal vs control CALL return by horizon

| Horizon | Signal mean | Control mean | Diff | p-value | n_sig | n_ctl |
|---|---|---|---|---|---|---|
| EOD * | +33.25% | +5.75% | +27.50% | 0.000 | 358 | 1074 |
| 1day | +0.64% | +4.87% | -4.23% | 0.300 | 358 | 1074 |
| 3day | +10.75% | +12.24% | -1.49% | 0.853 | 358 | 1074 |
| 5day | +17.85% | +20.04% | -2.19% | 0.815 | 358 | 1074 |

Best (highest signal mean) horizon: **EOD** (+33.25%).  (* = diff>0 and p<0.1)

## Q3 — approximate IV-crush impact (APPROXIMATE — not reliable without real IV)

- EOD: +0.00% drag
- 1day: -15.09% drag
- 3day: -9.82% drag
- 5day: -4.97% drag

## Q5 — net P&L per signal after adversarial costs ($/contract)

| Horizon | Signal net P&L | Control net P&L |
|---|---|---|
| EOD | $+115.48 | $+4.95 |
| 1day | $+20.37 | $-15.01 |
| 3day | $+76.59 | $+37.32 |
| 5day | $+99.41 | $+89.58 |

## Q4 — strong (gap<-2%) vs weak (-2%..-0.5%) call returns

| Horizon | Strong | Weak | Diff | n_strong | n_weak |
|---|---|---|---|---|---|
| EOD | +47.01% | +15.34% | +31.67% | 68 | 35 |
| 1day | +26.26% | -2.41% | +28.67% | 68 | 35 |
| 3day | +25.34% | +10.28% | +15.05% | 68 | 35 |
| 5day | +16.97% | +7.58% | +9.39% | 68 | 35 |

## Sanity checks

- Sanity 1 (dip-buy stock return positive): 1d=-0.16%, 3d=+0.20%
- Sanity 1b (GapDown gap_pct negative): -4.79%
- Sanity 3 (control ~0 drift): +0.09%

## Limitations

- yfinance EOD only; option prices are Black-Scholes RECONSTRUCTED.
- Realized vol used as IV proxy; no real historical IV surface.
- IV-crush is a crude 20% haircut assumption.
- Short ~3-week signal window; market-regime bias possible.
- EOD horizon uses the stock's open->close move for BOTH signal and control (symmetric, fair comparison) rather than the bot's actual intraday entry->close; treat the EOD magnitude as indicative, not exact.
- EOD call returns are large because 7-day ATM options are highly leveraged (a ~1.5-2% favorable intraday move ~= 30%+ on premium); this amplifies BOTH the edge and the risk and must be confirmed on real 1-min option quotes before being trusted.
- KEY READ: edge is concentrated INTRADAY (EOD) and the multi-day horizons show no signal-vs-control advantage; overnight IV crush (-15% at 1day) erodes it. The morning bot's same-day entry/EOD-close design aligns with where the (preliminary) edge appears.
- PRELIMINARY - based on yfinance EOD data, confirm with Alpaca 1-min data once collected