# Daily Comprehensive Action Review - 2026-11-19

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20261119T000141Z

- UTC timestamp: `20261119T000141Z`
- GitHub run: [#16156](https://github.com/28twagg-ops/TradingBot/actions/runs/44425397768)
- Run id: `44425397768`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20261119T000141Z_live_bot.log`, `logs/action_runs/20261119T000141Z_live_options.log`, `logs/action_runs/20261119T000141Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-18T19:01:45.832195-05:00","date":"2026-11-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.33},"signals":0,"placed":0,"equity":989501.77,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":8,"filled_today":7,"unattributed_contracts":0,"top_signals":[],"github_run":"16156","github_run_id":"44425397768","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
00:01:42  INFO      Mode: ext_exits
00:01:42  INFO        Daily log -> logs/daily/2026-11-19.md
00:01:42  INFO        Daily log reconciled -> logs/daily/2026-11-19.md (0 ledger rows)
00:01:43  INFO        Daily log -> logs/daily/2026-11-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         00:01 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $230.09|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AMP  P&L -0.4%  $-0.14          HOLDING until 9:35am scan (Pullback50)|
|  AMCR  P&L -0.3%  $-0.19         HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
=== options_live_micro LIVE 2026-11-18T19:01:43.581432-05:00 share=25% ===
2026-11-18 19:01:43,581 INFO === options_live_micro LIVE 2026-11-18T19:01:43.581432-05:00 share=25% ===
Live account equity $230.09 cash $126.80 #225458845 options_level=3
2026-11-18 19:01:43,733 INFO Live account equity $230.09 cash $126.80 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-11-18 19:01:43,871 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (225 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.09 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T000650Z

- UTC timestamp: `20261119T000650Z`
- GitHub run: [#16157](https://github.com/28twagg-ops/TradingBot/actions/runs/44426090569)
- Run id: `44426090569`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`10s`
- Full logs: `logs/action_runs/20261119T000650Z_live_bot.log`, `logs/action_runs/20261119T000650Z_live_options.log`, `logs/action_runs/20261119T000650Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-18T19:06:56.091842-05:00","date":"2026-11-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.51},"signals":0,"placed":0,"equity":989485.77,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":8,"filled_today":7,"unattributed_contracts":0,"top_signals":[],"github_run":"16157","github_run_id":"44426090569","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
00:06:51  INFO      Mode: ext_exits
00:06:53  INFO        Daily log -> logs/daily/2026-11-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         00:06 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $230.09|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AMP  P&L -0.4%  $-0.14          HOLDING until 9:35am scan (Pullback50)|
|  AMCR  P&L -0.3%  $-0.19         HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
=== options_live_micro LIVE 2026-11-18T19:06:53.558590-05:00 share=25% ===
2026-11-18 19:06:53,558 INFO === options_live_micro LIVE 2026-11-18T19:06:53.558590-05:00 share=25% ===
Live account equity $230.09 cash $126.80 #225458845 options_level=3
2026-11-18 19:06:53,769 INFO Live account equity $230.09 cash $126.80 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-11-18 19:06:53,976 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (225 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.09 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T001150Z

- UTC timestamp: `20261119T001150Z`
- GitHub run: [#16158](https://github.com/28twagg-ops/TradingBot/actions/runs/44426782657)
- Run id: `44426782657`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20261119T001150Z_live_bot.log`, `logs/action_runs/20261119T001150Z_live_options.log`, `logs/action_runs/20261119T001150Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-18T19:11:54.950617-05:00","date":"2026-11-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":989637.45,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":8,"filled_today":7,"unattributed_contracts":0,"top_signals":[],"github_run":"16158","github_run_id":"44426782657","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
00:11:51  INFO      Mode: ext_exits
00:11:52  INFO        Daily log -> logs/daily/2026-11-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         00:11 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $230.09|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AMP  P&L -0.4%  $-0.14          HOLDING until 9:35am scan (Pullback50)|
|  AMCR  P&L -0.3%  $-0.19         HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
=== options_live_micro LIVE 2026-11-18T19:11:52.716035-05:00 share=25% ===
2026-11-18 19:11:52,716 INFO === options_live_micro LIVE 2026-11-18T19:11:52.716035-05:00 share=25% ===
Live account equity $230.09 cash $126.80 #225458845 options_level=3
2026-11-18 19:11:52,765 INFO Live account equity $230.09 cash $126.80 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-11-18 19:11:52,799 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (225 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.09 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T001656Z

- UTC timestamp: `20261119T001656Z`
- GitHub run: [#16159](https://github.com/28twagg-ops/TradingBot/actions/runs/44427475675)
- Run id: `44427475675`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`15s`
- Full logs: `logs/action_runs/20261119T001656Z_live_bot.log`, `logs/action_runs/20261119T001656Z_live_options.log`, `logs/action_runs/20261119T001656Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-18T19:17:02.454874-05:00","date":"2026-11-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.52},"signals":0,"placed":0,"equity":989645.19,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":8,"filled_today":7,"unattributed_contracts":0,"top_signals":[],"github_run":"16159","github_run_id":"44427475675","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
00:16:57  INFO      Mode: ext_exits
00:16:58  INFO        Daily log -> logs/daily/2026-11-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         00:16 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $230.09|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AMP  P&L -0.4%  $-0.14          HOLDING until 9:35am scan (Pullback50)|
|  AMCR  P&L -0.3%  $-0.19         HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
=== options_live_micro LIVE 2026-11-18T19:16:59.177539-05:00 share=25% ===
2026-11-18 19:16:59,177 INFO === options_live_micro LIVE 2026-11-18T19:16:59.177539-05:00 share=25% ===
Live account equity $230.09 cash $126.80 #225458845 options_level=3
2026-11-18 19:16:59,389 INFO Live account equity $230.09 cash $126.80 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-11-18 19:16:59,593 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (225 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.09 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T002159Z

- UTC timestamp: `20261119T002159Z`
- GitHub run: [#16160](https://github.com/28twagg-ops/TradingBot/actions/runs/44428144751)
- Run id: `44428144751`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20261119T002159Z_live_bot.log`, `logs/action_runs/20261119T002159Z_live_options.log`, `logs/action_runs/20261119T002159Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-18T19:22:05.483868-05:00","date":"2026-11-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.52},"signals":0,"placed":0,"equity":989576.22,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":8,"filled_today":7,"unattributed_contracts":0,"top_signals":[],"github_run":"16160","github_run_id":"44428144751","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
00:22:01  INFO      Mode: ext_exits
00:22:02  INFO        Daily log -> logs/daily/2026-11-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         00:22 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $230.09|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AMP  P&L -0.4%  $-0.14          HOLDING until 9:35am scan (Pullback50)|
|  AMCR  P&L -0.3%  $-0.19         HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
=== options_live_micro LIVE 2026-11-18T19:22:02.848487-05:00 share=25% ===
2026-11-18 19:22:02,848 INFO === options_live_micro LIVE 2026-11-18T19:22:02.848487-05:00 share=25% ===
Live account equity $230.09 cash $126.80 #225458845 options_level=3
2026-11-18 19:22:03,059 INFO Live account equity $230.09 cash $126.80 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-11-18 19:22:03,266 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (225 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.09 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T002637Z

- UTC timestamp: `20261119T002637Z`
- GitHub run: [#16161](https://github.com/28twagg-ops/TradingBot/actions/runs/44428815543)
- Run id: `44428815543`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`10s`
- Full logs: `logs/action_runs/20261119T002637Z_live_bot.log`, `logs/action_runs/20261119T002637Z_live_options.log`, `logs/action_runs/20261119T002637Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-18T19:26:41.838737-05:00","date":"2026-11-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.35},"signals":0,"placed":0,"equity":989508.77,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":8,"filled_today":7,"unattributed_contracts":0,"top_signals":[],"github_run":"16161","github_run_id":"44428815543","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
00:26:38  INFO      Mode: ext_exits
00:26:39  INFO        Daily log -> logs/daily/2026-11-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         00:26 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $230.09|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AMP  P&L -0.4%  $-0.14          HOLDING until 9:35am scan (Pullback50)|
|  AMCR  P&L -0.3%  $-0.19         HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
=== options_live_micro LIVE 2026-11-18T19:26:39.680921-05:00 share=25% ===
2026-11-18 19:26:39,680 INFO === options_live_micro LIVE 2026-11-18T19:26:39.680921-05:00 share=25% ===
Live account equity $230.09 cash $126.80 #225458845 options_level=3
2026-11-18 19:26:39,837 INFO Live account equity $230.09 cash $126.80 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-11-18 19:26:39,976 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (225 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.09 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T003148Z

- UTC timestamp: `20261119T003148Z`
- GitHub run: [#16162](https://github.com/28twagg-ops/TradingBot/actions/runs/44429481247)
- Run id: `44429481247`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20261119T003148Z_live_bot.log`, `logs/action_runs/20261119T003148Z_live_options.log`, `logs/action_runs/20261119T003148Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-18T19:31:53.972291-05:00","date":"2026-11-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.48},"signals":0,"placed":0,"equity":989460.77,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":8,"filled_today":7,"unattributed_contracts":0,"top_signals":[],"github_run":"16162","github_run_id":"44429481247","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
00:31:49  INFO      Mode: ext_exits
00:31:50  INFO        Daily log -> logs/daily/2026-11-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         00:31 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $230.09|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AMP  P&L -0.4%  $-0.14          HOLDING until 9:35am scan (Pullback50)|
|  AMCR  P&L -0.3%  $-0.19         HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
=== options_live_micro LIVE 2026-11-18T19:31:50.923595-05:00 share=25% ===
2026-11-18 19:31:50,923 INFO === options_live_micro LIVE 2026-11-18T19:31:50.923595-05:00 share=25% ===
Live account equity $230.09 cash $126.80 #225458845 options_level=3
2026-11-18 19:31:51,149 INFO Live account equity $230.09 cash $126.80 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-11-18 19:31:51,349 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (225 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.09 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T003637Z

- UTC timestamp: `20261119T003637Z`
- GitHub run: [#16163](https://github.com/28twagg-ops/TradingBot/actions/runs/44430162254)
- Run id: `44430162254`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20261119T003637Z_live_bot.log`, `logs/action_runs/20261119T003637Z_live_options.log`, `logs/action_runs/20261119T003637Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-18T19:36:41.952495-05:00","date":"2026-11-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.18},"signals":0,"placed":0,"equity":989406.91,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":8,"filled_today":7,"unattributed_contracts":0,"top_signals":[],"github_run":"16163","github_run_id":"44430162254","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
00:36:38  INFO      Mode: ext_exits
00:36:38  INFO        Daily log -> logs/daily/2026-11-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         00:36 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $230.46|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AMP  P&L -0.4%  $-0.14          HOLDING until 9:35am scan (Pullback50)|
|  AMCR  P&L +0.3%  $+0.18         HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
=== options_live_micro LIVE 2026-11-18T19:36:39.564124-05:00 share=25% ===
2026-11-18 19:36:39,564 INFO === options_live_micro LIVE 2026-11-18T19:36:39.564124-05:00 share=25% ===
Live account equity $230.46 cash $126.80 #225458845 options_level=3
2026-11-18 19:36:39,636 INFO Live account equity $230.46 cash $126.80 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-11-18 19:36:39,700 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (225 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.46 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T004146Z

- UTC timestamp: `20261119T004146Z`
- GitHub run: [#16164](https://github.com/28twagg-ops/TradingBot/actions/runs/44430829555)
- Run id: `44430829555`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20261119T004146Z_live_bot.log`, `logs/action_runs/20261119T004146Z_live_options.log`, `logs/action_runs/20261119T004146Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-18T19:41:50.522374-05:00","date":"2026-11-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.26},"signals":0,"placed":0,"equity":989420.77,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":8,"filled_today":7,"unattributed_contracts":0,"top_signals":[],"github_run":"16164","github_run_id":"44430829555","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
00:41:47  INFO      Mode: ext_exits
00:41:47  INFO        Daily log -> logs/daily/2026-11-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         00:41 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $230.46|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AMP  P&L -0.4%  $-0.14          HOLDING until 9:35am scan (Pullback50)|
|  AMCR  P&L +0.3%  $+0.18         HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
=== options_live_micro LIVE 2026-11-18T19:41:48.425850-05:00 share=25% ===
2026-11-18 19:41:48,425 INFO === options_live_micro LIVE 2026-11-18T19:41:48.425850-05:00 share=25% ===
Live account equity $230.46 cash $126.80 #225458845 options_level=3
2026-11-18 19:41:48,597 INFO Live account equity $230.46 cash $126.80 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-11-18 19:41:48,734 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (225 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.46 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T004644Z

- UTC timestamp: `20261119T004644Z`
- GitHub run: [#16165](https://github.com/28twagg-ops/TradingBot/actions/runs/44431503440)
- Run id: `44431503440`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20261119T004644Z_live_bot.log`, `logs/action_runs/20261119T004644Z_live_options.log`, `logs/action_runs/20261119T004644Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-18T19:46:49.534200-05:00","date":"2026-11-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.1},"signals":0,"placed":0,"equity":989451.65,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":8,"filled_today":7,"unattributed_contracts":0,"top_signals":[],"github_run":"16165","github_run_id":"44431503440","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
00:46:45  INFO      Mode: ext_exits
00:46:45  INFO        Daily log -> logs/daily/2026-11-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         00:46 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $230.46|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AMP  P&L -0.4%  $-0.14          HOLDING until 9:35am scan (Pullback50)|
|  AMCR  P&L +0.3%  $+0.18         HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
=== options_live_micro LIVE 2026-11-18T19:46:46.713320-05:00 share=25% ===
2026-11-18 19:46:46,713 INFO === options_live_micro LIVE 2026-11-18T19:46:46.713320-05:00 share=25% ===
Live account equity $230.46 cash $126.80 #225458845 options_level=3
2026-11-18 19:46:46,953 INFO Live account equity $230.46 cash $126.80 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-11-18 19:46:46,989 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (225 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.46 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T005152Z

- UTC timestamp: `20261119T005152Z`
- GitHub run: [#16166](https://github.com/28twagg-ops/TradingBot/actions/runs/44432168188)
- Run id: `44432168188`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20261119T005152Z_live_bot.log`, `logs/action_runs/20261119T005152Z_live_options.log`, `logs/action_runs/20261119T005152Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-18T19:51:57.849888-05:00","date":"2026-11-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.08},"signals":0,"placed":0,"equity":989427.04,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":8,"filled_today":7,"unattributed_contracts":0,"top_signals":[],"github_run":"16166","github_run_id":"44432168188","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
00:51:54  INFO      Mode: ext_exits
00:51:54  INFO        Daily log -> logs/daily/2026-11-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         00:51 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $230.46|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AMP  P&L -0.4%  $-0.14          HOLDING until 9:35am scan (Pullback50)|
|  AMCR  P&L +0.3%  $+0.18         HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
=== options_live_micro LIVE 2026-11-18T19:51:55.385347-05:00 share=25% ===
2026-11-18 19:51:55,385 INFO === options_live_micro LIVE 2026-11-18T19:51:55.385347-05:00 share=25% ===
Live account equity $230.46 cash $126.80 #225458845 options_level=3
2026-11-18 19:51:55,415 INFO Live account equity $230.46 cash $126.80 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-11-18 19:51:55,436 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (225 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.46 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T005642Z

- UTC timestamp: `20261119T005642Z`
- GitHub run: [#16167](https://github.com/28twagg-ops/TradingBot/actions/runs/44432841008)
- Run id: `44432841008`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`8s`
- Full logs: `logs/action_runs/20261119T005642Z_live_bot.log`, `logs/action_runs/20261119T005642Z_live_options.log`, `logs/action_runs/20261119T005642Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-18T19:56:45.854358-05:00","date":"2026-11-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.5,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":989449.93,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":8,"filled_today":7,"unattributed_contracts":0,"top_signals":[],"github_run":"16167","github_run_id":"44432841008","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
00:56:43  INFO      Mode: ext_exits
00:56:43  INFO        Daily log -> logs/daily/2026-11-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         00:56 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $230.46|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AMP  P&L -0.4%  $-0.14          HOLDING until 9:35am scan (Pullback50)|
|  AMCR  P&L +0.3%  $+0.18         HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
=== options_live_micro LIVE 2026-11-18T19:56:44.213376-05:00 share=25% ===
2026-11-18 19:56:44,213 INFO === options_live_micro LIVE 2026-11-18T19:56:44.213376-05:00 share=25% ===
Live account equity $230.46 cash $126.80 #225458845 options_level=3
2026-11-18 19:56:44,260 INFO Live account equity $230.46 cash $126.80 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-11-18 19:56:44,291 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (225 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.46 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T140150Z

- UTC timestamp: `20261119T140150Z`
- GitHub run: [#16168](https://github.com/28twagg-ops/TradingBot/actions/runs/44539053787)
- Run id: `44539053787`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20261119T140150Z_live_bot.log`, `logs/action_runs/20261119T140150Z_live_options.log`, `logs/action_runs/20261119T140150Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-19T09:01:54.301016-05:00","date":"2026-11-19","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.17},"signals":0,"placed":0,"equity":988953.36,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"16168","github_run_id":"44539053787","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
14:01:51  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         14:01 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $230.74|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.74|
|  Cash                                                           $126.80|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Total invested                                                 $103.94|
|  Open P&L                                                        $+0.32|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMCR     Pullback50      $69.26     $43.82   $43.93   +0.3%   $+0.18  |
|  AMP      Pullback50      $34.69     $503.48  $505.59  +0.4%   $+0.15  |
|                                                                        |
|  Total invested                                                 $103.94|
|  Total open P&L                                                  $+0.32|
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
|  2026-11-18  SELL  ANET  Pullback50  $34.60  P&L $+0.06                |
|  2026-11-18  SELL  ESS  Pullback50  $34.38  P&L $-0.19                 |
|  2026-11-18  SELL  AMCR  Pullback50  $34.50  P&L $-0.20                |
|  2026-11-18  SELL  AES  Pullback50  $34.66  P&L $+0.11                 |
|  2026-11-17  SELL  AES  Pullback50  $34.58  P&L $+0.00                 |
|  2026-11-17  SELL  LOPE  MomReversal  $34.55  P&L $-0.20               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-11-19T09:01:52.041026-05:00 share=25% ===
2026-11-19 09:01:52,041 INFO === options_live_micro LIVE 2026-11-19T09:01:52.041026-05:00 share=25% ===
Live account equity $230.74 cash $126.80 #225458845 options_level=3
2026-11-19 09:01:52,096 INFO Live account equity $230.74 cash $126.80 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-11-19 09:01:52,108 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-11-19 09:01:52,118 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (225 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.74 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T140644Z

- UTC timestamp: `20261119T140644Z`
- GitHub run: [#16169](https://github.com/28twagg-ops/TradingBot/actions/runs/44539925563)
- Run id: `44539925563`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`15s`
- Full logs: `logs/action_runs/20261119T140644Z_live_bot.log`, `logs/action_runs/20261119T140644Z_live_options.log`, `logs/action_runs/20261119T140644Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-19T09:06:49.475880-05:00","date":"2026-11-19","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.08},"signals":0,"placed":0,"equity":988920.37,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"16169","github_run_id":"44539925563","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
14:06:44  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         14:06 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $230.74|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.74|
|  Cash                                                           $126.80|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Total invested                                                 $103.94|
|  Open P&L                                                        $+0.32|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMCR     Pullback50      $69.26     $43.82   $43.93   +0.3%   $+0.18  |
|  AMP      Pullback50      $34.69     $503.48  $505.59  +0.4%   $+0.15  |
|                                                                        |
|  Total invested                                                 $103.94|
|  Total open P&L                                                  $+0.32|
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
|  2026-11-18  SELL  ANET  Pullback50  $34.60  P&L $+0.06                |
|  2026-11-18  SELL  ESS  Pullback50  $34.38  P&L $-0.19                 |
|  2026-11-18  SELL  AMCR  Pullback50  $34.50  P&L $-0.20                |
|  2026-11-18  SELL  AES  Pullback50  $34.66  P&L $+0.11                 |
|  2026-11-17  SELL  AES  Pullback50  $34.58  P&L $+0.00                 |
|  2026-11-17  SELL  LOPE  MomReversal  $34.55  P&L $-0.20               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-11-19T09:06:45.969626-05:00 share=25% ===
2026-11-19 09:06:45,969 INFO === options_live_micro LIVE 2026-11-19T09:06:45.969626-05:00 share=25% ===
Live account equity $230.74 cash $126.80 #225458845 options_level=3
2026-11-19 09:06:46,246 INFO Live account equity $230.74 cash $126.80 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-11-19 09:06:46,255 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-11-19 09:06:46,265 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (225 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.74 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T141141Z

- UTC timestamp: `20261119T141141Z`
- GitHub run: [#16170](https://github.com/28twagg-ops/TradingBot/actions/runs/44540809406)
- Run id: `44540809406`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20261119T141141Z_live_bot.log`, `logs/action_runs/20261119T141141Z_live_options.log`, `logs/action_runs/20261119T141141Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-19T09:11:46.008389-05:00","date":"2026-11-19","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.1},"signals":0,"placed":0,"equity":988780.26,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"16170","github_run_id":"44540809406","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
14:11:42  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         14:11 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $230.74|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.74|
|  Cash                                                           $126.80|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Total invested                                                 $103.94|
|  Open P&L                                                        $+0.32|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMCR     Pullback50      $69.26     $43.82   $43.93   +0.3%   $+0.18  |
|  AMP      Pullback50      $34.69     $503.48  $505.59  +0.4%   $+0.15  |
|                                                                        |
|  Total invested                                                 $103.94|
|  Total open P&L                                                  $+0.32|
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
|  2026-11-18  SELL  ANET  Pullback50  $34.60  P&L $+0.06                |
|  2026-11-18  SELL  ESS  Pullback50  $34.38  P&L $-0.19                 |
|  2026-11-18  SELL  AMCR  Pullback50  $34.50  P&L $-0.20                |
|  2026-11-18  SELL  AES  Pullback50  $34.66  P&L $+0.11                 |
|  2026-11-17  SELL  AES  Pullback50  $34.58  P&L $+0.00                 |
|  2026-11-17  SELL  LOPE  MomReversal  $34.55  P&L $-0.20               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-11-19T09:11:43.772259-05:00 share=25% ===
2026-11-19 09:11:43,772 INFO === options_live_micro LIVE 2026-11-19T09:11:43.772259-05:00 share=25% ===
Live account equity $230.74 cash $126.80 #225458845 options_level=3
2026-11-19 09:11:43,823 INFO Live account equity $230.74 cash $126.80 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-11-19 09:11:43,834 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-11-19 09:11:43,845 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (225 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.74 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T141649Z

- UTC timestamp: `20261119T141649Z`
- GitHub run: [#16171](https://github.com/28twagg-ops/TradingBot/actions/runs/44541698216)
- Run id: `44541698216`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20261119T141649Z_live_bot.log`, `logs/action_runs/20261119T141649Z_live_options.log`, `logs/action_runs/20261119T141649Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-19T09:16:55.337311-05:00","date":"2026-11-19","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":988735.3,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"16171","github_run_id":"44541698216","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
14:16:52  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         14:16 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $230.74|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.74|
|  Cash                                                           $126.80|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Total invested                                                 $103.94|
|  Open P&L                                                        $+0.32|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMCR     Pullback50      $69.26     $43.82   $43.93   +0.3%   $+0.18  |
|  AMP      Pullback50      $34.69     $503.48  $505.59  +0.4%   $+0.15  |
|                                                                        |
|  Total invested                                                 $103.94|
|  Total open P&L                                                  $+0.32|
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
|  2026-11-18  SELL  ANET  Pullback50  $34.60  P&L $+0.06                |
|  2026-11-18  SELL  ESS  Pullback50  $34.38  P&L $-0.19                 |
|  2026-11-18  SELL  AMCR  Pullback50  $34.50  P&L $-0.20                |
|  2026-11-18  SELL  AES  Pullback50  $34.66  P&L $+0.11                 |
|  2026-11-17  SELL  AES  Pullback50  $34.58  P&L $+0.00                 |
|  2026-11-17  SELL  LOPE  MomReversal  $34.55  P&L $-0.20               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-11-19T09:16:53.080358-05:00 share=25% ===
2026-11-19 09:16:53,080 INFO === options_live_micro LIVE 2026-11-19T09:16:53.080358-05:00 share=25% ===
Live account equity $230.74 cash $126.80 #225458845 options_level=3
2026-11-19 09:16:53,133 INFO Live account equity $230.74 cash $126.80 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-11-19 09:16:53,145 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-11-19 09:16:53,155 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (225 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.74 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T142200Z

- UTC timestamp: `20261119T142200Z`
- GitHub run: [#16172](https://github.com/28twagg-ops/TradingBot/actions/runs/44542585857)
- Run id: `44542585857`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20261119T142200Z_live_bot.log`, `logs/action_runs/20261119T142200Z_live_options.log`, `logs/action_runs/20261119T142200Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-19T09:22:06.078620-05:00","date":"2026-11-19","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.53},"signals":0,"placed":0,"equity":988814.55,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"16172","github_run_id":"44542585857","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
14:22:01  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         14:22 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $230.74|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.74|
|  Cash                                                           $126.80|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Total invested                                                 $103.94|
|  Open P&L                                                        $+0.32|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMCR     Pullback50      $69.26     $43.82   $43.93   +0.3%   $+0.18  |
|  AMP      Pullback50      $34.69     $503.48  $505.59  +0.4%   $+0.15  |
|                                                                        |
|  Total invested                                                 $103.94|
|  Total open P&L                                                  $+0.32|
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
|  2026-11-18  SELL  ANET  Pullback50  $34.60  P&L $+0.06                |
|  2026-11-18  SELL  ESS  Pullback50  $34.38  P&L $-0.19                 |
|  2026-11-18  SELL  AMCR  Pullback50  $34.50  P&L $-0.20                |
|  2026-11-18  SELL  AES  Pullback50  $34.66  P&L $+0.11                 |
|  2026-11-17  SELL  AES  Pullback50  $34.58  P&L $+0.00                 |
|  2026-11-17  SELL  LOPE  MomReversal  $34.55  P&L $-0.20               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-11-19T09:22:03.139072-05:00 share=25% ===
2026-11-19 09:22:03,139 INFO === options_live_micro LIVE 2026-11-19T09:22:03.139072-05:00 share=25% ===
Live account equity $230.74 cash $126.80 #225458845 options_level=3
2026-11-19 09:22:03,364 INFO Live account equity $230.74 cash $126.80 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-11-19 09:22:03,436 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-11-19 09:22:03,508 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (225 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.74 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T142652Z

- UTC timestamp: `20261119T142652Z`
- GitHub run: [#16173](https://github.com/28twagg-ops/TradingBot/actions/runs/44543500992)
- Run id: `44543500992`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20261119T142652Z_live_bot.log`, `logs/action_runs/20261119T142652Z_live_options.log`, `logs/action_runs/20261119T142652Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-19T09:26:56.933342-05:00","date":"2026-11-19","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.1},"signals":0,"placed":0,"equity":988782.44,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"16173","github_run_id":"44543500992","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
14:26:53  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         14:26 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $230.74|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.74|
|  Cash                                                           $126.80|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Total invested                                                 $103.94|
|  Open P&L                                                        $+0.32|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMCR     Pullback50      $69.26     $43.82   $43.93   +0.3%   $+0.18  |
|  AMP      Pullback50      $34.69     $503.48  $505.59  +0.4%   $+0.15  |
|                                                                        |
|  Total invested                                                 $103.94|
|  Total open P&L                                                  $+0.32|
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
|  2026-11-18  SELL  ANET  Pullback50  $34.60  P&L $+0.06                |
|  2026-11-18  SELL  ESS  Pullback50  $34.38  P&L $-0.19                 |
|  2026-11-18  SELL  AMCR  Pullback50  $34.50  P&L $-0.20                |
|  2026-11-18  SELL  AES  Pullback50  $34.66  P&L $+0.11                 |
|  2026-11-17  SELL  AES  Pullback50  $34.58  P&L $+0.00                 |
|  2026-11-17  SELL  LOPE  MomReversal  $34.55  P&L $-0.20               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-11-19T09:26:54.403114-05:00 share=25% ===
2026-11-19 09:26:54,403 INFO === options_live_micro LIVE 2026-11-19T09:26:54.403114-05:00 share=25% ===
Live account equity $230.74 cash $126.80 #225458845 options_level=3
2026-11-19 09:26:54,433 INFO Live account equity $230.74 cash $126.80 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-11-19 09:26:54,442 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-11-19 09:26:54,449 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (225 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.74 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T143150Z

- UTC timestamp: `20261119T143150Z`
- GitHub run: [#16174](https://github.com/28twagg-ops/TradingBot/actions/runs/44544400695)
- Run id: `44544400695`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261119T143150Z_live_bot.log`, `logs/action_runs/20261119T143150Z_live_options.log`, `logs/action_runs/20261119T143150Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-19T09:26:56.933342-05:00","date":"2026-11-19","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.1},"signals":0,"placed":0,"equity":988782.44,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"16173","github_run_id":"44543500992","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
14:31:51  INFO      Mode: morning_prep
14:31:51  INFO        [prep_positions] 2/2 (2 valid)
14:31:51  INFO      Fetching tickers (universe=both)...
14:31:51  INFO        S&P 500: 503
14:31:51  INFO        MidCap 400: 400
14:31:51  INFO        Total: 903 tickers
14:31:52  INFO        [prep_universe] 40/901 (40 valid)
14:31:53  INFO        [prep_universe] 80/901 (80 valid)
14:31:54  INFO        [prep_universe] 120/901 (120 valid)
14:31:56  INFO        [prep_universe] 160/901 (160 valid)
14:31:57  INFO        [prep_universe] 200/901 (199 valid)
14:32:06  INFO        [prep_universe] 240/901 (238 valid)
14:32:16  INFO        [prep_universe] 280/901 (278 valid)
14:32:29  INFO        [prep_universe] 320/901 (318 valid)
14:32:42  INFO        [prep_universe] 360/901 (358 valid)
14:32:55  INFO        [prep_universe] 400/901 (398 valid)
14:33:05  INFO        [prep_universe] 440/901 (438 valid)
14:33:18  INFO        [prep_universe] 480/901 (477 valid)
14:33:30  INFO        [prep_universe] 520/901 (517 valid)
14:33:40  INFO        [prep_universe] 560/901 (557 valid)
14:33:53  INFO        [prep_universe] 600/901 (597 valid)
14:34:06  INFO        [prep_universe] 640/901 (637 valid)
14:34:19  INFO        [prep_universe] 680/901 (677 valid)
14:34:29  INFO        [prep_universe] 720/901 (717 valid)
14:34:42  INFO        [prep_universe] 760/901 (757 valid)
14:34:54  INFO        [prep_universe] 800/901 (797 valid)
14:35:04  INFO        [prep_universe] 840/901 (837 valid)
14:35:17  INFO        [prep_universe] 880/901 (876 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261119T143725Z

- UTC timestamp: `20261119T143725Z`
- GitHub run: [#16175](https://github.com/28twagg-ops/TradingBot/actions/runs/44545315470)
- Run id: `44545315470`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261119T143725Z_live_bot.log`, `logs/action_runs/20261119T143725Z_live_options.log`, `logs/action_runs/20261119T143725Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-19T09:26:56.933342-05:00","date":"2026-11-19","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.1},"signals":0,"placed":0,"equity":988782.44,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"16173","github_run_id":"44543500992","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
14:37:26  INFO      Mode: morning_prep
14:37:26  INFO        [prep_positions] 2/2 (2 valid)
14:37:26  INFO      Fetching tickers (universe=both)...
14:37:27  INFO        S&P 500: 503
14:37:27  INFO        MidCap 400: 400
14:37:27  INFO        Total: 903 tickers
14:37:28  INFO        [prep_universe] 40/901 (40 valid)
14:37:29  INFO        [prep_universe] 80/901 (80 valid)
14:37:30  INFO        [prep_universe] 120/901 (120 valid)
14:37:31  INFO        [prep_universe] 160/901 (160 valid)
14:37:32  INFO        [prep_universe] 200/901 (199 valid)
14:37:42  INFO        [prep_universe] 240/901 (238 valid)
14:37:52  INFO        [prep_universe] 280/901 (278 valid)
14:38:05  INFO        [prep_universe] 320/901 (318 valid)
14:38:18  INFO        [prep_universe] 360/901 (358 valid)
14:38:28  INFO        [prep_universe] 400/901 (398 valid)
14:38:41  INFO        [prep_universe] 440/901 (438 valid)
14:38:54  INFO        [prep_universe] 480/901 (477 valid)
14:39:04  INFO        [prep_universe] 520/901 (517 valid)
14:39:16  INFO        [prep_universe] 560/901 (557 valid)
14:39:29  INFO        [prep_universe] 600/901 (597 valid)
14:39:42  INFO        [prep_universe] 640/901 (637 valid)
14:39:52  INFO        [prep_universe] 680/901 (677 valid)
14:40:05  INFO        [prep_universe] 720/901 (717 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261119T144240Z

- UTC timestamp: `20261119T144240Z`
- GitHub run: [#16176](https://github.com/28twagg-ops/TradingBot/actions/runs/44546228568)
- Run id: `44546228568`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`49s`
- Full logs: `logs/action_runs/20261119T144240Z_live_bot.log`, `logs/action_runs/20261119T144240Z_live_options.log`, `logs/action_runs/20261119T144240Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-19T09:42:44.691493-05:00","date":"2026-11-19","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":38.4,"phases_s":{"reconcile":0.32,"cancel":0.1,"manage":5.76,"protective_stops":0.35,"scan":29.72,"entries":0.95,"reconcile2":0.31},"signals":65,"placed":1,"equity":988179.39,"open_positions":5,"pending_orders":1,"open_lots":5,"submitted_today":1,"filled_today":0,"unattributed_contracts":0,"top_signals":["S430:NVDA","S210:TSLA","S430:AMD","S430:SMCI","S430:PLTR","S430:CRWD","S430:SNOW","S430:AVGO"],"github_run":"16176","github_run_id":"44546228568","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
14:42:40  INFO      Mode: morning_prep
14:42:41  INFO        Prep cache reused; skipped full universe scan

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         14:42 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $229.21|
+========================================================================+

+========================================================================+
|                              MORNING PREP                              |
+========================================================================+
|  Goal                   Precompute exits/signals for next execution run|
|  Plan file                                 logs/plans/morning_plan.json|
|  Regime                                                            BULL|
+========================================================================+

+========================================================================+
|                               PREP CACHE                               |
+========================================================================+
|  Using cached plan                                   yes (fresh (7.3m))|
|  Exit candidates                                                      1|
|  Signal candidates                                                   23|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-11-19T09:42:42.026233-05:00 share=25% ===
2026-11-19 09:42:42,026 INFO === options_live_micro LIVE 2026-11-19T09:42:42.026233-05:00 share=25% ===
Live account equity $229.21 cash $170.02 #225458845 options_level=3
2026-11-19 09:42:42,176 INFO Live account equity $229.21 cash $170.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-11-19 09:42:42,295 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-11-19 09:42:42,374 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (244 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.74 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T144640Z

- UTC timestamp: `20261119T144640Z`
- GitHub run: [#16177](https://github.com/28twagg-ops/TradingBot/actions/runs/44547131239)
- Run id: `44547131239`
- Live bot: exit=`0`, duration=`25s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`39s`
- Full logs: `logs/action_runs/20261119T144640Z_live_bot.log`, `logs/action_runs/20261119T144640Z_live_options.log`, `logs/action_runs/20261119T144640Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-19T09:47:08.943250-05:00","date":"2026-11-19","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":29.7,"phases_s":{"reconcile":0.1,"cancel":0.04,"manage":0.35,"protective_stops":0.1,"scan":28.27,"entries":0.26,"reconcile2":0.09},"signals":65,"placed":0,"equity":988018.85,"open_positions":5,"pending_orders":1,"open_lots":5,"submitted_today":1,"filled_today":0,"unattributed_contracts":0,"top_signals":["S430:NVDA","S210:TSLA","S430:AMD","S430:SMCI","S430:PLTR","S430:CRWD","S430:SNOW","S430:AVGO"],"github_run":"16177","github_run_id":"44547131239","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
... (113 earlier lines - see full log file)
|  AVTR     Pullback50      eq     $15.62   43.5   -1.46   50MA bounce (-|
|  DBX      Pullback50      eq     $34.84   41.8   -0.96   50MA bounce (-|
|  EAT      Pullback50      eq     $200.00  41.4   -1.89   50MA bounce (-|
|  EQH      Pullback50      eq     $53.81   49.8   -2.07   50MA bounce (+|
|  KRYS     Pullback50      eq     $321.58  44.9   -1.15   50MA bounce (-|
|  MSA      Pullback50      eq     $178.72  50.1   -1.84   50MA bounce (-|
|  PNFP     Pullback50      eq     $98.32   41.7   -2.59   50MA bounce (+|
|  RGEN     Pullback50      eq     $176.66  49.8   -1.30   50MA bounce (-|
|  VNO      Pullback50      eq     $34.35   48.7   -1.65   50MA bounce (-|
|                                                                        |14:46:44  INFO        BUY  APA  $34.38  [Pullback50]  id=6b2b055a-384b-4eca-9f9f-2ae9fc94a79b
14:46:44  INFO        BUY  CNC  $34.38  [Pullback50]  id=77d332ab-7ae9-4dc0-b11a-1dff1f389567
14:47:05  INFO        place_all_stops: checking 3 positions...
14:47:05  INFO        STOP skipped AMP: fractional (0.0686 shares) — software exit will handle it
14:47:05  INFO        STOP skipped APA: fractional (0.7481 shares) — software exit will handle it
14:47:05  INFO        STOP skipped CNC: fractional (0.5182 shares) — software exit will handle it
14:47:05  INFO        Daily log -> logs/daily/2026-11-19.md
14:47:05  INFO        Dashboard written → logs/dashboard.md

+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] APA  Pullback50                                    $34.38|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] CNC  Pullback50                                    $34.38|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] ESS  Pullback50                                      cap 3|
|    SKIP [eq] FITB  Pullback50                                     cap 3|
|    SKIP [eq] FOXA  Pullback50                                     cap 3|
|    SKIP [eq] GDDY  Pullback50                                     cap 3|
|    SKIP [eq] MSFT  Pullback50                                     cap 3|
|    SKIP [eq] MCO  Pullback50                                      cap 3|
|    SKIP [eq] NTRS  Pullback50                                     cap 3|
|    SKIP [eq] PANW  Pullback50                                     cap 3|
|    SKIP [eq] SOLV  Pullback50                                     cap 3|
|    SKIP [eq] SNPS  Pullback50                                     cap 3|
|    SKIP [eq] TEL  Pullback50                                      cap 3|
|    SKIP [eq] WSM  Pullback50                                      cap 3|
|    SKIP [eq] AVTR  Pullback50                                     cap 3|
|    SKIP [eq] DBX  Pullback50                                      cap 3|
|    SKIP [eq] EAT  Pullback50                                      cap 3|
|    SKIP [eq] EQH  Pullback50                                      cap 3|
|    SKIP [eq] KRYS  Pullback50                                     cap 3|
|    SKIP [eq] MSA  Pullback50                                      cap 3|
|    SKIP [eq] PNFP  Pullback50                                     cap 3|
|    SKIP [eq] RGEN  Pullback50                                     cap 3|
|    SKIP [eq] VNO  Pullback50                                      cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      2|
+------------------------------------------------------------------------+
|  APA                                                  still unconfirmed|
|  CNC                                                  still unconfirmed|
+========================================================================+
+========================================================================+

+========================================================================+
|                           GTC STOP PLACEMENT                           |
+========================================================================+
|  Waiting 5s for 2 buy submit(s) to settle...                           |
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |
+========================================================================+
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Stra~  RubberBand + MomReversal (display only — schedule not enforced)|
|  Scanned                                                              0|
|  Signals                                                             23|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  2 unconfirmed|
|  Exits                                                                1|
|  Open pos                                                             3|
|  Equity                                                         $229.10|
|  Cash                                                           $125.89|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-11-19T09:47:06.520045-05:00 share=25% ===
2026-11-19 09:47:06,520 INFO === options_live_micro LIVE 2026-11-19T09:47:06.520045-05:00 share=25% ===
Live account equity $229.10 cash $125.89 #225458845 options_level=3
2026-11-19 09:47:06,573 INFO Live account equity $229.10 cash $125.89 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-11-19 09:47:06,714 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-11-19 09:47:06,734 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (244 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=229.1 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T145151Z

- UTC timestamp: `20261119T145151Z`
- GitHub run: [#16178](https://github.com/28twagg-ops/TradingBot/actions/runs/44548037607)
- Run id: `44548037607`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`53s`
- Full logs: `logs/action_runs/20261119T145151Z_live_bot.log`, `logs/action_runs/20261119T145151Z_live_options.log`, `logs/action_runs/20261119T145151Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-19T09:51:57.906413-05:00","date":"2026-11-19","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":41.1,"phases_s":{"reconcile":0.17,"cancel":0.05,"manage":0.44,"protective_stops":0.15,"scan":38.98,"entries":0.38,"reconcile2":0.2},"signals":65,"placed":0,"equity":988195.17,"open_positions":5,"pending_orders":1,"open_lots":5,"submitted_today":1,"filled_today":0,"unattributed_contracts":0,"top_signals":["S430:NVDA","S210:TSLA","S430:AMD","S430:SMCI","S430:PLTR","S430:CRWD","S430:SNOW","S430:AVGO"],"github_run":"16178","github_run_id":"44548037607","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
14:51:51  INFO      Mode: morning_scan
14:51:52  INFO      Morning scan already completed today (2026-11-19T14:47:05.852226Z) — exits-only pass
14:51:52  INFO        Daily log -> logs/daily/2026-11-19.md
14:51:52  INFO        Daily log reconciled -> logs/daily/2026-11-19.md (1 ledger rows)
14:51:52  INFO        place_all_stops: checking 3 positions...
14:51:52  INFO        STOP skipped AMP: fractional (0.0686 shares) — software exit will handle it
14:51:52  INFO        STOP skipped APA: fractional (0.7481 shares) — software exit will handle it
14:51:52  INFO        STOP skipped CNC: fractional (0.5182 shares) — software exit will handle it
14:51:52  INFO        [positions] 3/3 (3 valid)
14:51:52  INFO        SELL MARKET [urgent] CNC closed
14:51:54  INFO        TX logged: SELL CNC  P&L -1.15%
14:51:54  INFO        Daily log -> logs/daily/2026-11-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         14:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $228.86|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CNC  P&L -1.2%  $-0.40                         EXIT: stop_loss (-1.2%)|
|  APA  P&L -0.1%  $-0.04                                            HOLD|
|  AMP  P&L +0.3%  $+0.12                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  1 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
|  Logged exits                                                         1|
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
|  CNC                                         -1.15%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-11-19T09:51:55.428727-05:00 share=25% ===
2026-11-19 09:51:55,428 INFO === options_live_micro LIVE 2026-11-19T09:51:55.428727-05:00 share=25% ===
Live account equity $228.81 cash $159.82 #225458845 options_level=3
2026-11-19 09:51:55,502 INFO Live account equity $228.81 cash $159.82 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-11-19 09:51:55,568 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-11-19 09:51:55,612 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (244 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=228.81 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T145650Z

- UTC timestamp: `20261119T145650Z`
- GitHub run: [#16179](https://github.com/28twagg-ops/TradingBot/actions/runs/44548933993)
- Run id: `44548933993`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`63s`
- Full logs: `logs/action_runs/20261119T145650Z_live_bot.log`, `logs/action_runs/20261119T145650Z_live_options.log`, `logs/action_runs/20261119T145650Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-19T09:56:59.008433-05:00","date":"2026-11-19","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":49.2,"phases_s":{"reconcile":0.41,"cancel":0.19,"manage":1.02,"protective_stops":0.43,"scan":44.67,"entries":0.88,"reconcile2":0.46},"signals":65,"placed":0,"equity":988550.86,"open_positions":5,"pending_orders":1,"open_lots":5,"submitted_today":1,"filled_today":0,"unattributed_contracts":0,"top_signals":["S430:NVDA","S210:TSLA","S430:AMD","S430:SMCI","S430:PLTR","S430:CRWD","S430:SNOW","S430:AVGO"],"github_run":"16179","github_run_id":"44548933993","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
14:56:51  INFO      Mode: morning_scan
14:56:51  INFO      Morning scan already completed today (2026-11-19T14:47:05.852226Z) — exits-only pass
14:56:51  INFO        Daily log -> logs/daily/2026-11-19.md
14:56:51  INFO        Daily log reconciled -> logs/daily/2026-11-19.md (2 ledger rows)
14:56:51  INFO        place_all_stops: checking 2 positions...
14:56:51  INFO        STOP skipped AMP: fractional (0.0686 shares) — software exit will handle it
14:56:51  INFO        STOP skipped APA: fractional (0.7481 shares) — software exit will handle it
14:56:52  INFO        [positions] 2/2 (2 valid)
14:56:52  INFO        SELL MARKET [urgent] APA closed
14:56:54  INFO        TX logged: SELL APA  P&L -0.53%
14:56:54  INFO        Daily log -> logs/daily/2026-11-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         14:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $228.58|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APA  P&L -0.5%  $-0.18                         EXIT: stop_loss (-0.5%)|
|  AMP  P&L +0.1%  $+0.04                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  1 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
|  Logged exits                                                         1|
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
|  APA                                         -0.53%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-11-19T09:56:55.734099-05:00 share=25% ===
2026-11-19 09:56:55,734 INFO === options_live_micro LIVE 2026-11-19T09:56:55.734099-05:00 share=25% ===
Live account equity $228.59 cash $194.01 #225458845 options_level=3
2026-11-19 09:56:55,910 INFO Live account equity $228.59 cash $194.01 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-11-19 09:56:56,063 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-11-19 09:56:56,167 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (244 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=228.59 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T150155Z

- UTC timestamp: `20261119T150155Z`
- GitHub run: [#16180](https://github.com/28twagg-ops/TradingBot/actions/runs/44549838872)
- Run id: `44549838872`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`55s`
- Full logs: `logs/action_runs/20261119T150155Z_live_bot.log`, `logs/action_runs/20261119T150155Z_live_options.log`, `logs/action_runs/20261119T150155Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-19T10:02:00.663930-05:00","date":"2026-11-19","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":42.7,"phases_s":{"reconcile":0.23,"cancel":0.05,"manage":0.7,"protective_stops":0.17,"scan":40.27,"entries":0.39,"reconcile2":0.17},"signals":65,"placed":0,"equity":988360.99,"open_positions":5,"pending_orders":1,"open_lots":5,"submitted_today":1,"filled_today":0,"unattributed_contracts":0,"top_signals":["S430:NVDA","S210:TSLA","S430:AMD","S430:SMCI","S430:PLTR","S430:CRWD","S430:SNOW","S430:AVGO"],"github_run":"16180","github_run_id":"44549838872","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
15:01:56  INFO      Mode: exits
15:01:56  INFO        Daily log -> logs/daily/2026-11-19.md
15:01:56  INFO        Daily log reconciled -> logs/daily/2026-11-19.md (3 ledger rows)
15:01:56  INFO        place_all_stops: checking 1 positions...
15:01:56  INFO        STOP skipped AMP: fractional (0.0686 shares) — software exit will handle it
15:01:56  INFO        [positions] 1/1 (1 valid)
15:01:57  INFO        Daily log -> logs/daily/2026-11-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $228.54|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMP  P&L -0.0%  $-0.01                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-11-19T10:01:57.883905-05:00 share=25% ===
2026-11-19 10:01:57,883 INFO === options_live_micro LIVE 2026-11-19T10:01:57.883905-05:00 share=25% ===
Live account equity $228.54 cash $194.01 #225458845 options_level=3
2026-11-19 10:01:57,961 INFO Live account equity $228.54 cash $194.01 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-11-19 10:01:58,031 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-11-19 10:01:58,075 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (244 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=228.54 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T150653Z

- UTC timestamp: `20261119T150653Z`
- GitHub run: [#16181](https://github.com/28twagg-ops/TradingBot/actions/runs/44550775716)
- Run id: `44550775716`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`48s`
- Full logs: `logs/action_runs/20261119T150653Z_live_bot.log`, `logs/action_runs/20261119T150653Z_live_options.log`, `logs/action_runs/20261119T150653Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-19T10:06:59.189969-05:00","date":"2026-11-19","mode":"entry+manage","header":"entry+manage (3 new)","elapsed_s":37.4,"phases_s":{"reconcile":0.28,"cancel":0.09,"manage":0.86,"protective_stops":0.29,"scan":28.91,"entries":5.54,"reconcile2":0.29},"signals":65,"placed":3,"equity":988231.36,"open_positions":8,"pending_orders":1,"open_lots":8,"submitted_today":4,"filled_today":3,"unattributed_contracts":0,"top_signals":["S430:NVDA","S210:TSLA","S430:AMD","S430:SMCI","S430:PLTR","S430:CRWD","S430:SNOW","S430:AVGO"],"github_run":"16181","github_run_id":"44550775716","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
15:06:54  INFO      Mode: exits
15:06:55  INFO        Daily log -> logs/daily/2026-11-19.md
15:06:55  INFO        Daily log reconciled -> logs/daily/2026-11-19.md (3 ledger rows)
15:06:55  INFO        place_all_stops: checking 1 positions...
15:06:55  INFO        STOP skipped AMP: fractional (0.0686 shares) — software exit will handle it
15:06:55  INFO        [positions] 1/1 (1 valid)
15:06:55  INFO        Daily log -> logs/daily/2026-11-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $228.57|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMP  P&L +0.1%  $+0.02                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-11-19T10:06:56.507575-05:00 share=25% ===
2026-11-19 10:06:56,507 INFO === options_live_micro LIVE 2026-11-19T10:06:56.507575-05:00 share=25% ===
Live account equity $228.61 cash $194.01 #225458845 options_level=3
2026-11-19 10:06:56,666 INFO Live account equity $228.61 cash $194.01 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-11-19 10:06:56,799 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-11-19 10:06:56,887 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (248 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     8 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=228.57 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T151159Z

- UTC timestamp: `20261119T151159Z`
- GitHub run: [#16182](https://github.com/28twagg-ops/TradingBot/actions/runs/44551712737)
- Run id: `44551712737`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`47s`
- Full logs: `logs/action_runs/20261119T151159Z_live_bot.log`, `logs/action_runs/20261119T151159Z_live_options.log`, `logs/action_runs/20261119T151159Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-19T10:12:05.207348-05:00","date":"2026-11-19","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":37.9,"phases_s":{"reconcile":0.45,"cancel":0.15,"manage":3.01,"protective_stops":0.66,"scan":24.99,"entries":6.97,"reconcile2":0.45},"signals":65,"placed":0,"equity":988467.27,"open_positions":8,"pending_orders":1,"open_lots":8,"submitted_today":4,"filled_today":3,"unattributed_contracts":0,"top_signals":["S430:NVDA","S210:TSLA","S430:AMD","S430:SMCI","S430:PLTR","S430:CRWD","S430:SNOW","S430:AVGO"],"github_run":"16182","github_run_id":"44551712737","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
15:12:00  INFO      Mode: exits
15:12:01  INFO        Daily log -> logs/daily/2026-11-19.md
15:12:01  INFO        Daily log reconciled -> logs/daily/2026-11-19.md (3 ledger rows)
15:12:01  INFO        place_all_stops: checking 1 positions...
15:12:01  INFO        STOP skipped AMP: fractional (0.0686 shares) — software exit will handle it
15:12:01  INFO        [positions] 1/1 (1 valid)
15:12:01  INFO        Daily log -> logs/daily/2026-11-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:12 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $228.57|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMP  P&L +0.1%  $+0.02                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-11-19T10:12:02.416925-05:00 share=25% ===
2026-11-19 10:12:02,416 INFO === options_live_micro LIVE 2026-11-19T10:12:02.416925-05:00 share=25% ===
Live account equity $228.57 cash $194.01 #225458845 options_level=3
2026-11-19 10:12:02,629 INFO Live account equity $228.57 cash $194.01 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-11-19 10:12:02,839 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-11-19 10:12:02,979 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (247 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     8 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=228.57 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T151643Z

- UTC timestamp: `20261119T151643Z`
- GitHub run: [#16183](https://github.com/28twagg-ops/TradingBot/actions/runs/44552648866)
- Run id: `44552648866`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`43s`
- Full logs: `logs/action_runs/20261119T151643Z_live_bot.log`, `logs/action_runs/20261119T151643Z_live_options.log`, `logs/action_runs/20261119T151643Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-19T10:16:47.442854-05:00","date":"2026-11-19","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":32.4,"phases_s":{"reconcile":0.1,"cancel":0.03,"manage":1.27,"protective_stops":0.12,"scan":28.43,"entries":1.81,"reconcile2":0.13},"signals":65,"placed":0,"equity":988624.27,"open_positions":8,"pending_orders":1,"open_lots":8,"submitted_today":4,"filled_today":3,"unattributed_contracts":0,"top_signals":["S430:NVDA","S210:TSLA","S430:AMD","S430:SMCI","S430:PLTR","S430:CRWD","S430:SNOW","S430:AVGO"],"github_run":"16183","github_run_id":"44552648866","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
15:16:44  INFO      Mode: exits
15:16:44  INFO        Daily log -> logs/daily/2026-11-19.md
15:16:44  INFO        Daily log reconciled -> logs/daily/2026-11-19.md (3 ledger rows)
15:16:44  INFO        place_all_stops: checking 1 positions...
15:16:44  INFO        STOP skipped AMP: fractional (0.0686 shares) — software exit will handle it
15:16:44  INFO        [positions] 1/1 (1 valid)
15:16:44  INFO        Daily log -> logs/daily/2026-11-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $228.54|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMP  P&L -0.0%  $-0.01                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-11-19T10:16:45.247867-05:00 share=25% ===
2026-11-19 10:16:45,247 INFO === options_live_micro LIVE 2026-11-19T10:16:45.247867-05:00 share=25% ===
Live account equity $228.54 cash $194.01 #225458845 options_level=3
2026-11-19 10:16:45,453 INFO Live account equity $228.54 cash $194.01 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-11-19 10:16:45,486 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-11-19 10:16:45,508 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (247 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     8 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=228.54 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T152145Z

- UTC timestamp: `20261119T152145Z`
- GitHub run: [#16184](https://github.com/28twagg-ops/TradingBot/actions/runs/44553594017)
- Run id: `44553594017`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`43s`
- Full logs: `logs/action_runs/20261119T152145Z_live_bot.log`, `logs/action_runs/20261119T152145Z_live_options.log`, `logs/action_runs/20261119T152145Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-19T10:21:49.987543-05:00","date":"2026-11-19","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":32.3,"phases_s":{"reconcile":0.12,"cancel":0.04,"manage":1.35,"protective_stops":0.12,"scan":28.2,"entries":1.84,"reconcile2":0.1},"signals":65,"placed":0,"equity":988626.12,"open_positions":8,"pending_orders":1,"open_lots":8,"submitted_today":4,"filled_today":3,"unattributed_contracts":0,"top_signals":["S430:NVDA","S210:TSLA","S430:AMD","S430:SMCI","S430:PLTR","S430:CRWD","S430:SNOW","S430:AVGO"],"github_run":"16184","github_run_id":"44553594017","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
15:21:46  INFO      Mode: exits
15:21:46  INFO        Daily log -> logs/daily/2026-11-19.md
15:21:46  INFO        Daily log reconciled -> logs/daily/2026-11-19.md (3 ledger rows)
15:21:46  INFO        place_all_stops: checking 1 positions...
15:21:46  INFO        STOP skipped AMP: fractional (0.0686 shares) — software exit will handle it
15:21:46  INFO        [positions] 1/1 (1 valid)
15:21:47  INFO        Daily log -> logs/daily/2026-11-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:21 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $228.39|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMP  P&L -0.5%  $-0.16                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-11-19T10:21:47.679240-05:00 share=25% ===
2026-11-19 10:21:47,679 INFO === options_live_micro LIVE 2026-11-19T10:21:47.679240-05:00 share=25% ===
Live account equity $228.39 cash $194.01 #225458845 options_level=3
2026-11-19 10:21:47,726 INFO Live account equity $228.39 cash $194.01 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-11-19 10:21:47,758 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-11-19 10:21:47,780 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (247 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     8 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=228.39 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T152646Z

- UTC timestamp: `20261119T152646Z`
- GitHub run: [#16185](https://github.com/28twagg-ops/TradingBot/actions/runs/44554535905)
- Run id: `44554535905`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`43s`
- Full logs: `logs/action_runs/20261119T152646Z_live_bot.log`, `logs/action_runs/20261119T152646Z_live_options.log`, `logs/action_runs/20261119T152646Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-19T10:26:50.253636-05:00","date":"2026-11-19","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":33.0,"phases_s":{"reconcile":0.09,"cancel":0.03,"manage":1.37,"protective_stops":0.22,"scan":28.49,"entries":1.76,"reconcile2":0.24},"signals":65,"placed":0,"equity":988731.77,"open_positions":8,"pending_orders":1,"open_lots":8,"submitted_today":4,"filled_today":3,"unattributed_contracts":0,"top_signals":["S430:NVDA","S210:TSLA","S430:AMD","S430:SMCI","S430:PLTR","S430:CRWD","S430:SNOW","S430:AVGO"],"github_run":"16185","github_run_id":"44554535905","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
15:26:47  INFO      Mode: exits
15:26:47  INFO        Daily log -> logs/daily/2026-11-19.md
15:26:47  INFO        Daily log reconciled -> logs/daily/2026-11-19.md (3 ledger rows)
15:26:47  INFO        place_all_stops: checking 1 positions...
15:26:47  INFO        STOP skipped AMP: fractional (0.0686 shares) — software exit will handle it
15:26:47  INFO        [positions] 1/1 (1 valid)
15:26:47  INFO        Daily log -> logs/daily/2026-11-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:26 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $228.39|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMP  P&L -0.5%  $-0.16                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-11-19T10:26:48.258845-05:00 share=25% ===
2026-11-19 10:26:48,258 INFO === options_live_micro LIVE 2026-11-19T10:26:48.258845-05:00 share=25% ===
Live account equity $228.39 cash $194.01 #225458845 options_level=3
2026-11-19 10:26:48,304 INFO Live account equity $228.39 cash $194.01 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-11-19 10:26:48,335 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-11-19 10:26:48,355 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (247 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     8 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=228.39 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261119T153200Z

- UTC timestamp: `20261119T153200Z`
- GitHub run: [#16186](https://github.com/28twagg-ops/TradingBot/actions/runs/44555466769)
- Run id: `44555466769`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`48s`
- Full logs: `logs/action_runs/20261119T153200Z_live_bot.log`, `logs/action_runs/20261119T153200Z_live_options.log`, `logs/action_runs/20261119T153200Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1885 | 48.7 | -25.0 | +35.4 | $+21,164 |
| TAINTED | 2150 | 30.2 | -42.9 | +6.7 | $-14,316 |
| KEEP-only | 949 | 60.3 | +51.6 | +50.7 | $+15,094 |
| KEEP-only recent | 764 | 59.3 | +53.0 | +55.7 | $+11,585 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-19T10:32:06.905920-05:00","date":"2026-11-19","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":38.1,"phases_s":{"reconcile":0.53,"cancel":0.19,"manage":3.1,"protective_stops":0.65,"scan":24.98,"entries":6.88,"reconcile2":0.5},"signals":65,"placed":0,"equity":988905.96,"open_positions":8,"pending_orders":1,"open_lots":8,"submitted_today":4,"filled_today":3,"unattributed_contracts":0,"top_signals":["S430:NVDA","S210:TSLA","S430:AMD","S430:SMCI","S430:PLTR","S430:CRWD","S430:SNOW","S430:AVGO"],"github_run":"16186","github_run_id":"44555466769","status":"ok","data_quality":{"clean":{"n":1885,"win":48.7,"med":-25.0,"avg":35.43,"pnl":21163.83},"tainted":{"n":2150,"win":30.23,"med":-42.86,"avg":6.71,"pnl":-14316.28},"keep_only":{"n":949,"win":60.27,"med":51.56,"avg":50.71,"pnl":15094.45},"keep_only_recent":{"n":764,"win":59.29,"med":53.0,"avg":55.68,"pnl":11585.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
15:32:01  INFO      Mode: exits
15:32:02  INFO        Daily log -> logs/daily/2026-11-19.md
15:32:02  INFO        Daily log reconciled -> logs/daily/2026-11-19.md (3 ledger rows)
15:32:02  INFO        place_all_stops: checking 1 positions...
15:32:02  INFO        STOP skipped AMP: fractional (0.0686 shares) — software exit will handle it
15:32:02  INFO        [positions] 1/1 (1 valid)
15:32:03  INFO        Daily log -> logs/daily/2026-11-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:32 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $228.39|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMP  P&L -0.5%  $-0.16                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-11-19T10:32:04.044936-05:00 share=25% ===
2026-11-19 10:32:04,044 INFO === options_live_micro LIVE 2026-11-19T10:32:04.044936-05:00 share=25% ===
Live account equity $228.39 cash $194.01 #225458845 options_level=3
2026-11-19 10:32:04,262 INFO Live account equity $228.39 cash $194.01 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-11-19 10:32:04,470 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-11-19 10:32:04,609 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (247 earlier lines - see full log file)
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
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     8 | INFO |
| Total closed lots           |  3145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1885 med=-25.0% | TAINTED n=2150 med=-42.9% | KEEP-only n=949 med=+51.6% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=228.39 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
