# 📊 Paper Bot — Performance Dashboard (PAPER TRADING)
*Updated: 2026-05-17 17:05 UTC*

> ⚠️ **Paper trading only — no real money involved.**

## Account Snapshot
| | |
|---|---|
| **Current Equity** | $99571.31 |
| **Starting Equity** | $100000.00 |
| **Total Return** | -0.43% ($-428.69) |
| **Max Drawdown** | -99.48% |
| **Current Cash** | $93761.49 |
| **Open Positions** | 0 () |
| **Last Run** | 2026-05-17 17:05:07 |

## Trade Performance
| Metric | Value |
|---|---|
| **Total Closed Trades** | 9 |
| **Win Rate** | 55.6% |
| **Avg Win** | +0.39% |
| **Avg Loss** | -1.98% |
| **Profit Factor** | 2.94x |
| **Avg Hold Days** | 0.0d |
| **Total Realised P&L** | $+37.60 |

## Tranche Feature  (new in paper bot)
| Parameter | Value |
|---|---|
| Tranche 1 (entry day) | 50% of target size |
| Tranche 2 (next day) | 50% — only if price ≤ entry×1.005 |
| Partial exit | Sell 50% at midline, ride rest to time/stop |

## Exit Reasons
| Exit | Trades | WR | Avg P&L% |
|---|---|---|---|
| `rsi_exit` | 6 | 83% | +0.30% |
| `stop_loss` | 3 | 0% | -2.59% |

## Recent Closed Trades
| Date | Ticker | Strategy | P&L% | P&L$ | Hold | Exit |
|---|---|---|---|---|---|---|
| 2026-05-17 | **LINKUSD** | `CryptoRSI` | +0.55% | $+16.05 | 0d | rsi_exit (RSI=55) |
| 2026-05-17 | **ETHUSD** | `CryptoRSI` | +0.40% | $+11.67 | 0d | rsi_exit (RSI=60) |
| 2026-05-16 | **LINKUSD** | `CryptoRSI` | -3.76% | $-0.09 | 0d | stop_loss (-3.8%) |
| 2026-05-16 | **ETHUSD** | `CryptoRSI` | -1.97% | $-14.00 | 0d | stop_loss (-2.0%) |
| 2026-05-10 | **BTCUSD** | `CryptoRSI` | +0.18% | $+5.25 | 0d | rsi_exit (RSI=68) |
| 2026-05-10 | **SOLUSD** | `CryptoRSI` | +0.47% | $+13.63 | 0d | rsi_exit (RSI=63) |
| 2026-05-10 | **LINKUSD** | `CryptoRSI` | -0.15% | $-4.35 | 0d | rsi_exit (RSI=58) |
| 2026-05-10 | **AVAXUSD** | `CryptoRSI` | +0.35% | $+10.38 | 0d | rsi_exit (RSI=64) |
| 2026-05-06 | **ACGL** | `Pullback50` | -2.04% | $-0.94 | 0d | stop_loss (-2.0%) |

---
*Auto-generated. Paper account only.*