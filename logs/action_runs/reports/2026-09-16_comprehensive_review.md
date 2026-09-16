# Daily Comprehensive Action Review - 2026-09-16

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260916T130110Z

- UTC timestamp: `20260916T130110Z`
- GitHub run: [#10107](https://github.com/28twagg-ops/TradingBot/actions/runs/35099146155)
- Run id: `35099146155`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20260916T130110Z_live_bot.log`, `logs/action_runs/20260916T130110Z_live_options.log`, `logs/action_runs/20260916T130110Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1235 | 49.0 | -16.0 | +39.7 | $+15,916 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 643 | 62.7 | +51.0 | +62.5 | $+10,833 |
| KEEP-only recent | 446 | 60.5 | +53.3 | +71.6 | $+6,188 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-16T09:01:16.410055-04:00","date":"2026-09-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.52},"signals":0,"placed":0,"equity":1000216.66,"open_positions":22,"pending_orders":0,"open_lots":145,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10107","github_run_id":"35099146155","status":"ok","data_quality":{"clean":{"n":1235,"win":48.99,"med":-16.0,"avg":39.72,"pnl":15915.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":643,"win":62.67,"med":50.98,"avg":62.47,"pnl":10833.45},"keep_only_recent":{"n":446,"win":60.54,"med":53.33,"avg":71.62,"pnl":6188.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:01:11  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.38|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.38|
|  Cash                                                           $157.09|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $68.29|
|  Open P&L                                                        $+0.27|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAL      MomReversal     $34.18     $12.91   $12.94   +0.2%   $+0.08  |
|  ALLE     Pullback50      $34.11     $153.74  $154.60  +0.6%   $+0.19  |
|                                                                        |
|  Total invested                                                  $68.29|
|  Total open P&L                                                  $+0.27|
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
|  2026-09-15  SELL  MO  Pullback50  $33.72  P&L $+0.01                  |
|  2026-09-15  SELL  APO  Pullback50  $33.58  P&L $-0.20                 |
|  2026-09-15  SELL  AMZN  Pullback50  $33.54  P&L $-0.24                |
|  2026-09-15  SELL  AAL  MomReversal  $33.74  P&L $-0.18                |
|  2026-09-15  SELL  ROL  MomReversal  $33.38  P&L $-0.54                |
|  2026-09-14  SELL  AES  Pullback50  $33.91  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-16T09:01:13.415129-04:00 share=25% ===
2026-09-16 09:01:13,415 INFO === options_live_micro LIVE 2026-09-16T09:01:13.415129-04:00 share=25% ===
Live account equity $225.38 cash $157.09 #225458845 options_level=3
2026-09-16 09:01:13,617 INFO Live account equity $225.38 cash $157.09 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-16 09:01:13,722 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-16 09:01:13,779 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (168 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 263 | 15 |
| S164 | 295 | 20 |
| S165 | 1731 | 32 |
| S166 | 135 | 9 |
| S167 | 289 | 19 |
| S168 | 214 | 16 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-16
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    34 | WARN | <<<
| Orphaned lots (post-stable) |  1397 | WARN | <<<
| Missing exit records (post) |  1363 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   145 | INFO |
| Total closed lots           |  2231 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-16_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-16_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1235 med=-16.0% | TAINTED n=1844 med=-38.8% | KEEP-only n=643 med=+51.0% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.38 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260916T130609Z

- UTC timestamp: `20260916T130609Z`
- GitHub run: [#10108](https://github.com/28twagg-ops/TradingBot/actions/runs/35099661387)
- Run id: `35099661387`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260916T130609Z_live_bot.log`, `logs/action_runs/20260916T130609Z_live_options.log`, `logs/action_runs/20260916T130609Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1235 | 49.0 | -16.0 | +39.7 | $+15,916 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 643 | 62.7 | +51.0 | +62.5 | $+10,833 |
| KEEP-only recent | 446 | 60.5 | +53.3 | +71.6 | $+6,188 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-16T09:06:15.786980-04:00","date":"2026-09-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.47},"signals":0,"placed":0,"equity":1000269.66,"open_positions":22,"pending_orders":0,"open_lots":145,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10108","github_run_id":"35099661387","status":"ok","data_quality":{"clean":{"n":1235,"win":48.99,"med":-16.0,"avg":39.72,"pnl":15915.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":643,"win":62.67,"med":50.98,"avg":62.47,"pnl":10833.45},"keep_only_recent":{"n":446,"win":60.54,"med":53.33,"avg":71.62,"pnl":6188.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:06:10  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.27|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.27|
|  Cash                                                           $157.09|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $68.18|
|  Open P&L                                                        $+0.16|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAL      MomReversal     $34.07     $12.91   $12.90   -0.1%   $-0.03  |
|  ALLE     Pullback50      $34.11     $153.74  $154.60  +0.6%   $+0.19  |
|                                                                        |
|  Total invested                                                  $68.18|
|  Total open P&L                                                  $+0.16|
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
|  2026-09-15  SELL  MO  Pullback50  $33.72  P&L $+0.01                  |
|  2026-09-15  SELL  APO  Pullback50  $33.58  P&L $-0.20                 |
|  2026-09-15  SELL  AMZN  Pullback50  $33.54  P&L $-0.24                |
|  2026-09-15  SELL  AAL  MomReversal  $33.74  P&L $-0.18                |
|  2026-09-15  SELL  ROL  MomReversal  $33.38  P&L $-0.54                |
|  2026-09-14  SELL  AES  Pullback50  $33.91  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-16T09:06:12.408362-04:00 share=25% ===
2026-09-16 09:06:12,408 INFO === options_live_micro LIVE 2026-09-16T09:06:12.408362-04:00 share=25% ===
Live account equity $225.27 cash $157.09 #225458845 options_level=3
2026-09-16 09:06:12,643 INFO Live account equity $225.27 cash $157.09 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-16 09:06:12,717 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-16 09:06:12,797 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (168 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 263 | 15 |
| S164 | 295 | 20 |
| S165 | 1731 | 32 |
| S166 | 135 | 9 |
| S167 | 289 | 19 |
| S168 | 214 | 16 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-16
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    34 | WARN | <<<
| Orphaned lots (post-stable) |  1397 | WARN | <<<
| Missing exit records (post) |  1363 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   145 | INFO |
| Total closed lots           |  2231 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-16_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-16_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1235 med=-16.0% | TAINTED n=1844 med=-38.8% | KEEP-only n=643 med=+51.0% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.27 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260916T131110Z

- UTC timestamp: `20260916T131110Z`
- GitHub run: [#10109](https://github.com/28twagg-ops/TradingBot/actions/runs/35100179239)
- Run id: `35100179239`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260916T131110Z_live_bot.log`, `logs/action_runs/20260916T131110Z_live_options.log`, `logs/action_runs/20260916T131110Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1235 | 49.0 | -16.0 | +39.7 | $+15,916 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 643 | 62.7 | +51.0 | +62.5 | $+10,833 |
| KEEP-only recent | 446 | 60.5 | +53.3 | +71.6 | $+6,188 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-16T09:11:15.659370-04:00","date":"2026-09-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":1000265.66,"open_positions":22,"pending_orders":0,"open_lots":145,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10109","github_run_id":"35100179239","status":"ok","data_quality":{"clean":{"n":1235,"win":48.99,"med":-16.0,"avg":39.72,"pnl":15915.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":643,"win":62.67,"med":50.98,"avg":62.47,"pnl":10833.45},"keep_only_recent":{"n":446,"win":60.54,"med":53.33,"avg":71.62,"pnl":6188.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:11:11  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.32|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.32|
|  Cash                                                           $157.09|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $68.23|
|  Open P&L                                                        $+0.21|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAL      MomReversal     $34.12     $12.91   $12.92   +0.1%   $+0.02  |
|  ALLE     Pullback50      $34.11     $153.74  $154.60  +0.6%   $+0.19  |
|                                                                        |
|  Total invested                                                  $68.23|
|  Total open P&L                                                  $+0.21|
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
|  2026-09-15  SELL  MO  Pullback50  $33.72  P&L $+0.01                  |
|  2026-09-15  SELL  APO  Pullback50  $33.58  P&L $-0.20                 |
|  2026-09-15  SELL  AMZN  Pullback50  $33.54  P&L $-0.24                |
|  2026-09-15  SELL  AAL  MomReversal  $33.74  P&L $-0.18                |
|  2026-09-15  SELL  ROL  MomReversal  $33.38  P&L $-0.54                |
|  2026-09-14  SELL  AES  Pullback50  $33.91  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-16T09:11:12.853800-04:00 share=25% ===
2026-09-16 09:11:12,853 INFO === options_live_micro LIVE 2026-09-16T09:11:12.853800-04:00 share=25% ===
Live account equity $225.32 cash $157.09 #225458845 options_level=3
2026-09-16 09:11:12,895 INFO Live account equity $225.32 cash $157.09 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-16 09:11:12,905 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-16 09:11:12,912 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (168 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 263 | 15 |
| S164 | 295 | 20 |
| S165 | 1731 | 32 |
| S166 | 135 | 9 |
| S167 | 289 | 19 |
| S168 | 214 | 16 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-16
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    34 | WARN | <<<
| Orphaned lots (post-stable) |  1397 | WARN | <<<
| Missing exit records (post) |  1363 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   145 | INFO |
| Total closed lots           |  2231 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-16_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-16_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1235 med=-16.0% | TAINTED n=1844 med=-38.8% | KEEP-only n=643 med=+51.0% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.32 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260916T131609Z

- UTC timestamp: `20260916T131609Z`
- GitHub run: [#10110](https://github.com/28twagg-ops/TradingBot/actions/runs/35100706630)
- Run id: `35100706630`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260916T131609Z_live_bot.log`, `logs/action_runs/20260916T131609Z_live_options.log`, `logs/action_runs/20260916T131609Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1235 | 49.0 | -16.0 | +39.7 | $+15,916 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 643 | 62.7 | +51.0 | +62.5 | $+10,833 |
| KEEP-only recent | 446 | 60.5 | +53.3 | +71.6 | $+6,188 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-16T09:16:16.247987-04:00","date":"2026-09-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.48},"signals":0,"placed":0,"equity":1000222.77,"open_positions":22,"pending_orders":0,"open_lots":145,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10110","github_run_id":"35100706630","status":"ok","data_quality":{"clean":{"n":1235,"win":48.99,"med":-16.0,"avg":39.72,"pnl":15915.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":643,"win":62.67,"med":50.98,"avg":62.47,"pnl":10833.45},"keep_only_recent":{"n":446,"win":60.54,"med":53.33,"avg":71.62,"pnl":6188.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:16:10  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.46|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.46|
|  Cash                                                           $157.09|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $68.37|
|  Open P&L                                                        $+0.34|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAL      MomReversal     $34.26     $12.91   $12.97   +0.5%   $+0.16  |
|  ALLE     Pullback50      $34.11     $153.74  $154.60  +0.6%   $+0.19  |
|                                                                        |
|  Total invested                                                  $68.37|
|  Total open P&L                                                  $+0.34|
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
|  2026-09-15  SELL  MO  Pullback50  $33.72  P&L $+0.01                  |
|  2026-09-15  SELL  APO  Pullback50  $33.58  P&L $-0.20                 |
|  2026-09-15  SELL  AMZN  Pullback50  $33.54  P&L $-0.24                |
|  2026-09-15  SELL  AAL  MomReversal  $33.74  P&L $-0.18                |
|  2026-09-15  SELL  ROL  MomReversal  $33.38  P&L $-0.54                |
|  2026-09-14  SELL  AES  Pullback50  $33.91  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-16T09:16:12.868937-04:00 share=25% ===
2026-09-16 09:16:12,869 INFO === options_live_micro LIVE 2026-09-16T09:16:12.868937-04:00 share=25% ===
Live account equity $225.46 cash $157.09 #225458845 options_level=3
2026-09-16 09:16:13,073 INFO Live account equity $225.46 cash $157.09 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-16 09:16:13,225 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-16 09:16:13,285 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (168 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 263 | 15 |
| S164 | 295 | 20 |
| S165 | 1731 | 32 |
| S166 | 135 | 9 |
| S167 | 289 | 19 |
| S168 | 214 | 16 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-16
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    34 | WARN | <<<
| Orphaned lots (post-stable) |  1397 | WARN | <<<
| Missing exit records (post) |  1363 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   145 | INFO |
| Total closed lots           |  2231 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-16_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-16_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1235 med=-16.0% | TAINTED n=1844 med=-38.8% | KEEP-only n=643 med=+51.0% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.46 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260916T132114Z

- UTC timestamp: `20260916T132114Z`
- GitHub run: [#10111](https://github.com/28twagg-ops/TradingBot/actions/runs/35101233206)
- Run id: `35101233206`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20260916T132114Z_live_bot.log`, `logs/action_runs/20260916T132114Z_live_options.log`, `logs/action_runs/20260916T132114Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1235 | 49.0 | -16.0 | +39.7 | $+15,916 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 643 | 62.7 | +51.0 | +62.5 | $+10,833 |
| KEEP-only recent | 446 | 60.5 | +53.3 | +71.6 | $+6,188 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-16T09:21:20.812516-04:00","date":"2026-09-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.36},"signals":0,"placed":0,"equity":1000187.01,"open_positions":22,"pending_orders":0,"open_lots":145,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10111","github_run_id":"35101233206","status":"ok","data_quality":{"clean":{"n":1235,"win":48.99,"med":-16.0,"avg":39.72,"pnl":15915.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":643,"win":62.67,"med":50.98,"avg":62.47,"pnl":10833.45},"keep_only_recent":{"n":446,"win":60.54,"med":53.33,"avg":71.62,"pnl":6188.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
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
|  Equity                                                         $225.38|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.38|
|  Cash                                                           $157.09|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $68.29|
|  Open P&L                                                        $+0.27|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAL      MomReversal     $34.18     $12.91   $12.94   +0.2%   $+0.08  |
|  ALLE     Pullback50      $34.11     $153.74  $154.60  +0.6%   $+0.19  |
|                                                                        |
|  Total invested                                                  $68.29|
|  Total open P&L                                                  $+0.27|
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
|  2026-09-15  SELL  MO  Pullback50  $33.72  P&L $+0.01                  |
|  2026-09-15  SELL  APO  Pullback50  $33.58  P&L $-0.20                 |
|  2026-09-15  SELL  AMZN  Pullback50  $33.54  P&L $-0.24                |
|  2026-09-15  SELL  AAL  MomReversal  $33.74  P&L $-0.18                |
|  2026-09-15  SELL  ROL  MomReversal  $33.38  P&L $-0.54                |
|  2026-09-14  SELL  AES  Pullback50  $33.91  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-16T09:21:17.413809-04:00 share=25% ===
2026-09-16 09:21:17,413 INFO === options_live_micro LIVE 2026-09-16T09:21:17.413809-04:00 share=25% ===
Live account equity $225.38 cash $157.09 #225458845 options_level=3
2026-09-16 09:21:17,584 INFO Live account equity $225.38 cash $157.09 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-16 09:21:17,642 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-16 09:21:17,691 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (168 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 263 | 15 |
| S164 | 295 | 20 |
| S165 | 1731 | 32 |
| S166 | 135 | 9 |
| S167 | 289 | 19 |
| S168 | 214 | 16 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-16
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    34 | WARN | <<<
| Orphaned lots (post-stable) |  1397 | WARN | <<<
| Missing exit records (post) |  1363 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   145 | INFO |
| Total closed lots           |  2231 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-16_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-16_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1235 med=-16.0% | TAINTED n=1844 med=-38.8% | KEEP-only n=643 med=+51.0% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.38 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260916T132617Z

- UTC timestamp: `20260916T132617Z`
- GitHub run: [#10112](https://github.com/28twagg-ops/TradingBot/actions/runs/35101767909)
- Run id: `35101767909`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260916T132617Z_live_bot.log`, `logs/action_runs/20260916T132617Z_live_options.log`, `logs/action_runs/20260916T132617Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1235 | 49.0 | -16.0 | +39.7 | $+15,916 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 643 | 62.7 | +51.0 | +62.5 | $+10,833 |
| KEEP-only recent | 446 | 60.5 | +53.3 | +71.6 | $+6,188 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-16T09:26:25.093222-04:00","date":"2026-09-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":1000187.66,"open_positions":22,"pending_orders":0,"open_lots":145,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10112","github_run_id":"35101767909","status":"ok","data_quality":{"clean":{"n":1235,"win":48.99,"med":-16.0,"avg":39.72,"pnl":15915.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":643,"win":62.67,"med":50.98,"avg":62.47,"pnl":10833.45},"keep_only_recent":{"n":446,"win":60.54,"med":53.33,"avg":71.62,"pnl":6188.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:26:18  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.46|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.46|
|  Cash                                                           $157.09|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $68.37|
|  Open P&L                                                        $+0.34|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAL      MomReversal     $34.26     $12.91   $12.97   +0.5%   $+0.16  |
|  ALLE     Pullback50      $34.11     $153.74  $154.60  +0.6%   $+0.19  |
|                                                                        |
|  Total invested                                                  $68.37|
|  Total open P&L                                                  $+0.34|
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
|  2026-09-15  SELL  MO  Pullback50  $33.72  P&L $+0.01                  |
|  2026-09-15  SELL  APO  Pullback50  $33.58  P&L $-0.20                 |
|  2026-09-15  SELL  AMZN  Pullback50  $33.54  P&L $-0.24                |
|  2026-09-15  SELL  AAL  MomReversal  $33.74  P&L $-0.18                |
|  2026-09-15  SELL  ROL  MomReversal  $33.38  P&L $-0.54                |
|  2026-09-14  SELL  AES  Pullback50  $33.91  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-16T09:26:21.468779-04:00 share=25% ===
2026-09-16 09:26:21,468 INFO === options_live_micro LIVE 2026-09-16T09:26:21.468779-04:00 share=25% ===
Live account equity $225.46 cash $157.09 #225458845 options_level=3
2026-09-16 09:26:21,720 INFO Live account equity $225.46 cash $157.09 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-16 09:26:21,811 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-16 09:26:21,889 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (168 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 263 | 15 |
| S164 | 295 | 20 |
| S165 | 1731 | 32 |
| S166 | 135 | 9 |
| S167 | 289 | 19 |
| S168 | 214 | 16 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-16
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    34 | WARN | <<<
| Orphaned lots (post-stable) |  1397 | WARN | <<<
| Missing exit records (post) |  1363 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   145 | INFO |
| Total closed lots           |  2231 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-16_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-16_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1235 med=-16.0% | TAINTED n=1844 med=-38.8% | KEEP-only n=643 med=+51.0% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.46 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260916T133110Z

- UTC timestamp: `20260916T133110Z`
- GitHub run: [#10113](https://github.com/28twagg-ops/TradingBot/actions/runs/35102306634)
- Run id: `35102306634`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260916T133110Z_live_bot.log`, `logs/action_runs/20260916T133110Z_live_options.log`, `logs/action_runs/20260916T133110Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1235 | 49.0 | -16.0 | +39.7 | $+15,916 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 643 | 62.7 | +51.0 | +62.5 | $+10,833 |
| KEEP-only recent | 446 | 60.5 | +53.3 | +71.6 | $+6,188 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-16T09:26:25.093222-04:00","date":"2026-09-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":1000187.66,"open_positions":22,"pending_orders":0,"open_lots":145,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10112","github_run_id":"35101767909","status":"ok","data_quality":{"clean":{"n":1235,"win":48.99,"med":-16.0,"avg":39.72,"pnl":15915.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":643,"win":62.67,"med":50.98,"avg":62.47,"pnl":10833.45},"keep_only_recent":{"n":446,"win":60.54,"med":53.33,"avg":71.62,"pnl":6188.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:31:12  INFO      Mode: morning_prep
13:31:13  INFO        [prep_positions] 2/2 (2 valid)
13:31:13  INFO      Fetching tickers (universe=both)...
13:31:13  INFO        S&P 500: 503
13:31:13  INFO        MidCap 400: 400
13:31:13  INFO        Total: 903 tickers
13:31:14  INFO        [prep_universe] 40/901 (40 valid)
13:31:16  INFO        [prep_universe] 80/901 (80 valid)
13:31:17  INFO        [prep_universe] 120/901 (120 valid)
13:31:18  INFO        [prep_universe] 160/901 (160 valid)
13:31:19  INFO        [prep_universe] 200/901 (199 valid)
13:31:27  INFO        [prep_universe] 240/901 (238 valid)
13:31:39  INFO        [prep_universe] 280/901 (278 valid)
13:31:52  INFO        [prep_universe] 320/901 (318 valid)
13:32:02  INFO        [prep_universe] 360/901 (358 valid)
13:32:16  INFO        [prep_universe] 400/901 (398 valid)
13:32:28  INFO        [prep_universe] 440/901 (438 valid)
13:32:38  INFO        [prep_universe] 480/901 (478 valid)
13:32:51  INFO        [prep_universe] 520/901 (518 valid)
13:33:04  INFO        [prep_universe] 560/901 (558 valid)
13:33:14  INFO        [prep_universe] 600/901 (598 valid)
13:33:27  INFO        [prep_universe] 640/901 (638 valid)
13:33:40  INFO        [prep_universe] 680/901 (678 valid)
13:33:50  INFO        [prep_universe] 720/901 (718 valid)
13:34:03  INFO        [prep_universe] 760/901 (758 valid)
13:34:16  INFO        [prep_universe] 800/901 (798 valid)
13:34:29  INFO        [prep_universe] 840/901 (838 valid)
13:34:39  INFO        [prep_universe] 880/901 (878 valid)
13:34:45  INFO        [prep_universe] 901/901 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.45|
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
|  Invested                                                        $68.36|
|  Open P&L                                                        $+0.34|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAL      MomReversal     $34.14     $12.91   $12.93   +0.1%   $+0.04  |
|  ALLE     Pullback50      $34.22     $153.74  $155.11  +0.9%   $+0.30  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  AAL       OrderType.STOP    2         None        12.7                |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      0|
|  Signal candidates                                                   22|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-16T09:34:48.278147-04:00 share=25% ===
2026-09-16 09:34:48,278 INFO === options_live_micro LIVE 2026-09-16T09:34:48.278147-04:00 share=25% ===
Live account equity $225.13 cash $157.09 #225458845 options_level=3
2026-09-16 09:34:48,334 INFO Live account equity $225.13 cash $157.09 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-16 09:34:48,369 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-16 09:34:48,408 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=145 paper_keys=yes dry_run=False
  alpaca positions=21
  FLAG b298|S353|e719fbe8 missing from Alpaca
  FLAG b291|S352|f55a8789 missing from Alpaca
  FLAG b290|S352|ecf95e3d missing from Alpaca
  FLAG b283|S351|5e578bef missing from Alpaca
  FLAG b282|S351|903af79d missing from Alpaca
  FLAG b279|S350|9a0492cc missing from Alpaca
  FLAG b278|S350|8a8f0492 missing from Alpaca
  FLAG b1139|S163|57e57104 missing from Alpaca
  FLAG b1138|S163|55f134ef missing from Alpaca
  FLAG b1097|S167|8553d8d6 missing from Alpaca
  FLAG b1096|S167|3a014094 missing from Alpaca
  FLAG b1125|S168|dea8dffc missing from Alpaca
  FLAG b1124|S168|bab83b1b missing from Alpaca
  FLAG b1153|S164|71fb46ef missing from Alpaca
  FLAG b1152|S164|4339f817 missing from Alpaca
  FLAG b1055|S165|b7d19491 missing from Alpaca
  FLAG b1054|S165|e288f8da missing from Alpaca
  FLAG b887|S410|8c6de481 missing from Alpaca
  FLAG b886|S410|a7ad4146 missing from Alpaca
  FLAG b771|S396|785cfd7f missing from Alpaca
  FLAG b770|S396|1557502f missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$1,000,014.09
  buying_power=$3,945,736.36 cash=$1,031,525.09
  open option orders: 17
    SNOW260918C00347500 OrderSide.SELL qty=3 status=OrderStatus.NEW limit=None
    META260918C00725000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    META260918C00720000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    META260918C00727500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    PATH260918C00016000 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
  open option positions: 20
    MARA260918C00011500 qty=9 mkt=$270.00
    MARA260918C00012000 qty=78 mkt=$1,170.00
    MARA260918C00012500 qty=4 mkt=$32.00
    MARA260925C00011500 qty=-1 mkt=$-58.00
    MARA260925C00012500 qty=3 mkt=$75.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-16T09:34:51.787620-04:00 ===

[Run context]
Paper auth OK — equity $1000009.09, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-16 09:34:55,280 INFO   EXIT [b238|lab0238_s401_w3_1045_1120_r1|S401] take_profit (+74.5%) SELL 1 META260918C00720000 @<= 0.93
2026-09-16 09:34:55,693 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-76.5%) SELL 1 PATH260918C00014500 @<= 0.05
2026-09-16 09:34:56,214 INFO   EXIT [b234|lab0234_s401_w1_0928_1005_r1|S401] stop_loss (-77.9%) SELL 1 MSFT260918C00517500 @<= 0.12
2026-09-16 09:34:56,565 INFO   EXIT [b421|lab0421_s365_w2_1005_1045_r2|S365] stop_loss (-68.2%) SELL 1 PATH261002C00015000 @<= 0.18
2026-09-16 09:34:56,807 INFO   EXIT [b916|lab0916_s412_w3_1045_1120_r1|S412] stop_loss (-66.7%) SELL 1 PATH260918C00016000 @<= 0.02
2026-09-16 09:34:57,222 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-47.1%) SELL 1 MSTR260918C00157500 @<= 0.10
2026-09-16 09:34:57,371 INFO   EXIT [b312|lab0312_s355_w1_0928_1005_r1|S355] stop_loss (-50.1%) SELL 1 MARA260918C00012000 @<= 0.12
2026-09-16 09:34:57,572 INFO   EXIT [b407|lab0407_s364_w2_1005_1045_r2|S364] stop_loss (-100.0%) SELL 1 PATH260925C00015500 @<= 0.01
Protective stops: placed=1 upgraded=0 already=13 failed=4 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260916T133653Z

- UTC timestamp: `20260916T133653Z`
- GitHub run: [#10114](https://github.com/28twagg-ops/TradingBot/actions/runs/35102849351)
- Run id: `35102849351`
- Live bot: exit=`0`, duration=`216s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260916T133653Z_live_bot.log`, `logs/action_runs/20260916T133653Z_live_options.log`, `logs/action_runs/20260916T133653Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1235 | 49.0 | -16.0 | +39.7 | $+15,916 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 643 | 62.7 | +51.0 | +62.5 | $+10,833 |
| KEEP-only recent | 446 | 60.5 | +53.3 | +71.6 | $+6,188 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-16T09:26:25.093222-04:00","date":"2026-09-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":1000187.66,"open_positions":22,"pending_orders":0,"open_lots":145,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10112","github_run_id":"35101767909","status":"ok","data_quality":{"clean":{"n":1235,"win":48.99,"med":-16.0,"avg":39.72,"pnl":15915.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":643,"win":62.67,"med":50.98,"avg":62.47,"pnl":10833.45},"keep_only_recent":{"n":446,"win":60.54,"med":53.33,"avg":71.62,"pnl":6188.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:36:54  INFO      Mode: morning_prep
13:36:55  INFO        [prep_positions] 2/2 (2 valid)
13:36:55  INFO      Fetching tickers (universe=both)...
13:36:55  INFO        S&P 500: 503
13:36:55  INFO        MidCap 400: 400
13:36:55  INFO        Total: 903 tickers
13:36:57  INFO        [prep_universe] 40/901 (40 valid)
13:36:58  INFO        [prep_universe] 80/901 (80 valid)
13:36:59  INFO        [prep_universe] 120/901 (120 valid)
13:37:00  INFO        [prep_universe] 160/901 (160 valid)
13:37:02  INFO        [prep_universe] 200/901 (199 valid)
13:37:09  INFO        [prep_universe] 240/901 (238 valid)
13:37:22  INFO        [prep_universe] 280/901 (278 valid)
13:37:33  INFO        [prep_universe] 320/901 (318 valid)
13:37:46  INFO        [prep_universe] 360/901 (358 valid)
13:37:56  INFO        [prep_universe] 400/901 (398 valid)
13:38:10  INFO        [prep_universe] 440/901 (438 valid)
13:38:23  INFO        [prep_universe] 480/901 (478 valid)
13:38:33  INFO        [prep_universe] 520/901 (518 valid)
13:38:46  INFO        [prep_universe] 560/901 (558 valid)
13:38:57  INFO        [prep_universe] 600/901 (598 valid)
13:39:10  INFO        [prep_universe] 640/901 (638 valid)
13:39:20  INFO        [prep_universe] 680/901 (678 valid)
13:39:33  INFO        [prep_universe] 720/901 (718 valid)
13:39:47  INFO        [prep_universe] 760/901 (758 valid)
13:39:57  INFO        [prep_universe] 800/901 (798 valid)
13:40:10  INFO        [prep_universe] 840/901 (838 valid)
13:40:21  INFO        [prep_universe] 880/901 (878 valid)
13:40:27  INFO        [prep_universe] 901/901 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.28|
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
|  Invested                                                        $68.19|
|  Open P&L                                                        $+0.17|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAL      MomReversal     $33.95     $12.91   $12.86   -0.4%   $-0.15  |
|  ALLE     Pullback50      $34.24     $153.74  $155.17  +0.9%   $+0.32  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  AAL       OrderType.STOP    2         None        12.7                |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      0|
|  Signal candidates                                                   27|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-16T09:40:30.342943-04:00 share=25% ===
2026-09-16 09:40:30,343 INFO === options_live_micro LIVE 2026-09-16T09:40:30.342943-04:00 share=25% ===
Live account equity $225.13 cash $157.09 #225458845 options_level=3
2026-09-16 09:40:30,552 INFO Live account equity $225.13 cash $157.09 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-16 09:40:30,738 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-16 09:40:30,867 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=145 paper_keys=yes dry_run=False
  alpaca positions=18
  FLAG b234|S401|b9231ec1 missing from Alpaca
  FLAG b298|S353|e719fbe8 missing from Alpaca
  FLAG b291|S352|f55a8789 missing from Alpaca
  FLAG b290|S352|ecf95e3d missing from Alpaca
  FLAG b283|S351|5e578bef missing from Alpaca
  FLAG b282|S351|903af79d missing from Alpaca
  FLAG b279|S350|9a0492cc missing from Alpaca
  FLAG b278|S350|8a8f0492 missing from Alpaca
  FLAG b1139|S163|57e57104 missing from Alpaca
  FLAG b1138|S163|55f134ef missing from Alpaca
  FLAG b1097|S167|8553d8d6 missing from Alpaca
  FLAG b1096|S167|3a014094 missing from Alpaca
  FLAG b1125|S168|dea8dffc missing from Alpaca
  FLAG b1124|S168|bab83b1b missing from Alpaca
  FLAG b1153|S164|71fb46ef missing from Alpaca
  FLAG b1152|S164|4339f817 missing from Alpaca
  FLAG b1055|S165|b7d19491 missing from Alpaca
  FLAG b1054|S165|e288f8da missing from Alpaca
  FLAG b887|S410|8c6de481 missing from Alpaca
  FLAG b886|S410|a7ad4146 missing from Alpaca
  FLAG b771|S396|785cfd7f missing from Alpaca
  FLAG b770|S396|1557502f missing from Alpaca
  FLAG b238|S401|d8310518 missing from Alpaca
  FLAG b0|ORPHAN|668afe5d missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$1,000,281.47
  buying_power=$3,946,008.48 cash=$1,031,674.97
  open option orders: 15
    PATH260918C00014500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.18
    PATH260918C00016000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.02
    PATH261002C00015000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.18
    SNOW260918C00347500 OrderSide.SELL qty=3 status=OrderStatus.NEW limit=None
    META260918C00725000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
  open option positions: 17
    MARA260918C00011500 qty=9 mkt=$270.00
    MARA260918C00012000 qty=77 mkt=$1,155.00
    MARA260918C00012500 qty=4 mkt=$28.00
    MARA260925C00011500 qty=-1 mkt=$-57.00
    MARA260925C00012500 qty=3 mkt=$75.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-16T09:40:33.974781-04:00 ===

[Run context]
Paper auth OK — equity $1000281.47, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-16 09:40:36,497 INFO   EXIT [b803|lab0803_s404_w2_1005_1045_r2|S404] take_profit (+76.1%) SELL 1 SNOW260918C00345000 @<= 1.26
2026-09-16 09:40:37,987 INFO   EXIT [b305|lab0305_s354_w1_0928_1005_r2|S354] stop_loss (-50.1%) SELL 1 MARA260918C00012000 @<= 0.16
  EXIT [b861|lab0861_s408_w3_1045_1120_r2|S408] stop_loss (-58.8%) SELL failed MSTR260918C00157500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-16 09:40:40,697 INFO   EXIT [b406|lab0406_s364_w2_1005_1045_r1|S364] stop_loss (-63.0%) SELL 1 PATH260925C00015500 @<= 0.11
Protective stops: placed=0 upgraded=0 already=13 failed=2 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260916T134329Z

- UTC timestamp: `20260916T134329Z`
- GitHub run: [#10115](https://github.com/28twagg-ops/TradingBot/actions/runs/35103383374)
- Run id: `35103383374`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260916T134329Z_live_bot.log`, `logs/action_runs/20260916T134329Z_live_options.log`, `logs/action_runs/20260916T134329Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1235 | 49.0 | -16.0 | +39.7 | $+15,916 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 643 | 62.7 | +51.0 | +62.5 | $+10,833 |
| KEEP-only recent | 446 | 60.5 | +53.3 | +71.6 | $+6,188 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-16T09:26:25.093222-04:00","date":"2026-09-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":1000187.66,"open_positions":22,"pending_orders":0,"open_lots":145,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10112","github_run_id":"35101767909","status":"ok","data_quality":{"clean":{"n":1235,"win":48.99,"med":-16.0,"avg":39.72,"pnl":15915.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":643,"win":62.67,"med":50.98,"avg":62.47,"pnl":10833.45},"keep_only_recent":{"n":446,"win":60.54,"med":53.33,"avg":71.62,"pnl":6188.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:43:30  INFO      Mode: morning_prep
13:43:31  INFO        [prep_positions] 2/2 (2 valid)
13:43:31  INFO        Universe cache hit: 903 tickers (tickers_2026-09-16.json)
13:43:32  INFO        [prep_universe] 40/901 (40 valid)
13:43:33  INFO        [prep_universe] 80/901 (80 valid)
13:43:34  INFO        [prep_universe] 120/901 (120 valid)
13:43:36  INFO        [prep_universe] 160/901 (160 valid)
13:43:37  INFO        [prep_universe] 200/901 (199 valid)
13:43:44  INFO        [prep_universe] 240/901 (238 valid)
13:43:57  INFO        [prep_universe] 280/901 (278 valid)
13:44:10  INFO        [prep_universe] 320/901 (318 valid)
13:44:20  INFO        [prep_universe] 360/901 (358 valid)
13:44:33  INFO        [prep_universe] 400/901 (398 valid)
13:44:44  INFO        [prep_universe] 440/901 (438 valid)
13:44:57  INFO        [prep_universe] 480/901 (478 valid)
13:45:10  INFO        [prep_universe] 520/901 (518 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260916T134638Z

- UTC timestamp: `20260916T134638Z`
- GitHub run: [#10116](https://github.com/28twagg-ops/TradingBot/actions/runs/35103924343)
- Run id: `35103924343`
- Live bot: exit=`0`, duration=`246s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260916T134638Z_live_bot.log`, `logs/action_runs/20260916T134638Z_live_options.log`, `logs/action_runs/20260916T134638Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1235 | 49.0 | -16.0 | +39.7 | $+15,916 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 643 | 62.7 | +51.0 | +62.5 | $+10,833 |
| KEEP-only recent | 446 | 60.5 | +53.3 | +71.6 | $+6,188 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-16T09:26:25.093222-04:00","date":"2026-09-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":1000187.66,"open_positions":22,"pending_orders":0,"open_lots":145,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10112","github_run_id":"35101767909","status":"ok","data_quality":{"clean":{"n":1235,"win":48.99,"med":-16.0,"avg":39.72,"pnl":15915.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":643,"win":62.67,"med":50.98,"avg":62.47,"pnl":10833.45},"keep_only_recent":{"n":446,"win":60.54,"med":53.33,"avg":71.62,"pnl":6188.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
... (156 earlier lines - see full log file)
13:50:44  INFO        Daily log -> logs/daily/2026-09-16.md
13:50:44  INFO        Dashboard written → logs/dashboard.md

|  GEF      Pullback50      eq     $82.99   38.8   -2.46   50MA bounce (+|
|  KRYS     Pullback50      eq     $343.33  38.7   -2.65   50MA bounce (-|
|  LIVN     Pullback50      eq     $80.04   50.3   -2.91   50MA bounce (-|
|  RS       Pullback50      eq     $398.07  55.5   -1.86   50MA bounce (-|
|  SIRI     Pullback50      eq     $29.55   59.7   -2.44   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] ABNB  Pullback50                                   $33.78|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] ALL  Pullback50                                    $33.78|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] BMY  Pullback50                                      cap 3|
|    SKIP [eq] CAH  Pullback50                                      cap 3|
|    SKIP [eq] CB  Pullback50                                       cap 3|
|    SKIP [eq] CTAS  Pullback50                                     cap 3|
|    SKIP [eq] CTVA  Pullback50                                     cap 3|
|    SKIP [eq] ECL  Pullback50                                      cap 3|
|    SKIP [eq] FDS  Pullback50                                      cap 3|
|    SKIP [eq] GPC  Pullback50                                      cap 3|
|    SKIP [eq] HAS  Pullback50                                      cap 3|
|    SKIP [eq] INCY  Pullback50                                     cap 3|
|    SKIP [eq] MTD  Pullback50                                      cap 3|
|    SKIP [eq] MDLZ  Pullback50                                     cap 3|
|    SKIP [eq] NVDA  Pullback50                                     cap 3|
|    SKIP [eq] OKE  Pullback50                                      cap 3|
|    SKIP [eq] PAYX  Pullback50                                     cap 3|
|    SKIP [eq] PRU  Pullback50                                      cap 3|
|    SKIP [eq] STLD  Pullback50                                     cap 3|
|    SKIP [eq] VTRS  Pullback50                                     cap 3|
|    SKIP [eq] VLTO  Pullback50                                     cap 3|
|    SKIP [eq] WRB  Pullback50                                      cap 3|
|    SKIP [eq] WELL  Pullback50                                     cap 3|
|    SKIP [eq] ARMK  Pullback50                                     cap 3|
|    SKIP [eq] ASH  Pullback50                                      cap 3|
|    SKIP [eq] DOCN  Pullback50                                     cap 3|
|    SKIP [eq] ESNT  Pullback50                                     cap 3|
|    SKIP [eq] GEF  Pullback50                                      cap 3|
|    SKIP [eq] KRYS  Pullback50                                     cap 3|
|    SKIP [eq] LIVN  Pullback50                                     cap 3|
|    SKIP [eq] RS  Pullback50                                       cap 3|
|    SKIP [eq] SIRI  Pullback50                                     cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      2|
+------------------------------------------------------------------------+
|  ABNB                                                 still unconfirmed|
|  ALL                                                  still unconfirmed|
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
|  Strategy  GapDown + VolumeSpike (display only — schedule not enforced)|
|  Scanned                                                            900|
|  Signals                                                             32|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  2 unconfirmed|
|  Exits                                                                1|
|  Open pos                                                             3|
|  Equity                                                         $225.12|
|  Cash                                                           $123.42|
+========================================================================+
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260916T135204Z

- UTC timestamp: `20260916T135204Z`
- GitHub run: [#10117](https://github.com/28twagg-ops/TradingBot/actions/runs/35104465846)
- Run id: `35104465846`
- Live bot: exit=`0`, duration=`215s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260916T135204Z_live_bot.log`, `logs/action_runs/20260916T135204Z_live_options.log`, `logs/action_runs/20260916T135204Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1235 | 49.0 | -16.0 | +39.7 | $+15,916 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 643 | 62.7 | +51.0 | +62.5 | $+10,833 |
| KEEP-only recent | 446 | 60.5 | +53.3 | +71.6 | $+6,188 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-16T09:26:25.093222-04:00","date":"2026-09-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":1000187.66,"open_positions":22,"pending_orders":0,"open_lots":145,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10112","github_run_id":"35101767909","status":"ok","data_quality":{"clean":{"n":1235,"win":48.99,"med":-16.0,"avg":39.72,"pnl":15915.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":643,"win":62.67,"med":50.98,"avg":62.47,"pnl":10833.45},"keep_only_recent":{"n":446,"win":60.54,"med":53.33,"avg":71.62,"pnl":6188.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
... (104 earlier lines - see full log file)
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
|                         SIGNALS FOUND  --  34                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  GOOGL    Pullback50      eq     $347.12  54.0   -3.07   50MA bounce (+|
|  GOOG     Pullback50      eq     $343.37  53.6   -3.16   50MA bounce (-|
|  APO      Pullback50      eq     $127.99  36.9   -1.75   50MA bounce (-|
|  BMY      Pullback50      eq     $64.35   30.8   -2.45   50MA bounce (+|
|  CAH      Pullback50      eq     $233.60  43.2   -3.21   50MA bounce (-|
|  CB       Pullback50      eq     $343.42  49.5   -2.63   50MA bounce (-|
|  CTAS     Pullback50      eq     $200.31  36.6   -3.13   50MA bounce (-|
|  CTVA     Pullback50      eq     $82.94   50.2   -2.28   50MA bounce (-|
|  ECL      Pullback50      eq     $276.06  24.9   -2.59   50MA bounce (-|
|  FDS      Pullback50      eq     $276.10  40.8   -1.90   50MA bounce (-|
|  GPC      Pullback50      eq     $131.78  30.4   -2.62   50MA bounce (+|
|  INCY     Pullback50      eq     $122.25  37.1   -2.60   50MA bounce (+|
|  MDLZ     Pullback50      eq     $62.39   44.1   -3.22   50MA bounce (+|
|  MTD      Pullback50      eq     $1355.~  41.1   -1.60   50MA bounce (-|
|  NVDA     Pullback50      eq     $214.86  53.6   -2.02   50MA bounce (+|
|  PAYX     Pullback50      eq     $117.96  33.9   -2.76   50MA bounce (-|
|  STLD     Pullback50      eq     $242.46  57.2   -1.81   50MA bounce (-|
|  VLTO     Pullback50      eq     $96.59   41.3   -2.45   50MA bounce (+|
|  WRB      Pullback50      eq     $70.92   67.6   -1.94   50MA bounce (-|
|  WELL     Pullback50      eq     $235.74  39.4   -2.22   50MA bounce (-|
|  AFG      Pullback50      eq     $144.47  48.2   -2.00   50MA bounce (+|
|  ARMK     Pullback50      eq     $58.42   43.6   -2.66   50MA bounce (+|
|  ASH      Pullback50      eq     $70.69   34.3   -2.86   50MA bounce (-|
|  DOCN     Pullback50      eq     $123.16  55.7   -2.22   50MA bounce (+|
|  FTI      Pullback50      eq     $74.90   47.5   -3.09   50MA bounce (+|
|  GATX     Pullback50      eq     $179.63  52.9   -2.47   50MA bounce (+|13:55:39  INFO        place_all_stops: checking 3 positions...
13:55:39  INFO        STOP skipped ABNB: fractional (0.2010 shares) — software exit will handle it
13:55:39  INFO        STOP skipped ALL: fractional (0.1311 shares) — software exit will handle it
13:55:39  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
13:55:39  INFO        Daily log -> logs/daily/2026-09-16.md
13:55:39  INFO        Dashboard written → logs/dashboard.md

|  GEF      Pullback50      eq     $82.61   36.8   -2.46   50MA bounce (-|
|  KRYS     Pullback50      eq     $344.10  39.3   -2.64   50MA bounce (-|
|  LIVN     Pullback50      eq     $80.06   50.3   -2.91   50MA bounce (-|
|  RS       Pullback50      eq     $397.57  55.2   -1.85   50MA bounce (-|
|  SANM     Pullback50      eq     $198.69  50.0   -2.41   50MA bounce (-|
|  SCI      Pullback50      eq     $81.39   34.4   -2.90   50MA bounce (-|
|  SIRI     Pullback50      eq     $29.54   59.6   -2.43   50MA bounce (-|
|  UBSI     Pullback50      eq     $47.93   55.0   -3.30   50MA bounce (+|
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
|  Scanned                                                            898|
|  Signals                                                             34|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $225.24|
|  Cash                                                           $123.42|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-16T09:55:39.948768-04:00 share=25% ===
2026-09-16 09:55:39,948 INFO === options_live_micro LIVE 2026-09-16T09:55:39.948768-04:00 share=25% ===
Live account equity $225.24 cash $123.42 #225458845 options_level=3
2026-09-16 09:55:39,991 INFO Live account equity $225.24 cash $123.42 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-16 09:55:40,016 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-16 09:55:40,029 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=123 paper_keys=yes dry_run=False
  alpaca positions=17
  FLAG b234|S401|b9231ec1 missing from Alpaca
  FLAG b407|S364|b4bd56dd missing from Alpaca
  FLAG b406|S364|8716f37f missing from Alpaca
  FLAG b238|S401|d8310518 missing from Alpaca
  FLAG b0|ORPHAN|668afe5d missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$1,000,641.39
  buying_power=$3,945,908.56 cash=$1,031,848.89
  open option orders: 13
    PATH260918C00014500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.18
    PATH260918C00016000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.02
    SNOW260918C00347500 OrderSide.SELL qty=3 status=OrderStatus.NEW limit=None
    META260918C00725000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    META260918C00727500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 16
    MARA260918C00011500 qty=9 mkt=$333.00
    MARA260918C00012000 qty=76 mkt=$1,520.00
    MARA260918C00012500 qty=4 mkt=$40.00
    MARA260925C00011500 qty=-1 mkt=$-66.00
    MARA260925C00012500 qty=3 mkt=$90.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-16T09:55:42.253104-04:00 ===

[Run context]
Paper auth OK — equity $1000643.89, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-16 09:55:43,240 INFO   EXIT [b802|lab0802_s404_w2_1005_1045_r1|S404] take_profit (+63.4%) SELL 1 SNOW260918C00345000 @<= 1.13
  EXIT [b861|lab0861_s408_w3_1045_1120_r2|S408] stop_loss (-58.8%) SELL failed MSTR260918C00157500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=1 upgraded=0 already=9 failed=4 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---
