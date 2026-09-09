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
