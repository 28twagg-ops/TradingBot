# Daily Comprehensive Action Review - 2026-09-09

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260909T130110Z

- UTC timestamp: `20260909T130110Z`
- GitHub run: [#9448](https://github.com/28twagg-ops/TradingBot/actions/runs/34354336212)
- Run id: `34354336212`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260909T130110Z_live_bot.log`, `logs/action_runs/20260909T130110Z_live_options.log`, `logs/action_runs/20260909T130110Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1095 | 50.5 | +20.0 | +45.6 | $+16,013 |
| TAINTED | 1796 | 33.6 | -38.3 | +12.8 | $-8,550 |
| KEEP-only | 621 | 64.1 | +51.6 | +72.6 | $+11,127 |
| KEEP-only recent | 413 | 61.5 | +53.8 | +85.9 | $+5,870 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-09T09:01:16.907066-04:00","date":"2026-09-09","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.51},"signals":0,"placed":0,"equity":1003946.57,"open_positions":29,"pending_orders":0,"open_lots":102,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9448","github_run_id":"34354336212","status":"ok","data_quality":{"clean":{"n":1095,"win":50.5,"med":20.0,"avg":45.57,"pnl":16012.59},"tainted":{"n":1796,"win":33.63,"med":-38.25,"avg":12.79,"pnl":-8549.84},"keep_only":{"n":621,"win":64.09,"med":51.61,"avg":72.64,"pnl":11127.45},"keep_only_recent":{"n":413,"win":61.5,"med":53.85,"avg":85.88,"pnl":5870.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:01:12  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $229.18|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $229.18|
|  Cash                                                           $160.77|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $68.41|
|  Open P&L                                                        $-0.57|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MGM      MomReversal     $34.46     $40.92   $40.88   -0.1%   $-0.03  |
|  MKSI     MomReversal     $33.95     $266.16  $262.00  -1.6%   $-0.54  |
|                                                                        |
|  Total invested                                                  $68.41|
|  Total open P&L                                                  $-0.57|
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
|  2026-09-08  SELL  AMCR  Pullback50  $34.40  P&L $-0.19                |
|  2026-09-08  SELL  APD  Pullback50  $34.39  P&L $-0.20                 |
|  2026-09-08  SELL  ABBV  Pullback50  $34.41  P&L $-0.18                |
|  2026-09-04  SELL  APD  Pullback50  $34.37  P&L $-0.21                 |
|  2026-09-03  SELL  ACGL  Pullback50  $34.56  P&L $-0.00                |
|  2026-09-03  SELL  CNM  MomReversal  $34.27  P&L $-0.24                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-09T09:01:13.512852-04:00 share=25% ===
2026-09-09 09:01:13,512 INFO === options_live_micro LIVE 2026-09-09T09:01:13.512852-04:00 share=25% ===
Live account equity $229.18 cash $160.77 #225458845 options_level=3
2026-09-09 09:01:13,735 INFO Live account equity $229.18 cash $160.77 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-09 09:01:13,789 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-09 09:01:13,858 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (159 earlier lines - see full log file)
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
## Ledger health — 2026-09-09
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1071 | WARN | <<<
| Missing exit records (post) |  1069 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   102 | INFO |
| Total closed lots           |  2067 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-09_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-09_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1095 med=+20.0% | TAINTED n=1796 med=-38.3% | KEEP-only n=621 med=+51.6% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=229.18 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260909T130610Z

- UTC timestamp: `20260909T130610Z`
- GitHub run: [#9449](https://github.com/28twagg-ops/TradingBot/actions/runs/34354855702)
- Run id: `34354855702`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260909T130610Z_live_bot.log`, `logs/action_runs/20260909T130610Z_live_options.log`, `logs/action_runs/20260909T130610Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1095 | 50.5 | +20.0 | +45.6 | $+16,013 |
| TAINTED | 1796 | 33.6 | -38.3 | +12.8 | $-8,550 |
| KEEP-only | 621 | 64.1 | +51.6 | +72.6 | $+11,127 |
| KEEP-only recent | 413 | 61.5 | +53.8 | +85.9 | $+5,870 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-09T09:06:16.745466-04:00","date":"2026-09-09","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.56},"signals":0,"placed":0,"equity":1003884.63,"open_positions":29,"pending_orders":0,"open_lots":102,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9449","github_run_id":"34354855702","status":"ok","data_quality":{"clean":{"n":1095,"win":50.5,"med":20.0,"avg":45.57,"pnl":16012.59},"tainted":{"n":1796,"win":33.63,"med":-38.25,"avg":12.79,"pnl":-8549.84},"keep_only":{"n":621,"win":64.09,"med":51.61,"avg":72.64,"pnl":11127.45},"keep_only_recent":{"n":413,"win":61.5,"med":53.85,"avg":85.88,"pnl":5870.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:06:11  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $229.27|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $229.27|
|  Cash                                                           $160.77|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $68.50|
|  Open P&L                                                        $-0.48|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MGM      MomReversal     $34.46     $40.92   $40.88   -0.1%   $-0.03  |
|  MKSI     MomReversal     $34.04     $266.16  $262.72  -1.3%   $-0.45  |
|                                                                        |
|  Total invested                                                  $68.50|
|  Total open P&L                                                  $-0.48|
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
|  2026-09-08  SELL  AMCR  Pullback50  $34.40  P&L $-0.19                |
|  2026-09-08  SELL  APD  Pullback50  $34.39  P&L $-0.20                 |
|  2026-09-08  SELL  ABBV  Pullback50  $34.41  P&L $-0.18                |
|  2026-09-04  SELL  APD  Pullback50  $34.37  P&L $-0.21                 |
|  2026-09-03  SELL  ACGL  Pullback50  $34.56  P&L $-0.00                |
|  2026-09-03  SELL  CNM  MomReversal  $34.27  P&L $-0.24                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-09T09:06:13.083539-04:00 share=25% ===
2026-09-09 09:06:13,083 INFO === options_live_micro LIVE 2026-09-09T09:06:13.083539-04:00 share=25% ===
Live account equity $229.27 cash $160.77 #225458845 options_level=3
2026-09-09 09:06:13,304 INFO Live account equity $229.27 cash $160.77 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-09 09:06:13,373 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-09 09:06:13,442 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (159 earlier lines - see full log file)
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
## Ledger health — 2026-09-09
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1071 | WARN | <<<
| Missing exit records (post) |  1069 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   102 | INFO |
| Total closed lots           |  2067 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-09_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-09_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1095 med=+20.0% | TAINTED n=1796 med=-38.3% | KEEP-only n=621 med=+51.6% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=229.27 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260909T131108Z

- UTC timestamp: `20260909T131108Z`
- GitHub run: [#9450](https://github.com/28twagg-ops/TradingBot/actions/runs/34355367836)
- Run id: `34355367836`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`15s`
- Full logs: `logs/action_runs/20260909T131108Z_live_bot.log`, `logs/action_runs/20260909T131108Z_live_options.log`, `logs/action_runs/20260909T131108Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1095 | 50.5 | +20.0 | +45.6 | $+16,013 |
| TAINTED | 1796 | 33.6 | -38.3 | +12.8 | $-8,550 |
| KEEP-only | 621 | 64.1 | +51.6 | +72.6 | $+11,127 |
| KEEP-only recent | 413 | 61.5 | +53.8 | +85.9 | $+5,870 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-09T09:11:16.516525-04:00","date":"2026-09-09","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.5,"phases_s":{"reconcile":0.57},"signals":0,"placed":0,"equity":1003904.57,"open_positions":29,"pending_orders":0,"open_lots":102,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9450","github_run_id":"34355367836","status":"ok","data_quality":{"clean":{"n":1095,"win":50.5,"med":20.0,"avg":45.57,"pnl":16012.59},"tainted":{"n":1796,"win":33.63,"med":-38.25,"avg":12.79,"pnl":-8549.84},"keep_only":{"n":621,"win":64.09,"med":51.61,"avg":72.64,"pnl":11127.45},"keep_only_recent":{"n":413,"win":61.5,"med":53.85,"avg":85.88,"pnl":5870.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
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
|  Equity                                                         $229.27|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $229.27|
|  Cash                                                           $160.77|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $68.50|
|  Open P&L                                                        $-0.48|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MGM      MomReversal     $34.46     $40.92   $40.88   -0.1%   $-0.03  |
|  MKSI     MomReversal     $34.04     $266.16  $262.72  -1.3%   $-0.45  |
|                                                                        |
|  Total invested                                                  $68.50|
|  Total open P&L                                                  $-0.48|
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
|  2026-09-08  SELL  AMCR  Pullback50  $34.40  P&L $-0.19                |
|  2026-09-08  SELL  APD  Pullback50  $34.39  P&L $-0.20                 |
|  2026-09-08  SELL  ABBV  Pullback50  $34.41  P&L $-0.18                |
|  2026-09-04  SELL  APD  Pullback50  $34.37  P&L $-0.21                 |
|  2026-09-03  SELL  ACGL  Pullback50  $34.56  P&L $-0.00                |
|  2026-09-03  SELL  CNM  MomReversal  $34.27  P&L $-0.24                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-09T09:11:11.713622-04:00 share=25% ===
2026-09-09 09:11:11,713 INFO === options_live_micro LIVE 2026-09-09T09:11:11.713622-04:00 share=25% ===
Live account equity $229.27 cash $160.77 #225458845 options_level=3
2026-09-09 09:11:11,938 INFO Live account equity $229.27 cash $160.77 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-09 09:11:12,073 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-09 09:11:12,141 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (159 earlier lines - see full log file)
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
## Ledger health — 2026-09-09
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1071 | WARN | <<<
| Missing exit records (post) |  1069 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   102 | INFO |
| Total closed lots           |  2067 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-09_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-09_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1095 med=+20.0% | TAINTED n=1796 med=-38.3% | KEEP-only n=621 med=+51.6% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=229.27 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260909T131607Z

- UTC timestamp: `20260909T131607Z`
- GitHub run: [#9451](https://github.com/28twagg-ops/TradingBot/actions/runs/34355885993)
- Run id: `34355885993`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260909T131607Z_live_bot.log`, `logs/action_runs/20260909T131607Z_live_options.log`, `logs/action_runs/20260909T131607Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1095 | 50.5 | +20.0 | +45.6 | $+16,013 |
| TAINTED | 1796 | 33.6 | -38.3 | +12.8 | $-8,550 |
| KEEP-only | 621 | 64.1 | +51.6 | +72.6 | $+11,127 |
| KEEP-only recent | 413 | 61.5 | +53.8 | +85.9 | $+5,870 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-09T09:16:13.901178-04:00","date":"2026-09-09","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.56},"signals":0,"placed":0,"equity":1003886.57,"open_positions":29,"pending_orders":0,"open_lots":102,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9451","github_run_id":"34355885993","status":"ok","data_quality":{"clean":{"n":1095,"win":50.5,"med":20.0,"avg":45.57,"pnl":16012.59},"tainted":{"n":1796,"win":33.63,"med":-38.25,"avg":12.79,"pnl":-8549.84},"keep_only":{"n":621,"win":64.09,"med":51.61,"avg":72.64,"pnl":11127.45},"keep_only_recent":{"n":413,"win":61.5,"med":53.85,"avg":85.88,"pnl":5870.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:16:08  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $229.27|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $229.27|
|  Cash                                                           $160.77|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $68.50|
|  Open P&L                                                        $-0.48|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MGM      MomReversal     $34.46     $40.92   $40.88   -0.1%   $-0.03  |
|  MKSI     MomReversal     $34.04     $266.16  $262.72  -1.3%   $-0.45  |
|                                                                        |
|  Total invested                                                  $68.50|
|  Total open P&L                                                  $-0.48|
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
|  2026-09-08  SELL  AMCR  Pullback50  $34.40  P&L $-0.19                |
|  2026-09-08  SELL  APD  Pullback50  $34.39  P&L $-0.20                 |
|  2026-09-08  SELL  ABBV  Pullback50  $34.41  P&L $-0.18                |
|  2026-09-04  SELL  APD  Pullback50  $34.37  P&L $-0.21                 |
|  2026-09-03  SELL  ACGL  Pullback50  $34.56  P&L $-0.00                |
|  2026-09-03  SELL  CNM  MomReversal  $34.27  P&L $-0.24                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-09T09:16:10.076989-04:00 share=25% ===
2026-09-09 09:16:10,077 INFO === options_live_micro LIVE 2026-09-09T09:16:10.076989-04:00 share=25% ===
Live account equity $229.27 cash $160.77 #225458845 options_level=3
2026-09-09 09:16:10,299 INFO Live account equity $229.27 cash $160.77 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-09 09:16:10,367 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-09 09:16:10,434 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (159 earlier lines - see full log file)
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
## Ledger health — 2026-09-09
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1071 | WARN | <<<
| Missing exit records (post) |  1069 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   102 | INFO |
| Total closed lots           |  2067 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-09_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-09_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1095 med=+20.0% | TAINTED n=1796 med=-38.3% | KEEP-only n=621 med=+51.6% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=229.27 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260909T132105Z

- UTC timestamp: `20260909T132105Z`
- GitHub run: [#9452](https://github.com/28twagg-ops/TradingBot/actions/runs/34356404540)
- Run id: `34356404540`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260909T132105Z_live_bot.log`, `logs/action_runs/20260909T132105Z_live_options.log`, `logs/action_runs/20260909T132105Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1095 | 50.5 | +20.0 | +45.6 | $+16,013 |
| TAINTED | 1796 | 33.6 | -38.3 | +12.8 | $-8,550 |
| KEEP-only | 621 | 64.1 | +51.6 | +72.6 | $+11,127 |
| KEEP-only recent | 413 | 61.5 | +53.8 | +85.9 | $+5,870 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-09T09:21:11.251687-04:00","date":"2026-09-09","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.34},"signals":0,"placed":0,"equity":1003842.57,"open_positions":29,"pending_orders":0,"open_lots":102,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9452","github_run_id":"34356404540","status":"ok","data_quality":{"clean":{"n":1095,"win":50.5,"med":20.0,"avg":45.57,"pnl":16012.59},"tainted":{"n":1796,"win":33.63,"med":-38.25,"avg":12.79,"pnl":-8549.84},"keep_only":{"n":621,"win":64.09,"med":51.61,"avg":72.64,"pnl":11127.45},"keep_only_recent":{"n":413,"win":61.5,"med":53.85,"avg":85.88,"pnl":5870.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:21:06  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $229.27|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $229.27|
|  Cash                                                           $160.77|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $68.50|
|  Open P&L                                                        $-0.48|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MGM      MomReversal     $34.46     $40.92   $40.88   -0.1%   $-0.03  |
|  MKSI     MomReversal     $34.04     $266.16  $262.72  -1.3%   $-0.45  |
|                                                                        |
|  Total invested                                                  $68.50|
|  Total open P&L                                                  $-0.48|
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
|  2026-09-08  SELL  AMCR  Pullback50  $34.40  P&L $-0.19                |
|  2026-09-08  SELL  APD  Pullback50  $34.39  P&L $-0.20                 |
|  2026-09-08  SELL  ABBV  Pullback50  $34.41  P&L $-0.18                |
|  2026-09-04  SELL  APD  Pullback50  $34.37  P&L $-0.21                 |
|  2026-09-03  SELL  ACGL  Pullback50  $34.56  P&L $-0.00                |
|  2026-09-03  SELL  CNM  MomReversal  $34.27  P&L $-0.24                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-09T09:21:08.084336-04:00 share=25% ===
2026-09-09 09:21:08,084 INFO === options_live_micro LIVE 2026-09-09T09:21:08.084336-04:00 share=25% ===
Live account equity $229.27 cash $160.77 #225458845 options_level=3
2026-09-09 09:21:08,187 INFO Live account equity $229.27 cash $160.77 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-09 09:21:08,212 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-09 09:21:08,237 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (159 earlier lines - see full log file)
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
## Ledger health — 2026-09-09
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1071 | WARN | <<<
| Missing exit records (post) |  1069 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   102 | INFO |
| Total closed lots           |  2067 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-09_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-09_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1095 med=+20.0% | TAINTED n=1796 med=-38.3% | KEEP-only n=621 med=+51.6% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=229.27 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260909T132608Z

- UTC timestamp: `20260909T132608Z`
- GitHub run: [#9453](https://github.com/28twagg-ops/TradingBot/actions/runs/34356931247)
- Run id: `34356931247`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260909T132608Z_live_bot.log`, `logs/action_runs/20260909T132608Z_live_options.log`, `logs/action_runs/20260909T132608Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1095 | 50.5 | +20.0 | +45.6 | $+16,013 |
| TAINTED | 1796 | 33.6 | -38.3 | +12.8 | $-8,550 |
| KEEP-only | 621 | 64.1 | +51.6 | +72.6 | $+11,127 |
| KEEP-only recent | 413 | 61.5 | +53.8 | +85.9 | $+5,870 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-09T09:26:14.881436-04:00","date":"2026-09-09","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":1003831.57,"open_positions":29,"pending_orders":0,"open_lots":102,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9453","github_run_id":"34356931247","status":"ok","data_quality":{"clean":{"n":1095,"win":50.5,"med":20.0,"avg":45.57,"pnl":16012.59},"tainted":{"n":1796,"win":33.63,"med":-38.25,"avg":12.79,"pnl":-8549.84},"keep_only":{"n":621,"win":64.09,"med":51.61,"avg":72.64,"pnl":11127.45},"keep_only_recent":{"n":413,"win":61.5,"med":53.85,"avg":85.88,"pnl":5870.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:26:09  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $229.27|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $229.27|
|  Cash                                                           $160.77|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $68.50|
|  Open P&L                                                        $-0.48|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MGM      MomReversal     $34.46     $40.92   $40.88   -0.1%   $-0.03  |
|  MKSI     MomReversal     $34.04     $266.16  $262.72  -1.3%   $-0.45  |
|                                                                        |
|  Total invested                                                  $68.50|
|  Total open P&L                                                  $-0.48|
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
|  2026-09-08  SELL  AMCR  Pullback50  $34.40  P&L $-0.19                |
|  2026-09-08  SELL  APD  Pullback50  $34.39  P&L $-0.20                 |
|  2026-09-08  SELL  ABBV  Pullback50  $34.41  P&L $-0.18                |
|  2026-09-04  SELL  APD  Pullback50  $34.37  P&L $-0.21                 |
|  2026-09-03  SELL  ACGL  Pullback50  $34.56  P&L $-0.00                |
|  2026-09-03  SELL  CNM  MomReversal  $34.27  P&L $-0.24                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-09T09:26:11.446155-04:00 share=25% ===
2026-09-09 09:26:11,446 INFO === options_live_micro LIVE 2026-09-09T09:26:11.446155-04:00 share=25% ===
Live account equity $229.27 cash $160.77 #225458845 options_level=3
2026-09-09 09:26:11,670 INFO Live account equity $229.27 cash $160.77 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-09 09:26:11,739 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-09 09:26:11,806 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (159 earlier lines - see full log file)
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
## Ledger health — 2026-09-09
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |  1071 | WARN | <<<
| Missing exit records (post) |  1069 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   102 | INFO |
| Total closed lots           |  2067 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-09_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-09_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1095 med=+20.0% | TAINTED n=1796 med=-38.3% | KEEP-only n=621 med=+51.6% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=229.27 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260909T133103Z

- UTC timestamp: `20260909T133103Z`
- GitHub run: [#9454](https://github.com/28twagg-ops/TradingBot/actions/runs/34357457294)
- Run id: `34357457294`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260909T133103Z_live_bot.log`, `logs/action_runs/20260909T133103Z_live_options.log`, `logs/action_runs/20260909T133103Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1095 | 50.5 | +20.0 | +45.6 | $+16,013 |
| TAINTED | 1796 | 33.6 | -38.3 | +12.8 | $-8,550 |
| KEEP-only | 621 | 64.1 | +51.6 | +72.6 | $+11,127 |
| KEEP-only recent | 413 | 61.5 | +53.8 | +85.9 | $+5,870 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-09T09:26:14.881436-04:00","date":"2026-09-09","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":1003831.57,"open_positions":29,"pending_orders":0,"open_lots":102,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9453","github_run_id":"34356931247","status":"ok","data_quality":{"clean":{"n":1095,"win":50.5,"med":20.0,"avg":45.57,"pnl":16012.59},"tainted":{"n":1796,"win":33.63,"med":-38.25,"avg":12.79,"pnl":-8549.84},"keep_only":{"n":621,"win":64.09,"med":51.61,"avg":72.64,"pnl":11127.45},"keep_only_recent":{"n":413,"win":61.5,"med":53.85,"avg":85.88,"pnl":5870.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:31:04  INFO      Mode: morning_prep
13:31:05  INFO        [prep_positions] 2/2 (2 valid)
13:31:05  INFO      Fetching tickers (universe=both)...
13:31:05  INFO        S&P 500: 503
13:31:05  INFO        MidCap 400: 400
13:31:05  INFO        Total: 903 tickers
13:31:07  INFO        [prep_universe] 40/901 (40 valid)
13:31:09  INFO        [prep_universe] 80/901 (80 valid)
13:31:10  INFO        [prep_universe] 120/901 (120 valid)
13:31:12  INFO        [prep_universe] 160/901 (160 valid)
13:31:13  INFO        [prep_universe] 200/901 (199 valid)
13:31:20  INFO        [prep_universe] 240/901 (238 valid)
13:31:30  INFO        [prep_universe] 280/901 (278 valid)
13:31:43  INFO        [prep_universe] 320/901 (318 valid)
13:31:56  INFO        [prep_universe] 360/901 (358 valid)
13:32:06  INFO        [prep_universe] 400/901 (397 valid)
13:32:19  INFO        [prep_universe] 440/901 (437 valid)
13:32:32  INFO        [prep_universe] 480/901 (477 valid)
13:32:42  INFO        [prep_universe] 520/901 (517 valid)
13:32:56  INFO        [prep_universe] 560/901 (557 valid)
13:33:06  INFO        [prep_universe] 600/901 (597 valid)
13:33:19  INFO        [prep_universe] 640/901 (637 valid)
13:33:32  INFO        [prep_universe] 680/901 (677 valid)
13:33:42  INFO        [prep_universe] 720/901 (717 valid)
13:33:55  INFO        [prep_universe] 760/901 (757 valid)
13:34:08  INFO        [prep_universe] 800/901 (797 valid)
13:34:18  INFO        [prep_universe] 840/901 (837 valid)
13:34:31  INFO        [prep_universe] 880/901 (877 valid)
13:34:38  INFO        [prep_universe] 901/901 (898 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $229.33|
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
|  Invested                                                        $68.56|
|  Open P&L                                                        $-0.42|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MGM      MomReversal     $34.31     $40.92   $40.71   -0.5%   $-0.18  |
|  MKSI     MomReversal     $34.25     $266.16  $264.27  -0.7%   $-0.24  |
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
|  Signal candidates                                                   32|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-09T09:34:40.990559-04:00 share=25% ===
2026-09-09 09:34:40,990 INFO === options_live_micro LIVE 2026-09-09T09:34:40.990559-04:00 share=25% ===
Live account equity $229.63 cash $160.77 #225458845 options_level=3
2026-09-09 09:34:41,089 INFO Live account equity $229.63 cash $160.77 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-09 09:34:41,172 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-09 09:34:41,231 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=102 paper_keys=yes dry_run=False
  alpaca positions=28
  FLAG b437|S366|561eb755 missing from Alpaca
  FLAG b436|S366|2a2bf121 missing from Alpaca
  FLAG b237|S401|f05d12e3 missing from Alpaca
  FLAG b263|S403|7aaacc03 missing from Alpaca
  FLAG b262|S403|000e4fa3 missing from Alpaca
  FLAG b235|S401|aedd4437 missing from Alpaca
  FLAG b234|S401|bee86171 missing from Alpaca
  FLAG b0|ORPHAN|aec42dbd missing from Alpaca
  FLAG b197|S218|0aae1fae missing from Alpaca
  FLAG b196|S218|8fc32f76 missing from Alpaca
  FLAG b269|S403|dd548bed missing from Alpaca
  FLAG b268|S403|ba6e2116 missing from Alpaca
  FLAG b241|S401|f12d3e43 missing from Alpaca
  FLAG b240|S401|9574402b missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$1,003,697.12
  buying_power=$3,927,645.68 cash=$1,036,743.12
  open option orders: 20
    MARA260911C00012000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    MARA260911C00012500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    PANW260911C00360000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    CRWD260911C00222500 OrderSide.SELL qty=3 status=OrderStatus.NEW limit=None
    SNOW260911C00365000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
  open option positions: 27
    AVGO260909C00375000 qty=-1 mkt=$-21.00
    AVGO260909C00380000 qty=-1 mkt=$-7.00
    AVGO260911C00400000 qty=4 mkt=$52.00
    COIN260911C00215000 qty=1 mkt=$8.00
    CRWD260911C00222500 qty=3 mkt=$261.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-09T09:34:44.455603-04:00 ===

[Run context]
Paper auth OK — equity $1003659.12, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b330|lab0330_s357_w2_1005_1045_r1|S357] stop_loss (-88.9%) SELL failed PATH260925C00017000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-09 09:34:45,949 INFO   EXIT [b1139|lab1139_s163_w2_1005_1045_r2|S163] take_profit (+70.0%) SELL 1 TSLA260911C00395000 @<= 0.98
  EXIT [b1055|lab1055_s165_w2_1005_1045_r2|S165] stop_loss (-92.9%) SELL failed SHOP260911C00146000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b1054|lab1054_s165_w2_1005_1045_r1|S165] stop_loss (-92.9%) SELL failed SHOP260911C00146000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-09 09:34:46,740 INFO   EXIT [b296|lab0296_s353_w1_0928_1005_r1|S353] stop_loss (-70.9%) SELL 1 ZS260911C00180000 @<= 0.07
2026-09-09 09:34:47,071 INFO   EXIT [b298|lab0298_s353_w2_1005_1045_r1|S353] stop_loss (-97.5%) SELL 1 ZS260911C00177500 @<= 0.02
2026-09-09 09:34:47,239 INFO   EXIT [b362|lab0362_s361_w1_0928_1005_r1|S361] take_profit (+59.3%) SELL 1 MARA260911C00012000 @<= 0.44
2026-09-09 09:34:47,630 INFO   EXIT [b165|lab0165_s216_w1_0928_1005_r2|S216] stop_loss (-67.9%) SELL 1 AVGO260911C00400000 @<= 0.10
  EXIT [b333|lab0333_s357_w3_1045_1120_r2|S357] take_profit (+52.5%) SELL failed MARA260925C00012000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b332|lab0332_s357_w3_1045_1120_r1|S357] take_profit (+52.5%) SELL failed MARA260925C00012000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-09 09:34:49,643 INFO   EXIT [b794|lab0794_s399_w2_1005_1045_r1|S399] stop_loss (-66.7%) SELL 1 COIN260911C00215000 @<= 0.05
2026-09-09 09:34:50,249 INFO   EXIT [b323|lab0323_s356_w2_1005_1045_r2|S356] take_profit (+57.8%) SELL 1 MARA260918C00012000 @<= 0.68
2026-09-09 09:34:53,901 INFO   EXIT [b803|lab0803_s404_w2_1005_1045_r2|S404] stop_loss (-74.1%) SELL 1 ZS260911C00175000 @<= 0.16
2026-09-09 09:34:58,793 INFO   EXIT [b87|lab0087_s210_w4_1120_1135_r2|S210] stop_loss (-68.3%) SELL 1 SNOW260911C00365000 @<= 0.16
Protective stops: placed=2 upgraded=0 already=13 failed=8 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260909T133633Z

- UTC timestamp: `20260909T133633Z`
- GitHub run: [#9455](https://github.com/28twagg-ops/TradingBot/actions/runs/34357998330)
- Run id: `34357998330`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260909T133633Z_live_bot.log`, `logs/action_runs/20260909T133633Z_live_options.log`, `logs/action_runs/20260909T133633Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1095 | 50.5 | +20.0 | +45.6 | $+16,013 |
| TAINTED | 1796 | 33.6 | -38.3 | +12.8 | $-8,550 |
| KEEP-only | 621 | 64.1 | +51.6 | +72.6 | $+11,127 |
| KEEP-only recent | 413 | 61.5 | +53.8 | +85.9 | $+5,870 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-09T09:26:14.881436-04:00","date":"2026-09-09","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":1003831.57,"open_positions":29,"pending_orders":0,"open_lots":102,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9453","github_run_id":"34356931247","status":"ok","data_quality":{"clean":{"n":1095,"win":50.5,"med":20.0,"avg":45.57,"pnl":16012.59},"tainted":{"n":1796,"win":33.63,"med":-38.25,"avg":12.79,"pnl":-8549.84},"keep_only":{"n":621,"win":64.09,"med":51.61,"avg":72.64,"pnl":11127.45},"keep_only_recent":{"n":413,"win":61.5,"med":53.85,"avg":85.88,"pnl":5870.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:36:34  INFO      Mode: morning_prep
13:36:35  INFO        [prep_positions] 2/2 (2 valid)
13:36:35  INFO      Fetching tickers (universe=both)...
13:36:35  INFO        S&P 500: 503
13:36:35  INFO        MidCap 400: 400
13:36:35  INFO        Total: 903 tickers
13:36:36  INFO        [prep_universe] 40/901 (40 valid)
13:36:38  INFO        [prep_universe] 80/901 (80 valid)
13:36:39  INFO        [prep_universe] 120/901 (120 valid)
13:36:40  INFO        [prep_universe] 160/901 (160 valid)
13:36:41  INFO        [prep_universe] 200/901 (199 valid)
13:36:48  INFO        [prep_universe] 240/901 (238 valid)
13:37:02  INFO        [prep_universe] 280/901 (278 valid)
13:37:12  INFO        [prep_universe] 320/901 (318 valid)
13:37:25  INFO        [prep_universe] 360/901 (358 valid)
13:37:38  INFO        [prep_universe] 400/901 (397 valid)
13:37:48  INFO        [prep_universe] 440/901 (437 valid)
13:38:01  INFO        [prep_universe] 480/901 (477 valid)
13:38:15  INFO        [prep_universe] 520/901 (517 valid)
13:38:25  INFO        [prep_universe] 560/901 (557 valid)
13:38:38  INFO        [prep_universe] 600/901 (597 valid)
13:38:48  INFO        [prep_universe] 640/901 (637 valid)
13:39:01  INFO        [prep_universe] 680/901 (677 valid)
13:39:15  INFO        [prep_universe] 720/901 (717 valid)
13:39:25  INFO        [prep_universe] 760/901 (757 valid)
13:39:38  INFO        [prep_universe] 800/901 (797 valid)
13:39:48  INFO        [prep_universe] 840/901 (837 valid)
13:40:01  INFO        [prep_universe] 880/901 (877 valid)
13:40:08  INFO        [prep_universe] 901/901 (898 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $229.37|
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
|  Invested                                                        $68.60|
|  Open P&L                                                        $-0.38|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MGM      MomReversal     $33.99     $40.92   $40.33   -1.4%   $-0.50  |
|  MKSI     MomReversal     $34.60     $266.16  $267.02  +0.3%   $+0.11  |
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
|  Exit candidates                                                      1|
|  Signal candidates                                                   37|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-09T09:40:11.043825-04:00 share=25% ===
2026-09-09 09:40:11,043 INFO === options_live_micro LIVE 2026-09-09T09:40:11.043825-04:00 share=25% ===
Live account equity $229.27 cash $160.77 #225458845 options_level=3
2026-09-09 09:40:11,239 INFO Live account equity $229.27 cash $160.77 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-09 09:40:11,419 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-09 09:40:11,537 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=102 paper_keys=yes dry_run=False
  alpaca positions=27
  FLAG b437|S366|561eb755 missing from Alpaca
  FLAG b436|S366|2a2bf121 missing from Alpaca
  FLAG b237|S401|f05d12e3 missing from Alpaca
  FLAG b362|S361|b201cf8b missing from Alpaca
  FLAG b263|S403|7aaacc03 missing from Alpaca
  FLAG b262|S403|000e4fa3 missing from Alpaca
  FLAG b235|S401|aedd4437 missing from Alpaca
  FLAG b234|S401|bee86171 missing from Alpaca
  FLAG b0|ORPHAN|aec42dbd missing from Alpaca
  FLAG b795|S399|2592b200 missing from Alpaca
  FLAG b794|S399|cb18c1a5 missing from Alpaca
  FLAG b197|S218|0aae1fae missing from Alpaca
  FLAG b196|S218|8fc32f76 missing from Alpaca
  FLAG b269|S403|dd548bed missing from Alpaca
  FLAG b268|S403|ba6e2116 missing from Alpaca
  FLAG b241|S401|f12d3e43 missing from Alpaca
  FLAG b240|S401|9574402b missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$1,003,635.96
  buying_power=$3,928,847.84 cash=$1,037,057.96
  open option orders: 19
    MARA260911C00012000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    CRWD260911C00225000 OrderSide.SELL qty=7 status=OrderStatus.NEW limit=None
    SNOW260911C00365000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.16
    ZS260911C00177500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.02
    MARA260911C00012500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 26
    AVGO260909C00372500 qty=-1 mkt=$-30.00
    AVGO260909C00375000 qty=-1 mkt=$-14.00
    AVGO260909C00380000 qty=-1 mkt=$-4.00
    AVGO260911C00400000 qty=3 mkt=$33.00
    CRWD260911C00222500 qty=3 mkt=$249.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-09T09:40:15.018465-04:00 ===

[Run context]
Paper auth OK — equity $1003640.96, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-09 09:40:16,958 INFO   EXIT [b289|lab0289_s352_w1_0928_1005_r2|S352] stop_loss (-56.4%) SELL 1 ZS260911C00180000 @<= 0.12
  EXIT [b164|lab0164_s216_w1_0928_1005_r1|S216] stop_loss (-72.8%) SELL failed AVGO260911C00400000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b167|lab0167_s216_w2_1005_1045_r2|S216] stop_loss (-72.8%) SELL failed AVGO260911C00400000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b166|lab0166_s216_w2_1005_1045_r1|S216] stop_loss (-72.8%) SELL failed AVGO260911C00400000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b1055|lab1055_s165_w2_1005_1045_r2|S165] stop_loss (-98.2%) SELL failed SHOP260911C00146000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b1054|lab1054_s165_w2_1005_1045_r1|S165] stop_loss (-98.2%) SELL failed SHOP260911C00146000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-09 09:40:23,688 INFO   EXIT [b322|lab0322_s356_w2_1005_1045_r1|S356] take_profit (+51.1%) SELL 1 MARA260918C00012000 @<= 0.65
  EXIT [b330|lab0330_s357_w2_1005_1045_r1|S357] stop_loss (-84.4%) SELL failed PATH260925C00017000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=2 upgraded=0 already=13 failed=6 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260909T134216Z

- UTC timestamp: `20260909T134216Z`
- GitHub run: [#9456](https://github.com/28twagg-ops/TradingBot/actions/runs/34358535202)
- Run id: `34358535202`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260909T134216Z_live_bot.log`, `logs/action_runs/20260909T134216Z_live_options.log`, `logs/action_runs/20260909T134216Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1095 | 50.5 | +20.0 | +45.6 | $+16,013 |
| TAINTED | 1796 | 33.6 | -38.3 | +12.8 | $-8,550 |
| KEEP-only | 621 | 64.1 | +51.6 | +72.6 | $+11,127 |
| KEEP-only recent | 413 | 61.5 | +53.8 | +85.9 | $+5,870 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-09T09:26:14.881436-04:00","date":"2026-09-09","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":1003831.57,"open_positions":29,"pending_orders":0,"open_lots":102,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9453","github_run_id":"34356931247","status":"ok","data_quality":{"clean":{"n":1095,"win":50.5,"med":20.0,"avg":45.57,"pnl":16012.59},"tainted":{"n":1796,"win":33.63,"med":-38.25,"avg":12.79,"pnl":-8549.84},"keep_only":{"n":621,"win":64.09,"med":51.61,"avg":72.64,"pnl":11127.45},"keep_only_recent":{"n":413,"win":61.5,"med":53.85,"avg":85.88,"pnl":5870.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:42:17  INFO      Mode: morning_prep
13:42:19  INFO        [prep_positions] 2/2 (2 valid)
13:42:19  INFO        Universe cache hit: 903 tickers (tickers_2026-09-09.json)
13:42:20  INFO        [prep_universe] 40/901 (40 valid)
13:42:22  INFO        [prep_universe] 80/901 (80 valid)
13:42:23  INFO        [prep_universe] 120/901 (120 valid)
13:42:25  INFO        [prep_universe] 160/901 (160 valid)
13:42:26  INFO        [prep_universe] 200/901 (199 valid)
13:42:33  INFO        [prep_universe] 240/901 (238 valid)
13:42:44  INFO        [prep_universe] 280/901 (278 valid)
13:42:57  INFO        [prep_universe] 320/901 (318 valid)
13:43:08  INFO        [prep_universe] 360/901 (358 valid)
13:43:21  INFO        [prep_universe] 400/901 (397 valid)
13:43:31  INFO        [prep_universe] 440/901 (437 valid)
13:43:45  INFO        [prep_universe] 480/901 (477 valid)
13:43:58  INFO        [prep_universe] 520/901 (517 valid)
13:44:09  INFO        [prep_universe] 560/901 (557 valid)
13:44:22  INFO        [prep_universe] 600/901 (597 valid)
13:44:32  INFO        [prep_universe] 640/901 (637 valid)
13:44:45  INFO        [prep_universe] 680/901 (677 valid)
13:44:56  INFO        [prep_universe] 720/901 (717 valid)
13:45:09  INFO        [prep_universe] 760/901 (757 valid)
13:45:20  INFO        [prep_universe] 800/901 (797 valid)
13:45:33  INFO        [prep_universe] 840/901 (837 valid)
13:45:46  INFO        [prep_universe] 880/901 (877 valid)
13:45:50  INFO        [prep_universe] 901/901 (898 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:42 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $229.45|
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
|  Invested                                                        $68.68|
|  Open P&L                                                        $-0.30|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MGM      MomReversal     $34.06     $40.92   $40.41   -1.3%   $-0.43  |
|  MKSI     MomReversal     $34.63     $266.16  $267.20  +0.4%   $+0.14  |
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
|  Exit candidates                                                      1|
|  Signal candidates                                                   32|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-09T09:45:54.212342-04:00 share=25% ===
2026-09-09 09:45:54,212 INFO === options_live_micro LIVE 2026-09-09T09:45:54.212342-04:00 share=25% ===
Live account equity $229.27 cash $160.77 #225458845 options_level=3
2026-09-09 09:45:54,438 INFO Live account equity $229.27 cash $160.77 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-09 09:45:54,776 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-09 09:45:54,927 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=85 paper_keys=yes dry_run=False
  alpaca positions=26
  FLAG b362|S361|b201cf8b missing from Alpaca
  FLAG b298|S353|2a4a1284 missing from Alpaca
  FLAG b794|S399|cb18c1a5 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$1,003,784.38
  buying_power=$3,930,040.92 cash=$1,037,174.88
  open option orders: 19
    ZS260911C00175000 OrderSide.SELL qty=3 status=OrderStatus.NEW limit=None
    TSLA260911C00395000 OrderSide.SELL qty=5 status=OrderStatus.NEW limit=None
    MARA260911C00012000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    CRWD260911C00225000 OrderSide.SELL qty=7 status=OrderStatus.NEW limit=None
    MARA260911C00012500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 25
    AVGO260909C00372500 qty=-1 mkt=$-15.00
    AVGO260909C00375000 qty=-1 mkt=$-8.00
    AVGO260909C00380000 qty=-1 mkt=$-3.00
    AVGO260911C00400000 qty=3 mkt=$30.00
    CRWD260911C00222500 qty=3 mkt=$249.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-09T09:45:58.399017-04:00 ===

[Run context]
Paper auth OK — equity $1003773.88, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b164|lab0164_s216_w1_0928_1005_r1|S216] stop_loss (-75.3%) SELL failed AVGO260911C00400000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b167|lab0167_s216_w2_1005_1045_r2|S216] stop_loss (-75.3%) SELL failed AVGO260911C00400000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b166|lab0166_s216_w2_1005_1045_r1|S216] stop_loss (-75.3%) SELL failed AVGO260911C00400000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-09 09:46:04,982 INFO   EXIT [b288|lab0288_s352_w1_0928_1005_r1|S352] stop_loss (-56.4%) SELL 1 ZS260911C00180000 @<= 0.16
  EXIT [b330|lab0330_s357_w2_1005_1045_r1|S357] stop_loss (-75.6%) SELL failed PATH260925C00017000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-09 09:46:09,972 INFO   EXIT [b1138|lab1138_s163_w2_1005_1045_r1|S163] take_profit (+68.3%) SELL 1 TSLA260911C00395000 @<= 1.02
  EXIT [b1055|lab1055_s165_w2_1005_1045_r2|S165] stop_loss (-98.2%) SELL failed SHOP260911C00146000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b1054|lab1054_s165_w2_1005_1045_r1|S165] stop_loss (-98.2%) SELL failed SHOP260911C00146000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-09 09:46:12,623 INFO   EXIT [b863|lab0863_s408_w4_1120_1135_r2|S408] stop_loss (-61.5%) SELL 1 CRWD260911C00235000 @<= 0.11
Protective stops: placed=1 upgraded=0 already=13 failed=6 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260909T134745Z

- UTC timestamp: `20260909T134745Z`
- GitHub run: [#9457](https://github.com/28twagg-ops/TradingBot/actions/runs/34359082141)
- Run id: `34359082141`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260909T134745Z_live_bot.log`, `logs/action_runs/20260909T134745Z_live_options.log`, `logs/action_runs/20260909T134745Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1095 | 50.5 | +20.0 | +45.6 | $+16,013 |
| TAINTED | 1796 | 33.6 | -38.3 | +12.8 | $-8,550 |
| KEEP-only | 621 | 64.1 | +51.6 | +72.6 | $+11,127 |
| KEEP-only recent | 413 | 61.5 | +53.8 | +85.9 | $+5,870 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-09T09:26:14.881436-04:00","date":"2026-09-09","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":1003831.57,"open_positions":29,"pending_orders":0,"open_lots":102,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9453","github_run_id":"34356931247","status":"ok","data_quality":{"clean":{"n":1095,"win":50.5,"med":20.0,"avg":45.57,"pnl":16012.59},"tainted":{"n":1796,"win":33.63,"med":-38.25,"avg":12.79,"pnl":-8549.84},"keep_only":{"n":621,"win":64.09,"med":51.61,"avg":72.64,"pnl":11127.45},"keep_only_recent":{"n":413,"win":61.5,"med":53.85,"avg":85.88,"pnl":5870.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:47:46  INFO      Mode: morning_scan
13:47:46  INFO        [positions] 2/2 (2 valid)
13:47:46  INFO        SELL MARKET [urgent] MGM closed
13:47:49  INFO        TX logged: SELL MGM  P&L -1.21%
13:47:49  INFO        SELL MARKET [urgent] MKSI closed
13:47:51  INFO        TX logged: SELL MKSI  P&L -0.91%
13:47:51  INFO        Universe cache hit: 903 tickers (tickers_2026-09-09.json)
13:47:52  INFO        [universe] 40/903 (40 valid)
13:47:53  INFO        [universe] 80/903 (80 valid)
13:47:54  INFO        [universe] 120/903 (120 valid)
13:47:56  INFO        [universe] 160/903 (160 valid)
13:47:57  INFO        [universe] 200/903 (199 valid)
13:48:04  INFO        [universe] 240/903 (238 valid)
13:48:17  INFO        [universe] 280/903 (278 valid)
13:48:27  INFO        [universe] 320/903 (318 valid)
13:48:40  INFO        [universe] 360/903 (358 valid)
13:48:53  INFO        [universe] 400/903 (397 valid)
13:49:03  INFO        [universe] 440/903 (437 valid)
13:49:16  INFO        [universe] 480/903 (477 valid)
13:49:29  INFO        [universe] 520/903 (517 valid)
13:49:42  INFO        [universe] 560/903 (557 valid)
13:49:52  INFO        [universe] 600/903 (597 valid)
13:50:05  INFO        [universe] 640/903 (637 valid)
13:50:18  INFO        [universe] 680/903 (677 valid)
13:50:28  INFO        [universe] 720/903 (717 valid)
13:50:41  INFO        [universe] 760/903 (757 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260909T135201Z

- UTC timestamp: `20260909T135201Z`
- GitHub run: [#9458](https://github.com/28twagg-ops/TradingBot/actions/runs/34359627441)
- Run id: `34359627441`
- Live bot: exit=`0`, duration=`247s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260909T135201Z_live_bot.log`, `logs/action_runs/20260909T135201Z_live_options.log`, `logs/action_runs/20260909T135201Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1095 | 50.5 | +20.0 | +45.6 | $+16,013 |
| TAINTED | 1796 | 33.6 | -38.3 | +12.8 | $-8,550 |
| KEEP-only | 621 | 64.1 | +51.6 | +72.6 | $+11,127 |
| KEEP-only recent | 413 | 61.5 | +53.8 | +85.9 | $+5,870 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-09T09:26:14.881436-04:00","date":"2026-09-09","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":1003831.57,"open_positions":29,"pending_orders":0,"open_lots":102,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9453","github_run_id":"34356931247","status":"ok","data_quality":{"clean":{"n":1095,"win":50.5,"med":20.0,"avg":45.57,"pnl":16012.59},"tainted":{"n":1796,"win":33.63,"med":-38.25,"avg":12.79,"pnl":-8549.84},"keep_only":{"n":621,"win":64.09,"med":51.61,"avg":72.64,"pnl":11127.45},"keep_only_recent":{"n":413,"win":61.5,"med":53.85,"avg":85.88,"pnl":5870.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
... (132 earlier lines - see full log file)
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] AAPL  Pullback50                                   $34.34|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] BAX  Pullback50                                    $34.34|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] BRK-B  Pullback50                                  $34.34|
|    ENTER [eq] C  Pullback50                                      $34.34|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] COHR  Pullback50                                     cap 3|
|    SKIP [eq] EQIX  Pullback50                                     cap 3|13:56:07  INFO        place_all_stops: checking 3 positions...
13:56:07  INFO        STOP skipped AAPL: fractional (0.1085 shares) — software exit will handle it
13:56:07  INFO        STOP-MARKET placed BAX  qty=1 (pos=1.3828)  stop=$24.70  id=524059d2-0ef3-4e03-bd0d-ef5f74360a46
13:56:07  INFO        STOP skipped C: fractional (0.2519 shares) — software exit will handle it
13:56:08  INFO        Daily log -> logs/daily/2026-09-09.md
13:56:08  INFO        Dashboard written → logs/dashboard.md

|    SKIP [eq] F  Pullback50                                        cap 3|
|    SKIP [eq] GRMN  Pullback50                                     cap 3|
|    SKIP [eq] HAS  Pullback50                                      cap 3|
|    SKIP [eq] JPM  Pullback50                                      cap 3|
|    SKIP [eq] JBHT  Pullback50                                     cap 3|
|    SKIP [eq] MDLZ  Pullback50                                     cap 3|
|    SKIP [eq] STLD  Pullback50                                     cap 3|
|    SKIP [eq] SYY  Pullback50                                      cap 3|
|    SKIP [eq] TRV  Pullback50                                      cap 3|
|    SKIP [eq] VTRS  Pullback50                                     cap 3|
|    SKIP [eq] WAB  Pullback50                                      cap 3|
|    SKIP [eq] WELL  Pullback50                                     cap 3|
|    SKIP [eq] ZBH  Pullback50                                      cap 3|
|    SKIP [eq] ALV  Pullback50                                      cap 3|
|    SKIP [eq] ARMK  Pullback50                                     cap 3|
|    SKIP [eq] KEX  Pullback50                                      cap 3|
|    SKIP [eq] KRYS  Pullback50                                     cap 3|
|    SKIP [eq] LFUS  Pullback50                                     cap 3|
|    SKIP [eq] NLY  Pullback50                                      cap 3|
|    SKIP [eq] OGE  Pullback50                                      cap 3|
|    SKIP [eq] PK  Pullback50                                       cap 3|
|    SKIP [eq] SBRA  Pullback50                                     cap 3|
|    SKIP [eq] SLM  Pullback50                                      cap 3|
|    SKIP [eq] USFD  Pullback50                                     cap 3|
|    SKIP [eq] VIAV  Pullback50                                     cap 3|
|    SKIP [eq] WTS  Pullback50                                      cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      3|
+------------------------------------------------------------------------+
|  AAPL                                                 still unconfirmed|
|  BAX                                                  still unconfirmed|
|  C                                                    still unconfirmed|
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
|  Scanned                                                            900|
|  Signals                                                             32|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  3 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $228.92|
|  Cash                                                           $125.96|
+========================================================================+
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---
