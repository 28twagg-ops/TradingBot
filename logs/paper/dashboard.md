# 📊 Paper Bot — Performance Dashboard (PAPER TRADING)
*Updated: 2026-05-23 13:24 UTC*

> ⚠️ **Paper trading only — no real money involved.**

## Account Snapshot
| | |
|---|---|
| **Current Equity** | $99242.64 |
| **Starting Equity** | $100000.00 |
| **Total Return** | -0.76% ($-757.36) |
| **Max Drawdown** | -99.48% |
| **Current Cash** | $84579.96 |
| **Open Positions** | 0 () |
| **Last Run** | 2026-05-23 13:24:16 |

## Trade Performance
| Metric | Value |
|---|---|
| **Total Closed Trades** | 15 |
| **Win Rate** | 33.3% |
| **Avg Win** | +0.39% |
| **Avg Loss** | -2.29% |
| **Profit Factor** | 0.47x |
| **Avg Hold Days** | 0.0d |
| **Total Realised P&L** | $-65.39 |

## Tranche Feature  (new in paper bot)
| Parameter | Value |
|---|---|
| Tranche 1 (entry day) | 50% of target size |
| Tranche 2 (next day) | 50% — only if price ≤ entry×1.005 |
| Partial exit | Sell 50% at midline, ride rest to time/stop |

## Exit Reasons
| Exit | Trades | WR | Avg P&L% |
|---|---|---|---|
| `stop_loss` | 8 | 0% | -2.72% |
| `rsi_exit` | 7 | 71% | +0.11% |

## Recent Closed Trades
| Date | Ticker | Strategy | P&L% | P&L$ | Hold | Exit |
|---|---|---|---|---|---|---|
| 2026-05-23 | **SOLUSD** | `CryptoRSI` | -3.33% | $-0.91 | 0d | stop_loss (-3.3%) |
| 2026-05-23 | **ETHUSD** | `CryptoRSI` | -2.22% | $-18.81 | 0d | stop_loss (-2.2%) |
| 2026-05-23 | **BTCUSD** | `CryptoRSI` | -1.77% | $-51.71 | 0d | stop_loss (-1.8%) |
| 2026-05-23 | **AVAXUSD** | `CryptoRSI` | -4.94% | $-0.45 | 0d | stop_loss (-4.9%) |
| 2026-05-22 | **SOLUSD** | `CryptoRSI` | -1.69% | $-1.25 | 0d | stop_loss (-1.7%) |
| 2026-05-17 | **BTCUSD** | `CryptoRSI` | -1.02% | $-29.86 | 0d | rsi_exit (RSI=55) |
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