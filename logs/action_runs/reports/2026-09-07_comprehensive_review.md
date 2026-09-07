# Daily Comprehensive Action Review - 2026-09-07

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260907T130108Z

- UTC timestamp: `20260907T130108Z`
- GitHub run: [#9184](https://github.com/28twagg-ops/TradingBot/actions/runs/34124926527)
- Run id: `34124926527`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260907T130108Z_live_bot.log`, `logs/action_runs/20260907T130108Z_live_options.log`, `logs/action_runs/20260907T130108Z_options_bot.log`


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
{"ts_et":"2026-09-07T09:01:13.651507-04:00","date":"2026-09-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.6,"phases_s":{"reconcile":4.67},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9184","github_run_id":"34124926527","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:01:08  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
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
|  AMZN     Pullback50      $34.99     $255.49  $258.51  +1.2%   $+0.41  |
|  FLEX     MomReversal     $34.61     $109.37  $109.51  +0.1%   $+0.04  |
|  LII      MomReversal     $34.94     $386.29  $390.53  +1.1%   $+0.38  |
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
=== options_live_micro LIVE 2026-09-07T09:01:10.216104-04:00 share=25% ===
2026-09-07 09:01:10,216 INFO === options_live_micro LIVE 2026-09-07T09:01:10.216104-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 09:01:10,412 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-07 09:01:10,467 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-07 09:01:10,520 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (163 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T130555Z

- UTC timestamp: `20260907T130555Z`
- GitHub run: [#9185](https://github.com/28twagg-ops/TradingBot/actions/runs/34125383805)
- Run id: `34125383805`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`18s`
- Full logs: `logs/action_runs/20260907T130555Z_live_bot.log`, `logs/action_runs/20260907T130555Z_live_options.log`, `logs/action_runs/20260907T130555Z_options_bot.log`


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
{"ts_et":"2026-09-07T09:06:00.454043-04:00","date":"2026-09-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.4,"phases_s":{"reconcile":4.62},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9185","github_run_id":"34125383805","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:05:56  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:05 UTC|
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
|  AMZN     Pullback50      $34.99     $255.49  $258.51  +1.2%   $+0.41  |
|  FLEX     MomReversal     $34.61     $109.37  $109.51  +0.1%   $+0.04  |
|  LII      MomReversal     $34.94     $386.29  $390.53  +1.1%   $+0.38  |
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
=== options_live_micro LIVE 2026-09-07T09:05:57.637849-04:00 share=25% ===
2026-09-07 09:05:57,637 INFO === options_live_micro LIVE 2026-09-07T09:05:57.637849-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 09:05:57,836 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-07 09:05:57,898 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-07 09:05:57,956 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (157 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T131103Z

- UTC timestamp: `20260907T131103Z`
- GitHub run: [#9186](https://github.com/28twagg-ops/TradingBot/actions/runs/34125850229)
- Run id: `34125850229`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260907T131103Z_live_bot.log`, `logs/action_runs/20260907T131103Z_live_options.log`, `logs/action_runs/20260907T131103Z_options_bot.log`


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
{"ts_et":"2026-09-07T09:11:09.940238-04:00","date":"2026-09-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.4,"phases_s":{"reconcile":4.47},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9186","github_run_id":"34125850229","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:11:05  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
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
|  AMZN     Pullback50      $34.99     $255.49  $258.51  +1.2%   $+0.41  |
|  FLEX     MomReversal     $34.61     $109.37  $109.51  +0.1%   $+0.04  |
|  LII      MomReversal     $34.94     $386.29  $390.53  +1.1%   $+0.38  |
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
=== options_live_micro LIVE 2026-09-07T09:11:06.317618-04:00 share=25% ===
2026-09-07 09:11:06,317 INFO === options_live_micro LIVE 2026-09-07T09:11:06.317618-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 09:11:06,461 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-07 09:11:06,504 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-07 09:11:06,544 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (157 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T131608Z

- UTC timestamp: `20260907T131608Z`
- GitHub run: [#9187](https://github.com/28twagg-ops/TradingBot/actions/runs/34126332809)
- Run id: `34126332809`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260907T131608Z_live_bot.log`, `logs/action_runs/20260907T131608Z_live_options.log`, `logs/action_runs/20260907T131608Z_options_bot.log`


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
{"ts_et":"2026-09-07T09:16:14.673654-04:00","date":"2026-09-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.8,"phases_s":{"reconcile":4.74},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9187","github_run_id":"34126332809","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:16:09  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
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
|  AMZN     Pullback50      $34.99     $255.49  $258.51  +1.2%   $+0.41  |
|  FLEX     MomReversal     $34.61     $109.37  $109.51  +0.1%   $+0.04  |
|  LII      MomReversal     $34.94     $386.29  $390.53  +1.1%   $+0.38  |
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
=== options_live_micro LIVE 2026-09-07T09:16:11.055228-04:00 share=25% ===
2026-09-07 09:16:11,055 INFO === options_live_micro LIVE 2026-09-07T09:16:11.055228-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 09:16:11,282 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-07 09:16:11,354 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-07 09:16:11,424 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (157 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T132101Z

- UTC timestamp: `20260907T132101Z`
- GitHub run: [#9188](https://github.com/28twagg-ops/TradingBot/actions/runs/34126807545)
- Run id: `34126807545`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260907T132101Z_live_bot.log`, `logs/action_runs/20260907T132101Z_live_options.log`, `logs/action_runs/20260907T132101Z_options_bot.log`


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
{"ts_et":"2026-09-07T09:21:05.650287-04:00","date":"2026-09-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":10.8,"phases_s":{"reconcile":4.16},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9188","github_run_id":"34126807545","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:21:02  INFO      Mode: summary

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
|  AMZN     Pullback50      $34.99     $255.49  $258.51  +1.2%   $+0.41  |
|  FLEX     MomReversal     $34.61     $109.37  $109.51  +0.1%   $+0.04  |
|  LII      MomReversal     $34.94     $386.29  $390.53  +1.1%   $+0.38  |
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
=== options_live_micro LIVE 2026-09-07T09:21:03.089122-04:00 share=25% ===
2026-09-07 09:21:03,089 INFO === options_live_micro LIVE 2026-09-07T09:21:03.089122-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 09:21:03,131 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-07 09:21:03,138 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-07 09:21:03,145 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (157 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T132603Z

- UTC timestamp: `20260907T132603Z`
- GitHub run: [#9189](https://github.com/28twagg-ops/TradingBot/actions/runs/34127273953)
- Run id: `34127273953`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260907T132603Z_live_bot.log`, `logs/action_runs/20260907T132603Z_live_options.log`, `logs/action_runs/20260907T132603Z_options_bot.log`


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
{"ts_et":"2026-09-07T09:26:09.685385-04:00","date":"2026-09-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.4,"phases_s":{"reconcile":4.4},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9189","github_run_id":"34127273953","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:26:05  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
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
|  AMZN     Pullback50      $34.99     $255.49  $258.51  +1.2%   $+0.41  |
|  FLEX     MomReversal     $34.61     $109.37  $109.51  +0.1%   $+0.04  |
|  LII      MomReversal     $34.94     $386.29  $390.53  +1.1%   $+0.38  |
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
=== options_live_micro LIVE 2026-09-07T09:26:06.358694-04:00 share=25% ===
2026-09-07 09:26:06,358 INFO === options_live_micro LIVE 2026-09-07T09:26:06.358694-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 09:26:06,505 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-07 09:26:06,545 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-07 09:26:06,588 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (157 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T133059Z

- UTC timestamp: `20260907T133059Z`
- GitHub run: [#9190](https://github.com/28twagg-ops/TradingBot/actions/runs/34127725173)
- Run id: `34127725173`
- Live bot: exit=`0`, duration=`216s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260907T133059Z_live_bot.log`, `logs/action_runs/20260907T133059Z_live_options.log`, `logs/action_runs/20260907T133059Z_options_bot.log`


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
{"ts_et":"2026-09-07T09:26:09.685385-04:00","date":"2026-09-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.4,"phases_s":{"reconcile":4.4},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9189","github_run_id":"34127273953","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:31:00  INFO      Mode: morning_prep
13:31:02  INFO        [prep_positions] 3/3 (3 valid)
13:31:02  INFO      Fetching tickers (universe=both)...
13:31:02  INFO        S&P 500: 503
13:31:02  INFO        MidCap 400: 400
13:31:02  INFO        Total: 903 tickers
13:31:03  INFO        [prep_universe] 40/900 (40 valid)
13:31:04  INFO        [prep_universe] 80/900 (80 valid)
13:31:06  INFO        [prep_universe] 120/900 (120 valid)
13:31:07  INFO        [prep_universe] 160/900 (160 valid)
13:31:09  INFO        [prep_universe] 200/900 (199 valid)
13:31:16  INFO        [prep_universe] 240/900 (238 valid)
13:31:27  INFO        [prep_universe] 280/900 (278 valid)
13:31:40  INFO        [prep_universe] 320/900 (318 valid)
13:31:53  INFO        [prep_universe] 360/900 (358 valid)
13:32:04  INFO        [prep_universe] 400/900 (397 valid)
13:32:17  INFO        [prep_universe] 440/900 (437 valid)
13:32:27  INFO        [prep_universe] 480/900 (477 valid)
13:32:41  INFO        [prep_universe] 520/900 (517 valid)
13:32:51  INFO        [prep_universe] 560/900 (557 valid)
13:33:04  INFO        [prep_universe] 600/900 (597 valid)
13:33:15  INFO        [prep_universe] 640/900 (637 valid)
13:33:28  INFO        [prep_universe] 680/900 (677 valid)
13:33:38  INFO        [prep_universe] 720/900 (717 valid)
13:33:52  INFO        [prep_universe] 760/900 (757 valid)
13:34:05  INFO        [prep_universe] 800/900 (797 valid)
13:34:15  INFO        [prep_universe] 840/900 (837 valid)
13:34:29  INFO        [prep_universe] 880/900 (877 valid)
13:34:32  INFO        [prep_universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
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
|  Invested                                                       $104.54|
|  Open P&L                                                        $+0.83|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $34.99     $255.49  $258.51  +1.2%   $+0.41  |
|  FLEX     MomReversal     $34.61     $109.37  $109.51  +0.1%   $+0.04  |
|  LII      MomReversal     $34.94     $386.29  $390.53  +1.1%   $+0.38  |
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
|  Signal candidates                                                   90|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-07T09:34:36.297951-04:00 share=25% ===
2026-09-07 09:34:36,298 INFO === options_live_micro LIVE 2026-09-07T09:34:36.297951-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 09:34:36,526 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-07 09:34:36,733 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-07 09:34:36,871 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=121 paper_keys=yes dry_run=False
  alpaca positions=31
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE FAIL: {"code":50010000,"message":"internal server error occurred"}
paper probe failed (non-fatal)
=== options_morning_bot (PAPER) 2026-09-07T09:34:39.775672-04:00 ===

[Run context]
2026-09-07 09:34:40,001 WARNING paper get_account failed attempt 1/3 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 2s
2026-09-07 09:34:42,121 WARNING paper get_account failed attempt 2/3 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 4s
2026-09-07 09:34:46,208 ERROR paper get_account failed after 3 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=31). Keys are fine; Alpaca account endpoint is flaky. Using cached equity $1005125.39.
2026-09-07 09:34:46,355 WARNING paper get_account failed attempt 1/2 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 2s
2026-09-07 09:34:48,429 ERROR paper get_account failed after 2 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: using cached paper equity $1005125.39 (get_account: {"code":50010000,"message":"internal server error occurred"})
2026-09-07 09:34:48,536 WARNING lab get_account failed attempt 1/2: {"code":50010000,"message":"internal server error occurred"}
2026-09-07 09:34:50,607 ERROR lab get_account failed after 2 attempts: {"code":50010000,"message":"internal server error occurred"}

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b20|lab0020_s202_w3_1045_1120_r1|S202] stop_loss (-68.8%) SELL failed PATH260911C00016500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 upgraded=0 already=23 failed=6 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260907T133626Z

- UTC timestamp: `20260907T133626Z`
- GitHub run: [#9191](https://github.com/28twagg-ops/TradingBot/actions/runs/34128195676)
- Run id: `34128195676`
- Live bot: exit=`0`, duration=`215s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260907T133626Z_live_bot.log`, `logs/action_runs/20260907T133626Z_live_options.log`, `logs/action_runs/20260907T133626Z_options_bot.log`


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
{"ts_et":"2026-09-07T09:26:09.685385-04:00","date":"2026-09-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.4,"phases_s":{"reconcile":4.4},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9189","github_run_id":"34127273953","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:36:27  INFO      Mode: morning_prep
13:36:27  INFO        [prep_positions] 3/3 (3 valid)
13:36:27  INFO      Fetching tickers (universe=both)...
13:36:27  INFO        S&P 500: 503
13:36:27  INFO        MidCap 400: 400
13:36:27  INFO        Total: 903 tickers
13:36:28  INFO        [prep_universe] 40/900 (40 valid)
13:36:30  INFO        [prep_universe] 80/900 (80 valid)
13:36:31  INFO        [prep_universe] 120/900 (120 valid)
13:36:33  INFO        [prep_universe] 160/900 (160 valid)
13:36:34  INFO        [prep_universe] 200/900 (199 valid)
13:36:41  INFO        [prep_universe] 240/900 (238 valid)
13:36:54  INFO        [prep_universe] 280/900 (278 valid)
13:37:07  INFO        [prep_universe] 320/900 (318 valid)
13:37:17  INFO        [prep_universe] 360/900 (358 valid)
13:37:29  INFO        [prep_universe] 400/900 (397 valid)
13:37:42  INFO        [prep_universe] 440/900 (437 valid)
13:37:52  INFO        [prep_universe] 480/900 (477 valid)
13:38:05  INFO        [prep_universe] 520/900 (517 valid)
13:38:18  INFO        [prep_universe] 560/900 (557 valid)
13:38:28  INFO        [prep_universe] 600/900 (597 valid)
13:38:41  INFO        [prep_universe] 640/900 (637 valid)
13:38:54  INFO        [prep_universe] 680/900 (677 valid)
13:39:07  INFO        [prep_universe] 720/900 (717 valid)
13:39:17  INFO        [prep_universe] 760/900 (757 valid)
13:39:30  INFO        [prep_universe] 800/900 (797 valid)
13:39:43  INFO        [prep_universe] 840/900 (837 valid)
13:39:53  INFO        [prep_universe] 880/900 (877 valid)
13:39:59  INFO        [prep_universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
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
|  Invested                                                       $104.54|
|  Open P&L                                                        $+0.83|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $34.99     $255.49  $258.51  +1.2%   $+0.41  |
|  FLEX     MomReversal     $34.61     $109.37  $109.51  +0.1%   $+0.04  |
|  LII      MomReversal     $34.94     $386.29  $390.53  +1.1%   $+0.38  |
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
|  Signal candidates                                                   90|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-07T09:40:02.469787-04:00 share=25% ===
2026-09-07 09:40:02,469 INFO === options_live_micro LIVE 2026-09-07T09:40:02.469787-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 09:40:02,518 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-07 09:40:02,547 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-07 09:40:02,564 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=121 paper_keys=yes dry_run=False
  alpaca positions=31
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE FAIL: {"code":50010000,"message":"internal server error occurred"}
paper probe failed (non-fatal)
=== options_morning_bot (PAPER) 2026-09-07T09:40:05.410524-04:00 ===

[Run context]
2026-09-07 09:40:05,458 WARNING paper get_account failed attempt 1/3 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 2s
2026-09-07 09:40:07,468 WARNING paper get_account failed attempt 2/3 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 4s
2026-09-07 09:40:11,482 ERROR paper get_account failed after 3 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=31). Keys are fine; Alpaca account endpoint is flaky. Using cached equity $1005125.39.
2026-09-07 09:40:11,506 WARNING paper get_account failed attempt 1/2 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 2s
2026-09-07 09:40:13,525 ERROR paper get_account failed after 2 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: using cached paper equity $1005125.39 (get_account: {"code":50010000,"message":"internal server error occurred"})
2026-09-07 09:40:13,574 WARNING lab get_account failed attempt 1/2: {"code":50010000,"message":"internal server error occurred"}
2026-09-07 09:40:15,587 ERROR lab get_account failed after 2 attempts: {"code":50010000,"message":"internal server error occurred"}

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
```

---

## Run 20260907T134129Z

- UTC timestamp: `20260907T134129Z`
- GitHub run: [#9192](https://github.com/28twagg-ops/TradingBot/actions/runs/34128664028)
- Run id: `34128664028`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260907T134129Z_live_bot.log`, `logs/action_runs/20260907T134129Z_live_options.log`, `logs/action_runs/20260907T134129Z_options_bot.log`


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
{"ts_et":"2026-09-07T09:26:09.685385-04:00","date":"2026-09-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.4,"phases_s":{"reconcile":4.4},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9189","github_run_id":"34127273953","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:41:30  INFO      Mode: morning_prep
13:41:31  INFO        [prep_positions] 3/3 (3 valid)
13:41:31  INFO        Universe cache hit: 903 tickers (tickers_2026-09-07.json)
13:41:32  INFO        [prep_universe] 40/900 (40 valid)
13:41:34  INFO        [prep_universe] 80/900 (80 valid)
13:41:35  INFO        [prep_universe] 120/900 (120 valid)
13:41:36  INFO        [prep_universe] 160/900 (160 valid)
13:41:37  INFO        [prep_universe] 200/900 (199 valid)
13:41:45  INFO        [prep_universe] 240/900 (238 valid)
13:41:58  INFO        [prep_universe] 280/900 (278 valid)
13:42:08  INFO        [prep_universe] 320/900 (318 valid)
13:42:22  INFO        [prep_universe] 360/900 (358 valid)
13:42:32  INFO        [prep_universe] 400/900 (397 valid)
13:42:46  INFO        [prep_universe] 440/900 (437 valid)
13:42:59  INFO        [prep_universe] 480/900 (477 valid)
13:43:09  INFO        [prep_universe] 520/900 (517 valid)
13:43:22  INFO        [prep_universe] 560/900 (557 valid)
13:43:33  INFO        [prep_universe] 600/900 (597 valid)
13:43:46  INFO        [prep_universe] 640/900 (637 valid)
13:43:56  INFO        [prep_universe] 680/900 (677 valid)
13:44:10  INFO        [prep_universe] 720/900 (717 valid)
13:44:23  INFO        [prep_universe] 760/900 (757 valid)
13:44:33  INFO        [prep_universe] 800/900 (797 valid)
13:44:46  INFO        [prep_universe] 840/900 (837 valid)
13:44:57  INFO        [prep_universe] 880/900 (877 valid)
13:45:04  INFO        [prep_universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
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
|  Invested                                                       $104.54|
|  Open P&L                                                        $+0.83|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $34.99     $255.49  $258.51  +1.2%   $+0.41  |
|  FLEX     MomReversal     $34.61     $109.37  $109.51  +0.1%   $+0.04  |
|  LII      MomReversal     $34.94     $386.29  $390.53  +1.1%   $+0.38  |
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
|  Signal candidates                                                   90|
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

## Run 20260907T134626Z

- UTC timestamp: `20260907T134626Z`
- GitHub run: [#9193](https://github.com/28twagg-ops/TradingBot/actions/runs/34129133752)
- Run id: `34129133752`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260907T134626Z_live_bot.log`, `logs/action_runs/20260907T134626Z_live_options.log`, `logs/action_runs/20260907T134626Z_options_bot.log`


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
{"ts_et":"2026-09-07T09:26:09.685385-04:00","date":"2026-09-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.4,"phases_s":{"reconcile":4.4},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9189","github_run_id":"34127273953","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:46:27  INFO      Mode: morning_scan
13:46:28  INFO        [positions] 3/3 (3 valid)
13:46:28  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=6e61ecb8-b4e9-452f-aa01-1aa34e1f863e
13:46:49  INFO        SELL LIMIT not filled for FLEX, falling back to market
13:46:49  INFO        SELL MARKET FLEX closed
13:46:52  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=d3e3312f-1cf8-4ef7-8a4a-f746674a04a6
13:47:12  INFO        SELL LIMIT not filled for LII, falling back to market
13:47:12  INFO        SELL MARKET LII closed
13:47:15  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=ffeda294-8513-442a-9471-07909aeaca29
13:47:35  INFO        SELL LIMIT not filled for AMZN, falling back to market
13:47:35  INFO        SELL MARKET AMZN closed
13:47:38  INFO        Universe cache hit: 903 tickers (tickers_2026-09-07.json)
13:47:39  INFO        [universe] 40/900 (40 valid)
13:47:40  INFO        [universe] 80/900 (80 valid)
13:47:41  INFO        [universe] 120/900 (120 valid)
13:47:43  INFO        [universe] 160/900 (160 valid)
13:47:44  INFO        [universe] 200/900 (199 valid)
13:47:51  INFO        [universe] 240/900 (238 valid)
13:48:05  INFO        [universe] 280/900 (278 valid)
13:48:15  INFO        [universe] 320/900 (318 valid)
13:48:28  INFO        [universe] 360/900 (358 valid)
13:48:38  INFO        [universe] 400/900 (397 valid)
13:48:52  INFO        [universe] 440/900 (437 valid)
13:49:02  INFO        [universe] 480/900 (477 valid)
13:49:15  INFO        [universe] 520/900 (517 valid)
13:49:29  INFO        [universe] 560/900 (557 valid)
13:49:39  INFO        [universe] 600/900 (597 valid)
13:49:52  INFO        [universe] 640/900 (637 valid)
13:50:03  INFO        [universe] 680/900 (677 valid)
13:50:16  INFO        [universe] 720/900 (717 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260907T135139Z

- UTC timestamp: `20260907T135139Z`
- GitHub run: [#9194](https://github.com/28twagg-ops/TradingBot/actions/runs/34129605523)
- Run id: `34129605523`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260907T135139Z_live_bot.log`, `logs/action_runs/20260907T135139Z_live_options.log`, `logs/action_runs/20260907T135139Z_options_bot.log`


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
{"ts_et":"2026-09-07T09:26:09.685385-04:00","date":"2026-09-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.4,"phases_s":{"reconcile":4.4},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9189","github_run_id":"34127273953","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:51:42  INFO      Mode: morning_scan
13:51:43  INFO        [positions] 3/3 (3 valid)
13:51:43  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=fce5036e-87cf-4f61-88c2-9fff60cd2d67
13:51:43  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=a84fc78a-7e4b-4cd5-9ae9-44bf5cf54c53
13:52:03  INFO        SELL LIMIT not filled for FLEX, falling back to market
13:52:03  INFO        SELL MARKET FLEX closed
13:52:06  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=add6c6be-ec55-48a5-a1f7-d895e0c2c9f8
13:52:06  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=a8800010-0bf8-42cb-a89d-2ff43df57112
13:52:26  INFO        SELL LIMIT not filled for LII, falling back to market
13:52:26  INFO        SELL MARKET LII closed
13:52:28  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=d4d909db-5f04-4245-b5c6-e63ef6f7b159
13:52:29  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=9a7093ff-7468-4a94-969a-19e568fbbfa6
13:52:49  INFO        SELL LIMIT not filled for AMZN, falling back to market
13:52:49  INFO        SELL MARKET AMZN closed
13:52:51  INFO        Universe cache hit: 903 tickers (tickers_2026-09-07.json)
13:52:52  INFO        [universe] 40/900 (40 valid)
13:52:53  INFO        [universe] 80/900 (80 valid)
13:52:54  INFO        [universe] 120/900 (120 valid)
13:52:55  INFO        [universe] 160/900 (160 valid)
13:52:57  INFO        [universe] 200/900 (199 valid)
13:53:04  INFO        [universe] 240/900 (238 valid)
13:53:17  INFO        [universe] 280/900 (278 valid)
13:53:30  INFO        [universe] 320/900 (318 valid)
13:53:40  INFO        [universe] 360/900 (358 valid)
13:53:53  INFO        [universe] 400/900 (397 valid)
13:54:06  INFO        [universe] 440/900 (437 valid)
13:54:16  INFO        [universe] 480/900 (477 valid)
13:54:29  INFO        [universe] 520/900 (517 valid)
13:54:42  INFO        [universe] 560/900 (557 valid)
13:54:52  INFO        [universe] 600/900 (597 valid)
13:55:05  INFO        [universe] 640/900 (637 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260907T135627Z

- UTC timestamp: `20260907T135627Z`
- GitHub run: [#9195](https://github.com/28twagg-ops/TradingBot/actions/runs/34130061801)
- Run id: `34130061801`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260907T135627Z_live_bot.log`, `logs/action_runs/20260907T135627Z_live_options.log`, `logs/action_runs/20260907T135627Z_options_bot.log`


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
{"ts_et":"2026-09-07T09:26:09.685385-04:00","date":"2026-09-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.4,"phases_s":{"reconcile":4.4},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9189","github_run_id":"34127273953","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:56:28  INFO      Mode: morning_scan
13:56:29  INFO        [positions] 3/3 (3 valid)
13:56:29  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=b2639ab7-a562-4203-983b-79af98e3a1b5
13:56:29  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=5d9c0711-30ba-4f01-ab00-a7821ce9240c
13:56:50  INFO        SELL LIMIT not filled for FLEX, falling back to market
13:56:50  INFO        SELL MARKET FLEX closed
13:56:52  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=24abc6d1-219c-4a22-93aa-426be7af75e5
13:56:52  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=6e8f22b1-8d20-41f7-a8a4-684673027c16
13:57:13  INFO        SELL LIMIT not filled for LII, falling back to market
13:57:13  INFO        SELL MARKET LII closed
13:57:15  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=17720d00-91a8-475f-bbf0-b501c3c9fe70
13:57:15  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=13caeaf6-defd-42ef-9265-d8390d7835e6
13:57:35  INFO        SELL LIMIT not filled for AMZN, falling back to market
13:57:35  INFO        SELL MARKET AMZN closed
13:57:38  INFO        Universe cache hit: 903 tickers (tickers_2026-09-07.json)
13:57:39  INFO        [universe] 40/900 (40 valid)
13:57:40  INFO        [universe] 80/900 (80 valid)
13:57:42  INFO        [universe] 120/900 (120 valid)
13:57:43  INFO        [universe] 160/900 (160 valid)
13:57:44  INFO        [universe] 200/900 (199 valid)
13:57:52  INFO        [universe] 240/900 (238 valid)
13:58:05  INFO        [universe] 280/900 (278 valid)
13:58:15  INFO        [universe] 320/900 (318 valid)
13:58:28  INFO        [universe] 360/900 (358 valid)
13:58:39  INFO        [universe] 400/900 (397 valid)
13:58:52  INFO        [universe] 440/900 (437 valid)
13:59:05  INFO        [universe] 480/900 (477 valid)
13:59:15  INFO        [universe] 520/900 (517 valid)
13:59:28  INFO        [universe] 560/900 (557 valid)
13:59:39  INFO        [universe] 600/900 (597 valid)
13:59:52  INFO        [universe] 640/900 (637 valid)
14:00:02  INFO        [universe] 680/900 (677 valid)
14:00:15  INFO        [universe] 720/900 (717 valid)
14:00:28  INFO        [universe] 760/900 (757 valid)
14:00:39  INFO        [universe] 800/900 (797 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260907T140201Z

- UTC timestamp: `20260907T140201Z`
- GitHub run: [#9196](https://github.com/28twagg-ops/TradingBot/actions/runs/34130507185)
- Run id: `34130507185`
- Live bot: exit=`0`, duration=`69s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`79s`
- Full logs: `logs/action_runs/20260907T140201Z_live_bot.log`, `logs/action_runs/20260907T140201Z_live_options.log`, `logs/action_runs/20260907T140201Z_options_bot.log`


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
{"ts_et":"2026-09-07T10:03:13.865246-04:00","date":"2026-09-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":68.8,"phases_s":{"reconcile":2.21,"cancel":0.05,"manage":5.76,"protective_stops":1.26,"scan":50.83,"entries":0.03},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9196","github_run_id":"34130507185","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:02:02  INFO      Mode: exits
14:02:02  INFO        place_all_stops: checking 3 positions...
14:02:02  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:02:02  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
14:02:02  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:02:02  INFO        [positions] 3/3 (3 valid)
14:02:02  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=9a47d867-3908-4979-8f2c-331ae4af26e9
14:02:03  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=4eed49b2-4b06-4b2d-b51c-ef3c5d3f95a5
14:02:23  INFO        SELL LIMIT not filled for FLEX, falling back to market
14:02:23  INFO        SELL MARKET FLEX closed
14:02:25  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=ab182056-682a-455f-a6e6-969ebac95124
14:02:25  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=e43dc8fd-84ab-44ef-a921-48584e37c7e9
14:02:45  INFO        SELL LIMIT not filled for LII, falling back to market
14:02:45  INFO        SELL MARKET LII closed
14:02:47  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=ca651d37-4b55-4785-9c91-a4fc7a505733
14:02:47  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=437c0f6e-8511-4896-8b03-ef8403d73663
14:03:07  INFO        SELL LIMIT not filled for AMZN, falling back to market
14:03:07  INFO        SELL MARKET AMZN closed
14:03:10  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:02 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T10:03:10.782278-04:00 share=25% ===
2026-09-07 10:03:10,782 INFO === options_live_micro LIVE 2026-09-07T10:03:10.782278-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 10:03:10,866 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-07 10:03:10,931 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-07 10:03:10,973 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T140601Z

- UTC timestamp: `20260907T140601Z`
- GitHub run: [#9197](https://github.com/28twagg-ops/TradingBot/actions/runs/34130977712)
- Run id: `34130977712`
- Live bot: exit=`0`, duration=`71s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`68s`
- Full logs: `logs/action_runs/20260907T140601Z_live_bot.log`, `logs/action_runs/20260907T140601Z_live_options.log`, `logs/action_runs/20260907T140601Z_options_bot.log`


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
{"ts_et":"2026-09-07T10:07:15.481802-04:00","date":"2026-09-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":59.3,"phases_s":{"reconcile":2.51,"cancel":0.12,"manage":8.75,"protective_stops":3.22,"scan":35.72,"entries":0.07},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9197","github_run_id":"34130977712","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:06:01  INFO      Mode: exits
14:06:02  INFO        place_all_stops: checking 3 positions...
14:06:02  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:06:02  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
14:06:02  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:06:03  INFO        [positions] 3/3 (3 valid)
14:06:03  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=71ae8648-fcb1-4cf1-af28-d359570530b1
14:06:03  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=64a2c122-f620-4abe-9662-e9218478c145
14:06:23  INFO        SELL LIMIT not filled for FLEX, falling back to market
14:06:23  INFO        SELL MARKET FLEX closed
14:06:26  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=5829566b-1860-4ebe-bf80-7c859c5e2128
14:06:26  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=37b6e967-4797-4e90-9ba8-f859b79d66f0
14:06:46  INFO        SELL LIMIT not filled for LII, falling back to market
14:06:46  INFO        SELL MARKET LII closed
14:06:48  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=3a13858c-f577-4d2a-9ed1-13e66578e932
14:06:49  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=60468ac1-17db-4cf1-987d-6edfa83b9c63
14:07:09  INFO        SELL LIMIT not filled for AMZN, falling back to market
14:07:09  INFO        SELL MARKET AMZN closed
14:07:12  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T10:07:12.644932-04:00 share=25% ===
2026-09-07 10:07:12,644 INFO === options_live_micro LIVE 2026-09-07T10:07:12.644932-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 10:07:12,844 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-07 10:07:13,026 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-07 10:07:13,145 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T141100Z

- UTC timestamp: `20260907T141100Z`
- GitHub run: [#9198](https://github.com/28twagg-ops/TradingBot/actions/runs/34131444325)
- Run id: `34131444325`
- Live bot: exit=`0`, duration=`71s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`55s`
- Full logs: `logs/action_runs/20260907T141100Z_live_bot.log`, `logs/action_runs/20260907T141100Z_live_options.log`, `logs/action_runs/20260907T141100Z_options_bot.log`


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
{"ts_et":"2026-09-07T10:12:14.183853-04:00","date":"2026-09-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":48.0,"phases_s":{"reconcile":2.46,"cancel":0.12,"manage":8.85,"protective_stops":3.22,"scan":24.43,"entries":0.06},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9198","github_run_id":"34131444325","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:11:01  INFO      Mode: exits
14:11:01  INFO        place_all_stops: checking 3 positions...
14:11:01  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:11:01  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
14:11:01  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:11:02  INFO        [positions] 3/3 (3 valid)
14:11:02  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=964beffd-1b54-4b6b-809c-5bd009af4f08
14:11:02  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=11186296-c954-45c8-8962-bb83e6bf038c
14:11:22  INFO        SELL LIMIT not filled for FLEX, falling back to market
14:11:22  INFO        SELL MARKET FLEX closed
14:11:25  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=4fd40f7b-ecf9-4bea-a143-81f901f538f6
14:11:25  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=271a38d6-2e8e-43d0-afc0-bfa29787e9b3
14:11:45  INFO        SELL LIMIT not filled for LII, falling back to market
14:11:45  INFO        SELL MARKET LII closed
14:11:47  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=912e8400-7b05-465a-b0ec-52018968b66b
14:11:48  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=6c33c594-350d-4469-b8d2-e58d4d5615f7
14:12:08  INFO        SELL LIMIT not filled for AMZN, falling back to market
14:12:08  INFO        SELL MARKET AMZN closed
14:12:10  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T10:12:11.552296-04:00 share=25% ===
2026-09-07 10:12:11,552 INFO === options_live_micro LIVE 2026-09-07T10:12:11.552296-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 10:12:11,746 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-07 10:12:11,927 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-07 10:12:12,053 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T141557Z

- UTC timestamp: `20260907T141557Z`
- GitHub run: [#9199](https://github.com/28twagg-ops/TradingBot/actions/runs/34131920779)
- Run id: `34131920779`
- Live bot: exit=`0`, duration=`71s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`67s`
- Full logs: `logs/action_runs/20260907T141557Z_live_bot.log`, `logs/action_runs/20260907T141557Z_live_options.log`, `logs/action_runs/20260907T141557Z_options_bot.log`


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
{"ts_et":"2026-09-07T10:17:11.874774-04:00","date":"2026-09-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":58.4,"phases_s":{"reconcile":2.43,"cancel":0.11,"manage":8.89,"protective_stops":3.04,"scan":34.96,"entries":0.05},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9199","github_run_id":"34131920779","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:15:58  INFO      Mode: exits
14:15:59  INFO        place_all_stops: checking 3 positions...
14:15:59  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:15:59  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
14:15:59  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:15:59  INFO        [positions] 3/3 (3 valid)
14:15:59  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=e173c743-dfdd-4758-ae73-9a0686e7579c
14:15:59  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=173c8c96-d4f9-4250-b695-f3d76a2c5273
14:16:20  INFO        SELL LIMIT not filled for FLEX, falling back to market
14:16:20  INFO        SELL MARKET FLEX closed
14:16:22  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=47669d81-d9db-4610-b079-387d24ca831f
14:16:22  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=669c54cc-df22-4d90-8dfa-cf82dd23c314
14:16:43  INFO        SELL LIMIT not filled for LII, falling back to market
14:16:43  INFO        SELL MARKET LII closed
14:16:45  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=eeba874c-769a-44ac-8bac-d7363cc41f2d
14:16:45  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=3b84e1d1-8825-4458-9eab-a338464dd458
14:17:05  INFO        SELL LIMIT not filled for AMZN, falling back to market
14:17:06  INFO        SELL MARKET AMZN closed
14:17:08  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T10:17:09.122566-04:00 share=25% ===
2026-09-07 10:17:09,122 INFO === options_live_micro LIVE 2026-09-07T10:17:09.122566-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 10:17:09,317 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-07 10:17:09,478 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-07 10:17:09,586 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T142100Z

- UTC timestamp: `20260907T142100Z`
- GitHub run: [#9200](https://github.com/28twagg-ops/TradingBot/actions/runs/34132375691)
- Run id: `34132375691`
- Live bot: exit=`0`, duration=`68s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`73s`
- Full logs: `logs/action_runs/20260907T142100Z_live_bot.log`, `logs/action_runs/20260907T142100Z_live_options.log`, `logs/action_runs/20260907T142100Z_options_bot.log`


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
{"ts_et":"2026-09-07T10:22:11.935210-04:00","date":"2026-09-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":62.2,"phases_s":{"reconcile":2.15,"cancel":0.03,"manage":5.45,"protective_stops":0.81,"scan":45.14,"entries":0.01},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9200","github_run_id":"34132375691","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:21:01  INFO      Mode: exits
14:21:01  INFO        place_all_stops: checking 3 positions...
14:21:01  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:21:01  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
14:21:01  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:21:01  INFO        [positions] 3/3 (3 valid)
14:21:01  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=c89d6f17-3a98-4a44-bc74-88889d1d3ba4
14:21:01  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=aa7d49c6-f582-411d-ba8b-8f78401043b5
14:21:21  INFO        SELL LIMIT not filled for FLEX, falling back to market
14:21:21  INFO        SELL MARKET FLEX closed
14:21:23  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=8b549bf4-447a-4bab-a937-784af4ddbc8f
14:21:23  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=37f722a9-a3d6-4578-9ccc-52403109b648
14:21:44  INFO        SELL LIMIT not filled for LII, falling back to market
14:21:44  INFO        SELL MARKET LII closed
14:21:46  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=9070e648-d3af-4179-9b0c-785356b88b9c
14:21:46  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=ab6282ab-6b25-4bfe-bf5e-7de03840c79c
14:22:06  INFO        SELL LIMIT not filled for AMZN, falling back to market
14:22:06  INFO        SELL MARKET AMZN closed
14:22:08  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T10:22:09.183512-04:00 share=25% ===
2026-09-07 10:22:09,183 INFO === options_live_micro LIVE 2026-09-07T10:22:09.183512-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 10:22:09,242 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-07 10:22:09,285 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-07 10:22:09,308 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T142600Z

- UTC timestamp: `20260907T142600Z`
- GitHub run: [#9201](https://github.com/28twagg-ops/TradingBot/actions/runs/34132826671)
- Run id: `34132826671`
- Live bot: exit=`0`, duration=`71s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`81s`
- Full logs: `logs/action_runs/20260907T142600Z_live_bot.log`, `logs/action_runs/20260907T142600Z_live_options.log`, `logs/action_runs/20260907T142600Z_options_bot.log`


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
{"ts_et":"2026-09-07T10:27:15.234261-04:00","date":"2026-09-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":69.6,"phases_s":{"reconcile":2.47,"cancel":0.11,"manage":9.18,"protective_stops":3.0,"scan":45.79,"entries":0.06},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9201","github_run_id":"34132826671","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:26:01  INFO      Mode: exits
14:26:01  INFO        place_all_stops: checking 3 positions...
14:26:01  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:26:01  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
14:26:01  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:26:02  INFO        [positions] 3/3 (3 valid)
14:26:02  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=764e48ec-8899-4798-b29b-565b284579a2
14:26:02  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=ef942551-cf81-406a-a5c5-4b1b8d5d4fbc
14:26:22  INFO        SELL LIMIT not filled for FLEX, falling back to market
14:26:22  INFO        SELL MARKET FLEX closed
14:26:25  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=63280529-772c-4302-9b25-2adde40e4221
14:26:25  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=5c164129-8f63-4e56-bd07-1b2c19e05073
14:26:45  INFO        SELL LIMIT not filled for LII, falling back to market
14:26:45  INFO        SELL MARKET LII closed
14:26:47  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=38e8b6b7-754e-472a-958e-f73b337198b4
14:26:48  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=6cdd8a78-c232-49ad-be75-db6e58848845
14:27:08  INFO        SELL LIMIT not filled for AMZN, falling back to market
14:27:08  INFO        SELL MARKET AMZN closed
14:27:11  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T10:27:11.846861-04:00 share=25% ===
2026-09-07 10:27:11,846 INFO === options_live_micro LIVE 2026-09-07T10:27:11.846861-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 10:27:12,069 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-07 10:27:12,250 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-07 10:27:12,368 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T143100Z

- UTC timestamp: `20260907T143100Z`
- GitHub run: [#9202](https://github.com/28twagg-ops/TradingBot/actions/runs/34133281570)
- Run id: `34133281570`
- Live bot: exit=`0`, duration=`68s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`72s`
- Full logs: `logs/action_runs/20260907T143100Z_live_bot.log`, `logs/action_runs/20260907T143100Z_live_options.log`, `logs/action_runs/20260907T143100Z_options_bot.log`


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
{"ts_et":"2026-09-07T10:32:12.630624-04:00","date":"2026-09-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":61.7,"phases_s":{"reconcile":2.14,"cancel":0.03,"manage":5.31,"protective_stops":0.78,"scan":44.81,"entries":0.02},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9202","github_run_id":"34133281570","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:31:02  INFO      Mode: exits
14:31:02  INFO        place_all_stops: checking 3 positions...
14:31:02  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:31:02  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
14:31:02  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:31:02  INFO        [positions] 3/3 (3 valid)
14:31:02  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=c9b74527-af24-4c45-b5f6-b225f8bdbb96
14:31:02  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=bf030943-f1a2-4cf3-bc8c-17a0e8af8fe6
14:31:22  INFO        SELL LIMIT not filled for FLEX, falling back to market
14:31:22  INFO        SELL MARKET FLEX closed
14:31:24  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=8f4d103b-5243-460f-9258-d6d200d62f9c
14:31:24  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=565efdce-6dd0-4a25-8764-d06073f64a47
14:31:44  INFO        SELL LIMIT not filled for LII, falling back to market
14:31:44  INFO        SELL MARKET LII closed
14:31:46  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=d2cb39fc-03c1-4bff-b4a2-77b36148a8e8
14:31:46  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=9d97f57e-6e39-4593-9c76-b5ed06b60026
14:32:06  INFO        SELL LIMIT not filled for AMZN, falling back to market
14:32:06  INFO        SELL MARKET AMZN closed
14:32:09  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T10:32:09.870732-04:00 share=25% ===
2026-09-07 10:32:09,870 INFO === options_live_micro LIVE 2026-09-07T10:32:09.870732-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 10:32:09,933 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-07 10:32:09,968 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-07 10:32:09,990 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T143556Z

- UTC timestamp: `20260907T143556Z`
- GitHub run: [#9203](https://github.com/28twagg-ops/TradingBot/actions/runs/34133739499)
- Run id: `34133739499`
- Live bot: exit=`0`, duration=`69s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`75s`
- Full logs: `logs/action_runs/20260907T143556Z_live_bot.log`, `logs/action_runs/20260907T143556Z_live_options.log`, `logs/action_runs/20260907T143556Z_options_bot.log`


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
{"ts_et":"2026-09-07T10:37:09.161274-04:00","date":"2026-09-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":63.5,"phases_s":{"reconcile":2.24,"cancel":0.06,"manage":6.31,"protective_stops":1.53,"scan":44.64,"entries":0.03},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9203","github_run_id":"34133739499","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:35:57  INFO      Mode: exits
14:35:58  INFO        place_all_stops: checking 3 positions...
14:35:58  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:35:58  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
14:35:58  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:35:58  INFO        [positions] 3/3 (3 valid)
14:35:58  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=99b24084-ee06-4dd5-9487-5db521219022
14:35:58  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=2df58455-3778-4d34-8341-bafd61e1dac1
14:36:18  INFO        SELL LIMIT not filled for FLEX, falling back to market
14:36:18  INFO        SELL MARKET FLEX closed
14:36:20  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=f2c69caa-39ac-4f7d-8e84-6f1334f5e8c0
14:36:20  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=9b9d6230-7bf9-400d-9a07-5a385531e5db
14:36:40  INFO        SELL LIMIT not filled for LII, falling back to market
14:36:40  INFO        SELL MARKET LII closed
14:36:43  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=4cf8d64e-3e6d-4190-a7e5-de5440f4ed6d
14:36:43  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=229be6f4-f25e-4d70-bce0-c90215cb4435
14:37:03  INFO        SELL LIMIT not filled for AMZN, falling back to market
14:37:03  INFO        SELL MARKET AMZN closed
14:37:05  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T10:37:06.325903-04:00 share=25% ===
2026-09-07 10:37:06,325 INFO === options_live_micro LIVE 2026-09-07T10:37:06.325903-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 10:37:06,423 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-07 10:37:06,506 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-07 10:37:06,556 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T144103Z

- UTC timestamp: `20260907T144103Z`
- GitHub run: [#9204](https://github.com/28twagg-ops/TradingBot/actions/runs/34134198477)
- Run id: `34134198477`
- Live bot: exit=`0`, duration=`69s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`74s`
- Full logs: `logs/action_runs/20260907T144103Z_live_bot.log`, `logs/action_runs/20260907T144103Z_live_options.log`, `logs/action_runs/20260907T144103Z_options_bot.log`


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
{"ts_et":"2026-09-07T10:42:15.435560-04:00","date":"2026-09-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":62.1,"phases_s":{"reconcile":2.14,"cancel":0.03,"manage":5.29,"protective_stops":0.78,"scan":45.32,"entries":0.01},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9204","github_run_id":"34134198477","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:41:04  INFO      Mode: exits
14:41:05  INFO        place_all_stops: checking 3 positions...
14:41:05  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:41:05  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
14:41:05  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:41:05  INFO        [positions] 3/3 (3 valid)
14:41:05  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=1f91f370-efd0-46b5-9cf0-691726925f25
14:41:05  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=cab1c475-6a56-4435-8d58-bfe1ef7f8edc
14:41:25  INFO        SELL LIMIT not filled for FLEX, falling back to market
14:41:25  INFO        SELL MARKET FLEX closed
14:41:27  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=320605bf-8205-4557-b4ee-0ec5106ca240
14:41:27  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=fbc57163-6e1c-4c80-b7be-d266468b879a
14:41:47  INFO        SELL LIMIT not filled for LII, falling back to market
14:41:47  INFO        SELL MARKET LII closed
14:41:49  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=ce3cb14c-dff7-4937-9db2-8b41d5142e25
14:41:49  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=d65846f4-5d58-41ac-933b-971c1373b801
14:42:09  INFO        SELL LIMIT not filled for AMZN, falling back to market
14:42:09  INFO        SELL MARKET AMZN closed
14:42:11  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T10:42:12.714503-04:00 share=25% ===
2026-09-07 10:42:12,714 INFO === options_live_micro LIVE 2026-09-07T10:42:12.714503-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 10:42:12,776 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-07 10:42:12,825 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-07 10:42:12,848 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T144603Z

- UTC timestamp: `20260907T144603Z`
- GitHub run: [#9205](https://github.com/28twagg-ops/TradingBot/actions/runs/34134656999)
- Run id: `34134656999`
- Live bot: exit=`0`, duration=`72s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`76s`
- Full logs: `logs/action_runs/20260907T144603Z_live_bot.log`, `logs/action_runs/20260907T144603Z_live_options.log`, `logs/action_runs/20260907T144603Z_options_bot.log`


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
{"ts_et":"2026-09-07T10:47:19.196430-04:00","date":"2026-09-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":65.5,"phases_s":{"reconcile":2.49,"cancel":0.12,"manage":9.23,"protective_stops":3.33,"scan":41.31,"entries":0.1},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9205","github_run_id":"34134656999","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:46:04  INFO      Mode: exits
14:46:05  INFO        place_all_stops: checking 3 positions...
14:46:05  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:46:05  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
14:46:05  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:46:06  INFO        [positions] 3/3 (3 valid)
14:46:06  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=86bf5ba3-a77b-4e04-9db9-81d480f17631
14:46:06  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=4d643dff-8816-4c2d-92f6-95b0119da54d
14:46:26  INFO        SELL LIMIT not filled for FLEX, falling back to market
14:46:26  INFO        SELL MARKET FLEX closed
14:46:29  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=1f74b79e-d412-40e6-9a19-61b0da05d258
14:46:29  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=fe6eddd8-03c5-474f-8e65-6a1e18edc9f9
14:46:49  INFO        SELL LIMIT not filled for LII, falling back to market
14:46:49  INFO        SELL MARKET LII closed
14:46:51  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=7d9e570f-c9c9-464a-92cd-b0db3922929f
14:46:52  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=41ce5243-5f1b-4ab4-ac0f-98156fa76b7d
14:47:12  INFO        SELL LIMIT not filled for AMZN, falling back to market
14:47:12  INFO        SELL MARKET AMZN closed
14:47:15  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T10:47:15.829002-04:00 share=25% ===
2026-09-07 10:47:15,829 INFO === options_live_micro LIVE 2026-09-07T10:47:15.829002-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 10:47:16,041 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-07 10:47:16,259 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-07 10:47:16,394 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T145056Z

- UTC timestamp: `20260907T145056Z`
- GitHub run: [#9206](https://github.com/28twagg-ops/TradingBot/actions/runs/34135100479)
- Run id: `34135100479`
- Live bot: exit=`0`, duration=`68s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`78s`
- Full logs: `logs/action_runs/20260907T145056Z_live_bot.log`, `logs/action_runs/20260907T145056Z_live_options.log`, `logs/action_runs/20260907T145056Z_options_bot.log`


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
{"ts_et":"2026-09-07T10:52:08.120956-04:00","date":"2026-09-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":67.2,"phases_s":{"reconcile":2.15,"cancel":0.02,"manage":4.9,"protective_stops":0.61,"scan":50.96,"entries":0.05},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9206","github_run_id":"34135100479","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:50:57  INFO      Mode: exits
14:50:57  INFO        place_all_stops: checking 3 positions...
14:50:57  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:50:57  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
14:50:57  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:50:57  INFO        [positions] 3/3 (3 valid)
14:50:57  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=f483fabc-498b-4d4a-9c3f-2022dd60884d
14:50:57  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=6ffcabff-3752-4522-aefc-a96f724ba89d
14:51:17  INFO        SELL LIMIT not filled for FLEX, falling back to market
14:51:17  INFO        SELL MARKET FLEX closed
14:51:19  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=94d24d4d-f73d-4d52-876b-f6ba7622704f
14:51:19  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=9a4567a3-51bd-4042-9e2d-6acf6617b3eb
14:51:39  INFO        SELL LIMIT not filled for LII, falling back to market
14:51:40  INFO        SELL MARKET LII closed
14:51:42  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=a2932123-b715-487e-a02c-f554576521e5
14:51:42  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=8e2567ed-a44d-4597-b59f-f09a5df5dec7
14:52:02  INFO        SELL LIMIT not filled for AMZN, falling back to market
14:52:02  INFO        SELL MARKET AMZN closed
14:52:04  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T10:52:04.998279-04:00 share=25% ===
2026-09-07 10:52:04,998 INFO === options_live_micro LIVE 2026-09-07T10:52:04.998279-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 10:52:05,283 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-07 10:52:05,310 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-07 10:52:05,330 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T145557Z

- UTC timestamp: `20260907T145557Z`
- GitHub run: [#9207](https://github.com/28twagg-ops/TradingBot/actions/runs/34135541856)
- Run id: `34135541856`
- Live bot: exit=`0`, duration=`72s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`91s`
- Full logs: `logs/action_runs/20260907T145557Z_live_bot.log`, `logs/action_runs/20260907T145557Z_live_options.log`, `logs/action_runs/20260907T145557Z_options_bot.log`


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
{"ts_et":"2026-09-07T10:57:14.019967-04:00","date":"2026-09-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":79.8,"phases_s":{"reconcile":2.56,"cancel":0.15,"manage":10.26,"protective_stops":3.84,"scan":53.75,"entries":0.08},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9207","github_run_id":"34135541856","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:55:58  INFO      Mode: exits
14:55:59  INFO        place_all_stops: checking 3 positions...
14:55:59  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:55:59  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
14:55:59  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:56:00  INFO        [positions] 3/3 (3 valid)
14:56:00  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=714dbcf9-fa7f-4b5a-86db-bc1fc994f5a2
14:56:00  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=3a69a373-18d3-48b1-b61e-ff932ba0bb75
14:56:20  INFO        SELL LIMIT not filled for FLEX, falling back to market
14:56:20  INFO        SELL MARKET FLEX closed
14:56:23  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=8bcfde3f-d8b6-473c-8ad5-5415491495f0
14:56:23  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=46459a64-d9ab-469d-9d24-3cd7a3ad8846
14:56:43  INFO        SELL LIMIT not filled for LII, falling back to market
14:56:44  INFO        SELL MARKET LII closed
14:56:46  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=62437bf3-0441-4e23-8b55-fc3aeaca085b
14:56:46  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=5d90eb51-39e3-4b31-9453-3fc094fc77bc
14:57:06  INFO        SELL LIMIT not filled for AMZN, falling back to market
14:57:07  INFO        SELL MARKET AMZN closed
14:57:09  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T10:57:10.462505-04:00 share=25% ===
2026-09-07 10:57:10,462 INFO === options_live_micro LIVE 2026-09-07T10:57:10.462505-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 10:57:10,708 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-07 10:57:10,920 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-07 10:57:11,061 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T150058Z

- UTC timestamp: `20260907T150058Z`
- GitHub run: [#9208](https://github.com/28twagg-ops/TradingBot/actions/runs/34135972758)
- Run id: `34135972758`
- Live bot: exit=`0`, duration=`70s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`72s`
- Full logs: `logs/action_runs/20260907T150058Z_live_bot.log`, `logs/action_runs/20260907T150058Z_live_options.log`, `logs/action_runs/20260907T150058Z_options_bot.log`


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
{"ts_et":"2026-09-07T11:02:12.239424-04:00","date":"2026-09-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":61.1,"phases_s":{"reconcile":2.11,"cancel":0.02,"manage":5.29,"protective_stops":0.63,"scan":44.42,"entries":0.06},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9208","github_run_id":"34135972758","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:00:59  INFO      Mode: exits
15:01:02  INFO        place_all_stops: checking 3 positions...
15:01:02  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:01:02  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
15:01:02  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:01:02  INFO        [positions] 3/3 (3 valid)
15:01:02  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=1fbdeca7-843b-4e52-bbb2-17bd6c6960e0
15:01:02  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=632a8cd4-a154-4386-9935-948be55fec50
15:01:22  INFO        SELL LIMIT not filled for FLEX, falling back to market
15:01:22  INFO        SELL MARKET FLEX closed
15:01:24  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=e3037d50-4ab6-4dda-81c9-b65cd10cfc87
15:01:24  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=50c73afd-1e47-4558-a7d3-376079418136
15:01:44  INFO        SELL LIMIT not filled for LII, falling back to market
15:01:44  INFO        SELL MARKET LII closed
15:01:46  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=d3e65ef1-2254-4014-ae43-25c810a6b74f
15:01:46  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=39ffe25a-225a-405f-9a2f-c546199f6bcb
15:02:06  INFO        SELL LIMIT not filled for AMZN, falling back to market
15:02:06  INFO        SELL MARKET AMZN closed
15:02:08  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T11:02:09.593080-04:00 share=25% ===
2026-09-07 11:02:09,593 INFO === options_live_micro LIVE 2026-09-07T11:02:09.593080-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 11:02:09,636 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-07 11:02:09,664 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-07 11:02:09,677 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T150604Z

- UTC timestamp: `20260907T150604Z`
- GitHub run: [#9209](https://github.com/28twagg-ops/TradingBot/actions/runs/34136419831)
- Run id: `34136419831`
- Live bot: exit=`0`, duration=`72s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`91s`
- Full logs: `logs/action_runs/20260907T150604Z_live_bot.log`, `logs/action_runs/20260907T150604Z_live_options.log`, `logs/action_runs/20260907T150604Z_options_bot.log`


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
{"ts_et":"2026-09-07T11:07:20.867897-04:00","date":"2026-09-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":79.5,"phases_s":{"reconcile":2.56,"cancel":0.15,"manage":10.19,"protective_stops":4.02,"scan":53.35,"entries":0.08},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9209","github_run_id":"34136419831","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:06:05  INFO      Mode: exits
15:06:06  INFO        place_all_stops: checking 3 positions...
15:06:06  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:06:06  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
15:06:06  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:06:06  INFO        [positions] 3/3 (3 valid)
15:06:06  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=1a4f5ebe-73ed-401d-bed2-23f620b20c48
15:06:07  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=85f739b1-f8ce-4f00-beb7-8909effd3717
15:06:27  INFO        SELL LIMIT not filled for FLEX, falling back to market
15:06:27  INFO        SELL MARKET FLEX closed
15:06:30  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=c40de662-0efd-4f69-a7f6-8474bdb5a0c3
15:06:30  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=b05ae044-30a3-4d40-bf47-9a5a03e471e7
15:06:50  INFO        SELL LIMIT not filled for LII, falling back to market
15:06:50  INFO        SELL MARKET LII closed
15:06:53  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=56addf9e-1c91-4117-a1ac-1c875e70b0d5
15:06:53  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=61b80cd4-2e58-4875-bd41-7c9b45b42132
15:07:13  INFO        SELL LIMIT not filled for AMZN, falling back to market
15:07:13  INFO        SELL MARKET AMZN closed
15:07:16  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T11:07:17.297339-04:00 share=25% ===
2026-09-07 11:07:17,297 INFO === options_live_micro LIVE 2026-09-07T11:07:17.297339-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 11:07:17,524 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-07 11:07:17,732 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-07 11:07:17,871 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T151057Z

- UTC timestamp: `20260907T151057Z`
- GitHub run: [#9210](https://github.com/28twagg-ops/TradingBot/actions/runs/34136869400)
- Run id: `34136869400`
- Live bot: exit=`0`, duration=`68s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`75s`
- Full logs: `logs/action_runs/20260907T151057Z_live_bot.log`, `logs/action_runs/20260907T151057Z_live_options.log`, `logs/action_runs/20260907T151057Z_options_bot.log`


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
{"ts_et":"2026-09-07T11:12:09.301057-04:00","date":"2026-09-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":63.6,"phases_s":{"reconcile":2.21,"cancel":0.05,"manage":6.24,"protective_stops":1.29,"scan":45.1,"entries":0.03},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9210","github_run_id":"34136869400","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:10:57  INFO      Mode: exits
15:10:58  INFO        place_all_stops: checking 3 positions...
15:10:58  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:10:58  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
15:10:58  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:10:58  INFO        [positions] 3/3 (3 valid)
15:10:58  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=ea32d615-a3a8-4819-9a6b-c15f6fd0b4aa
15:10:58  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=bf76c8e7-48d7-4aca-b4ec-96d2e0fe44e1
15:11:18  INFO        SELL LIMIT not filled for FLEX, falling back to market
15:11:18  INFO        SELL MARKET FLEX closed
15:11:20  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=6eca0dfa-bf5a-4045-bd5b-e86171bc52b7
15:11:20  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=1ca01337-0dee-40d3-af97-2bb993ae6d91
15:11:41  INFO        SELL LIMIT not filled for LII, falling back to market
15:11:41  INFO        SELL MARKET LII closed
15:11:43  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=da700871-ff04-453e-a0a2-71005f25c2ef
15:11:43  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=e5eac087-6cf7-477f-969d-2f8a1c106ae3
15:12:03  INFO        SELL LIMIT not filled for AMZN, falling back to market
15:12:03  INFO        SELL MARKET AMZN closed
15:12:05  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T11:12:06.315902-04:00 share=25% ===
2026-09-07 11:12:06,315 INFO === options_live_micro LIVE 2026-09-07T11:12:06.315902-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 11:12:06,403 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-07 11:12:06,467 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-07 11:12:06,513 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T151605Z

- UTC timestamp: `20260907T151605Z`
- GitHub run: [#9211](https://github.com/28twagg-ops/TradingBot/actions/runs/34137321601)
- Run id: `34137321601`
- Live bot: exit=`0`, duration=`71s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`82s`
- Full logs: `logs/action_runs/20260907T151605Z_live_bot.log`, `logs/action_runs/20260907T151605Z_live_options.log`, `logs/action_runs/20260907T151605Z_options_bot.log`


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
{"ts_et":"2026-09-07T11:17:20.730202-04:00","date":"2026-09-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":70.0,"phases_s":{"reconcile":2.42,"cancel":0.11,"manage":9.29,"protective_stops":3.04,"scan":46.07,"entries":0.06},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9211","github_run_id":"34137321601","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:16:06  INFO      Mode: exits
15:16:07  INFO        place_all_stops: checking 3 positions...
15:16:07  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:16:07  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
15:16:07  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:16:07  INFO        [positions] 3/3 (3 valid)
15:16:07  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=4096436a-2e30-4927-b06d-958802e8b2d4
15:16:07  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=966be057-fc0f-4169-9306-d39fa81031e5
15:16:28  INFO        SELL LIMIT not filled for FLEX, falling back to market
15:16:28  INFO        SELL MARKET FLEX closed
15:16:30  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=d57ed763-ea77-43e8-bce3-954f348cc5be
15:16:30  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=359e5d25-e0cf-455f-b8bb-125ef0e7c783
15:16:51  INFO        SELL LIMIT not filled for LII, falling back to market
15:16:51  INFO        SELL MARKET LII closed
15:16:53  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=2ee4555a-a17a-4566-b8b6-0a45907cf15c
15:16:53  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=b3502413-9ce5-44a0-9637-91efa0b0e2f0
15:17:13  INFO        SELL LIMIT not filled for AMZN, falling back to market
15:17:14  INFO        SELL MARKET AMZN closed
15:17:16  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T11:17:17.314180-04:00 share=25% ===
2026-09-07 11:17:17,314 INFO === options_live_micro LIVE 2026-09-07T11:17:17.314180-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 11:17:17,530 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-07 11:17:17,723 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-07 11:17:17,844 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T152102Z

- UTC timestamp: `20260907T152102Z`
- GitHub run: [#9212](https://github.com/28twagg-ops/TradingBot/actions/runs/34137756940)
- Run id: `34137756940`
- Live bot: exit=`0`, duration=`72s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`91s`
- Full logs: `logs/action_runs/20260907T152102Z_live_bot.log`, `logs/action_runs/20260907T152102Z_live_options.log`, `logs/action_runs/20260907T152102Z_options_bot.log`


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
{"ts_et":"2026-09-07T11:22:18.803390-04:00","date":"2026-09-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":79.4,"phases_s":{"reconcile":2.52,"cancel":0.14,"manage":10.17,"protective_stops":3.74,"scan":53.67,"entries":0.08},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9212","github_run_id":"34137756940","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:21:03  INFO      Mode: exits
15:21:04  INFO        place_all_stops: checking 3 positions...
15:21:04  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:21:04  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
15:21:04  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:21:04  INFO        [positions] 3/3 (3 valid)
15:21:04  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=3b2a4206-8122-42ce-add9-eff243fe23fe
15:21:05  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=a663387e-d8d1-451f-bbef-6ce2ab81b3d4
15:21:25  INFO        SELL LIMIT not filled for FLEX, falling back to market
15:21:25  INFO        SELL MARKET FLEX closed
15:21:27  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=44210245-6bc8-4952-b44e-55c4bbf90259
15:21:28  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=ad78c470-c288-4629-99cb-acd4796d0e4b
15:21:48  INFO        SELL LIMIT not filled for LII, falling back to market
15:21:48  INFO        SELL MARKET LII closed
15:21:50  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=dfe05679-00aa-4165-8557-e2ca0755caa9
15:21:51  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=24fedcdd-18b6-4e98-af60-75827402e64f
15:22:11  INFO        SELL LIMIT not filled for AMZN, falling back to market
15:22:11  INFO        SELL MARKET AMZN closed
15:22:14  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T11:22:15.009387-04:00 share=25% ===
2026-09-07 11:22:15,009 INFO === options_live_micro LIVE 2026-09-07T11:22:15.009387-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 11:22:15,248 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-07 11:22:15,456 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-07 11:22:15,594 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T152604Z

- UTC timestamp: `20260907T152604Z`
- GitHub run: [#9213](https://github.com/28twagg-ops/TradingBot/actions/runs/34138190036)
- Run id: `34138190036`
- Live bot: exit=`0`, duration=`69s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`85s`
- Full logs: `logs/action_runs/20260907T152604Z_live_bot.log`, `logs/action_runs/20260907T152604Z_live_options.log`, `logs/action_runs/20260907T152604Z_options_bot.log`


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
{"ts_et":"2026-09-07T11:27:18.083954-04:00","date":"2026-09-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":72.9,"phases_s":{"reconcile":2.27,"cancel":0.07,"manage":7.91,"protective_stops":1.86,"scan":51.92,"entries":0.04},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9213","github_run_id":"34138190036","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:26:05  INFO      Mode: exits
15:26:05  INFO        place_all_stops: checking 3 positions...
15:26:05  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:26:05  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
15:26:05  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:26:05  INFO        [positions] 3/3 (3 valid)
15:26:05  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=ebcb6867-5ee7-4072-9bdd-8f4b20189eff
15:26:05  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=1c5224db-5096-44dd-b2f0-ab25b36a5c9c
15:26:26  INFO        SELL LIMIT not filled for FLEX, falling back to market
15:26:26  INFO        SELL MARKET FLEX closed
15:26:28  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=b09d08f4-7145-427f-9a85-fd8af2c70304
15:26:28  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=19d81995-87ce-4d63-ad33-8b13c3b67cc2
15:26:48  INFO        SELL LIMIT not filled for LII, falling back to market
15:26:48  INFO        SELL MARKET LII closed
15:26:51  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=9fc217c4-f444-4937-a212-e1702b860182
15:26:51  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=d448f0c9-3c00-4eaf-87f2-866ae28a96e2
15:27:11  INFO        SELL LIMIT not filled for AMZN, falling back to market
15:27:11  INFO        SELL MARKET AMZN closed
15:27:13  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T11:27:14.675239-04:00 share=25% ===
2026-09-07 11:27:14,675 INFO === options_live_micro LIVE 2026-09-07T11:27:14.675239-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 11:27:14,984 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-07 11:27:15,081 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-07 11:27:15,138 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T153059Z

- UTC timestamp: `20260907T153059Z`
- GitHub run: [#9214](https://github.com/28twagg-ops/TradingBot/actions/runs/34138620624)
- Run id: `34138620624`
- Live bot: exit=`0`, duration=`68s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`74s`
- Full logs: `logs/action_runs/20260907T153059Z_live_bot.log`, `logs/action_runs/20260907T153059Z_live_options.log`, `logs/action_runs/20260907T153059Z_options_bot.log`


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
{"ts_et":"2026-09-07T11:32:11.618077-04:00","date":"2026-09-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":62.2,"phases_s":{"reconcile":2.15,"cancel":0.03,"manage":5.42,"protective_stops":0.74,"scan":45.26,"entries":0.01},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9214","github_run_id":"34138620624","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:31:00  INFO      Mode: exits
15:31:00  INFO        place_all_stops: checking 3 positions...
15:31:00  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:31:00  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
15:31:00  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:31:01  INFO        [positions] 3/3 (3 valid)
15:31:01  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=28dca0ca-9672-457a-80c1-71c54ed891bc
15:31:01  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=1f3ea5e6-21be-49d6-9404-fa5addb4b280
15:31:21  INFO        SELL LIMIT not filled for FLEX, falling back to market
15:31:21  INFO        SELL MARKET FLEX closed
15:31:23  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=98387d92-16ef-4c2d-a965-4310b83db516
15:31:23  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=572d469f-e33e-4885-b407-f7534b23905f
15:31:43  INFO        SELL LIMIT not filled for LII, falling back to market
15:31:43  INFO        SELL MARKET LII closed
15:31:45  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=172115ca-37b5-4c8f-ba91-9eee8af6ab39
15:31:45  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=5365c887-2452-40f8-a56c-b2a1500fdc3a
15:32:05  INFO        SELL LIMIT not filled for AMZN, falling back to market
15:32:05  INFO        SELL MARKET AMZN closed
15:32:07  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T11:32:08.646399-04:00 share=25% ===
2026-09-07 11:32:08,646 INFO === options_live_micro LIVE 2026-09-07T11:32:08.646399-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 11:32:08,703 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-07 11:32:08,736 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-07 11:32:08,758 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T153602Z

- UTC timestamp: `20260907T153602Z`
- GitHub run: [#9215](https://github.com/28twagg-ops/TradingBot/actions/runs/34139046850)
- Run id: `34139046850`
- Live bot: exit=`0`, duration=`71s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`31s`
- Full logs: `logs/action_runs/20260907T153602Z_live_bot.log`, `logs/action_runs/20260907T153602Z_live_options.log`, `logs/action_runs/20260907T153602Z_options_bot.log`


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
{"ts_et":"2026-09-07T11:37:16.666983-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":20.4,"phases_s":{"reconcile":2.32,"cancel":0.13,"manage":6.87,"protective_stops":2.27},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9215","github_run_id":"34139046850","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:36:04  INFO      Mode: exits
15:36:04  INFO        place_all_stops: checking 3 positions...
15:36:04  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:36:04  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
15:36:04  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:36:04  INFO        [positions] 3/3 (3 valid)
15:36:04  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=ab649a61-1bf5-4602-8b6b-304098e1397c
15:36:04  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=12e04618-3baf-4f1d-995e-bacc49d898b5
15:36:25  INFO        SELL LIMIT not filled for FLEX, falling back to market
15:36:25  INFO        SELL MARKET FLEX closed
15:36:27  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=25395dc2-cb8d-4cd1-bd13-c024b789c755
15:36:27  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=34def581-13e7-4dae-b2da-bb500a63e8a2
15:36:47  INFO        SELL LIMIT not filled for LII, falling back to market
15:36:47  INFO        SELL MARKET LII closed
15:36:50  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=c8f576eb-6036-45da-b47f-ee7e1882f5d8
15:36:50  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=4636367e-2138-401e-ad13-c7edee737bee
15:37:10  INFO        SELL LIMIT not filled for AMZN, falling back to market
15:37:10  INFO        SELL MARKET AMZN closed
15:37:12  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T11:37:13.684576-04:00 share=25% ===
2026-09-07 11:37:13,684 INFO === options_live_micro LIVE 2026-09-07T11:37:13.684576-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 11:37:13,826 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 11:37:13,944 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 11:37:13,984 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T154101Z

- UTC timestamp: `20260907T154101Z`
- GitHub run: [#9216](https://github.com/28twagg-ops/TradingBot/actions/runs/34139465567)
- Run id: `34139465567`
- Live bot: exit=`0`, duration=`71s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`36s`
- Full logs: `logs/action_runs/20260907T154101Z_live_bot.log`, `logs/action_runs/20260907T154101Z_live_options.log`, `logs/action_runs/20260907T154101Z_options_bot.log`


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
{"ts_et":"2026-09-07T11:42:16.864631-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":24.8,"phases_s":{"reconcile":2.46,"cancel":0.18,"manage":9.55,"protective_stops":3.56},"signals":0,"placed":0,"equity":1005125.39,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9216","github_run_id":"34139465567","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:41:02  INFO      Mode: exits
15:41:02  INFO        place_all_stops: checking 3 positions...
15:41:02  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:41:02  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
15:41:02  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:41:03  INFO        [positions] 3/3 (3 valid)
15:41:03  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=2f44786b-7ec5-4910-a15b-55ba7f0e5ff3
15:41:04  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=ece1d456-8e8f-4d88-a12c-c0d666a4e7a8
15:41:24  INFO        SELL LIMIT not filled for FLEX, falling back to market
15:41:24  INFO        SELL MARKET FLEX closed
15:41:26  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=dc77a263-4bde-4913-ba6a-906b4cc217f6
15:41:26  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=45707b1a-4031-4ca2-be72-dd42302f0af3
15:41:47  INFO        SELL LIMIT not filled for LII, falling back to market
15:41:47  INFO        SELL MARKET LII closed
15:41:49  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=5e3c203a-e05f-4e29-add3-434821d99ccb
15:41:49  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=ee99c2e7-5532-4bd0-b09e-91c936c1dcda
15:42:10  INFO        SELL LIMIT not filled for AMZN, falling back to market
15:42:10  INFO        SELL MARKET AMZN closed
15:42:12  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T11:42:13.533803-04:00 share=25% ===
2026-09-07 11:42:13,533 INFO === options_live_micro LIVE 2026-09-07T11:42:13.533803-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 11:42:13,732 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 11:42:13,921 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 11:42:13,978 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T154602Z

- UTC timestamp: `20260907T154602Z`
- GitHub run: [#9217](https://github.com/28twagg-ops/TradingBot/actions/runs/34139880605)
- Run id: `34139880605`
- Live bot: exit=`0`, duration=`72s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`33s`
- Full logs: `logs/action_runs/20260907T154602Z_live_bot.log`, `logs/action_runs/20260907T154602Z_live_options.log`, `logs/action_runs/20260907T154602Z_options_bot.log`


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
{"ts_et":"2026-09-07T11:47:18.691106-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":21.3,"phases_s":{"reconcile":0.47,"cancel":0.22,"manage":10.36,"protective_stops":3.26},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9217","github_run_id":"34139880605","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:46:03  INFO      Mode: exits
15:46:04  INFO        place_all_stops: checking 3 positions...
15:46:04  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:46:04  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
15:46:04  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:46:04  INFO        [positions] 3/3 (3 valid)
15:46:04  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=d0e22147-3777-45b5-94ad-f3833b5aab90
15:46:05  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=d670ecc5-936a-43b1-8d45-b739e3a03428
15:46:25  INFO        SELL LIMIT not filled for FLEX, falling back to market
15:46:25  INFO        SELL MARKET FLEX closed
15:46:27  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=4d86a21e-7456-4ff9-a089-9cbcb66f0246
15:46:28  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=eb26207d-b757-4c12-9a8d-0d8067af9ffd
15:46:48  INFO        SELL LIMIT not filled for LII, falling back to market
15:46:48  INFO        SELL MARKET LII closed
15:46:50  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=1d4f6829-726f-41fb-b459-17635eaef0f8
15:46:51  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=8ba4a0fb-73b8-4832-85f3-9f68fbe9fed0
15:47:11  INFO        SELL LIMIT not filled for AMZN, falling back to market
15:47:11  INFO        SELL MARKET AMZN closed
15:47:14  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T11:47:15.150222-04:00 share=25% ===
2026-09-07 11:47:15,150 INFO === options_live_micro LIVE 2026-09-07T11:47:15.150222-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 11:47:15,374 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 11:47:15,581 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 11:47:15,649 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (158 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T155058Z

- UTC timestamp: `20260907T155058Z`
- GitHub run: [#9218](https://github.com/28twagg-ops/TradingBot/actions/runs/34140300271)
- Run id: `34140300271`
- Live bot: exit=`0`, duration=`68s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260907T155058Z_live_bot.log`, `logs/action_runs/20260907T155058Z_live_options.log`, `logs/action_runs/20260907T155058Z_options_bot.log`


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
{"ts_et":"2026-09-07T11:52:09.596619-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.4,"phases_s":{"reconcile":0.12,"cancel":0.04,"manage":5.25,"protective_stops":0.5},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9218","github_run_id":"34140300271","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:50:59  INFO      Mode: exits
15:50:59  INFO        place_all_stops: checking 3 positions...
15:50:59  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:50:59  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
15:50:59  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:50:59  INFO        [positions] 3/3 (3 valid)
15:50:59  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=bb519f4b-d297-40d9-9b0e-916285ea8d55
15:50:59  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=482d28b5-fe0d-4ce9-be5f-b8e28d1f0445
15:51:19  INFO        SELL LIMIT not filled for FLEX, falling back to market
15:51:19  INFO        SELL MARKET FLEX closed
15:51:21  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=5b9a19ea-5df7-44cf-82c4-2bee1ba852b4
15:51:21  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=b867db11-ed79-4798-b774-e2895eaa325e
15:51:41  INFO        SELL LIMIT not filled for LII, falling back to market
15:51:41  INFO        SELL MARKET LII closed
15:51:43  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=757d4c80-964f-494f-8b1a-e9d4d09460e8
15:51:43  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=4f85843a-568c-43e0-a788-6e73e3f46c2b
15:52:04  INFO        SELL LIMIT not filled for AMZN, falling back to market
15:52:04  INFO        SELL MARKET AMZN closed
15:52:06  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T11:52:06.938197-04:00 share=25% ===
2026-09-07 11:52:06,938 INFO === options_live_micro LIVE 2026-09-07T11:52:06.938197-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 11:52:06,996 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 11:52:07,030 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 11:52:07,040 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T155554Z

- UTC timestamp: `20260907T155554Z`
- GitHub run: [#9219](https://github.com/28twagg-ops/TradingBot/actions/runs/34140709575)
- Run id: `34140709575`
- Live bot: exit=`0`, duration=`68s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`15s`
- Full logs: `logs/action_runs/20260907T155554Z_live_bot.log`, `logs/action_runs/20260907T155554Z_live_options.log`, `logs/action_runs/20260907T155554Z_options_bot.log`


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
{"ts_et":"2026-09-07T11:57:05.601296-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.0,"phases_s":{"reconcile":0.09,"cancel":0.04,"manage":5.09,"protective_stops":0.33},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9219","github_run_id":"34140709575","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:55:55  INFO      Mode: exits
15:55:55  INFO        place_all_stops: checking 3 positions...
15:55:55  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:55:56  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
15:55:56  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:55:56  INFO        [positions] 3/3 (3 valid)
15:55:56  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=47475818-5875-449e-8f87-0a310dbfa0bb
15:55:56  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=da592d35-a596-4748-a270-95c65ae4a35a
15:56:16  INFO        SELL LIMIT not filled for FLEX, falling back to market
15:56:16  INFO        SELL MARKET FLEX closed
15:56:18  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=ed36b874-4dca-4078-a2a6-da49506faf88
15:56:18  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=1854257d-d423-46a0-aa11-72950ac1feda
15:56:38  INFO        SELL LIMIT not filled for LII, falling back to market
15:56:38  INFO        SELL MARKET LII closed
15:56:40  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=606a6bec-ca54-4247-814a-1fc769eb0cd7
15:56:40  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=66f4d9e6-73cc-4441-b1b7-79990c00c8b1
15:57:00  INFO        SELL LIMIT not filled for AMZN, falling back to market
15:57:00  INFO        SELL MARKET AMZN closed
15:57:02  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T11:57:03.341822-04:00 share=25% ===
2026-09-07 11:57:03,341 INFO === options_live_micro LIVE 2026-09-07T11:57:03.341822-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 11:57:03,381 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 11:57:03,405 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 11:57:03,414 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T160102Z

- UTC timestamp: `20260907T160102Z`
- GitHub run: [#9220](https://github.com/28twagg-ops/TradingBot/actions/runs/34141109059)
- Run id: `34141109059`
- Live bot: exit=`0`, duration=`68s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260907T160102Z_live_bot.log`, `logs/action_runs/20260907T160102Z_live_options.log`, `logs/action_runs/20260907T160102Z_options_bot.log`


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
{"ts_et":"2026-09-07T12:02:14.107842-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.0,"phases_s":{"reconcile":0.1,"cancel":0.03,"manage":5.11,"protective_stops":0.34},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9220","github_run_id":"34141109059","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:01:03  INFO      Mode: exits
16:01:03  INFO        place_all_stops: checking 3 positions...
16:01:03  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:01:03  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
16:01:03  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:01:04  INFO        [positions] 3/3 (3 valid)
16:01:04  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=7cb9d139-27e6-46e8-a701-0d44bd2e94c7
16:01:04  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=1d013f24-d090-4fd5-9f66-45c60350d67f
16:01:24  INFO        SELL LIMIT not filled for FLEX, falling back to market
16:01:24  INFO        SELL MARKET FLEX closed
16:01:26  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=17c0f6f6-6b70-4384-b06a-8c09ba84ef6f
16:01:26  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=7da92051-c7f6-431e-912f-8c524bc02d78
16:01:46  INFO        SELL LIMIT not filled for LII, falling back to market
16:01:46  INFO        SELL MARKET LII closed
16:01:48  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=49383cf9-6722-4d0a-84df-a1e187013701
16:01:48  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=a2e6d8de-a2f4-43bf-ba42-44c36d0957dc
16:02:08  INFO        SELL LIMIT not filled for AMZN, falling back to market
16:02:08  INFO        SELL MARKET AMZN closed
16:02:10  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T12:02:11.401616-04:00 share=25% ===
2026-09-07 12:02:11,401 INFO === options_live_micro LIVE 2026-09-07T12:02:11.401616-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 12:02:11,592 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 12:02:11,613 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 12:02:11,622 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T160558Z

- UTC timestamp: `20260907T160558Z`
- GitHub run: [#9221](https://github.com/28twagg-ops/TradingBot/actions/runs/34141527321)
- Run id: `34141527321`
- Live bot: exit=`0`, duration=`69s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`19s`
- Full logs: `logs/action_runs/20260907T160558Z_live_bot.log`, `logs/action_runs/20260907T160558Z_live_options.log`, `logs/action_runs/20260907T160558Z_options_bot.log`


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
{"ts_et":"2026-09-07T12:07:11.131613-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":7.7,"phases_s":{"reconcile":0.17,"cancel":0.07,"manage":6.04,"protective_stops":0.9},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9221","github_run_id":"34141527321","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:05:59  INFO      Mode: exits
16:05:59  INFO        place_all_stops: checking 3 positions...
16:05:59  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:05:59  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
16:05:59  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:05:59  INFO        [positions] 3/3 (3 valid)
16:06:00  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=c85eacf0-13da-4c1c-8c02-4fa37cb4eca3
16:06:00  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=604884ba-60cc-4017-8dba-affd32514467
16:06:20  INFO        SELL LIMIT not filled for FLEX, falling back to market
16:06:20  INFO        SELL MARKET FLEX closed
16:06:22  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=489c745b-4dc9-459e-ae40-d126079c80cb
16:06:22  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=4495fee4-3b89-4a66-bb07-ff86758ed6f5
16:06:42  INFO        SELL LIMIT not filled for LII, falling back to market
16:06:42  INFO        SELL MARKET LII closed
16:06:44  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=dcb9fa5f-b81e-46c0-9b94-37076c65367c
16:06:45  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=9525648a-035d-4ace-8986-7e93bffc1c51
16:07:05  INFO        SELL LIMIT not filled for AMZN, falling back to market
16:07:05  INFO        SELL MARKET AMZN closed
16:07:07  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T12:07:08.215064-04:00 share=25% ===
2026-09-07 12:07:08,215 INFO === options_live_micro LIVE 2026-09-07T12:07:08.215064-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 12:07:08,330 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 12:07:08,407 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 12:07:08,433 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T161102Z

- UTC timestamp: `20260907T161102Z`
- GitHub run: [#9222](https://github.com/28twagg-ops/TradingBot/actions/runs/34141946156)
- Run id: `34141946156`
- Live bot: exit=`0`, duration=`70s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`22s`
- Full logs: `logs/action_runs/20260907T161102Z_live_bot.log`, `logs/action_runs/20260907T161102Z_live_options.log`, `logs/action_runs/20260907T161102Z_options_bot.log`


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
{"ts_et":"2026-09-07T12:12:16.040520-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":10.8,"phases_s":{"reconcile":0.28,"cancel":0.13,"manage":8.18,"protective_stops":1.64},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9222","github_run_id":"34141946156","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:11:03  INFO      Mode: exits
16:11:03  INFO        place_all_stops: checking 3 positions...
16:11:03  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:11:03  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
16:11:03  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:11:04  INFO        [positions] 3/3 (3 valid)
16:11:04  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=3aad63ce-187c-4ff5-9c14-6cde246ff313
16:11:04  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=238030c4-3760-4687-a04c-a27416a774c3
16:11:24  INFO        SELL LIMIT not filled for FLEX, falling back to market
16:11:24  INFO        SELL MARKET FLEX closed
16:11:26  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=6296e52f-bf2f-499b-a10e-e68b07e5f29c
16:11:26  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=90f7c5d9-c2c8-47f7-8b76-466f929d9999
16:11:47  INFO        SELL LIMIT not filled for LII, falling back to market
16:11:47  INFO        SELL MARKET LII closed
16:11:49  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=a5e62c56-8f7d-44b6-8af8-d17c201ef18d
16:11:49  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=77d111f7-e16a-4e3c-a336-b91ec6baf8ca
16:12:09  INFO        SELL LIMIT not filled for AMZN, falling back to market
16:12:09  INFO        SELL MARKET AMZN closed
16:12:12  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T12:12:12.870339-04:00 share=25% ===
2026-09-07 12:12:12,870 INFO === options_live_micro LIVE 2026-09-07T12:12:12.870339-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 12:12:13,043 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 12:12:13,196 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 12:12:13,243 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T161602Z

- UTC timestamp: `20260907T161602Z`
- GitHub run: [#9223](https://github.com/28twagg-ops/TradingBot/actions/runs/34142364225)
- Run id: `34142364225`
- Live bot: exit=`0`, duration=`68s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260907T161602Z_live_bot.log`, `logs/action_runs/20260907T161602Z_live_options.log`, `logs/action_runs/20260907T161602Z_options_bot.log`


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
{"ts_et":"2026-09-07T12:17:14.753661-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":8.6,"phases_s":{"reconcile":0.18,"cancel":0.07,"manage":6.85,"protective_stops":0.96},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9223","github_run_id":"34142364225","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:16:03  INFO      Mode: exits
16:16:03  INFO        place_all_stops: checking 3 positions...
16:16:03  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:16:03  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
16:16:03  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:16:03  INFO        [positions] 3/3 (3 valid)
16:16:03  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=31881a43-474a-4f89-93ba-f2e88a31e457
16:16:03  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=cb686d47-5af8-4eeb-b987-fb1893cd4c16
16:16:23  INFO        SELL LIMIT not filled for FLEX, falling back to market
16:16:23  INFO        SELL MARKET FLEX closed
16:16:25  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=4f82b226-87ec-497a-a9ff-a0e53ec6301c
16:16:26  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=f5607eec-836e-49c3-9686-07113b344791
16:16:46  INFO        SELL LIMIT not filled for LII, falling back to market
16:16:46  INFO        SELL MARKET LII closed
16:16:48  INFO        SELL order cancelled AMZN  type=OrderType.MARKET  id=5da1a3a1-4ae5-4fd4-aeac-43f9568853b6
16:16:48  INFO        SELL LIMIT AMZN  qty=0.135349882  limit=$257.99  id=4885e360-3f26-4281-b040-8bbaed9766d8
16:17:08  INFO        SELL LIMIT not filled for AMZN, falling back to market
16:17:08  INFO        SELL MARKET AMZN closed
16:17:10  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                      EXIT: max_hold 5d (+1.2%)|
|  AMZN         PARTIAL SELL (0.1353 sh remain) — will retry this session|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  3 attempted  |  0 filled  |  3 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T12:17:11.638613-04:00 share=25% ===
2026-09-07 12:17:11,638 INFO === options_live_micro LIVE 2026-09-07T12:17:11.638613-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 12:17:11,722 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 12:17:11,796 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 12:17:11,818 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T162058Z

- UTC timestamp: `20260907T162058Z`
- GitHub run: [#9224](https://github.com/28twagg-ops/TradingBot/actions/runs/34142760421)
- Run id: `34142760421`
- Live bot: exit=`0`, duration=`46s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260907T162058Z_live_bot.log`, `logs/action_runs/20260907T162058Z_live_options.log`, `logs/action_runs/20260907T162058Z_options_bot.log`


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
{"ts_et":"2026-09-07T12:21:47.412308-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.0,"phases_s":{"reconcile":0.11,"cancel":0.04,"manage":4.97,"protective_stops":0.36},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9224","github_run_id":"34142760421","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:20:59  INFO      Mode: exits
16:20:59  INFO        place_all_stops: checking 3 positions...
16:20:59  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:20:59  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
16:20:59  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:20:59  INFO        [positions] 3/3 (3 valid)
16:20:59  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=2d2e835f-8d3f-4586-82d2-f9372a2100b3
16:20:59  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=794bb008-a320-4bb0-b909-2e52056dff60
16:21:19  INFO        SELL LIMIT not filled for FLEX, falling back to market
16:21:19  INFO        SELL MARKET FLEX closed
16:21:21  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=286a5a5c-2a52-4027-8599-c27c90918765
16:21:21  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=e7652449-d83d-4bb2-9305-af84608ab3ca
16:21:41  INFO        SELL LIMIT not filled for LII, falling back to market
16:21:41  INFO        SELL MARKET LII closed
16:21:43  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  2 attempted  |  0 filled  |  2 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T12:21:44.749198-04:00 share=25% ===
2026-09-07 12:21:44,749 INFO === options_live_micro LIVE 2026-09-07T12:21:44.749198-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 12:21:44,801 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 12:21:44,825 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 12:21:44,833 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T162559Z

- UTC timestamp: `20260907T162559Z`
- GitHub run: [#9225](https://github.com/28twagg-ops/TradingBot/actions/runs/34143159153)
- Run id: `34143159153`
- Live bot: exit=`0`, duration=`50s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`26s`
- Full logs: `logs/action_runs/20260907T162559Z_live_bot.log`, `logs/action_runs/20260907T162559Z_live_options.log`, `logs/action_runs/20260907T162559Z_options_bot.log`


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
{"ts_et":"2026-09-07T12:26:53.496856-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":14.5,"phases_s":{"reconcile":0.5,"cancel":0.22,"manage":10.0,"protective_stops":3.05},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9225","github_run_id":"34143159153","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:26:00  INFO      Mode: exits
16:26:01  INFO        place_all_stops: checking 3 positions...
16:26:01  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:26:01  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
16:26:01  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:26:02  INFO        [positions] 3/3 (3 valid)
16:26:02  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=31b028fe-5126-45c7-8ed2-f47b0457c745
16:26:02  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=db3a7003-bc4c-42c4-ac3c-e90ca7f414e5
16:26:23  INFO        SELL LIMIT not filled for FLEX, falling back to market
16:26:23  INFO        SELL MARKET FLEX closed
16:26:25  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=a9ef1183-6c58-4701-a55a-75a872860a1a
16:26:25  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=c243be6f-fc28-4515-962b-e817e1b3b3d8
16:26:46  INFO        SELL LIMIT not filled for LII, falling back to market
16:26:46  INFO        SELL MARKET LII closed
16:26:49  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  2 attempted  |  0 filled  |  2 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T12:26:49.930608-04:00 share=25% ===
2026-09-07 12:26:49,930 INFO === options_live_micro LIVE 2026-09-07T12:26:49.930608-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 12:26:50,178 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 12:26:50,404 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 12:26:50,476 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T163104Z

- UTC timestamp: `20260907T163104Z`
- GitHub run: [#9226](https://github.com/28twagg-ops/TradingBot/actions/runs/34143547172)
- Run id: `34143547172`
- Live bot: exit=`0`, duration=`48s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`25s`
- Full logs: `logs/action_runs/20260907T163104Z_live_bot.log`, `logs/action_runs/20260907T163104Z_live_options.log`, `logs/action_runs/20260907T163104Z_options_bot.log`


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
{"ts_et":"2026-09-07T12:31:57.364887-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":13.1,"phases_s":{"reconcile":0.41,"cancel":0.2,"manage":9.3,"protective_stops":2.48},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9226","github_run_id":"34143547172","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:31:05  INFO      Mode: exits
16:31:05  INFO        place_all_stops: checking 3 positions...
16:31:05  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:31:05  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
16:31:05  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:31:06  INFO        [positions] 3/3 (3 valid)
16:31:06  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=f1ae4b42-096f-4d71-b319-ffa91c3a0f44
16:31:06  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=2816a16c-ac0c-4499-80e9-ff734261e316
16:31:26  INFO        SELL LIMIT not filled for FLEX, falling back to market
16:31:27  INFO        SELL MARKET FLEX closed
16:31:29  INFO        SELL order cancelled LII  type=OrderType.MARKET  id=52576f0b-0bae-4902-bb2f-cce950c39942
16:31:29  INFO        SELL LIMIT LII  qty=0.089467389  limit=$389.75  id=7815afb3-5fc8-4ad2-849c-72229ff0c8bc
16:31:49  INFO        SELL LIMIT not filled for LII, falling back to market
16:31:49  INFO        SELL MARKET LII closed
16:31:52  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                       EXIT: max_hold 4d (+1.1%)|
|  LII          PARTIAL SELL (0.0895 sh remain) — will retry this session|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  2 attempted  |  0 filled  |  2 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T12:31:53.385813-04:00 share=25% ===
2026-09-07 12:31:53,385 INFO === options_live_micro LIVE 2026-09-07T12:31:53.385813-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 12:31:53,753 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 12:31:53,943 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 12:31:54,001 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T163600Z

- UTC timestamp: `20260907T163600Z`
- GitHub run: [#9227](https://github.com/28twagg-ops/TradingBot/actions/runs/34143933605)
- Run id: `34143933605`
- Live bot: exit=`0`, duration=`26s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`25s`
- Full logs: `logs/action_runs/20260907T163600Z_live_bot.log`, `logs/action_runs/20260907T163600Z_live_options.log`, `logs/action_runs/20260907T163600Z_options_bot.log`


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
{"ts_et":"2026-09-07T12:36:30.785577-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":12.9,"phases_s":{"reconcile":0.39,"cancel":0.17,"manage":9.36,"protective_stops":2.27},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9227","github_run_id":"34143933605","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:36:01  INFO      Mode: exits
16:36:02  INFO        place_all_stops: checking 3 positions...
16:36:02  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:36:02  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
16:36:02  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:36:03  INFO        [positions] 3/3 (3 valid)
16:36:03  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=3cfbd413-3e84-4fe7-9ee1-eb2b4b2a86a1
16:36:03  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=40140a0e-24ee-4846-999e-fe5d115cba7c
16:36:23  INFO        SELL LIMIT not filled for FLEX, falling back to market
16:36:23  INFO        SELL MARKET FLEX closed
16:36:26  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  0 filled  |  1 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T12:36:27.027124-04:00 share=25% ===
2026-09-07 12:36:27,027 INFO === options_live_micro LIVE 2026-09-07T12:36:27.027124-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 12:36:27,236 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 12:36:27,410 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 12:36:27,468 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T164059Z

- UTC timestamp: `20260907T164059Z`
- GitHub run: [#9228](https://github.com/28twagg-ops/TradingBot/actions/runs/34144313719)
- Run id: `34144313719`
- Live bot: exit=`0`, duration=`27s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260907T164059Z_live_bot.log`, `logs/action_runs/20260907T164059Z_live_options.log`, `logs/action_runs/20260907T164059Z_options_bot.log`


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
{"ts_et":"2026-09-07T12:41:30.450740-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":12.3,"phases_s":{"reconcile":0.4,"cancel":0.17,"manage":8.82,"protective_stops":2.27},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9228","github_run_id":"34144313719","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:41:01  INFO      Mode: exits
16:41:02  INFO        place_all_stops: checking 3 positions...
16:41:02  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:41:02  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
16:41:02  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:41:02  INFO        [positions] 3/3 (3 valid)
16:41:02  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=ec5a619a-9915-40de-a283-0bdce349022b
16:41:03  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=36310cfe-a908-4964-99d1-99219a1f17d2
16:41:23  INFO        SELL LIMIT not filled for FLEX, falling back to market
16:41:23  INFO        SELL MARKET FLEX closed
16:41:26  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  0 filled  |  1 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T12:41:26.841410-04:00 share=25% ===
2026-09-07 12:41:26,841 INFO === options_live_micro LIVE 2026-09-07T12:41:26.841410-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 12:41:27,061 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 12:41:27,234 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 12:41:27,292 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T164600Z

- UTC timestamp: `20260907T164600Z`
- GitHub run: [#9229](https://github.com/28twagg-ops/TradingBot/actions/runs/34144681552)
- Run id: `34144681552`
- Live bot: exit=`0`, duration=`26s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`25s`
- Full logs: `logs/action_runs/20260907T164600Z_live_bot.log`, `logs/action_runs/20260907T164600Z_live_options.log`, `logs/action_runs/20260907T164600Z_options_bot.log`


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
{"ts_et":"2026-09-07T12:46:30.924962-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":12.8,"phases_s":{"reconcile":0.4,"cancel":0.19,"manage":9.0,"protective_stops":2.51},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9229","github_run_id":"34144681552","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:46:01  INFO      Mode: exits
16:46:02  INFO        place_all_stops: checking 3 positions...
16:46:02  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:46:02  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
16:46:02  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:46:03  INFO        [positions] 3/3 (3 valid)
16:46:03  INFO        SELL order cancelled FLEX  type=OrderType.MARKET  id=ad8e581e-921f-4151-8396-ade82dc871a6
16:46:03  INFO        SELL LIMIT FLEX  qty=0.31607724  limit=$109.29  id=7f3e869b-2e48-43c4-9111-d19cb2404fb0
16:46:24  INFO        SELL LIMIT not filled for FLEX, falling back to market
16:46:24  INFO        SELL MARKET FLEX closed
16:46:26  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                      EXIT: max_hold 3d (+0.1%)|
|  FLEX         PARTIAL SELL (0.3161 sh remain) — will retry this session|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  0 filled  |  1 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-07T12:46:27.398541-04:00 share=25% ===
2026-09-07 12:46:27,398 INFO === options_live_micro LIVE 2026-09-07T12:46:27.398541-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 12:46:27,604 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 12:46:27,778 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 12:46:27,836 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T165056Z

- UTC timestamp: `20260907T165056Z`
- GitHub run: [#9230](https://github.com/28twagg-ops/TradingBot/actions/runs/34145041576)
- Run id: `34145041576`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260907T165056Z_live_bot.log`, `logs/action_runs/20260907T165056Z_live_options.log`, `logs/action_runs/20260907T165056Z_options_bot.log`


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
{"ts_et":"2026-09-07T12:51:01.846419-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.1,"phases_s":{"reconcile":0.3,"cancel":0.03,"manage":4.9,"protective_stops":0.41},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9230","github_run_id":"34145041576","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:50:58  INFO      Mode: exits
16:50:58  INFO        place_all_stops: checking 3 positions...
16:50:58  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:50:58  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
16:50:58  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:50:58  INFO        [positions] 3/3 (3 valid)
16:50:58  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T12:50:59.121146-04:00 share=25% ===
2026-09-07 12:50:59,121 INFO === options_live_micro LIVE 2026-09-07T12:50:59.121146-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 12:50:59,163 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 12:50:59,191 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 12:50:59,198 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T165559Z

- UTC timestamp: `20260907T165559Z`
- GitHub run: [#9231](https://github.com/28twagg-ops/TradingBot/actions/runs/34145392377)
- Run id: `34145392377`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260907T165559Z_live_bot.log`, `logs/action_runs/20260907T165559Z_live_options.log`, `logs/action_runs/20260907T165559Z_options_bot.log`


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
{"ts_et":"2026-09-07T12:56:04.247654-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.0,"phases_s":{"reconcile":0.09,"cancel":0.03,"manage":5.05,"protective_stops":0.37},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9231","github_run_id":"34145392377","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:56:00  INFO      Mode: exits
16:56:00  INFO        place_all_stops: checking 3 positions...
16:56:00  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:56:00  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
16:56:00  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:56:00  INFO        [positions] 3/3 (3 valid)
16:56:00  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T12:56:01.615871-04:00 share=25% ===
2026-09-07 12:56:01,615 INFO === options_live_micro LIVE 2026-09-07T12:56:01.615871-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 12:56:01,661 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 12:56:01,689 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 12:56:01,696 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T170101Z

- UTC timestamp: `20260907T170101Z`
- GitHub run: [#9232](https://github.com/28twagg-ops/TradingBot/actions/runs/34145732088)
- Run id: `34145732088`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260907T170101Z_live_bot.log`, `logs/action_runs/20260907T170101Z_live_options.log`, `logs/action_runs/20260907T170101Z_options_bot.log`


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
{"ts_et":"2026-09-07T13:01:08.867708-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":8.6,"phases_s":{"reconcile":0.2,"cancel":0.08,"manage":6.55,"protective_stops":1.19},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9232","github_run_id":"34145732088","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:01:02  INFO      Mode: exits
17:01:03  INFO        place_all_stops: checking 3 positions...
17:01:03  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:01:03  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
17:01:03  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:01:03  INFO        [positions] 3/3 (3 valid)
17:01:03  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T13:01:05.089230-04:00 share=25% ===
2026-09-07 13:01:05,089 INFO === options_live_micro LIVE 2026-09-07T13:01:05.089230-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 13:01:05,187 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 13:01:05,304 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 13:01:05,329 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T170557Z

- UTC timestamp: `20260907T170557Z`
- GitHub run: [#9233](https://github.com/28twagg-ops/TradingBot/actions/runs/34146092818)
- Run id: `34146092818`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`22s`
- Full logs: `logs/action_runs/20260907T170557Z_live_bot.log`, `logs/action_runs/20260907T170557Z_live_options.log`, `logs/action_runs/20260907T170557Z_options_bot.log`


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
{"ts_et":"2026-09-07T13:06:04.146638-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":12.1,"phases_s":{"reconcile":0.39,"cancel":0.22,"manage":8.55,"protective_stops":2.36},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9233","github_run_id":"34146092818","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:05:58  INFO      Mode: exits
17:05:59  INFO        place_all_stops: checking 3 positions...
17:05:59  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:05:59  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
17:05:59  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:05:59  INFO        [positions] 3/3 (3 valid)
17:06:00  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T13:06:00.948999-04:00 share=25% ===
2026-09-07 13:06:00,949 INFO === options_live_micro LIVE 2026-09-07T13:06:00.948999-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 13:06:01,157 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 13:06:01,349 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 13:06:01,408 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T171056Z

- UTC timestamp: `20260907T171056Z`
- GitHub run: [#9234](https://github.com/28twagg-ops/TradingBot/actions/runs/34146452107)
- Run id: `34146452107`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`23s`
- Full logs: `logs/action_runs/20260907T171056Z_live_bot.log`, `logs/action_runs/20260907T171056Z_live_options.log`, `logs/action_runs/20260907T171056Z_options_bot.log`


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
{"ts_et":"2026-09-07T13:11:02.884338-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":13.1,"phases_s":{"reconcile":0.4,"cancel":0.19,"manage":9.36,"protective_stops":2.47},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9234","github_run_id":"34146452107","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:10:57  INFO      Mode: exits
17:10:57  INFO        place_all_stops: checking 3 positions...
17:10:57  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:10:57  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
17:10:57  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:10:58  INFO        [positions] 3/3 (3 valid)
17:10:58  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T13:10:59.504467-04:00 share=25% ===
2026-09-07 13:10:59,504 INFO === options_live_micro LIVE 2026-09-07T13:10:59.504467-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 13:10:59,716 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 13:10:59,899 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 13:10:59,957 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T171600Z

- UTC timestamp: `20260907T171600Z`
- GitHub run: [#9235](https://github.com/28twagg-ops/TradingBot/actions/runs/34146807667)
- Run id: `34146807667`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`20s`
- Full logs: `logs/action_runs/20260907T171600Z_live_bot.log`, `logs/action_runs/20260907T171600Z_live_options.log`, `logs/action_runs/20260907T171600Z_options_bot.log`


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
{"ts_et":"2026-09-07T13:16:06.315635-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":8.1,"phases_s":{"reconcile":0.22,"cancel":0.09,"manage":6.09,"protective_stops":1.15},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9235","github_run_id":"34146807667","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:16:01  INFO      Mode: exits
17:16:01  INFO        place_all_stops: checking 3 positions...
17:16:01  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:16:01  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
17:16:01  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:16:02  INFO        [positions] 3/3 (3 valid)
17:16:02  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T13:16:03.179205-04:00 share=25% ===
2026-09-07 13:16:03,179 INFO === options_live_micro LIVE 2026-09-07T13:16:03.179205-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 13:16:03,264 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 13:16:03,351 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 13:16:03,372 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T172058Z

- UTC timestamp: `20260907T172058Z`
- GitHub run: [#9236](https://github.com/28twagg-ops/TradingBot/actions/runs/34147162815)
- Run id: `34147162815`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`19s`
- Full logs: `logs/action_runs/20260907T172058Z_live_bot.log`, `logs/action_runs/20260907T172058Z_live_options.log`, `logs/action_runs/20260907T172058Z_options_bot.log`


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
{"ts_et":"2026-09-07T13:21:04.109786-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.9,"phases_s":{"reconcile":0.12,"cancel":0.04,"manage":5.68,"protective_stops":0.57},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9236","github_run_id":"34147162815","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:20:59  INFO      Mode: exits
17:20:59  INFO        place_all_stops: checking 3 positions...
17:20:59  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:20:59  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
17:20:59  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:21:00  INFO        [positions] 3/3 (3 valid)
17:21:00  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T13:21:01.032992-04:00 share=25% ===
2026-09-07 13:21:01,033 INFO === options_live_micro LIVE 2026-09-07T13:21:01.032992-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 13:21:01,091 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 13:21:01,128 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 13:21:01,140 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T172558Z

- UTC timestamp: `20260907T172558Z`
- GitHub run: [#9237](https://github.com/28twagg-ops/TradingBot/actions/runs/34147515044)
- Run id: `34147515044`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`25s`
- Full logs: `logs/action_runs/20260907T172558Z_live_bot.log`, `logs/action_runs/20260907T172558Z_live_options.log`, `logs/action_runs/20260907T172558Z_options_bot.log`


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
{"ts_et":"2026-09-07T13:26:06.063475-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":14.5,"phases_s":{"reconcile":0.59,"cancel":0.22,"manage":10.03,"protective_stops":2.9},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9237","github_run_id":"34147515044","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:25:59  INFO      Mode: exits
17:25:59  INFO        place_all_stops: checking 3 positions...
17:25:59  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:25:59  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
17:25:59  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:26:00  INFO        [positions] 3/3 (3 valid)
17:26:00  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T13:26:01.550554-04:00 share=25% ===
2026-09-07 13:26:01,550 INFO === options_live_micro LIVE 2026-09-07T13:26:01.550554-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 13:26:02,151 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 13:26:02,359 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 13:26:02,428 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T173241Z

- UTC timestamp: `20260907T173241Z`
- GitHub run: [#9238](https://github.com/28twagg-ops/TradingBot/actions/runs/34147854457)
- Run id: `34147854457`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260907T173241Z_live_bot.log`, `logs/action_runs/20260907T173241Z_live_options.log`, `logs/action_runs/20260907T173241Z_options_bot.log`


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
{"ts_et":"2026-09-07T13:32:46.322565-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":5.9,"phases_s":{"reconcile":0.1,"cancel":0.03,"manage":4.95,"protective_stops":0.34},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9238","github_run_id":"34147854457","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:32:42  INFO      Mode: exits
17:32:42  INFO        place_all_stops: checking 3 positions...
17:32:42  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:32:42  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
17:32:42  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:32:42  INFO        [positions] 3/3 (3 valid)
17:32:42  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:32 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T13:32:43.573271-04:00 share=25% ===
2026-09-07 13:32:43,573 INFO === options_live_micro LIVE 2026-09-07T13:32:43.573271-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 13:32:43,627 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 13:32:43,658 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 13:32:43,666 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T173604Z

- UTC timestamp: `20260907T173604Z`
- GitHub run: [#9239](https://github.com/28twagg-ops/TradingBot/actions/runs/34148203630)
- Run id: `34148203630`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`26s`
- Full logs: `logs/action_runs/20260907T173604Z_live_bot.log`, `logs/action_runs/20260907T173604Z_live_options.log`, `logs/action_runs/20260907T173604Z_options_bot.log`


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
{"ts_et":"2026-09-07T13:36:11.593471-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":14.0,"phases_s":{"reconcile":0.46,"cancel":0.22,"manage":9.77,"protective_stops":2.87},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9239","github_run_id":"34148203630","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:36:05  INFO      Mode: exits
17:36:06  INFO        place_all_stops: checking 3 positions...
17:36:06  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:36:06  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
17:36:06  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:36:06  INFO        [positions] 3/3 (3 valid)
17:36:07  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T13:36:08.018285-04:00 share=25% ===
2026-09-07 13:36:08,018 INFO === options_live_micro LIVE 2026-09-07T13:36:08.018285-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 13:36:08,244 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 13:36:08,461 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 13:36:08,531 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T174057Z

- UTC timestamp: `20260907T174057Z`
- GitHub run: [#9240](https://github.com/28twagg-ops/TradingBot/actions/runs/34148540877)
- Run id: `34148540877`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260907T174057Z_live_bot.log`, `logs/action_runs/20260907T174057Z_live_options.log`, `logs/action_runs/20260907T174057Z_options_bot.log`


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
{"ts_et":"2026-09-07T13:41:02.775838-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.1,"phases_s":{"reconcile":0.28,"cancel":0.03,"manage":4.84,"protective_stops":0.39},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9240","github_run_id":"34148540877","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:40:59  INFO      Mode: exits
17:40:59  INFO        place_all_stops: checking 3 positions...
17:40:59  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:40:59  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
17:40:59  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:40:59  INFO        [positions] 3/3 (3 valid)
17:40:59  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T13:41:00.116370-04:00 share=25% ===
2026-09-07 13:41:00,116 INFO === options_live_micro LIVE 2026-09-07T13:41:00.116370-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 13:41:00,162 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 13:41:00,196 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 13:41:00,210 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T174601Z

- UTC timestamp: `20260907T174601Z`
- GitHub run: [#9241](https://github.com/28twagg-ops/TradingBot/actions/runs/34148873327)
- Run id: `34148873327`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`28s`
- Full logs: `logs/action_runs/20260907T174601Z_live_bot.log`, `logs/action_runs/20260907T174601Z_live_options.log`, `logs/action_runs/20260907T174601Z_options_bot.log`


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
{"ts_et":"2026-09-07T13:46:09.896883-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":15.3,"phases_s":{"reconcile":0.47,"cancel":0.22,"manage":10.53,"protective_stops":2.99},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9241","github_run_id":"34148873327","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:46:02  INFO      Mode: exits
17:46:03  INFO        place_all_stops: checking 3 positions...
17:46:03  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:46:03  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
17:46:03  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:46:03  INFO        [positions] 3/3 (3 valid)
17:46:04  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T13:46:05.300836-04:00 share=25% ===
2026-09-07 13:46:05,300 INFO === options_live_micro LIVE 2026-09-07T13:46:05.300836-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 13:46:05,537 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 13:46:05,749 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 13:46:05,819 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T175054Z

- UTC timestamp: `20260907T175054Z`
- GitHub run: [#9242](https://github.com/28twagg-ops/TradingBot/actions/runs/34149204946)
- Run id: `34149204946`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`20s`
- Full logs: `logs/action_runs/20260907T175054Z_live_bot.log`, `logs/action_runs/20260907T175054Z_live_options.log`, `logs/action_runs/20260907T175054Z_options_bot.log`


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
{"ts_et":"2026-09-07T13:51:00.526956-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":10.3,"phases_s":{"reconcile":0.38,"cancel":0.11,"manage":7.79,"protective_stops":1.37},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9242","github_run_id":"34149204946","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:50:55  INFO      Mode: exits
17:50:56  INFO        place_all_stops: checking 3 positions...
17:50:56  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:50:56  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
17:50:56  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:50:56  INFO        [positions] 3/3 (3 valid)
17:50:56  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T13:50:57.562899-04:00 share=25% ===
2026-09-07 13:50:57,562 INFO === options_live_micro LIVE 2026-09-07T13:50:57.562899-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 13:50:57,682 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 13:50:57,779 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 13:50:57,810 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T175556Z

- UTC timestamp: `20260907T175556Z`
- GitHub run: [#9243](https://github.com/28twagg-ops/TradingBot/actions/runs/34149538714)
- Run id: `34149538714`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`18s`
- Full logs: `logs/action_runs/20260907T175556Z_live_bot.log`, `logs/action_runs/20260907T175556Z_live_options.log`, `logs/action_runs/20260907T175556Z_options_bot.log`


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
{"ts_et":"2026-09-07T13:56:01.047730-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.7,"phases_s":{"reconcile":0.19,"cancel":0.04,"manage":5.44,"protective_stops":0.5},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9243","github_run_id":"34149538714","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:55:57  INFO      Mode: exits
17:55:57  INFO        place_all_stops: checking 3 positions...
17:55:57  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:55:57  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
17:55:57  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:55:57  INFO        [positions] 3/3 (3 valid)
17:55:57  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T13:55:58.231520-04:00 share=25% ===
2026-09-07 13:55:58,231 INFO === options_live_micro LIVE 2026-09-07T13:55:58.231520-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 13:55:58,292 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 13:55:58,328 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 13:55:58,351 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T180059Z

- UTC timestamp: `20260907T180059Z`
- GitHub run: [#9244](https://github.com/28twagg-ops/TradingBot/actions/runs/34149854970)
- Run id: `34149854970`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260907T180059Z_live_bot.log`, `logs/action_runs/20260907T180059Z_live_options.log`, `logs/action_runs/20260907T180059Z_options_bot.log`


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
{"ts_et":"2026-09-07T14:01:03.791266-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.4,"phases_s":{"reconcile":0.09,"cancel":0.03,"manage":5.45,"protective_stops":0.33},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9244","github_run_id":"34149854970","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
18:01:00  INFO      Mode: exits
18:01:00  INFO        place_all_stops: checking 3 positions...
18:01:00  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
18:01:00  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
18:01:00  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
18:01:00  INFO        [positions] 3/3 (3 valid)
18:01:00  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T14:01:01.154830-04:00 share=25% ===
2026-09-07 14:01:01,154 INFO === options_live_micro LIVE 2026-09-07T14:01:01.154830-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 14:01:01,196 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 14:01:01,223 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 14:01:01,230 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T180600Z

- UTC timestamp: `20260907T180600Z`
- GitHub run: [#9245](https://github.com/28twagg-ops/TradingBot/actions/runs/34150198112)
- Run id: `34150198112`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`18s`
- Full logs: `logs/action_runs/20260907T180600Z_live_bot.log`, `logs/action_runs/20260907T180600Z_live_options.log`, `logs/action_runs/20260907T180600Z_options_bot.log`


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
{"ts_et":"2026-09-07T14:06:05.782550-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":9.6,"phases_s":{"reconcile":0.32,"cancel":0.13,"manage":7.02,"protective_stops":1.66},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9245","github_run_id":"34150198112","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
18:06:01  INFO      Mode: exits
18:06:01  INFO        place_all_stops: checking 3 positions...
18:06:01  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
18:06:01  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
18:06:01  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
18:06:02  INFO        [positions] 3/3 (3 valid)
18:06:02  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T14:06:03.192137-04:00 share=25% ===
2026-09-07 14:06:03,192 INFO === options_live_micro LIVE 2026-09-07T14:06:03.192137-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 14:06:03,310 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 14:06:03,404 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 14:06:03,434 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T181059Z

- UTC timestamp: `20260907T181059Z`
- GitHub run: [#9246](https://github.com/28twagg-ops/TradingBot/actions/runs/34150525934)
- Run id: `34150525934`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`20s`
- Full logs: `logs/action_runs/20260907T181059Z_live_bot.log`, `logs/action_runs/20260907T181059Z_live_options.log`, `logs/action_runs/20260907T181059Z_options_bot.log`


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
{"ts_et":"2026-09-07T14:11:05.614715-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":9.9,"phases_s":{"reconcile":0.27,"cancel":0.12,"manage":7.41,"protective_stops":1.56},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9246","github_run_id":"34150525934","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
18:11:01  INFO      Mode: exits
18:11:01  INFO        place_all_stops: checking 3 positions...
18:11:01  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
18:11:01  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
18:11:01  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
18:11:01  INFO        [positions] 3/3 (3 valid)
18:11:02  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T14:11:02.733496-04:00 share=25% ===
2026-09-07 14:11:02,733 INFO === options_live_micro LIVE 2026-09-07T14:11:02.733496-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 14:11:02,857 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 14:11:02,969 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 14:11:03,005 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T181559Z

- UTC timestamp: `20260907T181559Z`
- GitHub run: [#9247](https://github.com/28twagg-ops/TradingBot/actions/runs/34150867423)
- Run id: `34150867423`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`22s`
- Full logs: `logs/action_runs/20260907T181559Z_live_bot.log`, `logs/action_runs/20260907T181559Z_live_options.log`, `logs/action_runs/20260907T181559Z_options_bot.log`


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
{"ts_et":"2026-09-07T14:16:06.238824-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":12.3,"phases_s":{"reconcile":0.41,"cancel":0.19,"manage":8.61,"protective_stops":2.5},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9247","github_run_id":"34150867423","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
18:16:00  INFO      Mode: exits
18:16:01  INFO        place_all_stops: checking 3 positions...
18:16:01  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
18:16:01  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
18:16:01  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
18:16:01  INFO        [positions] 3/3 (3 valid)
18:16:02  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T14:16:02.969389-04:00 share=25% ===
2026-09-07 14:16:02,969 INFO === options_live_micro LIVE 2026-09-07T14:16:02.969389-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 14:16:03,185 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 14:16:03,364 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 14:16:03,435 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T182100Z

- UTC timestamp: `20260907T182100Z`
- GitHub run: [#9248](https://github.com/28twagg-ops/TradingBot/actions/runs/34151198725)
- Run id: `34151198725`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260907T182100Z_live_bot.log`, `logs/action_runs/20260907T182100Z_live_options.log`, `logs/action_runs/20260907T182100Z_options_bot.log`


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
{"ts_et":"2026-09-07T14:21:07.732479-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.5,"phases_s":{"reconcile":0.13,"cancel":0.04,"manage":5.23,"protective_stops":0.55},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9248","github_run_id":"34151198725","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
18:21:01  INFO      Mode: exits
18:21:03  INFO        place_all_stops: checking 3 positions...
18:21:03  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
18:21:03  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
18:21:03  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
18:21:04  INFO        [positions] 3/3 (3 valid)
18:21:04  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T14:21:05.027771-04:00 share=25% ===
2026-09-07 14:21:05,027 INFO === options_live_micro LIVE 2026-09-07T14:21:05.027771-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 14:21:05,085 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 14:21:05,122 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 14:21:05,133 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T182556Z

- UTC timestamp: `20260907T182556Z`
- GitHub run: [#9249](https://github.com/28twagg-ops/TradingBot/actions/runs/34151535203)
- Run id: `34151535203`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`15s`
- Full logs: `logs/action_runs/20260907T182556Z_live_bot.log`, `logs/action_runs/20260907T182556Z_live_options.log`, `logs/action_runs/20260907T182556Z_options_bot.log`


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
{"ts_et":"2026-09-07T14:26:01.041984-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":5.7,"phases_s":{"reconcile":0.16,"cancel":0.03,"manage":4.74,"protective_stops":0.36},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9249","github_run_id":"34151535203","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
18:25:58  INFO      Mode: exits
18:25:58  INFO        place_all_stops: checking 3 positions...
18:25:58  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
18:25:58  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
18:25:58  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
18:25:58  INFO        [positions] 3/3 (3 valid)
18:25:58  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T14:25:58.948020-04:00 share=25% ===
2026-09-07 14:25:58,948 INFO === options_live_micro LIVE 2026-09-07T14:25:58.948020-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 14:25:58,986 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 14:25:59,006 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 14:25:59,012 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T183059Z

- UTC timestamp: `20260907T183059Z`
- GitHub run: [#9250](https://github.com/28twagg-ops/TradingBot/actions/runs/34151873909)
- Run id: `34151873909`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260907T183059Z_live_bot.log`, `logs/action_runs/20260907T183059Z_live_options.log`, `logs/action_runs/20260907T183059Z_options_bot.log`


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
{"ts_et":"2026-09-07T14:31:05.073862-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":11.9,"phases_s":{"reconcile":0.38,"cancel":0.18,"manage":8.35,"protective_stops":2.39},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9250","github_run_id":"34151873909","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
18:30:59  INFO      Mode: exits
18:31:00  INFO        place_all_stops: checking 3 positions...
18:31:00  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
18:31:00  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
18:31:00  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
18:31:01  INFO        [positions] 3/3 (3 valid)
18:31:01  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T14:31:02.032550-04:00 share=25% ===
2026-09-07 14:31:02,032 INFO === options_live_micro LIVE 2026-09-07T14:31:02.032550-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 14:31:02,239 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 14:31:02,416 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 14:31:02,501 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T183552Z

- UTC timestamp: `20260907T183552Z`
- GitHub run: [#9251](https://github.com/28twagg-ops/TradingBot/actions/runs/34152211765)
- Run id: `34152211765`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260907T183552Z_live_bot.log`, `logs/action_runs/20260907T183552Z_live_options.log`, `logs/action_runs/20260907T183552Z_options_bot.log`


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
{"ts_et":"2026-09-07T14:35:56.427235-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":5.3,"phases_s":{"reconcile":0.09,"cancel":0.03,"manage":4.43,"protective_stops":0.34},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9251","github_run_id":"34152211765","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
18:35:53  INFO      Mode: exits
18:35:53  INFO        place_all_stops: checking 3 positions...
18:35:53  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
18:35:53  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
18:35:53  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
18:35:53  INFO        [positions] 3/3 (3 valid)
18:35:53  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T14:35:54.328133-04:00 share=25% ===
2026-09-07 14:35:54,328 INFO === options_live_micro LIVE 2026-09-07T14:35:54.328133-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 14:35:54,386 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 14:35:54,415 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 14:35:54,423 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T184056Z

- UTC timestamp: `20260907T184056Z`
- GitHub run: [#9252](https://github.com/28twagg-ops/TradingBot/actions/runs/34152541851)
- Run id: `34152541851`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`20s`
- Full logs: `logs/action_runs/20260907T184056Z_live_bot.log`, `logs/action_runs/20260907T184056Z_live_options.log`, `logs/action_runs/20260907T184056Z_options_bot.log`


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
{"ts_et":"2026-09-07T14:41:01.521403-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":8.5,"phases_s":{"reconcile":0.44,"cancel":0.07,"manage":6.49,"protective_stops":0.89},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9252","github_run_id":"34152541851","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
18:40:57  INFO      Mode: exits
18:40:57  INFO        place_all_stops: checking 3 positions...
18:40:57  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
18:40:57  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
18:40:57  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
18:40:57  INFO        [positions] 3/3 (3 valid)
18:40:57  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T14:40:58.593775-04:00 share=25% ===
2026-09-07 14:40:58,593 INFO === options_live_micro LIVE 2026-09-07T14:40:58.593775-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 14:40:58,676 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 14:40:58,740 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 14:40:58,761 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T184556Z

- UTC timestamp: `20260907T184556Z`
- GitHub run: [#9253](https://github.com/28twagg-ops/TradingBot/actions/runs/34152882670)
- Run id: `34152882670`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260907T184556Z_live_bot.log`, `logs/action_runs/20260907T184556Z_live_options.log`, `logs/action_runs/20260907T184556Z_options_bot.log`


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
{"ts_et":"2026-09-07T14:46:02.124953-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":12.2,"phases_s":{"reconcile":0.39,"cancel":0.18,"manage":8.52,"protective_stops":2.54},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9253","github_run_id":"34152882670","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
18:45:57  INFO      Mode: exits
18:45:57  INFO        place_all_stops: checking 3 positions...
18:45:57  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
18:45:57  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
18:45:57  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
18:45:58  INFO        [positions] 3/3 (3 valid)
18:45:58  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T14:45:59.251802-04:00 share=25% ===
2026-09-07 14:45:59,251 INFO === options_live_micro LIVE 2026-09-07T14:45:59.251802-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 14:45:59,451 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 14:45:59,625 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 14:45:59,683 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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

## Run 20260907T185059Z

- UTC timestamp: `20260907T185059Z`
- GitHub run: [#9254](https://github.com/28twagg-ops/TradingBot/actions/runs/34153218204)
- Run id: `34153218204`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`23s`
- Full logs: `logs/action_runs/20260907T185059Z_live_bot.log`, `logs/action_runs/20260907T185059Z_live_options.log`, `logs/action_runs/20260907T185059Z_options_bot.log`


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
{"ts_et":"2026-09-07T14:51:05.329845-04:00","date":"2026-09-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":13.4,"phases_s":{"reconcile":0.6,"cancel":0.2,"manage":9.2,"protective_stops":2.69},"signals":0,"placed":0,"equity":1005240.75,"open_positions":30,"pending_orders":0,"open_lots":121,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"9254","github_run_id":"34153218204","status":"ok","data_quality":{"clean":{"n":1029,"win":50.15,"med":12.5,"avg":47.58,"pnl":15692.21},"tainted":{"n":1791,"win":33.5,"med":-38.36,"avg":12.71,"pnl":-8650.84},"keep_only":{"n":551,"win":64.25,"med":51.39,"avg":73.64,"pnl":10279.45},"keep_only_recent":{"n":343,"win":61.22,"med":53.57,"avg":90.18,"pnl":5022.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
18:50:59  INFO      Mode: exits
18:51:00  INFO        place_all_stops: checking 3 positions...
18:51:00  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
18:51:00  INFO        STOP skipped FLEX: fractional (0.3161 shares) — software exit will handle it
18:51:00  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
18:51:00  INFO        [positions] 3/3 (3 valid)
18:51:01  INFO        Daily log -> logs/daily/2026-09-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  FLEX  P&L +0.1%  $+0.04                                           HOLD|
|  LII  P&L +1.1%  $+0.38                                            HOLD|
|  AMZN  P&L +1.2%  $+0.41                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-09-07T14:51:01.963311-04:00 share=25% ===
2026-09-07 14:51:01,963 INFO === options_live_micro LIVE 2026-09-07T14:51:01.963311-04:00 share=25% ===
Live account equity $230.56 cash $126.02 #225458845 options_level=3
2026-09-07 14:51:02,194 INFO Live account equity $230.56 cash $126.02 #225458845 options_level=3
Live micro: manage/exits only
2026-09-07 14:51:02,395 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-07 14:51:02,457 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
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
## Ledger health — 2026-09-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1034 | WARN | <<<
| Missing exit records (post) |  1032 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2000 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-07_data_quality.csv
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
