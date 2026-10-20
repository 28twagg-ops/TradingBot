# Daily Comprehensive Action Review - 2026-10-20

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20261020T130144Z

- UTC timestamp: `20261020T130144Z`
- GitHub run: [#13270](https://github.com/28twagg-ops/TradingBot/actions/runs/39426703872)
- Run id: `39426703872`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20261020T130144Z_live_bot.log`, `logs/action_runs/20261020T130144Z_live_options.log`, `logs/action_runs/20261020T130144Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1700 | 48.2 | -27.6 | +36.8 | $+18,423 |
| TAINTED | 2008 | 32.3 | -40.6 | +10.7 | $-11,098 |
| KEEP-only | 838 | 60.4 | +50.7 | +54.1 | $+12,615 |
| KEEP-only recent | 645 | 58.8 | +52.9 | +59.8 | $+8,554 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-20T09:01:49.575184-04:00","date":"2026-10-20","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.48},"signals":0,"placed":0,"equity":993100.43,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13270","github_run_id":"39426703872","status":"ok","data_quality":{"clean":{"n":1700,"win":48.18,"med":-27.62,"avg":36.85,"pnl":18422.83},"tainted":{"n":2008,"win":32.27,"med":-40.61,"avg":10.66,"pnl":-11098.28},"keep_only":{"n":838,"win":60.38,"med":50.71,"avg":54.12,"pnl":12615.45},"keep_only_recent":{"n":645,"win":58.76,"med":52.94,"avg":59.75,"pnl":8554.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:01:45  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.20|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.20|
|  Cash                                                           $123.97|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.23|
|  Open P&L                                                        $-0.08|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $33.73     $14.96   $14.94   -0.1%   $-0.05  |
|  ALL      Pullback50      $33.80     $246.57  $246.85  +0.1%   $+0.04  |
|  AMCR     Pullback50      $33.70     $44.04   $43.95   -0.2%   $-0.07  |
|                                                                        |
|  Total invested                                                 $101.23|
|  Total open P&L                                                  $-0.08|
+========================================================================+

+========================================================================+
|                     OPTION HOLDINGS  (0 contracts)                     |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                        EXIT LOGIC ACTIVE  (v8)                         |
+========================================================================+
|  Profit target                              price > 20-day MA (midline)|
|  Stop loss                                             -0.5% from entry|
|  Time stop                                          max 3 calendar days|
+========================================================================+

+========================================================================+
|                          RECENT TRANSACTIONS                           |
+========================================================================+
|  2026-10-19  SELL  AES  Pullback50  $33.80  P&L $+0.03                 |
|  2026-10-19  SELL  AMCR  Pullback50  $33.81  P&L $+0.03                |
|  2026-10-19  SELL  ALL  Pullback50  $33.79  P&L $+0.01                 |
|  2026-10-19  SELL  AMZN  Pullback50  $34.56  P&L $+0.85                |
|  2026-10-19  SELL  BAX  Pullback50  $8.58  P&L $-0.06                  |
|  2026-10-19  SELL  ALL  Pullback50  $33.54  P&L $-0.17                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-20T09:01:46.714043-04:00 share=25% ===
2026-10-20 09:01:46,714 INFO === options_live_micro LIVE 2026-10-20T09:01:46.714043-04:00 share=25% ===
Live account equity $225.20 cash $123.97 #225458845 options_level=3
2026-10-20 09:01:46,929 INFO Live account equity $225.20 cash $123.97 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-20 09:01:46,988 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-20 09:01:47,047 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
| S169 | 0 | 0 |
| S170 | 0 | 0 |
| S171 | 0 | 0 |
| S172 | 0 | 0 |
| S175 | 0 | 0 |
| S173 | 1911 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |    0 |    0 |    0 |    0 |    0 |  118 |   48 |   444 |
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |    0 |    0 |    0 |    0 |    0 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   237 |
| 2026-07-24 |   75 |   87 |   85 |   15 |   77 |   55 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   434 |
| 2026-07-27 |   14 |    0 |   14 |   14 |   14 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    70 |
| 2026-07-28 |    6 |    8 |    8 |    8 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-07-29 |   10 |   10 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-01 |    8 |    6 |    6 |    2 |    6 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    34 |
| 2026-09-02 |   10 |   10 |   10 |    2 |   10 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    56 |
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-09-15 |    4 |   14 |   14 |    0 |   14 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    54 |
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1915 | WARN | <<<
| Missing exit records (post) |  1915 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |  2819 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-20_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-20_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1700 med=-27.6% | TAINTED n=2008 med=-40.6% | KEEP-only n=838 med=+50.7% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.2 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261020T130821Z

- UTC timestamp: `20261020T130821Z`
- GitHub run: [#13271](https://github.com/28twagg-ops/TradingBot/actions/runs/39427401625)
- Run id: `39427401625`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20261020T130821Z_live_bot.log`, `logs/action_runs/20261020T130821Z_live_options.log`, `logs/action_runs/20261020T130821Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1700 | 48.2 | -27.6 | +36.8 | $+18,423 |
| TAINTED | 2008 | 32.3 | -40.6 | +10.7 | $-11,098 |
| KEEP-only | 838 | 60.4 | +50.7 | +54.1 | $+12,615 |
| KEEP-only recent | 645 | 58.8 | +52.9 | +59.8 | $+8,554 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-20T09:08:26.623216-04:00","date":"2026-10-20","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.44},"signals":0,"placed":0,"equity":993005.17,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13271","github_run_id":"39427401625","status":"ok","data_quality":{"clean":{"n":1700,"win":48.18,"med":-27.62,"avg":36.85,"pnl":18422.83},"tainted":{"n":2008,"win":32.27,"med":-40.61,"avg":10.66,"pnl":-11098.28},"keep_only":{"n":838,"win":60.38,"med":50.71,"avg":54.12,"pnl":12615.45},"keep_only_recent":{"n":645,"win":58.76,"med":52.94,"avg":59.75,"pnl":8554.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:08:22  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:08 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.20|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.20|
|  Cash                                                           $123.97|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.23|
|  Open P&L                                                        $-0.08|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $33.73     $14.96   $14.94   -0.1%   $-0.05  |
|  ALL      Pullback50      $33.80     $246.57  $246.85  +0.1%   $+0.04  |
|  AMCR     Pullback50      $33.70     $44.04   $43.95   -0.2%   $-0.07  |
|                                                                        |
|  Total invested                                                 $101.23|
|  Total open P&L                                                  $-0.08|
+========================================================================+

+========================================================================+
|                     OPTION HOLDINGS  (0 contracts)                     |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                        EXIT LOGIC ACTIVE  (v8)                         |
+========================================================================+
|  Profit target                              price > 20-day MA (midline)|
|  Stop loss                                             -0.5% from entry|
|  Time stop                                          max 3 calendar days|
+========================================================================+

+========================================================================+
|                          RECENT TRANSACTIONS                           |
+========================================================================+
|  2026-10-19  SELL  AES  Pullback50  $33.80  P&L $+0.03                 |
|  2026-10-19  SELL  AMCR  Pullback50  $33.81  P&L $+0.03                |
|  2026-10-19  SELL  ALL  Pullback50  $33.79  P&L $+0.01                 |
|  2026-10-19  SELL  AMZN  Pullback50  $34.56  P&L $+0.85                |
|  2026-10-19  SELL  BAX  Pullback50  $8.58  P&L $-0.06                  |
|  2026-10-19  SELL  ALL  Pullback50  $33.54  P&L $-0.17                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-20T09:08:23.988878-04:00 share=25% ===
2026-10-20 09:08:23,988 INFO === options_live_micro LIVE 2026-10-20T09:08:23.988878-04:00 share=25% ===
Live account equity $225.20 cash $123.97 #225458845 options_level=3
2026-10-20 09:08:24,183 INFO Live account equity $225.20 cash $123.97 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-20 09:08:24,240 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-20 09:08:24,297 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
| S169 | 0 | 0 |
| S170 | 0 | 0 |
| S171 | 0 | 0 |
| S172 | 0 | 0 |
| S175 | 0 | 0 |
| S173 | 1911 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |    0 |    0 |    0 |    0 |    0 |  118 |   48 |   444 |
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |    0 |    0 |    0 |    0 |    0 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   237 |
| 2026-07-24 |   75 |   87 |   85 |   15 |   77 |   55 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   434 |
| 2026-07-27 |   14 |    0 |   14 |   14 |   14 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    70 |
| 2026-07-28 |    6 |    8 |    8 |    8 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-07-29 |   10 |   10 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-01 |    8 |    6 |    6 |    2 |    6 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    34 |
| 2026-09-02 |   10 |   10 |   10 |    2 |   10 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    56 |
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-09-15 |    4 |   14 |   14 |    0 |   14 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    54 |
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1915 | WARN | <<<
| Missing exit records (post) |  1915 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |  2819 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-20_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-20_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1700 med=-27.6% | TAINTED n=2008 med=-40.6% | KEEP-only n=838 med=+50.7% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.2 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261020T131133Z

- UTC timestamp: `20261020T131133Z`
- GitHub run: [#13272](https://github.com/28twagg-ops/TradingBot/actions/runs/39428089001)
- Run id: `39428089001`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20261020T131133Z_live_bot.log`, `logs/action_runs/20261020T131133Z_live_options.log`, `logs/action_runs/20261020T131133Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1700 | 48.2 | -27.6 | +36.8 | $+18,423 |
| TAINTED | 2008 | 32.3 | -40.6 | +10.7 | $-11,098 |
| KEEP-only | 838 | 60.4 | +50.7 | +54.1 | $+12,615 |
| KEEP-only recent | 645 | 58.8 | +52.9 | +59.8 | $+8,554 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-20T09:11:39.211597-04:00","date":"2026-10-20","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.42},"signals":0,"placed":0,"equity":993003.65,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13272","github_run_id":"39428089001","status":"ok","data_quality":{"clean":{"n":1700,"win":48.18,"med":-27.62,"avg":36.85,"pnl":18422.83},"tainted":{"n":2008,"win":32.27,"med":-40.61,"avg":10.66,"pnl":-11098.28},"keep_only":{"n":838,"win":60.38,"med":50.71,"avg":54.12,"pnl":12615.45},"keep_only_recent":{"n":645,"win":58.76,"med":52.94,"avg":59.75,"pnl":8554.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:11:34  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.20|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.20|
|  Cash                                                           $123.97|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.23|
|  Open P&L                                                        $-0.08|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $33.73     $14.96   $14.94   -0.1%   $-0.05  |
|  ALL      Pullback50      $33.80     $246.57  $246.85  +0.1%   $+0.04  |
|  AMCR     Pullback50      $33.70     $44.04   $43.95   -0.2%   $-0.07  |
|                                                                        |
|  Total invested                                                 $101.23|
|  Total open P&L                                                  $-0.08|
+========================================================================+

+========================================================================+
|                     OPTION HOLDINGS  (0 contracts)                     |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                        EXIT LOGIC ACTIVE  (v8)                         |
+========================================================================+
|  Profit target                              price > 20-day MA (midline)|
|  Stop loss                                             -0.5% from entry|
|  Time stop                                          max 3 calendar days|
+========================================================================+

+========================================================================+
|                          RECENT TRANSACTIONS                           |
+========================================================================+
|  2026-10-19  SELL  AES  Pullback50  $33.80  P&L $+0.03                 |
|  2026-10-19  SELL  AMCR  Pullback50  $33.81  P&L $+0.03                |
|  2026-10-19  SELL  ALL  Pullback50  $33.79  P&L $+0.01                 |
|  2026-10-19  SELL  AMZN  Pullback50  $34.56  P&L $+0.85                |
|  2026-10-19  SELL  BAX  Pullback50  $8.58  P&L $-0.06                  |
|  2026-10-19  SELL  ALL  Pullback50  $33.54  P&L $-0.17                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-20T09:11:36.021603-04:00 share=25% ===
2026-10-20 09:11:36,021 INFO === options_live_micro LIVE 2026-10-20T09:11:36.021603-04:00 share=25% ===
Live account equity $225.20 cash $123.97 #225458845 options_level=3
2026-10-20 09:11:36,227 INFO Live account equity $225.20 cash $123.97 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-20 09:11:36,285 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-20 09:11:36,344 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
| S169 | 0 | 0 |
| S170 | 0 | 0 |
| S171 | 0 | 0 |
| S172 | 0 | 0 |
| S175 | 0 | 0 |
| S173 | 1911 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |    0 |    0 |    0 |    0 |    0 |  118 |   48 |   444 |
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |    0 |    0 |    0 |    0 |    0 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   237 |
| 2026-07-24 |   75 |   87 |   85 |   15 |   77 |   55 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   434 |
| 2026-07-27 |   14 |    0 |   14 |   14 |   14 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    70 |
| 2026-07-28 |    6 |    8 |    8 |    8 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-07-29 |   10 |   10 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-01 |    8 |    6 |    6 |    2 |    6 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    34 |
| 2026-09-02 |   10 |   10 |   10 |    2 |   10 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    56 |
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-09-15 |    4 |   14 |   14 |    0 |   14 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    54 |
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1915 | WARN | <<<
| Missing exit records (post) |  1915 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |  2819 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-20_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-20_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1700 med=-27.6% | TAINTED n=2008 med=-40.6% | KEEP-only n=838 med=+50.7% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.2 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261020T131639Z

- UTC timestamp: `20261020T131639Z`
- GitHub run: [#13273](https://github.com/28twagg-ops/TradingBot/actions/runs/39428790104)
- Run id: `39428790104`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20261020T131639Z_live_bot.log`, `logs/action_runs/20261020T131639Z_live_options.log`, `logs/action_runs/20261020T131639Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1700 | 48.2 | -27.6 | +36.8 | $+18,423 |
| TAINTED | 2008 | 32.3 | -40.6 | +10.7 | $-11,098 |
| KEEP-only | 838 | 60.4 | +50.7 | +54.1 | $+12,615 |
| KEEP-only recent | 645 | 58.8 | +52.9 | +59.8 | $+8,554 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-20T09:16:44.675483-04:00","date":"2026-10-20","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.09},"signals":0,"placed":0,"equity":992948.84,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13273","github_run_id":"39428790104","status":"ok","data_quality":{"clean":{"n":1700,"win":48.18,"med":-27.62,"avg":36.85,"pnl":18422.83},"tainted":{"n":2008,"win":32.27,"med":-40.61,"avg":10.66,"pnl":-11098.28},"keep_only":{"n":838,"win":60.38,"med":50.71,"avg":54.12,"pnl":12615.45},"keep_only_recent":{"n":645,"win":58.76,"med":52.94,"avg":59.75,"pnl":8554.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:16:40  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.48|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.48|
|  Cash                                                           $123.97|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.51|
|  Open P&L                                                        $+0.21|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $33.73     $14.96   $14.94   -0.1%   $-0.05  |
|  ALL      Pullback50      $33.80     $246.57  $246.85  +0.1%   $+0.04  |
|  AMCR     Pullback50      $33.98     $44.04   $44.32   +0.6%   $+0.21  |
|                                                                        |
|  Total invested                                                 $101.51|
|  Total open P&L                                                  $+0.21|
+========================================================================+

+========================================================================+
|                     OPTION HOLDINGS  (0 contracts)                     |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                        EXIT LOGIC ACTIVE  (v8)                         |
+========================================================================+
|  Profit target                              price > 20-day MA (midline)|
|  Stop loss                                             -0.5% from entry|
|  Time stop                                          max 3 calendar days|
+========================================================================+

+========================================================================+
|                          RECENT TRANSACTIONS                           |
+========================================================================+
|  2026-10-19  SELL  AES  Pullback50  $33.80  P&L $+0.03                 |
|  2026-10-19  SELL  AMCR  Pullback50  $33.81  P&L $+0.03                |
|  2026-10-19  SELL  ALL  Pullback50  $33.79  P&L $+0.01                 |
|  2026-10-19  SELL  AMZN  Pullback50  $34.56  P&L $+0.85                |
|  2026-10-19  SELL  BAX  Pullback50  $8.58  P&L $-0.06                  |
|  2026-10-19  SELL  ALL  Pullback50  $33.54  P&L $-0.17                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-20T09:16:42.028189-04:00 share=25% ===
2026-10-20 09:16:42,028 INFO === options_live_micro LIVE 2026-10-20T09:16:42.028189-04:00 share=25% ===
Live account equity $225.48 cash $123.97 #225458845 options_level=3
2026-10-20 09:16:42,073 INFO Live account equity $225.48 cash $123.97 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-20 09:16:42,082 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-20 09:16:42,091 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
| S169 | 0 | 0 |
| S170 | 0 | 0 |
| S171 | 0 | 0 |
| S172 | 0 | 0 |
| S175 | 0 | 0 |
| S173 | 1911 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |    0 |    0 |    0 |    0 |    0 |  118 |   48 |   444 |
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |    0 |    0 |    0 |    0 |    0 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   237 |
| 2026-07-24 |   75 |   87 |   85 |   15 |   77 |   55 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   434 |
| 2026-07-27 |   14 |    0 |   14 |   14 |   14 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    70 |
| 2026-07-28 |    6 |    8 |    8 |    8 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-07-29 |   10 |   10 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-01 |    8 |    6 |    6 |    2 |    6 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    34 |
| 2026-09-02 |   10 |   10 |   10 |    2 |   10 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    56 |
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-09-15 |    4 |   14 |   14 |    0 |   14 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    54 |
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1915 | WARN | <<<
| Missing exit records (post) |  1915 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |  2819 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-20_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-20_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1700 med=-27.6% | TAINTED n=2008 med=-40.6% | KEEP-only n=838 med=+50.7% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.48 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261020T132145Z

- UTC timestamp: `20261020T132145Z`
- GitHub run: [#13274](https://github.com/28twagg-ops/TradingBot/actions/runs/39429486180)
- Run id: `39429486180`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20261020T132145Z_live_bot.log`, `logs/action_runs/20261020T132145Z_live_options.log`, `logs/action_runs/20261020T132145Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1700 | 48.2 | -27.6 | +36.8 | $+18,423 |
| TAINTED | 2008 | 32.3 | -40.6 | +10.7 | $-11,098 |
| KEEP-only | 838 | 60.4 | +50.7 | +54.1 | $+12,615 |
| KEEP-only recent | 645 | 58.8 | +52.9 | +59.8 | $+8,554 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-20T09:21:50.364040-04:00","date":"2026-10-20","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.19},"signals":0,"placed":0,"equity":992780.58,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13274","github_run_id":"39429486180","status":"ok","data_quality":{"clean":{"n":1700,"win":48.18,"med":-27.62,"avg":36.85,"pnl":18422.83},"tainted":{"n":2008,"win":32.27,"med":-40.61,"avg":10.66,"pnl":-11098.28},"keep_only":{"n":838,"win":60.38,"med":50.71,"avg":54.12,"pnl":12615.45},"keep_only_recent":{"n":645,"win":58.76,"med":52.94,"avg":59.75,"pnl":8554.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:21:46  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.48|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.48|
|  Cash                                                           $123.97|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.51|
|  Open P&L                                                        $+0.21|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $33.73     $14.96   $14.94   -0.1%   $-0.05  |
|  ALL      Pullback50      $33.80     $246.57  $246.85  +0.1%   $+0.04  |
|  AMCR     Pullback50      $33.98     $44.04   $44.32   +0.6%   $+0.21  |
|                                                                        |
|  Total invested                                                 $101.51|
|  Total open P&L                                                  $+0.21|
+========================================================================+

+========================================================================+
|                     OPTION HOLDINGS  (0 contracts)                     |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                        EXIT LOGIC ACTIVE  (v8)                         |
+========================================================================+
|  Profit target                              price > 20-day MA (midline)|
|  Stop loss                                             -0.5% from entry|
|  Time stop                                          max 3 calendar days|
+========================================================================+

+========================================================================+
|                          RECENT TRANSACTIONS                           |
+========================================================================+
|  2026-10-19  SELL  AES  Pullback50  $33.80  P&L $+0.03                 |
|  2026-10-19  SELL  AMCR  Pullback50  $33.81  P&L $+0.03                |
|  2026-10-19  SELL  ALL  Pullback50  $33.79  P&L $+0.01                 |
|  2026-10-19  SELL  AMZN  Pullback50  $34.56  P&L $+0.85                |
|  2026-10-19  SELL  BAX  Pullback50  $8.58  P&L $-0.06                  |
|  2026-10-19  SELL  ALL  Pullback50  $33.54  P&L $-0.17                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-20T09:21:48.206542-04:00 share=25% ===
2026-10-20 09:21:48,206 INFO === options_live_micro LIVE 2026-10-20T09:21:48.206542-04:00 share=25% ===
Live account equity $225.48 cash $123.97 #225458845 options_level=3
2026-10-20 09:21:48,253 INFO Live account equity $225.48 cash $123.97 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-20 09:21:48,260 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-20 09:21:48,267 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
| S169 | 0 | 0 |
| S170 | 0 | 0 |
| S171 | 0 | 0 |
| S172 | 0 | 0 |
| S175 | 0 | 0 |
| S173 | 1911 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |    0 |    0 |    0 |    0 |    0 |  118 |   48 |   444 |
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |    0 |    0 |    0 |    0 |    0 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   237 |
| 2026-07-24 |   75 |   87 |   85 |   15 |   77 |   55 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   434 |
| 2026-07-27 |   14 |    0 |   14 |   14 |   14 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    70 |
| 2026-07-28 |    6 |    8 |    8 |    8 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-07-29 |   10 |   10 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-01 |    8 |    6 |    6 |    2 |    6 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    34 |
| 2026-09-02 |   10 |   10 |   10 |    2 |   10 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    56 |
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-09-15 |    4 |   14 |   14 |    0 |   14 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    54 |
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1915 | WARN | <<<
| Missing exit records (post) |  1915 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |  2819 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-20_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-20_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1700 med=-27.6% | TAINTED n=2008 med=-40.6% | KEEP-only n=838 med=+50.7% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.48 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261020T132640Z

- UTC timestamp: `20261020T132640Z`
- GitHub run: [#13275](https://github.com/28twagg-ops/TradingBot/actions/runs/39430199798)
- Run id: `39430199798`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`15s`
- Full logs: `logs/action_runs/20261020T132640Z_live_bot.log`, `logs/action_runs/20261020T132640Z_live_options.log`, `logs/action_runs/20261020T132640Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1700 | 48.2 | -27.6 | +36.8 | $+18,423 |
| TAINTED | 2008 | 32.3 | -40.6 | +10.7 | $-11,098 |
| KEEP-only | 838 | 60.4 | +50.7 | +54.1 | $+12,615 |
| KEEP-only recent | 645 | 58.8 | +52.9 | +59.8 | $+8,554 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-20T09:26:46.268233-04:00","date":"2026-10-20","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":993003.84,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13275","github_run_id":"39430199798","status":"ok","data_quality":{"clean":{"n":1700,"win":48.18,"med":-27.62,"avg":36.85,"pnl":18422.83},"tainted":{"n":2008,"win":32.27,"med":-40.61,"avg":10.66,"pnl":-11098.28},"keep_only":{"n":838,"win":60.38,"med":50.71,"avg":54.12,"pnl":12615.45},"keep_only_recent":{"n":645,"win":58.76,"med":52.94,"avg":59.75,"pnl":8554.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:26:42  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.50|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.50|
|  Cash                                                           $123.97|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.53|
|  Open P&L                                                        $+0.23|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $33.75     $14.96   $14.95   -0.1%   $-0.02  |
|  ALL      Pullback50      $33.80     $246.57  $246.85  +0.1%   $+0.04  |
|  AMCR     Pullback50      $33.98     $44.04   $44.32   +0.6%   $+0.21  |
|                                                                        |
|  Total invested                                                 $101.53|
|  Total open P&L                                                  $+0.23|
+========================================================================+

+========================================================================+
|                     OPTION HOLDINGS  (0 contracts)                     |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                        EXIT LOGIC ACTIVE  (v8)                         |
+========================================================================+
|  Profit target                              price > 20-day MA (midline)|
|  Stop loss                                             -0.5% from entry|
|  Time stop                                          max 3 calendar days|
+========================================================================+

+========================================================================+
|                          RECENT TRANSACTIONS                           |
+========================================================================+
|  2026-10-19  SELL  AES  Pullback50  $33.80  P&L $+0.03                 |
|  2026-10-19  SELL  AMCR  Pullback50  $33.81  P&L $+0.03                |
|  2026-10-19  SELL  ALL  Pullback50  $33.79  P&L $+0.01                 |
|  2026-10-19  SELL  AMZN  Pullback50  $34.56  P&L $+0.85                |
|  2026-10-19  SELL  BAX  Pullback50  $8.58  P&L $-0.06                  |
|  2026-10-19  SELL  ALL  Pullback50  $33.54  P&L $-0.17                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-20T09:26:43.277553-04:00 share=25% ===
2026-10-20 09:26:43,277 INFO === options_live_micro LIVE 2026-10-20T09:26:43.277553-04:00 share=25% ===
Live account equity $225.50 cash $123.97 #225458845 options_level=3
2026-10-20 09:26:43,337 INFO Live account equity $225.50 cash $123.97 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-20 09:26:43,351 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-20 09:26:43,362 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
| S169 | 0 | 0 |
| S170 | 0 | 0 |
| S171 | 0 | 0 |
| S172 | 0 | 0 |
| S175 | 0 | 0 |
| S173 | 1911 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |    0 |    0 |    0 |    0 |    0 |  118 |   48 |   444 |
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |    0 |    0 |    0 |    0 |    0 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   237 |
| 2026-07-24 |   75 |   87 |   85 |   15 |   77 |   55 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   434 |
| 2026-07-27 |   14 |    0 |   14 |   14 |   14 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    70 |
| 2026-07-28 |    6 |    8 |    8 |    8 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-07-29 |   10 |   10 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-01 |    8 |    6 |    6 |    2 |    6 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    34 |
| 2026-09-02 |   10 |   10 |   10 |    2 |   10 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    56 |
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-09-15 |    4 |   14 |   14 |    0 |   14 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    54 |
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1915 | WARN | <<<
| Missing exit records (post) |  1915 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |  2819 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-20_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-20_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1700 med=-27.6% | TAINTED n=2008 med=-40.6% | KEEP-only n=838 med=+50.7% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.5 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261020T133137Z

- UTC timestamp: `20261020T133137Z`
- GitHub run: [#13276](https://github.com/28twagg-ops/TradingBot/actions/runs/39430911551)
- Run id: `39430911551`
- Live bot: exit=`0`, duration=`215s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261020T133137Z_live_bot.log`, `logs/action_runs/20261020T133137Z_live_options.log`, `logs/action_runs/20261020T133137Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1700 | 48.2 | -27.6 | +36.8 | $+18,423 |
| TAINTED | 2008 | 32.3 | -40.6 | +10.7 | $-11,098 |
| KEEP-only | 838 | 60.4 | +50.7 | +54.1 | $+12,615 |
| KEEP-only recent | 645 | 58.8 | +52.9 | +59.8 | $+8,554 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-20T09:26:46.268233-04:00","date":"2026-10-20","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":993003.84,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13275","github_run_id":"39430199798","status":"ok","data_quality":{"clean":{"n":1700,"win":48.18,"med":-27.62,"avg":36.85,"pnl":18422.83},"tainted":{"n":2008,"win":32.27,"med":-40.61,"avg":10.66,"pnl":-11098.28},"keep_only":{"n":838,"win":60.38,"med":50.71,"avg":54.12,"pnl":12615.45},"keep_only_recent":{"n":645,"win":58.76,"med":52.94,"avg":59.75,"pnl":8554.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:31:38  INFO      Mode: morning_prep
13:31:38  INFO        [prep_positions] 3/3 (3 valid)
13:31:38  INFO      Fetching tickers (universe=both)...
13:31:39  INFO        S&P 500: 503
13:31:39  INFO        MidCap 400: 400
13:31:39  INFO        Total: 903 tickers
13:31:41  INFO        [prep_universe] 40/900 (40 valid)
13:31:42  INFO        [prep_universe] 80/900 (80 valid)
13:31:44  INFO        [prep_universe] 120/900 (120 valid)
13:31:45  INFO        [prep_universe] 160/900 (160 valid)
13:31:46  INFO        [prep_universe] 200/900 (199 valid)
13:31:53  INFO        [prep_universe] 240/900 (238 valid)
13:32:04  INFO        [prep_universe] 280/900 (278 valid)
13:32:18  INFO        [prep_universe] 320/900 (318 valid)
13:32:28  INFO        [prep_universe] 360/900 (358 valid)
13:32:41  INFO        [prep_universe] 400/900 (398 valid)
13:32:51  INFO        [prep_universe] 440/900 (438 valid)
13:33:05  INFO        [prep_universe] 480/900 (477 valid)
13:33:18  INFO        [prep_universe] 520/900 (517 valid)
13:33:28  INFO        [prep_universe] 560/900 (557 valid)
13:33:41  INFO        [prep_universe] 600/900 (597 valid)
13:33:54  INFO        [prep_universe] 640/900 (637 valid)
13:34:04  INFO        [prep_universe] 680/900 (677 valid)
13:34:17  INFO        [prep_universe] 720/900 (717 valid)
13:34:30  INFO        [prep_universe] 760/900 (757 valid)
13:34:40  INFO        [prep_universe] 800/900 (797 valid)
13:34:53  INFO        [prep_universe] 840/900 (837 valid)
13:35:04  INFO        [prep_universe] 880/900 (877 valid)
13:35:11  INFO        [prep_universe] 900/900 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.87|
+========================================================================+

+========================================================================+
|                              MORNING PREP                              |
+========================================================================+
|  Goal                   Precompute exits/signals for next execution run|
|  Plan file                                 logs/plans/morning_plan.json|
|  Regime                                                            BULL|
+========================================================================+

+========================================================================+
|                       OPEN POSITION P&L SNAPSHOT                       |
+========================================================================+
|  Open positions                                                       3|
|  Invested                                                       $101.90|
|  Open P&L                                                        $+0.60|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $33.77     $14.96   $14.96   +0.0%   $+0.00  |
|  ALL      Pullback50      $34.39     $246.57  $251.16  +1.9%   $+0.63  |
|  AMCR     Pullback50      $33.74     $44.04   $44.00   -0.1%   $-0.03  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                0|
|                                                                        |
|  No open sell orders.                                                  |
|                                                                        |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      3|
|  Signal candidates                                                   43|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261020T133701Z

- UTC timestamp: `20261020T133701Z`
- GitHub run: [#13277](https://github.com/28twagg-ops/TradingBot/actions/runs/39431653369)
- Run id: `39431653369`
- Live bot: exit=`0`, duration=`216s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261020T133701Z_live_bot.log`, `logs/action_runs/20261020T133701Z_live_options.log`, `logs/action_runs/20261020T133701Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1700 | 48.2 | -27.6 | +36.8 | $+18,423 |
| TAINTED | 2008 | 32.3 | -40.6 | +10.7 | $-11,098 |
| KEEP-only | 838 | 60.4 | +50.7 | +54.1 | $+12,615 |
| KEEP-only recent | 645 | 58.8 | +52.9 | +59.8 | $+8,554 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-20T09:26:46.268233-04:00","date":"2026-10-20","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":993003.84,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13275","github_run_id":"39430199798","status":"ok","data_quality":{"clean":{"n":1700,"win":48.18,"med":-27.62,"avg":36.85,"pnl":18422.83},"tainted":{"n":2008,"win":32.27,"med":-40.61,"avg":10.66,"pnl":-11098.28},"keep_only":{"n":838,"win":60.38,"med":50.71,"avg":54.12,"pnl":12615.45},"keep_only_recent":{"n":645,"win":58.76,"med":52.94,"avg":59.75,"pnl":8554.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:37:02  INFO      Mode: morning_prep
13:37:03  INFO        [prep_positions] 3/3 (3 valid)
13:37:03  INFO      Fetching tickers (universe=both)...
13:37:03  INFO        S&P 500: 503
13:37:04  INFO        MidCap 400: 400
13:37:04  INFO        Total: 903 tickers
13:37:05  INFO        [prep_universe] 40/900 (40 valid)
13:37:06  INFO        [prep_universe] 80/900 (80 valid)
13:37:07  INFO        [prep_universe] 120/900 (120 valid)
13:37:09  INFO        [prep_universe] 160/900 (160 valid)
13:37:11  INFO        [prep_universe] 200/900 (199 valid)
13:37:18  INFO        [prep_universe] 240/900 (238 valid)
13:37:28  INFO        [prep_universe] 280/900 (278 valid)
13:37:41  INFO        [prep_universe] 320/900 (318 valid)
13:37:54  INFO        [prep_universe] 360/900 (358 valid)
13:38:04  INFO        [prep_universe] 400/900 (398 valid)
13:38:18  INFO        [prep_universe] 440/900 (438 valid)
13:38:28  INFO        [prep_universe] 480/900 (477 valid)
13:38:41  INFO        [prep_universe] 520/900 (517 valid)
13:38:54  INFO        [prep_universe] 560/900 (557 valid)
13:39:05  INFO        [prep_universe] 600/900 (597 valid)
13:39:18  INFO        [prep_universe] 640/900 (637 valid)
13:39:28  INFO        [prep_universe] 680/900 (677 valid)
13:39:41  INFO        [prep_universe] 720/900 (717 valid)
13:39:54  INFO        [prep_universe] 760/900 (757 valid)
13:40:05  INFO        [prep_universe] 800/900 (797 valid)
13:40:18  INFO        [prep_universe] 840/900 (837 valid)
13:40:31  INFO        [prep_universe] 880/900 (877 valid)
13:40:35  INFO        [prep_universe] 900/900 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:37 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.03|
+========================================================================+

+========================================================================+
|                              MORNING PREP                              |
+========================================================================+
|  Goal                   Precompute exits/signals for next execution run|
|  Plan file                                 logs/plans/morning_plan.json|
|  Regime                                                            BULL|
+========================================================================+

+========================================================================+
|                       OPEN POSITION P&L SNAPSHOT                       |
+========================================================================+
|  Open positions                                                       3|
|  Invested                                                       $102.06|
|  Open P&L                                                        $+0.76|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $33.80     $14.96   $14.97   +0.1%   $+0.02  |
|  ALL      Pullback50      $34.31     $246.57  $250.56  +1.6%   $+0.55  |
|  AMCR     Pullback50      $33.96     $44.04   $44.29   +0.6%   $+0.19  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                0|
|                                                                        |
|  No open sell orders.                                                  |
|                                                                        |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      3|
|  Signal candidates                                                   46|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-20T09:40:38.409752-04:00 share=25% ===
2026-10-20 09:40:38,409 INFO === options_live_micro LIVE 2026-10-20T09:40:38.409752-04:00 share=25% ===
Live account equity $226.32 cash $123.97 #225458845 options_level=3
2026-10-20 09:40:38,537 INFO Live account equity $226.32 cash $123.97 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-20 09:40:38,644 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-20 09:40:38,712 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text

```

---

## Run 20261020T134247Z

- UTC timestamp: `20261020T134247Z`
- GitHub run: [#13278](https://github.com/28twagg-ops/TradingBot/actions/runs/39432377338)
- Run id: `39432377338`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261020T134247Z_live_bot.log`, `logs/action_runs/20261020T134247Z_live_options.log`, `logs/action_runs/20261020T134247Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1700 | 48.2 | -27.6 | +36.8 | $+18,423 |
| TAINTED | 2008 | 32.3 | -40.6 | +10.7 | $-11,098 |
| KEEP-only | 838 | 60.4 | +50.7 | +54.1 | $+12,615 |
| KEEP-only recent | 645 | 58.8 | +52.9 | +59.8 | $+8,554 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-20T09:26:46.268233-04:00","date":"2026-10-20","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":993003.84,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13275","github_run_id":"39430199798","status":"ok","data_quality":{"clean":{"n":1700,"win":48.18,"med":-27.62,"avg":36.85,"pnl":18422.83},"tainted":{"n":2008,"win":32.27,"med":-40.61,"avg":10.66,"pnl":-11098.28},"keep_only":{"n":838,"win":60.38,"med":50.71,"avg":54.12,"pnl":12615.45},"keep_only_recent":{"n":645,"win":58.76,"med":52.94,"avg":59.75,"pnl":8554.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:42:48  INFO      Mode: morning_prep
13:42:49  INFO        [prep_positions] 3/3 (3 valid)
13:42:49  INFO        Universe cache hit: 903 tickers (tickers_2026-10-20.json)
13:42:49  INFO        [prep_universe] 40/900 (40 valid)
13:42:51  INFO        [prep_universe] 80/900 (80 valid)
13:42:52  INFO        [prep_universe] 120/900 (120 valid)
13:42:52  INFO        [prep_universe] 160/900 (160 valid)
13:42:54  INFO        [prep_universe] 200/900 (199 valid)
13:43:03  INFO        [prep_universe] 240/900 (238 valid)
13:43:17  INFO        [prep_universe] 280/900 (278 valid)
13:43:27  INFO        [prep_universe] 320/900 (318 valid)
13:43:40  INFO        [prep_universe] 360/900 (358 valid)
13:43:50  INFO        [prep_universe] 400/900 (398 valid)
13:44:03  INFO        [prep_universe] 440/900 (438 valid)
13:44:16  INFO        [prep_universe] 480/900 (477 valid)
13:44:26  INFO        [prep_universe] 520/900 (517 valid)
13:44:39  INFO        [prep_universe] 560/900 (557 valid)
13:44:52  INFO        [prep_universe] 600/900 (597 valid)
13:45:02  INFO        [prep_universe] 640/900 (637 valid)
13:45:15  INFO        [prep_universe] 680/900 (677 valid)
13:45:28  INFO        [prep_universe] 720/900 (717 valid)
13:45:38  INFO        [prep_universe] 760/900 (757 valid)
13:45:52  INFO        [prep_universe] 800/900 (797 valid)
13:46:02  INFO        [prep_universe] 840/900 (837 valid)
13:46:16  INFO        [prep_universe] 880/900 (877 valid)
13:46:20  INFO        [prep_universe] 900/900 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:42 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.24|
+========================================================================+

+========================================================================+
|                              MORNING PREP                              |
+========================================================================+
|  Goal                   Precompute exits/signals for next execution run|
|  Plan file                                 logs/plans/morning_plan.json|
|  Regime                                                            BULL|
+========================================================================+

+========================================================================+
|                       OPEN POSITION P&L SNAPSHOT                       |
+========================================================================+
|  Open positions                                                       3|
|  Invested                                                       $102.27|
|  Open P&L                                                        $+0.97|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $33.77     $14.96   $14.96   +0.0%   $+0.00  |
|  ALL      Pullback50      $34.54     $246.57  $252.26  +2.3%   $+0.78  |
|  AMCR     Pullback50      $33.96     $44.04   $44.29   +0.6%   $+0.19  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                0|
|                                                                        |
|  No open sell orders.                                                  |
|                                                                        |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      3|
|  Signal candidates                                                   47|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---
