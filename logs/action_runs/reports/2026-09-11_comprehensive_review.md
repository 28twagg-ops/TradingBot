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
