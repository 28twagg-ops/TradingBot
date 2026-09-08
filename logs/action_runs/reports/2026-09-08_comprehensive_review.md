# Daily Comprehensive Action Review - 2026-09-08

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260908T130103Z

- UTC timestamp: `20260908T130103Z`
- GitHub run: [#9316](https://github.com/28twagg-ops/TradingBot/actions/runs/34229308033)
- Run id: `34229308033`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260908T130103Z_live_bot.log`, `logs/action_runs/20260908T130103Z_live_options.log`, `logs/action_runs/20260908T130103Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1029 | 50.1 | +12.5 | +47.6 | $+15,692 |
| TAINTED | 1791 | 33.5 | -38.4 | +12.7 | $-8,651 |
| KEEP-only | 551 | 64.2 | +51.4 | +73.6 | $+10,279 |
| KEEP-only recent | 343 | 61.2 | +53.6 | +90.2 | $+5,022 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T09:01:08.470978-04:00","date":"2026-09-08","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.32},"signals":0,"placed":0,"equity":1004770.25,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9316","github_run_id":"34229308033","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:01:04  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.39|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.39|
|  Cash                                                           $126.02|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $104.37|
|  Open P&L                                                        $+0.66|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     unknown         $34.65     $255.49  $256.01  +0.2%   $+0.07  |
|  FLEX     unknown         $35.01     $109.37  $110.76  +1.3%   $+0.44  |
|  LII      unknown         $34.71     $386.29  $388.01  +0.4%   $+0.15  |
|                                                                        |
|  Total invested                                                 $104.37|
|  Total open P&L                                                  $+0.66|
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
|  2026-09-04  SELL  APD  Pullback50  $34.37  P&L $-0.21                 |
|  2026-09-03  SELL  ACGL  Pullback50  $34.56  P&L $-0.00                |
|  2026-09-03  SELL  CNM  MomReversal  $34.27  P&L $-0.24                |
|  2026-09-03  SELL  ACGL  Pullback50  $34.60  P&L $+0.00                |
|  2026-09-03  SELL  AES  Pullback50  $34.50  P&L $+0.00                 |
|  2026-09-02  SELL  MO  Pullback50  $34.52  P&L $+0.00                  |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-08T09:01:05.610150-04:00 share=25% ===
2026-09-08 09:01:05,610 INFO === options_live_micro LIVE 2026-09-08T09:01:05.610150-04:00 share=25% ===
Live account equity $230.39 cash $126.02 #225458845 options_level=3
2026-09-08 09:01:05,652 INFO Live account equity $230.39 cash $126.02 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-08 09:01:05,662 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-08 09:01:05,670 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (162 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1052 | WARN | <<<
| Missing exit records (post) |  1050 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1029 med=+12.5% | TAINTED n=1791 med=-38.4% | KEEP-only n=551 med=+51.4% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.39 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260908T130606Z

- UTC timestamp: `20260908T130606Z`
- GitHub run: [#9317](https://github.com/28twagg-ops/TradingBot/actions/runs/34229800731)
- Run id: `34229800731`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260908T130606Z_live_bot.log`, `logs/action_runs/20260908T130606Z_live_options.log`, `logs/action_runs/20260908T130606Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1029 | 50.1 | +12.5 | +47.6 | $+15,692 |
| TAINTED | 1791 | 33.5 | -38.4 | +12.7 | $-8,651 |
| KEEP-only | 551 | 64.2 | +51.4 | +73.6 | $+10,279 |
| KEEP-only recent | 343 | 61.2 | +53.6 | +90.2 | $+5,022 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T09:06:11.280990-04:00","date":"2026-09-08","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.13},"signals":0,"placed":0,"equity":1004783.47,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9317","github_run_id":"34229800731","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:06:07  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.43|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.43|
|  Cash                                                           $126.02|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $104.41|
|  Open P&L                                                        $+0.70|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     unknown         $34.68     $255.49  $256.24  +0.3%   $+0.10  |
|  FLEX     unknown         $35.01     $109.37  $110.76  +1.3%   $+0.44  |
|  LII      unknown         $34.71     $386.29  $388.01  +0.4%   $+0.15  |
|                                                                        |
|  Total invested                                                 $104.41|
|  Total open P&L                                                  $+0.70|
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
|  2026-09-04  SELL  APD  Pullback50  $34.37  P&L $-0.21                 |
|  2026-09-03  SELL  ACGL  Pullback50  $34.56  P&L $-0.00                |
|  2026-09-03  SELL  CNM  MomReversal  $34.27  P&L $-0.24                |
|  2026-09-03  SELL  ACGL  Pullback50  $34.60  P&L $+0.00                |
|  2026-09-03  SELL  AES  Pullback50  $34.50  P&L $+0.00                 |
|  2026-09-02  SELL  MO  Pullback50  $34.52  P&L $+0.00                  |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-08T09:06:08.564297-04:00 share=25% ===
2026-09-08 09:06:08,564 INFO === options_live_micro LIVE 2026-09-08T09:06:08.564297-04:00 share=25% ===
Live account equity $230.43 cash $126.02 #225458845 options_level=3
2026-09-08 09:06:08,622 INFO Live account equity $230.43 cash $126.02 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-08 09:06:08,636 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-08 09:06:08,672 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (162 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1052 | WARN | <<<
| Missing exit records (post) |  1050 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1029 med=+12.5% | TAINTED n=1791 med=-38.4% | KEEP-only n=551 med=+51.4% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.43 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260908T131107Z

- UTC timestamp: `20260908T131107Z`
- GitHub run: [#9318](https://github.com/28twagg-ops/TradingBot/actions/runs/34230306819)
- Run id: `34230306819`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260908T131107Z_live_bot.log`, `logs/action_runs/20260908T131107Z_live_options.log`, `logs/action_runs/20260908T131107Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1029 | 50.1 | +12.5 | +47.6 | $+15,692 |
| TAINTED | 1791 | 33.5 | -38.4 | +12.7 | $-8,651 |
| KEEP-only | 551 | 64.2 | +51.4 | +73.6 | $+10,279 |
| KEEP-only recent | 343 | 61.2 | +53.6 | +90.2 | $+5,022 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T09:11:14.852309-04:00","date":"2026-09-08","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.57},"signals":0,"placed":0,"equity":1004814.5,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9318","github_run_id":"34230306819","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:11:09  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.54|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.54|
|  Cash                                                           $126.02|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $104.52|
|  Open P&L                                                        $+0.81|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     unknown         $34.74     $255.49  $256.70  +0.5%   $+0.16  |
|  FLEX     unknown         $35.07     $109.37  $110.94  +1.4%   $+0.50  |
|  LII      unknown         $34.71     $386.29  $388.01  +0.4%   $+0.15  |
|                                                                        |
|  Total invested                                                 $104.52|
|  Total open P&L                                                  $+0.81|
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
|  2026-09-04  SELL  APD  Pullback50  $34.37  P&L $-0.21                 |
|  2026-09-03  SELL  ACGL  Pullback50  $34.56  P&L $-0.00                |
|  2026-09-03  SELL  CNM  MomReversal  $34.27  P&L $-0.24                |
|  2026-09-03  SELL  ACGL  Pullback50  $34.60  P&L $+0.00                |
|  2026-09-03  SELL  AES  Pullback50  $34.50  P&L $+0.00                 |
|  2026-09-02  SELL  MO  Pullback50  $34.52  P&L $+0.00                  |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-08T09:11:11.312148-04:00 share=25% ===
2026-09-08 09:11:11,312 INFO === options_live_micro LIVE 2026-09-08T09:11:11.312148-04:00 share=25% ===
Live account equity $230.54 cash $126.02 #225458845 options_level=3
2026-09-08 09:11:11,540 INFO Live account equity $230.54 cash $126.02 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-08 09:11:11,610 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-08 09:11:11,678 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (162 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1052 | WARN | <<<
| Missing exit records (post) |  1050 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1029 med=+12.5% | TAINTED n=1791 med=-38.4% | KEEP-only n=551 med=+51.4% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.54 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260908T131600Z

- UTC timestamp: `20260908T131600Z`
- GitHub run: [#9319](https://github.com/28twagg-ops/TradingBot/actions/runs/34230809153)
- Run id: `34230809153`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260908T131600Z_live_bot.log`, `logs/action_runs/20260908T131600Z_live_options.log`, `logs/action_runs/20260908T131600Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1029 | 50.1 | +12.5 | +47.6 | $+15,692 |
| TAINTED | 1791 | 33.5 | -38.4 | +12.7 | $-8,651 |
| KEEP-only | 551 | 64.2 | +51.4 | +73.6 | $+10,279 |
| KEEP-only recent | 343 | 61.2 | +53.6 | +90.2 | $+5,022 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T09:16:06.356202-04:00","date":"2026-09-08","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.48},"signals":0,"placed":0,"equity":1004816.25,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9319","github_run_id":"34230809153","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:16:01  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.55|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.55|
|  Cash                                                           $126.02|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $104.53|
|  Open P&L                                                        $+0.82|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     unknown         $34.75     $255.49  $256.77  +0.5%   $+0.17  |
|  FLEX     unknown         $35.07     $109.37  $110.94  +1.4%   $+0.50  |
|  LII      unknown         $34.71     $386.29  $388.01  +0.4%   $+0.15  |
|                                                                        |
|  Total invested                                                 $104.53|
|  Total open P&L                                                  $+0.82|
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
|  2026-09-04  SELL  APD  Pullback50  $34.37  P&L $-0.21                 |
|  2026-09-03  SELL  ACGL  Pullback50  $34.56  P&L $-0.00                |
|  2026-09-03  SELL  CNM  MomReversal  $34.27  P&L $-0.24                |
|  2026-09-03  SELL  ACGL  Pullback50  $34.60  P&L $+0.00                |
|  2026-09-03  SELL  AES  Pullback50  $34.50  P&L $+0.00                 |
|  2026-09-02  SELL  MO  Pullback50  $34.52  P&L $+0.00                  |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-08T09:16:03.142424-04:00 share=25% ===
2026-09-08 09:16:03,142 INFO === options_live_micro LIVE 2026-09-08T09:16:03.142424-04:00 share=25% ===
Live account equity $230.55 cash $126.02 #225458845 options_level=3
2026-09-08 09:16:03,343 INFO Live account equity $230.55 cash $126.02 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-08 09:16:03,402 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-08 09:16:03,460 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (162 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1052 | WARN | <<<
| Missing exit records (post) |  1050 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1029 med=+12.5% | TAINTED n=1791 med=-38.4% | KEEP-only n=551 med=+51.4% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.55 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260908T132104Z

- UTC timestamp: `20260908T132104Z`
- GitHub run: [#9320](https://github.com/28twagg-ops/TradingBot/actions/runs/34231311397)
- Run id: `34231311397`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260908T132104Z_live_bot.log`, `logs/action_runs/20260908T132104Z_live_options.log`, `logs/action_runs/20260908T132104Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1029 | 50.1 | +12.5 | +47.6 | $+15,692 |
| TAINTED | 1791 | 33.5 | -38.4 | +12.7 | $-8,651 |
| KEEP-only | 551 | 64.2 | +51.4 | +73.6 | $+10,279 |
| KEEP-only recent | 343 | 61.2 | +53.6 | +90.2 | $+5,022 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T09:21:10.619558-04:00","date":"2026-09-08","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.24},"signals":0,"placed":0,"equity":1004806.25,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9320","github_run_id":"34231311397","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:21:05  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.56|
|  Cash                                                           $126.02|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $104.54|
|  Open P&L                                                        $+0.83|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     unknown         $34.76     $255.49  $256.80  +0.5%   $+0.18  |
|  FLEX     unknown         $35.07     $109.37  $110.94  +1.4%   $+0.50  |
|  LII      unknown         $34.71     $386.29  $388.01  +0.4%   $+0.15  |
|                                                                        |
|  Total invested                                                 $104.54|
|  Total open P&L                                                  $+0.83|
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
|  2026-09-04  SELL  APD  Pullback50  $34.37  P&L $-0.21                 |
|  2026-09-03  SELL  ACGL  Pullback50  $34.56  P&L $-0.00                |
|  2026-09-03  SELL  CNM  MomReversal  $34.27  P&L $-0.24                |
|  2026-09-03  SELL  ACGL  Pullback50  $34.60  P&L $+0.00                |
|  2026-09-03  SELL  AES  Pullback50  $34.50  P&L $+0.00                 |
|  2026-09-02  SELL  MO  Pullback50  $34.52  P&L $+0.00                  |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-08T09:21:07.143100-04:00 share=25% ===
2026-09-08 09:21:07,143 INFO === options_live_micro LIVE 2026-09-08T09:21:07.143100-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-08 09:21:07,454 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-08 09:21:07,494 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-08 09:21:07,520 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (162 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1052 | WARN | <<<
| Missing exit records (post) |  1050 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1029 med=+12.5% | TAINTED n=1791 med=-38.4% | KEEP-only n=551 med=+51.4% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.56 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260908T132558Z

- UTC timestamp: `20260908T132558Z`
- GitHub run: [#9321](https://github.com/28twagg-ops/TradingBot/actions/runs/34231824080)
- Run id: `34231824080`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`10s`
- Full logs: `logs/action_runs/20260908T132558Z_live_bot.log`, `logs/action_runs/20260908T132558Z_live_options.log`, `logs/action_runs/20260908T132558Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1029 | 50.1 | +12.5 | +47.6 | $+15,692 |
| TAINTED | 1791 | 33.5 | -38.4 | +12.7 | $-8,651 |
| KEEP-only | 551 | 64.2 | +51.4 | +73.6 | $+10,279 |
| KEEP-only recent | 343 | 61.2 | +53.6 | +90.2 | $+5,022 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T09:26:02.382276-04:00","date":"2026-09-08","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.21},"signals":0,"placed":0,"equity":1004668.25,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9321","github_run_id":"34231824080","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:25:59  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.70|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.70|
|  Cash                                                           $126.02|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $104.68|
|  Open P&L                                                        $+0.97|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     unknown         $34.78     $255.49  $256.98  +0.6%   $+0.20  |
|  FLEX     unknown         $35.18     $109.37  $111.31  +1.8%   $+0.61  |
|  LII      unknown         $34.71     $386.29  $388.01  +0.4%   $+0.15  |
|                                                                        |
|  Total invested                                                 $104.68|
|  Total open P&L                                                  $+0.97|
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
|  2026-09-04  SELL  APD  Pullback50  $34.37  P&L $-0.21                 |
|  2026-09-03  SELL  ACGL  Pullback50  $34.56  P&L $-0.00                |
|  2026-09-03  SELL  CNM  MomReversal  $34.27  P&L $-0.24                |
|  2026-09-03  SELL  ACGL  Pullback50  $34.60  P&L $+0.00                |
|  2026-09-03  SELL  AES  Pullback50  $34.50  P&L $+0.00                 |
|  2026-09-02  SELL  MO  Pullback50  $34.52  P&L $+0.00                  |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-08T09:26:00.101743-04:00 share=25% ===
2026-09-08 09:26:00,101 INFO === options_live_micro LIVE 2026-09-08T09:26:00.101743-04:00 share=25% ===
Live account equity $230.70 cash $126.02 #225458845 options_level=3
2026-09-08 09:26:00,183 INFO Live account equity $230.70 cash $126.02 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-08 09:26:00,205 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-08 09:26:00,227 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (162 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1052 | WARN | <<<
| Missing exit records (post) |  1050 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1029 med=+12.5% | TAINTED n=1791 med=-38.4% | KEEP-only n=551 med=+51.4% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260908T133108Z

- UTC timestamp: `20260908T133108Z`
- GitHub run: [#9322](https://github.com/28twagg-ops/TradingBot/actions/runs/34232338469)
- Run id: `34232338469`
- Live bot: exit=`0`, duration=`218s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260908T133108Z_live_bot.log`, `logs/action_runs/20260908T133108Z_live_options.log`, `logs/action_runs/20260908T133108Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1029 | 50.1 | +12.5 | +47.6 | $+15,692 |
| TAINTED | 1791 | 33.5 | -38.4 | +12.7 | $-8,651 |
| KEEP-only | 551 | 64.2 | +51.4 | +73.6 | $+10,279 |
| KEEP-only recent | 343 | 61.2 | +53.6 | +90.2 | $+5,022 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T09:26:02.382276-04:00","date":"2026-09-08","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.21},"signals":0,"placed":0,"equity":1004668.25,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9321","github_run_id":"34231824080","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:31:09  INFO      Mode: morning_prep
13:31:10  INFO      Fetching tickers (universe=both)...
13:31:11  INFO        S&P 500: 503
13:31:11  INFO        MidCap 400: 400
13:31:11  INFO        Total: 903 tickers
13:31:12  INFO        [prep_universe] 40/903 (40 valid)
13:31:14  INFO        [prep_universe] 80/903 (80 valid)
13:31:16  INFO        [prep_universe] 120/903 (120 valid)
13:31:18  INFO        [prep_universe] 160/903 (160 valid)
13:31:19  INFO        [prep_universe] 200/903 (199 valid)
13:31:24  INFO        [prep_universe] 240/903 (238 valid)
13:31:37  INFO        [prep_universe] 280/903 (278 valid)
13:31:47  INFO        [prep_universe] 320/903 (318 valid)
13:32:01  INFO        [prep_universe] 360/903 (358 valid)
13:32:11  INFO        [prep_universe] 400/903 (397 valid)
13:32:25  INFO        [prep_universe] 440/903 (437 valid)
13:32:35  INFO        [prep_universe] 480/903 (477 valid)
13:32:49  INFO        [prep_universe] 520/903 (517 valid)
13:33:02  INFO        [prep_universe] 560/903 (557 valid)
13:33:12  INFO        [prep_universe] 600/903 (597 valid)
13:33:26  INFO        [prep_universe] 640/903 (637 valid)
13:33:36  INFO        [prep_universe] 680/903 (677 valid)
13:33:49  INFO        [prep_universe] 720/903 (717 valid)
13:33:59  INFO        [prep_universe] 760/903 (757 valid)
13:34:13  INFO        [prep_universe] 800/903 (797 valid)
13:34:23  INFO        [prep_universe] 840/903 (837 valid)
13:34:36  INFO        [prep_universe] 880/903 (877 valid)
13:34:43  INFO        [prep_universe] 903/903 (900 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.65|
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
|  Open positions                                                       0|
|  Invested                                                         $0.00|
|  Open P&L                                                        $+0.00|
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
|  Exit candidates                                                      0|
|  Signal candidates                                                   22|
|  Universe scanned                                                   903|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-08T09:34:47.385126-04:00 share=25% ===
2026-09-08 09:34:47,385 INFO === options_live_micro LIVE 2026-09-08T09:34:47.385126-04:00 share=25% ===
Live account equity $230.65 cash $230.65 #225458845 options_level=3
2026-09-08 09:34:47,711 INFO Live account equity $230.65 cash $230.65 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-08 09:34:47,910 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-08 09:34:48,043 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (22 earlier lines - see full log file)
  FLAG b769|S396|dee68d48 missing from Alpaca
  FLAG b768|S396|b42bcd2e missing from Alpaca
  FLAG b17|S202|cd4cb496 missing from Alpaca
  FLAG b16|S202|64636843 missing from Alpaca
  FLAG b913|S412|b3e4dda2 missing from Alpaca
  FLAG b912|S412|d7862491 missing from Alpaca
  FLAG b899|S411|01f19e7a missing from Alpaca
  FLAG b898|S411|146c5042 missing from Alpaca
  FLAG b90|S406|7f115fd5 missing from Alpaca
  FLAG b792|S399|6dbafdfc missing from Alpaca
  FLAG b405|S364|ee6d042e missing from Alpaca
  FLAG b404|S364|b5bf5868 missing from Alpaca
  FLAG b391|S363|27abfa07 missing from Alpaca
  FLAG b390|S363|315d92f7 missing from Alpaca
  FLAG b313|S355|3eee2971 missing from Alpaca
  FLAG b312|S355|5cdecd71 missing from Alpaca
  FLAG b1137|S163|50900b75 missing from Alpaca
  FLAG b1136|S163|73249aea missing from Alpaca
  FLAG b1109|S166|f04751eb missing from Alpaca
  FLAG b1122|S168|090a3a14 missing from Alpaca
  FLAG b0|ORPHAN|916c1acd missing from Alpaca
  FLAG b787|S398|c35b80bf missing from Alpaca
  FLAG b786|S398|115f87aa missing from Alpaca
  FLAG b1097|S167|f505f56b missing from Alpaca
  FLAG b1096|S167|f1a33d8e missing from Alpaca
  FLAG b1055|S165|881135f4 missing from Alpaca
  FLAG b0|ORPHAN|12a1c6cd missing from Alpaca
  FLAG b180|S217|c043e7a8 missing from Alpaca
  FLAG b859|S408|2154e9f8 missing from Alpaca
  FLAG b858|S408|c61e6f26 missing from Alpaca
  FLAG b90|S404|5e2e74cf missing from Alpaca
  FLAG b789|S398|1ec1c616 missing from Alpaca
  FLAG b788|S398|6f1d3691 missing from Alpaca
  FLAG b309|S354|ccef31e9 missing from Alpaca
  FLAG b308|S354|6a421c94 missing from Alpaca
  FLAG b1099|S167|57912312 missing from Alpaca
  FLAG b1098|S167|266b2b97 missing from Alpaca
  FLAG b1057|S165|d6b3e8db missing from Alpaca
  FLAG b1056|S165|2e74b9d5 missing from Alpaca
  FLAG b241|S401|a1f93441 missing from Alpaca
  FLAG b240|S401|f2cc4a68 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$1,003,624.18
  buying_power=$3,952,031.24 cash=$1,037,457.75
  open option orders: 16
    UPST260911C00029000 OrderSide.SELL qty=3 status=OrderStatus.NEW limit=None
    AVGO260911C00385000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    MARA260918C00012000 OrderSide.SELL qty=16 status=OrderStatus.NEW limit=None
    MARA260911C00012500 OrderSide.SELL qty=6 status=OrderStatus.NEW limit=None
    MARA260925C00012500 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
  open option positions: 16
    AVGO260909C00380000 qty=3 mkt=$417.00
    AVGO260911C00385000 qty=1 mkt=$207.00
    BA260911C00220000 qty=4 mkt=$200.00
    MARA260911C00011000 qty=2 mkt=$114.00
    MARA260911C00012500 qty=6 mkt=$60.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-08T09:34:53.315393-04:00 ===

[Run context]
Paper auth OK — equity $1003644.47, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-08 09:34:55,406 INFO   EXIT [b1112|lab1112_s166_w3_1045_1120_r1|S166] take_profit (+281.1%) SELL 1 AVGO260909C00380000 @<= 1.38
  EXIT [b20|lab0020_s202_w3_1045_1120_r1|S202] stop_loss (-100.0%) SELL failed PATH260911C00016500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-08 09:34:56,512 INFO   EXIT [b1114|lab1114_s166_w4_1120_1135_r1|S166] take_profit (+197.2%) SELL 1 AVGO260911C00385000 @<= 1.75
2026-09-08 09:35:00,327 INFO   EXIT [b331|lab0331_s357_w2_1005_1045_r2|S357] stop_loss (-88.9%) SELL 1 PATH260925C00017000 @<= 0.02
Protective stops: placed=2 upgraded=0 already=10 failed=3 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260908T133650Z

- UTC timestamp: `20260908T133650Z`
- GitHub run: [#9323](https://github.com/28twagg-ops/TradingBot/actions/runs/34232855268)
- Run id: `34232855268`
- Live bot: exit=`0`, duration=`218s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260908T133650Z_live_bot.log`, `logs/action_runs/20260908T133650Z_live_options.log`, `logs/action_runs/20260908T133650Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1029 | 50.1 | +12.5 | +47.6 | $+15,692 |
| TAINTED | 1791 | 33.5 | -38.4 | +12.7 | $-8,651 |
| KEEP-only | 551 | 64.2 | +51.4 | +73.6 | $+10,279 |
| KEEP-only recent | 343 | 61.2 | +53.6 | +90.2 | $+5,022 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T09:26:02.382276-04:00","date":"2026-09-08","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.21},"signals":0,"placed":0,"equity":1004668.25,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9321","github_run_id":"34231824080","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:36:52  INFO      Mode: morning_prep
13:36:53  INFO      Fetching tickers (universe=both)...
13:36:53  INFO        S&P 500: 503
13:36:53  INFO        MidCap 400: 400
13:36:53  INFO        Total: 903 tickers
13:36:54  INFO        [prep_universe] 40/903 (40 valid)
13:36:56  INFO        [prep_universe] 80/903 (80 valid)
13:36:57  INFO        [prep_universe] 120/903 (120 valid)
13:36:59  INFO        [prep_universe] 160/903 (160 valid)
13:37:00  INFO        [prep_universe] 200/903 (199 valid)
13:37:07  INFO        [prep_universe] 240/903 (238 valid)
13:37:18  INFO        [prep_universe] 280/903 (278 valid)
13:37:31  INFO        [prep_universe] 320/903 (318 valid)
13:37:42  INFO        [prep_universe] 360/903 (358 valid)
13:37:55  INFO        [prep_universe] 400/903 (397 valid)
13:38:05  INFO        [prep_universe] 440/903 (437 valid)
13:38:19  INFO        [prep_universe] 480/903 (477 valid)
13:38:32  INFO        [prep_universe] 520/903 (517 valid)
13:38:43  INFO        [prep_universe] 560/903 (557 valid)
13:38:56  INFO        [prep_universe] 600/903 (597 valid)
13:39:06  INFO        [prep_universe] 640/903 (637 valid)
13:39:20  INFO        [prep_universe] 680/903 (677 valid)
13:39:30  INFO        [prep_universe] 720/903 (717 valid)
13:39:44  INFO        [prep_universe] 760/903 (757 valid)
13:39:54  INFO        [prep_universe] 800/903 (797 valid)
13:40:07  INFO        [prep_universe] 840/903 (837 valid)
13:40:18  INFO        [prep_universe] 880/903 (877 valid)
13:40:25  INFO        [prep_universe] 903/903 (900 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.65|
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
|  Open positions                                                       0|
|  Invested                                                         $0.00|
|  Open P&L                                                        $+0.00|
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
|  Exit candidates                                                      0|
|  Signal candidates                                                   35|
|  Universe scanned                                                   903|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-08T09:40:29.379593-04:00 share=25% ===
2026-09-08 09:40:29,379 INFO === options_live_micro LIVE 2026-09-08T09:40:29.379593-04:00 share=25% ===
Live account equity $230.65 cash $230.65 #225458845 options_level=3
2026-09-08 09:40:29,602 INFO Live account equity $230.65 cash $230.65 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-08 09:40:29,807 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-08 09:40:29,942 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (26 earlier lines - see full log file)
  FLAG b16|S202|64636843 missing from Alpaca
  FLAG b913|S412|b3e4dda2 missing from Alpaca
  FLAG b912|S412|d7862491 missing from Alpaca
  FLAG b899|S411|01f19e7a missing from Alpaca
  FLAG b898|S411|146c5042 missing from Alpaca
  FLAG b90|S406|7f115fd5 missing from Alpaca
  FLAG b792|S399|6dbafdfc missing from Alpaca
  FLAG b405|S364|ee6d042e missing from Alpaca
  FLAG b404|S364|b5bf5868 missing from Alpaca
  FLAG b391|S363|27abfa07 missing from Alpaca
  FLAG b390|S363|315d92f7 missing from Alpaca
  FLAG b313|S355|3eee2971 missing from Alpaca
  FLAG b312|S355|5cdecd71 missing from Alpaca
  FLAG b1137|S163|50900b75 missing from Alpaca
  FLAG b1136|S163|73249aea missing from Alpaca
  FLAG b1109|S166|f04751eb missing from Alpaca
  FLAG b1122|S168|090a3a14 missing from Alpaca
  FLAG b0|ORPHAN|916c1acd missing from Alpaca
  FLAG b787|S398|c35b80bf missing from Alpaca
  FLAG b786|S398|115f87aa missing from Alpaca
  FLAG b1097|S167|f505f56b missing from Alpaca
  FLAG b1096|S167|f1a33d8e missing from Alpaca
  FLAG b1055|S165|881135f4 missing from Alpaca
  FLAG b0|ORPHAN|12a1c6cd missing from Alpaca
  FLAG b180|S217|c043e7a8 missing from Alpaca
  FLAG b859|S408|2154e9f8 missing from Alpaca
  FLAG b858|S408|c61e6f26 missing from Alpaca
  FLAG b90|S404|5e2e74cf missing from Alpaca
  FLAG b789|S398|1ec1c616 missing from Alpaca
  FLAG b788|S398|6f1d3691 missing from Alpaca
  FLAG b309|S354|ccef31e9 missing from Alpaca
  FLAG b308|S354|6a421c94 missing from Alpaca
  FLAG b1099|S167|57912312 missing from Alpaca
  FLAG b1098|S167|266b2b97 missing from Alpaca
  FLAG b1057|S165|d6b3e8db missing from Alpaca
  FLAG b1056|S165|2e74b9d5 missing from Alpaca
  FLAG b804|S404|c61e5d0a missing from Alpaca
  FLAG b781|S397|79b9b8f9 missing from Alpaca
  FLAG b780|S397|b3e07126 missing from Alpaca
  FLAG b241|S401|a1f93441 missing from Alpaca
  FLAG b240|S401|f2cc4a68 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$1,003,281.62
  buying_power=$3,953,108.48 cash=$1,037,844.62
  open option orders: 15
    BA260911C00220000 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
    PATH260911C00016500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.15
    MARA260918C00012000 OrderSide.SELL qty=16 status=OrderStatus.NEW limit=None
    MARA260911C00012500 OrderSide.SELL qty=6 status=OrderStatus.NEW limit=None
    MARA260925C00012500 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
  open option positions: 14
    AVGO260909C00380000 qty=2 mkt=$260.00
    BA260911C00220000 qty=4 mkt=$180.00
    MARA260911C00011000 qty=2 mkt=$114.00
    MARA260911C00012500 qty=6 mkt=$60.00
    MARA260918C00012000 qty=17 mkt=$680.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-08T09:40:35.387947-04:00 ===

[Run context]
Paper auth OK — equity $1003272.62, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b1127|lab1127_s168_w3_1045_1120_r2|S168] take_profit (+275.7%) SELL failed AVGO260909C00380000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b1126|lab1126_s168_w3_1045_1120_r1|S168] take_profit (+275.7%) SELL failed AVGO260909C00380000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b330|lab0330_s357_w2_1005_1045_r1|S357] stop_loss (-77.8%) SELL failed PATH260925C00017000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-08 09:40:40,198 INFO   EXIT [b20|lab0020_s202_w3_1045_1120_r1|S202] stop_loss (-100.0%) SELL 1 PATH260911C00016500 @<= 0.01
Protective stops: placed=0 upgraded=0 already=10 failed=3 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260908T134220Z

- UTC timestamp: `20260908T134220Z`
- GitHub run: [#9324](https://github.com/28twagg-ops/TradingBot/actions/runs/34233374403)
- Run id: `34233374403`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260908T134220Z_live_bot.log`, `logs/action_runs/20260908T134220Z_live_options.log`, `logs/action_runs/20260908T134220Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1029 | 50.1 | +12.5 | +47.6 | $+15,692 |
| TAINTED | 1791 | 33.5 | -38.4 | +12.7 | $-8,651 |
| KEEP-only | 551 | 64.2 | +51.4 | +73.6 | $+10,279 |
| KEEP-only recent | 343 | 61.2 | +53.6 | +90.2 | $+5,022 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T09:26:02.382276-04:00","date":"2026-09-08","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.21},"signals":0,"placed":0,"equity":1004668.25,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9321","github_run_id":"34231824080","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:42:21  INFO      Mode: morning_prep
13:42:22  INFO        Universe cache hit: 903 tickers (tickers_2026-09-08.json)
13:42:23  INFO        [prep_universe] 40/903 (40 valid)
13:42:24  INFO        [prep_universe] 80/903 (80 valid)
13:42:25  INFO        [prep_universe] 120/903 (120 valid)
13:42:26  INFO        [prep_universe] 160/903 (160 valid)
13:42:28  INFO        [prep_universe] 200/903 (199 valid)
13:42:35  INFO        [prep_universe] 240/903 (238 valid)
13:42:48  INFO        [prep_universe] 280/903 (278 valid)
13:42:58  INFO        [prep_universe] 320/903 (318 valid)
13:43:11  INFO        [prep_universe] 360/903 (358 valid)
13:43:22  INFO        [prep_universe] 400/903 (397 valid)
13:43:35  INFO        [prep_universe] 440/903 (437 valid)
13:43:48  INFO        [prep_universe] 480/903 (477 valid)
13:43:58  INFO        [prep_universe] 520/903 (517 valid)
13:44:11  INFO        [prep_universe] 560/903 (557 valid)
13:44:24  INFO        [prep_universe] 600/903 (597 valid)
13:44:35  INFO        [prep_universe] 640/903 (637 valid)
13:44:48  INFO        [prep_universe] 680/903 (677 valid)
13:44:58  INFO        [prep_universe] 720/903 (717 valid)
13:45:11  INFO        [prep_universe] 760/903 (757 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260908T134649Z

- UTC timestamp: `20260908T134649Z`
- GitHub run: [#9325](https://github.com/28twagg-ops/TradingBot/actions/runs/34233896047)
- Run id: `34233896047`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260908T134649Z_live_bot.log`, `logs/action_runs/20260908T134649Z_live_options.log`, `logs/action_runs/20260908T134649Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1029 | 50.1 | +12.5 | +47.6 | $+15,692 |
| TAINTED | 1791 | 33.5 | -38.4 | +12.7 | $-8,651 |
| KEEP-only | 551 | 64.2 | +51.4 | +73.6 | $+10,279 |
| KEEP-only recent | 343 | 61.2 | +53.6 | +90.2 | $+5,022 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T09:26:02.382276-04:00","date":"2026-09-08","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.21},"signals":0,"placed":0,"equity":1004668.25,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9321","github_run_id":"34231824080","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
... (66 earlier lines - see full log file)
|  Buys today: 0  |  entry cap: 3  |  max open: 3                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (18731.4m))|
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
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  43                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  ABBV     Pullback50      eq     $254.04  43.9   -3.18   50MA bounce (-|
|  APD      Pullback50      eq     $300.50  46.3   -2.45   50MA bounce (-|
|  AMCR     Pullback50      eq     $44.96   44.6   -2.61   50MA bounce (-|
|  AMZN     Pullback50      eq     $256.69  47.3   -2.85   50MA bounce (+|
|  AME      Pullback50      eq     $239.09  36.3   -2.52   50MA bounce (-|
|  BF-B     Pullback50      eq     $27.14   51.7   -2.20   50MA bounce (+|
|  ECL      Pullback50      eq     $279.54  49.3   -2.18   50MA bounce (+|
|  EQIX     Pullback50      eq     $1041.~  36.5   -2.58   50MA bounce (-|
|  EG       Pullback50      eq     $375.07  57.6   -2.74   50MA bounce (+|
|  GRMN     Pullback50      eq     $275.24  15.9   -1.99   50MA bounce (+|
|  JBHT     Pullback50      eq     $274.44  50.2   -2.38   50MA bounce (-|
|  NTRS     Pullback50      eq     $185.57  40.3   -2.61   50MA bounce (+|
|  PGR      Pullback50      eq     $217.03  62.2   -1.87   50MA bounce (-|
|  TER      Pullback50      eq     $373.36  39.0   -2.18   50MA bounce (+|
|  TRV      Pullback50      eq     $367.32  49.3   -2.55   50MA bounce (+|
|  TFC      Pullback50      eq     $51.46   43.7   -3.34   50MA bounce (-|
|  USB      Pullback50      eq     $63.08   40.0   -2.94   50MA bounce (-|
|  VLTO     Pullback50      eq     $95.61   48.1   -2.30   50MA bounce (+|
|  VTRS     Pullback50      eq     $16.73   60.6   -2.15   50MA bounce (-|
|  WAB      Pullback50      eq     $283.50  34.7   -2.48   50MA bounce (-|
|  WELL     Pullback50      eq     $238.12  55.0   -2.21   50MA bounce (+|
|  AFG      Pullback50      eq     $142.53  38.9   -3.13   50MA bounce (-|
|  AHR      Pullback50      eq     $54.83   52.5   -1.45   50MA bounce (-|
|  ARMK     Pullback50      eq     $57.96   35.1   -2.10   50MA bounce (+|
|  ASB      Pullback50      eq     $30.94   40.0   -2.51   50MA bounce (-|
|  BKH      Pullback50      eq     $73.50   52.2   -2.92   50MA bounce (-|
|  CBSH     Pullback50      eq     $59.07   45.5   -3.19   50MA bounce (+|
|  CHE      Pullback50      eq     $519.43  43.5   -1.92   50MA bounce (+|
|  EPR      Pullback50      eq     $60.30   49.5   -2.44   50MA bounce (-|
|  ENTG     Pullback50      eq     $141.34  41.0   -2.04   50MA bounce (-|
|  FAF      Pullback50      eq     $72.46   50.0   -2.28   50MA bounce (-|
|  KNX      Pullback50      eq     $72.48   54.7   -2.89   50MA bounce (+|
|  MSM      Pullback50      eq     $121.45  47.6   -3.10   50MA bounce (-|
|  NLY      Pullback50      eq     $22.84   38.0   -2.63   50MA bounce (-|
|  NVST     Pullback50      eq     $27.12   42.0   -2.74   50MA bounce (-|
|  NWE      Pullback50      eq     $71.28   54.0   -2.93   50MA bounce (+|
|  OGE      Pullback50      eq     $47.27   52.1   -2.69   50MA bounce (-|
|  PB       Pullback50      eq     $72.56   38.2   -2.85   50MA bounce (-|
|  SCI      Pullback50      eq     $82.03   48.3   -3.63   50MA bounce (+|
|  SBRA     Pullback50      eq     $20.76   58.7   -1.46   50MA bounce (+|
|  TREX     Pullback50      eq     $45.95   40.2   -2.46   50MA bounce (-|
|  UBSI     Pullback50      eq     $47.69   37.6   -3.14   50MA bounce (+|
|  ZION     Pullback50      eq     $69.32   41.6   -2.66   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |13:50:27  INFO        BUY  ABBV  $34.60  [Pullback50]  id=f04762fc-d39d-4fbe-8bbf-07dfe30b8c87
13:50:28  INFO        BUY  APD  $34.60  [Pullback50]  id=74864e0a-8ea9-4097-bf44-996a07328194
13:50:28  INFO        BUY  AMCR  $34.60  [Pullback50]  id=ee3125ae-44cd-4c2b-85a2-c063ad090e1f
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260908T135212Z

- UTC timestamp: `20260908T135212Z`
- GitHub run: [#9326](https://github.com/28twagg-ops/TradingBot/actions/runs/34234419429)
- Run id: `34234419429`
- Live bot: exit=`0`, duration=`219s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260908T135212Z_live_bot.log`, `logs/action_runs/20260908T135212Z_live_options.log`, `logs/action_runs/20260908T135212Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1029 | 50.1 | +12.5 | +47.6 | $+15,692 |
| TAINTED | 1791 | 33.5 | -38.4 | +12.7 | $-8,651 |
| KEEP-only | 551 | 64.2 | +51.4 | +73.6 | $+10,279 |
| KEEP-only recent | 343 | 61.2 | +53.6 | +90.2 | $+5,022 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T09:26:02.382276-04:00","date":"2026-09-08","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.21},"signals":0,"placed":0,"equity":1004668.25,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9321","github_run_id":"34231824080","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
... (118 earlier lines - see full log file)
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AES      Pullback50      eq     $14.79   58.6   -1.96   50MA bounce (+|
|  AMD      Pullback50      eq     $493.89  53.4   -2.75   50MA bounce (-|
|  ALL      Pullback50      eq     $256.86  44.9   -2.18   50MA bounce (-|
|  TECH     Pullback50      eq     $72.38   55.7   -2.43   50MA bounce (+|
|  BRK-B    Pullback50      eq     $503.98  51.6   -2.75   50MA bounce (+|
|  BF-B     Pullback50      eq     $26.85   49.4   -2.18   50MA bounce (-|
|  GLW      Pullback50      eq     $163.35  53.5   -2.79   50MA bounce (-|
|  ECL      Pullback50      eq     $279.66  49.5   -2.16   50MA bounce (+|
|  EQIX     Pullback50      eq     $1040.~  36.3   -2.56   50MA bounce (-|
|  EG       Pullback50      eq     $375.86  58.5   -2.72   50MA bounce (+|
|  GRMN     Pullback50      eq     $275.41  16.0   -1.97   50MA bounce (+|
|  INTC     Pullback50      eq     $100.92  57.2   -2.10   50MA bounce (+|
|  IBKR     Pullback50      eq     $92.82   54.2   -2.42   50MA bounce (+|
|  JBHT     Pullback50      eq     $273.69  49.6   -2.37   50MA bounce (-|
|  JCI      Pullback50      eq     $145.86  42.1   -2.92   50MA bounce (+|
|  MTB      Pullback50      eq     $242.53  38.7   -2.04   50MA bounce (-|
|  NTRS     Pullback50      eq     $185.82  40.7   -2.60   50MA bounce (+|
|  STLD     Pullback50      eq     $242.86  45.2   -1.74   50MA bounce (+|
|  TER      Pullback50      eq     $371.44  38.2   -2.15   50MA bounce (+|
|  TFC      Pullback50      eq     $51.43   43.5   -3.33   50MA bounce (-|
|  TRV      Pullback50      eq     $366.06  47.9   -2.54   50MA bounce (+|
|  USB      Pullback50      eq     $63.05   39.9   -2.93   50MA bounce (-|
|  VLTO     Pullback50      eq     $95.89   49.2   -2.27   50MA bounce (+|
|  VTRS     Pullback50      eq     $16.73   60.5   -2.15   50MA bounce (-|
|  WAB      Pullback50      eq     $283.15  34.0   -2.48   50MA bounce (-|
|  WELL     Pullback50      eq     $237.77  54.4   -2.19   50MA bounce (+|13:55:50  INFO        place_all_stops: checking 3 positions...
13:55:50  INFO        STOP skipped ABBV: fractional (0.1369 shares) — software exit will handle it
13:55:50  INFO        STOP skipped AMCR: fractional (0.7714 shares) — software exit will handle it
13:55:50  INFO        STOP skipped APD: fractional (0.1154 shares) — software exit will handle it
13:55:51  INFO        Daily log -> logs/daily/2026-09-08.md
13:55:51  INFO        Dashboard written → logs/dashboard.md

|  AFG      Pullback50      eq     $142.53  38.9   -3.12   50MA bounce (-|
|  AHR      Pullback50      eq     $54.90   53.0   -1.45   50MA bounce (-|
|  ARMK     Pullback50      eq     $57.93   34.9   -2.09   50MA bounce (+|
|  ASB      Pullback50      eq     $30.95   40.1   -2.51   50MA bounce (-|
|  BKH      Pullback50      eq     $73.67   53.2   -2.92   50MA bounce (+|
|  CBSH     Pullback50      eq     $58.97   44.4   -3.18   50MA bounce (+|
|  CHE      Pullback50      eq     $517.92  42.6   -1.84   50MA bounce (+|
|  EPR      Pullback50      eq     $60.46   50.7   -2.43   50MA bounce (-|
|  FAF      Pullback50      eq     $72.65   50.8   -2.27   50MA bounce (-|
|  KNX      Pullback50      eq     $72.20   54.0   -2.88   50MA bounce (+|
|  MSM      Pullback50      eq     $121.39  47.5   -3.09   50MA bounce (-|
|  NLY      Pullback50      eq     $22.87   38.6   -2.61   50MA bounce (-|
|  NVST     Pullback50      eq     $27.17   42.5   -2.44   50MA bounce (-|
|  NOVT     Pullback50      eq     $150.89  42.0   -2.75   50MA bounce (-|
|  NWE      Pullback50      eq     $71.24   53.8   -2.92   50MA bounce (+|
|  OGE      Pullback50      eq     $47.40   53.3   -2.68   50MA bounce (-|
|  PB       Pullback50      eq     $72.40   37.4   -2.85   50MA bounce (-|
|  SBRA     Pullback50      eq     $20.73   58.0   -1.44   50MA bounce (+|
|  SCI      Pullback50      eq     $82.13   48.8   -3.62   50MA bounce (+|
|  TREX     Pullback50      eq     $46.19   41.7   -2.42   50MA bounce (-|
|  UBSI     Pullback50      eq     $47.65   37.3   -3.12   50MA bounce (+|
|  ZION     Pullback50      eq     $69.15   40.9   -2.66   50MA bounce (-|
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
|  Scanned                                                            897|
|  Signals                                                             48|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $230.46|
|  Cash                                                           $126.88|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-08T09:55:51.895976-04:00 share=25% ===
2026-09-08 09:55:51,896 INFO === options_live_micro LIVE 2026-09-08T09:55:51.895976-04:00 share=25% ===
Live account equity $230.46 cash $126.88 #225458845 options_level=3
2026-09-08 09:55:52,166 INFO Live account equity $230.46 cash $126.88 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-08 09:55:52,424 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-08 09:55:52,620 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=61 paper_keys=yes dry_run=False
  alpaca positions=14
  FLAG b1114|S166|7a91ff51 missing from Alpaca
  FLAG b803|S404|08d46875 missing from Alpaca
  FLAG b802|S404|dbf5fb12 missing from Alpaca
  FLAG b779|S397|d37ab7f5 missing from Alpaca
  FLAG b778|S397|4f36dcc3 missing from Alpaca
  FLAG b804|S404|c61e5d0a missing from Alpaca
  FLAG b781|S397|79b9b8f9 missing from Alpaca
  FLAG b780|S397|b3e07126 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$1,003,842.52
  buying_power=$3,954,692.88 cash=$1,037,988.52
  open option orders: 14
    PATH260911C00016500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.01
    BA260911C00220000 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
    MARA260918C00012000 OrderSide.SELL qty=16 status=OrderStatus.NEW limit=None
    MARA260911C00012500 OrderSide.SELL qty=6 status=OrderStatus.NEW limit=None
    MARA260925C00012500 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
  open option positions: 13
    AVGO260909C00380000 qty=2 mkt=$174.00
    BA260911C00220000 qty=4 mkt=$292.00
    MARA260911C00011000 qty=2 mkt=$150.00
    MARA260911C00012500 qty=6 mkt=$90.00
    MARA260918C00012000 qty=17 mkt=$884.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-08T09:55:56.075778-04:00 ===

[Run context]
Paper auth OK — equity $1003834.52, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b330|lab0330_s357_w2_1005_1045_r1|S357] stop_loss (-84.4%) SELL failed PATH260925C00017000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b1127|lab1127_s168_w3_1045_1120_r2|S168] take_profit (+135.1%) SELL failed AVGO260909C00380000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b1126|lab1126_s168_w3_1045_1120_r1|S168] take_profit (+135.1%) SELL failed AVGO260909C00380000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 upgraded=0 already=9 failed=3 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260908T135750Z

- UTC timestamp: `20260908T135750Z`
- GitHub run: [#9327](https://github.com/28twagg-ops/TradingBot/actions/runs/34234940475)
- Run id: `34234940475`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260908T135750Z_live_bot.log`, `logs/action_runs/20260908T135750Z_live_options.log`, `logs/action_runs/20260908T135750Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1029 | 50.1 | +12.5 | +47.6 | $+15,692 |
| TAINTED | 1791 | 33.5 | -38.4 | +12.7 | $-8,651 |
| KEEP-only | 551 | 64.2 | +51.4 | +73.6 | $+10,279 |
| KEEP-only recent | 343 | 61.2 | +53.6 | +90.2 | $+5,022 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T09:26:02.382276-04:00","date":"2026-09-08","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.21},"signals":0,"placed":0,"equity":1004668.25,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9321","github_run_id":"34231824080","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:57:51  INFO      Mode: morning_scan
13:57:52  INFO        [positions] 3/3 (3 valid)
13:57:52  INFO        SELL MARKET [urgent] ABBV closed
13:57:55  INFO        TX logged: SELL ABBV  P&L -0.53%
13:57:55  INFO        Universe cache hit: 903 tickers (tickers_2026-09-08.json)
13:57:56  INFO        [universe] 40/901 (40 valid)
13:57:58  INFO        [universe] 80/901 (80 valid)
13:57:59  INFO        [universe] 120/901 (120 valid)
13:58:00  INFO        [universe] 160/901 (160 valid)
13:58:02  INFO        [universe] 200/901 (199 valid)
13:58:09  INFO        [universe] 240/901 (238 valid)
13:58:20  INFO        [universe] 280/901 (278 valid)
13:58:33  INFO        [universe] 320/901 (318 valid)
13:58:46  INFO        [universe] 360/901 (358 valid)
13:58:57  INFO        [universe] 400/901 (397 valid)
13:59:10  INFO        [universe] 440/901 (437 valid)
13:59:20  INFO        [universe] 480/901 (477 valid)
13:59:33  INFO        [universe] 520/901 (517 valid)
13:59:43  INFO        [universe] 560/901 (557 valid)
13:59:57  INFO        [universe] 600/901 (597 valid)
14:00:10  INFO        [universe] 640/901 (637 valid)
14:00:20  INFO        [universe] 680/901 (677 valid)
14:00:34  INFO        [universe] 720/901 (717 valid)
14:00:44  INFO        [universe] 760/901 (757 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260908T140209Z

- UTC timestamp: `20260908T140209Z`
- GitHub run: [#9328](https://github.com/28twagg-ops/TradingBot/actions/runs/34235460951)
- Run id: `34235460951`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`148s`
- Full logs: `logs/action_runs/20260908T140209Z_live_bot.log`, `logs/action_runs/20260908T140209Z_live_options.log`, `logs/action_runs/20260908T140209Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1031 | 50.1 | +12.5 | +47.7 | $+15,753 |
| TAINTED | 1791 | 33.5 | -38.4 | +12.7 | $-8,651 |
| KEEP-only | 552 | 64.1 | +51.2 | +73.3 | $+10,239 |
| KEEP-only recent | 344 | 61.0 | +53.4 | +89.7 | $+4,982 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T10:02:15.082419-04:00","date":"2026-09-08","mode":"entry+manage","header":"entry+manage (49 new)","elapsed_s":139.5,"phases_s":{"reconcile":0.33,"cancel":0.09,"manage":3.4,"protective_stops":1.32,"scan":29.44,"entries":89.54,"reconcile2":0.82},"signals":268,"placed":49,"equity":1003779.0,"open_positions":18,"pending_orders":29,"open_lots":70,"submitted_today":49,"filled_today":20,"unattributed_contracts":3,"top_signals":["S165:COIN","S164:COIN","S168:COIN","S167:COIN","S163:COIN","S350:COIN","S351:COIN","S352:COIN"],"github_run":"9328","github_run_id":"34235460951","status":"ok","data_quality":{"clean":{"n":1031,"win":50.15,"med":12.5,"avg":47.67,"pnl":15753.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":552,"win":64.13,"med":51.18,"avg":73.34,"pnl":10239.45},"keep_only_recent":{"n":344,"win":61.05,"med":53.45,"avg":89.66,"pnl":4982.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:02:10  INFO      Mode: exits
14:02:11  INFO        place_all_stops: checking 2 positions...
14:02:11  INFO        STOP skipped AMCR: fractional (0.7714 shares) — software exit will handle it
14:02:11  INFO        STOP skipped APD: fractional (0.1154 shares) — software exit will handle it
14:02:11  INFO        [positions] 2/2 (2 valid)
14:02:11  INFO        Daily log -> logs/daily/2026-09-08.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:02 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.59|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMCR  P&L +0.2%  $+0.06                                           HOLD|
|  APD  P&L +0.4%  $+0.13                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
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
=== options_live_micro LIVE 2026-09-08T10:02:12.266069-04:00 share=25% ===
2026-09-08 10:02:12,266 INFO === options_live_micro LIVE 2026-09-08T10:02:12.266069-04:00 share=25% ===
Live account equity $230.59 cash $161.23 #225458845 options_level=3
2026-09-08 10:02:12,383 INFO Live account equity $230.59 cash $161.23 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-08 10:02:12,544 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-08 10:02:12,622 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (190 earlier lines - see full log file)
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 249 | 13 |
| S164 | 265 | 14 |
| S165 | 1705 | 27 |
| S166 | 135 | 9 |
| S167 | 259 | 14 |
| S168 | 192 | 12 |
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
| 2026-09-08 |    4 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1052 | WARN | <<<
| Missing exit records (post) |  1050 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    70 | INFO |
| Total closed lots           |  2002 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1031 med=+12.5% | TAINTED n=1791 med=-38.4% | KEEP-only n=552 med=+51.2% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.59 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260908T140607Z

- UTC timestamp: `20260908T140607Z`
- GitHub run: [#9329](https://github.com/28twagg-ops/TradingBot/actions/runs/34235988686)
- Run id: `34235988686`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`150s`
- Full logs: `logs/action_runs/20260908T140607Z_live_bot.log`, `logs/action_runs/20260908T140607Z_live_options.log`, `logs/action_runs/20260908T140607Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1032 | 50.2 | +12.8 | +47.7 | $+15,791 |
| TAINTED | 1792 | 33.5 | -38.3 | +12.7 | $-8,620 |
| KEEP-only | 552 | 64.1 | +51.2 | +73.3 | $+10,239 |
| KEEP-only recent | 344 | 61.0 | +53.4 | +89.7 | $+4,982 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T10:06:16.568493-04:00","date":"2026-09-08","mode":"entry+manage","header":"entry+manage (24 new)","elapsed_s":139.6,"phases_s":{"reconcile":1.63,"cancel":0.15,"manage":6.42,"protective_stops":3.03,"scan":35.54,"entries":78.53,"reconcile2":1.31},"signals":268,"placed":24,"equity":1003832.51,"open_positions":21,"pending_orders":19,"open_lots":103,"submitted_today":73,"filled_today":54,"unattributed_contracts":0,"top_signals":["S165:COIN","S164:COIN","S168:COIN","S167:COIN","S163:COIN","S350:COIN","S351:COIN","S352:COIN"],"github_run":"9329","github_run_id":"34235988686","status":"ok","data_quality":{"clean":{"n":1032,"win":50.19,"med":12.8,"avg":47.72,"pnl":15791.21},"tainted":{"n":1792,"win":33.54,"med":-38.34,"avg":12.75,"pnl":-8619.84},"keep_only":{"n":552,"win":64.13,"med":51.18,"avg":73.34,"pnl":10239.45},"keep_only_recent":{"n":344,"win":61.05,"med":53.45,"avg":89.66,"pnl":4982.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:06:09  INFO      Mode: exits
14:06:10  INFO        Daily log -> logs/daily/2026-09-08.md
14:06:10  INFO        Daily log reconciled -> logs/daily/2026-09-08.md (1 ledger rows)
14:06:10  INFO        place_all_stops: checking 2 positions...
14:06:10  INFO        STOP skipped AMCR: fractional (0.7714 shares) — software exit will handle it
14:06:10  INFO        STOP skipped APD: fractional (0.1154 shares) — software exit will handle it
14:06:11  INFO        [positions] 2/2 (2 valid)
14:06:11  INFO        Daily log -> logs/daily/2026-09-08.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.58|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMCR  P&L +0.0%  $+0.01                                           HOLD|
|  APD  P&L +0.5%  $+0.17                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
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
=== options_live_micro LIVE 2026-09-08T10:06:12.452137-04:00 share=25% ===
2026-09-08 10:06:12,452 INFO === options_live_micro LIVE 2026-09-08T10:06:12.452137-04:00 share=25% ===
Live account equity $230.58 cash $161.23 #225458845 options_level=3
2026-09-08 10:06:12,709 INFO Live account equity $230.58 cash $161.23 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-08 10:06:12,925 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-08 10:06:13,103 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (203 earlier lines - see full log file)
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 249 | 13 |
| S164 | 267 | 14 |
| S165 | 1707 | 27 |
| S166 | 135 | 9 |
| S167 | 261 | 14 |
| S168 | 194 | 12 |
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
| 2026-09-08 |    4 |    4 |    4 |    0 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    20 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1052 | WARN | <<<
| Missing exit records (post) |  1050 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   103 | INFO |
| Total closed lots           |  2004 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1032 med=+12.8% | TAINTED n=1792 med=-38.3% | KEEP-only n=552 med=+51.2% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.58 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260908T141105Z

- UTC timestamp: `20260908T141105Z`
- GitHub run: [#9330](https://github.com/28twagg-ops/TradingBot/actions/runs/34236519757)
- Run id: `34236519757`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`148s`
- Full logs: `logs/action_runs/20260908T141105Z_live_bot.log`, `logs/action_runs/20260908T141105Z_live_options.log`, `logs/action_runs/20260908T141105Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1033 | 50.2 | +13.1 | +47.8 | $+15,834 |
| TAINTED | 1792 | 33.5 | -38.3 | +12.7 | $-8,620 |
| KEEP-only | 552 | 64.1 | +51.2 | +73.3 | $+10,239 |
| KEEP-only recent | 344 | 61.0 | +53.4 | +89.7 | $+4,982 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T10:11:14.845532-04:00","date":"2026-09-08","mode":"entry+manage","header":"entry+manage (4 new)","elapsed_s":135.6,"phases_s":{"reconcile":1.07,"cancel":0.14,"manage":9.64,"protective_stops":3.25,"scan":53.13,"entries":55.2,"reconcile2":3.77},"signals":268,"placed":4,"equity":1003143.74,"open_positions":23,"pending_orders":8,"open_lots":117,"submitted_today":77,"filled_today":69,"unattributed_contracts":0,"top_signals":["S165:COIN","S164:COIN","S168:COIN","S167:COIN","S163:COIN","S350:COIN","S351:COIN","S352:COIN"],"github_run":"9330","github_run_id":"34236519757","status":"ok","data_quality":{"clean":{"n":1033,"win":50.24,"med":13.11,"avg":47.79,"pnl":15834.21},"tainted":{"n":1792,"win":33.54,"med":-38.34,"avg":12.75,"pnl":-8619.84},"keep_only":{"n":552,"win":64.13,"med":51.18,"avg":73.34,"pnl":10239.45},"keep_only_recent":{"n":344,"win":61.05,"med":53.45,"avg":89.66,"pnl":4982.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:11:08  INFO      Mode: exits
14:11:09  INFO        Daily log -> logs/daily/2026-09-08.md
14:11:09  INFO        Daily log reconciled -> logs/daily/2026-09-08.md (1 ledger rows)
14:11:09  INFO        place_all_stops: checking 2 positions...
14:11:09  INFO        STOP skipped AMCR: fractional (0.7714 shares) — software exit will handle it
14:11:09  INFO        STOP skipped APD: fractional (0.1154 shares) — software exit will handle it
14:11:09  INFO        [positions] 2/2 (2 valid)
14:11:10  INFO        Daily log -> logs/daily/2026-09-08.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.46|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMCR  P&L -0.1%  $-0.04                                           HOLD|
|  APD  P&L +0.3%  $+0.10                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
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
=== options_live_micro LIVE 2026-09-08T10:11:10.984230-04:00 share=25% ===
2026-09-08 10:11:10,984 INFO === options_live_micro LIVE 2026-09-08T10:11:10.984230-04:00 share=25% ===
Live account equity $230.45 cash $161.23 #225458845 options_level=3
2026-09-08 10:11:11,223 INFO Live account equity $230.45 cash $161.23 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-08 10:11:11,429 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-08 10:11:11,616 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (215 earlier lines - see full log file)
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 249 | 13 |
| S164 | 267 | 14 |
| S165 | 1707 | 27 |
| S166 | 135 | 9 |
| S167 | 261 | 14 |
| S168 | 194 | 12 |
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
| 2026-09-08 |    4 |    4 |    4 |    0 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    20 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1052 | WARN | <<<
| Missing exit records (post) |  1050 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   117 | INFO |
| Total closed lots           |  2005 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1033 med=+13.1% | TAINTED n=1792 med=-38.3% | KEEP-only n=552 med=+51.2% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.45 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260908T141611Z

- UTC timestamp: `20260908T141611Z`
- GitHub run: [#9331](https://github.com/28twagg-ops/TradingBot/actions/runs/34237048387)
- Run id: `34237048387`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`92s`
- Full logs: `logs/action_runs/20260908T141611Z_live_bot.log`, `logs/action_runs/20260908T141611Z_live_options.log`, `logs/action_runs/20260908T141611Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1035 | 50.1 | +12.5 | +47.6 | $+15,776 |
| TAINTED | 1792 | 33.5 | -38.3 | +12.7 | $-8,620 |
| KEEP-only | 554 | 63.9 | +50.9 | +72.9 | $+10,181 |
| KEEP-only recent | 346 | 60.7 | +53.3 | +88.9 | $+4,924 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T10:16:16.911277-04:00","date":"2026-09-08","mode":"entry+manage","header":"entry+manage (16 new)","elapsed_s":83.3,"phases_s":{"reconcile":0.56,"cancel":0.1,"manage":7.61,"protective_stops":2.08,"scan":29.01,"entries":28.94,"reconcile2":0.4},"signals":268,"placed":16,"equity":1003318.88,"open_positions":23,"pending_orders":22,"open_lots":117,"submitted_today":93,"filled_today":71,"unattributed_contracts":0,"top_signals":["S165:COIN","S164:COIN","S168:COIN","S167:COIN","S163:COIN","S350:COIN","S351:COIN","S352:COIN"],"github_run":"9331","github_run_id":"34237048387","status":"ok","data_quality":{"clean":{"n":1035,"win":50.14,"med":12.5,"avg":47.6,"pnl":15776.21},"tainted":{"n":1792,"win":33.54,"med":-38.34,"avg":12.75,"pnl":-8619.84},"keep_only":{"n":554,"win":63.9,"med":50.93,"avg":72.9,"pnl":10181.45},"keep_only_recent":{"n":346,"win":60.69,"med":53.33,"avg":88.86,"pnl":4924.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:16:12  INFO      Mode: exits
14:16:13  INFO        Daily log -> logs/daily/2026-09-08.md
14:16:13  INFO        Daily log reconciled -> logs/daily/2026-09-08.md (1 ledger rows)
14:16:13  INFO        place_all_stops: checking 2 positions...
14:16:13  INFO        STOP skipped AMCR: fractional (0.7714 shares) — software exit will handle it
14:16:13  INFO        STOP skipped APD: fractional (0.1154 shares) — software exit will handle it
14:16:13  INFO        [positions] 2/2 (2 valid)
14:16:13  INFO        Daily log -> logs/daily/2026-09-08.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.55|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMCR  P&L -0.0%  $-0.01                                           HOLD|
|  APD  P&L +0.4%  $+0.15                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
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
=== options_live_micro LIVE 2026-09-08T10:16:14.407327-04:00 share=25% ===
2026-09-08 10:16:14,407 INFO === options_live_micro LIVE 2026-09-08T10:16:14.407327-04:00 share=25% ===
Live account equity $230.55 cash $161.23 #225458845 options_level=3
2026-09-08 10:16:14,536 INFO Live account equity $230.55 cash $161.23 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-08 10:16:14,665 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-08 10:16:14,756 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (186 earlier lines - see full log file)
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 249 | 13 |
| S164 | 269 | 15 |
| S165 | 1709 | 28 |
| S166 | 135 | 9 |
| S167 | 263 | 15 |
| S168 | 196 | 13 |
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
| 2026-09-08 |    4 |    6 |    6 |    0 |    6 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    28 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1052 | WARN | <<<
| Missing exit records (post) |  1050 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   117 | INFO |
| Total closed lots           |  2007 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1035 med=+12.5% | TAINTED n=1792 med=-38.3% | KEEP-only n=554 med=+50.9% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.55 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260908T142104Z

- UTC timestamp: `20260908T142104Z`
- GitHub run: [#9332](https://github.com/28twagg-ops/TradingBot/actions/runs/34237579707)
- Run id: `34237579707`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`81s`
- Full logs: `logs/action_runs/20260908T142104Z_live_bot.log`, `logs/action_runs/20260908T142104Z_live_options.log`, `logs/action_runs/20260908T142104Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1035 | 50.1 | +12.5 | +47.6 | $+15,776 |
| TAINTED | 1792 | 33.5 | -38.3 | +12.7 | $-8,620 |
| KEEP-only | 554 | 63.9 | +50.9 | +72.9 | $+10,181 |
| KEEP-only recent | 346 | 60.7 | +53.3 | +88.9 | $+4,924 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T10:21:09.508587-04:00","date":"2026-09-08","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":69.6,"phases_s":{"reconcile":1.48,"cancel":0.04,"manage":5.37,"protective_stops":0.69,"scan":45.99,"entries":8.49,"reconcile2":0.23},"signals":268,"placed":2,"equity":1002816.81,"open_positions":25,"pending_orders":6,"open_lots":135,"submitted_today":95,"filled_today":89,"unattributed_contracts":0,"top_signals":["S165:COIN","S164:COIN","S168:COIN","S167:COIN","S163:COIN","S350:COIN","S351:COIN","S352:COIN"],"github_run":"9332","github_run_id":"34237579707","status":"ok","data_quality":{"clean":{"n":1035,"win":50.14,"med":12.5,"avg":47.6,"pnl":15776.21},"tainted":{"n":1792,"win":33.54,"med":-38.34,"avg":12.75,"pnl":-8619.84},"keep_only":{"n":554,"win":63.9,"med":50.93,"avg":72.9,"pnl":10181.45},"keep_only_recent":{"n":346,"win":60.69,"med":53.33,"avg":88.86,"pnl":4924.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:21:05  INFO      Mode: exits
14:21:05  INFO        Daily log -> logs/daily/2026-09-08.md
14:21:05  INFO        Daily log reconciled -> logs/daily/2026-09-08.md (1 ledger rows)
14:21:05  INFO        place_all_stops: checking 2 positions...
14:21:05  INFO        STOP skipped AMCR: fractional (0.7714 shares) — software exit will handle it
14:21:05  INFO        STOP skipped APD: fractional (0.1154 shares) — software exit will handle it
14:21:05  INFO        [positions] 2/2 (2 valid)
14:21:05  INFO        Daily log -> logs/daily/2026-09-08.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.52|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMCR  P&L -0.1%  $-0.05                                           HOLD|
|  APD  P&L +0.5%  $+0.16                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
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
=== options_live_micro LIVE 2026-09-08T10:21:06.646635-04:00 share=25% ===
2026-09-08 10:21:06,646 INFO === options_live_micro LIVE 2026-09-08T10:21:06.646635-04:00 share=25% ===
Live account equity $230.52 cash $161.23 #225458845 options_level=3
2026-09-08 10:21:06,709 INFO Live account equity $230.52 cash $161.23 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-08 10:21:06,752 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-08 10:21:06,777 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (190 earlier lines - see full log file)
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 249 | 13 |
| S164 | 271 | 15 |
| S165 | 1711 | 28 |
| S166 | 135 | 9 |
| S167 | 265 | 15 |
| S168 | 198 | 13 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1052 | WARN | <<<
| Missing exit records (post) |  1050 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   135 | INFO |
| Total closed lots           |  2007 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1035 med=+12.5% | TAINTED n=1792 med=-38.3% | KEEP-only n=554 med=+50.9% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.52 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260908T142601Z

- UTC timestamp: `20260908T142601Z`
- GitHub run: [#9333](https://github.com/28twagg-ops/TradingBot/actions/runs/34238113031)
- Run id: `34238113031`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`65s`
- Full logs: `logs/action_runs/20260908T142601Z_live_bot.log`, `logs/action_runs/20260908T142601Z_live_options.log`, `logs/action_runs/20260908T142601Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1037 | 50.0 | +4.8 | +47.4 | $+15,709 |
| TAINTED | 1792 | 33.5 | -38.3 | +12.7 | $-8,620 |
| KEEP-only | 556 | 63.7 | +50.9 | +72.4 | $+10,114 |
| KEEP-only recent | 348 | 60.3 | +53.3 | +88.0 | $+4,857 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T10:26:06.077688-04:00","date":"2026-09-08","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":56.8,"phases_s":{"reconcile":0.14,"cancel":0.03,"manage":4.94,"protective_stops":0.43,"scan":35.48,"entries":5.81,"reconcile2":0.14},"signals":268,"placed":0,"equity":1002944.23,"open_positions":25,"pending_orders":6,"open_lots":133,"submitted_today":95,"filled_today":89,"unattributed_contracts":0,"top_signals":["S165:COIN","S164:COIN","S168:COIN","S167:COIN","S163:COIN","S350:COIN","S351:COIN","S352:COIN"],"github_run":"9333","github_run_id":"34238113031","status":"ok","data_quality":{"clean":{"n":1037,"win":50.05,"med":4.76,"avg":47.4,"pnl":15709.21},"tainted":{"n":1792,"win":33.54,"med":-38.34,"avg":12.75,"pnl":-8619.84},"keep_only":{"n":556,"win":63.67,"med":50.87,"avg":72.43,"pnl":10114.45},"keep_only_recent":{"n":348,"win":60.34,"med":53.33,"avg":88.02,"pnl":4857.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:26:02  INFO      Mode: exits
14:26:02  INFO        Daily log -> logs/daily/2026-09-08.md
14:26:02  INFO        Daily log reconciled -> logs/daily/2026-09-08.md (1 ledger rows)
14:26:02  INFO        place_all_stops: checking 2 positions...
14:26:02  INFO        STOP skipped AMCR: fractional (0.7714 shares) — software exit will handle it
14:26:03  INFO        STOP skipped APD: fractional (0.1154 shares) — software exit will handle it
14:26:03  INFO        [positions] 2/2 (2 valid)
14:26:03  INFO        Daily log -> logs/daily/2026-09-08.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.55|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMCR  P&L -0.3%  $-0.09                                           HOLD|
|  APD  P&L +0.7%  $+0.23                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
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
=== options_live_micro LIVE 2026-09-08T10:26:03.832169-04:00 share=25% ===
2026-09-08 10:26:03,832 INFO === options_live_micro LIVE 2026-09-08T10:26:03.832169-04:00 share=25% ===
Live account equity $230.55 cash $161.23 #225458845 options_level=3
2026-09-08 10:26:03,881 INFO Live account equity $230.55 cash $161.23 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-08 10:26:03,915 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-08 10:26:03,930 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (185 earlier lines - see full log file)
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 249 | 13 |
| S164 | 271 | 15 |
| S165 | 1711 | 28 |
| S166 | 135 | 9 |
| S167 | 265 | 15 |
| S168 | 198 | 13 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1052 | WARN | <<<
| Missing exit records (post) |  1050 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   133 | INFO |
| Total closed lots           |  2009 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1037 med=+4.8% | TAINTED n=1792 med=-38.3% | KEEP-only n=556 med=+50.9% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.55 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260908T143106Z

- UTC timestamp: `20260908T143106Z`
- GitHub run: [#9334](https://github.com/28twagg-ops/TradingBot/actions/runs/34238648408)
- Run id: `34238648408`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`86s`
- Full logs: `logs/action_runs/20260908T143106Z_live_bot.log`, `logs/action_runs/20260908T143106Z_live_options.log`, `logs/action_runs/20260908T143106Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1040 | 49.9 | +0.0 | +47.1 | $+15,642 |
| TAINTED | 1792 | 33.5 | -38.3 | +12.7 | $-8,620 |
| KEEP-only | 558 | 63.4 | +50.4 | +72.0 | $+10,049 |
| KEEP-only recent | 350 | 60.0 | +53.3 | +87.2 | $+4,792 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T10:31:11.728702-04:00","date":"2026-09-08","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":75.5,"phases_s":{"reconcile":0.25,"cancel":0.02,"manage":6.68,"protective_stops":0.83,"scan":53.58,"entries":6.78,"reconcile2":0.27},"signals":268,"placed":0,"equity":1002808.71,"open_positions":24,"pending_orders":6,"open_lots":130,"submitted_today":95,"filled_today":89,"unattributed_contracts":0,"top_signals":["S165:COIN","S164:COIN","S168:COIN","S167:COIN","S163:COIN","S350:COIN","S351:COIN","S352:COIN"],"github_run":"9334","github_run_id":"34238648408","status":"ok","data_quality":{"clean":{"n":1040,"win":49.9,"med":0.0,"avg":47.08,"pnl":15642.21},"tainted":{"n":1792,"win":33.54,"med":-38.34,"avg":12.75,"pnl":-8619.84},"keep_only":{"n":558,"win":63.44,"med":50.43,"avg":71.96,"pnl":10049.45},"keep_only_recent":{"n":350,"win":60.0,"med":53.28,"avg":87.18,"pnl":4792.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:31:07  INFO      Mode: exits
14:31:07  INFO        Daily log -> logs/daily/2026-09-08.md
14:31:07  INFO        Daily log reconciled -> logs/daily/2026-09-08.md (1 ledger rows)
14:31:07  INFO        place_all_stops: checking 2 positions...
14:31:07  INFO        STOP skipped AMCR: fractional (0.7714 shares) — software exit will handle it
14:31:07  INFO        STOP skipped APD: fractional (0.1154 shares) — software exit will handle it
14:31:07  INFO        [positions] 2/2 (2 valid)
14:31:08  INFO        Daily log -> logs/daily/2026-09-08.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.62|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMCR  P&L -0.2%  $-0.07                                           HOLD|
|  APD  P&L +0.8%  $+0.28                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
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
=== options_live_micro LIVE 2026-09-08T10:31:08.765327-04:00 share=25% ===
2026-09-08 10:31:08,765 INFO === options_live_micro LIVE 2026-09-08T10:31:08.765327-04:00 share=25% ===
Live account equity $230.62 cash $161.23 #225458845 options_level=3
2026-09-08 10:31:08,817 INFO Live account equity $230.62 cash $161.23 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-08 10:31:08,886 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-08 10:31:08,933 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (187 earlier lines - see full log file)
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 249 | 13 |
| S164 | 271 | 15 |
| S165 | 1711 | 28 |
| S166 | 135 | 9 |
| S167 | 265 | 15 |
| S168 | 198 | 13 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1052 | WARN | <<<
| Missing exit records (post) |  1050 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   130 | INFO |
| Total closed lots           |  2012 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1040 med=+0.0% | TAINTED n=1792 med=-38.3% | KEEP-only n=558 med=+50.4% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.62 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260908T143603Z

- UTC timestamp: `20260908T143603Z`
- GitHub run: [#9335](https://github.com/28twagg-ops/TradingBot/actions/runs/34239190918)
- Run id: `34239190918`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`84s`
- Full logs: `logs/action_runs/20260908T143603Z_live_bot.log`, `logs/action_runs/20260908T143603Z_live_options.log`, `logs/action_runs/20260908T143603Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1041 | 49.9 | +0.0 | +47.0 | $+15,640 |
| TAINTED | 1792 | 33.5 | -38.3 | +12.7 | $-8,620 |
| KEEP-only | 558 | 63.4 | +50.4 | +72.0 | $+10,049 |
| KEEP-only recent | 350 | 60.0 | +53.3 | +87.2 | $+4,792 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T10:36:09.721172-04:00","date":"2026-09-08","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":73.4,"phases_s":{"reconcile":0.42,"cancel":0.1,"manage":8.11,"protective_stops":1.91,"scan":45.2,"entries":15.09,"reconcile2":0.36},"signals":268,"placed":0,"equity":1002691.59,"open_positions":24,"pending_orders":4,"open_lots":131,"submitted_today":95,"filled_today":91,"unattributed_contracts":0,"top_signals":["S165:COIN","S164:COIN","S168:COIN","S167:COIN","S163:COIN","S350:COIN","S351:COIN","S352:COIN"],"github_run":"9335","github_run_id":"34239190918","status":"ok","data_quality":{"clean":{"n":1041,"win":49.86,"med":0.0,"avg":46.97,"pnl":15640.21},"tainted":{"n":1792,"win":33.54,"med":-38.34,"avg":12.75,"pnl":-8619.84},"keep_only":{"n":558,"win":63.44,"med":50.43,"avg":71.96,"pnl":10049.45},"keep_only_recent":{"n":350,"win":60.0,"med":53.28,"avg":87.18,"pnl":4792.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:36:04  INFO      Mode: exits
14:36:05  INFO        Daily log -> logs/daily/2026-09-08.md
14:36:05  INFO        Daily log reconciled -> logs/daily/2026-09-08.md (1 ledger rows)
14:36:05  INFO        place_all_stops: checking 2 positions...
14:36:05  INFO        STOP skipped AMCR: fractional (0.7714 shares) — software exit will handle it
14:36:05  INFO        STOP skipped APD: fractional (0.1154 shares) — software exit will handle it
14:36:05  INFO        [positions] 2/2 (2 valid)
14:36:05  INFO        Daily log -> logs/daily/2026-09-08.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.68|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMCR  P&L -0.1%  $-0.05                                           HOLD|
|  APD  P&L +0.9%  $+0.32                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
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
=== options_live_micro LIVE 2026-09-08T10:36:06.483942-04:00 share=25% ===
2026-09-08 10:36:06,484 INFO === options_live_micro LIVE 2026-09-08T10:36:06.483942-04:00 share=25% ===
Live account equity $230.68 cash $161.23 #225458845 options_level=3
2026-09-08 10:36:06,699 INFO Live account equity $230.68 cash $161.23 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-08 10:36:06,884 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-08 10:36:06,966 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (189 earlier lines - see full log file)
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 249 | 13 |
| S164 | 271 | 15 |
| S165 | 1711 | 28 |
| S166 | 135 | 9 |
| S167 | 265 | 15 |
| S168 | 198 | 13 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1052 | WARN | <<<
| Missing exit records (post) |  1050 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   131 | INFO |
| Total closed lots           |  2013 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1041 med=+0.0% | TAINTED n=1792 med=-38.3% | KEEP-only n=558 med=+50.4% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.68 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260908T144100Z

- UTC timestamp: `20260908T144100Z`
- GitHub run: [#9336](https://github.com/28twagg-ops/TradingBot/actions/runs/34239729586)
- Run id: `34239729586`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`81s`
- Full logs: `logs/action_runs/20260908T144100Z_live_bot.log`, `logs/action_runs/20260908T144100Z_live_options.log`, `logs/action_runs/20260908T144100Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1041 | 49.9 | +0.0 | +47.0 | $+15,640 |
| TAINTED | 1793 | 33.6 | -38.3 | +12.7 | $-8,612 |
| KEEP-only | 558 | 63.4 | +50.4 | +72.0 | $+10,049 |
| KEEP-only recent | 350 | 60.0 | +53.3 | +87.2 | $+4,792 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T10:41:08.255551-04:00","date":"2026-09-08","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":72.0,"phases_s":{"reconcile":0.5,"cancel":0.12,"manage":8.23,"protective_stops":2.41,"scan":35.8,"entries":21.46,"reconcile2":0.62},"signals":268,"placed":0,"equity":1002875.51,"open_positions":26,"pending_orders":0,"open_lots":135,"submitted_today":95,"filled_today":95,"unattributed_contracts":0,"top_signals":["S165:COIN","S164:COIN","S168:COIN","S167:COIN","S163:COIN","S350:COIN","S351:COIN","S352:COIN"],"github_run":"9336","github_run_id":"34239729586","status":"ok","data_quality":{"clean":{"n":1041,"win":49.86,"med":0.0,"avg":46.97,"pnl":15640.21},"tainted":{"n":1793,"win":33.58,"med":-38.33,"avg":12.75,"pnl":-8611.84},"keep_only":{"n":558,"win":63.44,"med":50.43,"avg":71.96,"pnl":10049.45},"keep_only_recent":{"n":350,"win":60.0,"med":53.28,"avg":87.18,"pnl":4792.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:41:01  INFO      Mode: exits
14:41:02  INFO        Daily log -> logs/daily/2026-09-08.md
14:41:02  INFO        Daily log reconciled -> logs/daily/2026-09-08.md (1 ledger rows)
14:41:02  INFO        place_all_stops: checking 2 positions...
14:41:02  INFO        STOP skipped AMCR: fractional (0.7714 shares) — software exit will handle it
14:41:02  INFO        STOP skipped APD: fractional (0.1154 shares) — software exit will handle it
14:41:03  INFO        [positions] 2/2 (2 valid)
14:41:03  INFO        Daily log -> logs/daily/2026-09-08.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.69|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMCR  P&L -0.1%  $-0.04                                           HOLD|
|  APD  P&L +0.9%  $+0.32                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
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
=== options_live_micro LIVE 2026-09-08T10:41:04.419065-04:00 share=25% ===
2026-09-08 10:41:04,419 INFO === options_live_micro LIVE 2026-09-08T10:41:04.419065-04:00 share=25% ===
Live account equity $230.69 cash $161.23 #225458845 options_level=3
2026-09-08 10:41:04,641 INFO Live account equity $230.69 cash $161.23 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-08 10:41:04,830 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-08 10:41:04,954 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (177 earlier lines - see full log file)
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 249 | 13 |
| S164 | 271 | 15 |
| S165 | 1711 | 28 |
| S166 | 135 | 9 |
| S167 | 265 | 15 |
| S168 | 198 | 13 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1052 | WARN | <<<
| Missing exit records (post) |  1050 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   135 | INFO |
| Total closed lots           |  2014 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1041 med=+0.0% | TAINTED n=1793 med=-38.3% | KEEP-only n=558 med=+50.4% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.69 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260908T144634Z

- UTC timestamp: `20260908T144634Z`
- GitHub run: [#9337](https://github.com/28twagg-ops/TradingBot/actions/runs/34240269719)
- Run id: `34240269719`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`185s`
- Full logs: `logs/action_runs/20260908T144634Z_live_bot.log`, `logs/action_runs/20260908T144634Z_live_options.log`, `logs/action_runs/20260908T144634Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1041 | 49.9 | +0.0 | +47.0 | $+15,640 |
| TAINTED | 1794 | 33.6 | -38.3 | +12.7 | $-8,647 |
| KEEP-only | 558 | 63.4 | +50.4 | +72.0 | $+10,049 |
| KEEP-only recent | 350 | 60.0 | +53.3 | +87.2 | $+4,792 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-08T10:46:42.543278-04:00","date":"2026-09-08","mode":"entry+manage","header":"entry+manage (16 new)","elapsed_s":172.5,"phases_s":{"reconcile":0.55,"cancel":0.15,"manage":9.87,"protective_stops":2.83,"scan":55.93,"entries":88.36,"reconcile2":1.04},"signals":268,"placed":16,"equity":1003030.45,"open_positions":30,"pending_orders":6,"open_lots":145,"submitted_today":111,"filled_today":105,"unattributed_contracts":0,"top_signals":["S165:COIN","S164:COIN","S168:COIN","S167:COIN","S163:COIN","S350:COIN","S351:COIN","S352:COIN"],"github_run":"9337","github_run_id":"34240269719","status":"ok","data_quality":{"clean":{"n":1041,"win":49.86,"med":0.0,"avg":46.97,"pnl":15640.21},"tainted":{"n":1794,"win":33.56,"med":-38.34,"avg":12.7,"pnl":-8646.84},"keep_only":{"n":558,"win":63.44,"med":50.43,"avg":71.96,"pnl":10049.45},"keep_only_recent":{"n":350,"win":60.0,"med":53.28,"avg":87.18,"pnl":4792.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:46:35  INFO      Mode: exits
14:46:36  INFO        Daily log -> logs/daily/2026-09-08.md
14:46:36  INFO        Daily log reconciled -> logs/daily/2026-09-08.md (1 ledger rows)
14:46:36  INFO        place_all_stops: checking 2 positions...
14:46:36  INFO        STOP skipped AMCR: fractional (0.7714 shares) — software exit will handle it
14:46:36  INFO        STOP skipped APD: fractional (0.1154 shares) — software exit will handle it
14:46:37  INFO        [positions] 2/2 (2 valid)
14:46:37  INFO        Daily log -> logs/daily/2026-09-08.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.75|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMCR  P&L +0.0%  $+0.00                                           HOLD|
|  APD  P&L +1.0%  $+0.34                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
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
=== options_live_micro LIVE 2026-09-08T10:46:38.452290-04:00 share=25% ===
2026-09-08 10:46:38,452 INFO === options_live_micro LIVE 2026-09-08T10:46:38.452290-04:00 share=25% ===
Live account equity $230.76 cash $161.23 #225458845 options_level=3
2026-09-08 10:46:38,676 INFO Live account equity $230.76 cash $161.23 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-08 10:46:38,900 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-08 10:46:39,050 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (209 earlier lines - see full log file)
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 249 | 13 |
| S164 | 271 | 15 |
| S165 | 1711 | 28 |
| S166 | 135 | 9 |
| S167 | 265 | 15 |
| S168 | 198 | 13 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1052 | WARN | <<<
| Missing exit records (post) |  1050 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   145 | INFO |
| Total closed lots           |  2015 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1041 med=+0.0% | TAINTED n=1794 med=-38.3% | KEEP-only n=558 med=+50.4% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.76 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
