# 📊 Paper Bot — Performance Dashboard (PAPER TRADING)
*Updated: 2026-05-29 22:20 UTC*

> ⚠️ **Paper trading only — no real money involved.**

## Account Snapshot
| | |
|---|---|
| **Current Equity** | $99367.26 |
| **Starting Equity** | $100000.00 |
| **Total Return** | -0.63% ($-632.74) |
| **Max Drawdown** | -99.48% |
| **Current Cash** | $99367.26 |
| **Open Positions** | 0 () |
| **Last Run** | 2026-05-29 22:20:13 |

## Trade Performance
| Metric | Value |
|---|---|
| **Total Closed Trades** | 22 |
| **Win Rate** | 45.5% |
| **Avg Win** | +2.33% |
| **Avg Loss** | -2.22% |
| **Profit Factor** | 5.52x |
| **Avg Hold Days** | 0.0d |
| **Total Realised P&L** | $+554.44 |

## Tranche Feature  (new in paper bot)
| Parameter | Value |
|---|---|
| Tranche 1 (entry day) | 50% of target size |
| Tranche 2 (next day) | 50% — only if price ≤ entry×1.005 |
| Partial exit | Sell 50% at midline, ride rest to time/stop |

## Exit Reasons
| Exit | Trades | WR | Avg P&L% |
|---|---|---|---|
| `rsi_exit` | 12 | 83% | +1.84% |
| `stop_loss` | 10 | 0% | -2.55% |

## Recent Closed Trades
| Date | Ticker | Strategy | P&L% | P&L$ | Hold | Exit |
|---|---|---|---|---|---|---|
| 2026-05-24 | **LINKUSD** | `CryptoRSI` | -1.62% | $-0.15 | 0d | stop_loss (-1.6%) |
| 2026-05-24 | **AVAXUSD** | `CryptoRSI` | -2.17% | $-0.16 | 0d | stop_loss (-2.2%) |
| 2026-05-23 | **SOLUSD** | `CryptoRSI` | +5.14% | $+149.45 | 0d | rsi_exit (RSI=66) |
| 2026-05-23 | **LINKUSD** | `CryptoRSI` | +3.68% | $+107.14 | 0d | rsi_exit (RSI=70) |
| 2026-05-23 | **ETHUSD** | `CryptoRSI` | +4.31% | $+125.55 | 0d | rsi_exit (RSI=72) |
| 2026-05-23 | **BTCUSD** | `CryptoRSI` | +2.23% | $+64.88 | 0d | rsi_exit (RSI=72) |
| 2026-05-23 | **AVAXUSD** | `CryptoRSI` | +5.96% | $+173.12 | 0d | rsi_exit (RSI=70) |
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

---
*Auto-generated. Paper account only.*