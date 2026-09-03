# Daily Comprehensive Action Review - 2026-09-03

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260903T130103Z

- UTC timestamp: `20260903T130103Z`
- GitHub run: [#8920](https://github.com/28twagg-ops/TradingBot/actions/runs/33758493417)
- Run id: `33758493417`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260903T130103Z_live_bot.log`, `logs/action_runs/20260903T130103Z_live_options.log`, `logs/action_runs/20260903T130103Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 871 | 42.5 | -46.9 | +15.6 | $+8,494 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 355 | 62.0 | +37.7 | +41.1 | $+5,979 |
| KEEP-only recent | 167 | 57.5 | +50.0 | +46.5 | $+1,953 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (19): ORPHAN, S165, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-03T09:01:08.597095-04:00","date":"2026-09-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":999486.18,"open_positions":26,"pending_orders":0,"open_lots":118,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8920","github_run_id":"33758493417","status":"ok","data_quality":{"clean":{"n":871,"win":42.48,"med":-46.88,"avg":15.58,"pnl":8493.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":355,"win":61.97,"med":37.69,"avg":41.06,"pnl":5979.45},"keep_only_recent":{"n":167,"win":57.49,"med":50.0,"avg":46.53,"pnl":1953.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408","S411"]}}
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
|  Equity                                                         $230.37|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.37|
|  Cash                                                           $195.68|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $34.69|
|  Open P&L                                                        $+0.11|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $34.69     $255.49  $256.30  +0.3%   $+0.11  |
|                                                                        |
|  Total invested                                                  $34.69|
|  Total open P&L                                                  $+0.11|
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
|  2026-09-02  SELL  MO  Pullback50  $34.52  P&L $+0.00                  |
|  2026-09-02  SELL  AES  Pullback50  $34.50  P&L $-0.03                 |
|  2026-09-02  SELL  AES  Pullback50  $34.57  P&L $-0.01                 |
|  2026-09-02  SELL  AIZ  Pullback50  $34.26  P&L $-0.32                 |
|  2026-09-02  SELL  SYNA  MomReversal  $34.43  P&L $-0.27               |
|  2026-09-02  SELL  GME  EarningsDrift  $35.03  P&L $+0.35              |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-03T09:01:05.666150-04:00 share=25% ===
2026-09-03 09:01:05,666 INFO === options_live_micro LIVE 2026-09-03T09:01:05.666150-04:00 share=25% ===
Live account equity $230.37 cash $195.68 #225458845 options_level=3
2026-09-03 09:01:05,719 INFO Live account equity $230.37 cash $195.68 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-03 09:01:05,726 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-03 09:01:05,736 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (153 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    4 |   10 |    2 |    5 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    40 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 245 | 10 |
| S165 | 1691 | 23 |
| S166 | 109 | 6 |
| S167 | 245 | 10 |
| S168 | 170 | 8 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-03
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   981 | WARN | <<<
| Missing exit records (post) |   981 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |   118 | INFO |
| Total closed lots           |  1823 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-03_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-03_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=871 med=-46.9% | TAINTED n=1766 med=-39.2% | KEEP-only n=355 med=+37.7% | KILL=19 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.37 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260903T130600Z

- UTC timestamp: `20260903T130600Z`
- GitHub run: [#8921](https://github.com/28twagg-ops/TradingBot/actions/runs/33758999109)
- Run id: `33758999109`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260903T130600Z_live_bot.log`, `logs/action_runs/20260903T130600Z_live_options.log`, `logs/action_runs/20260903T130600Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 871 | 42.5 | -46.9 | +15.6 | $+8,494 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 355 | 62.0 | +37.7 | +41.1 | $+5,979 |
| KEEP-only recent | 167 | 57.5 | +50.0 | +46.5 | $+1,953 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (19): ORPHAN, S165, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-03T09:06:06.263970-04:00","date":"2026-09-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.19},"signals":0,"placed":0,"equity":999486.18,"open_positions":26,"pending_orders":0,"open_lots":118,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8921","github_run_id":"33758999109","status":"ok","data_quality":{"clean":{"n":871,"win":42.48,"med":-46.88,"avg":15.58,"pnl":8493.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":355,"win":61.97,"med":37.69,"avg":41.06,"pnl":5979.45},"keep_only_recent":{"n":167,"win":57.49,"med":50.0,"avg":46.53,"pnl":1953.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:06:02  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.39|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.39|
|  Cash                                                           $195.68|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $34.71|
|  Open P&L                                                        $+0.13|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $34.71     $255.49  $256.46  +0.4%   $+0.13  |
|                                                                        |
|  Total invested                                                  $34.71|
|  Total open P&L                                                  $+0.13|
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
|  2026-09-02  SELL  MO  Pullback50  $34.52  P&L $+0.00                  |
|  2026-09-02  SELL  AES  Pullback50  $34.50  P&L $-0.03                 |
|  2026-09-02  SELL  AES  Pullback50  $34.57  P&L $-0.01                 |
|  2026-09-02  SELL  AIZ  Pullback50  $34.26  P&L $-0.32                 |
|  2026-09-02  SELL  SYNA  MomReversal  $34.43  P&L $-0.27               |
|  2026-09-02  SELL  GME  EarningsDrift  $35.03  P&L $+0.35              |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-03T09:06:03.380917-04:00 share=25% ===
2026-09-03 09:06:03,380 INFO === options_live_micro LIVE 2026-09-03T09:06:03.380917-04:00 share=25% ===
Live account equity $230.39 cash $195.68 #225458845 options_level=3
2026-09-03 09:06:03,466 INFO Live account equity $230.39 cash $195.68 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-03 09:06:03,488 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-03 09:06:03,509 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (153 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    4 |   10 |    2 |    5 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    40 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 245 | 10 |
| S165 | 1691 | 23 |
| S166 | 109 | 6 |
| S167 | 245 | 10 |
| S168 | 170 | 8 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-03
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   981 | WARN | <<<
| Missing exit records (post) |   981 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |   118 | INFO |
| Total closed lots           |  1823 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-03_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-03_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=871 med=-46.9% | TAINTED n=1766 med=-39.2% | KEEP-only n=355 med=+37.7% | KILL=19 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.39 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260903T131103Z

- UTC timestamp: `20260903T131103Z`
- GitHub run: [#8922](https://github.com/28twagg-ops/TradingBot/actions/runs/33759503789)
- Run id: `33759503789`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260903T131103Z_live_bot.log`, `logs/action_runs/20260903T131103Z_live_options.log`, `logs/action_runs/20260903T131103Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 871 | 42.5 | -46.9 | +15.6 | $+8,494 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 355 | 62.0 | +37.7 | +41.1 | $+5,979 |
| KEEP-only recent | 167 | 57.5 | +50.0 | +46.5 | $+1,953 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (19): ORPHAN, S165, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-03T09:11:08.898724-04:00","date":"2026-09-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.2},"signals":0,"placed":0,"equity":999486.18,"open_positions":26,"pending_orders":0,"open_lots":118,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8922","github_run_id":"33759503789","status":"ok","data_quality":{"clean":{"n":871,"win":42.48,"med":-46.88,"avg":15.58,"pnl":8493.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":355,"win":61.97,"med":37.69,"avg":41.06,"pnl":5979.45},"keep_only_recent":{"n":167,"win":57.49,"med":50.0,"avg":46.53,"pnl":1953.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:11:04  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.34|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.34|
|  Cash                                                           $195.68|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $34.66|
|  Open P&L                                                        $+0.08|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $34.66     $255.49  $256.08  +0.2%   $+0.08  |
|                                                                        |
|  Total invested                                                  $34.66|
|  Total open P&L                                                  $+0.08|
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
|  2026-09-02  SELL  MO  Pullback50  $34.52  P&L $+0.00                  |
|  2026-09-02  SELL  AES  Pullback50  $34.50  P&L $-0.03                 |
|  2026-09-02  SELL  AES  Pullback50  $34.57  P&L $-0.01                 |
|  2026-09-02  SELL  AIZ  Pullback50  $34.26  P&L $-0.32                 |
|  2026-09-02  SELL  SYNA  MomReversal  $34.43  P&L $-0.27               |
|  2026-09-02  SELL  GME  EarningsDrift  $35.03  P&L $+0.35              |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-03T09:11:05.918315-04:00 share=25% ===
2026-09-03 09:11:05,918 INFO === options_live_micro LIVE 2026-09-03T09:11:05.918315-04:00 share=25% ===
Live account equity $230.34 cash $195.68 #225458845 options_level=3
2026-09-03 09:11:06,029 INFO Live account equity $230.34 cash $195.68 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-03 09:11:06,057 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-03 09:11:06,088 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (153 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    4 |   10 |    2 |    5 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    40 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 245 | 10 |
| S165 | 1691 | 23 |
| S166 | 109 | 6 |
| S167 | 245 | 10 |
| S168 | 170 | 8 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-03
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   981 | WARN | <<<
| Missing exit records (post) |   981 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |   118 | INFO |
| Total closed lots           |  1823 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-03_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-03_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=871 med=-46.9% | TAINTED n=1766 med=-39.2% | KEEP-only n=355 med=+37.7% | KILL=19 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.34 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260903T131601Z

- UTC timestamp: `20260903T131601Z`
- GitHub run: [#8923](https://github.com/28twagg-ops/TradingBot/actions/runs/33760013702)
- Run id: `33760013702`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260903T131601Z_live_bot.log`, `logs/action_runs/20260903T131601Z_live_options.log`, `logs/action_runs/20260903T131601Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 871 | 42.5 | -46.9 | +15.6 | $+8,494 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 355 | 62.0 | +37.7 | +41.1 | $+5,979 |
| KEEP-only recent | 167 | 57.5 | +50.0 | +46.5 | $+1,953 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (19): ORPHAN, S165, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-03T09:16:07.099540-04:00","date":"2026-09-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.46},"signals":0,"placed":0,"equity":999486.18,"open_positions":26,"pending_orders":0,"open_lots":118,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8923","github_run_id":"33760013702","status":"ok","data_quality":{"clean":{"n":871,"win":42.48,"med":-46.88,"avg":15.58,"pnl":8493.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":355,"win":61.97,"med":37.69,"avg":41.06,"pnl":5979.45},"keep_only_recent":{"n":167,"win":57.49,"med":50.0,"avg":46.53,"pnl":1953.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408","S411"]}}
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
|  Equity                                                         $230.35|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.35|
|  Cash                                                           $195.68|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $34.67|
|  Open P&L                                                        $+0.09|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $34.67     $255.49  $256.13  +0.3%   $+0.09  |
|                                                                        |
|  Total invested                                                  $34.67|
|  Total open P&L                                                  $+0.09|
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
|  2026-09-02  SELL  MO  Pullback50  $34.52  P&L $+0.00                  |
|  2026-09-02  SELL  AES  Pullback50  $34.50  P&L $-0.03                 |
|  2026-09-02  SELL  AES  Pullback50  $34.57  P&L $-0.01                 |
|  2026-09-02  SELL  AIZ  Pullback50  $34.26  P&L $-0.32                 |
|  2026-09-02  SELL  SYNA  MomReversal  $34.43  P&L $-0.27               |
|  2026-09-02  SELL  GME  EarningsDrift  $35.03  P&L $+0.35              |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-03T09:16:03.811317-04:00 share=25% ===
2026-09-03 09:16:03,811 INFO === options_live_micro LIVE 2026-09-03T09:16:03.811317-04:00 share=25% ===
Live account equity $230.35 cash $195.68 #225458845 options_level=3
2026-09-03 09:16:04,013 INFO Live account equity $230.35 cash $195.68 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-03 09:16:04,071 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-03 09:16:04,131 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (153 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    4 |   10 |    2 |    5 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    40 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 245 | 10 |
| S165 | 1691 | 23 |
| S166 | 109 | 6 |
| S167 | 245 | 10 |
| S168 | 170 | 8 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-03
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   981 | WARN | <<<
| Missing exit records (post) |   981 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |   118 | INFO |
| Total closed lots           |  1823 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-03_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-03_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=871 med=-46.9% | TAINTED n=1766 med=-39.2% | KEEP-only n=355 med=+37.7% | KILL=19 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.35 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260903T132058Z

- UTC timestamp: `20260903T132058Z`
- GitHub run: [#8924](https://github.com/28twagg-ops/TradingBot/actions/runs/33760529038)
- Run id: `33760529038`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260903T132058Z_live_bot.log`, `logs/action_runs/20260903T132058Z_live_options.log`, `logs/action_runs/20260903T132058Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 871 | 42.5 | -46.9 | +15.6 | $+8,494 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 355 | 62.0 | +37.7 | +41.1 | $+5,979 |
| KEEP-only recent | 167 | 57.5 | +50.0 | +46.5 | $+1,953 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (19): ORPHAN, S165, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-03T09:21:02.955530-04:00","date":"2026-09-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.21},"signals":0,"placed":0,"equity":999486.18,"open_positions":26,"pending_orders":0,"open_lots":118,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8924","github_run_id":"33760529038","status":"ok","data_quality":{"clean":{"n":871,"win":42.48,"med":-46.88,"avg":15.58,"pnl":8493.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":355,"win":61.97,"med":37.69,"avg":41.06,"pnl":5979.45},"keep_only_recent":{"n":167,"win":57.49,"med":50.0,"avg":46.53,"pnl":1953.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:20:59  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.33|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.33|
|  Cash                                                           $195.68|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $34.65|
|  Open P&L                                                        $+0.07|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $34.65     $255.49  $255.99  +0.2%   $+0.07  |
|                                                                        |
|  Total invested                                                  $34.65|
|  Total open P&L                                                  $+0.07|
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
|  2026-09-02  SELL  MO  Pullback50  $34.52  P&L $+0.00                  |
|  2026-09-02  SELL  AES  Pullback50  $34.50  P&L $-0.03                 |
|  2026-09-02  SELL  AES  Pullback50  $34.57  P&L $-0.01                 |
|  2026-09-02  SELL  AIZ  Pullback50  $34.26  P&L $-0.32                 |
|  2026-09-02  SELL  SYNA  MomReversal  $34.43  P&L $-0.27               |
|  2026-09-02  SELL  GME  EarningsDrift  $35.03  P&L $+0.35              |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-03T09:21:00.229051-04:00 share=25% ===
2026-09-03 09:21:00,229 INFO === options_live_micro LIVE 2026-09-03T09:21:00.229051-04:00 share=25% ===
Live account equity $230.33 cash $195.68 #225458845 options_level=3
2026-09-03 09:21:00,271 INFO Live account equity $230.33 cash $195.68 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-03 09:21:00,279 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-03 09:21:00,286 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (153 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    4 |   10 |    2 |    5 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    40 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 245 | 10 |
| S165 | 1691 | 23 |
| S166 | 109 | 6 |
| S167 | 245 | 10 |
| S168 | 170 | 8 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-03
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   981 | WARN | <<<
| Missing exit records (post) |   981 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |   118 | INFO |
| Total closed lots           |  1823 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-03_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-03_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=871 med=-46.9% | TAINTED n=1766 med=-39.2% | KEEP-only n=355 med=+37.7% | KILL=19 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.33 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260903T132605Z

- UTC timestamp: `20260903T132605Z`
- GitHub run: [#8925](https://github.com/28twagg-ops/TradingBot/actions/runs/33761029854)
- Run id: `33761029854`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260903T132605Z_live_bot.log`, `logs/action_runs/20260903T132605Z_live_options.log`, `logs/action_runs/20260903T132605Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 871 | 42.5 | -46.9 | +15.6 | $+8,494 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 355 | 62.0 | +37.7 | +41.1 | $+5,979 |
| KEEP-only recent | 167 | 57.5 | +50.0 | +46.5 | $+1,953 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (19): ORPHAN, S165, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-03T09:26:11.896061-04:00","date":"2026-09-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.48},"signals":0,"placed":0,"equity":999486.18,"open_positions":26,"pending_orders":0,"open_lots":118,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8925","github_run_id":"33761029854","status":"ok","data_quality":{"clean":{"n":871,"win":42.48,"med":-46.88,"avg":15.58,"pnl":8493.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":355,"win":61.97,"med":37.69,"avg":41.06,"pnl":5979.45},"keep_only_recent":{"n":167,"win":57.49,"med":50.0,"avg":46.53,"pnl":1953.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:26:06  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.35|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.35|
|  Cash                                                           $195.68|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $34.67|
|  Open P&L                                                        $+0.09|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $34.67     $255.49  $256.18  +0.3%   $+0.09  |
|                                                                        |
|  Total invested                                                  $34.67|
|  Total open P&L                                                  $+0.09|
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
|  2026-09-02  SELL  MO  Pullback50  $34.52  P&L $+0.00                  |
|  2026-09-02  SELL  AES  Pullback50  $34.50  P&L $-0.03                 |
|  2026-09-02  SELL  AES  Pullback50  $34.57  P&L $-0.01                 |
|  2026-09-02  SELL  AIZ  Pullback50  $34.26  P&L $-0.32                 |
|  2026-09-02  SELL  SYNA  MomReversal  $34.43  P&L $-0.27               |
|  2026-09-02  SELL  GME  EarningsDrift  $35.03  P&L $+0.35              |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-03T09:26:08.354830-04:00 share=25% ===
2026-09-03 09:26:08,354 INFO === options_live_micro LIVE 2026-09-03T09:26:08.354830-04:00 share=25% ===
Live account equity $230.35 cash $195.68 #225458845 options_level=3
2026-09-03 09:26:08,579 INFO Live account equity $230.35 cash $195.68 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-03 09:26:08,649 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-03 09:26:08,717 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (153 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    4 |   10 |    2 |    5 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    40 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 245 | 10 |
| S165 | 1691 | 23 |
| S166 | 109 | 6 |
| S167 | 245 | 10 |
| S168 | 170 | 8 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-03
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   981 | WARN | <<<
| Missing exit records (post) |   981 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |   118 | INFO |
| Total closed lots           |  1823 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-03_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-03_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=871 med=-46.9% | TAINTED n=1766 med=-39.2% | KEEP-only n=355 med=+37.7% | KILL=19 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.35 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260903T133103Z

- UTC timestamp: `20260903T133103Z`
- GitHub run: [#8926](https://github.com/28twagg-ops/TradingBot/actions/runs/33761491253)
- Run id: `33761491253`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260903T133103Z_live_bot.log`, `logs/action_runs/20260903T133103Z_live_options.log`, `logs/action_runs/20260903T133103Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 871 | 42.5 | -46.9 | +15.6 | $+8,494 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 355 | 62.0 | +37.7 | +41.1 | $+5,979 |
| KEEP-only recent | 167 | 57.5 | +50.0 | +46.5 | $+1,953 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (19): ORPHAN, S165, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-03T09:26:11.896061-04:00","date":"2026-09-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.48},"signals":0,"placed":0,"equity":999486.18,"open_positions":26,"pending_orders":0,"open_lots":118,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8925","github_run_id":"33761029854","status":"ok","data_quality":{"clean":{"n":871,"win":42.48,"med":-46.88,"avg":15.58,"pnl":8493.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":355,"win":61.97,"med":37.69,"avg":41.06,"pnl":5979.45},"keep_only_recent":{"n":167,"win":57.49,"med":50.0,"avg":46.53,"pnl":1953.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:31:04  INFO      Mode: morning_prep
13:31:06  INFO        [prep_positions] 3/3 (3 valid)
13:31:06  INFO      Fetching tickers (universe=both)...
13:31:06  INFO        S&P 500: 503
13:31:07  INFO        MidCap 400: 400
13:31:07  INFO        Total: 903 tickers
13:31:08  INFO        [prep_universe] 40/900 (40 valid)
13:31:10  INFO        [prep_universe] 80/900 (80 valid)
13:31:12  INFO        [prep_universe] 120/900 (120 valid)
13:31:14  INFO        [prep_universe] 160/900 (160 valid)
13:31:17  INFO        [prep_universe] 200/900 (199 valid)
13:31:21  INFO        [prep_universe] 240/900 (238 valid)
13:31:32  INFO        [prep_universe] 280/900 (278 valid)
13:31:45  INFO        [prep_universe] 320/900 (318 valid)
13:31:56  INFO        [prep_universe] 360/900 (358 valid)
13:32:09  INFO        [prep_universe] 400/900 (397 valid)
13:32:20  INFO        [prep_universe] 440/900 (437 valid)
13:32:33  INFO        [prep_universe] 480/900 (477 valid)
13:32:44  INFO        [prep_universe] 520/900 (517 valid)
13:32:58  INFO        [prep_universe] 560/900 (557 valid)
13:33:08  INFO        [prep_universe] 600/900 (597 valid)
13:33:22  INFO        [prep_universe] 640/900 (637 valid)
13:33:32  INFO        [prep_universe] 680/900 (677 valid)
13:33:43  INFO        [prep_universe] 720/900 (717 valid)
13:33:56  INFO        [prep_universe] 760/900 (757 valid)
13:34:10  INFO        [prep_universe] 800/900 (797 valid)
13:34:20  INFO        [prep_universe] 840/900 (837 valid)
13:34:34  INFO        [prep_universe] 880/900 (877 valid)
13:34:38  INFO        [prep_universe] 900/900 (897 valid)

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
|  Invested                                                       $103.89|
|  Open P&L                                                        $+0.29|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $34.51     $14.82   $14.82   +0.0%   $+0.00  |
|  AMZN     Pullback50      $34.71     $255.49  $256.46  +0.4%   $+0.13  |
|  CNM      MomReversal     $34.67     $44.25   $44.45   +0.5%   $+0.16  |
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
|  Signal candidates                                                   29|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-03T09:34:41.305670-04:00 share=25% ===
2026-09-03 09:34:41,305 INFO === options_live_micro LIVE 2026-09-03T09:34:41.305670-04:00 share=25% ===
Live account equity $230.84 cash $126.65 #225458845 options_level=3
2026-09-03 09:34:41,615 INFO Live account equity $230.84 cash $126.65 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-03 09:34:41,834 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-03 09:34:41,986 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=118 paper_keys=yes dry_run=False
  alpaca positions=25
  FLAG b241|S401|2ed268db missing from Alpaca
  FLAG b240|S401|588fbdd9 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$1,000,629.13
  buying_power=$3,981,756.52 cash=$995,589.13
  open option orders: 19
    MARA260904C00011000 OrderSide.SELL qty=29 status=OrderStatus.NEW limit=None
    UPST260904C00029000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    AFRM260904C00078000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    MARA260925C00011000 OrderSide.SELL qty=8 status=OrderStatus.NEW limit=None
    MARA260911C00010500 OrderSide.SELL qty=19 status=OrderStatus.NEW limit=None
  open option positions: 25
    AFRM260904C00078000 qty=2 mkt=$14.00
    AMD260904C00502500 qty=1 mkt=$4.00
    BA260904C00215000 qty=1 mkt=$30.00
    BA260904C00217500 qty=-1 mkt=$-20.00
    GOOGL260904C00347500 qty=5 mkt=$550.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-03T09:34:45.508490-04:00 ===

[Run context]
Paper auth OK — equity $1000625.13, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-03 09:34:47,959 INFO   EXIT [b913|lab0913_s412_w1_0928_1005_r2|S412] take_profit (+81.8%) SELL 1 MARA260904C00010500 @<= 0.31
2026-09-03 09:34:49,179 INFO   EXIT [b239|lab0239_s401_w3_1045_1120_r2|S401] take_profit (+471.4%) SELL 1 NVDA260904C00227500 @<= 1.96
2026-09-03 09:34:49,701 INFO   EXIT [b199|lab0199_s218_w4_1120_1135_r2|S218] stop_loss (-72.0%) SELL 1 AFRM260904C00078000 @<= 0.04
2026-09-03 09:34:50,717 INFO   EXIT [b798|lab0798_s399_w4_1120_1135_r1|S399] stop_loss (-88.6%) SELL 1 AMD260904C00502500 @<= 0.01
  EXIT [b901|lab0901_s411_w2_1005_1045_r2|S411] take_profit (+274.4%) SELL failed RBLX260904C00042000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b900|lab0900_s411_w2_1005_1045_r1|S411] take_profit (+274.4%) SELL failed RBLX260904C00042000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-03 09:34:51,933 INFO   EXIT [b407|lab0407_s364_w2_1005_1045_r2|S364] take_profit (+57.9%) SELL 1 MARA260911C00010500 @<= 0.54
2026-09-03 09:34:52,908 INFO   EXIT [b425|lab0425_s365_w4_1120_1135_r2|S365] take_profit (+62.3%) SELL 1 MSFT260918C00545000 @<= 1.13
2026-09-03 09:34:53,274 INFO   EXIT [b362|lab0362_s361_w1_0928_1005_r1|S361] take_profit (+85.7%) SELL 1 MARA260904C00011000 @<= 0.10
2026-09-03 09:34:55,746 INFO   EXIT [b194|lab0194_s218_w2_1005_1045_r1|S218] take_profit (+119.1%) SELL 1 GOOGL260904C00347500 @<= 1.11
Protective stops: placed=0 upgraded=0 already=13 failed=9 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260903T133634Z

- UTC timestamp: `20260903T133634Z`
- GitHub run: [#8927](https://github.com/28twagg-ops/TradingBot/actions/runs/33761942278)
- Run id: `33761942278`
- Live bot: exit=`0`, duration=`218s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260903T133634Z_live_bot.log`, `logs/action_runs/20260903T133634Z_live_options.log`, `logs/action_runs/20260903T133634Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 871 | 42.5 | -46.9 | +15.6 | $+8,494 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 355 | 62.0 | +37.7 | +41.1 | $+5,979 |
| KEEP-only recent | 167 | 57.5 | +50.0 | +46.5 | $+1,953 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (19): ORPHAN, S165, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-03T09:26:11.896061-04:00","date":"2026-09-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.48},"signals":0,"placed":0,"equity":999486.18,"open_positions":26,"pending_orders":0,"open_lots":118,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8925","github_run_id":"33761029854","status":"ok","data_quality":{"clean":{"n":871,"win":42.48,"med":-46.88,"avg":15.58,"pnl":8493.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":355,"win":61.97,"med":37.69,"avg":41.06,"pnl":5979.45},"keep_only_recent":{"n":167,"win":57.49,"med":50.0,"avg":46.53,"pnl":1953.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:36:35  INFO      Mode: morning_prep
13:36:36  INFO        [prep_positions] 3/3 (3 valid)
13:36:36  INFO      Fetching tickers (universe=both)...
13:36:36  INFO        S&P 500: 503
13:36:37  INFO        MidCap 400: 400
13:36:37  INFO        Total: 903 tickers
13:36:38  INFO        [prep_universe] 40/900 (40 valid)
13:36:39  INFO        [prep_universe] 80/900 (80 valid)
13:36:40  INFO        [prep_universe] 120/900 (120 valid)
13:36:42  INFO        [prep_universe] 160/900 (160 valid)
13:36:43  INFO        [prep_universe] 200/900 (199 valid)
13:36:50  INFO        [prep_universe] 240/900 (238 valid)
13:37:04  INFO        [prep_universe] 280/900 (278 valid)
13:37:14  INFO        [prep_universe] 320/900 (318 valid)
13:37:27  INFO        [prep_universe] 360/900 (358 valid)
13:37:37  INFO        [prep_universe] 400/900 (397 valid)
13:37:51  INFO        [prep_universe] 440/900 (437 valid)
13:38:04  INFO        [prep_universe] 480/900 (477 valid)
13:38:14  INFO        [prep_universe] 520/900 (517 valid)
13:38:27  INFO        [prep_universe] 560/900 (557 valid)
13:38:38  INFO        [prep_universe] 600/900 (597 valid)
13:38:51  INFO        [prep_universe] 640/900 (637 valid)
13:39:01  INFO        [prep_universe] 680/900 (677 valid)
13:39:15  INFO        [prep_universe] 720/900 (717 valid)
13:39:26  INFO        [prep_universe] 760/900 (757 valid)
13:39:39  INFO        [prep_universe] 800/900 (797 valid)
13:39:49  INFO        [prep_universe] 840/900 (837 valid)
13:40:02  INFO        [prep_universe] 880/900 (877 valid)
13:40:09  INFO        [prep_universe] 900/900 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $231.02|
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
|  Invested                                                       $104.37|
|  Open P&L                                                        $+0.77|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $34.56     $14.82   $14.84   +0.1%   $+0.05  |
|  AMZN     Pullback50      $34.99     $255.49  $258.50  +1.2%   $+0.41  |
|  CNM      MomReversal     $34.82     $44.25   $44.65   +0.9%   $+0.31  |
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
|  Signal candidates                                                   34|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-03T09:40:12.658441-04:00 share=25% ===
2026-09-03 09:40:12,658 INFO === options_live_micro LIVE 2026-09-03T09:40:12.658441-04:00 share=25% ===
Live account equity $230.67 cash $126.65 #225458845 options_level=3
2026-09-03 09:40:12,865 INFO Live account equity $230.67 cash $126.65 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-03 09:40:13,099 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-03 09:40:13,223 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=118 paper_keys=yes dry_run=False
  alpaca positions=24
  FLAG b798|S399|c9912ae4 missing from Alpaca
  FLAG b241|S401|2ed268db missing from Alpaca
  FLAG b240|S401|588fbdd9 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$1,000,826.97
  buying_power=$3,983,899.88 cash=$996,124.97
  open option orders: 13
    UPST260904C00029000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    MARA260925C00011000 OrderSide.SELL qty=8 status=OrderStatus.NEW limit=None
    MARA260904C00011500 OrderSide.SELL qty=3 status=OrderStatus.NEW limit=None
    IWM260904C00297000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    NVDA260904C00235000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 24
    AFRM260904C00078000 qty=1 mkt=$7.00
    BA260904C00215000 qty=1 mkt=$25.00
    BA260904C00217500 qty=-1 mkt=$-21.00
    GOOGL260904C00347500 qty=4 mkt=$576.00
    IWM260904C00297000 qty=2 mkt=$96.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-03T09:40:16.115508-04:00 ===

[Run context]
Paper auth OK — equity $1000824.97, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-03 09:40:17,874 INFO   EXIT [b912|lab0912_s412_w1_0928_1005_r1|S412] take_profit (+92.5%) SELL 1 MARA260904C00010500 @<= 0.33
  EXIT [b182|lab0182_s217_w3_1045_1120_r1|S217] stop_loss (-56.1%) SELL failed BA260904C00215000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-03 09:40:18,837 INFO   EXIT [b345|lab0345_s359_w1_0928_1005_r2|S359] take_profit (+100.0%) SELL 1 MARA260904C00011000 @<= 0.15
2026-09-03 09:40:19,732 INFO   EXIT [b195|lab0195_s218_w2_1005_1045_r2|S218] take_profit (+186.9%) SELL 1 GOOGL260904C00347500 @<= 1.45
2026-09-03 09:40:20,344 INFO   EXIT [b198|lab0198_s218_w4_1120_1135_r1|S218] stop_loss (-72.0%) SELL 1 AFRM260904C00078000 @<= 0.08
2026-09-03 09:40:21,394 INFO   EXIT [b424|lab0424_s365_w4_1120_1135_r1|S365] take_profit (+111.6%) SELL 1 MSFT260918C00545000 @<= 1.43
  EXIT [b901|lab0901_s411_w2_1005_1045_r2|S411] take_profit (+179.5%) SELL failed RBLX260904C00042000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b900|lab0900_s411_w2_1005_1045_r1|S411] take_profit (+179.5%) SELL failed RBLX260904C00042000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-03 09:40:22,602 INFO   EXIT [b406|lab0406_s364_w2_1005_1045_r1|S364] take_profit (+55.1%) SELL 1 MARA260911C00010500 @<= 0.53
  EXIT [b238|lab0238_s401_w3_1045_1120_r1|S401] take_profit (+491.4%) SELL failed NVDA260904C00227500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 upgraded=0 already=14 failed=7 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260903T134212Z

- UTC timestamp: `20260903T134212Z`
- GitHub run: [#8928](https://github.com/28twagg-ops/TradingBot/actions/runs/33762412020)
- Run id: `33762412020`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260903T134212Z_live_bot.log`, `logs/action_runs/20260903T134212Z_live_options.log`, `logs/action_runs/20260903T134212Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 871 | 42.5 | -46.9 | +15.6 | $+8,494 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 355 | 62.0 | +37.7 | +41.1 | $+5,979 |
| KEEP-only recent | 167 | 57.5 | +50.0 | +46.5 | $+1,953 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (19): ORPHAN, S165, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-03T09:26:11.896061-04:00","date":"2026-09-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.48},"signals":0,"placed":0,"equity":999486.18,"open_positions":26,"pending_orders":0,"open_lots":118,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8925","github_run_id":"33761029854","status":"ok","data_quality":{"clean":{"n":871,"win":42.48,"med":-46.88,"avg":15.58,"pnl":8493.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":355,"win":61.97,"med":37.69,"avg":41.06,"pnl":5979.45},"keep_only_recent":{"n":167,"win":57.49,"med":50.0,"avg":46.53,"pnl":1953.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:42:13  INFO      Mode: morning_prep
13:42:15  INFO        [prep_positions] 3/3 (3 valid)
13:42:15  INFO        Universe cache hit: 903 tickers (tickers_2026-09-03.json)
13:42:16  INFO        [prep_universe] 40/900 (40 valid)
13:42:17  INFO        [prep_universe] 80/900 (80 valid)
13:42:18  INFO        [prep_universe] 120/900 (120 valid)
13:42:20  INFO        [prep_universe] 160/900 (160 valid)
13:42:21  INFO        [prep_universe] 200/900 (199 valid)
13:42:28  INFO        [prep_universe] 240/900 (238 valid)
13:42:42  INFO        [prep_universe] 280/900 (278 valid)
13:42:52  INFO        [prep_universe] 320/900 (318 valid)
13:43:05  INFO        [prep_universe] 360/900 (358 valid)
13:43:16  INFO        [prep_universe] 400/900 (397 valid)
13:43:29  INFO        [prep_universe] 440/900 (437 valid)
13:43:43  INFO        [prep_universe] 480/900 (477 valid)
13:43:53  INFO        [prep_universe] 520/900 (517 valid)
13:44:06  INFO        [prep_universe] 560/900 (557 valid)
13:44:17  INFO        [prep_universe] 600/900 (597 valid)
13:44:30  INFO        [prep_universe] 640/900 (637 valid)
13:44:41  INFO        [prep_universe] 680/900 (677 valid)
13:44:55  INFO        [prep_universe] 720/900 (717 valid)
13:45:05  INFO        [prep_universe] 760/900 (757 valid)
13:45:18  INFO        [prep_universe] 800/900 (797 valid)
13:45:28  INFO        [prep_universe] 840/900 (837 valid)
13:45:42  INFO        [prep_universe] 880/900 (877 valid)
13:45:46  INFO        [prep_universe] 900/900 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:42 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.72|
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
|  Invested                                                       $104.06|
|  Open P&L                                                        $+0.46|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $34.52     $14.82   $14.82   +0.0%   $+0.01  |
|  AMZN     Pullback50      $34.98     $255.49  $258.42  +1.1%   $+0.40  |
|  CNM      MomReversal     $34.56     $44.25   $44.32   +0.2%   $+0.05  |
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
|  Signal candidates                                                   26|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-03T09:45:49.725200-04:00 share=25% ===
2026-09-03 09:45:49,725 INFO === options_live_micro LIVE 2026-09-03T09:45:49.725200-04:00 share=25% ===
Live account equity $230.78 cash $126.65 #225458845 options_level=3
2026-09-03 09:45:49,956 INFO Live account equity $230.78 cash $126.65 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-03 09:45:50,185 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-03 09:45:50,323 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=116 paper_keys=yes dry_run=False
  alpaca positions=22
  FLAG b425|S365|65934967 missing from Alpaca
  FLAG b424|S365|6293c02e missing from Alpaca
  FLAG b798|S399|c9912ae4 missing from Alpaca
  FLAG b199|S218|8539e1f8 missing from Alpaca
  FLAG b198|S218|a29f0405 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$1,001,185.85
  buying_power=$3,985,531.40 cash=$996,532.85
  open option orders: 13
    UPST260904C00029000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    MARA260925C00011000 OrderSide.SELL qty=8 status=OrderStatus.NEW limit=None
    MARA260904C00011500 OrderSide.SELL qty=3 status=OrderStatus.NEW limit=None
    IWM260904C00297000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    NVDA260904C00235000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 22
    BA260904C00215000 qty=1 mkt=$19.00
    BA260904C00217500 qty=-1 mkt=$-10.00
    GOOGL260904C00347500 qty=3 mkt=$345.00
    IWM260904C00297000 qty=2 mkt=$102.00
    MARA260904C00009500 qty=4 mkt=$428.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-03T09:45:54.224665-04:00 ===

[Run context]
Paper auth OK — equity $1001185.85, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-03 09:45:56,338 INFO   EXIT [b835|lab0835_s406_w4_1120_1135_r2|S406] take_profit (+66.7%) SELL 1 MARA260904C00011500 @<= 0.06
  EXIT [b901|lab0901_s411_w2_1005_1045_r2|S411] take_profit (+230.8%) SELL failed RBLX260904C00042000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b900|lab0900_s411_w2_1005_1045_r1|S411] take_profit (+230.8%) SELL failed RBLX260904C00042000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-03 09:45:58,271 INFO   EXIT [b193|lab0193_s218_w1_0928_1005_r2|S218] take_profit (+129.1%) SELL 1 GOOGL260904C00347500 @<= 1.18
2026-09-03 09:45:59,271 INFO   EXIT [b344|lab0344_s359_w1_0928_1005_r1|S359] take_profit (+142.9%) SELL 1 MARA260904C00011000 @<= 0.18
2026-09-03 09:45:59,579 INFO   EXIT [b409|lab0409_s364_w3_1045_1120_r2|S364] take_profit (+71.7%) SELL 1 MARA260911C00010500 @<= 0.60
  EXIT [b182|lab0182_s217_w3_1045_1120_r1|S217] stop_loss (-66.7%) SELL failed BA260904C00215000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-03 09:46:00,473 INFO   EXIT [b419|lab0419_s365_w1_0928_1005_r2|S365] take_profit (+57.4%) SELL 1 MARA260918C00010500 @<= 0.86
2026-09-03 09:46:00,975 INFO   EXIT [b915|lab0915_s412_w2_1005_1045_r2|S412] take_profit (+119.3%) SELL 1 MARA260904C00010500 @<= 0.43
  EXIT [b238|lab0238_s401_w3_1045_1120_r1|S401] take_profit (+551.4%) SELL failed NVDA260904C00227500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 upgraded=0 already=14 failed=5 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260903T134740Z

- UTC timestamp: `20260903T134740Z`
- GitHub run: [#8929](https://github.com/28twagg-ops/TradingBot/actions/runs/33762875175)
- Run id: `33762875175`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260903T134740Z_live_bot.log`, `logs/action_runs/20260903T134740Z_live_options.log`, `logs/action_runs/20260903T134740Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 871 | 42.5 | -46.9 | +15.6 | $+8,494 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 355 | 62.0 | +37.7 | +41.1 | $+5,979 |
| KEEP-only recent | 167 | 57.5 | +50.0 | +46.5 | $+1,953 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (19): ORPHAN, S165, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-03T09:26:11.896061-04:00","date":"2026-09-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.48},"signals":0,"placed":0,"equity":999486.18,"open_positions":26,"pending_orders":0,"open_lots":118,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8925","github_run_id":"33761029854","status":"ok","data_quality":{"clean":{"n":871,"win":42.48,"med":-46.88,"avg":15.58,"pnl":8493.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":355,"win":61.97,"med":37.69,"avg":41.06,"pnl":5979.45},"keep_only_recent":{"n":167,"win":57.49,"med":50.0,"avg":46.53,"pnl":1953.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:47:41  INFO      Mode: morning_scan
13:47:41  INFO        [positions] 3/3 (3 valid)
13:47:41  INFO        SELL LIMIT AES  qty=2.328609986  limit=$14.81  id=57398f4e-72e6-4bda-a87a-71cb6ab6b56a
13:48:11  INFO        SELL LIMIT filled AES (confirmed by position check)
13:48:11  INFO        TX logged: SELL AES  P&L 0.0%
13:48:11  INFO        Universe cache hit: 903 tickers (tickers_2026-09-03.json)
13:48:12  INFO        [universe] 40/901 (40 valid)
13:48:13  INFO        [universe] 80/901 (80 valid)
13:48:14  INFO        [universe] 120/901 (120 valid)
13:48:15  INFO        [universe] 160/901 (160 valid)
13:48:16  INFO        [universe] 200/901 (199 valid)
13:48:26  INFO        [universe] 240/901 (238 valid)
13:48:36  INFO        [universe] 280/901 (278 valid)
13:48:49  INFO        [universe] 320/901 (318 valid)
13:49:02  INFO        [universe] 360/901 (358 valid)
13:49:15  INFO        [universe] 400/901 (397 valid)
13:49:24  INFO        [universe] 440/901 (437 valid)
13:49:37  INFO        [universe] 480/901 (477 valid)
13:49:50  INFO        [universe] 520/901 (517 valid)
13:50:00  INFO        [universe] 560/901 (557 valid)
13:50:13  INFO        [universe] 600/901 (597 valid)
13:50:26  INFO        [universe] 640/901 (637 valid)
13:50:38  INFO        [universe] 680/901 (677 valid)
13:50:48  INFO        [universe] 720/901 (717 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---
