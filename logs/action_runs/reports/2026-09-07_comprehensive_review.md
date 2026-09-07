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
