# Daily Comprehensive Action Review - 2026-09-28

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260928T130122Z

- UTC timestamp: `20260928T130122Z`
- GitHub run: [#11163](https://github.com/28twagg-ops/TradingBot/actions/runs/36425509010)
- Run id: `36425509010`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260928T130122Z_live_bot.log`, `logs/action_runs/20260928T130122Z_live_options.log`, `logs/action_runs/20260928T130122Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1508 | 50.2 | +8.6 | +43.6 | $+19,714 |
| TAINTED | 1908 | 33.4 | -38.8 | +12.7 | $-9,602 |
| KEEP-only | 798 | 63.3 | +52.8 | +66.8 | $+13,806 |
| KEEP-only recent | 603 | 62.5 | +56.9 | +76.9 | $+9,721 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:01:29.203386-04:00","date":"2026-09-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.2,"phases_s":{"reconcile":4.44},"signals":0,"placed":0,"equity":996963.17,"open_positions":18,"pending_orders":0,"open_lots":77,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11163","github_run_id":"36425509010","status":"ok","data_quality":{"clean":{"n":1508,"win":50.2,"med":8.63,"avg":43.62,"pnl":19714.16},"tainted":{"n":1908,"win":33.39,"med":-38.81,"avg":12.66,"pnl":-9602.28},"keep_only":{"n":798,"win":63.28,"med":52.75,"avg":66.75,"pnl":13806.45},"keep_only_recent":{"n":603,"win":62.52,"med":56.92,"avg":76.9,"pnl":9721.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:01:24  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.89|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $223.89|
|  Cash                                                           $156.73|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.16|
|  Open P&L                                                        $+0.02|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CVS      MomReversal     $33.63     $89.14   $89.30   +0.2%   $+0.06  |
|  EVR      MomReversal     $33.53     $262.43  $262.10  -0.1%   $-0.04  |
|                                                                        |
|  Total invested                                                  $67.16|
|  Total open P&L                                                  $+0.02|
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
|  2026-09-25  SELL  AYI  MomReversal  $33.58  P&L $+0.01                |
|  2026-09-25  SELL  COP  Pullback50  $33.54  P&L $-0.17                 |
|  2026-09-25  SELL  GOOG  Pullback50  $33.59  P&L $-0.01                |
|  2026-09-25  SELL  GOOGL  Pullback50  $33.59  P&L $-0.01               |
|  2026-09-25  SELL  KNF  MomReversal  $33.28  P&L $-0.47                |
|  2026-09-24  SELL  AES  Pullback50  $33.74  P&L $-0.02                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T09:01:25.441314-04:00 share=25% ===
2026-09-28 09:01:25,441 INFO === options_live_micro LIVE 2026-09-28T09:01:25.441314-04:00 share=25% ===
Live account equity $223.89 cash $156.73 #225458845 options_level=3
2026-09-28 09:01:25,575 INFO Live account equity $223.89 cash $156.73 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-28 09:01:25,607 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-28 09:01:25,639 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (189 earlier lines - see full log file)

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 293 | 21 |
| S164 | 333 | 24 |
| S165 | 1759 | 36 |
| S166 | 139 | 10 |
| S167 | 316 | 23 |
| S168 | 236 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    77 | INFO |
| Total closed lots           |  2539 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1508 med=+8.6% | TAINTED n=1908 med=-38.8% | KEEP-only n=798 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.89 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T130616Z

- UTC timestamp: `20260928T130616Z`
- GitHub run: [#11164](https://github.com/28twagg-ops/TradingBot/actions/runs/36426083938)
- Run id: `36426083938`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260928T130616Z_live_bot.log`, `logs/action_runs/20260928T130616Z_live_options.log`, `logs/action_runs/20260928T130616Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1508 | 50.2 | +8.6 | +43.6 | $+19,714 |
| TAINTED | 1908 | 33.4 | -38.8 | +12.7 | $-9,602 |
| KEEP-only | 798 | 63.3 | +52.8 | +66.8 | $+13,806 |
| KEEP-only recent | 603 | 62.5 | +56.9 | +76.9 | $+9,721 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:06:22.556782-04:00","date":"2026-09-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.5,"phases_s":{"reconcile":4.63},"signals":0,"placed":0,"equity":996963.17,"open_positions":18,"pending_orders":0,"open_lots":77,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11164","github_run_id":"36426083938","status":"ok","data_quality":{"clean":{"n":1508,"win":50.2,"med":8.63,"avg":43.62,"pnl":19714.16},"tainted":{"n":1908,"win":33.39,"med":-38.81,"avg":12.66,"pnl":-9602.28},"keep_only":{"n":798,"win":63.28,"med":52.75,"avg":66.75,"pnl":13806.45},"keep_only_recent":{"n":603,"win":62.52,"med":56.92,"avg":76.9,"pnl":9721.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:06:17  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.16|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.16|
|  Cash                                                           $156.73|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.43|
|  Open P&L                                                        $+0.29|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CVS      MomReversal     $33.67     $89.14   $89.40   +0.3%   $+0.10  |
|  EVR      MomReversal     $33.76     $262.43  $263.91  +0.6%   $+0.19  |
|                                                                        |
|  Total invested                                                  $67.43|
|  Total open P&L                                                  $+0.29|
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
|  2026-09-25  SELL  AYI  MomReversal  $33.58  P&L $+0.01                |
|  2026-09-25  SELL  COP  Pullback50  $33.54  P&L $-0.17                 |
|  2026-09-25  SELL  GOOG  Pullback50  $33.59  P&L $-0.01                |
|  2026-09-25  SELL  GOOGL  Pullback50  $33.59  P&L $-0.01               |
|  2026-09-25  SELL  KNF  MomReversal  $33.28  P&L $-0.47                |
|  2026-09-24  SELL  AES  Pullback50  $33.74  P&L $-0.02                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T09:06:19.589600-04:00 share=25% ===
2026-09-28 09:06:19,589 INFO === options_live_micro LIVE 2026-09-28T09:06:19.589600-04:00 share=25% ===
Live account equity $224.16 cash $156.73 #225458845 options_level=3
2026-09-28 09:06:19,778 INFO Live account equity $224.16 cash $156.73 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-28 09:06:19,853 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-28 09:06:19,909 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 293 | 21 |
| S164 | 333 | 24 |
| S165 | 1759 | 36 |
| S166 | 139 | 10 |
| S167 | 316 | 23 |
| S168 | 236 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    77 | INFO |
| Total closed lots           |  2539 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1508 med=+8.6% | TAINTED n=1908 med=-38.8% | KEEP-only n=798 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T131117Z

- UTC timestamp: `20260928T131117Z`
- GitHub run: [#11165](https://github.com/28twagg-ops/TradingBot/actions/runs/36426670662)
- Run id: `36426670662`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`23s`
- Full logs: `logs/action_runs/20260928T131117Z_live_bot.log`, `logs/action_runs/20260928T131117Z_live_options.log`, `logs/action_runs/20260928T131117Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1508 | 50.2 | +8.6 | +43.6 | $+19,714 |
| TAINTED | 1908 | 33.4 | -38.8 | +12.7 | $-9,602 |
| KEEP-only | 798 | 63.3 | +52.8 | +66.8 | $+13,806 |
| KEEP-only recent | 603 | 62.5 | +56.9 | +76.9 | $+9,721 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:11:22.767778-04:00","date":"2026-09-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":10.9,"phases_s":{"reconcile":4.15},"signals":0,"placed":0,"equity":996963.17,"open_positions":18,"pending_orders":0,"open_lots":77,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11165","github_run_id":"36426670662","status":"ok","data_quality":{"clean":{"n":1508,"win":50.2,"med":8.63,"avg":43.62,"pnl":19714.16},"tainted":{"n":1908,"win":33.39,"med":-38.81,"avg":12.66,"pnl":-9602.28},"keep_only":{"n":798,"win":63.28,"med":52.75,"avg":66.75,"pnl":13806.45},"keep_only_recent":{"n":603,"win":62.52,"med":56.92,"avg":76.9,"pnl":9721.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:11:19  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.20|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.20|
|  Cash                                                           $156.73|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.47|
|  Open P&L                                                        $+0.33|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CVS      MomReversal     $33.71     $89.14   $89.50   +0.4%   $+0.14  |
|  EVR      MomReversal     $33.76     $262.43  $263.91  +0.6%   $+0.19  |
|                                                                        |
|  Total invested                                                  $67.47|
|  Total open P&L                                                  $+0.33|
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
|  2026-09-25  SELL  AYI  MomReversal  $33.58  P&L $+0.01                |
|  2026-09-25  SELL  COP  Pullback50  $33.54  P&L $-0.17                 |
|  2026-09-25  SELL  GOOG  Pullback50  $33.59  P&L $-0.01                |
|  2026-09-25  SELL  GOOGL  Pullback50  $33.59  P&L $-0.01               |
|  2026-09-25  SELL  KNF  MomReversal  $33.28  P&L $-0.47                |
|  2026-09-24  SELL  AES  Pullback50  $33.74  P&L $-0.02                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T09:11:20.043324-04:00 share=25% ===
2026-09-28 09:11:20,043 INFO === options_live_micro LIVE 2026-09-28T09:11:20.043324-04:00 share=25% ===
Live account equity $224.20 cash $156.73 #225458845 options_level=3
2026-09-28 09:11:20,087 INFO Live account equity $224.20 cash $156.73 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-28 09:11:20,096 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-28 09:11:20,103 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 293 | 21 |
| S164 | 333 | 24 |
| S165 | 1759 | 36 |
| S166 | 139 | 10 |
| S167 | 316 | 23 |
| S168 | 236 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    77 | INFO |
| Total closed lots           |  2539 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1508 med=+8.6% | TAINTED n=1908 med=-38.8% | KEEP-only n=798 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.2 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T131625Z

- UTC timestamp: `20260928T131625Z`
- GitHub run: [#11166](https://github.com/28twagg-ops/TradingBot/actions/runs/36427265384)
- Run id: `36427265384`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260928T131625Z_live_bot.log`, `logs/action_runs/20260928T131625Z_live_options.log`, `logs/action_runs/20260928T131625Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1508 | 50.2 | +8.6 | +43.6 | $+19,714 |
| TAINTED | 1908 | 33.4 | -38.8 | +12.7 | $-9,602 |
| KEEP-only | 798 | 63.3 | +52.8 | +66.8 | $+13,806 |
| KEEP-only recent | 603 | 62.5 | +56.9 | +76.9 | $+9,721 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:16:31.071320-04:00","date":"2026-09-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.8,"phases_s":{"reconcile":4.86},"signals":0,"placed":0,"equity":996963.17,"open_positions":18,"pending_orders":0,"open_lots":77,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11166","github_run_id":"36427265384","status":"ok","data_quality":{"clean":{"n":1508,"win":50.2,"med":8.63,"avg":43.62,"pnl":19714.16},"tainted":{"n":1908,"win":33.39,"med":-38.81,"avg":12.66,"pnl":-9602.28},"keep_only":{"n":798,"win":63.28,"med":52.75,"avg":66.75,"pnl":13806.45},"keep_only_recent":{"n":603,"win":62.52,"med":56.92,"avg":76.9,"pnl":9721.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:16:26  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.20|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.20|
|  Cash                                                           $156.73|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.47|
|  Open P&L                                                        $+0.33|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CVS      MomReversal     $33.71     $89.14   $89.52   +0.4%   $+0.14  |
|  EVR      MomReversal     $33.76     $262.43  $263.91  +0.6%   $+0.19  |
|                                                                        |
|  Total invested                                                  $67.47|
|  Total open P&L                                                  $+0.33|
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
|  2026-09-25  SELL  AYI  MomReversal  $33.58  P&L $+0.01                |
|  2026-09-25  SELL  COP  Pullback50  $33.54  P&L $-0.17                 |
|  2026-09-25  SELL  GOOG  Pullback50  $33.59  P&L $-0.01                |
|  2026-09-25  SELL  GOOGL  Pullback50  $33.59  P&L $-0.01               |
|  2026-09-25  SELL  KNF  MomReversal  $33.28  P&L $-0.47                |
|  2026-09-24  SELL  AES  Pullback50  $33.74  P&L $-0.02                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T09:16:28.245843-04:00 share=25% ===
2026-09-28 09:16:28,245 INFO === options_live_micro LIVE 2026-09-28T09:16:28.245843-04:00 share=25% ===
Live account equity $224.20 cash $156.73 #225458845 options_level=3
2026-09-28 09:16:28,439 INFO Live account equity $224.20 cash $156.73 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-28 09:16:28,502 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-28 09:16:28,559 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 293 | 21 |
| S164 | 333 | 24 |
| S165 | 1759 | 36 |
| S166 | 139 | 10 |
| S167 | 316 | 23 |
| S168 | 236 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    77 | INFO |
| Total closed lots           |  2539 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1508 med=+8.6% | TAINTED n=1908 med=-38.8% | KEEP-only n=798 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.2 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T132122Z

- UTC timestamp: `20260928T132122Z`
- GitHub run: [#11167](https://github.com/28twagg-ops/TradingBot/actions/runs/36427867423)
- Run id: `36427867423`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`25s`
- Full logs: `logs/action_runs/20260928T132122Z_live_bot.log`, `logs/action_runs/20260928T132122Z_live_options.log`, `logs/action_runs/20260928T132122Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1508 | 50.2 | +8.6 | +43.6 | $+19,714 |
| TAINTED | 1908 | 33.4 | -38.8 | +12.7 | $-9,602 |
| KEEP-only | 798 | 63.3 | +52.8 | +66.8 | $+13,806 |
| KEEP-only recent | 603 | 62.5 | +56.9 | +76.9 | $+9,721 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:21:29.714547-04:00","date":"2026-09-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.9,"phases_s":{"reconcile":4.78},"signals":0,"placed":0,"equity":996963.17,"open_positions":18,"pending_orders":0,"open_lots":77,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11167","github_run_id":"36427867423","status":"ok","data_quality":{"clean":{"n":1508,"win":50.2,"med":8.63,"avg":43.62,"pnl":19714.16},"tainted":{"n":1908,"win":33.39,"med":-38.81,"avg":12.66,"pnl":-9602.28},"keep_only":{"n":798,"win":63.28,"med":52.75,"avg":66.75,"pnl":13806.45},"keep_only_recent":{"n":603,"win":62.52,"med":56.92,"avg":76.9,"pnl":9721.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:21:23  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.01|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.01|
|  Cash                                                           $156.73|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.28|
|  Open P&L                                                        $+0.14|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CVS      MomReversal     $33.71     $89.14   $89.52   +0.4%   $+0.14  |
|  EVR      MomReversal     $33.57     $262.43  $262.41  -0.0%   $-0.00  |
|                                                                        |
|  Total invested                                                  $67.28|
|  Total open P&L                                                  $+0.14|
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
|  2026-09-25  SELL  AYI  MomReversal  $33.58  P&L $+0.01                |
|  2026-09-25  SELL  COP  Pullback50  $33.54  P&L $-0.17                 |
|  2026-09-25  SELL  GOOG  Pullback50  $33.59  P&L $-0.01                |
|  2026-09-25  SELL  GOOGL  Pullback50  $33.59  P&L $-0.01               |
|  2026-09-25  SELL  KNF  MomReversal  $33.28  P&L $-0.47                |
|  2026-09-24  SELL  AES  Pullback50  $33.74  P&L $-0.02                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T09:21:26.094727-04:00 share=25% ===
2026-09-28 09:21:26,094 INFO === options_live_micro LIVE 2026-09-28T09:21:26.094727-04:00 share=25% ===
Live account equity $224.01 cash $156.73 #225458845 options_level=3
2026-09-28 09:21:26,341 INFO Live account equity $224.01 cash $156.73 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-28 09:21:26,415 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-28 09:21:26,488 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 293 | 21 |
| S164 | 333 | 24 |
| S165 | 1759 | 36 |
| S166 | 139 | 10 |
| S167 | 316 | 23 |
| S168 | 236 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    77 | INFO |
| Total closed lots           |  2539 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1508 med=+8.6% | TAINTED n=1908 med=-38.8% | KEEP-only n=798 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.01 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T132628Z

- UTC timestamp: `20260928T132628Z`
- GitHub run: [#11168](https://github.com/28twagg-ops/TradingBot/actions/runs/36428453493)
- Run id: `36428453493`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260928T132628Z_live_bot.log`, `logs/action_runs/20260928T132628Z_live_options.log`, `logs/action_runs/20260928T132628Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1508 | 50.2 | +8.6 | +43.6 | $+19,714 |
| TAINTED | 1908 | 33.4 | -38.8 | +12.7 | $-9,602 |
| KEEP-only | 798 | 63.3 | +52.8 | +66.8 | $+13,806 |
| KEEP-only recent | 603 | 62.5 | +56.9 | +76.9 | $+9,721 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:26:34.508343-04:00","date":"2026-09-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.4,"phases_s":{"reconcile":4.51},"signals":0,"placed":0,"equity":996963.17,"open_positions":18,"pending_orders":0,"open_lots":77,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11168","github_run_id":"36428453493","status":"ok","data_quality":{"clean":{"n":1508,"win":50.2,"med":8.63,"avg":43.62,"pnl":19714.16},"tainted":{"n":1908,"win":33.39,"med":-38.81,"avg":12.66,"pnl":-9602.28},"keep_only":{"n":798,"win":63.28,"med":52.75,"avg":66.75,"pnl":13806.45},"keep_only_recent":{"n":603,"win":62.52,"med":56.92,"avg":76.9,"pnl":9721.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:26:29  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.01|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.01|
|  Cash                                                           $156.73|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.28|
|  Open P&L                                                        $+0.14|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CVS      MomReversal     $33.71     $89.14   $89.52   +0.4%   $+0.14  |
|  EVR      MomReversal     $33.57     $262.43  $262.41  -0.0%   $-0.00  |
|                                                                        |
|  Total invested                                                  $67.28|
|  Total open P&L                                                  $+0.14|
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
|  2026-09-25  SELL  AYI  MomReversal  $33.58  P&L $+0.01                |
|  2026-09-25  SELL  COP  Pullback50  $33.54  P&L $-0.17                 |
|  2026-09-25  SELL  GOOG  Pullback50  $33.59  P&L $-0.01                |
|  2026-09-25  SELL  GOOGL  Pullback50  $33.59  P&L $-0.01               |
|  2026-09-25  SELL  KNF  MomReversal  $33.28  P&L $-0.47                |
|  2026-09-24  SELL  AES  Pullback50  $33.74  P&L $-0.02                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T09:26:31.006751-04:00 share=25% ===
2026-09-28 09:26:31,006 INFO === options_live_micro LIVE 2026-09-28T09:26:31.006751-04:00 share=25% ===
Live account equity $224.01 cash $156.73 #225458845 options_level=3
2026-09-28 09:26:31,172 INFO Live account equity $224.01 cash $156.73 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-28 09:26:31,216 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-28 09:26:31,260 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 293 | 21 |
| S164 | 333 | 24 |
| S165 | 1759 | 36 |
| S166 | 139 | 10 |
| S167 | 316 | 23 |
| S168 | 236 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    77 | INFO |
| Total closed lots           |  2539 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1508 med=+8.6% | TAINTED n=1908 med=-38.8% | KEEP-only n=798 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.01 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T133125Z

- UTC timestamp: `20260928T133125Z`
- GitHub run: [#11169](https://github.com/28twagg-ops/TradingBot/actions/runs/36429045855)
- Run id: `36429045855`
- Live bot: exit=`0`, duration=`215s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T133125Z_live_bot.log`, `logs/action_runs/20260928T133125Z_live_options.log`, `logs/action_runs/20260928T133125Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1508 | 50.2 | +8.6 | +43.6 | $+19,714 |
| TAINTED | 1908 | 33.4 | -38.8 | +12.7 | $-9,602 |
| KEEP-only | 798 | 63.3 | +52.8 | +66.8 | $+13,806 |
| KEEP-only recent | 603 | 62.5 | +56.9 | +76.9 | $+9,721 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:26:34.508343-04:00","date":"2026-09-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.4,"phases_s":{"reconcile":4.51},"signals":0,"placed":0,"equity":996963.17,"open_positions":18,"pending_orders":0,"open_lots":77,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11168","github_run_id":"36428453493","status":"ok","data_quality":{"clean":{"n":1508,"win":50.2,"med":8.63,"avg":43.62,"pnl":19714.16},"tainted":{"n":1908,"win":33.39,"med":-38.81,"avg":12.66,"pnl":-9602.28},"keep_only":{"n":798,"win":63.28,"med":52.75,"avg":66.75,"pnl":13806.45},"keep_only_recent":{"n":603,"win":62.52,"med":56.92,"avg":76.9,"pnl":9721.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:31:26  INFO      Mode: morning_prep
13:31:26  INFO        [prep_positions] 2/2 (2 valid)
13:31:26  INFO      Fetching tickers (universe=both)...
13:31:27  INFO        S&P 500: 503
13:31:27  INFO        MidCap 400: 400
13:31:27  INFO        Total: 903 tickers
13:31:28  INFO        [prep_universe] 40/901 (40 valid)
13:31:29  INFO        [prep_universe] 80/901 (80 valid)
13:31:30  INFO        [prep_universe] 120/901 (120 valid)
13:31:32  INFO        [prep_universe] 160/901 (160 valid)
13:31:33  INFO        [prep_universe] 200/901 (199 valid)
13:31:40  INFO        [prep_universe] 240/901 (238 valid)
13:31:53  INFO        [prep_universe] 280/901 (278 valid)
13:32:06  INFO        [prep_universe] 320/901 (318 valid)
13:32:16  INFO        [prep_universe] 360/901 (358 valid)
13:32:29  INFO        [prep_universe] 400/901 (398 valid)
13:32:39  INFO        [prep_universe] 440/901 (438 valid)
13:32:52  INFO        [prep_universe] 480/901 (478 valid)
13:33:05  INFO        [prep_universe] 520/901 (518 valid)
13:33:16  INFO        [prep_universe] 560/901 (558 valid)
13:33:28  INFO        [prep_universe] 600/901 (598 valid)
13:33:41  INFO        [prep_universe] 640/901 (638 valid)
13:33:51  INFO        [prep_universe] 680/901 (678 valid)
13:34:05  INFO        [prep_universe] 720/901 (718 valid)
13:34:18  INFO        [prep_universe] 760/901 (758 valid)
13:34:28  INFO        [prep_universe] 800/901 (798 valid)
13:34:41  INFO        [prep_universe] 840/901 (838 valid)
13:34:54  INFO        [prep_universe] 880/901 (878 valid)
13:34:58  INFO        [prep_universe] 901/901 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.82|
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
|  Open positions                                                       2|
|  Invested                                                        $67.09|
|  Open P&L                                                        $-0.05|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CVS      MomReversal     $33.64     $89.14   $89.33   +0.2%   $+0.07  |
|  EVR      MomReversal     $33.45     $262.43  $261.48  -0.4%   $-0.12  |
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
|  Exit candidates                                                      2|
|  Signal candidates                                                   16|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T09:35:01.056841-04:00 share=25% ===
2026-09-28 09:35:01,056 INFO === options_live_micro LIVE 2026-09-28T09:35:01.056841-04:00 share=25% ===
Live account equity $223.15 cash $156.73 #225458845 options_level=3
2026-09-28 09:35:01,416 INFO Live account equity $223.15 cash $156.73 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 09:35:01,484 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 09:35:01,571 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=77 paper_keys=yes dry_run=False
  alpaca positions=20
  FLAG b165|S216|5d7c0be9 missing from Alpaca
  FLAG b164|S216|5ffa0bf9 missing from Alpaca
  FLAG b235|S401|f217bb6f missing from Alpaca
  FLAG b234|S401|fbe8f114 missing from Alpaca
  FLAG b193|S218|2903f4ed missing from Alpaca
  FLAG b0|ORPHAN|7b0f4512 missing from Alpaca
  FLAG b179|S217|29d1def0 missing from Alpaca
  FLAG b178|S217|e851d44d missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$995,925.10
  buying_power=$3,852,911.19 cash=$975,894.11
  open option orders: 8
    XOM261002C00170000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    DKNG261002C00021500 OrderSide.SELL qty=22 status=OrderStatus.NEW limit=None
    DKNG261009C00022500 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    NKE261002C00039500 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    NKE261002C00038500 OrderSide.SELL qty=6 status=OrderStatus.NEW limit=None
  open option positions: 16
    DKNG261002C00021000 qty=4 mkt=$320.00
    DKNG261002C00021500 qty=22 mkt=$1,386.00
    DKNG261002C00022000 qty=4 mkt=$176.00
    DKNG261002C00022500 qty=2 mkt=$42.00
    DKNG261009C00022500 qty=2 mkt=$84.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-28T09:35:04.631133-04:00 ===

[Run context]
Paper auth OK — equity $995930.11, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-28 09:35:07,016 INFO   EXIT [b318|lab0318_s355_w4_1120_1135_r1|S355] stop_loss (-57.1%) SELL 1 MARA261002C00013500 @<= 0.19
  EXIT [b86|lab0086_s210_w4_1120_1135_r1|S210] stop_loss (-89.3%) SELL failed SPY260928C00775000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=5 upgraded=0 already=9 failed=1 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260928T133653Z

- UTC timestamp: `20260928T133653Z`
- GitHub run: [#11170](https://github.com/28twagg-ops/TradingBot/actions/runs/36429632432)
- Run id: `36429632432`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T133653Z_live_bot.log`, `logs/action_runs/20260928T133653Z_live_options.log`, `logs/action_runs/20260928T133653Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1508 | 50.2 | +8.6 | +43.6 | $+19,714 |
| TAINTED | 1908 | 33.4 | -38.8 | +12.7 | $-9,602 |
| KEEP-only | 798 | 63.3 | +52.8 | +66.8 | $+13,806 |
| KEEP-only recent | 603 | 62.5 | +56.9 | +76.9 | $+9,721 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:26:34.508343-04:00","date":"2026-09-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.4,"phases_s":{"reconcile":4.51},"signals":0,"placed":0,"equity":996963.17,"open_positions":18,"pending_orders":0,"open_lots":77,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11168","github_run_id":"36428453493","status":"ok","data_quality":{"clean":{"n":1508,"win":50.2,"med":8.63,"avg":43.62,"pnl":19714.16},"tainted":{"n":1908,"win":33.39,"med":-38.81,"avg":12.66,"pnl":-9602.28},"keep_only":{"n":798,"win":63.28,"med":52.75,"avg":66.75,"pnl":13806.45},"keep_only_recent":{"n":603,"win":62.52,"med":56.92,"avg":76.9,"pnl":9721.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:36:54  INFO      Mode: morning_prep
13:36:55  INFO        [prep_positions] 2/2 (2 valid)
13:36:55  INFO      Fetching tickers (universe=both)...
13:36:55  INFO        S&P 500: 503
13:36:55  INFO        MidCap 400: 400
13:36:55  INFO        Total: 903 tickers
13:36:56  INFO        [prep_universe] 40/901 (40 valid)
13:36:57  INFO        [prep_universe] 80/901 (80 valid)
13:36:59  INFO        [prep_universe] 120/901 (120 valid)
13:37:00  INFO        [prep_universe] 160/901 (160 valid)
13:37:01  INFO        [prep_universe] 200/901 (199 valid)
13:37:08  INFO        [prep_universe] 240/901 (238 valid)
13:37:21  INFO        [prep_universe] 280/901 (278 valid)
13:37:34  INFO        [prep_universe] 320/901 (318 valid)
13:37:44  INFO        [prep_universe] 360/901 (358 valid)
13:37:57  INFO        [prep_universe] 400/901 (398 valid)
13:38:10  INFO        [prep_universe] 440/901 (438 valid)
13:38:20  INFO        [prep_universe] 480/901 (478 valid)
13:38:33  INFO        [prep_universe] 520/901 (518 valid)
13:38:46  INFO        [prep_universe] 560/901 (558 valid)
13:38:58  INFO        [prep_universe] 600/901 (598 valid)
13:39:08  INFO        [prep_universe] 640/901 (638 valid)
13:39:21  INFO        [prep_universe] 680/901 (678 valid)
13:39:34  INFO        [prep_universe] 720/901 (718 valid)
13:39:44  INFO        [prep_universe] 760/901 (758 valid)
13:39:57  INFO        [prep_universe] 800/901 (798 valid)
13:40:10  INFO        [prep_universe] 840/901 (838 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260928T134151Z

- UTC timestamp: `20260928T134151Z`
- GitHub run: [#11171](https://github.com/28twagg-ops/TradingBot/actions/runs/36430227046)
- Run id: `36430227046`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T134151Z_live_bot.log`, `logs/action_runs/20260928T134151Z_live_options.log`, `logs/action_runs/20260928T134151Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1508 | 50.2 | +8.6 | +43.6 | $+19,714 |
| TAINTED | 1908 | 33.4 | -38.8 | +12.7 | $-9,602 |
| KEEP-only | 798 | 63.3 | +52.8 | +66.8 | $+13,806 |
| KEEP-only recent | 603 | 62.5 | +56.9 | +76.9 | $+9,721 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:26:34.508343-04:00","date":"2026-09-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.4,"phases_s":{"reconcile":4.51},"signals":0,"placed":0,"equity":996963.17,"open_positions":18,"pending_orders":0,"open_lots":77,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11168","github_run_id":"36428453493","status":"ok","data_quality":{"clean":{"n":1508,"win":50.2,"med":8.63,"avg":43.62,"pnl":19714.16},"tainted":{"n":1908,"win":33.39,"med":-38.81,"avg":12.66,"pnl":-9602.28},"keep_only":{"n":798,"win":63.28,"med":52.75,"avg":66.75,"pnl":13806.45},"keep_only_recent":{"n":603,"win":62.52,"med":56.92,"avg":76.9,"pnl":9721.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:41:52  INFO      Mode: morning_prep
13:41:53  INFO        [prep_positions] 2/2 (2 valid)
13:41:53  INFO        Universe cache hit: 903 tickers (tickers_2026-09-28.json)
13:41:54  INFO        [prep_universe] 40/901 (40 valid)
13:41:55  INFO        [prep_universe] 80/901 (80 valid)
13:41:56  INFO        [prep_universe] 120/901 (120 valid)
13:41:58  INFO        [prep_universe] 160/901 (160 valid)
13:41:59  INFO        [prep_universe] 200/901 (199 valid)
13:42:06  INFO        [prep_universe] 240/901 (238 valid)
13:42:19  INFO        [prep_universe] 280/901 (278 valid)
13:42:32  INFO        [prep_universe] 320/901 (318 valid)
13:42:42  INFO        [prep_universe] 360/901 (358 valid)
13:42:55  INFO        [prep_universe] 400/901 (398 valid)
13:43:06  INFO        [prep_universe] 440/901 (438 valid)
13:43:19  INFO        [prep_universe] 480/901 (478 valid)
13:43:32  INFO        [prep_universe] 520/901 (518 valid)
13:43:42  INFO        [prep_universe] 560/901 (558 valid)
13:43:55  INFO        [prep_universe] 600/901 (598 valid)
13:44:08  INFO        [prep_universe] 640/901 (638 valid)
13:44:19  INFO        [prep_universe] 680/901 (678 valid)
13:44:32  INFO        [prep_universe] 720/901 (718 valid)
13:44:42  INFO        [prep_universe] 760/901 (758 valid)
13:44:55  INFO        [prep_universe] 800/901 (798 valid)
13:45:08  INFO        [prep_universe] 840/901 (838 valid)
13:45:18  INFO        [prep_universe] 880/901 (878 valid)
13:45:26  INFO        [prep_universe] 901/901 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.20|
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
|  Open positions                                                       2|
|  Invested                                                        $66.47|
|  Open P&L                                                        $-0.67|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CVS      MomReversal     $33.53     $89.14   $89.03   -0.1%   $-0.04  |
|  EVR      MomReversal     $32.95     $262.43  $257.55  -1.9%   $-0.62  |
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
|  Exit candidates                                                      2|
|  Signal candidates                                                   34|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T09:45:28.835562-04:00 share=25% ===
2026-09-28 09:45:28,835 INFO === options_live_micro LIVE 2026-09-28T09:45:28.835562-04:00 share=25% ===
Live account equity $223.74 cash $156.73 #225458845 options_level=3
2026-09-28 09:45:28,953 INFO Live account equity $223.74 cash $156.73 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 09:45:29,051 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 09:45:29,117 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text

```

---

## Run 20260928T134715Z

- UTC timestamp: `20260928T134715Z`
- GitHub run: [#11172](https://github.com/28twagg-ops/TradingBot/actions/runs/36430830658)
- Run id: `36430830658`
- Live bot: exit=`0`, duration=`56s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T134715Z_live_bot.log`, `logs/action_runs/20260928T134715Z_live_options.log`, `logs/action_runs/20260928T134715Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1508 | 50.2 | +8.6 | +43.6 | $+19,714 |
| TAINTED | 1908 | 33.4 | -38.8 | +12.7 | $-9,602 |
| KEEP-only | 798 | 63.3 | +52.8 | +66.8 | $+13,806 |
| KEEP-only recent | 603 | 62.5 | +56.9 | +76.9 | $+9,721 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:26:34.508343-04:00","date":"2026-09-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.4,"phases_s":{"reconcile":4.51},"signals":0,"placed":0,"equity":996963.17,"open_positions":18,"pending_orders":0,"open_lots":77,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11168","github_run_id":"36428453493","status":"ok","data_quality":{"clean":{"n":1508,"win":50.2,"med":8.63,"avg":43.62,"pnl":19714.16},"tainted":{"n":1908,"win":33.39,"med":-38.81,"avg":12.66,"pnl":-9602.28},"keep_only":{"n":798,"win":63.28,"med":52.75,"avg":66.75,"pnl":13806.45},"keep_only_recent":{"n":603,"win":62.52,"med":56.92,"avg":76.9,"pnl":9721.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
... (123 earlier lines - see full log file)
|  RNR      Pullback50      eq     $326.53  56.3   -2.10   50MA bounce (+|
|  TTC      Pullback50      eq     $96.85   60.7   -1.87   50MA bounce (+|
|  UNM      Pullback50      eq     $91.61   41.2   -1.51   50MA bounce (+|13:47:41  INFO        BUY  AES  $33.58  [Pullback50]  id=2603368f-ad1f-4610-a3e2-6e6843c3d02a
13:47:41  INFO        BUY  AKAM  $33.58  [Pullback50]  id=3b859902-6edc-4aca-a5cf-c6b73f20fb7a
13:47:41  INFO        BUY  GOOGL  $33.58  [Pullback50]  id=3660ac1c-4c58-4ccd-96db-2b046e41b98e
13:48:11  INFO        place_all_stops: checking 3 positions...
13:48:11  INFO        STOP-MARKET placed AES  qty=2 (pos=2.2563)  stop=$14.80  id=43881840-a6e3-4c98-9dff-9b85aaf9f451
13:48:11  INFO        STOP skipped AKAM: fractional (0.2986 shares) — software exit will handle it
13:48:11  INFO        STOP skipped GOOGL: fractional (0.0979 shares) — software exit will handle it
13:48:11  INFO        Daily log -> logs/daily/2026-09-28.md
13:48:11  INFO        Dashboard written → logs/dashboard.md

|  WTS      Pullback50      eq     $357.67  45.7   -1.74   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] AES  Pullback50                                    $33.58|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] AKAM  Pullback50                                   $33.58|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] GOOGL  Pullback50                                  $33.58|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] MO  Pullback50                                       cap 3|
|    SKIP [eq] GOOG  Pullback50                                     cap 3|
|    SKIP [eq] TECH  Pullback50                                     cap 3|
|    SKIP [eq] ECL  Pullback50                                      cap 3|
|    SKIP [eq] FCX  Pullback50                                      cap 3|
|    SKIP [eq] IEX  Pullback50                                      cap 3|
|    SKIP [eq] INCY  Pullback50                                     cap 3|
|    SKIP [eq] LLY  Pullback50                                      cap 3|
|    SKIP [eq] MSI  Pullback50                                      cap 3|
|    SKIP [eq] PM  Pullback50                                       cap 3|
|    SKIP [eq] DGX  Pullback50                                      cap 3|
|    SKIP [eq] ROST  Pullback50                                     cap 3|
|    SKIP [eq] TT  Pullback50                                       cap 3|
|    SKIP [eq] V  Pullback50                                        cap 3|
|    SKIP [eq] ITT  Pullback50                                      cap 3|
|    SKIP [eq] MOG-A  Pullback50                                    cap 3|
|    SKIP [eq] MSM  Pullback50                                      cap 3|
|    SKIP [eq] QLYS  Pullback50                                     cap 3|
|    SKIP [eq] RNR  Pullback50                                      cap 3|
|    SKIP [eq] TTC  Pullback50                                      cap 3|
|    SKIP [eq] UNM  Pullback50                                      cap 3|
|    SKIP [eq] WTS  Pullback50                                      cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      3|
+------------------------------------------------------------------------+
|  AES                                                  still unconfirmed|
|  AKAM                                                 still unconfirmed|
|  GOOGL                                                still unconfirmed|
+========================================================================+
+========================================================================+

+========================================================================+
|                           GTC STOP PLACEMENT                           |
+========================================================================+
|  Waiting 5s for 3 buy submit(s) to settle...                           |
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |
+========================================================================+
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Strategy  GapDown + VolumeSpike (display only — schedule not enforced)|
|  Scanned                                                              0|
|  Signals                                                             25|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  3 unconfirmed|
|  Exits                                                                2|
|  Open pos                                                             3|
|  Equity                                                         $223.61|
|  Cash                                                           $122.96|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T09:48:12.352751-04:00 share=25% ===
2026-09-28 09:48:12,352 INFO === options_live_micro LIVE 2026-09-28T09:48:12.352751-04:00 share=25% ===
Live account equity $223.62 cash $122.96 #225458845 options_level=3
2026-09-28 09:48:12,488 INFO Live account equity $223.62 cash $122.96 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 09:48:12,605 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 09:48:12,677 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=77 paper_keys=yes dry_run=False
  alpaca positions=20
  FLAG b165|S216|5d7c0be9 missing from Alpaca
  FLAG b164|S216|5ffa0bf9 missing from Alpaca
  FLAG b235|S401|f217bb6f missing from Alpaca
  FLAG b234|S401|fbe8f114 missing from Alpaca
  FLAG b193|S218|2903f4ed missing from Alpaca
  FLAG b0|ORPHAN|7b0f4512 missing from Alpaca
  FLAG b179|S217|29d1def0 missing from Alpaca
  FLAG b178|S217|e851d44d missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,010.59
  buying_power=$3,854,287.16 cash=$975,914.09
  open option orders: 13
    DKNG261002C00022500 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    DKNG261002C00022000 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
    DKNG261002C00021000 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
    MARA261016C00014500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    SMCI261002C00044500 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
  open option positions: 16
    DKNG261002C00021000 qty=4 mkt=$300.00
    DKNG261002C00021500 qty=22 mkt=$1,056.00
    DKNG261002C00022000 qty=4 mkt=$124.00
    DKNG261002C00022500 qty=2 mkt=$36.00
    DKNG261009C00022500 qty=2 mkt=$80.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-28T09:48:15.156437-04:00 ===

[Run context]
Paper auth OK — equity $996009.08, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b86|lab0086_s210_w4_1120_1135_r1|S210] stop_loss (-91.1%) SELL failed SPY260928C00775000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=1 upgraded=0 already=13 failed=1 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
Found 464 signal(s); top: ['S401:PLTR', 'S359:PLTR', 'S361:PLTR', 'S362:PLTR', 'S363:PLTR', 'S364:PLTR', 'S365:PLTR', 'S366:PLTR']
Paper lab: $996009 broker equity -> 1164 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260928T135205Z

- UTC timestamp: `20260928T135205Z`
- GitHub run: [#11173](https://github.com/28twagg-ops/TradingBot/actions/runs/36431443478)
- Run id: `36431443478`
- Live bot: exit=`0`, duration=`93s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T135205Z_live_bot.log`, `logs/action_runs/20260928T135205Z_live_options.log`, `logs/action_runs/20260928T135205Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1508 | 50.2 | +8.6 | +43.6 | $+19,714 |
| TAINTED | 1908 | 33.4 | -38.8 | +12.7 | $-9,602 |
| KEEP-only | 798 | 63.3 | +52.8 | +66.8 | $+13,806 |
| KEEP-only recent | 603 | 62.5 | +56.9 | +76.9 | $+9,721 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:26:34.508343-04:00","date":"2026-09-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.4,"phases_s":{"reconcile":4.51},"signals":0,"placed":0,"equity":996963.17,"open_positions":18,"pending_orders":0,"open_lots":77,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11168","github_run_id":"36428453493","status":"ok","data_quality":{"clean":{"n":1508,"win":50.2,"med":8.63,"avg":43.62,"pnl":19714.16},"tainted":{"n":1908,"win":33.39,"med":-38.81,"avg":12.66,"pnl":-9602.28},"keep_only":{"n":798,"win":63.28,"med":52.75,"avg":66.75,"pnl":13806.45},"keep_only_recent":{"n":603,"win":62.52,"med":56.92,"avg":76.9,"pnl":9721.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
... (80 earlier lines - see full log file)
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 3 | filled 3 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 0|
|  Stop-loss breaches                                                none|
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+

+========================================================================+
|                             DATA DOWNLOAD                              |
+========================================================================+
|  Universe: both  |  Alpaca primary / yfinance fallback                 |
+========================================================================+

+========================================================================+
|                              SIGNAL SCAN                               |
+========================================================================+
|  Month: Sep  |  Regime: BULL                                           |
|  Primary: GapDown  |  Secondary: VolumeSpike (display only — schedule ~|
|  Source                          cached signals (signals fresh (11.6m))|
|  Universe scanned in prep                                           901|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  25                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AES      Pullback50      eq     $14.87   60.0   -2.34   50MA bounce (+|
|  AKAM     Pullback50      eq     $113.39  59.1   -0.64   50MA bounce (+|
|  GOOGL    Pullback50      eq     $342.47  52.9   -2.63   50MA bounce (-|
|  MO       Pullback50      eq     $69.16   57.6   -2.62   50MA bounce (+|
|  GOOG     Pullback50      eq     $338.92  52.7   -2.46   50MA bounce (-|
|  TECH     Pullback50      eq     $72.58   64.6   -2.44   50MA bounce (+|
|  ECL      Pullback50      eq     $278.29  50.3   -2.45   50MA bounce (+|
|  FCX      Pullback50      eq     $70.08   31.1   -2.39   50MA bounce (+|
|  IEX      Pullback50      eq     $230.22  59.3   -2.56   50MA bounce (+|
|  INCY     Pullback50      eq     $123.88  48.8   -2.09   50MA bounce (+|
|  LLY      Pullback50      eq     $1188.~  75.9   -2.64   50MA bounce (+|
|  MSI      Pullback50      eq     $456.45  43.7   -2.57   50MA bounce (-|
|  PM       Pullback50      eq     $191.33  64.1   -2.20   50MA bounce (+|
|  DGX      Pullback50      eq     $235.81  50.4   -2.00   50MA bounce (-|
|  ROST     Pullback50      eq     $237.11  61.6   -2.52   50MA bounce (-|
|  TT       Pullback50      eq     $452.12  54.6   -2.52   50MA bounce (-|
|  V        Pullback50      eq     $368.14  49.3   -1.50   50MA bounce (-|
|  ITT      Pullback50      eq     $205.80  54.2   -1.90   50MA bounce (+|
|  MOG-A    Pullback50      eq     $387.81  66.3   -1.51   50MA bounce (-|
|  MSM      Pullback50      eq     $121.86  55.2   -2.02   50MA bounce (+|
|  QLYS     Pullback50      eq     $171.02  50.4   -2.08   50MA bounce (+|
|  RNR      Pullback50      eq     $326.53  56.3   -2.10   50MA bounce (+|
|  TTC      Pullback50      eq     $96.85   60.7   -1.87   50MA bounce (+|13:53:38  INFO        Daily log -> logs/daily/2026-09-28.md
13:53:38  INFO        Dashboard written → logs/dashboard.md

|  UNM      Pullback50      eq     $91.61   41.2   -1.51   50MA bounce (+|
|  WTS      Pullback50      eq     $357.67  45.7   -1.74   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|  Skipped                                  no entry slots (max_trades=0)|
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |
+========================================================================+
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Strategy  GapDown + VolumeSpike (display only — schedule not enforced)|
|  Scanned                                                              0|
|  Signals                                                             25|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                3|
|  Open pos                                                             0|
|  Equity                                                         $223.66|
|  Cash                                                           $223.66|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T09:53:39.021959-04:00 share=25% ===
2026-09-28 09:53:39,022 INFO === options_live_micro LIVE 2026-09-28T09:53:39.021959-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 09:53:39,096 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 09:53:39,139 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 09:53:39,169 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=69 paper_keys=yes dry_run=False
  alpaca positions=24
  FLAG b318|S355|c3aa6da9 missing from Alpaca
  FLAG b311|S354|6ee30227 missing from Alpaca
  FLAG b310|S354|45a22a8b missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,012.91
  buying_power=$3,849,929.26 cash=$975,012.53
  open option orders: 20
    MSFT260928C00510000 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
    MCD261002C00242500 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    CVNA261002C00070000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.14
    CVNA261002C00070000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.14
    CVNA261002C00070000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.14
  open option positions: 20
    DKNG261002C00021000 qty=4 mkt=$272.00
    DKNG261002C00021500 qty=22 mkt=$1,034.00
    DKNG261002C00022000 qty=4 mkt=$116.00
    DKNG261002C00022500 qty=2 mkt=$32.00
    DKNG261009C00022500 qty=2 mkt=$80.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-28T09:53:41.889632-04:00 ===

[Run context]
Paper auth OK — equity $996013.03, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-28 09:53:45,151 INFO   EXIT [b345|lab0345_s359_w1_0928_1005_r2|S359] take_profit (+80.6%) SELL 1 MSFT260928C00510000 @<= 1.07
  EXIT [b86|lab0086_s210_w4_1120_1135_r1|S210] stop_loss (-91.1%) SELL failed SPY260928C00775000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=3 upgraded=0 already=14 failed=2 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
Found 464 signal(s); top: ['S401:PLTR', 'S359:PLTR', 'S361:PLTR', 'S362:PLTR', 'S363:PLTR', 'S364:PLTR', 'S365:PLTR', 'S366:PLTR']
Paper lab: $996013 broker equity -> 1164 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260928T135659Z

- UTC timestamp: `20260928T135659Z`
- GitHub run: [#11174](https://github.com/28twagg-ops/TradingBot/actions/runs/36432053690)
- Run id: `36432053690`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`145s`
- Full logs: `logs/action_runs/20260928T135659Z_live_bot.log`, `logs/action_runs/20260928T135659Z_live_options.log`, `logs/action_runs/20260928T135659Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1910 | 33.4 | -38.8 | +12.7 | $-9,579 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:57:06.750600-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (3 new)","elapsed_s":132.3,"phases_s":{"reconcile":0.56,"cancel":0.15,"manage":7.71,"protective_stops":2.06,"scan":53.71,"entries":58.82,"reconcile2":0.51},"signals":464,"placed":3,"equity":995996.14,"open_positions":21,"pending_orders":11,"open_lots":81,"submitted_today":28,"filled_today":17,"unattributed_contracts":7,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11174","github_run_id":"36432053690","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1910,"win":33.4,"med":-38.81,"avg":12.65,"pnl":-9579.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:57:00  INFO      Mode: morning_scan
13:57:01  INFO      Morning scan already completed today (2026-09-28T13:48:11.713808Z) — exits-only pass
13:57:01  INFO        Daily log -> logs/daily/2026-09-28.md
13:57:01  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (2 ledger rows)
13:57:02  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:57 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T09:57:03.110003-04:00 share=25% ===
2026-09-28 09:57:03,110 INFO === options_live_micro LIVE 2026-09-28T09:57:03.110003-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 09:57:03,330 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 09:57:03,531 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 09:57:03,665 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (197 earlier lines - see full log file)

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 293 | 21 |
| S164 | 333 | 24 |
| S165 | 1759 | 36 |
| S166 | 139 | 10 |
| S167 | 316 | 23 |
| S168 | 236 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    81 | INFO |
| Total closed lots           |  2542 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1509 med=+12.5% | TAINTED n=1910 med=-38.8% | KEEP-only n=799 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T140404Z

- UTC timestamp: `20260928T140404Z`
- GitHub run: [#11175](https://github.com/28twagg-ops/TradingBot/actions/runs/36432667125)
- Run id: `36432667125`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T140404Z_live_bot.log`, `logs/action_runs/20260928T140404Z_live_options.log`, `logs/action_runs/20260928T140404Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1910 | 33.4 | -38.8 | +12.7 | $-9,579 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:57:06.750600-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (3 new)","elapsed_s":132.3,"phases_s":{"reconcile":0.56,"cancel":0.15,"manage":7.71,"protective_stops":2.06,"scan":53.71,"entries":58.82,"reconcile2":0.51},"signals":464,"placed":3,"equity":995996.14,"open_positions":21,"pending_orders":11,"open_lots":81,"submitted_today":28,"filled_today":17,"unattributed_contracts":7,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11174","github_run_id":"36432053690","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1910,"win":33.4,"med":-38.81,"avg":12.65,"pnl":-9579.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:04:05  INFO      Mode: exits
14:04:06  INFO        Daily log -> logs/daily/2026-09-28.md
14:04:06  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
14:04:06  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:04 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T10:04:06.965057-04:00 share=25% ===
2026-09-28 10:04:06,965 INFO === options_live_micro LIVE 2026-09-28T10:04:06.965057-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 10:04:07,006 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 10:04:07,025 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 10:04:07,038 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=81 paper_keys=yes dry_run=False
  alpaca positions=25
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,427.85
  buying_power=$3,850,475.96 cash=$975,113.25
  open option orders: 20
    MSFT260928C00510000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    LLY261002C01300000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.37
    WFC261002C00083000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.68
    WFC261002C00083000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.68
    PLTR261002C00205000 OrderSide.SELL qty=6 status=OrderStatus.NEW limit=None
  open option positions: 21
    CVNA261002C00070000 qty=8 mkt=$64.00
    DKNG261002C00021000 qty=4 mkt=$332.00
    DKNG261002C00021500 qty=22 mkt=$1,232.00
    DKNG261002C00022000 qty=4 mkt=$136.00
    DKNG261002C00022500 qty=2 mkt=$34.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-28T10:04:09.694612-04:00 ===

[Run context]
Paper auth OK — equity $996415.73, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b86|lab0086_s210_w4_1120_1135_r1|S210] stop_loss (-91.1%) SELL failed SPY260928C00775000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-28 10:04:14,428 INFO   EXIT [b277|lab0277_s350_w1_0928_1005_r2|S350] take_profit (+143.5%) SELL 1 MSFT260928C00510000 @<= 1.45
Protective stops: placed=1 upgraded=0 already=18 failed=1 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
Found 464 signal(s); top: ['S401:PLTR', 'S359:PLTR', 'S361:PLTR', 'S362:PLTR', 'S363:PLTR', 'S364:PLTR', 'S365:PLTR', 'S366:PLTR']
Paper lab: $996416 broker equity -> 1164 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260928T140729Z

- UTC timestamp: `20260928T140729Z`
- GitHub run: [#11176](https://github.com/28twagg-ops/TradingBot/actions/runs/36433288356)
- Run id: `36433288356`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T140729Z_live_bot.log`, `logs/action_runs/20260928T140729Z_live_options.log`, `logs/action_runs/20260928T140729Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1910 | 33.4 | -38.8 | +12.7 | $-9,579 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:57:06.750600-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (3 new)","elapsed_s":132.3,"phases_s":{"reconcile":0.56,"cancel":0.15,"manage":7.71,"protective_stops":2.06,"scan":53.71,"entries":58.82,"reconcile2":0.51},"signals":464,"placed":3,"equity":995996.14,"open_positions":21,"pending_orders":11,"open_lots":81,"submitted_today":28,"filled_today":17,"unattributed_contracts":7,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11174","github_run_id":"36432053690","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1910,"win":33.4,"med":-38.81,"avg":12.65,"pnl":-9579.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:07:31  INFO      Mode: exits
14:07:31  INFO        Daily log -> logs/daily/2026-09-28.md
14:07:31  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
14:07:32  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:07 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T10:07:32.948969-04:00 share=25% ===
2026-09-28 10:07:32,949 INFO === options_live_micro LIVE 2026-09-28T10:07:32.948969-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 10:07:33,415 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 10:07:33,609 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 10:07:33,687 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=81 paper_keys=yes dry_run=False
  alpaca positions=25
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,543.65
  buying_power=$3,851,562.88 cash=$975,258.23
  open option orders: 20
    CVNA261002C00070000 OrderSide.SELL qty=8 status=OrderStatus.NEW limit=None
    LLY261002C01300000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.37
    WFC261002C00083000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.68
    WFC261002C00083000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.68
    PLTR261002C00205000 OrderSide.SELL qty=6 status=OrderStatus.NEW limit=None
  open option positions: 21
    CVNA261002C00070000 qty=8 mkt=$64.00
    DKNG261002C00021000 qty=4 mkt=$344.00
    DKNG261002C00021500 qty=22 mkt=$1,276.00
    DKNG261002C00022000 qty=4 mkt=$144.00
    DKNG261002C00022500 qty=2 mkt=$48.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-28T10:07:36.762786-04:00 ===

[Run context]
Paper auth OK — equity $996543.90, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b86|lab0086_s210_w4_1120_1135_r1|S210] stop_loss (-92.9%) SELL failed SPY260928C00775000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-28 10:07:42,812 INFO   EXIT [b276|lab0276_s350_w1_0928_1005_r1|S350] take_profit (+67.7%) SELL 1 MSFT260928C00510000 @<= 1.01
Protective stops: placed=0 upgraded=0 already=18 failed=2 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
Found 464 signal(s); top: ['S401:PLTR', 'S359:PLTR', 'S361:PLTR', 'S362:PLTR', 'S363:PLTR', 'S364:PLTR', 'S365:PLTR', 'S366:PLTR']
Paper lab: $996544 broker equity -> 1164 bucket(s) ($500 virtual each, unlimited paper)
  [b236 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b237 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b364 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b365 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b378 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b379 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b392 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b393 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b900 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b901 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b914 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b915 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b392 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b393 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b900 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"9bd36d3d-8427-42a7-81c0-b4570d22b72a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b901 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"9bd36d3d-8427-42a7-81c0-b4570d22b72a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b914 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"2fa42a0b-385b-4145-8d38-8c1c9c1692e5","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b915 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"2fa42a0b-385b-4145-8d38-8c1c9c1692e5","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
```

---

## Run 20260928T141217Z

- UTC timestamp: `20260928T141217Z`
- GitHub run: [#11177](https://github.com/28twagg-ops/TradingBot/actions/runs/36433921045)
- Run id: `36433921045`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T141217Z_live_bot.log`, `logs/action_runs/20260928T141217Z_live_options.log`, `logs/action_runs/20260928T141217Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1910 | 33.4 | -38.8 | +12.7 | $-9,579 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:57:06.750600-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (3 new)","elapsed_s":132.3,"phases_s":{"reconcile":0.56,"cancel":0.15,"manage":7.71,"protective_stops":2.06,"scan":53.71,"entries":58.82,"reconcile2":0.51},"signals":464,"placed":3,"equity":995996.14,"open_positions":21,"pending_orders":11,"open_lots":81,"submitted_today":28,"filled_today":17,"unattributed_contracts":7,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11174","github_run_id":"36432053690","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1910,"win":33.4,"med":-38.81,"avg":12.65,"pnl":-9579.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:12:18  INFO      Mode: exits
14:12:18  INFO        Daily log -> logs/daily/2026-09-28.md
14:12:18  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
14:12:19  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:12 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T10:12:19.897908-04:00 share=25% ===
2026-09-28 10:12:19,897 INFO === options_live_micro LIVE 2026-09-28T10:12:19.897908-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 10:12:20,023 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 10:12:20,120 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 10:12:20,184 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=89 paper_keys=yes dry_run=False
  alpaca positions=25
  FLAG b277|S350|d9481e7f missing from Alpaca
  FLAG b276|S350|9629162a missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,963.85
  buying_power=$3,851,950.08 cash=$975,296.15
  open option orders: 20
    CVNA261002C00068000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.27
    CVNA261002C00068000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.27
    CVNA261002C00068000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.27
    CVNA261002C00068000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.27
    CVNA261002C00068000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.27
  open option positions: 21
    CVNA261002C00070000 qty=8 mkt=$88.00
    DKNG261002C00021000 qty=4 mkt=$352.00
    DKNG261002C00021500 qty=22 mkt=$1,298.00
    DKNG261002C00022000 qty=4 mkt=$168.00
    DKNG261002C00022500 qty=2 mkt=$52.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-28T10:12:23.123552-04:00 ===

[Run context]
Paper auth OK — equity $996981.65, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b86|lab0086_s210_w4_1120_1135_r1|S210] stop_loss (-92.9%) SELL failed SPY260928C00775000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=1 upgraded=0 already=18 failed=1 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
Found 464 signal(s); top: ['S401:PLTR', 'S359:PLTR', 'S361:PLTR', 'S362:PLTR', 'S363:PLTR', 'S364:PLTR', 'S365:PLTR', 'S366:PLTR']
Paper lab: $996982 broker equity -> 1164 bucket(s) ($500 virtual each, unlimited paper)
  [b364 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b365 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b378 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b379 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b392 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b393 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b914 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b915 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b364 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b365 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b378 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b379 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b392 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b393 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b914 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b915 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b282 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"72862e86-8f2a-4a8a-a78e-bd02af64adc1","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b283 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"72862e86-8f2a-4a8a-a78e-bd02af64adc1","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b794 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"72862e86-8f2a-4a8a-a78e-bd02af64adc1","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b795 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"72862e86-8f2a-4a8a-a78e-bd02af64adc1","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
```

---

## Run 20260928T141705Z

- UTC timestamp: `20260928T141705Z`
- GitHub run: [#11178](https://github.com/28twagg-ops/TradingBot/actions/runs/36434550685)
- Run id: `36434550685`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`217s`
- Full logs: `logs/action_runs/20260928T141705Z_live_bot.log`, `logs/action_runs/20260928T141705Z_live_options.log`, `logs/action_runs/20260928T141705Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1912 | 33.5 | -38.6 | +12.7 | $-9,478 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T10:17:10.345686-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (23 new)","elapsed_s":204.4,"phases_s":{"reconcile":0.85,"cancel":0.03,"manage":5.66,"protective_stops":0.35,"scan":53.7,"entries":129.8,"reconcile2":3.98},"signals":464,"placed":23,"equity":996603.15,"open_positions":27,"pending_orders":14,"open_lots":121,"submitted_today":59,"filled_today":59,"unattributed_contracts":0,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11178","github_run_id":"36434550685","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1912,"win":33.47,"med":-38.59,"avg":12.73,"pnl":-9478.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:17:06  INFO      Mode: exits
14:17:06  INFO        Daily log -> logs/daily/2026-09-28.md
14:17:06  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
14:17:06  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:17 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T10:17:07.611344-04:00 share=25% ===
2026-09-28 10:17:07,611 INFO === options_live_micro LIVE 2026-09-28T10:17:07.611344-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 10:17:07,655 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 10:17:07,675 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 10:17:07,688 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (217 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 335 | 24 |
| S165 | 1761 | 36 |
| S166 | 139 | 10 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-28 |    2 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2544 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1509 med=+12.5% | TAINTED n=1912 med=-38.6% | KEEP-only n=799 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T142221Z

- UTC timestamp: `20260928T142221Z`
- GitHub run: [#11179](https://github.com/28twagg-ops/TradingBot/actions/runs/36435179709)
- Run id: `36435179709`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`178s`
- Full logs: `logs/action_runs/20260928T142221Z_live_bot.log`, `logs/action_runs/20260928T142221Z_live_options.log`, `logs/action_runs/20260928T142221Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1911 | 33.4 | -38.8 | +12.7 | $-9,564 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T10:22:26.093716-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":165.3,"phases_s":{"reconcile":1.65,"cancel":0.03,"manage":6.58,"protective_stops":0.33,"scan":53.75,"entries":92.79,"reconcile2":0.17},"signals":464,"placed":0,"equity":996846.69,"open_positions":27,"pending_orders":5,"open_lots":121,"submitted_today":44,"filled_today":59,"unattributed_contracts":0,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11179","github_run_id":"36435179709","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1911,"win":33.44,"med":-38.81,"avg":12.66,"pnl":-9564.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:22:21  INFO      Mode: exits
14:22:22  INFO        Daily log -> logs/daily/2026-09-28.md
14:22:22  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
14:22:22  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:22 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T10:22:23.033405-04:00 share=25% ===
2026-09-28 10:22:23,033 INFO === options_live_micro LIVE 2026-09-28T10:22:23.033405-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 10:22:23,368 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 10:22:23,389 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 10:22:23,403 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (198 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 335 | 24 |
| S165 | 1761 | 36 |
| S166 | 139 | 10 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-28 |    2 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2543 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1509 med=+12.5% | TAINTED n=1911 med=-38.8% | KEEP-only n=799 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T142700Z

- UTC timestamp: `20260928T142700Z`
- GitHub run: [#11180](https://github.com/28twagg-ops/TradingBot/actions/runs/36435795608)
- Run id: `36435795608`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`106s`
- Full logs: `logs/action_runs/20260928T142700Z_live_bot.log`, `logs/action_runs/20260928T142700Z_live_options.log`, `logs/action_runs/20260928T142700Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1912 | 33.5 | -38.6 | +12.7 | $-9,478 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T10:27:05.213834-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (4 new)","elapsed_s":97.6,"phases_s":{"reconcile":0.48,"cancel":0.09,"manage":7.36,"protective_stops":1.1,"scan":24.05,"entries":53.61,"reconcile2":3.26},"signals":464,"placed":4,"equity":996717.69,"open_positions":27,"pending_orders":18,"open_lots":121,"submitted_today":63,"filled_today":59,"unattributed_contracts":0,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11180","github_run_id":"36435795608","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1912,"win":33.47,"med":-38.59,"avg":12.73,"pnl":-9478.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:27:00  INFO      Mode: exits
14:27:01  INFO        Daily log -> logs/daily/2026-09-28.md
14:27:01  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
14:27:01  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:27 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T10:27:02.468072-04:00 share=25% ===
2026-09-28 10:27:02,468 INFO === options_live_micro LIVE 2026-09-28T10:27:02.468072-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 10:27:02,626 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 10:27:02,750 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 10:27:02,831 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (203 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 335 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-28 |    2 |    2 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2544 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1509 med=+12.5% | TAINTED n=1912 med=-38.6% | KEEP-only n=799 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T143119Z

- UTC timestamp: `20260928T143119Z`
- GitHub run: [#11181](https://github.com/28twagg-ops/TradingBot/actions/runs/36436436530)
- Run id: `36436436530`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`134s`
- Full logs: `logs/action_runs/20260928T143119Z_live_bot.log`, `logs/action_runs/20260928T143119Z_live_options.log`, `logs/action_runs/20260928T143119Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1913 | 33.5 | -38.8 | +12.7 | $-9,501 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T10:31:25.249174-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":121.4,"phases_s":{"reconcile":0.34,"cancel":0.03,"manage":9.03,"protective_stops":0.5,"scan":53.07,"entries":45.17,"reconcile2":3.29},"signals":464,"placed":1,"equity":996567.42,"open_positions":29,"pending_orders":14,"open_lots":122,"submitted_today":64,"filled_today":66,"unattributed_contracts":0,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11181","github_run_id":"36436436530","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1913,"win":33.46,"med":-38.81,"avg":12.7,"pnl":-9501.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:31:20  INFO      Mode: exits
14:31:20  INFO        Daily log -> logs/daily/2026-09-28.md
14:31:20  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
14:31:21  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T10:31:21.961494-04:00 share=25% ===
2026-09-28 10:31:21,961 INFO === options_live_micro LIVE 2026-09-28T10:31:21.961494-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 10:31:22,230 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 10:31:22,250 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 10:31:22,265 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (210 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 335 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-28 |    2 |    2 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |   122 | INFO |
| Total closed lots           |  2545 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1509 med=+12.5% | TAINTED n=1913 med=-38.8% | KEEP-only n=799 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T143625Z

- UTC timestamp: `20260928T143625Z`
- GitHub run: [#11182](https://github.com/28twagg-ops/TradingBot/actions/runs/36437069144)
- Run id: `36437069144`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`113s`
- Full logs: `logs/action_runs/20260928T143625Z_live_bot.log`, `logs/action_runs/20260928T143625Z_live_options.log`, `logs/action_runs/20260928T143625Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1913 | 33.5 | -38.8 | +12.7 | $-9,501 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T10:36:31.325463-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":101.9,"phases_s":{"reconcile":0.28,"cancel":0.09,"manage":8.98,"protective_stops":1.37,"scan":36.82,"entries":42.89,"reconcile2":0.36},"signals":464,"placed":0,"equity":996348.37,"open_positions":29,"pending_orders":14,"open_lots":122,"submitted_today":64,"filled_today":66,"unattributed_contracts":0,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11182","github_run_id":"36437069144","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1913,"win":33.46,"med":-38.81,"avg":12.7,"pnl":-9501.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:36:26  INFO      Mode: exits
14:36:27  INFO        Daily log -> logs/daily/2026-09-28.md
14:36:27  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
14:36:27  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T10:36:28.462334-04:00 share=25% ===
2026-09-28 10:36:28,462 INFO === options_live_micro LIVE 2026-09-28T10:36:28.462334-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 10:36:28,641 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 10:36:28,778 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 10:36:28,868 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (203 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 335 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-28 |    2 |    2 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |   122 | INFO |
| Total closed lots           |  2545 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1509 med=+12.5% | TAINTED n=1913 med=-38.8% | KEEP-only n=799 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T144128Z

- UTC timestamp: `20260928T144128Z`
- GitHub run: [#11183](https://github.com/28twagg-ops/TradingBot/actions/runs/36437697537)
- Run id: `36437697537`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`100s`
- Full logs: `logs/action_runs/20260928T144128Z_live_bot.log`, `logs/action_runs/20260928T144128Z_live_options.log`, `logs/action_runs/20260928T144128Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1913 | 33.5 | -38.8 | +12.7 | $-9,501 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T10:41:35.277184-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":92.5,"phases_s":{"reconcile":0.25,"cancel":0.08,"manage":7.48,"protective_stops":1.16,"scan":28.99,"entries":43.47,"reconcile2":0.25},"signals":464,"placed":0,"equity":996267.33,"open_positions":29,"pending_orders":14,"open_lots":122,"submitted_today":64,"filled_today":66,"unattributed_contracts":0,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11183","github_run_id":"36437697537","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1913,"win":33.46,"med":-38.81,"avg":12.7,"pnl":-9501.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:41:30  INFO      Mode: exits
14:41:31  INFO        Daily log -> logs/daily/2026-09-28.md
14:41:31  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
14:41:31  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T10:41:32.445444-04:00 share=25% ===
2026-09-28 10:41:32,445 INFO === options_live_micro LIVE 2026-09-28T10:41:32.445444-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 10:41:32,577 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 10:41:32,695 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 10:41:32,756 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (203 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 335 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-28 |    2 |    2 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |   122 | INFO |
| Total closed lots           |  2545 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1509 med=+12.5% | TAINTED n=1913 med=-38.8% | KEEP-only n=799 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T144627Z

- UTC timestamp: `20260928T144627Z`
- GitHub run: [#11184](https://github.com/28twagg-ops/TradingBot/actions/runs/36438318099)
- Run id: `36438318099`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T144627Z_live_bot.log`, `logs/action_runs/20260928T144627Z_live_options.log`, `logs/action_runs/20260928T144627Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1913 | 33.5 | -38.8 | +12.7 | $-9,501 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T10:41:35.277184-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":92.5,"phases_s":{"reconcile":0.25,"cancel":0.08,"manage":7.48,"protective_stops":1.16,"scan":28.99,"entries":43.47,"reconcile2":0.25},"signals":464,"placed":0,"equity":996267.33,"open_positions":29,"pending_orders":14,"open_lots":122,"submitted_today":64,"filled_today":66,"unattributed_contracts":0,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11183","github_run_id":"36437697537","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1913,"win":33.46,"med":-38.81,"avg":12.7,"pnl":-9501.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:46:28  INFO      Mode: exits
14:46:28  INFO        Daily log -> logs/daily/2026-09-28.md
14:46:28  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
14:46:28  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T10:46:29.399688-04:00 share=25% ===
2026-09-28 10:46:29,399 INFO === options_live_micro LIVE 2026-09-28T10:46:29.399688-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 10:46:29,600 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 10:46:29,623 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 10:46:29,638 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (4 earlier lines - see full log file)
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,265.33
  buying_power=$3,845,821.36 cash=$973,451.83
  open option orders: 20
    DKNG261016C00023000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    WFC261002C00083000 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
    DKNG261016C00023500 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    RBLX261002C00047500 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.17
    RBLX261002C00047500 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.17
  open option positions: 29
    BAC261002C00057000 qty=2 mkt=$56.00
    CVNA261002C00067000 qty=12 mkt=$444.00
    CVNA261002C00070000 qty=8 mkt=$88.00
    DKNG261002C00021000 qty=4 mkt=$284.00
    DKNG261002C00021500 qty=22 mkt=$1,078.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-28T10:46:32.662618-04:00 ===

[Run context]
Paper auth OK — equity $996266.33, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b86|lab0086_s210_w4_1120_1135_r1|S210] stop_loss (-96.4%) SELL failed SPY260928C00775000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 upgraded=0 already=27 failed=1 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
Found 464 signal(s); top: ['S401:PLTR', 'S359:PLTR', 'S361:PLTR', 'S362:PLTR', 'S363:PLTR', 'S364:PLTR', 'S365:PLTR', 'S366:PLTR']
Paper lab: $996266 broker equity -> 1164 bucket(s) ($500 virtual each, unlimited paper)
  [b238 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b239 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b366 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b367 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b380 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b381 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b394 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b395 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b832 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b833 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b902 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"524978e6-2a42-40da-9be5-49d1d4e2e82a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b903 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"524978e6-2a42-40da-9be5-49d1d4e2e82a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b916 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b917 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b238 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"af95b899-99fc-4d54-acd0-16c48d46385b","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b239 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"af95b899-99fc-4d54-acd0-16c48d46385b","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b394 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b395 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b422 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"7e1330ff-e514-41ff-88ca-1df704d0bbdc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b423 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"7e1330ff-e514-41ff-88ca-1df704d0bbdc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b902 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"9bd36d3d-8427-42a7-81c0-b4570d22b72a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b903 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"9bd36d3d-8427-42a7-81c0-b4570d22b72a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b916 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b917 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b1056 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"325cb8d8-4735-44a2-b2e4-01c094854964","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b1057 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"325cb8d8-4735-44a2-b2e4-01c094854964","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b1154 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"72862e86-8f2a-4a8a-a78e-bd02af64adc1","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b1155 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"72862e86-8f2a-4a8a-a78e-bd02af64adc1","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b1126 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"72862e86-8f2a-4a8a-a78e-bd02af64adc1","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b1127 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"72862e86-8f2a-4a8a-a78e-bd02af64adc1","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b1098 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"325cb8d8-4735-44a2-b2e4-01c094854964","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b1099 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"325cb8d8-4735-44a2-b2e4-01c094854964","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b1140 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"72862e86-8f2a-4a8a-a78e-bd02af64adc1","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b1141 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"72862e86-8f2a-4a8a-a78e-bd02af64adc1","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b284 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"325cb8d8-4735-44a2-b2e4-01c094854964","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b285 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"325cb8d8-4735-44a2-b2e4-01c094854964","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b292 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"325cb8d8-4735-44a2-b2e4-01c094854964","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b293 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"325cb8d8-4735-44a2-b2e4-01c094854964","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b300 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"72862e86-8f2a-4a8a-a78e-bd02af64adc1","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b301 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"72862e86-8f2a-4a8a-a78e-bd02af64adc1","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b308 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"72862e86-8f2a-4a8a-a78e-bd02af64adc1","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b309 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"72862e86-8f2a-4a8a-a78e-bd02af64adc1","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b788 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"325cb8d8-4735-44a2-b2e4-01c094854964","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b789 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"325cb8d8-4735-44a2-b2e4-01c094854964","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
```

---

## Run 20260928T145159Z

- UTC timestamp: `20260928T145159Z`
- GitHub run: [#11185](https://github.com/28twagg-ops/TradingBot/actions/runs/36438950162)
- Run id: `36438950162`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T145159Z_live_bot.log`, `logs/action_runs/20260928T145159Z_live_options.log`, `logs/action_runs/20260928T145159Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1913 | 33.5 | -38.8 | +12.7 | $-9,501 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T10:41:35.277184-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":92.5,"phases_s":{"reconcile":0.25,"cancel":0.08,"manage":7.48,"protective_stops":1.16,"scan":28.99,"entries":43.47,"reconcile2":0.25},"signals":464,"placed":0,"equity":996267.33,"open_positions":29,"pending_orders":14,"open_lots":122,"submitted_today":64,"filled_today":66,"unattributed_contracts":0,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11183","github_run_id":"36437697537","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1913,"win":33.46,"med":-38.81,"avg":12.7,"pnl":-9501.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:52:00  INFO      Mode: exits
14:52:01  INFO        Daily log -> logs/daily/2026-09-28.md
14:52:01  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
14:52:01  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:52 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T10:52:02.858651-04:00 share=25% ===
2026-09-28 10:52:02,858 INFO === options_live_micro LIVE 2026-09-28T10:52:02.858651-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 10:52:02,958 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 10:52:03,061 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 10:52:03,103 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=122 paper_keys=yes dry_run=False
  alpaca positions=37
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$995,903.95
  buying_power=$3,843,181.36 cash=$973,031.38
  open option orders: 20
    RBLX261002C00046000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.35
    RBLX261002C00046000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.35
    RBLX261002C00046000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.35
    RBLX261002C00046000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.35
    RBLX261002C00046000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.35
  open option positions: 33
    BAC261002C00057000 qty=2 mkt=$52.00
    CVNA261002C00067000 qty=12 mkt=$372.00
    CVNA261002C00068000 qty=8 mkt=$160.00
    CVNA261002C00070000 qty=8 mkt=$88.00
    DKNG261002C00021000 qty=4 mkt=$284.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-28T10:52:06.133575-04:00 ===

[Run context]
Paper auth OK — equity $995899.88, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b86|lab0086_s210_w4_1120_1135_r1|S210] stop_loss (-96.4%) SELL failed SPY260928C00775000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=3 upgraded=0 already=27 failed=2 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
Found 464 signal(s); top: ['S401:PLTR', 'S359:PLTR', 'S361:PLTR', 'S362:PLTR', 'S363:PLTR', 'S364:PLTR', 'S365:PLTR', 'S366:PLTR']
Paper lab: $995900 broker equity -> 1164 bucket(s) ($500 virtual each, unlimited paper)
  [b394 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b395 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b902 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"524978e6-2a42-40da-9be5-49d1d4e2e82a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b903 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"524978e6-2a42-40da-9be5-49d1d4e2e82a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b916 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b917 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b394 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b395 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b422 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"7e1330ff-e514-41ff-88ca-1df704d0bbdc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b423 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"7e1330ff-e514-41ff-88ca-1df704d0bbdc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b902 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"9bd36d3d-8427-42a7-81c0-b4570d22b72a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b903 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"9bd36d3d-8427-42a7-81c0-b4570d22b72a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b1140 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"325cb8d8-4735-44a2-b2e4-01c094854964","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b1141 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"325cb8d8-4735-44a2-b2e4-01c094854964","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b284 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"325cb8d8-4735-44a2-b2e4-01c094854964","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b285 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"325cb8d8-4735-44a2-b2e4-01c094854964","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b84 MSFT] ENTRY failed: {"code":40310000,"existing_order_id":"f4b6dee4-c749-448a-ac95-a58513a6ca51","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b85 MSFT] ENTRY failed: {"code":40310000,"existing_order_id":"f4b6dee4-c749-448a-ac95-a58513a6ca51","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
```

---

## Run 20260928T145855Z

- UTC timestamp: `20260928T145855Z`
- GitHub run: [#11186](https://github.com/28twagg-ops/TradingBot/actions/runs/36439579165)
- Run id: `36439579165`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T145855Z_live_bot.log`, `logs/action_runs/20260928T145855Z_live_options.log`, `logs/action_runs/20260928T145855Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1913 | 33.5 | -38.8 | +12.7 | $-9,501 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T10:41:35.277184-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":92.5,"phases_s":{"reconcile":0.25,"cancel":0.08,"manage":7.48,"protective_stops":1.16,"scan":28.99,"entries":43.47,"reconcile2":0.25},"signals":464,"placed":0,"equity":996267.33,"open_positions":29,"pending_orders":14,"open_lots":122,"submitted_today":64,"filled_today":66,"unattributed_contracts":0,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11183","github_run_id":"36437697537","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1913,"win":33.46,"med":-38.81,"avg":12.7,"pnl":-9501.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:58:56  INFO      Mode: exits
14:58:57  INFO        Daily log -> logs/daily/2026-09-28.md
14:58:57  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
14:58:57  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:58 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T10:58:58.178086-04:00 share=25% ===
2026-09-28 10:58:58,178 INFO === options_live_micro LIVE 2026-09-28T10:58:58.178086-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 10:58:58,263 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 10:58:58,327 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 10:58:58,367 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=122 paper_keys=yes dry_run=False
  alpaca positions=41
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$995,823.65
  buying_power=$3,839,919.82 cash=$972,405.02
  open option orders: 20
    CVNA261002C00066000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.5
    CVNA261002C00066000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.5
    CVNA261002C00068000 OrderSide.SELL qty=8 status=OrderStatus.NEW limit=None
    RBLX261002C00047500 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
    HOOD261002C00129000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
  open option positions: 37
    BAC261002C00057000 qty=2 mkt=$54.00
    CVNA261002C00066000 qty=4 mkt=$196.00
    CVNA261002C00067000 qty=12 mkt=$384.00
    CVNA261002C00068000 qty=8 mkt=$168.00
    CVNA261002C00070000 qty=8 mkt=$64.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-28T10:59:01.148332-04:00 ===

[Run context]
Paper auth OK — equity $995821.14, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b86|lab0086_s210_w4_1120_1135_r1|S210] stop_loss (-94.6%) SELL failed SPY260928C00775000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=3 upgraded=0 already=30 failed=3 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
Found 464 signal(s); top: ['S401:PLTR', 'S359:PLTR', 'S361:PLTR', 'S362:PLTR', 'S363:PLTR', 'S364:PLTR', 'S365:PLTR', 'S366:PLTR']
Paper lab: $995821 broker equity -> 1164 bucket(s) ($500 virtual each, unlimited paper)
  [b394 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b902 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"524978e6-2a42-40da-9be5-49d1d4e2e82a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b903 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"524978e6-2a42-40da-9be5-49d1d4e2e82a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b916 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b917 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b422 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"7e1330ff-e514-41ff-88ca-1df704d0bbdc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b423 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"7e1330ff-e514-41ff-88ca-1df704d0bbdc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
```

---

## Run 20260928T150740Z

- UTC timestamp: `20260928T150740Z`
- GitHub run: [#11188](https://github.com/28twagg-ops/TradingBot/actions/runs/36440868363)
- Run id: `36440868363`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T150740Z_live_bot.log`, `logs/action_runs/20260928T150740Z_live_options.log`, `logs/action_runs/20260928T150740Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1913 | 33.5 | -38.8 | +12.7 | $-9,501 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T10:41:35.277184-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":92.5,"phases_s":{"reconcile":0.25,"cancel":0.08,"manage":7.48,"protective_stops":1.16,"scan":28.99,"entries":43.47,"reconcile2":0.25},"signals":464,"placed":0,"equity":996267.33,"open_positions":29,"pending_orders":14,"open_lots":122,"submitted_today":64,"filled_today":66,"unattributed_contracts":0,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11183","github_run_id":"36437697537","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1913,"win":33.46,"med":-38.81,"avg":12.7,"pnl":-9501.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:07:42  INFO      Mode: exits
15:07:42  INFO        Daily log -> logs/daily/2026-09-28.md
15:07:42  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
15:07:43  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:07 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T11:07:44.355897-04:00 share=25% ===
2026-09-28 11:07:44,355 INFO === options_live_micro LIVE 2026-09-28T11:07:44.355897-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 11:07:44,580 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 11:07:44,791 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 11:07:44,926 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=149 paper_keys=yes dry_run=False
  alpaca positions=42
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,101.46
  buying_power=$3,838,636.32 cash=$972,300.96
  open option orders: 20
    MSFT260930C00525000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    RBLX261002C00047000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.22
    RBLX261002C00047000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.22
    RBLX261002C00047000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.22
    RBLX261002C00047000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.22
  open option positions: 38
    BAC261002C00057000 qty=2 mkt=$54.00
    CVNA261002C00066000 qty=4 mkt=$188.00
    CVNA261002C00067000 qty=12 mkt=$384.00
    CVNA261002C00068000 qty=8 mkt=$184.00
    CVNA261002C00070000 qty=8 mkt=$72.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-28T11:07:48.205186-04:00 ===

[Run context]
Paper auth OK — equity $996101.46, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-28 11:07:51,292 INFO   EXIT [b285|lab0285_s351_w3_1045_1120_r2|S351] take_profit (+127.5%) SELL 1 MSFT260928C00510000 @<= 0.88
  EXIT [b86|lab0086_s210_w4_1120_1135_r1|S210] stop_loss (-94.6%) SELL failed SPY260928C00775000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 upgraded=0 already=33 failed=4 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
Found 464 signal(s); top: ['S401:PLTR', 'S359:PLTR', 'S361:PLTR', 'S362:PLTR', 'S363:PLTR', 'S364:PLTR', 'S365:PLTR', 'S366:PLTR']
Paper lab: $996101 broker equity -> 1164 bucket(s) ($500 virtual each, unlimited paper)
  [b902 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"524978e6-2a42-40da-9be5-49d1d4e2e82a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b903 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"524978e6-2a42-40da-9be5-49d1d4e2e82a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b422 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"7e1330ff-e514-41ff-88ca-1df704d0bbdc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b423 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"7e1330ff-e514-41ff-88ca-1df704d0bbdc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b902 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"9bd36d3d-8427-42a7-81c0-b4570d22b72a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b903 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"9bd36d3d-8427-42a7-81c0-b4570d22b72a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b182 MCD] ENTRY failed: {"code":40310000,"existing_order_id":"5c028247-6517-4973-9ec6-5ae42f7628f8","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b168 WFC] ENTRY failed: {"code":40310000,"existing_order_id":"61c76d6b-0ce1-4064-9f47-522b657859ec","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b169 WFC] ENTRY failed: {"code":40310000,"existing_order_id":"61c76d6b-0ce1-4064-9f47-522b657859ec","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
```

---

## Run 20260928T151207Z

- UTC timestamp: `20260928T151207Z`
- GitHub run: [#11189](https://github.com/28twagg-ops/TradingBot/actions/runs/36441511470)
- Run id: `36441511470`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`187s`
- Full logs: `logs/action_runs/20260928T151207Z_live_bot.log`, `logs/action_runs/20260928T151207Z_live_options.log`, `logs/action_runs/20260928T151207Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1510 | 50.3 | +12.8 | +43.7 | $+19,811 |
| TAINTED | 1917 | 33.5 | -38.8 | +12.7 | $-9,454 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T11:12:13.320520-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (3 new)","elapsed_s":175.2,"phases_s":{"reconcile":0.44,"cancel":0.07,"manage":10.65,"protective_stops":1.65,"scan":53.38,"entries":91.02,"reconcile2":0.54},"signals":464,"placed":3,"equity":996116.94,"open_positions":37,"pending_orders":21,"open_lots":154,"submitted_today":89,"filled_today":101,"unattributed_contracts":0,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11189","github_run_id":"36441511470","status":"ok","data_quality":{"clean":{"n":1510,"win":50.26,"med":12.8,"avg":43.7,"pnl":19811.16},"tainted":{"n":1917,"win":33.49,"med":-38.81,"avg":12.67,"pnl":-9454.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:12:08  INFO      Mode: exits
15:12:09  INFO        Daily log -> logs/daily/2026-09-28.md
15:12:09  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
15:12:09  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:12 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T11:12:10.205016-04:00 share=25% ===
2026-09-28 11:12:10,205 INFO === options_live_micro LIVE 2026-09-28T11:12:10.205016-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 11:12:10,303 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 11:12:10,380 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 11:12:10,430 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (209 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 335 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-28 |    2 |    2 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   154 | INFO |
| Total closed lots           |  2550 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1510 med=+12.8% | TAINTED n=1917 med=-38.8% | KEEP-only n=799 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T151654Z

- UTC timestamp: `20260928T151654Z`
- GitHub run: [#11190](https://github.com/28twagg-ops/TradingBot/actions/runs/36442130515)
- Run id: `36442130515`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`195s`
- Full logs: `logs/action_runs/20260928T151654Z_live_bot.log`, `logs/action_runs/20260928T151654Z_live_options.log`, `logs/action_runs/20260928T151654Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1510 | 50.3 | +12.8 | +43.7 | $+19,793 |
| TAINTED | 1917 | 33.5 | -38.8 | +12.6 | $-9,460 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T11:17:00.041202-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":183.2,"phases_s":{"reconcile":0.6,"cancel":0.06,"manage":12.71,"protective_stops":1.07,"scan":53.68,"entries":97.5,"reconcile2":3.36},"signals":464,"placed":2,"equity":996330.22,"open_positions":38,"pending_orders":21,"open_lots":156,"submitted_today":89,"filled_today":103,"unattributed_contracts":0,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11190","github_run_id":"36442130515","status":"ok","data_quality":{"clean":{"n":1510,"win":50.26,"med":12.8,"avg":43.65,"pnl":19793.16},"tainted":{"n":1917,"win":33.49,"med":-38.81,"avg":12.65,"pnl":-9460.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:16:55  INFO      Mode: exits
15:16:55  INFO        Daily log -> logs/daily/2026-09-28.md
15:16:55  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
15:16:56  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T11:16:56.966798-04:00 share=25% ===
2026-09-28 11:16:56,966 INFO === options_live_micro LIVE 2026-09-28T11:16:56.966798-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 11:16:57,061 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 11:16:57,134 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 11:16:57,181 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (212 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 335 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-28 |    2 |    2 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  2550 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1510 med=+12.8% | TAINTED n=1917 med=-38.8% | KEEP-only n=799 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T152853Z

- UTC timestamp: `20260928T152853Z`
- GitHub run: [#11192](https://github.com/28twagg-ops/TradingBot/actions/runs/36443409259)
- Run id: `36443409259`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T152853Z_live_bot.log`, `logs/action_runs/20260928T152853Z_live_options.log`, `logs/action_runs/20260928T152853Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1510 | 50.3 | +12.8 | +43.7 | $+19,793 |
| TAINTED | 1917 | 33.5 | -38.8 | +12.6 | $-9,460 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T11:17:00.041202-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":183.2,"phases_s":{"reconcile":0.6,"cancel":0.06,"manage":12.71,"protective_stops":1.07,"scan":53.68,"entries":97.5,"reconcile2":3.36},"signals":464,"placed":2,"equity":996330.22,"open_positions":38,"pending_orders":21,"open_lots":156,"submitted_today":89,"filled_today":103,"unattributed_contracts":0,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11190","github_run_id":"36442130515","status":"ok","data_quality":{"clean":{"n":1510,"win":50.26,"med":12.8,"avg":43.65,"pnl":19793.16},"tainted":{"n":1917,"win":33.49,"med":-38.81,"avg":12.65,"pnl":-9460.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:28:54  INFO      Mode: exits
15:28:55  INFO        Daily log -> logs/daily/2026-09-28.md
15:28:55  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
15:28:56  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:28 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T11:28:57.201812-04:00 share=25% ===
2026-09-28 11:28:57,201 INFO === options_live_micro LIVE 2026-09-28T11:28:57.201812-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 11:28:57,459 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 11:28:57,694 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 11:28:57,851 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=156 paper_keys=yes dry_run=False
  alpaca positions=43
  FLAG b179|S217|ed77e203 missing from Alpaca
  FLAG b178|S217|865ebb51 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$995,859.49
  buying_power=$3,838,360.68 cash=$972,079.49
  open option orders: 20
    MSFT260928C00512500 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    CVNA261002C00066000 OrderSide.SELL qty=9 status=OrderStatus.NEW limit=None
    BAC261002C00056000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    MSFT260930C00525000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    RBLX261002C00047000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.22
  open option positions: 39
    BAC261002C00056000 qty=1 mkt=$63.00
    BAC261002C00057000 qty=2 mkt=$50.00
    CVNA261002C00066000 qty=9 mkt=$306.00
    CVNA261002C00067000 qty=12 mkt=$252.00
    CVNA261002C00068000 qty=8 mkt=$120.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-28T11:29:01.164200-04:00 ===

[Run context]
Paper auth OK — equity $995859.99, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-28 11:29:06,275 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-40.0%) SELL 1 MCD261002C00245000 @<= 0.16
2026-09-28 11:29:08,699 INFO   EXIT [b787|lab0787_s398_w2_1005_1045_r2|S398] stop_loss (-52.8%) SELL 1 CVNA261002C00067000 @<= 0.22
  EXIT [b86|lab0086_s210_w4_1120_1135_r1|S210] stop_loss (-94.6%) SELL failed SPY260928C00775000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-28 11:29:12,413 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-42.3%) SELL 1 CVNA261002C00068000 @<= 0.16
2026-09-28 11:29:16,077 INFO   EXIT [b297|lab0297_s353_w1_0928_1005_r2|S353] stop_loss (-92.9%) SELL 1 CVNA261002C00070000 @<= 0.01
Protective stops: placed=2 upgraded=0 already=33 failed=3 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
Found 464 signal(s); top: ['S401:PLTR', 'S359:PLTR', 'S361:PLTR', 'S362:PLTR', 'S363:PLTR', 'S364:PLTR', 'S365:PLTR', 'S366:PLTR']
Paper lab: $995860 broker equity -> 1164 bucket(s) ($500 virtual each, unlimited paper)
  [b240 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b241 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b368 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b369 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b382 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b383 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b396 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b397 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b904 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b905 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b918 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b919 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b240 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"af95b899-99fc-4d54-acd0-16c48d46385b","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b241 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"af95b899-99fc-4d54-acd0-16c48d46385b","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b368 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b369 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b382 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b383 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b396 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b397 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b424 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"7e1330ff-e514-41ff-88ca-1df704d0bbdc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b425 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"7e1330ff-e514-41ff-88ca-1df704d0bbdc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b904 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"9bd36d3d-8427-42a7-81c0-b4570d22b72a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b905 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"9bd36d3d-8427-42a7-81c0-b4570d22b72a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b918 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b919 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
```

---

## Run 20260928T153253Z

- UTC timestamp: `20260928T153253Z`
- GitHub run: [#11193](https://github.com/28twagg-ops/TradingBot/actions/runs/36444045889)
- Run id: `36444045889`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T153253Z_live_bot.log`, `logs/action_runs/20260928T153253Z_live_options.log`, `logs/action_runs/20260928T153253Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1510 | 50.3 | +12.8 | +43.7 | $+19,811 |
| TAINTED | 1917 | 33.5 | -38.8 | +12.7 | $-9,454 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T11:12:13.320520-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (3 new)","elapsed_s":175.2,"phases_s":{"reconcile":0.44,"cancel":0.07,"manage":10.65,"protective_stops":1.65,"scan":53.38,"entries":91.02,"reconcile2":0.54},"signals":464,"placed":3,"equity":996116.94,"open_positions":37,"pending_orders":21,"open_lots":154,"submitted_today":89,"filled_today":101,"unattributed_contracts":0,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11189","github_run_id":"36441511470","status":"ok","data_quality":{"clean":{"n":1510,"win":50.26,"med":12.8,"avg":43.7,"pnl":19811.16},"tainted":{"n":1917,"win":33.49,"med":-38.81,"avg":12.67,"pnl":-9454.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:32:56  INFO      Mode: exits
15:32:57  INFO        Daily log -> logs/daily/2026-09-28.md
15:32:57  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
15:32:57  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:32 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T11:32:57.937258-04:00 share=25% ===
2026-09-28 11:32:57,937 INFO === options_live_micro LIVE 2026-09-28T11:32:57.937258-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 11:32:58,041 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 11:32:58,119 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 11:32:58,169 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=154 paper_keys=yes dry_run=False
  alpaca positions=45
  FLAG b179|S217|ed77e203 missing from Alpaca
  FLAG b178|S217|865ebb51 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$995,932.08
  buying_power=$3,837,134.56 cash=$971,898.11
  open option orders: 20
    HOOD261002C00128000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.54
    HOOD261002C00128000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.54
    DKNG261002C00023500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    LLY261002C01300000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    CVNA261002C00068000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.16
  open option positions: 41
    BAC261002C00056000 qty=1 mkt=$64.00
    BAC261002C00057000 qty=2 mkt=$54.00
    CVNA261002C00066000 qty=9 mkt=$315.00
    CVNA261002C00067000 qty=12 mkt=$252.00
    CVNA261002C00068000 qty=8 mkt=$120.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-28T11:33:00.869480-04:00 ===

[Run context]
Paper auth OK — equity $995941.51, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-28 11:33:11,143 INFO   EXIT [b296|lab0296_s353_w1_0928_1005_r1|S353] stop_loss (-92.9%) SELL 1 CVNA261002C00070000 @<= 0.02
  EXIT [b86|lab0086_s210_w4_1120_1135_r1|S210] stop_loss (-94.6%) SELL failed SPY260928C00775000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=2 upgraded=0 already=36 failed=2 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
Found 464 signal(s); top: ['S401:PLTR', 'S359:PLTR', 'S361:PLTR', 'S362:PLTR', 'S363:PLTR', 'S364:PLTR', 'S365:PLTR', 'S366:PLTR']
Paper lab: $995942 broker equity -> 1164 bucket(s) ($500 virtual each, unlimited paper)
  [b368 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b369 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b382 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b383 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b396 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b397 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b834 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"c6a45a04-a57e-40d2-a59c-a788ad414cbd","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b904 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b905 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b918 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b919 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b368 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b369 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b382 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b383 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b396 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b397 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b424 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"34118f67-7f1e-4f67-b8cc-72d45513d8ce","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b425 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"34118f67-7f1e-4f67-b8cc-72d45513d8ce","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b904 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"9bd36d3d-8427-42a7-81c0-b4570d22b72a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b905 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"9bd36d3d-8427-42a7-81c0-b4570d22b72a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b798 CVNA] ENTRY failed: {"buy_limit_price":"0.2","code":40310000,"existing_order_id":"bc1c8894-1a38-4c0b-999f-749e12769c4b","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.16"}
  [b799 CVNA] ENTRY failed: {"buy_limit_price":"0.2","code":40310000,"existing_order_id":"bc1c8894-1a38-4c0b-999f-749e12769c4b","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.16"}
```

---

## Run 20260928T153819Z

- UTC timestamp: `20260928T153819Z`
- GitHub run: [#11194](https://github.com/28twagg-ops/TradingBot/actions/runs/36444683377)
- Run id: `36444683377`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`28s`
- Full logs: `logs/action_runs/20260928T153819Z_live_bot.log`, `logs/action_runs/20260928T153819Z_live_options.log`, `logs/action_runs/20260928T153819Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1512 | 50.2 | +8.6 | +43.5 | $+19,772 |
| TAINTED | 1920 | 33.5 | -38.6 | +12.8 | $-9,344 |
| KEEP-only | 800 | 63.2 | +52.8 | +66.5 | $+13,831 |
| KEEP-only recent | 605 | 62.5 | +56.9 | +76.6 | $+9,746 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T11:38:25.676247-04:00","date":"2026-09-28","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":20.2,"phases_s":{"reconcile":0.99,"cancel":1.77,"manage":13.83,"protective_stops":2.8},"signals":0,"placed":0,"equity":996031.97,"open_positions":42,"pending_orders":20,"open_lots":170,"submitted_today":103,"filled_today":121,"unattributed_contracts":0,"top_signals":[],"github_run":"11194","github_run_id":"36444683377","status":"ok","data_quality":{"clean":{"n":1512,"win":50.2,"med":8.63,"avg":43.51,"pnl":19772.16},"tainted":{"n":1920,"win":33.54,"med":-38.59,"avg":12.78,"pnl":-9344.28},"keep_only":{"n":800,"win":63.25,"med":52.75,"avg":66.54,"pnl":13831.45},"keep_only_recent":{"n":605,"win":62.48,"med":56.92,"avg":76.59,"pnl":9746.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:38:21  INFO      Mode: exits
15:38:21  INFO        Daily log -> logs/daily/2026-09-28.md
15:38:21  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
15:38:22  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:38 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T11:38:23.081073-04:00 share=25% ===
2026-09-28 11:38:23,081 INFO === options_live_micro LIVE 2026-09-28T11:38:23.081073-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 11:38:23,281 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: manage/exits only
2026-09-28 11:38:23,451 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-28 11:38:23,507 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (199 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |    10 | WARN | <<<
| Total open lots             |   170 | INFO |
| Total closed lots           |  2554 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1512 med=+8.6% | TAINTED n=1920 med=-38.6% | KEEP-only n=800 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T154129Z

- UTC timestamp: `20260928T154129Z`
- GitHub run: [#11195](https://github.com/28twagg-ops/TradingBot/actions/runs/36445314999)
- Run id: `36445314999`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`33s`
- Full logs: `logs/action_runs/20260928T154129Z_live_bot.log`, `logs/action_runs/20260928T154129Z_live_options.log`, `logs/action_runs/20260928T154129Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1512 | 50.2 | +8.6 | +43.5 | $+19,772 |
| TAINTED | 1920 | 33.5 | -38.6 | +12.8 | $-9,344 |
| KEEP-only | 800 | 63.2 | +52.8 | +66.5 | $+13,831 |
| KEEP-only recent | 605 | 62.5 | +56.9 | +76.6 | $+9,746 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T11:41:37.363137-04:00","date":"2026-09-28","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":20.1,"phases_s":{"reconcile":0.49,"cancel":0.22,"manage":15.17,"protective_stops":3.39},"signals":0,"placed":0,"equity":996072.41,"open_positions":42,"pending_orders":0,"open_lots":170,"submitted_today":103,"filled_today":121,"unattributed_contracts":0,"top_signals":[],"github_run":"11195","github_run_id":"36445314999","status":"ok","data_quality":{"clean":{"n":1512,"win":50.2,"med":8.63,"avg":43.51,"pnl":19772.16},"tainted":{"n":1920,"win":33.54,"med":-38.59,"avg":12.78,"pnl":-9344.28},"keep_only":{"n":800,"win":63.25,"med":52.75,"avg":66.54,"pnl":13831.45},"keep_only_recent":{"n":605,"win":62.48,"med":56.92,"avg":76.59,"pnl":9746.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:41:31  INFO      Mode: exits
15:41:32  INFO        Daily log -> logs/daily/2026-09-28.md
15:41:32  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
15:41:32  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T11:41:33.663288-04:00 share=25% ===
2026-09-28 11:41:33,663 INFO === options_live_micro LIVE 2026-09-28T11:41:33.663288-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 11:41:33,891 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: manage/exits only
2026-09-28 11:41:34,096 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-28 11:41:34,164 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (188 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |    10 | WARN | <<<
| Total open lots             |   170 | INFO |
| Total closed lots           |  2554 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1512 med=+8.6% | TAINTED n=1920 med=-38.6% | KEEP-only n=800 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T154903Z

- UTC timestamp: `20260928T154903Z`
- GitHub run: [#11196](https://github.com/28twagg-ops/TradingBot/actions/runs/36445947215)
- Run id: `36445947215`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260928T154903Z_live_bot.log`, `logs/action_runs/20260928T154903Z_live_options.log`, `logs/action_runs/20260928T154903Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1513 | 50.2 | +4.8 | +43.5 | $+19,751 |
| TAINTED | 1920 | 33.5 | -38.6 | +12.8 | $-9,344 |
| KEEP-only | 800 | 63.2 | +52.8 | +66.5 | $+13,831 |
| KEEP-only recent | 605 | 62.5 | +56.9 | +76.6 | $+9,746 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T11:49:09.255268-04:00","date":"2026-09-28","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":11.4,"phases_s":{"reconcile":0.25,"cancel":0.09,"manage":9.02,"protective_stops":1.39},"signals":0,"placed":0,"equity":995587.51,"open_positions":42,"pending_orders":0,"open_lots":169,"submitted_today":103,"filled_today":121,"unattributed_contracts":0,"top_signals":[],"github_run":"11196","github_run_id":"36445947215","status":"ok","data_quality":{"clean":{"n":1513,"win":50.17,"med":4.76,"avg":43.46,"pnl":19751.16},"tainted":{"n":1920,"win":33.54,"med":-38.59,"avg":12.78,"pnl":-9344.28},"keep_only":{"n":800,"win":63.25,"med":52.75,"avg":66.54,"pnl":13831.45},"keep_only_recent":{"n":605,"win":62.48,"med":56.92,"avg":76.59,"pnl":9746.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:49:04  INFO      Mode: exits
15:49:05  INFO        Daily log -> logs/daily/2026-09-28.md
15:49:05  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
15:49:05  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:49 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T11:49:06.399561-04:00 share=25% ===
2026-09-28 11:49:06,399 INFO === options_live_micro LIVE 2026-09-28T11:49:06.399561-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 11:49:06,486 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: manage/exits only
2026-09-28 11:49:06,550 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-28 11:49:06,571 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (188 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |   169 | INFO |
| Total closed lots           |  2554 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1513 med=+4.8% | TAINTED n=1920 med=-38.6% | KEEP-only n=800 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T155125Z

- UTC timestamp: `20260928T155125Z`
- GitHub run: [#11197](https://github.com/28twagg-ops/TradingBot/actions/runs/36446572444)
- Run id: `36446572444`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`25s`
- Full logs: `logs/action_runs/20260928T155125Z_live_bot.log`, `logs/action_runs/20260928T155125Z_live_options.log`, `logs/action_runs/20260928T155125Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1514 | 50.1 | +4.6 | +43.4 | $+19,730 |
| TAINTED | 1920 | 33.5 | -38.6 | +12.8 | $-9,344 |
| KEEP-only | 800 | 63.2 | +52.8 | +66.5 | $+13,831 |
| KEEP-only recent | 605 | 62.5 | +56.9 | +76.6 | $+9,746 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T11:51:31.139556-04:00","date":"2026-09-28","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":12.5,"phases_s":{"reconcile":0.25,"cancel":0.09,"manage":10.36,"protective_stops":1.15},"signals":0,"placed":0,"equity":995685.41,"open_positions":42,"pending_orders":0,"open_lots":168,"submitted_today":103,"filled_today":121,"unattributed_contracts":0,"top_signals":[],"github_run":"11197","github_run_id":"36446572444","status":"ok","data_quality":{"clean":{"n":1514,"win":50.13,"med":4.62,"avg":43.4,"pnl":19729.83},"tainted":{"n":1920,"win":33.54,"med":-38.59,"avg":12.78,"pnl":-9344.28},"keep_only":{"n":800,"win":63.25,"med":52.75,"avg":66.54,"pnl":13831.45},"keep_only_recent":{"n":605,"win":62.48,"med":56.92,"avg":76.59,"pnl":9746.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:51:26  INFO      Mode: exits
15:51:27  INFO        Daily log -> logs/daily/2026-09-28.md
15:51:27  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
15:51:27  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T11:51:28.090799-04:00 share=25% ===
2026-09-28 11:51:28,090 INFO === options_live_micro LIVE 2026-09-28T11:51:28.090799-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 11:51:28,176 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: manage/exits only
2026-09-28 11:51:28,240 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-28 11:51:28,261 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (186 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   168 | INFO |
| Total closed lots           |  2554 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1514 med=+4.6% | TAINTED n=1920 med=-38.6% | KEEP-only n=800 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T155622Z

- UTC timestamp: `20260928T155622Z`
- GitHub run: [#11198](https://github.com/28twagg-ops/TradingBot/actions/runs/36447200493)
- Run id: `36447200493`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`26s`
- Full logs: `logs/action_runs/20260928T155622Z_live_bot.log`, `logs/action_runs/20260928T155622Z_live_options.log`, `logs/action_runs/20260928T155622Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1514 | 50.1 | +4.6 | +43.4 | $+19,730 |
| TAINTED | 1920 | 33.5 | -38.6 | +12.8 | $-9,344 |
| KEEP-only | 800 | 63.2 | +52.8 | +66.5 | $+13,831 |
| KEEP-only recent | 605 | 62.5 | +56.9 | +76.6 | $+9,746 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T11:56:28.686723-04:00","date":"2026-09-28","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":16.2,"phases_s":{"reconcile":0.3,"cancel":0.13,"manage":13.41,"protective_stops":1.72},"signals":0,"placed":0,"equity":995503.49,"open_positions":42,"pending_orders":0,"open_lots":168,"submitted_today":103,"filled_today":121,"unattributed_contracts":0,"top_signals":[],"github_run":"11198","github_run_id":"36447200493","status":"ok","data_quality":{"clean":{"n":1514,"win":50.13,"med":4.62,"avg":43.4,"pnl":19729.83},"tainted":{"n":1920,"win":33.54,"med":-38.59,"avg":12.78,"pnl":-9344.28},"keep_only":{"n":800,"win":63.25,"med":52.75,"avg":66.54,"pnl":13831.45},"keep_only_recent":{"n":605,"win":62.48,"med":56.92,"avg":76.59,"pnl":9746.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:56:23  INFO      Mode: exits
15:56:23  INFO        Daily log -> logs/daily/2026-09-28.md
15:56:23  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
15:56:24  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T11:56:25.268443-04:00 share=25% ===
2026-09-28 11:56:25,268 INFO === options_live_micro LIVE 2026-09-28T11:56:25.268443-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 11:56:25,406 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: manage/exits only
2026-09-28 11:56:25,525 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-28 11:56:25,562 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (188 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   168 | INFO |
| Total closed lots           |  2554 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1514 med=+4.6% | TAINTED n=1920 med=-38.6% | KEEP-only n=800 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T160216Z

- UTC timestamp: `20260928T160216Z`
- GitHub run: [#11199](https://github.com/28twagg-ops/TradingBot/actions/runs/36447812724)
- Run id: `36447812724`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`25s`
- Full logs: `logs/action_runs/20260928T160216Z_live_bot.log`, `logs/action_runs/20260928T160216Z_live_options.log`, `logs/action_runs/20260928T160216Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1514 | 50.1 | +4.6 | +43.4 | $+19,730 |
| TAINTED | 1920 | 33.5 | -38.6 | +12.8 | $-9,344 |
| KEEP-only | 800 | 63.2 | +52.8 | +66.5 | $+13,831 |
| KEEP-only recent | 605 | 62.5 | +56.9 | +76.6 | $+9,746 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T12:02:21.560092-04:00","date":"2026-09-28","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":13.8,"phases_s":{"reconcile":0.23,"cancel":0.08,"manage":11.83,"protective_stops":1.04},"signals":0,"placed":0,"equity":995601.99,"open_positions":42,"pending_orders":0,"open_lots":168,"submitted_today":103,"filled_today":121,"unattributed_contracts":0,"top_signals":[],"github_run":"11199","github_run_id":"36447812724","status":"ok","data_quality":{"clean":{"n":1514,"win":50.13,"med":4.62,"avg":43.4,"pnl":19729.83},"tainted":{"n":1920,"win":33.54,"med":-38.59,"avg":12.78,"pnl":-9344.28},"keep_only":{"n":800,"win":63.25,"med":52.75,"avg":66.54,"pnl":13831.45},"keep_only_recent":{"n":605,"win":62.48,"med":56.92,"avg":76.59,"pnl":9746.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:02:17  INFO      Mode: exits
16:02:17  INFO        Daily log -> logs/daily/2026-09-28.md
16:02:17  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
16:02:17  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:02 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T12:02:18.738498-04:00 share=25% ===
2026-09-28 12:02:18,738 INFO === options_live_micro LIVE 2026-09-28T12:02:18.738498-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 12:02:18,822 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: manage/exits only
2026-09-28 12:02:18,889 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-28 12:02:18,909 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (187 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   168 | INFO |
| Total closed lots           |  2554 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1514 med=+4.6% | TAINTED n=1920 med=-38.6% | KEEP-only n=800 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T160632Z

- UTC timestamp: `20260928T160632Z`
- GitHub run: [#11200](https://github.com/28twagg-ops/TradingBot/actions/runs/36448427465)
- Run id: `36448427465`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`33s`
- Full logs: `logs/action_runs/20260928T160632Z_live_bot.log`, `logs/action_runs/20260928T160632Z_live_options.log`, `logs/action_runs/20260928T160632Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1514 | 50.1 | +4.6 | +43.4 | $+19,730 |
| TAINTED | 1920 | 33.5 | -38.6 | +12.8 | $-9,344 |
| KEEP-only | 800 | 63.2 | +52.8 | +66.5 | $+13,831 |
| KEEP-only recent | 605 | 62.5 | +56.9 | +76.6 | $+9,746 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T12:06:39.795623-04:00","date":"2026-09-28","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":20.2,"phases_s":{"reconcile":0.53,"cancel":0.25,"manage":14.97,"protective_stops":3.45},"signals":0,"placed":0,"equity":995790.63,"open_positions":42,"pending_orders":0,"open_lots":168,"submitted_today":103,"filled_today":121,"unattributed_contracts":0,"top_signals":[],"github_run":"11200","github_run_id":"36448427465","status":"ok","data_quality":{"clean":{"n":1514,"win":50.13,"med":4.62,"avg":43.4,"pnl":19729.83},"tainted":{"n":1920,"win":33.54,"med":-38.59,"avg":12.78,"pnl":-9344.28},"keep_only":{"n":800,"win":63.25,"med":52.75,"avg":66.54,"pnl":13831.45},"keep_only_recent":{"n":605,"win":62.48,"med":56.92,"avg":76.59,"pnl":9746.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:06:33  INFO      Mode: exits
16:06:34  INFO        Daily log -> logs/daily/2026-09-28.md
16:06:34  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
16:06:34  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T12:06:35.678592-04:00 share=25% ===
2026-09-28 12:06:35,678 INFO === options_live_micro LIVE 2026-09-28T12:06:35.678592-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 12:06:36,148 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: manage/exits only
2026-09-28 12:06:36,380 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-28 12:06:36,458 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (187 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   168 | INFO |
| Total closed lots           |  2554 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1514 med=+4.6% | TAINTED n=1920 med=-38.6% | KEEP-only n=800 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T161121Z

- UTC timestamp: `20260928T161121Z`
- GitHub run: [#11201](https://github.com/28twagg-ops/TradingBot/actions/runs/36449051001)
- Run id: `36449051001`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`31s`
- Full logs: `logs/action_runs/20260928T161121Z_live_bot.log`, `logs/action_runs/20260928T161121Z_live_options.log`, `logs/action_runs/20260928T161121Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1514 | 50.1 | +4.6 | +43.4 | $+19,730 |
| TAINTED | 1920 | 33.5 | -38.6 | +12.8 | $-9,344 |
| KEEP-only | 800 | 63.2 | +52.8 | +66.5 | $+13,831 |
| KEEP-only recent | 605 | 62.5 | +56.9 | +76.6 | $+9,746 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T12:11:28.168899-04:00","date":"2026-09-28","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":18.9,"phases_s":{"reconcile":0.48,"cancel":0.2,"manage":14.7,"protective_stops":2.76},"signals":0,"placed":0,"equity":995944.49,"open_positions":42,"pending_orders":0,"open_lots":168,"submitted_today":103,"filled_today":121,"unattributed_contracts":0,"top_signals":[],"github_run":"11201","github_run_id":"36449051001","status":"ok","data_quality":{"clean":{"n":1514,"win":50.13,"med":4.62,"avg":43.4,"pnl":19729.83},"tainted":{"n":1920,"win":33.54,"med":-38.59,"avg":12.78,"pnl":-9344.28},"keep_only":{"n":800,"win":63.25,"med":52.75,"avg":66.54,"pnl":13831.45},"keep_only_recent":{"n":605,"win":62.48,"med":56.92,"avg":76.59,"pnl":9746.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:11:22  INFO      Mode: exits
16:11:23  INFO        Daily log -> logs/daily/2026-09-28.md
16:11:23  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
16:11:23  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T12:11:24.698097-04:00 share=25% ===
2026-09-28 12:11:24,698 INFO === options_live_micro LIVE 2026-09-28T12:11:24.698097-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 12:11:24,897 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: manage/exits only
2026-09-28 12:11:25,068 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-28 12:11:25,125 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (193 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   168 | INFO |
| Total closed lots           |  2554 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1514 med=+4.6% | TAINTED n=1920 med=-38.6% | KEEP-only n=800 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T161617Z

- UTC timestamp: `20260928T161617Z`
- GitHub run: [#11202](https://github.com/28twagg-ops/TradingBot/actions/runs/36449662567)
- Run id: `36449662567`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260928T161617Z_live_bot.log`, `logs/action_runs/20260928T161617Z_live_options.log`, `logs/action_runs/20260928T161617Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1516 | 50.2 | +8.6 | +43.4 | $+19,814 |
| TAINTED | 1920 | 33.5 | -38.6 | +12.8 | $-9,344 |
| KEEP-only | 801 | 63.3 | +52.8 | +66.5 | $+13,872 |
| KEEP-only recent | 606 | 62.5 | +56.9 | +76.6 | $+9,787 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T12:16:22.629417-04:00","date":"2026-09-28","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":9.9,"phases_s":{"reconcile":0.25,"cancel":0.05,"manage":8.4,"protective_stops":0.56},"signals":0,"placed":0,"equity":995764.45,"open_positions":41,"pending_orders":0,"open_lots":166,"submitted_today":103,"filled_today":121,"unattributed_contracts":0,"top_signals":[],"github_run":"11202","github_run_id":"36449662567","status":"ok","data_quality":{"clean":{"n":1516,"win":50.2,"med":8.63,"avg":43.42,"pnl":19813.83},"tainted":{"n":1920,"win":33.54,"med":-38.59,"avg":12.78,"pnl":-9344.28},"keep_only":{"n":801,"win":63.3,"med":52.78,"avg":66.53,"pnl":13872.45},"keep_only_recent":{"n":606,"win":62.54,"med":56.92,"avg":76.56,"pnl":9787.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:16:18  INFO      Mode: exits
16:16:18  INFO        Daily log -> logs/daily/2026-09-28.md
16:16:18  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
16:16:19  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T12:16:19.868984-04:00 share=25% ===
2026-09-28 12:16:19,869 INFO === options_live_micro LIVE 2026-09-28T12:16:19.868984-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 12:16:19,933 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: manage/exits only
2026-09-28 12:16:19,968 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-28 12:16:19,978 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (192 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   166 | INFO |
| Total closed lots           |  2556 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1516 med=+8.6% | TAINTED n=1920 med=-38.6% | KEEP-only n=801 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T162201Z

- UTC timestamp: `20260928T162201Z`
- GitHub run: [#11203](https://github.com/28twagg-ops/TradingBot/actions/runs/36450256589)
- Run id: `36450256589`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`23s`
- Full logs: `logs/action_runs/20260928T162201Z_live_bot.log`, `logs/action_runs/20260928T162201Z_live_options.log`, `logs/action_runs/20260928T162201Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1518 | 50.2 | +8.6 | +43.4 | $+19,827 |
| TAINTED | 1921 | 33.5 | -38.8 | +12.7 | $-9,355 |
| KEEP-only | 803 | 63.3 | +52.8 | +66.4 | $+13,885 |
| KEEP-only recent | 608 | 62.5 | +56.9 | +76.3 | $+9,800 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T12:22:07.126803-04:00","date":"2026-09-28","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":10.5,"phases_s":{"reconcile":0.25,"cancel":0.04,"manage":9.12,"protective_stops":0.53},"signals":0,"placed":0,"equity":996519.26,"open_positions":40,"pending_orders":0,"open_lots":162,"submitted_today":103,"filled_today":121,"unattributed_contracts":0,"top_signals":[],"github_run":"11203","github_run_id":"36450256589","status":"ok","data_quality":{"clean":{"n":1518,"win":50.2,"med":8.63,"avg":43.37,"pnl":19826.83},"tainted":{"n":1921,"win":33.52,"med":-38.81,"avg":12.73,"pnl":-9355.28},"keep_only":{"n":803,"win":63.26,"med":52.78,"avg":66.37,"pnl":13885.45},"keep_only_recent":{"n":608,"win":62.5,"med":56.92,"avg":76.31,"pnl":9800.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:22:02  INFO      Mode: exits
16:22:03  INFO        Daily log -> logs/daily/2026-09-28.md
16:22:03  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
16:22:03  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:22 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T12:22:04.300812-04:00 share=25% ===
2026-09-28 12:22:04,300 INFO === options_live_micro LIVE 2026-09-28T12:22:04.300812-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 12:22:04,352 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: manage/exits only
2026-09-28 12:22:04,373 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-28 12:22:04,380 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (197 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   162 | INFO |
| Total closed lots           |  2559 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1518 med=+8.6% | TAINTED n=1921 med=-38.8% | KEEP-only n=803 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T162919Z

- UTC timestamp: `20260928T162919Z`
- GitHub run: [#11204](https://github.com/28twagg-ops/TradingBot/actions/runs/36450862439)
- Run id: `36450862439`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`33s`
- Full logs: `logs/action_runs/20260928T162919Z_live_bot.log`, `logs/action_runs/20260928T162919Z_live_options.log`, `logs/action_runs/20260928T162919Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1522 | 50.2 | +8.6 | +43.3 | $+19,889 |
| TAINTED | 1921 | 33.5 | -38.8 | +12.7 | $-9,355 |
| KEEP-only | 807 | 63.2 | +52.8 | +66.1 | $+13,947 |
| KEEP-only recent | 612 | 62.4 | +56.9 | +75.9 | $+9,862 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T12:29:27.583069-04:00","date":"2026-09-28","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":20.8,"phases_s":{"reconcile":0.71,"cancel":0.24,"manage":15.23,"protective_stops":3.76},"signals":0,"placed":0,"equity":997199.27,"open_positions":40,"pending_orders":0,"open_lots":157,"submitted_today":103,"filled_today":121,"unattributed_contracts":0,"top_signals":[],"github_run":"11204","github_run_id":"36450862439","status":"ok","data_quality":{"clean":{"n":1522,"win":50.2,"med":8.63,"avg":43.27,"pnl":19888.83},"tainted":{"n":1921,"win":33.52,"med":-38.81,"avg":12.73,"pnl":-9355.28},"keep_only":{"n":807,"win":63.2,"med":52.78,"avg":66.08,"pnl":13947.45},"keep_only_recent":{"n":612,"win":62.42,"med":56.92,"avg":75.87,"pnl":9862.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:29:20  INFO      Mode: exits
16:29:21  INFO        Daily log -> logs/daily/2026-09-28.md
16:29:21  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
16:29:22  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:29 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T12:29:23.380936-04:00 share=25% ===
2026-09-28 12:29:23,381 INFO === options_live_micro LIVE 2026-09-28T12:29:23.380936-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 12:29:23,636 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: manage/exits only
2026-09-28 12:29:23,865 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-28 12:29:23,943 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (193 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   157 | INFO |
| Total closed lots           |  2563 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1522 med=+8.6% | TAINTED n=1921 med=-38.8% | KEEP-only n=807 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T163137Z

- UTC timestamp: `20260928T163137Z`
- GitHub run: [#11205](https://github.com/28twagg-ops/TradingBot/actions/runs/36451474773)
- Run id: `36451474773`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`32s`
- Full logs: `logs/action_runs/20260928T163137Z_live_bot.log`, `logs/action_runs/20260928T163137Z_live_options.log`, `logs/action_runs/20260928T163137Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1522 | 50.2 | +8.6 | +43.3 | $+19,889 |
| TAINTED | 1921 | 33.5 | -38.8 | +12.7 | $-9,355 |
| KEEP-only | 807 | 63.2 | +52.8 | +66.1 | $+13,947 |
| KEEP-only recent | 612 | 62.4 | +56.9 | +75.9 | $+9,862 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T12:31:45.343233-04:00","date":"2026-09-28","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":19.0,"phases_s":{"reconcile":0.69,"cancel":0.23,"manage":13.43,"protective_stops":3.74},"signals":0,"placed":0,"equity":996989.24,"open_positions":40,"pending_orders":0,"open_lots":157,"submitted_today":103,"filled_today":121,"unattributed_contracts":0,"top_signals":[],"github_run":"11205","github_run_id":"36451474773","status":"ok","data_quality":{"clean":{"n":1522,"win":50.2,"med":8.63,"avg":43.27,"pnl":19888.83},"tainted":{"n":1921,"win":33.52,"med":-38.81,"avg":12.73,"pnl":-9355.28},"keep_only":{"n":807,"win":63.2,"med":52.78,"avg":66.08,"pnl":13947.45},"keep_only_recent":{"n":612,"win":62.42,"med":56.92,"avg":75.87,"pnl":9862.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:31:39  INFO      Mode: exits
16:31:40  INFO        Daily log -> logs/daily/2026-09-28.md
16:31:40  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
16:31:40  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T12:31:41.577634-04:00 share=25% ===
2026-09-28 12:31:41,577 INFO === options_live_micro LIVE 2026-09-28T12:31:41.577634-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 12:31:41,812 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: manage/exits only
2026-09-28 12:31:42,020 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-28 12:31:42,092 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (191 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   157 | INFO |
| Total closed lots           |  2563 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1522 med=+8.6% | TAINTED n=1921 med=-38.8% | KEEP-only n=807 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T163622Z

- UTC timestamp: `20260928T163622Z`
- GitHub run: [#11206](https://github.com/28twagg-ops/TradingBot/actions/runs/36452083618)
- Run id: `36452083618`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`23s`
- Full logs: `logs/action_runs/20260928T163622Z_live_bot.log`, `logs/action_runs/20260928T163622Z_live_options.log`, `logs/action_runs/20260928T163622Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1522 | 50.2 | +8.6 | +43.3 | $+19,889 |
| TAINTED | 1921 | 33.5 | -38.8 | +12.7 | $-9,355 |
| KEEP-only | 807 | 63.2 | +52.8 | +66.1 | $+13,947 |
| KEEP-only recent | 612 | 62.4 | +56.9 | +75.9 | $+9,862 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T12:36:27.157051-04:00","date":"2026-09-28","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":10.2,"phases_s":{"reconcile":0.12,"cancel":0.04,"manage":8.83,"protective_stops":0.59},"signals":0,"placed":0,"equity":996691.27,"open_positions":40,"pending_orders":0,"open_lots":157,"submitted_today":103,"filled_today":121,"unattributed_contracts":0,"top_signals":[],"github_run":"11206","github_run_id":"36452083618","status":"ok","data_quality":{"clean":{"n":1522,"win":50.2,"med":8.63,"avg":43.27,"pnl":19888.83},"tainted":{"n":1921,"win":33.52,"med":-38.81,"avg":12.73,"pnl":-9355.28},"keep_only":{"n":807,"win":63.2,"med":52.78,"avg":66.08,"pnl":13947.45},"keep_only_recent":{"n":612,"win":62.42,"med":56.92,"avg":75.87,"pnl":9862.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:36:22  INFO      Mode: exits
16:36:23  INFO        Daily log -> logs/daily/2026-09-28.md
16:36:23  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
16:36:23  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T12:36:24.268867-04:00 share=25% ===
2026-09-28 12:36:24,268 INFO === options_live_micro LIVE 2026-09-28T12:36:24.268867-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 12:36:24,353 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: manage/exits only
2026-09-28 12:36:24,375 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-28 12:36:24,381 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (191 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   157 | INFO |
| Total closed lots           |  2563 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1522 med=+8.6% | TAINTED n=1921 med=-38.8% | KEEP-only n=807 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T164400Z

- UTC timestamp: `20260928T164400Z`
- GitHub run: [#11207](https://github.com/28twagg-ops/TradingBot/actions/runs/36452684593)
- Run id: `36452684593`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260928T164400Z_live_bot.log`, `logs/action_runs/20260928T164400Z_live_options.log`, `logs/action_runs/20260928T164400Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1522 | 50.2 | +8.6 | +43.3 | $+19,889 |
| TAINTED | 1921 | 33.5 | -38.8 | +12.7 | $-9,355 |
| KEEP-only | 807 | 63.2 | +52.8 | +66.1 | $+13,947 |
| KEEP-only recent | 612 | 62.4 | +56.9 | +75.9 | $+9,862 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T12:44:04.989978-04:00","date":"2026-09-28","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":8.7,"phases_s":{"reconcile":0.12,"cancel":0.04,"manage":7.37,"protective_stops":0.63},"signals":0,"placed":0,"equity":996365.27,"open_positions":40,"pending_orders":0,"open_lots":157,"submitted_today":103,"filled_today":121,"unattributed_contracts":0,"top_signals":[],"github_run":"11207","github_run_id":"36452684593","status":"ok","data_quality":{"clean":{"n":1522,"win":50.2,"med":8.63,"avg":43.27,"pnl":19888.83},"tainted":{"n":1921,"win":33.52,"med":-38.81,"avg":12.73,"pnl":-9355.28},"keep_only":{"n":807,"win":63.2,"med":52.78,"avg":66.08,"pnl":13947.45},"keep_only_recent":{"n":612,"win":62.42,"med":56.92,"avg":75.87,"pnl":9862.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:44:00  INFO      Mode: exits
16:44:01  INFO        Daily log -> logs/daily/2026-09-28.md
16:44:01  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
16:44:01  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:44 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T12:44:02.304890-04:00 share=25% ===
2026-09-28 12:44:02,304 INFO === options_live_micro LIVE 2026-09-28T12:44:02.304890-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 12:44:02,349 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: manage/exits only
2026-09-28 12:44:02,370 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-28 12:44:02,377 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (189 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   157 | INFO |
| Total closed lots           |  2563 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1522 med=+8.6% | TAINTED n=1921 med=-38.8% | KEEP-only n=807 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T164632Z

- UTC timestamp: `20260928T164632Z`
- GitHub run: [#11208](https://github.com/28twagg-ops/TradingBot/actions/runs/36453273038)
- Run id: `36453273038`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`20s`
- Full logs: `logs/action_runs/20260928T164632Z_live_bot.log`, `logs/action_runs/20260928T164632Z_live_options.log`, `logs/action_runs/20260928T164632Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1522 | 50.2 | +8.6 | +43.3 | $+19,889 |
| TAINTED | 1921 | 33.5 | -38.8 | +12.7 | $-9,355 |
| KEEP-only | 807 | 63.2 | +52.8 | +66.1 | $+13,947 |
| KEEP-only recent | 612 | 62.4 | +56.9 | +75.9 | $+9,862 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T12:46:37.684285-04:00","date":"2026-09-28","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":8.5,"phases_s":{"reconcile":0.15,"cancel":0.06,"manage":7.04,"protective_stops":0.7},"signals":0,"placed":0,"equity":996261.17,"open_positions":40,"pending_orders":0,"open_lots":157,"submitted_today":103,"filled_today":121,"unattributed_contracts":0,"top_signals":[],"github_run":"11208","github_run_id":"36453273038","status":"ok","data_quality":{"clean":{"n":1522,"win":50.2,"med":8.63,"avg":43.27,"pnl":19888.83},"tainted":{"n":1921,"win":33.52,"med":-38.81,"avg":12.73,"pnl":-9355.28},"keep_only":{"n":807,"win":63.2,"med":52.78,"avg":66.08,"pnl":13947.45},"keep_only_recent":{"n":612,"win":62.42,"med":56.92,"avg":75.87,"pnl":9862.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:46:33  INFO      Mode: exits
16:46:34  INFO        Daily log -> logs/daily/2026-09-28.md
16:46:34  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
16:46:34  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T12:46:34.993074-04:00 share=25% ===
2026-09-28 12:46:34,993 INFO === options_live_micro LIVE 2026-09-28T12:46:34.993074-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 12:46:35,051 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: manage/exits only
2026-09-28 12:46:35,085 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-28 12:46:35,096 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (191 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   157 | INFO |
| Total closed lots           |  2563 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1522 med=+8.6% | TAINTED n=1921 med=-38.8% | KEEP-only n=807 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
