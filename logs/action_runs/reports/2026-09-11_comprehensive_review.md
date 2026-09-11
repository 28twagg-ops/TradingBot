# Daily Comprehensive Action Review - 2026-09-11

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260911T130123Z

- UTC timestamp: `20260911T130123Z`
- GitHub run: [#9712](https://github.com/28twagg-ops/TradingBot/actions/runs/34601859849)
- Run id: `34601859849`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260911T130123Z_live_bot.log`, `logs/action_runs/20260911T130123Z_live_options.log`, `logs/action_runs/20260911T130123Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1176 | 48.5 | -23.1 | +40.5 | $+15,122 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 584 | 63.2 | +51.2 | +67.1 | $+10,415 |
| KEEP-only recent | 387 | 61.0 | +53.3 | +80.0 | $+5,770 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T09:01:29.574847-04:00","date":"2026-09-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.59},"signals":0,"placed":0,"equity":998495.13,"open_positions":27,"pending_orders":0,"open_lots":91,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9712","github_run_id":"34601859849","status":"ok","data_quality":{"clean":{"n":1176,"win":48.47,"med":-23.12,"avg":40.52,"pnl":15122.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":584,"win":63.18,"med":51.18,"avg":67.07,"pnl":10415.45},"keep_only_recent":{"n":387,"win":60.98,"med":53.33,"avg":79.96,"pnl":5770.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
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
|  Equity                                                         $228.39|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $228.39|
|  Cash                                                           $159.03|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $69.36|
|  Open P&L                                                        $+1.27|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ABBV     Pullback50      $34.38     $254.21  $256.85  +1.0%   $+0.35  |
|  RL       MomReversal     $34.98     $335.08  $344.11  +2.7%   $+0.92  |
|                                                                        |
|  Total invested                                                  $69.36|
|  Total open P&L                                                  $+1.27|
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
|  2026-09-10  SELL  AES  Pullback50  $34.05  P&L $-0.00                 |
|  2026-09-10  SELL  ABBV  Pullback50  $33.90  P&L $-0.20                |
|  2026-09-10  SELL  AES  Pullback50  $34.09  P&L $+0.01                 |
|  2026-09-10  SELL  CNM  MomReversal  $34.08  P&L $-0.23                |
|  2026-09-10  SELL  TXT  MomReversal  $33.88  P&L $-0.43                |
|  2026-09-10  SELL  FSLR  MomReversal  $33.83  P&L $-0.48               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-11T09:01:25.765856-04:00 share=25% ===
2026-09-11 09:01:25,765 INFO === options_live_micro LIVE 2026-09-11T09:01:25.765856-04:00 share=25% ===
Live account equity $228.39 cash $159.03 #225458845 options_level=3
2026-09-11 09:01:25,981 INFO Live account equity $228.39 cash $159.03 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-11 09:01:26,039 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-11 09:01:26,108 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (170 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    91 | INFO |
| Total closed lots           |  2165 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1176 med=-23.1% | TAINTED n=1827 med=-38.8% | KEEP-only n=584 med=+51.2% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=228.39 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T130602Z

- UTC timestamp: `20260911T130602Z`
- GitHub run: [#9713](https://github.com/28twagg-ops/TradingBot/actions/runs/34602314846)
- Run id: `34602314846`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260911T130602Z_live_bot.log`, `logs/action_runs/20260911T130602Z_live_options.log`, `logs/action_runs/20260911T130602Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1176 | 48.5 | -23.1 | +40.5 | $+15,122 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 584 | 63.2 | +51.2 | +67.1 | $+10,415 |
| KEEP-only recent | 387 | 61.0 | +53.3 | +80.0 | $+5,770 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T09:06:06.908100-04:00","date":"2026-09-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.41},"signals":0,"placed":0,"equity":998511.0,"open_positions":27,"pending_orders":0,"open_lots":91,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9713","github_run_id":"34602314846","status":"ok","data_quality":{"clean":{"n":1176,"win":48.47,"med":-23.12,"avg":40.52,"pnl":15122.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":584,"win":63.18,"med":51.18,"avg":67.07,"pnl":10415.45},"keep_only_recent":{"n":387,"win":60.98,"med":53.33,"avg":79.96,"pnl":5770.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:06:03  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $228.39|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $228.39|
|  Cash                                                           $159.03|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $69.36|
|  Open P&L                                                        $+1.28|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ABBV     Pullback50      $34.39     $254.21  $256.89  +1.1%   $+0.36  |
|  RL       MomReversal     $34.98     $335.08  $344.11  +2.7%   $+0.92  |
|                                                                        |
|  Total invested                                                  $69.36|
|  Total open P&L                                                  $+1.28|
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
|  2026-09-10  SELL  AES  Pullback50  $34.05  P&L $-0.00                 |
|  2026-09-10  SELL  ABBV  Pullback50  $33.90  P&L $-0.20                |
|  2026-09-10  SELL  AES  Pullback50  $34.09  P&L $+0.01                 |
|  2026-09-10  SELL  CNM  MomReversal  $34.08  P&L $-0.23                |
|  2026-09-10  SELL  TXT  MomReversal  $33.88  P&L $-0.43                |
|  2026-09-10  SELL  FSLR  MomReversal  $33.83  P&L $-0.48               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-11T09:06:04.194446-04:00 share=25% ===
2026-09-11 09:06:04,194 INFO === options_live_micro LIVE 2026-09-11T09:06:04.194446-04:00 share=25% ===
Live account equity $228.39 cash $159.03 #225458845 options_level=3
2026-09-11 09:06:04,263 INFO Live account equity $228.39 cash $159.03 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-11 09:06:04,275 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-11 09:06:04,287 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (170 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    91 | INFO |
| Total closed lots           |  2165 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1176 med=-23.1% | TAINTED n=1827 med=-38.8% | KEEP-only n=584 med=+51.2% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=228.39 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T131104Z

- UTC timestamp: `20260911T131104Z`
- GitHub run: [#9714](https://github.com/28twagg-ops/TradingBot/actions/runs/34602774458)
- Run id: `34602774458`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260911T131104Z_live_bot.log`, `logs/action_runs/20260911T131104Z_live_options.log`, `logs/action_runs/20260911T131104Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1176 | 48.5 | -23.1 | +40.5 | $+15,122 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 584 | 63.2 | +51.2 | +67.1 | $+10,415 |
| KEEP-only recent | 387 | 61.0 | +53.3 | +80.0 | $+5,770 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T09:11:11.919761-04:00","date":"2026-09-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.46},"signals":0,"placed":0,"equity":998534.99,"open_positions":27,"pending_orders":0,"open_lots":91,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9714","github_run_id":"34602774458","status":"ok","data_quality":{"clean":{"n":1176,"win":48.47,"med":-23.12,"avg":40.52,"pnl":15122.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":584,"win":63.18,"med":51.18,"avg":67.07,"pnl":10415.45},"keep_only_recent":{"n":387,"win":60.98,"med":53.33,"avg":79.96,"pnl":5770.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
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
|  Equity                                                         $228.21|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $228.21|
|  Cash                                                           $159.03|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $69.18|
|  Open P&L                                                        $+1.10|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ABBV     Pullback50      $34.21     $254.21  $255.55  +0.5%   $+0.18  |
|  RL       MomReversal     $34.98     $335.08  $344.11  +2.7%   $+0.92  |
|                                                                        |
|  Total invested                                                  $69.18|
|  Total open P&L                                                  $+1.10|
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
|  2026-09-10  SELL  AES  Pullback50  $34.05  P&L $-0.00                 |
|  2026-09-10  SELL  ABBV  Pullback50  $33.90  P&L $-0.20                |
|  2026-09-10  SELL  AES  Pullback50  $34.09  P&L $+0.01                 |
|  2026-09-10  SELL  CNM  MomReversal  $34.08  P&L $-0.23                |
|  2026-09-10  SELL  TXT  MomReversal  $33.88  P&L $-0.43                |
|  2026-09-10  SELL  FSLR  MomReversal  $33.83  P&L $-0.48               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-11T09:11:08.239696-04:00 share=25% ===
2026-09-11 09:11:08,239 INFO === options_live_micro LIVE 2026-09-11T09:11:08.239696-04:00 share=25% ===
Live account equity $228.21 cash $159.03 #225458845 options_level=3
2026-09-11 09:11:08,447 INFO Live account equity $228.21 cash $159.03 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-11 09:11:08,584 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-11 09:11:08,637 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (170 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    91 | INFO |
| Total closed lots           |  2165 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1176 med=-23.1% | TAINTED n=1827 med=-38.8% | KEEP-only n=584 med=+51.2% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=228.21 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T131601Z

- UTC timestamp: `20260911T131601Z`
- GitHub run: [#9715](https://github.com/28twagg-ops/TradingBot/actions/runs/34603233053)
- Run id: `34603233053`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260911T131601Z_live_bot.log`, `logs/action_runs/20260911T131601Z_live_options.log`, `logs/action_runs/20260911T131601Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1176 | 48.5 | -23.1 | +40.5 | $+15,122 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 584 | 63.2 | +51.2 | +67.1 | $+10,415 |
| KEEP-only recent | 387 | 61.0 | +53.3 | +80.0 | $+5,770 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T09:16:06.011008-04:00","date":"2026-09-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":998588.06,"open_positions":27,"pending_orders":0,"open_lots":91,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9715","github_run_id":"34603233053","status":"ok","data_quality":{"clean":{"n":1176,"win":48.47,"med":-23.12,"avg":40.52,"pnl":15122.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":584,"win":63.18,"med":51.18,"avg":67.07,"pnl":10415.45},"keep_only_recent":{"n":387,"win":60.98,"med":53.33,"avg":79.96,"pnl":5770.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:16:02  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $228.21|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $228.21|
|  Cash                                                           $159.03|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $69.18|
|  Open P&L                                                        $+1.10|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ABBV     Pullback50      $34.21     $254.21  $255.55  +0.5%   $+0.18  |
|  RL       MomReversal     $34.98     $335.08  $344.11  +2.7%   $+0.92  |
|                                                                        |
|  Total invested                                                  $69.18|
|  Total open P&L                                                  $+1.10|
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
|  2026-09-10  SELL  AES  Pullback50  $34.05  P&L $-0.00                 |
|  2026-09-10  SELL  ABBV  Pullback50  $33.90  P&L $-0.20                |
|  2026-09-10  SELL  AES  Pullback50  $34.09  P&L $+0.01                 |
|  2026-09-10  SELL  CNM  MomReversal  $34.08  P&L $-0.23                |
|  2026-09-10  SELL  TXT  MomReversal  $33.88  P&L $-0.43                |
|  2026-09-10  SELL  FSLR  MomReversal  $33.83  P&L $-0.48               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-11T09:16:03.170860-04:00 share=25% ===
2026-09-11 09:16:03,170 INFO === options_live_micro LIVE 2026-09-11T09:16:03.170860-04:00 share=25% ===
Live account equity $228.21 cash $159.03 #225458845 options_level=3
2026-09-11 09:16:03,222 INFO Live account equity $228.21 cash $159.03 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-11 09:16:03,233 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-11 09:16:03,241 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (170 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    91 | INFO |
| Total closed lots           |  2165 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1176 med=-23.1% | TAINTED n=1827 med=-38.8% | KEEP-only n=584 med=+51.2% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=228.21 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T132114Z

- UTC timestamp: `20260911T132114Z`
- GitHub run: [#9716](https://github.com/28twagg-ops/TradingBot/actions/runs/34603702497)
- Run id: `34603702497`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260911T132114Z_live_bot.log`, `logs/action_runs/20260911T132114Z_live_options.log`, `logs/action_runs/20260911T132114Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1176 | 48.5 | -23.1 | +40.5 | $+15,122 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 584 | 63.2 | +51.2 | +67.1 | $+10,415 |
| KEEP-only recent | 387 | 61.0 | +53.3 | +80.0 | $+5,770 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T09:21:20.086925-04:00","date":"2026-09-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.13},"signals":0,"placed":0,"equity":998588.8,"open_positions":27,"pending_orders":0,"open_lots":91,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9716","github_run_id":"34603702497","status":"ok","data_quality":{"clean":{"n":1176,"win":48.47,"med":-23.12,"avg":40.52,"pnl":15122.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":584,"win":63.18,"med":51.18,"avg":67.07,"pnl":10415.45},"keep_only_recent":{"n":387,"win":60.98,"med":53.33,"avg":79.96,"pnl":5770.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:21:15  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $228.21|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $228.21|
|  Cash                                                           $159.03|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $69.18|
|  Open P&L                                                        $+1.10|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ABBV     Pullback50      $34.21     $254.21  $255.55  +0.5%   $+0.18  |
|  RL       MomReversal     $34.98     $335.08  $344.11  +2.7%   $+0.92  |
|                                                                        |
|  Total invested                                                  $69.18|
|  Total open P&L                                                  $+1.10|
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
|  2026-09-10  SELL  AES  Pullback50  $34.05  P&L $-0.00                 |
|  2026-09-10  SELL  ABBV  Pullback50  $33.90  P&L $-0.20                |
|  2026-09-10  SELL  AES  Pullback50  $34.09  P&L $+0.01                 |
|  2026-09-10  SELL  CNM  MomReversal  $34.08  P&L $-0.23                |
|  2026-09-10  SELL  TXT  MomReversal  $33.88  P&L $-0.43                |
|  2026-09-10  SELL  FSLR  MomReversal  $33.83  P&L $-0.48               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-11T09:21:16.999579-04:00 share=25% ===
2026-09-11 09:21:16,999 INFO === options_live_micro LIVE 2026-09-11T09:21:16.999579-04:00 share=25% ===
Live account equity $228.21 cash $159.03 #225458845 options_level=3
2026-09-11 09:21:17,061 INFO Live account equity $228.21 cash $159.03 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-11 09:21:17,073 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-11 09:21:17,086 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (170 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    91 | INFO |
| Total closed lots           |  2165 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1176 med=-23.1% | TAINTED n=1827 med=-38.8% | KEEP-only n=584 med=+51.2% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=228.21 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T132609Z

- UTC timestamp: `20260911T132609Z`
- GitHub run: [#9717](https://github.com/28twagg-ops/TradingBot/actions/runs/34604175612)
- Run id: `34604175612`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260911T132609Z_live_bot.log`, `logs/action_runs/20260911T132609Z_live_options.log`, `logs/action_runs/20260911T132609Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1176 | 48.5 | -23.1 | +40.5 | $+15,122 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 584 | 63.2 | +51.2 | +67.1 | $+10,415 |
| KEEP-only recent | 387 | 61.0 | +53.3 | +80.0 | $+5,770 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T09:26:15.992436-04:00","date":"2026-09-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.49},"signals":0,"placed":0,"equity":998581.0,"open_positions":27,"pending_orders":0,"open_lots":91,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9717","github_run_id":"34604175612","status":"ok","data_quality":{"clean":{"n":1176,"win":48.47,"med":-23.12,"avg":40.52,"pnl":15122.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":584,"win":63.18,"med":51.18,"avg":67.07,"pnl":10415.45},"keep_only_recent":{"n":387,"win":60.98,"med":53.33,"avg":79.96,"pnl":5770.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:26:10  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $228.50|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $228.50|
|  Cash                                                           $159.03|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $69.47|
|  Open P&L                                                        $+1.38|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ABBV     Pullback50      $34.49     $254.21  $257.70  +1.4%   $+0.47  |
|  RL       MomReversal     $34.98     $335.08  $344.11  +2.7%   $+0.92  |
|                                                                        |
|  Total invested                                                  $69.47|
|  Total open P&L                                                  $+1.38|
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
|  2026-09-10  SELL  AES  Pullback50  $34.05  P&L $-0.00                 |
|  2026-09-10  SELL  ABBV  Pullback50  $33.90  P&L $-0.20                |
|  2026-09-10  SELL  AES  Pullback50  $34.09  P&L $+0.01                 |
|  2026-09-10  SELL  CNM  MomReversal  $34.08  P&L $-0.23                |
|  2026-09-10  SELL  TXT  MomReversal  $33.88  P&L $-0.43                |
|  2026-09-10  SELL  FSLR  MomReversal  $33.83  P&L $-0.48               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-11T09:26:12.574075-04:00 share=25% ===
2026-09-11 09:26:12,574 INFO === options_live_micro LIVE 2026-09-11T09:26:12.574075-04:00 share=25% ===
Live account equity $228.50 cash $159.03 #225458845 options_level=3
2026-09-11 09:26:12,782 INFO Live account equity $228.50 cash $159.03 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-11 09:26:12,879 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-11 09:26:12,948 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (170 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    91 | INFO |
| Total closed lots           |  2165 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1176 med=-23.1% | TAINTED n=1827 med=-38.8% | KEEP-only n=584 med=+51.2% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=228.5 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T133108Z

- UTC timestamp: `20260911T133108Z`
- GitHub run: [#9718](https://github.com/28twagg-ops/TradingBot/actions/runs/34604648251)
- Run id: `34604648251`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260911T133108Z_live_bot.log`, `logs/action_runs/20260911T133108Z_live_options.log`, `logs/action_runs/20260911T133108Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1176 | 48.5 | -23.1 | +40.5 | $+15,122 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 584 | 63.2 | +51.2 | +67.1 | $+10,415 |
| KEEP-only recent | 387 | 61.0 | +53.3 | +80.0 | $+5,770 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T09:26:15.992436-04:00","date":"2026-09-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.49},"signals":0,"placed":0,"equity":998581.0,"open_positions":27,"pending_orders":0,"open_lots":91,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9717","github_run_id":"34604175612","status":"ok","data_quality":{"clean":{"n":1176,"win":48.47,"med":-23.12,"avg":40.52,"pnl":15122.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":584,"win":63.18,"med":51.18,"avg":67.07,"pnl":10415.45},"keep_only_recent":{"n":387,"win":60.98,"med":53.33,"avg":79.96,"pnl":5770.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:31:09  INFO      Mode: morning_prep
13:31:11  INFO        [prep_positions] 2/2 (2 valid)
13:31:11  INFO      Fetching tickers (universe=both)...
13:31:11  INFO        S&P 500: 503
13:31:11  INFO        MidCap 400: 400
13:31:11  INFO        Total: 903 tickers
13:31:13  INFO        [prep_universe] 40/901 (40 valid)
13:31:15  INFO        [prep_universe] 80/901 (80 valid)
13:31:17  INFO        [prep_universe] 120/901 (120 valid)
13:31:18  INFO        [prep_universe] 160/901 (160 valid)
13:31:19  INFO        [prep_universe] 200/901 (199 valid)
13:31:26  INFO        [prep_universe] 240/901 (238 valid)
13:31:37  INFO        [prep_universe] 280/901 (278 valid)
13:31:50  INFO        [prep_universe] 320/901 (318 valid)
13:32:00  INFO        [prep_universe] 360/901 (358 valid)
13:32:14  INFO        [prep_universe] 400/901 (398 valid)
13:32:24  INFO        [prep_universe] 440/901 (438 valid)
13:32:37  INFO        [prep_universe] 480/901 (478 valid)
13:32:50  INFO        [prep_universe] 520/901 (518 valid)
13:33:00  INFO        [prep_universe] 560/901 (558 valid)
13:33:13  INFO        [prep_universe] 600/901 (598 valid)
13:33:24  INFO        [prep_universe] 640/901 (638 valid)
13:33:37  INFO        [prep_universe] 680/901 (678 valid)
13:33:50  INFO        [prep_universe] 720/901 (718 valid)
13:34:00  INFO        [prep_universe] 760/901 (758 valid)
13:34:13  INFO        [prep_universe] 800/901 (798 valid)
13:34:24  INFO        [prep_universe] 840/901 (838 valid)
13:34:37  INFO        [prep_universe] 880/901 (878 valid)
13:34:44  INFO        [prep_universe] 901/901 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.91|
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
|  Invested                                                        $68.88|
|  Open P&L                                                        $+0.79|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ABBV     Pullback50      $34.26     $254.21  $255.93  +0.7%   $+0.23  |
|  RL       MomReversal     $34.62     $335.08  $340.62  +1.7%   $+0.56  |
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
|  Signal candidates                                                   39|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-11T09:34:46.396217-04:00 share=25% ===
2026-09-11 09:34:46,396 INFO === options_live_micro LIVE 2026-09-11T09:34:46.396217-04:00 share=25% ===
Live account equity $228.00 cash $159.03 #225458845 options_level=3
2026-09-11 09:34:46,599 INFO Live account equity $228.00 cash $159.03 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-11 09:34:46,778 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-11 09:34:46,904 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=91 paper_keys=yes dry_run=False
  alpaca positions=24
  FLAG b900|S411|2ac69311 missing from Alpaca
  FLAG b805|S404|933ff6a9 missing from Alpaca
  FLAG b804|S404|183ba985 missing from Alpaca
  FLAG b781|S397|747e68a7 missing from Alpaca
  FLAG b780|S397|9e1f70ce missing from Alpaca
  FLAG b285|S351|355c8ee9 missing from Alpaca
  FLAG b284|S351|d8b95c2b missing from Alpaca
  FLAG b905|S411|8ee5841b missing from Alpaca
  FLAG b904|S411|135984dc missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$999,314.72
  buying_power=$3,933,670.48 cash=$1,032,327.72
  open option orders: 14
    AVGO260911C00400000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.01
    AMD260914C00547500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.36
    UPST260918C00027500 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    GOOGL260914C00345000 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
    MARA260911C00011500 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
  open option positions: 23
    AMD260914C00550000 qty=2 mkt=$22.00
    AMD260914C00552500 qty=-1 mkt=$-55.00
    AMZN260914C00262500 qty=2 mkt=$68.00
    AVGO260911C00400000 qty=1 mkt=$0.00
    CRWD260911C00222500 qty=-1 mkt=$-9.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-11T09:34:49.611278-04:00 ===

[Run context]
Paper auth OK — equity $999317.72, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-11 09:34:51,282 INFO   EXIT [b393|lab0393_s363_w2_1005_1045_r2|S363] stop_loss (-54.8%) SELL 1 SMCI260918C00042000 @<= 0.25
  EXIT [b862|lab0862_s408_w4_1120_1135_r1|S408] stop_loss (-100.0%) SELL failed CRWD260911C00235000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-11 09:34:53,796 INFO   EXIT [b239|lab0239_s401_w3_1045_1120_r2|S401] take_profit (+181.6%) SELL 1 GOOGL260914C00345000 @<= 1.08
  EXIT [b1055|lab1055_s165_w2_1005_1045_r2|S165] stop_loss (-100.0%) SELL failed SHOP260911C00146000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b1054|lab1054_s165_w2_1005_1045_r1|S165] stop_loss (-100.0%) SELL failed SHOP260911C00146000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b802|lab0802_s404_w2_1005_1045_r1|S404] stop_loss (-81.7%) SELL failed AMD260914C00550000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b779|lab0779_s397_w2_1005_1045_r2|S397] stop_loss (-81.7%) SELL failed AMD260914C00550000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-11 09:34:55,986 INFO   EXIT [b1150|lab1150_s164_w1_0928_1005_r1|S164] stop_loss (-96.9%) SELL 1 ZS260911C00180000 @<= 0.01
2026-09-11 09:34:56,477 INFO   EXIT [b267|lab0267_s403_w3_1045_1120_r2|S403] take_profit (+129.0%) SELL 1 V260911C00372500 @<= 0.63
  EXIT [b330|lab0330_s357_w2_1005_1045_r1|S357] stop_loss (-91.1%) SELL failed PATH260925C00017000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-11 09:34:58,146 INFO   EXIT [b860|lab0860_s408_w3_1045_1120_r1|S408] stop_loss (-70.0%) SELL 1 TSLA260914C00405000 @<= 0.03
Protective stops: placed=0 upgraded=0 already=7 failed=11 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260911T133646Z

- UTC timestamp: `20260911T133646Z`
- GitHub run: [#9719](https://github.com/28twagg-ops/TradingBot/actions/runs/34605133737)
- Run id: `34605133737`
- Live bot: exit=`0`, duration=`218s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260911T133646Z_live_bot.log`, `logs/action_runs/20260911T133646Z_live_options.log`, `logs/action_runs/20260911T133646Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1176 | 48.5 | -23.1 | +40.5 | $+15,122 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 584 | 63.2 | +51.2 | +67.1 | $+10,415 |
| KEEP-only recent | 387 | 61.0 | +53.3 | +80.0 | $+5,770 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T09:26:15.992436-04:00","date":"2026-09-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.49},"signals":0,"placed":0,"equity":998581.0,"open_positions":27,"pending_orders":0,"open_lots":91,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9717","github_run_id":"34604175612","status":"ok","data_quality":{"clean":{"n":1176,"win":48.47,"med":-23.12,"avg":40.52,"pnl":15122.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":584,"win":63.18,"med":51.18,"avg":67.07,"pnl":10415.45},"keep_only_recent":{"n":387,"win":60.98,"med":53.33,"avg":79.96,"pnl":5770.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:36:48  INFO      Mode: morning_prep
13:36:49  INFO        [prep_positions] 2/2 (2 valid)
13:36:49  INFO      Fetching tickers (universe=both)...
13:36:49  INFO        S&P 500: 503
13:36:49  INFO        MidCap 400: 400
13:36:49  INFO        Total: 903 tickers
13:36:50  INFO        [prep_universe] 40/901 (40 valid)
13:36:52  INFO        [prep_universe] 80/901 (80 valid)
13:36:53  INFO        [prep_universe] 120/901 (120 valid)
13:36:55  INFO        [prep_universe] 160/901 (160 valid)
13:36:56  INFO        [prep_universe] 200/901 (199 valid)
13:37:03  INFO        [prep_universe] 240/901 (238 valid)
13:37:14  INFO        [prep_universe] 280/901 (278 valid)
13:37:27  INFO        [prep_universe] 320/901 (318 valid)
13:37:41  INFO        [prep_universe] 360/901 (358 valid)
13:37:51  INFO        [prep_universe] 400/901 (398 valid)
13:38:04  INFO        [prep_universe] 440/901 (438 valid)
13:38:15  INFO        [prep_universe] 480/901 (478 valid)
13:38:28  INFO        [prep_universe] 520/901 (518 valid)
13:38:39  INFO        [prep_universe] 560/901 (558 valid)
13:38:52  INFO        [prep_universe] 600/901 (598 valid)
13:39:02  INFO        [prep_universe] 640/901 (638 valid)
13:39:16  INFO        [prep_universe] 680/901 (678 valid)
13:39:26  INFO        [prep_universe] 720/901 (718 valid)
13:39:39  INFO        [prep_universe] 760/901 (758 valid)
13:39:50  INFO        [prep_universe] 800/901 (798 valid)
13:40:03  INFO        [prep_universe] 840/901 (838 valid)
13:40:14  INFO        [prep_universe] 880/901 (878 valid)
13:40:21  INFO        [prep_universe] 901/901 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $228.12|
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
|  Invested                                                        $69.09|
|  Open P&L                                                        $+1.00|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ABBV     Pullback50      $34.58     $254.21  $258.31  +1.6%   $+0.55  |
|  RL       MomReversal     $34.51     $335.08  $339.54  +1.3%   $+0.45  |
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
|  Signal candidates                                                   34|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-11T09:40:24.935991-04:00 share=25% ===
2026-09-11 09:40:24,936 INFO === options_live_micro LIVE 2026-09-11T09:40:24.935991-04:00 share=25% ===
Live account equity $228.20 cash $159.03 #225458845 options_level=3
2026-09-11 09:40:25,158 INFO Live account equity $228.20 cash $159.03 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-11 09:40:25,364 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-11 09:40:25,521 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=91 paper_keys=yes dry_run=False
  alpaca positions=23
  FLAG b900|S411|2ac69311 missing from Alpaca
  FLAG b805|S404|933ff6a9 missing from Alpaca
  FLAG b804|S404|183ba985 missing from Alpaca
  FLAG b781|S397|747e68a7 missing from Alpaca
  FLAG b780|S397|9e1f70ce missing from Alpaca
  FLAG b861|S408|63fea2cf missing from Alpaca
  FLAG b860|S408|0b8c0d6d missing from Alpaca
  FLAG b285|S351|355c8ee9 missing from Alpaca
  FLAG b284|S351|d8b95c2b missing from Alpaca
  FLAG b905|S411|8ee5841b missing from Alpaca
  FLAG b904|S411|135984dc missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$999,598.12
  buying_power=$3,934,175.88 cash=$1,032,536.62
  open option orders: 12
    AVGO260911C00400000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.01
    AMD260914C00547500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.36
    UPST260918C00027500 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    MARA260911C00011500 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    MARA261002C00012500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 22
    AMD260914C00550000 qty=2 mkt=$12.00
    AMD260914C00552500 qty=-1 mkt=$-20.00
    AMZN260914C00262500 qty=2 mkt=$62.00
    AVGO260911C00400000 qty=1 mkt=$0.00
    CRWD260911C00222500 qty=-1 mkt=$-3.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-11T09:40:29.155287-04:00 ===

[Run context]
Paper auth OK — equity $999614.12, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-11 09:40:31,379 INFO   EXIT [b392|lab0392_s363_w2_1005_1045_r1|S363] stop_loss (-54.8%) SELL 1 SMCI260918C00042000 @<= 0.29
  EXIT [b862|lab0862_s408_w4_1120_1135_r1|S408] stop_loss (-100.0%) SELL failed CRWD260911C00235000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b1055|lab1055_s165_w2_1005_1045_r2|S165] stop_loss (-100.0%) SELL failed SHOP260911C00146000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b1054|lab1054_s165_w2_1005_1045_r1|S165] stop_loss (-100.0%) SELL failed SHOP260911C00146000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b802|lab0802_s404_w2_1005_1045_r1|S404] stop_loss (-90.0%) SELL failed AMD260914C00550000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b779|lab0779_s397_w2_1005_1045_r2|S397] stop_loss (-90.0%) SELL failed AMD260914C00550000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-11 09:40:35,153 INFO   EXIT [b1053|lab1053_s165_w1_0928_1005_r2|S165] stop_loss (-96.9%) SELL 1 ZS260911C00180000 @<= 0.02
2026-09-11 09:40:36,893 INFO   EXIT [b238|lab0238_s401_w3_1045_1120_r1|S401] take_profit (+55.3%) SELL 1 GOOGL260914C00345000 @<= 0.59
  EXIT [b330|lab0330_s357_w2_1005_1045_r1|S357] stop_loss (-88.9%) SELL failed PATH260925C00017000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=1 upgraded=0 already=9 failed=7 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260911T134258Z

- UTC timestamp: `20260911T134258Z`
- GitHub run: [#9720](https://github.com/28twagg-ops/TradingBot/actions/runs/34605611966)
- Run id: `34605611966`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260911T134258Z_live_bot.log`, `logs/action_runs/20260911T134258Z_live_options.log`, `logs/action_runs/20260911T134258Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1176 | 48.5 | -23.1 | +40.5 | $+15,122 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 584 | 63.2 | +51.2 | +67.1 | $+10,415 |
| KEEP-only recent | 387 | 61.0 | +53.3 | +80.0 | $+5,770 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T09:26:15.992436-04:00","date":"2026-09-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.49},"signals":0,"placed":0,"equity":998581.0,"open_positions":27,"pending_orders":0,"open_lots":91,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9717","github_run_id":"34604175612","status":"ok","data_quality":{"clean":{"n":1176,"win":48.47,"med":-23.12,"avg":40.52,"pnl":15122.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":584,"win":63.18,"med":51.18,"avg":67.07,"pnl":10415.45},"keep_only_recent":{"n":387,"win":60.98,"med":53.33,"avg":79.96,"pnl":5770.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:42:59  INFO      Mode: morning_prep
13:43:00  INFO        [prep_positions] 2/2 (2 valid)
13:43:00  INFO        Universe cache hit: 903 tickers (tickers_2026-09-11.json)
13:43:01  INFO        [prep_universe] 40/901 (40 valid)
13:43:02  INFO        [prep_universe] 80/901 (80 valid)
13:43:03  INFO        [prep_universe] 120/901 (120 valid)
13:43:05  INFO        [prep_universe] 160/901 (160 valid)
13:43:06  INFO        [prep_universe] 200/901 (199 valid)
13:43:13  INFO        [prep_universe] 240/901 (238 valid)
13:43:26  INFO        [prep_universe] 280/901 (278 valid)
13:43:37  INFO        [prep_universe] 320/901 (318 valid)
13:43:50  INFO        [prep_universe] 360/901 (358 valid)
13:44:03  INFO        [prep_universe] 400/901 (398 valid)
13:44:13  INFO        [prep_universe] 440/901 (438 valid)
13:44:26  INFO        [prep_universe] 480/901 (478 valid)
13:44:39  INFO        [prep_universe] 520/901 (518 valid)
13:44:49  INFO        [prep_universe] 560/901 (558 valid)
13:45:02  INFO        [prep_universe] 600/901 (598 valid)
13:45:13  INFO        [prep_universe] 640/901 (638 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260911T134633Z

- UTC timestamp: `20260911T134633Z`
- GitHub run: [#9721](https://github.com/28twagg-ops/TradingBot/actions/runs/34606093916)
- Run id: `34606093916`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260911T134633Z_live_bot.log`, `logs/action_runs/20260911T134633Z_live_options.log`, `logs/action_runs/20260911T134633Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1176 | 48.5 | -23.1 | +40.5 | $+15,122 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 584 | 63.2 | +51.2 | +67.1 | $+10,415 |
| KEEP-only recent | 387 | 61.0 | +53.3 | +80.0 | $+5,770 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T09:26:15.992436-04:00","date":"2026-09-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.49},"signals":0,"placed":0,"equity":998581.0,"open_positions":27,"pending_orders":0,"open_lots":91,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9717","github_run_id":"34604175612","status":"ok","data_quality":{"clean":{"n":1176,"win":48.47,"med":-23.12,"avg":40.52,"pnl":15122.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":584,"win":63.18,"med":51.18,"avg":67.07,"pnl":10415.45},"keep_only_recent":{"n":387,"win":60.98,"med":53.33,"avg":79.96,"pnl":5770.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
... (70 earlier lines - see full log file)
|  RL       MomReversal     $34.21     $335.08  $336.51  +0.4%   $+0.15  |
|                                                                        |
|  Total invested                                                  $68.85|
|  Total open P&L                                                  $+0.76|
|  Buys today: 0  |  entry cap: 1  |  max open: 3                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (23051.1m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  RL  P&L +0.4%  $+0.15                                             HOLD|
|  ABBV  P&L +1.8%  $+0.61                          EXIT: midline (+1.8%)|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 1 | filled 1 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 1|
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
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  27                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      eq     $255.90  47.0   -2.80   50MA bounce (+|
|  ADI      Pullback50      eq     $371.77  48.8   -2.43   50MA bounce (-|
|  AME      Pullback50      eq     $240.31  51.0   -2.78   50MA bounce (-|
|  ADP      Pullback50      eq     $265.87  31.5   -2.83   50MA bounce (+|
|  TECH     Pullback50      eq     $72.23   46.9   -2.33   50MA bounce (+|
|  CTAS     Pullback50      eq     $200.69  43.2   -3.10   50MA bounce (+|
|  DRI      Pullback50      eq     $209.04  35.7   -2.93   50MA bounce (-|
|  DLR      Pullback50      eq     $188.21  46.1   -1.56   50MA bounce (+|
|  EME      Pullback50      eq     $767.48  47.7   -2.88   50MA bounce (-|
|  EQIX     Pullback50      eq     $1041.~  42.8   -1.92   50MA bounce (-|
|  FFIV     Pullback50      eq     $406.48  59.5   -2.41   50MA bounce (+|
|  GRMN     Pullback50      eq     $275.44  20.4   -2.06   50MA bounce (-|
|  JCI      Pullback50      eq     $145.37  54.8   -2.99   50MA bounce (+|
|  SYY      Pullback50      eq     $83.14   45.0   -1.98   50MA bounce (+|
|  WELL     Pullback50      eq     $237.41  46.4   -2.29   50MA bounce (-|
|  WMB      Pullback50      eq     $72.85   59.8   -1.88   50MA bounce (-|
|  ATI      Pullback50      eq     $203.01  46.1   -0.87   50MA bounce (-|
|  CGNX     Pullback50      eq     $63.74   60.4   -2.54   50MA bounce (+|
|  ENTG     Pullback50      eq     $140.68  47.2   -2.09   50MA bounce (+|
|  ITT      Pullback50      eq     $200.18  41.5   -2.81   50MA bounce (-|
|  KRYS     Pullback50      eq     $349.85  52.0   -2.56   50MA bounce (+|
|  LFUS     Pullback50      eq     $424.90  57.2   -2.04   50MA bounce (+|
|  MSM      Pullback50      eq     $122.09  55.4   -3.20   50MA bounce (-|
|  MTSI     Pullback50      eq     $279.54  56.6   -2.18   50MA bounce (-|
|  PATH     Pullback50      eq     $14.20   37.6   -3.11   50MA bounce (+|
|  SLAB     Pullback50      eq     $219.69  65.0   -2.21   50MA bounce (+|
|  VIAV     Pullback50      eq     $39.16   50.7   -2.11   50MA bounce (+|
|                                                                        |13:50:41  INFO        BUY  AMZN  $34.19  [Pullback50]  id=bec42e2c-3394-4eef-aa92-dd0d298cbdfb
13:50:42  INFO        BUY  ADI  $34.19  [Pullback50]  id=ef3d926c-2d5c-479d-bb7e-8906e14f6e6d
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260911T135212Z

- UTC timestamp: `20260911T135212Z`
- GitHub run: [#9722](https://github.com/28twagg-ops/TradingBot/actions/runs/34606577102)
- Run id: `34606577102`
- Live bot: exit=`0`, duration=`248s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260911T135212Z_live_bot.log`, `logs/action_runs/20260911T135212Z_live_options.log`, `logs/action_runs/20260911T135212Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1176 | 48.5 | -23.1 | +40.5 | $+15,122 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 584 | 63.2 | +51.2 | +67.1 | $+10,415 |
| KEEP-only recent | 387 | 61.0 | +53.3 | +80.0 | $+5,770 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T09:26:15.992436-04:00","date":"2026-09-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.49},"signals":0,"placed":0,"equity":998581.0,"open_positions":27,"pending_orders":0,"open_lots":91,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9717","github_run_id":"34604175612","status":"ok","data_quality":{"clean":{"n":1176,"win":48.47,"med":-23.12,"avg":40.52,"pnl":15122.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":584,"win":63.18,"med":51.18,"avg":67.07,"pnl":10415.45},"keep_only_recent":{"n":387,"win":60.98,"med":53.33,"avg":79.96,"pnl":5770.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
... (96 earlier lines - see full log file)
+========================================================================+
|  Exit eval    attempted 1 | filled 1 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 2|
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
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  24                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  ALLE     Pullback50      eq     $153.07  30.8   -0.81   50MA bounce (-|
|  AME      Pullback50      eq     $239.49  49.9   -2.76   50MA bounce (-|
|  ADP      Pullback50      eq     $266.45  32.0   -2.82   50MA bounce (+|
|  TECH     Pullback50      eq     $72.25   47.3   -2.27   50MA bounce (+|
|  CTAS     Pullback50      eq     $200.62  43.1   -3.09   50MA bounce (+|
|  DLR      Pullback50      eq     $187.12  44.1   -1.53   50MA bounce (+|
|  EMR      Pullback50      eq     $151.11  39.5   -3.08   50MA bounce (+|
|  EQIX     Pullback50      eq     $1034.~  40.4   -1.91   50MA bounce (-|
|  FFIV     Pullback50      eq     $404.02  58.7   -2.41   50MA bounce (+|
|  GRMN     Pullback50      eq     $276.17  22.1   -2.06   50MA bounce (+|
|  JCI      Pullback50      eq     $144.72  53.6   -2.98   50MA bounce (-|
|  SYY      Pullback50      eq     $83.29   45.9   -1.97   50MA bounce (+|
|  WMB      Pullback50      eq     $73.08   60.5   -1.86   50MA bounce (-|
|  ATI      Pullback50      eq     $202.14  45.2   -0.86   50MA bounce (-|
|  CART     Pullback50      eq     $47.51   39.8   -2.15   50MA bounce (-|
|  CGNX     Pullback50      eq     $63.30   59.2   -2.52   50MA bounce (-|
|  CXT      Pullback50      eq     $51.50   58.0   -2.81   50MA bounce (+|
|  ENTG     Pullback50      eq     $140.34  46.8   -2.08   50MA bounce (+|
|  ITT      Pullback50      eq     $200.17  41.5   -2.79   50MA bounce (-|
|  LFUS     Pullback50      eq     $425.43  57.5   -2.03   50MA bounce (+|
|  MSM      Pullback50      eq     $121.83  54.8   -3.19   50MA bounce (-|
|  PATH     Pullback50      eq     $14.26   38.0   -3.10   50MA bounce (+|
|  SLAB     Pullback50      eq     $219.56  64.2   -2.19   50MA bounce (+|
|  VIAV     Pullback50      eq     $38.86   49.9   -2.08   50MA bounce (-|
|                                                                        |
+========================================================================+13:56:19  INFO        place_all_stops: checking 2 positions...
13:56:19  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
13:56:19  INFO        STOP skipped RL: fractional (0.1016 shares) — software exit will handle it
13:56:19  INFO        Daily log -> logs/daily/2026-09-11.md
13:56:19  INFO        Dashboard written → logs/dashboard.md


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
|  Scanned                                                            899|
|  Signals                                                             24|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                1|
|  Open pos                                                             2|
|  Equity                                                         $227.51|
|  Cash                                                           $159.31|
+========================================================================+
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260911T135737Z

- UTC timestamp: `20260911T135737Z`
- GitHub run: [#9723](https://github.com/28twagg-ops/TradingBot/actions/runs/34607055769)
- Run id: `34607055769`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260911T135737Z_live_bot.log`, `logs/action_runs/20260911T135737Z_live_options.log`, `logs/action_runs/20260911T135737Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1176 | 48.5 | -23.1 | +40.5 | $+15,122 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 584 | 63.2 | +51.2 | +67.1 | $+10,415 |
| KEEP-only recent | 387 | 61.0 | +53.3 | +80.0 | $+5,770 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T09:26:15.992436-04:00","date":"2026-09-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.49},"signals":0,"placed":0,"equity":998581.0,"open_positions":27,"pending_orders":0,"open_lots":91,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9717","github_run_id":"34604175612","status":"ok","data_quality":{"clean":{"n":1176,"win":48.47,"med":-23.12,"avg":40.52,"pnl":15122.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":584,"win":63.18,"med":51.18,"avg":67.07,"pnl":10415.45},"keep_only_recent":{"n":387,"win":60.98,"med":53.33,"avg":79.96,"pnl":5770.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:57:39  INFO      Mode: morning_scan
13:57:39  INFO        [positions] 2/2 (2 valid)
13:57:39  INFO        Universe cache hit: 903 tickers (tickers_2026-09-11.json)
13:57:40  INFO        [universe] 40/901 (40 valid)
13:57:42  INFO        [universe] 80/901 (80 valid)
13:57:43  INFO        [universe] 120/901 (120 valid)
13:57:44  INFO        [universe] 160/901 (160 valid)
13:57:46  INFO        [universe] 200/901 (199 valid)
13:57:53  INFO        [universe] 240/901 (238 valid)
13:58:06  INFO        [universe] 280/901 (278 valid)
13:58:19  INFO        [universe] 320/901 (318 valid)
13:58:29  INFO        [universe] 360/901 (358 valid)
13:58:42  INFO        [universe] 400/901 (398 valid)
13:58:54  INFO        [universe] 440/901 (438 valid)
13:59:04  INFO        [universe] 480/901 (478 valid)
13:59:17  INFO        [universe] 520/901 (518 valid)
13:59:30  INFO        [universe] 560/901 (558 valid)
13:59:40  INFO        [universe] 600/901 (598 valid)
13:59:53  INFO        [universe] 640/901 (638 valid)
14:00:06  INFO        [universe] 680/901 (678 valid)
14:00:16  INFO        [universe] 720/901 (718 valid)
14:00:29  INFO        [universe] 760/901 (758 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260911T140158Z

- UTC timestamp: `20260911T140158Z`
- GitHub run: [#9724](https://github.com/28twagg-ops/TradingBot/actions/runs/34607536644)
- Run id: `34607536644`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`81s`
- Full logs: `logs/action_runs/20260911T140158Z_live_bot.log`, `logs/action_runs/20260911T140158Z_live_options.log`, `logs/action_runs/20260911T140158Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1182 | 48.4 | -23.3 | +40.3 | $+15,112 |
| TAINTED | 1828 | 33.4 | -38.8 | +12.0 | $-9,082 |
| KEEP-only | 587 | 63.2 | +51.4 | +67.1 | $+10,486 |
| KEEP-only recent | 390 | 61.0 | +53.4 | +80.0 | $+5,841 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T10:02:06.673851-04:00","date":"2026-09-11","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":67.6,"phases_s":{"reconcile":0.57,"cancel":0.11,"manage":7.76,"protective_stops":2.13,"scan":53.37,"entries":2.97},"signals":11,"placed":0,"equity":1000853.04,"open_positions":19,"pending_orders":0,"open_lots":71,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S211:CRWD","S210:DOCN","S403:FSLY","S217:HD","S217:UNP","S216:LMT","S216:HON","S217:LLY"],"github_run":"9724","github_run_id":"34607536644","status":"ok","data_quality":{"clean":{"n":1182,"win":48.39,"med":-23.29,"avg":40.27,"pnl":15112.09},"tainted":{"n":1828,"win":33.37,"med":-38.81,"avg":12.01,"pnl":-9081.84},"keep_only":{"n":587,"win":63.2,"med":51.39,"avg":67.14,"pnl":10486.45},"keep_only_recent":{"n":390,"win":61.03,"med":53.45,"avg":79.97,"pnl":5841.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:01:59  INFO      Mode: exits
14:02:00  INFO        Daily log -> logs/daily/2026-09-11.md
14:02:00  INFO        Daily log reconciled -> logs/daily/2026-09-11.md (2 ledger rows)
14:02:00  INFO        place_all_stops: checking 2 positions...
14:02:00  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
14:02:00  INFO        STOP skipped RL: fractional (0.1016 shares) — software exit will handle it
14:02:01  INFO        [positions] 2/2 (2 valid)
14:02:01  INFO        Daily log -> logs/daily/2026-09-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:02 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.65|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.1%  $+0.02                                           HOLD|
|  RL  P&L +0.2%  $+0.07                                             HOLD|
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
=== options_live_micro LIVE 2026-09-11T10:02:02.297259-04:00 share=25% ===
2026-09-11 10:02:02,297 INFO === options_live_micro LIVE 2026-09-11T10:02:02.297259-04:00 share=25% ===
Live account equity $227.65 cash $159.31 #225458845 options_level=3
2026-09-11 10:02:02,496 INFO Live account equity $227.65 cash $159.31 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-11 10:02:02,698 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-11 10:02:02,802 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (199 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    71 | INFO |
| Total closed lots           |  2172 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1182 med=-23.3% | TAINTED n=1828 med=-38.8% | KEEP-only n=587 med=+51.4% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.64 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T140614Z

- UTC timestamp: `20260911T140614Z`
- GitHub run: [#9725](https://github.com/28twagg-ops/TradingBot/actions/runs/34608032460)
- Run id: `34608032460`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`74s`
- Full logs: `logs/action_runs/20260911T140614Z_live_bot.log`, `logs/action_runs/20260911T140614Z_live_options.log`, `logs/action_runs/20260911T140614Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1185 | 48.5 | -22.9 | +40.4 | $+15,241 |
| TAINTED | 1828 | 33.4 | -38.8 | +12.0 | $-9,082 |
| KEEP-only | 587 | 63.2 | +51.4 | +67.1 | $+10,486 |
| KEEP-only recent | 390 | 61.0 | +53.4 | +80.0 | $+5,841 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T10:06:20.305127-04:00","date":"2026-09-11","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":62.5,"phases_s":{"reconcile":0.79,"cancel":0.05,"manage":3.98,"protective_stops":1.42,"scan":53.95,"entries":1.45},"signals":11,"placed":0,"equity":1001110.94,"open_positions":18,"pending_orders":0,"open_lots":66,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S211:CRWD","S210:DOCN","S403:FSLY","S217:HD","S217:UNP","S216:LMT","S216:HON","S217:LLY"],"github_run":"9725","github_run_id":"34608032460","status":"ok","data_quality":{"clean":{"n":1185,"win":48.52,"med":-22.95,"avg":40.4,"pnl":15241.09},"tainted":{"n":1828,"win":33.37,"med":-38.81,"avg":12.01,"pnl":-9081.84},"keep_only":{"n":587,"win":63.2,"med":51.39,"avg":67.14,"pnl":10486.45},"keep_only_recent":{"n":390,"win":61.03,"med":53.45,"avg":79.97,"pnl":5841.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:06:15  INFO      Mode: exits
14:06:15  INFO        Daily log -> logs/daily/2026-09-11.md
14:06:15  INFO        Daily log reconciled -> logs/daily/2026-09-11.md (2 ledger rows)
14:06:15  INFO        place_all_stops: checking 2 positions...
14:06:15  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
14:06:15  INFO        STOP skipped RL: fractional (0.1016 shares) — software exit will handle it
14:06:16  INFO        [positions] 2/2 (2 valid)
14:06:16  INFO        Daily log -> logs/daily/2026-09-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.52|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  RL  P&L -0.1%  $-0.05                                             HOLD|
|  AMZN  P&L +0.0%  $+0.01                                           HOLD|
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
=== options_live_micro LIVE 2026-09-11T10:06:17.033754-04:00 share=25% ===
2026-09-11 10:06:17,033 INFO === options_live_micro LIVE 2026-09-11T10:06:17.033754-04:00 share=25% ===
Live account equity $227.52 cash $159.31 #225458845 options_level=3
2026-09-11 10:06:17,349 INFO Live account equity $227.52 cash $159.31 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-11 10:06:17,412 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-11 10:06:17,452 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (197 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    14 | WARN | <<<
| Orphaned lots (post-stable) |  1199 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    66 | INFO |
| Total closed lots           |  2175 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1185 med=-22.9% | TAINTED n=1828 med=-38.8% | KEEP-only n=587 med=+51.4% | KILL=20 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.52 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T141107Z

- UTC timestamp: `20260911T141107Z`
- GitHub run: [#9726](https://github.com/28twagg-ops/TradingBot/actions/runs/34608514142)
- Run id: `34608514142`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`83s`
- Full logs: `logs/action_runs/20260911T141107Z_live_bot.log`, `logs/action_runs/20260911T141107Z_live_options.log`, `logs/action_runs/20260911T141107Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1191 | 48.8 | -17.2 | +40.6 | $+15,465 |
| TAINTED | 1828 | 33.4 | -38.8 | +12.0 | $-9,082 |
| KEEP-only | 605 | 63.1 | +51.4 | +65.6 | $+10,561 |
| KEEP-only recent | 408 | 61.0 | +53.4 | +77.2 | $+5,916 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T10:11:15.713857-04:00","date":"2026-09-11","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":71.0,"phases_s":{"reconcile":0.69,"cancel":0.15,"manage":6.15,"protective_stops":3.16,"scan":53.65,"entries":3.01,"reconcile2":0.62},"signals":11,"placed":2,"equity":1000558.32,"open_positions":18,"pending_orders":0,"open_lots":61,"submitted_today":2,"filled_today":2,"unattributed_contracts":0,"top_signals":["S211:CRWD","S210:DOCN","S403:FSLY","S217:HD","S217:UNP","S216:LMT","S216:HON","S217:LLY"],"github_run":"9726","github_run_id":"34608514142","status":"ok","data_quality":{"clean":{"n":1191,"win":48.78,"med":-17.24,"avg":40.58,"pnl":15465.09},"tainted":{"n":1828,"win":33.37,"med":-38.81,"avg":12.01,"pnl":-9081.84},"keep_only":{"n":605,"win":63.14,"med":51.39,"avg":65.63,"pnl":10561.45},"keep_only_recent":{"n":408,"win":61.03,"med":53.45,"avg":77.16,"pnl":5916.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:11:08  INFO      Mode: exits
14:11:09  INFO        Daily log -> logs/daily/2026-09-11.md
14:11:09  INFO        Daily log reconciled -> logs/daily/2026-09-11.md (2 ledger rows)
14:11:09  INFO        place_all_stops: checking 2 positions...
14:11:09  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
14:11:09  INFO        STOP skipped RL: fractional (0.1016 shares) — software exit will handle it
14:11:10  INFO        [positions] 2/2 (2 valid)
14:11:10  INFO        Daily log -> logs/daily/2026-09-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.57|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  RL  P&L -0.1%  $-0.03                                             HOLD|
|  AMZN  P&L +0.1%  $+0.04                                           HOLD|
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
=== options_live_micro LIVE 2026-09-11T10:11:11.623108-04:00 share=25% ===
2026-09-11 10:11:11,623 INFO === options_live_micro LIVE 2026-09-11T10:11:11.623108-04:00 share=25% ===
Live account equity $227.56 cash $159.31 #225458845 options_level=3
2026-09-11 10:11:11,873 INFO Live account equity $227.56 cash $159.31 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-11 10:11:12,165 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-11 10:11:12,340 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (188 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    11 | WARN | <<<
| Orphaned lots (post-stable) |  1196 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    61 | INFO |
| Total closed lots           |  2181 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1191 med=-17.2% | TAINTED n=1828 med=-38.8% | KEEP-only n=605 med=+51.4% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.57 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T141602Z

- UTC timestamp: `20260911T141602Z`
- GitHub run: [#9727](https://github.com/28twagg-ops/TradingBot/actions/runs/34609005719)
- Run id: `34609005719`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`71s`
- Full logs: `logs/action_runs/20260911T141602Z_live_bot.log`, `logs/action_runs/20260911T141602Z_live_options.log`, `logs/action_runs/20260911T141602Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1192 | 48.8 | -17.2 | +40.6 | $+15,516 |
| TAINTED | 1828 | 33.4 | -38.8 | +12.0 | $-9,082 |
| KEEP-only | 605 | 63.1 | +51.4 | +65.6 | $+10,561 |
| KEEP-only recent | 408 | 61.0 | +53.4 | +77.2 | $+5,916 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T10:16:07.295751-04:00","date":"2026-09-11","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":59.6,"phases_s":{"reconcile":0.5,"cancel":0.02,"manage":3.42,"protective_stops":0.36,"scan":54.06,"entries":0.52},"signals":11,"placed":0,"equity":1000897.47,"open_positions":18,"pending_orders":0,"open_lots":60,"submitted_today":2,"filled_today":2,"unattributed_contracts":0,"top_signals":["S211:CRWD","S210:DOCN","S403:FSLY","S217:HD","S217:UNP","S216:LMT","S216:HON","S217:LLY"],"github_run":"9727","github_run_id":"34609005719","status":"ok","data_quality":{"clean":{"n":1192,"win":48.83,"med":-17.22,"avg":40.62,"pnl":15516.09},"tainted":{"n":1828,"win":33.37,"med":-38.81,"avg":12.01,"pnl":-9081.84},"keep_only":{"n":605,"win":63.14,"med":51.39,"avg":65.63,"pnl":10561.45},"keep_only_recent":{"n":408,"win":61.03,"med":53.45,"avg":77.16,"pnl":5916.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:16:03  INFO      Mode: exits
14:16:03  INFO        Daily log -> logs/daily/2026-09-11.md
14:16:03  INFO        Daily log reconciled -> logs/daily/2026-09-11.md (2 ledger rows)
14:16:03  INFO        place_all_stops: checking 2 positions...
14:16:03  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
14:16:03  INFO        STOP skipped RL: fractional (0.1016 shares) — software exit will handle it
14:16:03  INFO        [positions] 2/2 (2 valid)
14:16:03  INFO        Daily log -> logs/daily/2026-09-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.49|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  RL  P&L -0.2%  $-0.06                                             HOLD|
|  AMZN  P&L -0.0%  $-0.00                                           HOLD|
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
=== options_live_micro LIVE 2026-09-11T10:16:04.490689-04:00 share=25% ===
2026-09-11 10:16:04,490 INFO === options_live_micro LIVE 2026-09-11T10:16:04.490689-04:00 share=25% ===
Live account equity $227.50 cash $159.31 #225458845 options_level=3
2026-09-11 10:16:04,532 INFO Live account equity $227.50 cash $159.31 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-11 10:16:04,556 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-11 10:16:04,574 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (186 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    11 | WARN | <<<
| Orphaned lots (post-stable) |  1196 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    60 | INFO |
| Total closed lots           |  2182 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1192 med=-17.2% | TAINTED n=1828 med=-38.8% | KEEP-only n=605 med=+51.4% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.49 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T142113Z

- UTC timestamp: `20260911T142113Z`
- GitHub run: [#9728](https://github.com/28twagg-ops/TradingBot/actions/runs/34609490607)
- Run id: `34609490607`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`78s`
- Full logs: `logs/action_runs/20260911T142113Z_live_bot.log`, `logs/action_runs/20260911T142113Z_live_options.log`, `logs/action_runs/20260911T142113Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1193 | 48.9 | -17.2 | +40.6 | $+15,549 |
| TAINTED | 1828 | 33.4 | -38.8 | +12.0 | $-9,082 |
| KEEP-only | 605 | 63.1 | +51.4 | +65.6 | $+10,561 |
| KEEP-only recent | 408 | 61.0 | +53.4 | +77.2 | $+5,916 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T10:21:21.524254-04:00","date":"2026-09-11","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":66.2,"phases_s":{"reconcile":0.51,"cancel":0.14,"manage":5.53,"protective_stops":3.0,"scan":53.75,"entries":2.58},"signals":11,"placed":0,"equity":1000929.2,"open_positions":17,"pending_orders":0,"open_lots":59,"submitted_today":2,"filled_today":2,"unattributed_contracts":0,"top_signals":["S211:CRWD","S210:DOCN","S403:FSLY","S217:HD","S217:UNP","S216:LMT","S216:HON","S217:LLY"],"github_run":"9728","github_run_id":"34609490607","status":"ok","data_quality":{"clean":{"n":1193,"win":48.87,"med":-17.19,"avg":40.65,"pnl":15549.09},"tainted":{"n":1828,"win":33.37,"med":-38.81,"avg":12.01,"pnl":-9081.84},"keep_only":{"n":605,"win":63.14,"med":51.39,"avg":65.63,"pnl":10561.45},"keep_only_recent":{"n":408,"win":61.03,"med":53.45,"avg":77.16,"pnl":5916.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:21:14  INFO      Mode: exits
14:21:15  INFO        Daily log -> logs/daily/2026-09-11.md
14:21:15  INFO        Daily log reconciled -> logs/daily/2026-09-11.md (2 ledger rows)
14:21:15  INFO        place_all_stops: checking 2 positions...
14:21:15  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
14:21:15  INFO        STOP skipped RL: fractional (0.1016 shares) — software exit will handle it
14:21:16  INFO        [positions] 2/2 (2 valid)
14:21:16  INFO        Daily log -> logs/daily/2026-09-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.64|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  RL  P&L +0.0%  $+0.00                                             HOLD|
|  AMZN  P&L +0.3%  $+0.09                                           HOLD|
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
=== options_live_micro LIVE 2026-09-11T10:21:17.471079-04:00 share=25% ===
2026-09-11 10:21:17,471 INFO === options_live_micro LIVE 2026-09-11T10:21:17.471079-04:00 share=25% ===
Live account equity $227.64 cash $159.31 #225458845 options_level=3
2026-09-11 10:21:17,702 INFO Live account equity $227.64 cash $159.31 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-11 10:21:18,011 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-11 10:21:18,173 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (186 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    10 | WARN | <<<
| Orphaned lots (post-stable) |  1195 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    59 | INFO |
| Total closed lots           |  2183 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1193 med=-17.2% | TAINTED n=1828 med=-38.8% | KEEP-only n=605 med=+51.4% | KILL=19 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.64 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T142625Z

- UTC timestamp: `20260911T142625Z`
- GitHub run: [#9729](https://github.com/28twagg-ops/TradingBot/actions/runs/34609984488)
- Run id: `34609984488`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`72s`
- Full logs: `logs/action_runs/20260911T142625Z_live_bot.log`, `logs/action_runs/20260911T142625Z_live_options.log`, `logs/action_runs/20260911T142625Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1194 | 48.9 | -16.6 | +40.7 | $+15,582 |
| TAINTED | 1828 | 33.4 | -38.8 | +12.0 | $-9,082 |
| KEEP-only | 618 | 62.9 | +50.9 | +64.4 | $+10,566 |
| KEEP-only recent | 421 | 60.8 | +53.3 | +75.0 | $+5,921 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T10:26:33.296190-04:00","date":"2026-09-11","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":60.2,"phases_s":{"reconcile":0.25,"cancel":0.05,"manage":2.96,"protective_stops":0.92,"scan":54.25,"entries":1.02},"signals":11,"placed":0,"equity":1000452.16,"open_positions":17,"pending_orders":0,"open_lots":57,"submitted_today":2,"filled_today":2,"unattributed_contracts":0,"top_signals":["S211:CRWD","S210:DOCN","S403:FSLY","S217:HD","S217:UNP","S216:LMT","S216:HON","S217:LLY"],"github_run":"9729","github_run_id":"34609984488","status":"ok","data_quality":{"clean":{"n":1194,"win":48.91,"med":-16.6,"avg":40.68,"pnl":15582.09},"tainted":{"n":1828,"win":33.37,"med":-38.81,"avg":12.01,"pnl":-9081.84},"keep_only":{"n":618,"win":62.94,"med":50.91,"avg":64.39,"pnl":10566.45},"keep_only_recent":{"n":421,"win":60.81,"med":53.33,"avg":74.99,"pnl":5921.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:26:26  INFO      Mode: exits
14:26:26  INFO        Daily log -> logs/daily/2026-09-11.md
14:26:26  INFO        Daily log reconciled -> logs/daily/2026-09-11.md (2 ledger rows)
14:26:26  INFO        place_all_stops: checking 2 positions...
14:26:26  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
14:26:26  INFO        STOP skipped RL: fractional (0.1016 shares) — software exit will handle it
14:26:27  INFO        [positions] 2/2 (2 valid)
14:26:27  INFO        SELL MARKET [urgent] RL closed
14:26:29  INFO        TX logged: SELL RL  P&L -0.73%
14:26:29  INFO        Daily log -> logs/daily/2026-09-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.28|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  RL  P&L -0.7%  $-0.25                          EXIT: stop_loss (-0.7%)|
|  AMZN  P&L -0.1%  $-0.02                                           HOLD|
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
|  RL                                          -0.73%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-11T10:26:30.271004-04:00 share=25% ===
2026-09-11 10:26:30,271 INFO === options_live_micro LIVE 2026-09-11T10:26:30.271004-04:00 share=25% ===
Live account equity $227.19 cash $193.04 #225458845 options_level=3
2026-09-11 10:26:30,355 INFO Live account equity $227.19 cash $193.04 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-11 10:26:30,417 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-11 10:26:30,462 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (185 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     8 | WARN | <<<
| Orphaned lots (post-stable) |  1194 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    57 | INFO |
| Total closed lots           |  2184 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1194 med=-16.6% | TAINTED n=1828 med=-38.8% | KEEP-only n=618 med=+50.9% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.19 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T143108Z

- UTC timestamp: `20260911T143108Z`
- GitHub run: [#9730](https://github.com/28twagg-ops/TradingBot/actions/runs/34610486538)
- Run id: `34610486538`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`65s`
- Full logs: `logs/action_runs/20260911T143108Z_live_bot.log`, `logs/action_runs/20260911T143108Z_live_options.log`, `logs/action_runs/20260911T143108Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1195 | 49.0 | -16.0 | +40.7 | $+15,606 |
| TAINTED | 1828 | 33.4 | -38.8 | +12.0 | $-9,082 |
| KEEP-only | 619 | 63.0 | +50.9 | +64.4 | $+10,590 |
| KEEP-only recent | 422 | 60.9 | +53.3 | +74.9 | $+5,945 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T10:31:16.085357-04:00","date":"2026-09-11","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":54.1,"phases_s":{"reconcile":0.33,"cancel":0.08,"manage":4.14,"protective_stops":1.26,"scan":45.84,"entries":1.82},"signals":11,"placed":0,"equity":1000600.14,"open_positions":17,"pending_orders":0,"open_lots":56,"submitted_today":2,"filled_today":2,"unattributed_contracts":0,"top_signals":["S211:CRWD","S210:DOCN","S403:FSLY","S217:HD","S217:UNP","S216:LMT","S216:HON","S217:LLY"],"github_run":"9730","github_run_id":"34610486538","status":"ok","data_quality":{"clean":{"n":1195,"win":48.95,"med":-16.0,"avg":40.69,"pnl":15606.09},"tainted":{"n":1828,"win":33.37,"med":-38.81,"avg":12.01,"pnl":-9081.84},"keep_only":{"n":619,"win":63.0,"med":50.94,"avg":64.38,"pnl":10590.45},"keep_only_recent":{"n":422,"win":60.9,"med":53.33,"avg":74.94,"pnl":5945.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:31:11  INFO      Mode: exits
14:31:11  INFO        Daily log -> logs/daily/2026-09-11.md
14:31:11  INFO        Daily log reconciled -> logs/daily/2026-09-11.md (3 ledger rows)
14:31:11  INFO        place_all_stops: checking 1 positions...
14:31:11  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
14:31:11  INFO        [positions] 1/1 (1 valid)
14:31:12  INFO        Daily log -> logs/daily/2026-09-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.2%  $-0.06                                           HOLD|
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
=== options_live_micro LIVE 2026-09-11T10:31:12.909395-04:00 share=25% ===
2026-09-11 10:31:12,909 INFO === options_live_micro LIVE 2026-09-11T10:31:12.909395-04:00 share=25% ===
Live account equity $227.16 cash $193.04 #225458845 options_level=3
2026-09-11 10:31:13,053 INFO Live account equity $227.16 cash $193.04 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-11 10:31:13,164 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-11 10:31:13,236 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (183 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     7 | WARN | <<<
| Orphaned lots (post-stable) |  1193 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    56 | INFO |
| Total closed lots           |  2185 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1195 med=-16.0% | TAINTED n=1828 med=-38.8% | KEEP-only n=619 med=+50.9% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T143607Z

- UTC timestamp: `20260911T143607Z`
- GitHub run: [#9731](https://github.com/28twagg-ops/TradingBot/actions/runs/34610987896)
- Run id: `34610987896`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`49s`
- Full logs: `logs/action_runs/20260911T143607Z_live_bot.log`, `logs/action_runs/20260911T143607Z_live_options.log`, `logs/action_runs/20260911T143607Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1196 | 48.9 | -16.6 | +40.6 | $+15,584 |
| TAINTED | 1828 | 33.4 | -38.8 | +12.0 | $-9,082 |
| KEEP-only | 619 | 63.0 | +50.9 | +64.4 | $+10,590 |
| KEEP-only recent | 422 | 60.9 | +53.3 | +74.9 | $+5,945 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T10:36:12.672636-04:00","date":"2026-09-11","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":39.5,"phases_s":{"reconcile":0.17,"cancel":0.02,"manage":2.14,"protective_stops":0.28,"scan":35.29,"entries":0.62,"reconcile2":0.14},"signals":11,"placed":2,"equity":1000439.14,"open_positions":17,"pending_orders":2,"open_lots":55,"submitted_today":4,"filled_today":2,"unattributed_contracts":0,"top_signals":["S211:CRWD","S210:DOCN","S403:FSLY","S217:HD","S217:UNP","S216:LMT","S216:HON","S217:LLY"],"github_run":"9731","github_run_id":"34610987896","status":"ok","data_quality":{"clean":{"n":1196,"win":48.91,"med":-16.6,"avg":40.62,"pnl":15584.09},"tainted":{"n":1828,"win":33.37,"med":-38.81,"avg":12.01,"pnl":-9081.84},"keep_only":{"n":619,"win":63.0,"med":50.94,"avg":64.38,"pnl":10590.45},"keep_only_recent":{"n":422,"win":60.9,"med":53.33,"avg":74.94,"pnl":5945.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:36:09  INFO      Mode: exits
14:36:09  INFO        Daily log -> logs/daily/2026-09-11.md
14:36:09  INFO        Daily log reconciled -> logs/daily/2026-09-11.md (3 ledger rows)
14:36:09  INFO        place_all_stops: checking 1 positions...
14:36:09  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
14:36:09  INFO        [positions] 1/1 (1 valid)
14:36:09  INFO        Daily log -> logs/daily/2026-09-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.10|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.3%  $-0.12                                           HOLD|
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
=== options_live_micro LIVE 2026-09-11T10:36:10.470508-04:00 share=25% ===
2026-09-11 10:36:10,470 INFO === options_live_micro LIVE 2026-09-11T10:36:10.470508-04:00 share=25% ===
Live account equity $227.10 cash $193.04 #225458845 options_level=3
2026-09-11 10:36:10,548 INFO Live account equity $227.10 cash $193.04 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-11 10:36:10,602 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-11 10:36:10,618 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (192 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     7 | WARN | <<<
| Orphaned lots (post-stable) |  1193 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    55 | INFO |
| Total closed lots           |  2186 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1196 med=-16.6% | TAINTED n=1828 med=-38.8% | KEEP-only n=619 med=+50.9% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.1 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T144113Z

- UTC timestamp: `20260911T144113Z`
- GitHub run: [#9732](https://github.com/28twagg-ops/TradingBot/actions/runs/34611485153)
- Run id: `34611485153`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`69s`
- Full logs: `logs/action_runs/20260911T144113Z_live_bot.log`, `logs/action_runs/20260911T144113Z_live_options.log`, `logs/action_runs/20260911T144113Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1196 | 48.9 | -16.6 | +40.6 | $+15,584 |
| TAINTED | 1828 | 33.4 | -38.8 | +12.0 | $-9,082 |
| KEEP-only | 619 | 63.0 | +50.9 | +64.4 | $+10,590 |
| KEEP-only recent | 422 | 60.9 | +53.3 | +74.9 | $+5,945 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T10:41:20.494001-04:00","date":"2026-09-11","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":57.3,"phases_s":{"reconcile":0.42,"cancel":0.12,"manage":4.29,"protective_stops":1.82,"scan":46.0,"entries":1.7,"reconcile2":0.4},"signals":11,"placed":0,"equity":1000241.12,"open_positions":17,"pending_orders":2,"open_lots":55,"submitted_today":4,"filled_today":2,"unattributed_contracts":0,"top_signals":["S211:CRWD","S210:DOCN","S403:FSLY","S217:HD","S217:UNP","S216:LMT","S216:HON","S217:LLY"],"github_run":"9732","github_run_id":"34611485153","status":"ok","data_quality":{"clean":{"n":1196,"win":48.91,"med":-16.6,"avg":40.62,"pnl":15584.09},"tainted":{"n":1828,"win":33.37,"med":-38.81,"avg":12.01,"pnl":-9081.84},"keep_only":{"n":619,"win":63.0,"med":50.94,"avg":64.38,"pnl":10590.45},"keep_only_recent":{"n":422,"win":60.9,"med":53.33,"avg":74.94,"pnl":5945.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:41:14  INFO      Mode: exits
14:41:15  INFO        Daily log -> logs/daily/2026-09-11.md
14:41:15  INFO        Daily log reconciled -> logs/daily/2026-09-11.md (3 ledger rows)
14:41:15  INFO        place_all_stops: checking 1 positions...
14:41:15  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
14:41:15  INFO        [positions] 1/1 (1 valid)
14:41:15  INFO        Daily log -> logs/daily/2026-09-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.07|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.4%  $-0.15                                           HOLD|
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
=== options_live_micro LIVE 2026-09-11T10:41:16.522461-04:00 share=25% ===
2026-09-11 10:41:16,522 INFO === options_live_micro LIVE 2026-09-11T10:41:16.522461-04:00 share=25% ===
Live account equity $227.07 cash $193.04 #225458845 options_level=3
2026-09-11 10:41:16,741 INFO Live account equity $227.07 cash $193.04 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-11 10:41:17,137 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-11 10:41:17,251 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (191 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     7 | WARN | <<<
| Orphaned lots (post-stable) |  1193 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    55 | INFO |
| Total closed lots           |  2186 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1196 med=-16.6% | TAINTED n=1828 med=-38.8% | KEEP-only n=619 med=+50.9% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.07 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T144607Z

- UTC timestamp: `20260911T144607Z`
- GitHub run: [#9733](https://github.com/28twagg-ops/TradingBot/actions/runs/34611986226)
- Run id: `34611986226`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`53s`
- Full logs: `logs/action_runs/20260911T144607Z_live_bot.log`, `logs/action_runs/20260911T144607Z_live_options.log`, `logs/action_runs/20260911T144607Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1196 | 48.9 | -16.6 | +40.6 | $+15,584 |
| TAINTED | 1828 | 33.4 | -38.8 | +12.0 | $-9,082 |
| KEEP-only | 619 | 63.0 | +50.9 | +64.4 | $+10,590 |
| KEEP-only recent | 422 | 60.9 | +53.3 | +74.9 | $+5,945 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T10:46:13.482343-04:00","date":"2026-09-11","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":43.2,"phases_s":{"reconcile":0.27,"cancel":0.07,"manage":3.11,"protective_stops":1.1,"scan":34.73,"entries":2.06,"reconcile2":0.26},"signals":11,"placed":0,"equity":1000181.13,"open_positions":17,"pending_orders":2,"open_lots":55,"submitted_today":4,"filled_today":2,"unattributed_contracts":0,"top_signals":["S211:CRWD","S210:DOCN","S403:FSLY","S217:HD","S217:UNP","S216:LMT","S216:HON","S217:LLY"],"github_run":"9733","github_run_id":"34611986226","status":"ok","data_quality":{"clean":{"n":1196,"win":48.91,"med":-16.6,"avg":40.62,"pnl":15584.09},"tainted":{"n":1828,"win":33.37,"med":-38.81,"avg":12.01,"pnl":-9081.84},"keep_only":{"n":619,"win":63.0,"med":50.94,"avg":64.38,"pnl":10590.45},"keep_only_recent":{"n":422,"win":60.9,"med":53.33,"avg":74.94,"pnl":5945.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:46:07  INFO      Mode: exits
14:46:08  INFO        Daily log -> logs/daily/2026-09-11.md
14:46:08  INFO        Daily log reconciled -> logs/daily/2026-09-11.md (3 ledger rows)
14:46:08  INFO        place_all_stops: checking 1 positions...
14:46:08  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
14:46:08  INFO        [positions] 1/1 (1 valid)
14:46:08  INFO        Daily log -> logs/daily/2026-09-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.09|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.4%  $-0.13                                           HOLD|
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
=== options_live_micro LIVE 2026-09-11T10:46:09.675263-04:00 share=25% ===
2026-09-11 10:46:09,675 INFO === options_live_micro LIVE 2026-09-11T10:46:09.675263-04:00 share=25% ===
Live account equity $227.09 cash $193.04 #225458845 options_level=3
2026-09-11 10:46:09,867 INFO Live account equity $227.09 cash $193.04 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-11 10:46:10,023 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-11 10:46:10,116 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (193 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     7 | WARN | <<<
| Orphaned lots (post-stable) |  1193 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    55 | INFO |
| Total closed lots           |  2186 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1196 med=-16.6% | TAINTED n=1828 med=-38.8% | KEEP-only n=619 med=+50.9% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.09 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T145108Z

- UTC timestamp: `20260911T145108Z`
- GitHub run: [#9734](https://github.com/28twagg-ops/TradingBot/actions/runs/34612487737)
- Run id: `34612487737`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`62s`
- Full logs: `logs/action_runs/20260911T145108Z_live_bot.log`, `logs/action_runs/20260911T145108Z_live_options.log`, `logs/action_runs/20260911T145108Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1196 | 48.9 | -16.6 | +40.6 | $+15,584 |
| TAINTED | 1828 | 33.4 | -38.8 | +12.0 | $-9,082 |
| KEEP-only | 619 | 63.0 | +50.9 | +64.4 | $+10,590 |
| KEEP-only recent | 422 | 60.9 | +53.3 | +74.9 | $+5,945 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T10:51:14.544970-04:00","date":"2026-09-11","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":51.6,"phases_s":{"reconcile":0.23,"cancel":0.04,"manage":2.78,"protective_stops":0.54,"scan":46.1,"entries":1.41},"signals":11,"placed":0,"equity":1000228.56,"open_positions":18,"pending_orders":0,"open_lots":57,"submitted_today":4,"filled_today":4,"unattributed_contracts":0,"top_signals":["S211:CRWD","S210:DOCN","S403:FSLY","S217:HD","S217:UNP","S216:LMT","S216:HON","S217:LLY"],"github_run":"9734","github_run_id":"34612487737","status":"ok","data_quality":{"clean":{"n":1196,"win":48.91,"med":-16.6,"avg":40.62,"pnl":15584.09},"tainted":{"n":1828,"win":33.37,"med":-38.81,"avg":12.01,"pnl":-9081.84},"keep_only":{"n":619,"win":63.0,"med":50.94,"avg":64.38,"pnl":10590.45},"keep_only_recent":{"n":422,"win":60.9,"med":53.33,"avg":74.94,"pnl":5945.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:51:10  INFO      Mode: exits
14:51:10  INFO        Daily log -> logs/daily/2026-09-11.md
14:51:10  INFO        Daily log reconciled -> logs/daily/2026-09-11.md (3 ledger rows)
14:51:10  INFO        place_all_stops: checking 1 positions...
14:51:10  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
14:51:10  INFO        [positions] 1/1 (1 valid)
14:51:11  INFO        Daily log -> logs/daily/2026-09-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.10|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.3%  $-0.12                                           HOLD|
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
=== options_live_micro LIVE 2026-09-11T10:51:11.778019-04:00 share=25% ===
2026-09-11 10:51:11,778 INFO === options_live_micro LIVE 2026-09-11T10:51:11.778019-04:00 share=25% ===
Live account equity $227.10 cash $193.04 #225458845 options_level=3
2026-09-11 10:51:11,839 INFO Live account equity $227.10 cash $193.04 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-11 10:51:11,885 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-11 10:51:11,912 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (186 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     7 | WARN | <<<
| Orphaned lots (post-stable) |  1193 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    57 | INFO |
| Total closed lots           |  2186 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1196 med=-16.6% | TAINTED n=1828 med=-38.8% | KEEP-only n=619 med=+50.9% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.1 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T145613Z

- UTC timestamp: `20260911T145613Z`
- GitHub run: [#9735](https://github.com/28twagg-ops/TradingBot/actions/runs/34612989029)
- Run id: `34612989029`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`47s`
- Full logs: `logs/action_runs/20260911T145613Z_live_bot.log`, `logs/action_runs/20260911T145613Z_live_options.log`, `logs/action_runs/20260911T145613Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1197 | 48.9 | -17.2 | +40.5 | $+15,563 |
| TAINTED | 1828 | 33.4 | -38.8 | +12.0 | $-9,082 |
| KEEP-only | 620 | 62.9 | +50.9 | +64.2 | $+10,569 |
| KEEP-only recent | 423 | 60.8 | +53.3 | +74.6 | $+5,924 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T10:56:20.083098-04:00","date":"2026-09-11","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":37.9,"phases_s":{"reconcile":0.67,"cancel":0.09,"manage":3.42,"protective_stops":1.38,"scan":29.57,"entries":2.12},"signals":11,"placed":0,"equity":1000295.04,"open_positions":18,"pending_orders":0,"open_lots":56,"submitted_today":4,"filled_today":4,"unattributed_contracts":0,"top_signals":["S211:CRWD","S210:DOCN","S403:FSLY","S217:HD","S217:UNP","S216:LMT","S216:HON","S217:LLY"],"github_run":"9735","github_run_id":"34612989029","status":"ok","data_quality":{"clean":{"n":1197,"win":48.87,"med":-17.19,"avg":40.54,"pnl":15563.09},"tainted":{"n":1828,"win":33.37,"med":-38.81,"avg":12.01,"pnl":-9081.84},"keep_only":{"n":620,"win":62.9,"med":50.91,"avg":64.19,"pnl":10569.45},"keep_only_recent":{"n":423,"win":60.76,"med":53.33,"avg":74.65,"pnl":5924.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:56:15  INFO      Mode: exits
14:56:15  INFO        Daily log -> logs/daily/2026-09-11.md
14:56:15  INFO        Daily log reconciled -> logs/daily/2026-09-11.md (3 ledger rows)
14:56:15  INFO        place_all_stops: checking 1 positions...
14:56:15  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
14:56:15  INFO        [positions] 1/1 (1 valid)
14:56:16  INFO        Daily log -> logs/daily/2026-09-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.07|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.4%  $-0.15                                           HOLD|
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
=== options_live_micro LIVE 2026-09-11T10:56:16.646966-04:00 share=25% ===
2026-09-11 10:56:16,647 INFO === options_live_micro LIVE 2026-09-11T10:56:16.646966-04:00 share=25% ===
Live account equity $227.07 cash $193.04 #225458845 options_level=3
2026-09-11 10:56:16,772 INFO Live account equity $227.07 cash $193.04 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-11 10:56:16,878 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-11 10:56:16,943 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (184 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     7 | WARN | <<<
| Orphaned lots (post-stable) |  1193 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    56 | INFO |
| Total closed lots           |  2187 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1197 med=-17.2% | TAINTED n=1828 med=-38.8% | KEEP-only n=620 med=+50.9% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.07 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T150117Z

- UTC timestamp: `20260911T150117Z`
- GitHub run: [#9736](https://github.com/28twagg-ops/TradingBot/actions/runs/34613486048)
- Run id: `34613486048`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`65s`
- Full logs: `logs/action_runs/20260911T150117Z_live_bot.log`, `logs/action_runs/20260911T150117Z_live_options.log`, `logs/action_runs/20260911T150117Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1197 | 48.9 | -17.2 | +40.5 | $+15,563 |
| TAINTED | 1828 | 33.4 | -38.8 | +12.0 | $-9,082 |
| KEEP-only | 620 | 62.9 | +50.9 | +64.2 | $+10,569 |
| KEEP-only recent | 423 | 60.8 | +53.3 | +74.6 | $+5,924 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T11:01:25.546284-04:00","date":"2026-09-11","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":53.4,"phases_s":{"reconcile":0.21,"cancel":0.06,"manage":3.69,"protective_stops":1.01,"scan":46.22,"entries":1.51},"signals":11,"placed":0,"equity":1000409.04,"open_positions":18,"pending_orders":0,"open_lots":56,"submitted_today":4,"filled_today":4,"unattributed_contracts":0,"top_signals":["S211:CRWD","S210:DOCN","S403:FSLY","S217:HD","S217:UNP","S216:LMT","S216:HON","S217:LLY"],"github_run":"9736","github_run_id":"34613486048","status":"ok","data_quality":{"clean":{"n":1197,"win":48.87,"med":-17.19,"avg":40.54,"pnl":15563.09},"tainted":{"n":1828,"win":33.37,"med":-38.81,"avg":12.01,"pnl":-9081.84},"keep_only":{"n":620,"win":62.9,"med":50.91,"avg":64.19,"pnl":10569.45},"keep_only_recent":{"n":423,"win":60.76,"med":53.33,"avg":74.65,"pnl":5924.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:01:19  INFO      Mode: exits
15:01:20  INFO        Daily log -> logs/daily/2026-09-11.md
15:01:20  INFO        Daily log reconciled -> logs/daily/2026-09-11.md (3 ledger rows)
15:01:20  INFO        place_all_stops: checking 1 positions...
15:01:20  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
15:01:20  INFO        [positions] 1/1 (1 valid)
15:01:21  INFO        Daily log -> logs/daily/2026-09-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.09|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.4%  $-0.13                                           HOLD|
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
=== options_live_micro LIVE 2026-09-11T11:01:22.325406-04:00 share=25% ===
2026-09-11 11:01:22,325 INFO === options_live_micro LIVE 2026-09-11T11:01:22.325406-04:00 share=25% ===
Live account equity $227.09 cash $193.04 #225458845 options_level=3
2026-09-11 11:01:22,454 INFO Live account equity $227.09 cash $193.04 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-11 11:01:22,590 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-11 11:01:22,644 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (184 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     7 | WARN | <<<
| Orphaned lots (post-stable) |  1193 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    56 | INFO |
| Total closed lots           |  2187 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1197 med=-17.2% | TAINTED n=1828 med=-38.8% | KEEP-only n=620 med=+50.9% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.09 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T150605Z

- UTC timestamp: `20260911T150605Z`
- GitHub run: [#9737](https://github.com/28twagg-ops/TradingBot/actions/runs/34613996119)
- Run id: `34613996119`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`70s`
- Full logs: `logs/action_runs/20260911T150605Z_live_bot.log`, `logs/action_runs/20260911T150605Z_live_options.log`, `logs/action_runs/20260911T150605Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1197 | 48.9 | -17.2 | +40.5 | $+15,563 |
| TAINTED | 1828 | 33.4 | -38.8 | +12.0 | $-9,082 |
| KEEP-only | 620 | 62.9 | +50.9 | +64.2 | $+10,569 |
| KEEP-only recent | 423 | 60.8 | +53.3 | +74.6 | $+5,924 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T11:06:11.795736-04:00","date":"2026-09-11","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":58.7,"phases_s":{"reconcile":0.11,"cancel":0.03,"manage":2.49,"protective_stops":0.36,"scan":54.38,"entries":0.82},"signals":11,"placed":0,"equity":1000561.54,"open_positions":18,"pending_orders":0,"open_lots":56,"submitted_today":4,"filled_today":4,"unattributed_contracts":0,"top_signals":["S211:CRWD","S210:DOCN","S403:FSLY","S217:HD","S217:UNP","S216:LMT","S216:HON","S217:LLY"],"github_run":"9737","github_run_id":"34613996119","status":"ok","data_quality":{"clean":{"n":1197,"win":48.87,"med":-17.19,"avg":40.54,"pnl":15563.09},"tainted":{"n":1828,"win":33.37,"med":-38.81,"avg":12.01,"pnl":-9081.84},"keep_only":{"n":620,"win":62.9,"med":50.91,"avg":64.19,"pnl":10569.45},"keep_only_recent":{"n":423,"win":60.76,"med":53.33,"avg":74.65,"pnl":5924.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:06:06  INFO      Mode: exits
15:06:07  INFO        Daily log -> logs/daily/2026-09-11.md
15:06:07  INFO        Daily log reconciled -> logs/daily/2026-09-11.md (3 ledger rows)
15:06:07  INFO        place_all_stops: checking 1 positions...
15:06:07  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
15:06:07  INFO        [positions] 1/1 (1 valid)
15:06:07  INFO        Daily log -> logs/daily/2026-09-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.14|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.2%  $-0.08                                           HOLD|
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
=== options_live_micro LIVE 2026-09-11T11:06:08.959461-04:00 share=25% ===
2026-09-11 11:06:08,959 INFO === options_live_micro LIVE 2026-09-11T11:06:08.959461-04:00 share=25% ===
Live account equity $227.14 cash $193.04 #225458845 options_level=3
2026-09-11 11:06:09,004 INFO Live account equity $227.14 cash $193.04 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-11 11:06:09,080 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-11 11:06:09,108 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (184 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     7 | WARN | <<<
| Orphaned lots (post-stable) |  1193 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    56 | INFO |
| Total closed lots           |  2187 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1197 med=-17.2% | TAINTED n=1828 med=-38.8% | KEEP-only n=620 med=+50.9% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.14 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T151105Z

- UTC timestamp: `20260911T151105Z`
- GitHub run: [#9738](https://github.com/28twagg-ops/TradingBot/actions/runs/34614496173)
- Run id: `34614496173`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`75s`
- Full logs: `logs/action_runs/20260911T151105Z_live_bot.log`, `logs/action_runs/20260911T151105Z_live_options.log`, `logs/action_runs/20260911T151105Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1198 | 48.9 | -16.6 | +40.6 | $+15,590 |
| TAINTED | 1828 | 33.4 | -38.8 | +12.0 | $-9,082 |
| KEEP-only | 621 | 63.0 | +50.9 | +64.2 | $+10,596 |
| KEEP-only recent | 424 | 60.8 | +53.3 | +74.6 | $+5,951 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T11:11:12.032435-04:00","date":"2026-09-11","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":63.9,"phases_s":{"reconcile":0.44,"cancel":0.08,"manage":4.27,"protective_stops":1.6,"scan":54.38,"entries":2.39},"signals":11,"placed":0,"equity":1000625.52,"open_positions":18,"pending_orders":0,"open_lots":55,"submitted_today":4,"filled_today":4,"unattributed_contracts":0,"top_signals":["S211:CRWD","S210:DOCN","S403:FSLY","S217:HD","S217:UNP","S216:LMT","S216:HON","S217:LLY"],"github_run":"9738","github_run_id":"34614496173","status":"ok","data_quality":{"clean":{"n":1198,"win":48.91,"med":-16.6,"avg":40.56,"pnl":15590.09},"tainted":{"n":1828,"win":33.37,"med":-38.81,"avg":12.01,"pnl":-9081.84},"keep_only":{"n":621,"win":62.96,"med":50.94,"avg":64.19,"pnl":10596.45},"keep_only_recent":{"n":424,"win":60.85,"med":53.33,"avg":74.61,"pnl":5951.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:11:06  INFO      Mode: exits
15:11:07  INFO        Daily log -> logs/daily/2026-09-11.md
15:11:07  INFO        Daily log reconciled -> logs/daily/2026-09-11.md (3 ledger rows)
15:11:07  INFO        place_all_stops: checking 1 positions...
15:11:07  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
15:11:07  INFO        [positions] 1/1 (1 valid)
15:11:07  INFO        Daily log -> logs/daily/2026-09-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.18|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.1%  $-0.04                                           HOLD|
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
=== options_live_micro LIVE 2026-09-11T11:11:08.737642-04:00 share=25% ===
2026-09-11 11:11:08,737 INFO === options_live_micro LIVE 2026-09-11T11:11:08.737642-04:00 share=25% ===
Live account equity $227.18 cash $193.04 #225458845 options_level=3
2026-09-11 11:11:08,883 INFO Live account equity $227.18 cash $193.04 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-11 11:11:09,039 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-11 11:11:09,120 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (187 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     6 | WARN | <<<
| Orphaned lots (post-stable) |  1192 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    55 | INFO |
| Total closed lots           |  2188 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1198 med=-16.6% | TAINTED n=1828 med=-38.8% | KEEP-only n=621 med=+50.9% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.18 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T151608Z

- UTC timestamp: `20260911T151608Z`
- GitHub run: [#9739](https://github.com/28twagg-ops/TradingBot/actions/runs/34614996226)
- Run id: `34614996226`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`80s`
- Full logs: `logs/action_runs/20260911T151608Z_live_bot.log`, `logs/action_runs/20260911T151608Z_live_options.log`, `logs/action_runs/20260911T151608Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1199 | 49.0 | -16.0 | +40.6 | $+15,615 |
| TAINTED | 1828 | 33.4 | -38.8 | +12.0 | $-9,082 |
| KEEP-only | 622 | 63.0 | +51.0 | +64.2 | $+10,621 |
| KEEP-only recent | 425 | 60.9 | +53.3 | +74.6 | $+5,976 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T11:16:18.436214-04:00","date":"2026-09-11","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":68.3,"phases_s":{"reconcile":0.55,"cancel":0.16,"manage":5.58,"protective_stops":2.83,"scan":54.02,"entries":4.41},"signals":11,"placed":0,"equity":1000547.0,"open_positions":18,"pending_orders":0,"open_lots":54,"submitted_today":4,"filled_today":4,"unattributed_contracts":0,"top_signals":["S211:CRWD","S210:DOCN","S403:FSLY","S217:HD","S217:UNP","S216:LMT","S216:HON","S217:LLY"],"github_run":"9739","github_run_id":"34614996226","status":"ok","data_quality":{"clean":{"n":1199,"win":48.96,"med":-16.0,"avg":40.58,"pnl":15615.09},"tainted":{"n":1828,"win":33.37,"med":-38.81,"avg":12.01,"pnl":-9081.84},"keep_only":{"n":622,"win":63.02,"med":50.96,"avg":64.18,"pnl":10621.45},"keep_only_recent":{"n":425,"win":60.94,"med":53.33,"avg":74.57,"pnl":5976.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:16:10  INFO      Mode: exits
15:16:13  INFO        Daily log -> logs/daily/2026-09-11.md
15:16:13  INFO        Daily log reconciled -> logs/daily/2026-09-11.md (3 ledger rows)
15:16:13  INFO        place_all_stops: checking 1 positions...
15:16:13  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
15:16:13  INFO        [positions] 1/1 (1 valid)
15:16:13  INFO        Daily log -> logs/daily/2026-09-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.23|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.0%  $+0.01                                           HOLD|
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
=== options_live_micro LIVE 2026-09-11T11:16:14.701198-04:00 share=25% ===
2026-09-11 11:16:14,701 INFO === options_live_micro LIVE 2026-09-11T11:16:14.701198-04:00 share=25% ===
Live account equity $227.23 cash $193.04 #225458845 options_level=3
2026-09-11 11:16:14,947 INFO Live account equity $227.23 cash $193.04 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-11 11:16:15,179 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-11 11:16:15,332 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (186 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     5 | WARN | <<<
| Orphaned lots (post-stable) |  1191 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    54 | INFO |
| Total closed lots           |  2189 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1199 med=-16.0% | TAINTED n=1828 med=-38.8% | KEEP-only n=622 med=+51.0% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.23 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T152105Z

- UTC timestamp: `20260911T152105Z`
- GitHub run: [#9740](https://github.com/28twagg-ops/TradingBot/actions/runs/34615493236)
- Run id: `34615493236`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`63s`
- Full logs: `logs/action_runs/20260911T152105Z_live_bot.log`, `logs/action_runs/20260911T152105Z_live_options.log`, `logs/action_runs/20260911T152105Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1200 | 49.0 | -15.9 | +40.6 | $+15,639 |
| TAINTED | 1828 | 33.4 | -38.8 | +12.0 | $-9,082 |
| KEEP-only | 623 | 63.1 | +51.0 | +64.2 | $+10,645 |
| KEEP-only recent | 426 | 61.0 | +53.3 | +74.5 | $+6,000 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T11:21:11.614459-04:00","date":"2026-09-11","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":51.1,"phases_s":{"reconcile":0.16,"cancel":0.03,"manage":2.72,"protective_stops":0.58,"scan":45.63,"entries":1.48},"signals":11,"placed":0,"equity":1000410.98,"open_positions":18,"pending_orders":0,"open_lots":53,"submitted_today":4,"filled_today":4,"unattributed_contracts":0,"top_signals":["S211:CRWD","S210:DOCN","S403:FSLY","S217:HD","S217:UNP","S216:LMT","S216:HON","S217:LLY"],"github_run":"9740","github_run_id":"34615493236","status":"ok","data_quality":{"clean":{"n":1200,"win":49.0,"med":-15.93,"avg":40.59,"pnl":15639.09},"tainted":{"n":1828,"win":33.37,"med":-38.81,"avg":12.01,"pnl":-9081.84},"keep_only":{"n":623,"win":63.08,"med":50.98,"avg":64.16,"pnl":10645.45},"keep_only_recent":{"n":426,"win":61.03,"med":53.33,"avg":74.52,"pnl":6000.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:21:06  INFO      Mode: exits
15:21:06  INFO        Daily log -> logs/daily/2026-09-11.md
15:21:06  INFO        Daily log reconciled -> logs/daily/2026-09-11.md (3 ledger rows)
15:21:06  INFO        place_all_stops: checking 1 positions...
15:21:06  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
15:21:06  INFO        [positions] 1/1 (1 valid)
15:21:06  INFO        Daily log -> logs/daily/2026-09-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.26|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.1%  $+0.04                                           HOLD|
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
=== options_live_micro LIVE 2026-09-11T11:21:07.747599-04:00 share=25% ===
2026-09-11 11:21:07,747 INFO === options_live_micro LIVE 2026-09-11T11:21:07.747599-04:00 share=25% ===
Live account equity $227.26 cash $193.04 #225458845 options_level=3
2026-09-11 11:21:07,819 INFO Live account equity $227.26 cash $193.04 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-11 11:21:07,881 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-11 11:21:07,930 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (184 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1190 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    53 | INFO |
| Total closed lots           |  2190 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1200 med=-15.9% | TAINTED n=1828 med=-38.8% | KEEP-only n=623 med=+51.0% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T152604Z

- UTC timestamp: `20260911T152604Z`
- GitHub run: [#9741](https://github.com/28twagg-ops/TradingBot/actions/runs/34615988391)
- Run id: `34615988391`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`80s`
- Full logs: `logs/action_runs/20260911T152604Z_live_bot.log`, `logs/action_runs/20260911T152604Z_live_options.log`, `logs/action_runs/20260911T152604Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1200 | 49.0 | -15.9 | +40.6 | $+15,639 |
| TAINTED | 1828 | 33.4 | -38.8 | +12.0 | $-9,082 |
| KEEP-only | 623 | 63.1 | +51.0 | +64.2 | $+10,645 |
| KEEP-only recent | 426 | 61.0 | +53.3 | +74.5 | $+6,000 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T11:26:12.130743-04:00","date":"2026-09-11","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":67.4,"phases_s":{"reconcile":0.5,"cancel":0.14,"manage":5.15,"protective_stops":2.8,"scan":54.2,"entries":3.81},"signals":11,"placed":0,"equity":1000448.98,"open_positions":18,"pending_orders":0,"open_lots":53,"submitted_today":4,"filled_today":4,"unattributed_contracts":0,"top_signals":["S211:CRWD","S210:DOCN","S403:FSLY","S217:HD","S217:UNP","S216:LMT","S216:HON","S217:LLY"],"github_run":"9741","github_run_id":"34615988391","status":"ok","data_quality":{"clean":{"n":1200,"win":49.0,"med":-15.93,"avg":40.59,"pnl":15639.09},"tainted":{"n":1828,"win":33.37,"med":-38.81,"avg":12.01,"pnl":-9081.84},"keep_only":{"n":623,"win":63.08,"med":50.98,"avg":64.16,"pnl":10645.45},"keep_only_recent":{"n":426,"win":61.03,"med":53.33,"avg":74.52,"pnl":6000.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:26:05  INFO      Mode: exits
15:26:06  INFO        Daily log -> logs/daily/2026-09-11.md
15:26:06  INFO        Daily log reconciled -> logs/daily/2026-09-11.md (3 ledger rows)
15:26:06  INFO        place_all_stops: checking 1 positions...
15:26:06  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
15:26:06  INFO        [positions] 1/1 (1 valid)
15:26:07  INFO        Daily log -> logs/daily/2026-09-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.25|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.1%  $+0.03                                           HOLD|
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
=== options_live_micro LIVE 2026-09-11T11:26:08.209718-04:00 share=25% ===
2026-09-11 11:26:08,209 INFO === options_live_micro LIVE 2026-09-11T11:26:08.209718-04:00 share=25% ===
Live account equity $227.25 cash $193.04 #225458845 options_level=3
2026-09-11 11:26:08,440 INFO Live account equity $227.25 cash $193.04 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-11 11:26:08,706 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-11 11:26:08,856 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (186 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1190 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    53 | INFO |
| Total closed lots           |  2190 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1200 med=-15.9% | TAINTED n=1828 med=-38.8% | KEEP-only n=623 med=+51.0% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.25 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T153104Z

- UTC timestamp: `20260911T153104Z`
- GitHub run: [#9742](https://github.com/28twagg-ops/TradingBot/actions/runs/34616484052)
- Run id: `34616484052`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`44s`
- Full logs: `logs/action_runs/20260911T153104Z_live_bot.log`, `logs/action_runs/20260911T153104Z_live_options.log`, `logs/action_runs/20260911T153104Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1202 | 49.1 | -14.2 | +40.7 | $+15,750 |
| TAINTED | 1828 | 33.4 | -38.8 | +12.0 | $-9,082 |
| KEEP-only | 624 | 63.1 | +51.2 | +64.2 | $+10,672 |
| KEEP-only recent | 427 | 61.1 | +53.3 | +74.5 | $+6,027 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T11:31:09.572350-04:00","date":"2026-09-11","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":36.4,"phases_s":{"reconcile":0.56,"cancel":0.12,"manage":5.23,"protective_stops":1.99,"scan":24.58,"entries":3.28},"signals":11,"placed":0,"equity":1000622.94,"open_positions":17,"pending_orders":0,"open_lots":51,"submitted_today":4,"filled_today":4,"unattributed_contracts":0,"top_signals":["S211:CRWD","S210:DOCN","S403:FSLY","S217:HD","S217:UNP","S216:LMT","S216:HON","S217:LLY"],"github_run":"9742","github_run_id":"34616484052","status":"ok","data_quality":{"clean":{"n":1202,"win":49.08,"med":-14.18,"avg":40.72,"pnl":15749.82},"tainted":{"n":1828,"win":33.37,"med":-38.81,"avg":12.01,"pnl":-9081.84},"keep_only":{"n":624,"win":63.14,"med":51.18,"avg":64.16,"pnl":10672.45},"keep_only_recent":{"n":427,"win":61.12,"med":53.33,"avg":74.5,"pnl":6027.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:31:04  INFO      Mode: exits
15:31:05  INFO        Daily log -> logs/daily/2026-09-11.md
15:31:05  INFO        Daily log reconciled -> logs/daily/2026-09-11.md (3 ledger rows)
15:31:05  INFO        place_all_stops: checking 1 positions...
15:31:05  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
15:31:05  INFO        [positions] 1/1 (1 valid)
15:31:06  INFO        Daily log -> logs/daily/2026-09-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.21|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.0%  $-0.01                                           HOLD|
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
=== options_live_micro LIVE 2026-09-11T11:31:06.712779-04:00 share=25% ===
2026-09-11 11:31:06,712 INFO === options_live_micro LIVE 2026-09-11T11:31:06.712779-04:00 share=25% ===
Live account equity $227.21 cash $193.04 #225458845 options_level=3
2026-09-11 11:31:06,914 INFO Live account equity $227.21 cash $193.04 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-11 11:31:07,089 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-11 11:31:07,204 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (187 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1190 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    51 | INFO |
| Total closed lots           |  2191 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1202 med=-14.2% | TAINTED n=1828 med=-38.8% | KEEP-only n=624 med=+51.2% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.21 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T153611Z

- UTC timestamp: `20260911T153611Z`
- GitHub run: [#9743](https://github.com/28twagg-ops/TradingBot/actions/runs/34616981105)
- Run id: `34616981105`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`19s`
- Full logs: `logs/action_runs/20260911T153611Z_live_bot.log`, `logs/action_runs/20260911T153611Z_live_options.log`, `logs/action_runs/20260911T153611Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1203 | 49.1 | -12.5 | +40.8 | $+15,783 |
| TAINTED | 1828 | 33.4 | -38.8 | +12.0 | $-9,082 |
| KEEP-only | 625 | 63.2 | +51.4 | +64.2 | $+10,705 |
| KEEP-only recent | 428 | 61.2 | +53.3 | +74.5 | $+6,060 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T11:36:18.823051-04:00","date":"2026-09-11","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":9.5,"phases_s":{"reconcile":0.96,"cancel":0.21,"manage":5.32,"protective_stops":2.21},"signals":0,"placed":0,"equity":1000501.92,"open_positions":17,"pending_orders":0,"open_lots":50,"submitted_today":4,"filled_today":4,"unattributed_contracts":0,"top_signals":[],"github_run":"9743","github_run_id":"34616981105","status":"ok","data_quality":{"clean":{"n":1203,"win":49.13,"med":-12.5,"avg":40.76,"pnl":15782.82},"tainted":{"n":1828,"win":33.37,"med":-38.81,"avg":12.01,"pnl":-9081.84},"keep_only":{"n":625,"win":63.2,"med":51.39,"avg":64.18,"pnl":10705.45},"keep_only_recent":{"n":428,"win":61.21,"med":53.33,"avg":74.51,"pnl":6060.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:36:12  INFO      Mode: exits
15:36:14  INFO        Daily log -> logs/daily/2026-09-11.md
15:36:14  INFO        Daily log reconciled -> logs/daily/2026-09-11.md (3 ledger rows)
15:36:14  INFO        place_all_stops: checking 1 positions...
15:36:14  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
15:36:14  INFO        [positions] 1/1 (1 valid)
15:36:14  INFO        Daily log -> logs/daily/2026-09-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.20|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.1%  $-0.02                                           HOLD|
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
=== options_live_micro LIVE 2026-09-11T11:36:15.381591-04:00 share=25% ===
2026-09-11 11:36:15,381 INFO === options_live_micro LIVE 2026-09-11T11:36:15.381591-04:00 share=25% ===
Live account equity $227.20 cash $193.04 #225458845 options_level=3
2026-09-11 11:36:15,614 INFO Live account equity $227.20 cash $193.04 #225458845 options_level=3
Live micro: manage/exits only
2026-09-11 11:36:15,845 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-11 11:36:15,979 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (180 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1190 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2192 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1203 med=-12.5% | TAINTED n=1828 med=-38.8% | KEEP-only n=625 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.2 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260911T154108Z

- UTC timestamp: `20260911T154108Z`
- GitHub run: [#9744](https://github.com/28twagg-ops/TradingBot/actions/runs/34617475774)
- Run id: `34617475774`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`16s`
- Full logs: `logs/action_runs/20260911T154108Z_live_bot.log`, `logs/action_runs/20260911T154108Z_live_options.log`, `logs/action_runs/20260911T154108Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1203 | 49.1 | -12.5 | +40.8 | $+15,783 |
| TAINTED | 1828 | 33.4 | -38.8 | +12.0 | $-9,082 |
| KEEP-only | 625 | 63.2 | +51.4 | +64.2 | $+10,705 |
| KEEP-only recent | 428 | 61.2 | +53.3 | +74.5 | $+6,060 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-11T11:41:14.171959-04:00","date":"2026-09-11","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.1,"phases_s":{"reconcile":0.12,"cancel":0.05,"manage":2.78,"protective_stops":0.51},"signals":0,"placed":0,"equity":1000529.42,"open_positions":17,"pending_orders":0,"open_lots":50,"submitted_today":4,"filled_today":4,"unattributed_contracts":0,"top_signals":[],"github_run":"9744","github_run_id":"34617475774","status":"ok","data_quality":{"clean":{"n":1203,"win":49.13,"med":-12.5,"avg":40.76,"pnl":15782.82},"tainted":{"n":1828,"win":33.37,"med":-38.81,"avg":12.01,"pnl":-9081.84},"keep_only":{"n":625,"win":63.2,"med":51.39,"avg":64.18,"pnl":10705.45},"keep_only_recent":{"n":428,"win":61.21,"med":53.33,"avg":74.51,"pnl":6060.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:41:09  INFO      Mode: exits
15:41:09  INFO        Daily log -> logs/daily/2026-09-11.md
15:41:09  INFO        Daily log reconciled -> logs/daily/2026-09-11.md (3 ledger rows)
15:41:09  INFO        place_all_stops: checking 1 positions...
15:41:09  INFO        STOP skipped AMZN: fractional (0.1335 shares) — software exit will handle it
15:41:09  INFO        [positions] 1/1 (1 valid)
15:41:10  INFO        Daily log -> logs/daily/2026-09-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.22|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.0%  $+0.00                                           HOLD|
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
=== options_live_micro LIVE 2026-09-11T11:41:10.861684-04:00 share=25% ===
2026-09-11 11:41:10,861 INFO === options_live_micro LIVE 2026-09-11T11:41:10.861684-04:00 share=25% ===
Live account equity $227.22 cash $193.04 #225458845 options_level=3
2026-09-11 11:41:10,920 INFO Live account equity $227.22 cash $193.04 #225458845 options_level=3
Live micro: manage/exits only
2026-09-11 11:41:10,990 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-11 11:41:11,001 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (179 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1190 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2192 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-11_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1203 med=-12.5% | TAINTED n=1828 med=-38.8% | KEEP-only n=625 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.22 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
