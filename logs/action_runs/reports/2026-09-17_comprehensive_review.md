# Daily Comprehensive Action Review - 2026-09-17

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260917T130113Z

- UTC timestamp: `20260917T130113Z`
- GitHub run: [#10239](https://github.com/28twagg-ops/TradingBot/actions/runs/35224369170)
- Run id: `35224369170`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260917T130113Z_live_bot.log`, `logs/action_runs/20260917T130113Z_live_options.log`, `logs/action_runs/20260917T130113Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1270 | 48.3 | -24.6 | +38.0 | $+15,688 |
| TAINTED | 1859 | 33.4 | -39.0 | +12.1 | $-9,274 |
| KEEP-only | 663 | 62.0 | +50.9 | +60.5 | $+10,921 |
| KEEP-only recent | 466 | 59.7 | +53.1 | +68.4 | $+6,276 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T09:01:20.055616-04:00","date":"2026-09-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.21},"signals":0,"placed":0,"equity":996704.91,"open_positions":17,"pending_orders":0,"open_lots":94,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10239","github_run_id":"35224369170","status":"ok","data_quality":{"clean":{"n":1270,"win":48.27,"med":-24.62,"avg":38.03,"pnl":15688.16},"tainted":{"n":1859,"win":33.41,"med":-38.98,"avg":12.07,"pnl":-9274.28},"keep_only":{"n":663,"win":61.99,"med":50.88,"avg":60.45,"pnl":10921.45},"keep_only_recent":{"n":466,"win":59.66,"med":53.09,"avg":68.36,"pnl":6276.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:01:14  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.26|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.26|
|  Cash                                                           $156.74|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.52|
|  Open P&L                                                        $+0.28|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CTAS     Pullback50      $33.75     $198.92  $199.68  +0.4%   $+0.13  |
|  RBC      MomReversal     $33.77     $484.91  $487.14  +0.5%   $+0.15  |
|                                                                        |
|  Total invested                                                  $67.52|
|  Total open P&L                                                  $+0.28|
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
|  2026-09-16  SELL  CIEN  MomReversal  $33.44  P&L $-0.18               |
|  2026-09-16  SELL  ABNB  Pullback50  $33.55  P&L $-0.22                |
|  2026-09-16  SELL  ALLE  Pullback50  $33.67  P&L $-0.25                |
|  2026-09-16  SELL  ALL  Pullback50  $33.57  P&L $-0.20                 |
|  2026-09-16  SELL  AAL  MomReversal  $33.90  P&L $-0.21                |
|  2026-09-15  SELL  MO  Pullback50  $33.72  P&L $+0.01                  |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-17T09:01:16.832173-04:00 share=25% ===
2026-09-17 09:01:16,832 INFO === options_live_micro LIVE 2026-09-17T09:01:16.832173-04:00 share=25% ===
Live account equity $224.26 cash $156.74 #225458845 options_level=3
2026-09-17 09:01:16,927 INFO Live account equity $224.26 cash $156.74 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-17 09:01:16,969 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-17 09:01:16,990 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (165 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    29 | WARN | <<<
| Orphaned lots (post-stable) |  1394 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    94 | INFO |
| Total closed lots           |  2268 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1270 med=-24.6% | TAINTED n=1859 med=-39.0% | KEEP-only n=663 med=+50.9% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T130612Z

- UTC timestamp: `20260917T130612Z`
- GitHub run: [#10240](https://github.com/28twagg-ops/TradingBot/actions/runs/35224877666)
- Run id: `35224877666`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260917T130612Z_live_bot.log`, `logs/action_runs/20260917T130612Z_live_options.log`, `logs/action_runs/20260917T130612Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1270 | 48.3 | -24.6 | +38.0 | $+15,688 |
| TAINTED | 1859 | 33.4 | -39.0 | +12.1 | $-9,274 |
| KEEP-only | 663 | 62.0 | +50.9 | +60.5 | $+10,921 |
| KEEP-only recent | 466 | 59.7 | +53.1 | +68.4 | $+6,276 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T09:06:20.530496-04:00","date":"2026-09-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.55},"signals":0,"placed":0,"equity":996726.84,"open_positions":17,"pending_orders":0,"open_lots":94,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10240","github_run_id":"35224877666","status":"ok","data_quality":{"clean":{"n":1270,"win":48.27,"med":-24.62,"avg":38.03,"pnl":15688.16},"tainted":{"n":1859,"win":33.41,"med":-38.98,"avg":12.07,"pnl":-9274.28},"keep_only":{"n":663,"win":61.99,"med":50.88,"avg":60.45,"pnl":10921.45},"keep_only_recent":{"n":466,"win":59.66,"med":53.09,"avg":68.36,"pnl":6276.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:06:15  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.26|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.26|
|  Cash                                                           $156.74|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.52|
|  Open P&L                                                        $+0.28|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CTAS     Pullback50      $33.75     $198.92  $199.68  +0.4%   $+0.13  |
|  RBC      MomReversal     $33.77     $484.91  $487.14  +0.5%   $+0.15  |
|                                                                        |
|  Total invested                                                  $67.52|
|  Total open P&L                                                  $+0.28|
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
|  2026-09-16  SELL  CIEN  MomReversal  $33.44  P&L $-0.18               |
|  2026-09-16  SELL  ABNB  Pullback50  $33.55  P&L $-0.22                |
|  2026-09-16  SELL  ALLE  Pullback50  $33.67  P&L $-0.25                |
|  2026-09-16  SELL  ALL  Pullback50  $33.57  P&L $-0.20                 |
|  2026-09-16  SELL  AAL  MomReversal  $33.90  P&L $-0.21                |
|  2026-09-15  SELL  MO  Pullback50  $33.72  P&L $+0.01                  |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-17T09:06:16.835539-04:00 share=25% ===
2026-09-17 09:06:16,835 INFO === options_live_micro LIVE 2026-09-17T09:06:16.835539-04:00 share=25% ===
Live account equity $224.26 cash $156.74 #225458845 options_level=3
2026-09-17 09:06:17,076 INFO Live account equity $224.26 cash $156.74 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-17 09:06:17,150 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-17 09:06:17,223 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (165 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    29 | WARN | <<<
| Orphaned lots (post-stable) |  1394 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    94 | INFO |
| Total closed lots           |  2268 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1270 med=-24.6% | TAINTED n=1859 med=-39.0% | KEEP-only n=663 med=+50.9% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T131108Z

- UTC timestamp: `20260917T131108Z`
- GitHub run: [#10241](https://github.com/28twagg-ops/TradingBot/actions/runs/35225381595)
- Run id: `35225381595`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260917T131108Z_live_bot.log`, `logs/action_runs/20260917T131108Z_live_options.log`, `logs/action_runs/20260917T131108Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1270 | 48.3 | -24.6 | +38.0 | $+15,688 |
| TAINTED | 1859 | 33.4 | -39.0 | +12.1 | $-9,274 |
| KEEP-only | 663 | 62.0 | +50.9 | +60.5 | $+10,921 |
| KEEP-only recent | 466 | 59.7 | +53.1 | +68.4 | $+6,276 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T09:11:17.350922-04:00","date":"2026-09-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.5,"phases_s":{"reconcile":0.59},"signals":0,"placed":0,"equity":996725.84,"open_positions":17,"pending_orders":0,"open_lots":94,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10241","github_run_id":"35225381595","status":"ok","data_quality":{"clean":{"n":1270,"win":48.27,"med":-24.62,"avg":38.03,"pnl":15688.16},"tainted":{"n":1859,"win":33.41,"med":-38.98,"avg":12.07,"pnl":-9274.28},"keep_only":{"n":663,"win":61.99,"med":50.88,"avg":60.45,"pnl":10921.45},"keep_only_recent":{"n":466,"win":59.66,"med":53.09,"avg":68.36,"pnl":6276.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
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
|  Equity                                                         $224.26|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.26|
|  Cash                                                           $156.74|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.52|
|  Open P&L                                                        $+0.28|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CTAS     Pullback50      $33.75     $198.92  $199.68  +0.4%   $+0.13  |
|  RBC      MomReversal     $33.77     $484.91  $487.14  +0.5%   $+0.15  |
|                                                                        |
|  Total invested                                                  $67.52|
|  Total open P&L                                                  $+0.28|
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
|  2026-09-16  SELL  CIEN  MomReversal  $33.44  P&L $-0.18               |
|  2026-09-16  SELL  ABNB  Pullback50  $33.55  P&L $-0.22                |
|  2026-09-16  SELL  ALLE  Pullback50  $33.67  P&L $-0.25                |
|  2026-09-16  SELL  ALL  Pullback50  $33.57  P&L $-0.20                 |
|  2026-09-16  SELL  AAL  MomReversal  $33.90  P&L $-0.21                |
|  2026-09-15  SELL  MO  Pullback50  $33.72  P&L $+0.01                  |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-17T09:11:13.568219-04:00 share=25% ===
2026-09-17 09:11:13,568 INFO === options_live_micro LIVE 2026-09-17T09:11:13.568219-04:00 share=25% ===
Live account equity $224.26 cash $156.74 #225458845 options_level=3
2026-09-17 09:11:13,818 INFO Live account equity $224.26 cash $156.74 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-17 09:11:13,901 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-17 09:11:13,979 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (165 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    29 | WARN | <<<
| Orphaned lots (post-stable) |  1394 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    94 | INFO |
| Total closed lots           |  2268 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1270 med=-24.6% | TAINTED n=1859 med=-39.0% | KEEP-only n=663 med=+50.9% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T131607Z

- UTC timestamp: `20260917T131607Z`
- GitHub run: [#10242](https://github.com/28twagg-ops/TradingBot/actions/runs/35225891083)
- Run id: `35225891083`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260917T131607Z_live_bot.log`, `logs/action_runs/20260917T131607Z_live_options.log`, `logs/action_runs/20260917T131607Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1270 | 48.3 | -24.6 | +38.0 | $+15,688 |
| TAINTED | 1859 | 33.4 | -39.0 | +12.1 | $-9,274 |
| KEEP-only | 663 | 62.0 | +50.9 | +60.5 | $+10,921 |
| KEEP-only recent | 466 | 59.7 | +53.1 | +68.4 | $+6,276 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T09:16:13.285275-04:00","date":"2026-09-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":996728.84,"open_positions":17,"pending_orders":0,"open_lots":94,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10242","github_run_id":"35225891083","status":"ok","data_quality":{"clean":{"n":1270,"win":48.27,"med":-24.62,"avg":38.03,"pnl":15688.16},"tainted":{"n":1859,"win":33.41,"med":-38.98,"avg":12.07,"pnl":-9274.28},"keep_only":{"n":663,"win":61.99,"med":50.88,"avg":60.45,"pnl":10921.45},"keep_only_recent":{"n":466,"win":59.66,"med":53.09,"avg":68.36,"pnl":6276.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
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
|  Equity                                                         $224.26|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.26|
|  Cash                                                           $156.74|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.52|
|  Open P&L                                                        $+0.28|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CTAS     Pullback50      $33.75     $198.92  $199.68  +0.4%   $+0.13  |
|  RBC      MomReversal     $33.77     $484.91  $487.14  +0.5%   $+0.15  |
|                                                                        |
|  Total invested                                                  $67.52|
|  Total open P&L                                                  $+0.28|
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
|  2026-09-16  SELL  CIEN  MomReversal  $33.44  P&L $-0.18               |
|  2026-09-16  SELL  ABNB  Pullback50  $33.55  P&L $-0.22                |
|  2026-09-16  SELL  ALLE  Pullback50  $33.67  P&L $-0.25                |
|  2026-09-16  SELL  ALL  Pullback50  $33.57  P&L $-0.20                 |
|  2026-09-16  SELL  AAL  MomReversal  $33.90  P&L $-0.21                |
|  2026-09-15  SELL  MO  Pullback50  $33.72  P&L $+0.01                  |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-17T09:16:10.396851-04:00 share=25% ===
2026-09-17 09:16:10,396 INFO === options_live_micro LIVE 2026-09-17T09:16:10.396851-04:00 share=25% ===
Live account equity $224.26 cash $156.74 #225458845 options_level=3
2026-09-17 09:16:10,452 INFO Live account equity $224.26 cash $156.74 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-17 09:16:10,466 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-17 09:16:10,476 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (165 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    29 | WARN | <<<
| Orphaned lots (post-stable) |  1394 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    94 | INFO |
| Total closed lots           |  2268 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1270 med=-24.6% | TAINTED n=1859 med=-39.0% | KEEP-only n=663 med=+50.9% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T132101Z

- UTC timestamp: `20260917T132101Z`
- GitHub run: [#10243](https://github.com/28twagg-ops/TradingBot/actions/runs/35226405064)
- Run id: `35226405064`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20260917T132101Z_live_bot.log`, `logs/action_runs/20260917T132101Z_live_options.log`, `logs/action_runs/20260917T132101Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1270 | 48.3 | -24.6 | +38.0 | $+15,688 |
| TAINTED | 1859 | 33.4 | -39.0 | +12.1 | $-9,274 |
| KEEP-only | 663 | 62.0 | +50.9 | +60.5 | $+10,921 |
| KEEP-only recent | 466 | 59.7 | +53.1 | +68.4 | $+6,276 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T09:21:06.144873-04:00","date":"2026-09-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.29},"signals":0,"placed":0,"equity":996730.84,"open_positions":17,"pending_orders":0,"open_lots":94,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10243","github_run_id":"35226405064","status":"ok","data_quality":{"clean":{"n":1270,"win":48.27,"med":-24.62,"avg":38.03,"pnl":15688.16},"tainted":{"n":1859,"win":33.41,"med":-38.98,"avg":12.07,"pnl":-9274.28},"keep_only":{"n":663,"win":61.99,"med":50.88,"avg":60.45,"pnl":10921.45},"keep_only_recent":{"n":466,"win":59.66,"med":53.09,"avg":68.36,"pnl":6276.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
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
|  Equity                                                         $224.26|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.26|
|  Cash                                                           $156.74|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.52|
|  Open P&L                                                        $+0.28|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CTAS     Pullback50      $33.75     $198.92  $199.68  +0.4%   $+0.13  |
|  RBC      MomReversal     $33.77     $484.91  $487.14  +0.5%   $+0.15  |
|                                                                        |
|  Total invested                                                  $67.52|
|  Total open P&L                                                  $+0.28|
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
|  2026-09-16  SELL  CIEN  MomReversal  $33.44  P&L $-0.18               |
|  2026-09-16  SELL  ABNB  Pullback50  $33.55  P&L $-0.22                |
|  2026-09-16  SELL  ALLE  Pullback50  $33.67  P&L $-0.25                |
|  2026-09-16  SELL  ALL  Pullback50  $33.57  P&L $-0.20                 |
|  2026-09-16  SELL  AAL  MomReversal  $33.90  P&L $-0.21                |
|  2026-09-15  SELL  MO  Pullback50  $33.72  P&L $+0.01                  |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-17T09:21:03.775147-04:00 share=25% ===
2026-09-17 09:21:03,775 INFO === options_live_micro LIVE 2026-09-17T09:21:03.775147-04:00 share=25% ===
Live account equity $224.26 cash $156.74 #225458845 options_level=3
2026-09-17 09:21:03,942 INFO Live account equity $224.26 cash $156.74 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-17 09:21:04,021 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-17 09:21:04,051 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (165 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    29 | WARN | <<<
| Orphaned lots (post-stable) |  1394 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    94 | INFO |
| Total closed lots           |  2268 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1270 med=-24.6% | TAINTED n=1859 med=-39.0% | KEEP-only n=663 med=+50.9% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T132610Z

- UTC timestamp: `20260917T132610Z`
- GitHub run: [#10244](https://github.com/28twagg-ops/TradingBot/actions/runs/35226928849)
- Run id: `35226928849`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20260917T132610Z_live_bot.log`, `logs/action_runs/20260917T132610Z_live_options.log`, `logs/action_runs/20260917T132610Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1270 | 48.3 | -24.6 | +38.0 | $+15,688 |
| TAINTED | 1859 | 33.4 | -39.0 | +12.1 | $-9,274 |
| KEEP-only | 663 | 62.0 | +50.9 | +60.5 | $+10,921 |
| KEEP-only recent | 466 | 59.7 | +53.1 | +68.4 | $+6,276 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T09:26:17.601036-04:00","date":"2026-09-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.58},"signals":0,"placed":0,"equity":996788.34,"open_positions":17,"pending_orders":0,"open_lots":94,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10244","github_run_id":"35226928849","status":"ok","data_quality":{"clean":{"n":1270,"win":48.27,"med":-24.62,"avg":38.03,"pnl":15688.16},"tainted":{"n":1859,"win":33.41,"med":-38.98,"avg":12.07,"pnl":-9274.28},"keep_only":{"n":663,"win":61.99,"med":50.88,"avg":60.45,"pnl":10921.45},"keep_only_recent":{"n":466,"win":59.66,"med":53.09,"avg":68.36,"pnl":6276.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:26:12  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.26|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.26|
|  Cash                                                           $156.74|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.52|
|  Open P&L                                                        $+0.28|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CTAS     Pullback50      $33.75     $198.92  $199.68  +0.4%   $+0.13  |
|  RBC      MomReversal     $33.77     $484.91  $487.14  +0.5%   $+0.15  |
|                                                                        |
|  Total invested                                                  $67.52|
|  Total open P&L                                                  $+0.28|
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
|  2026-09-16  SELL  CIEN  MomReversal  $33.44  P&L $-0.18               |
|  2026-09-16  SELL  ABNB  Pullback50  $33.55  P&L $-0.22                |
|  2026-09-16  SELL  ALLE  Pullback50  $33.67  P&L $-0.25                |
|  2026-09-16  SELL  ALL  Pullback50  $33.57  P&L $-0.20                 |
|  2026-09-16  SELL  AAL  MomReversal  $33.90  P&L $-0.21                |
|  2026-09-15  SELL  MO  Pullback50  $33.72  P&L $+0.01                  |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-17T09:26:13.866162-04:00 share=25% ===
2026-09-17 09:26:13,866 INFO === options_live_micro LIVE 2026-09-17T09:26:13.866162-04:00 share=25% ===
Live account equity $224.26 cash $156.74 #225458845 options_level=3
2026-09-17 09:26:14,069 INFO Live account equity $224.26 cash $156.74 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-17 09:26:14,255 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-17 09:26:14,311 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (165 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    29 | WARN | <<<
| Orphaned lots (post-stable) |  1394 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    94 | INFO |
| Total closed lots           |  2268 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1270 med=-24.6% | TAINTED n=1859 med=-39.0% | KEEP-only n=663 med=+50.9% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T133111Z

- UTC timestamp: `20260917T133111Z`
- GitHub run: [#10245](https://github.com/28twagg-ops/TradingBot/actions/runs/35227448980)
- Run id: `35227448980`
- Live bot: exit=`0`, duration=`218s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260917T133111Z_live_bot.log`, `logs/action_runs/20260917T133111Z_live_options.log`, `logs/action_runs/20260917T133111Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1270 | 48.3 | -24.6 | +38.0 | $+15,688 |
| TAINTED | 1859 | 33.4 | -39.0 | +12.1 | $-9,274 |
| KEEP-only | 663 | 62.0 | +50.9 | +60.5 | $+10,921 |
| KEEP-only recent | 466 | 59.7 | +53.1 | +68.4 | $+6,276 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T09:26:17.601036-04:00","date":"2026-09-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.58},"signals":0,"placed":0,"equity":996788.34,"open_positions":17,"pending_orders":0,"open_lots":94,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10244","github_run_id":"35226928849","status":"ok","data_quality":{"clean":{"n":1270,"win":48.27,"med":-24.62,"avg":38.03,"pnl":15688.16},"tainted":{"n":1859,"win":33.41,"med":-38.98,"avg":12.07,"pnl":-9274.28},"keep_only":{"n":663,"win":61.99,"med":50.88,"avg":60.45,"pnl":10921.45},"keep_only_recent":{"n":466,"win":59.66,"med":53.09,"avg":68.36,"pnl":6276.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:31:11  INFO      Mode: morning_prep
13:31:13  INFO        [prep_positions] 3/3 (3 valid)
13:31:13  INFO      Fetching tickers (universe=both)...
13:31:14  INFO        S&P 500: 503
13:31:14  INFO        MidCap 400: 400
13:31:14  INFO        Total: 903 tickers
13:31:15  INFO        [prep_universe] 40/900 (40 valid)
13:31:17  INFO        [prep_universe] 80/900 (80 valid)
13:31:18  INFO        [prep_universe] 120/900 (120 valid)
13:31:20  INFO        [prep_universe] 160/900 (160 valid)
13:31:21  INFO        [prep_universe] 200/900 (199 valid)
13:31:28  INFO        [prep_universe] 240/900 (238 valid)
13:31:39  INFO        [prep_universe] 280/900 (278 valid)
13:31:52  INFO        [prep_universe] 320/900 (318 valid)
13:32:03  INFO        [prep_universe] 360/900 (358 valid)
13:32:16  INFO        [prep_universe] 400/900 (398 valid)
13:32:27  INFO        [prep_universe] 440/900 (438 valid)
13:32:40  INFO        [prep_universe] 480/900 (478 valid)
13:32:50  INFO        [prep_universe] 520/900 (518 valid)
13:33:04  INFO        [prep_universe] 560/900 (558 valid)
13:33:14  INFO        [prep_universe] 600/900 (598 valid)
13:33:28  INFO        [prep_universe] 640/900 (638 valid)
13:33:38  INFO        [prep_universe] 680/900 (678 valid)
13:33:51  INFO        [prep_universe] 720/900 (718 valid)
13:34:05  INFO        [prep_universe] 760/900 (758 valid)
13:34:15  INFO        [prep_universe] 800/900 (798 valid)
13:34:29  INFO        [prep_universe] 840/900 (838 valid)
13:34:39  INFO        [prep_universe] 880/900 (878 valid)
13:34:46  INFO        [prep_universe] 900/900 (898 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.58|
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
|  Invested                                                       $102.46|
|  Open P&L                                                        $+1.61|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CIEN     MomReversal     $34.38     $350.60  $358.62  +2.3%   $+0.77  |
|  CTAS     Pullback50      $33.63     $198.92  $198.98  +0.0%   $+0.01  |
|  RBC      MomReversal     $34.45     $484.91  $496.83  +2.5%   $+0.83  |
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
|  Signal candidates                                                   17|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-17T09:34:49.688741-04:00 share=25% ===
2026-09-17 09:34:49,688 INFO === options_live_micro LIVE 2026-09-17T09:34:49.688741-04:00 share=25% ===
Live account equity $225.79 cash $123.12 #225458845 options_level=3
2026-09-17 09:34:49,946 INFO Live account equity $225.79 cash $123.12 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 09:34:50,179 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 09:34:50,329 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=94 paper_keys=yes dry_run=False
  alpaca positions=17
  FLAG b779|S397|01866ade missing from Alpaca
  FLAG b778|S397|9ab83dc6 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$997,099.73
  buying_power=$3,937,334.12 cash=$1,030,713.73
  open option orders: 9
    CRWD260918C00285000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.01
    GTLB260925C00052000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    HON260918C00217500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    AAPL260918C00340000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    LLY260918C01225000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
  open option positions: 16
    AAPL260918C00340000 qty=2 mkt=$80.00
    CRWD260918C00285000 qty=1 mkt=$0.00
    FSLY260918C00025000 qty=1 mkt=$10.00
    GTLB260925C00052000 qty=1 mkt=$15.00
    HON260918C00215000 qty=1 mkt=$0.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-17T09:34:53.575706-04:00 ===

[Run context]
Paper auth OK — equity $997104.73, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b861|lab0861_s408_w3_1045_1120_r2|S408] stop_loss (-100.0%) SELL failed MSTR260918C00157500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-17 09:34:56,501 INFO   EXIT [b267|lab0267_s403_w3_1045_1120_r2|S403] stop_loss (-100.0%) SELL 1 PATH260918C00016000 @<= 0.01
2026-09-17 09:34:57,497 INFO   EXIT [b168|lab0168_s216_w3_1045_1120_r1|S216] stop_loss (-72.0%) SELL 1 LLY260918C01225000 @<= 0.04
2026-09-17 09:34:59,011 INFO   EXIT [b781|lab0781_s397_w3_1045_1120_r2|S397] stop_loss (-78.6%) SELL 1 GTLB260925C00052000 @<= 0.16
  EXIT [b182|lab0182_s217_w3_1045_1120_r1|S217] stop_loss (-100.0%) SELL failed HON260918C00215000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-17 09:34:59,817 INFO   EXIT [b314|lab0314_s355_w2_1005_1045_r1|S355] stop_loss (-55.1%) SELL 1 MARA260918C00012000 @<= 0.14
2026-09-17 09:35:00,530 INFO   EXIT [b366|lab0366_s361_w3_1045_1120_r1|S361] stop_loss (-81.8%) SELL 1 FSLY260918C00025000 @<= 0.11
Protective stops: placed=0 upgraded=0 already=7 failed=5 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260917T133645Z

- UTC timestamp: `20260917T133645Z`
- GitHub run: [#10246](https://github.com/28twagg-ops/TradingBot/actions/runs/35227980068)
- Run id: `35227980068`
- Live bot: exit=`0`, duration=`215s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260917T133645Z_live_bot.log`, `logs/action_runs/20260917T133645Z_live_options.log`, `logs/action_runs/20260917T133645Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1270 | 48.3 | -24.6 | +38.0 | $+15,688 |
| TAINTED | 1859 | 33.4 | -39.0 | +12.1 | $-9,274 |
| KEEP-only | 663 | 62.0 | +50.9 | +60.5 | $+10,921 |
| KEEP-only recent | 466 | 59.7 | +53.1 | +68.4 | $+6,276 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T09:26:17.601036-04:00","date":"2026-09-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.58},"signals":0,"placed":0,"equity":996788.34,"open_positions":17,"pending_orders":0,"open_lots":94,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10244","github_run_id":"35226928849","status":"ok","data_quality":{"clean":{"n":1270,"win":48.27,"med":-24.62,"avg":38.03,"pnl":15688.16},"tainted":{"n":1859,"win":33.41,"med":-38.98,"avg":12.07,"pnl":-9274.28},"keep_only":{"n":663,"win":61.99,"med":50.88,"avg":60.45,"pnl":10921.45},"keep_only_recent":{"n":466,"win":59.66,"med":53.09,"avg":68.36,"pnl":6276.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:36:46  INFO      Mode: morning_prep
13:36:47  INFO        [prep_positions] 3/3 (3 valid)
13:36:47  INFO      Fetching tickers (universe=both)...
13:36:47  INFO        S&P 500: 503
13:36:48  INFO        MidCap 400: 400
13:36:48  INFO        Total: 903 tickers
13:36:49  INFO        [prep_universe] 40/900 (40 valid)
13:36:50  INFO        [prep_universe] 80/900 (80 valid)
13:36:51  INFO        [prep_universe] 120/900 (120 valid)
13:36:51  INFO        [prep_universe] 160/900 (160 valid)
13:36:53  INFO        [prep_universe] 200/900 (199 valid)
13:37:03  INFO        [prep_universe] 240/900 (238 valid)
13:37:12  INFO        [prep_universe] 280/900 (278 valid)
13:37:25  INFO        [prep_universe] 320/900 (318 valid)
13:37:38  INFO        [prep_universe] 360/900 (358 valid)
13:37:48  INFO        [prep_universe] 400/900 (398 valid)
13:38:01  INFO        [prep_universe] 440/900 (438 valid)
13:38:14  INFO        [prep_universe] 480/900 (478 valid)
13:38:24  INFO        [prep_universe] 520/900 (518 valid)
13:38:37  INFO        [prep_universe] 560/900 (558 valid)
13:38:50  INFO        [prep_universe] 600/900 (598 valid)
13:39:00  INFO        [prep_universe] 640/900 (638 valid)
13:39:13  INFO        [prep_universe] 680/900 (678 valid)
13:39:26  INFO        [prep_universe] 720/900 (718 valid)
13:39:36  INFO        [prep_universe] 760/900 (758 valid)
13:39:49  INFO        [prep_universe] 800/900 (798 valid)
13:40:02  INFO        [prep_universe] 840/900 (838 valid)
13:40:12  INFO        [prep_universe] 880/900 (878 valid)
13:40:19  INFO        [prep_universe] 900/900 (898 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.91|
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
|  Invested                                                       $103.79|
|  Open P&L                                                        $+2.94|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CIEN     MomReversal     $35.43     $350.60  $369.61  +5.4%   $+1.82  |
|  CTAS     Pullback50      $33.53     $198.92  $198.41  -0.3%   $-0.09  |
|  RBC      MomReversal     $34.82     $484.91  $502.22  +3.6%   $+1.20  |
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
|  Signal candidates                                                   15|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-17T09:40:21.388058-04:00 share=25% ===
2026-09-17 09:40:21,388 INFO === options_live_micro LIVE 2026-09-17T09:40:21.388058-04:00 share=25% ===
Live account equity $226.42 cash $123.12 #225458845 options_level=3
2026-09-17 09:40:21,508 INFO Live account equity $226.42 cash $123.12 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 09:40:21,606 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 09:40:21,673 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=94 paper_keys=yes dry_run=False
  alpaca positions=15
  FLAG b779|S397|01866ade missing from Alpaca
  FLAG b778|S397|9ab83dc6 missing from Alpaca
  FLAG b367|S361|5a194e94 missing from Alpaca
  FLAG b366|S361|4fa5fa74 missing from Alpaca
  FLAG b101|S211|64be1a51 missing from Alpaca
  FLAG b100|S211|399c668c missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,928.62
  buying_power=$3,938,138.48 cash=$1,030,831.62
  open option orders: 8
    GTLB260925C00052000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.16
    PATH260918C00016000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.01
    CRWD260918C00285000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.01
    HON260918C00217500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    SNOW260918C00345000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 14
    CRWD260918C00285000 qty=1 mkt=$0.00
    GTLB260925C00052000 qty=1 mkt=$15.00
    HON260918C00215000 qty=1 mkt=$0.00
    LLY260918C01225000 qty=1 mkt=$7.00
    MARA260918C00011000 qty=-1 mkt=$-45.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-17T09:40:24.029380-04:00 ===

[Run context]
Paper auth OK — equity $996928.62, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b861|lab0861_s408_w3_1045_1120_r2|S408] stop_loss (-100.0%) SELL failed MSTR260918C00157500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-17 09:40:25,814 INFO   EXIT [b409|lab0409_s364_w3_1045_1120_r2|S364] stop_loss (-75.8%) SELL 1 MARA260918C00012000 @<= 0.04
  EXIT [b182|lab0182_s217_w3_1045_1120_r1|S217] stop_loss (-100.0%) SELL failed HON260918C00215000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b434|lab0434_s366_w2_1005_1045_r1|S366] stop_loss (-61.7%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b433|lab0433_s366_w1_0928_1005_r2|S366] stop_loss (-61.7%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b432|lab0432_s366_w1_0928_1005_r1|S366] stop_loss (-61.7%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-17 09:40:27,362 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-72.0%) SELL 1 LLY260918C01225000 @<= 0.08
  EXIT [b783|lab0783_s397_w4_1120_1135_r2|S397] take_profit (+174.6%) SELL failed SNOW260918C00347500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 upgraded=0 already=5 failed=5 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
Found 103 signal(s); top: ['S165:CRWD', 'S164:CRWD', 'S168:CRWD', 'S167:CRWD', 'S163:CRWD', 'S350:CRWD', 'S351:CRWD', 'S352:CRWD']
Paper lab: $996929 broker equity -> 1164 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260917T134222Z

- UTC timestamp: `20260917T134222Z`
- GitHub run: [#10247](https://github.com/28twagg-ops/TradingBot/actions/runs/35228514376)
- Run id: `35228514376`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260917T134222Z_live_bot.log`, `logs/action_runs/20260917T134222Z_live_options.log`, `logs/action_runs/20260917T134222Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1270 | 48.3 | -24.6 | +38.0 | $+15,688 |
| TAINTED | 1859 | 33.4 | -39.0 | +12.1 | $-9,274 |
| KEEP-only | 663 | 62.0 | +50.9 | +60.5 | $+10,921 |
| KEEP-only recent | 466 | 59.7 | +53.1 | +68.4 | $+6,276 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T09:26:17.601036-04:00","date":"2026-09-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.58},"signals":0,"placed":0,"equity":996788.34,"open_positions":17,"pending_orders":0,"open_lots":94,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10244","github_run_id":"35226928849","status":"ok","data_quality":{"clean":{"n":1270,"win":48.27,"med":-24.62,"avg":38.03,"pnl":15688.16},"tainted":{"n":1859,"win":33.41,"med":-38.98,"avg":12.07,"pnl":-9274.28},"keep_only":{"n":663,"win":61.99,"med":50.88,"avg":60.45,"pnl":10921.45},"keep_only_recent":{"n":466,"win":59.66,"med":53.09,"avg":68.36,"pnl":6276.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:42:23  INFO      Mode: morning_prep
13:42:25  INFO        [prep_positions] 3/3 (3 valid)
13:42:25  INFO        Universe cache hit: 903 tickers (tickers_2026-09-17.json)
13:42:26  INFO        [prep_universe] 40/900 (40 valid)
13:42:28  INFO        [prep_universe] 80/900 (80 valid)
13:42:29  INFO        [prep_universe] 120/900 (120 valid)
13:42:30  INFO        [prep_universe] 160/900 (160 valid)
13:42:32  INFO        [prep_universe] 200/900 (199 valid)
13:42:39  INFO        [prep_universe] 240/900 (238 valid)
13:42:52  INFO        [prep_universe] 280/900 (278 valid)
13:43:02  INFO        [prep_universe] 320/900 (318 valid)
13:43:15  INFO        [prep_universe] 360/900 (358 valid)
13:43:27  INFO        [prep_universe] 400/900 (398 valid)
13:43:39  INFO        [prep_universe] 440/900 (438 valid)
13:43:51  INFO        [prep_universe] 480/900 (478 valid)
13:44:03  INFO        [prep_universe] 520/900 (518 valid)
13:44:17  INFO        [prep_universe] 560/900 (558 valid)
13:44:27  INFO        [prep_universe] 600/900 (598 valid)
13:44:40  INFO        [prep_universe] 640/900 (638 valid)
13:44:50  INFO        [prep_universe] 680/900 (678 valid)
13:45:03  INFO        [prep_universe] 720/900 (718 valid)
13:45:17  INFO        [prep_universe] 760/900 (758 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260917T134642Z

- UTC timestamp: `20260917T134642Z`
- GitHub run: [#10248](https://github.com/28twagg-ops/TradingBot/actions/runs/35229057029)
- Run id: `35229057029`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260917T134642Z_live_bot.log`, `logs/action_runs/20260917T134642Z_live_options.log`, `logs/action_runs/20260917T134642Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1270 | 48.3 | -24.6 | +38.0 | $+15,688 |
| TAINTED | 1859 | 33.4 | -39.0 | +12.1 | $-9,274 |
| KEEP-only | 663 | 62.0 | +50.9 | +60.5 | $+10,921 |
| KEEP-only recent | 466 | 59.7 | +53.1 | +68.4 | $+6,276 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T09:26:17.601036-04:00","date":"2026-09-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.58},"signals":0,"placed":0,"equity":996788.34,"open_positions":17,"pending_orders":0,"open_lots":94,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10244","github_run_id":"35226928849","status":"ok","data_quality":{"clean":{"n":1270,"win":48.27,"med":-24.62,"avg":38.03,"pnl":15688.16},"tainted":{"n":1859,"win":33.41,"med":-38.98,"avg":12.07,"pnl":-9274.28},"keep_only":{"n":663,"win":61.99,"med":50.88,"avg":60.45,"pnl":10921.45},"keep_only_recent":{"n":466,"win":59.66,"med":53.09,"avg":68.36,"pnl":6276.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:46:43  INFO      Mode: morning_scan
13:46:44  INFO        [positions] 3/3 (3 valid)
13:46:45  INFO        SELL LIMIT RBC  qty=0.069332453  limit=$503.78  id=ad11e33c-3dcd-49bf-8432-19451afc9579
13:47:15  INFO        SELL LIMIT filled RBC (confirmed by position check)
13:47:15  INFO        TX logged: SELL RBC  P&L 4.1%
13:47:15  INFO        SELL LIMIT CIEN  qty=0.095864232  limit=$371.02  id=ee2e7cac-e720-4933-827e-d85e29850378
13:47:46  INFO        SELL LIMIT filled CIEN (confirmed by position check)
13:47:46  INFO        TX logged: SELL CIEN  P&L 6.04%
13:47:46  INFO        Universe cache hit: 903 tickers (tickers_2026-09-17.json)
13:47:47  INFO        [universe] 40/902 (40 valid)
13:47:48  INFO        [universe] 80/902 (80 valid)
13:47:49  INFO        [universe] 120/902 (120 valid)
13:47:50  INFO        [universe] 160/902 (160 valid)
13:47:51  INFO        [universe] 200/902 (199 valid)
13:47:59  INFO        [universe] 240/902 (238 valid)
13:48:12  INFO        [universe] 280/902 (278 valid)
13:48:25  INFO        [universe] 320/902 (318 valid)
13:48:35  INFO        [universe] 360/902 (358 valid)
13:48:48  INFO        [universe] 400/902 (398 valid)
13:48:59  INFO        [universe] 440/902 (438 valid)
13:49:12  INFO        [universe] 480/902 (478 valid)
13:49:25  INFO        [universe] 520/902 (518 valid)
13:49:35  INFO        [universe] 560/902 (558 valid)
13:49:48  INFO        [universe] 600/902 (598 valid)
13:50:01  INFO        [universe] 640/902 (638 valid)
13:50:11  INFO        [universe] 680/902 (678 valid)
13:50:25  INFO        [universe] 720/902 (718 valid)
13:50:35  INFO        [universe] 760/902 (758 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260917T135159Z

- UTC timestamp: `20260917T135159Z`
- GitHub run: [#10249](https://github.com/28twagg-ops/TradingBot/actions/runs/35229594240)
- Run id: `35229594240`
- Live bot: exit=`0`, duration=`239s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260917T135159Z_live_bot.log`, `logs/action_runs/20260917T135159Z_live_options.log`, `logs/action_runs/20260917T135159Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1270 | 48.3 | -24.6 | +38.0 | $+15,688 |
| TAINTED | 1859 | 33.4 | -39.0 | +12.1 | $-9,274 |
| KEEP-only | 663 | 62.0 | +50.9 | +60.5 | $+10,921 |
| KEEP-only recent | 466 | 59.7 | +53.1 | +68.4 | $+6,276 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T09:26:17.601036-04:00","date":"2026-09-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.58},"signals":0,"placed":0,"equity":996788.34,"open_positions":17,"pending_orders":0,"open_lots":94,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10244","github_run_id":"35226928849","status":"ok","data_quality":{"clean":{"n":1270,"win":48.27,"med":-24.62,"avg":38.03,"pnl":15688.16},"tainted":{"n":1859,"win":33.41,"med":-38.98,"avg":12.07,"pnl":-9274.28},"keep_only":{"n":663,"win":61.99,"med":50.88,"avg":60.45,"pnl":10921.45},"keep_only_recent":{"n":466,"win":59.66,"med":53.09,"avg":68.36,"pnl":6276.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
... (120 earlier lines - see full log file)
|  ETN      Pullback50      eq     $417.88  50.6   -2.63   50MA bounce (+|
|  EOG      Pullback50      eq     $144.82  50.6   -3.14   50MA bounce (+|
|  FDS      Pullback50      eq     $274.95  34.9   -1.90   50MA bounce (-|
|  OKE      Pullback50      eq     $92.59   41.1   -2.88   50MA bounce (-|
|  SLB      Pullback50      eq     $52.68   43.3   -1.77   50MA bounce (+|
|  STLD     Pullback50      eq     $245.04  59.2   -1.99   50MA bounce (+|
|  ARMK     Pullback50      eq     $58.19   46.2   -2.63   50MA bounce (+|
|  FAF      Pullback50      eq     $72.46   42.9   -2.34   50MA bounce (-|
|  GATX     Pullback50      eq     $180.06  53.7   -2.30   50MA bounce (+|
|  JAZZ     Pullback50      eq     $246.72  45.6   -0.92   50MA bounce (-|
|  KEX      Pullback50      eq     $138.27  45.6   -3.38   50MA bounce (-|
|  KRYS     Pullback50      eq     $342.15  38.9   -2.75   50MA bounce (-|
|  MOH      Pullback50      eq     $205.50  56.6   -2.18   50MA bounce (-|
|  RS       Pullback50      eq     $399.87  56.4   -1.92   50MA bounce (-|
|  SITM     Pullback50      eq     $600.62  50.1   -2.24   50MA bounce (+|
|  VICR     Pullback50      eq     $211.26  53.0   -1.85   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] AMP  Pullback50                                    $34.08|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] GLW  Pullback50                                    $34.08|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] ETN  Pullback50                                      cap 3|
|    SKIP [eq] EOG  Pullback50                                      cap 3|13:55:57  INFO        place_all_stops: checking 3 positions...
13:55:57  INFO        STOP skipped AMP: fractional (0.0625 shares) — software exit will handle it
13:55:57  INFO        STOP skipped CTAS: fractional (0.1690 shares) — software exit will handle it
13:55:57  INFO        STOP skipped GLW: fractional (0.2213 shares) — software exit will handle it
13:55:57  INFO        Daily log -> logs/daily/2026-09-17.md
13:55:57  INFO        Dashboard written → logs/dashboard.md

|    SKIP [eq] FDS  Pullback50                                      cap 3|
|    SKIP [eq] OKE  Pullback50                                      cap 3|
|    SKIP [eq] SLB  Pullback50                                      cap 3|
|    SKIP [eq] STLD  Pullback50                                     cap 3|
|    SKIP [eq] ARMK  Pullback50                                     cap 3|
|    SKIP [eq] FAF  Pullback50                                      cap 3|
|    SKIP [eq] GATX  Pullback50                                     cap 3|
|    SKIP [eq] JAZZ  Pullback50                                     cap 3|
|    SKIP [eq] KEX  Pullback50                                      cap 3|
|    SKIP [eq] KRYS  Pullback50                                     cap 3|
|    SKIP [eq] MOH  Pullback50                                      cap 3|
|    SKIP [eq] RS  Pullback50                                       cap 3|
|    SKIP [eq] SITM  Pullback50                                     cap 3|
|    SKIP [eq] VICR  Pullback50                                     cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      2|
+------------------------------------------------------------------------+
|  AMP                                                  still unconfirmed|
|  GLW                                                  still unconfirmed|
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
|  Signals                                                             18|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  2 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $227.02|
|  Cash                                                           $125.54|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-17T09:55:58.792131-04:00 share=25% ===
2026-09-17 09:55:58,792 INFO === options_live_micro LIVE 2026-09-17T09:55:58.792131-04:00 share=25% ===
Live account equity $226.99 cash $125.54 #225458845 options_level=3
2026-09-17 09:55:58,868 INFO Live account equity $226.99 cash $125.54 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 09:55:58,910 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 09:55:58,934 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=89 paper_keys=yes dry_run=False
  alpaca positions=15
  FLAG b860|S408|149b7278 missing from Alpaca
  FLAG b781|S397|86413d79 missing from Alpaca
  FLAG b366|S361|4fa5fa74 missing from Alpaca
  FLAG b101|S211|64be1a51 missing from Alpaca
  FLAG b100|S211|399c668c missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,463.33
  buying_power=$3,935,136.24 cash=$1,030,758.33
  open option orders: 16
    UBER260918C00072000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    MARA260918C00012000 OrderSide.SELL qty=70 status=OrderStatus.NEW limit=0.21
    CRWD260918C00255000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.57
    CRWD260918C00255000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.57
    CRWD260918C00255000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.57
  open option positions: 14
    HON260918C00215000 qty=1 mkt=$0.00
    LLY260918C01225000 qty=1 mkt=$7.00
    MARA260918C00011000 qty=-1 mkt=$-30.00
    MARA260918C00011500 qty=2 mkt=$22.00
    MARA260918C00012000 qty=70 mkt=$280.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-17T09:56:01.996424-04:00 ===

[Run context]
Paper auth OK — equity $996460.33, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b861|lab0861_s408_w3_1045_1120_r2|S408] stop_loss (-100.0%) SELL failed MSTR260918C00157500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-17 09:56:04,185 INFO   EXIT [b408|lab0408_s364_w3_1045_1120_r1|S364] stop_loss (-86.2%) SELL 1 MARA260918C00012000 @<= 0.05
  EXIT [b182|lab0182_s217_w3_1045_1120_r1|S217] stop_loss (-100.0%) SELL failed HON260918C00215000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b783|lab0783_s397_w4_1120_1135_r2|S397] take_profit (+265.1%) SELL failed SNOW260918C00347500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b434|lab0434_s366_w2_1005_1045_r1|S366] stop_loss (-67.8%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b433|lab0433_s366_w1_0928_1005_r2|S366] stop_loss (-67.8%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b432|lab0432_s366_w1_0928_1005_r1|S366] stop_loss (-67.8%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=1 upgraded=0 already=5 failed=4 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260917T135733Z

- UTC timestamp: `20260917T135733Z`
- GitHub run: [#10250](https://github.com/28twagg-ops/TradingBot/actions/runs/35230136168)
- Run id: `35230136168`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260917T135733Z_live_bot.log`, `logs/action_runs/20260917T135733Z_live_options.log`, `logs/action_runs/20260917T135733Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1270 | 48.3 | -24.6 | +38.0 | $+15,688 |
| TAINTED | 1859 | 33.4 | -39.0 | +12.1 | $-9,274 |
| KEEP-only | 663 | 62.0 | +50.9 | +60.5 | $+10,921 |
| KEEP-only recent | 466 | 59.7 | +53.1 | +68.4 | $+6,276 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T09:26:17.601036-04:00","date":"2026-09-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.58},"signals":0,"placed":0,"equity":996788.34,"open_positions":17,"pending_orders":0,"open_lots":94,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10244","github_run_id":"35226928849","status":"ok","data_quality":{"clean":{"n":1270,"win":48.27,"med":-24.62,"avg":38.03,"pnl":15688.16},"tainted":{"n":1859,"win":33.41,"med":-38.98,"avg":12.07,"pnl":-9274.28},"keep_only":{"n":663,"win":61.99,"med":50.88,"avg":60.45,"pnl":10921.45},"keep_only_recent":{"n":466,"win":59.66,"med":53.09,"avg":68.36,"pnl":6276.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:57:36  INFO      Mode: morning_scan
13:57:37  INFO        [positions] 3/3 (3 valid)
13:57:37  INFO        SELL MARKET [urgent] CTAS closed
13:57:39  INFO        TX logged: SELL CTAS  P&L -0.87%
13:57:39  INFO        SELL LIMIT GLW  qty=0.221288369  limit=$153.25  id=7b27519d-0933-492d-a8d7-3db7a8ef55c5
13:58:09  INFO        SELL LIMIT filled GLW (confirmed by position check)
13:58:09  INFO        TX logged: SELL GLW  P&L -0.4%
13:58:09  INFO        Universe cache hit: 903 tickers (tickers_2026-09-17.json)
13:58:10  INFO        [universe] 40/902 (40 valid)
13:58:11  INFO        [universe] 80/902 (80 valid)
13:58:13  INFO        [universe] 120/902 (120 valid)
13:58:14  INFO        [universe] 160/902 (160 valid)
13:58:15  INFO        [universe] 200/902 (199 valid)
13:58:22  INFO        [universe] 240/902 (238 valid)
13:58:35  INFO        [universe] 280/902 (278 valid)
13:58:48  INFO        [universe] 320/902 (318 valid)
13:58:58  INFO        [universe] 360/902 (358 valid)
13:59:11  INFO        [universe] 400/902 (398 valid)
13:59:24  INFO        [universe] 440/902 (438 valid)
13:59:34  INFO        [universe] 480/902 (478 valid)
13:59:47  INFO        [universe] 520/902 (518 valid)
14:00:00  INFO        [universe] 560/902 (558 valid)
14:00:10  INFO        [universe] 600/902 (598 valid)
14:00:23  INFO        [universe] 640/902 (638 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260917T140159Z

- UTC timestamp: `20260917T140159Z`
- GitHub run: [#10251](https://github.com/28twagg-ops/TradingBot/actions/runs/35230670255)
- Run id: `35230670255`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`70s`
- Full logs: `logs/action_runs/20260917T140159Z_live_bot.log`, `logs/action_runs/20260917T140159Z_live_options.log`, `logs/action_runs/20260917T140159Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1273 | 48.2 | -25.0 | +37.8 | $+15,604 |
| TAINTED | 1865 | 33.4 | -39.0 | +12.9 | $-9,309 |
| KEEP-only | 665 | 61.8 | +50.9 | +60.0 | $+10,855 |
| KEEP-only recent | 468 | 59.4 | +53.0 | +67.7 | $+6,210 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T10:02:08.768187-04:00","date":"2026-09-17","mode":"entry+manage","header":"entry+manage (7 new)","elapsed_s":60.5,"phases_s":{"reconcile":0.45,"cancel":0.13,"manage":3.57,"protective_stops":1.54,"scan":35.66,"entries":15.79,"reconcile2":0.6},"signals":94,"placed":7,"equity":996560.81,"open_positions":16,"pending_orders":2,"open_lots":87,"submitted_today":7,"filled_today":11,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S350:CRWD","S351:CRWD","S352:CRWD"],"github_run":"10251","github_run_id":"35230670255","status":"ok","data_quality":{"clean":{"n":1273,"win":48.15,"med":-25.0,"avg":37.76,"pnl":15604.16},"tainted":{"n":1865,"win":33.4,"med":-39.02,"avg":12.92,"pnl":-9309.28},"keep_only":{"n":665,"win":61.8,"med":50.85,"avg":60.04,"pnl":10855.45},"keep_only_recent":{"n":468,"win":59.4,"med":53.0,"avg":67.74,"pnl":6210.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:02:00  INFO      Mode: exits
14:02:00  INFO        Daily log -> logs/daily/2026-09-17.md
14:02:00  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (2 ledger rows)
14:02:00  INFO        place_all_stops: checking 1 positions...
14:02:00  INFO        STOP skipped AMP: fractional (0.0625 shares) — software exit will handle it
14:02:01  INFO        [positions] 1/1 (1 valid)
14:02:01  INFO        SELL MARKET [urgent] AMP closed
14:02:03  INFO        TX logged: SELL AMP  P&L -0.51%
14:02:04  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:02 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.69|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMP  P&L -0.5%  $-0.17                         EXIT: stop_loss (-0.5%)|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  1 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
|  AMP                                         -0.51%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-17T10:02:05.106393-04:00 share=25% ===
2026-09-17 10:02:05,106 INFO === options_live_micro LIVE 2026-09-17T10:02:05.106393-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 10:02:05,306 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 10:02:05,637 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 10:02:05,749 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (198 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    25 | WARN | <<<
| Orphaned lots (post-stable) |  1390 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    87 | INFO |
| Total closed lots           |  2277 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1273 med=-25.0% | TAINTED n=1865 med=-39.0% | KEEP-only n=665 med=+50.9% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T140615Z

- UTC timestamp: `20260917T140615Z`
- GitHub run: [#10252](https://github.com/28twagg-ops/TradingBot/actions/runs/35231223191)
- Run id: `35231223191`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`61s`
- Full logs: `logs/action_runs/20260917T140615Z_live_bot.log`, `logs/action_runs/20260917T140615Z_live_options.log`, `logs/action_runs/20260917T140615Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1273 | 48.2 | -25.0 | +37.8 | $+15,604 |
| TAINTED | 1869 | 33.4 | -39.0 | +13.0 | $-9,297 |
| KEEP-only | 665 | 61.8 | +50.9 | +60.0 | $+10,855 |
| KEEP-only recent | 468 | 59.4 | +53.0 | +67.7 | $+6,210 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T10:06:21.688876-04:00","date":"2026-09-17","mode":"entry+manage","header":"entry+manage (18 new)","elapsed_s":52.9,"phases_s":{"reconcile":0.26,"cancel":0.07,"manage":3.41,"protective_stops":1.06,"scan":27.93,"entries":14.25,"reconcile2":0.87},"signals":94,"placed":18,"equity":996399.11,"open_positions":20,"pending_orders":6,"open_lots":99,"submitted_today":25,"filled_today":25,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S350:CRWD","S351:CRWD","S352:CRWD"],"github_run":"10252","github_run_id":"35231223191","status":"ok","data_quality":{"clean":{"n":1273,"win":48.15,"med":-25.0,"avg":37.76,"pnl":15604.16},"tainted":{"n":1869,"win":33.44,"med":-38.98,"avg":13.02,"pnl":-9297.28},"keep_only":{"n":665,"win":61.8,"med":50.85,"avg":60.04,"pnl":10855.45},"keep_only_recent":{"n":468,"win":59.4,"med":53.0,"avg":67.74,"pnl":6210.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:06:16  INFO      Mode: exits
14:06:17  INFO        Daily log -> logs/daily/2026-09-17.md
14:06:17  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
14:06:17  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T10:06:18.171188-04:00 share=25% ===
2026-09-17 10:06:18,171 INFO === options_live_micro LIVE 2026-09-17T10:06:18.171188-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 10:06:18,293 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 10:06:18,584 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 10:06:18,647 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (205 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    25 | WARN | <<<
| Orphaned lots (post-stable) |  1390 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    99 | INFO |
| Total closed lots           |  2281 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1273 med=-25.0% | TAINTED n=1869 med=-39.0% | KEEP-only n=665 med=+50.9% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T141132Z

- UTC timestamp: `20260917T141132Z`
- GitHub run: [#10253](https://github.com/28twagg-ops/TradingBot/actions/runs/35231763015)
- Run id: `35231763015`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`74s`
- Full logs: `logs/action_runs/20260917T141132Z_live_bot.log`, `logs/action_runs/20260917T141132Z_live_options.log`, `logs/action_runs/20260917T141132Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1274 | 48.1 | -25.6 | +37.7 | $+15,600 |
| TAINTED | 1869 | 33.4 | -39.0 | +13.0 | $-9,297 |
| KEEP-only | 665 | 61.8 | +50.9 | +60.0 | $+10,855 |
| KEEP-only recent | 468 | 59.4 | +53.0 | +67.7 | $+6,210 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T10:11:39.096824-04:00","date":"2026-09-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":63.0,"phases_s":{"reconcile":0.26,"cancel":0.02,"manage":4.56,"protective_stops":0.37,"scan":53.06,"entries":3.56,"reconcile2":0.2},"signals":94,"placed":0,"equity":996301.07,"open_positions":21,"pending_orders":2,"open_lots":102,"submitted_today":25,"filled_today":29,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S350:CRWD","S351:CRWD","S352:CRWD"],"github_run":"10253","github_run_id":"35231763015","status":"ok","data_quality":{"clean":{"n":1274,"win":48.12,"med":-25.61,"avg":37.7,"pnl":15600.16},"tainted":{"n":1869,"win":33.44,"med":-38.98,"avg":13.02,"pnl":-9297.28},"keep_only":{"n":665,"win":61.8,"med":50.85,"avg":60.04,"pnl":10855.45},"keep_only_recent":{"n":468,"win":59.4,"med":53.0,"avg":67.74,"pnl":6210.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:11:35  INFO      Mode: exits
14:11:35  INFO        Daily log -> logs/daily/2026-09-17.md
14:11:35  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
14:11:35  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T10:11:36.439905-04:00 share=25% ===
2026-09-17 10:11:36,439 INFO === options_live_micro LIVE 2026-09-17T10:11:36.439905-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 10:11:36,484 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 10:11:36,508 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 10:11:36,525 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (202 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    25 | WARN | <<<
| Orphaned lots (post-stable) |  1390 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   102 | INFO |
| Total closed lots           |  2282 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1274 med=-25.6% | TAINTED n=1869 med=-39.0% | KEEP-only n=665 med=+50.9% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T141614Z

- UTC timestamp: `20260917T141614Z`
- GitHub run: [#10254](https://github.com/28twagg-ops/TradingBot/actions/runs/35232309168)
- Run id: `35232309168`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`60s`
- Full logs: `logs/action_runs/20260917T141614Z_live_bot.log`, `logs/action_runs/20260917T141614Z_live_options.log`, `logs/action_runs/20260917T141614Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1274 | 48.1 | -25.6 | +37.7 | $+15,600 |
| TAINTED | 1869 | 33.4 | -39.0 | +13.0 | $-9,297 |
| KEEP-only | 665 | 61.8 | +50.9 | +60.0 | $+10,855 |
| KEEP-only recent | 468 | 59.4 | +53.0 | +67.7 | $+6,210 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T10:16:20.865710-04:00","date":"2026-09-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":52.4,"phases_s":{"reconcile":0.64,"cancel":0.13,"manage":6.58,"protective_stops":2.19,"scan":23.43,"entries":16.01,"reconcile2":0.4},"signals":94,"placed":0,"equity":996498.05,"open_positions":21,"pending_orders":2,"open_lots":102,"submitted_today":25,"filled_today":29,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S350:CRWD","S351:CRWD","S352:CRWD"],"github_run":"10254","github_run_id":"35232309168","status":"ok","data_quality":{"clean":{"n":1274,"win":48.12,"med":-25.61,"avg":37.7,"pnl":15600.16},"tainted":{"n":1869,"win":33.44,"med":-38.98,"avg":13.02,"pnl":-9297.28},"keep_only":{"n":665,"win":61.8,"med":50.85,"avg":60.04,"pnl":10855.45},"keep_only_recent":{"n":468,"win":59.4,"med":53.0,"avg":67.74,"pnl":6210.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:16:15  INFO      Mode: exits
14:16:16  INFO        Daily log -> logs/daily/2026-09-17.md
14:16:16  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
14:16:16  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T10:16:17.290972-04:00 share=25% ===
2026-09-17 10:16:17,291 INFO === options_live_micro LIVE 2026-09-17T10:16:17.290972-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 10:16:17,504 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 10:16:17,971 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 10:16:18,085 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (200 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    25 | WARN | <<<
| Orphaned lots (post-stable) |  1390 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   102 | INFO |
| Total closed lots           |  2282 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1274 med=-25.6% | TAINTED n=1869 med=-39.0% | KEEP-only n=665 med=+50.9% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T142114Z

- UTC timestamp: `20260917T142114Z`
- GitHub run: [#10255](https://github.com/28twagg-ops/TradingBot/actions/runs/35232850755)
- Run id: `35232850755`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`99s`
- Full logs: `logs/action_runs/20260917T142114Z_live_bot.log`, `logs/action_runs/20260917T142114Z_live_options.log`, `logs/action_runs/20260917T142114Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1275 | 48.1 | -26.2 | +37.6 | $+15,598 |
| TAINTED | 1869 | 33.4 | -39.0 | +13.0 | $-9,297 |
| KEEP-only | 666 | 61.7 | +50.4 | +59.9 | $+10,853 |
| KEEP-only recent | 469 | 59.3 | +52.9 | +67.5 | $+6,208 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T10:21:22.452108-04:00","date":"2026-09-17","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":86.7,"phases_s":{"reconcile":0.51,"cancel":0.15,"manage":8.53,"protective_stops":2.71,"scan":53.64,"entries":17.32,"reconcile2":0.48},"signals":94,"placed":2,"equity":996574.53,"open_positions":21,"pending_orders":4,"open_lots":101,"submitted_today":27,"filled_today":29,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S350:CRWD","S351:CRWD","S352:CRWD"],"github_run":"10255","github_run_id":"35232850755","status":"ok","data_quality":{"clean":{"n":1275,"win":48.08,"med":-26.23,"avg":37.63,"pnl":15598.16},"tainted":{"n":1869,"win":33.44,"med":-38.98,"avg":13.02,"pnl":-9297.28},"keep_only":{"n":666,"win":61.71,"med":50.43,"avg":59.88,"pnl":10853.45},"keep_only_recent":{"n":469,"win":59.28,"med":52.94,"avg":67.49,"pnl":6208.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:21:15  INFO      Mode: exits
14:21:16  INFO        Daily log -> logs/daily/2026-09-17.md
14:21:16  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
14:21:17  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T10:21:18.464367-04:00 share=25% ===
2026-09-17 10:21:18,464 INFO === options_live_micro LIVE 2026-09-17T10:21:18.464367-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 10:21:18,689 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 10:21:18,894 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 10:21:19,032 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (199 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    25 | WARN | <<<
| Orphaned lots (post-stable) |  1390 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   101 | INFO |
| Total closed lots           |  2283 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1275 med=-26.2% | TAINTED n=1869 med=-39.0% | KEEP-only n=666 med=+50.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T142615Z

- UTC timestamp: `20260917T142615Z`
- GitHub run: [#10256](https://github.com/28twagg-ops/TradingBot/actions/runs/35233407974)
- Run id: `35233407974`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`100s`
- Full logs: `logs/action_runs/20260917T142615Z_live_bot.log`, `logs/action_runs/20260917T142615Z_live_options.log`, `logs/action_runs/20260917T142615Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1278 | 48.2 | -25.0 | +37.7 | $+15,718 |
| TAINTED | 1869 | 33.4 | -39.0 | +13.0 | $-9,297 |
| KEEP-only | 668 | 61.8 | +50.9 | +59.9 | $+10,917 |
| KEEP-only recent | 471 | 59.4 | +53.1 | +67.6 | $+6,272 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T10:26:24.616271-04:00","date":"2026-09-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":87.6,"phases_s":{"reconcile":0.51,"cancel":0.16,"manage":9.73,"protective_stops":3.4,"scan":53.46,"entries":16.43,"reconcile2":0.75},"signals":94,"placed":0,"equity":996871.03,"open_positions":20,"pending_orders":4,"open_lots":98,"submitted_today":27,"filled_today":29,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S350:CRWD","S351:CRWD","S352:CRWD"],"github_run":"10256","github_run_id":"35233407974","status":"ok","data_quality":{"clean":{"n":1278,"win":48.2,"med":-25.0,"avg":37.74,"pnl":15718.16},"tainted":{"n":1869,"win":33.44,"med":-38.98,"avg":13.02,"pnl":-9297.28},"keep_only":{"n":668,"win":61.83,"med":50.87,"avg":59.95,"pnl":10917.45},"keep_only_recent":{"n":471,"win":59.45,"med":53.06,"avg":67.56,"pnl":6272.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:26:17  INFO      Mode: exits
14:26:19  INFO        Daily log -> logs/daily/2026-09-17.md
14:26:19  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
14:26:19  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T10:26:20.425014-04:00 share=25% ===
2026-09-17 10:26:20,425 INFO === options_live_micro LIVE 2026-09-17T10:26:20.425014-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 10:26:21,020 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 10:26:21,225 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 10:26:21,364 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (206 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    25 | WARN | <<<
| Orphaned lots (post-stable) |  1390 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    98 | INFO |
| Total closed lots           |  2286 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1278 med=-25.0% | TAINTED n=1869 med=-39.0% | KEEP-only n=668 med=+50.9% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T143111Z

- UTC timestamp: `20260917T143111Z`
- GitHub run: [#10257](https://github.com/28twagg-ops/TradingBot/actions/runs/35233971450)
- Run id: `35233971450`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`69s`
- Full logs: `logs/action_runs/20260917T143111Z_live_bot.log`, `logs/action_runs/20260917T143111Z_live_options.log`, `logs/action_runs/20260917T143111Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1278 | 48.2 | -25.0 | +37.7 | $+15,718 |
| TAINTED | 1869 | 33.4 | -39.0 | +13.0 | $-9,297 |
| KEEP-only | 668 | 61.8 | +50.9 | +59.9 | $+10,917 |
| KEEP-only recent | 471 | 59.4 | +53.1 | +67.6 | $+6,272 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T10:31:17.159111-04:00","date":"2026-09-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":57.2,"phases_s":{"reconcile":0.16,"cancel":0.03,"manage":5.0,"protective_stops":0.43,"scan":45.54,"entries":5.06,"reconcile2":0.17},"signals":94,"placed":0,"equity":996984.97,"open_positions":20,"pending_orders":4,"open_lots":98,"submitted_today":27,"filled_today":29,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S350:CRWD","S351:CRWD","S352:CRWD"],"github_run":"10257","github_run_id":"35233971450","status":"ok","data_quality":{"clean":{"n":1278,"win":48.2,"med":-25.0,"avg":37.74,"pnl":15718.16},"tainted":{"n":1869,"win":33.44,"med":-38.98,"avg":13.02,"pnl":-9297.28},"keep_only":{"n":668,"win":61.83,"med":50.87,"avg":59.95,"pnl":10917.45},"keep_only_recent":{"n":471,"win":59.45,"med":53.06,"avg":67.56,"pnl":6272.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:31:12  INFO      Mode: exits
14:31:13  INFO        Daily log -> logs/daily/2026-09-17.md
14:31:13  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
14:31:13  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T10:31:14.278395-04:00 share=25% ===
2026-09-17 10:31:14,278 INFO === options_live_micro LIVE 2026-09-17T10:31:14.278395-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 10:31:14,336 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 10:31:14,436 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 10:31:14,455 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (206 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    25 | WARN | <<<
| Orphaned lots (post-stable) |  1390 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    98 | INFO |
| Total closed lots           |  2286 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1278 med=-25.0% | TAINTED n=1869 med=-39.0% | KEEP-only n=668 med=+50.9% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T143626Z

- UTC timestamp: `20260917T143626Z`
- GitHub run: [#10258](https://github.com/28twagg-ops/TradingBot/actions/runs/35234536593)
- Run id: `35234536593`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`73s`
- Full logs: `logs/action_runs/20260917T143626Z_live_bot.log`, `logs/action_runs/20260917T143626Z_live_options.log`, `logs/action_runs/20260917T143626Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1283 | 48.4 | -24.1 | +38.0 | $+15,944 |
| TAINTED | 1869 | 33.4 | -39.0 | +13.0 | $-9,297 |
| KEEP-only | 672 | 62.1 | +51.0 | +60.2 | $+11,068 |
| KEEP-only recent | 475 | 59.8 | +53.2 | +67.9 | $+6,423 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T10:36:34.823224-04:00","date":"2026-09-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":62.9,"phases_s":{"reconcile":0.5,"cancel":0.13,"manage":6.51,"protective_stops":2.13,"scan":36.13,"entries":14.02,"reconcile2":0.57},"signals":94,"placed":0,"equity":996972.93,"open_positions":19,"pending_orders":4,"open_lots":93,"submitted_today":27,"filled_today":29,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S350:CRWD","S351:CRWD","S352:CRWD"],"github_run":"10258","github_run_id":"35234536593","status":"ok","data_quality":{"clean":{"n":1283,"win":48.4,"med":-24.14,"avg":38.02,"pnl":15944.16},"tainted":{"n":1869,"win":33.44,"med":-38.98,"avg":13.02,"pnl":-9297.28},"keep_only":{"n":672,"win":62.05,"med":50.96,"avg":60.24,"pnl":11068.45},"keep_only_recent":{"n":475,"win":59.79,"med":53.23,"avg":67.9,"pnl":6423.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
14:36:27  INFO      Mode: exits
14:36:29  INFO        Daily log -> logs/daily/2026-09-17.md
14:36:29  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
14:36:29  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T10:36:30.654262-04:00 share=25% ===
2026-09-17 10:36:30,654 INFO === options_live_micro LIVE 2026-09-17T10:36:30.654262-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 10:36:30,883 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 10:36:31,172 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 10:36:31,292 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (204 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    25 | WARN | <<<
| Orphaned lots (post-stable) |  1390 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    93 | INFO |
| Total closed lots           |  2291 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1283 med=-24.1% | TAINTED n=1869 med=-39.0% | KEEP-only n=672 med=+51.0% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T144109Z

- UTC timestamp: `20260917T144109Z`
- GitHub run: [#10259](https://github.com/28twagg-ops/TradingBot/actions/runs/35235098118)
- Run id: `35235098118`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`51s`
- Full logs: `logs/action_runs/20260917T144109Z_live_bot.log`, `logs/action_runs/20260917T144109Z_live_options.log`, `logs/action_runs/20260917T144109Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1284 | 48.4 | -23.7 | +38.1 | $+15,994 |
| TAINTED | 1869 | 33.4 | -39.0 | +13.0 | $-9,297 |
| KEEP-only | 673 | 62.1 | +51.0 | +60.3 | $+11,118 |
| KEEP-only recent | 476 | 59.9 | +53.3 | +67.9 | $+6,473 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T10:41:17.438576-04:00","date":"2026-09-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":42.5,"phases_s":{"reconcile":0.34,"cancel":0.08,"manage":4.54,"protective_stops":1.29,"scan":24.59,"entries":9.49,"reconcile2":0.32},"signals":94,"placed":0,"equity":996986.87,"open_positions":19,"pending_orders":4,"open_lots":92,"submitted_today":27,"filled_today":29,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S350:CRWD","S351:CRWD","S352:CRWD"],"github_run":"10259","github_run_id":"35235098118","status":"ok","data_quality":{"clean":{"n":1284,"win":48.44,"med":-23.71,"avg":38.05,"pnl":15994.16},"tainted":{"n":1869,"win":33.44,"med":-38.98,"avg":13.02,"pnl":-9297.28},"keep_only":{"n":673,"win":62.11,"med":50.98,"avg":60.26,"pnl":11118.45},"keep_only_recent":{"n":476,"win":59.87,"med":53.28,"avg":67.92,"pnl":6473.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
14:41:11  INFO      Mode: exits
14:41:11  INFO        Daily log -> logs/daily/2026-09-17.md
14:41:11  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
14:41:11  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T10:41:13.170701-04:00 share=25% ===
2026-09-17 10:41:13,170 INFO === options_live_micro LIVE 2026-09-17T10:41:13.170701-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 10:41:13,298 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 10:41:13,913 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 10:41:13,973 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (204 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    25 | WARN | <<<
| Orphaned lots (post-stable) |  1390 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    92 | INFO |
| Total closed lots           |  2292 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1284 med=-23.7% | TAINTED n=1869 med=-39.0% | KEEP-only n=673 med=+51.0% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T144716Z

- UTC timestamp: `20260917T144716Z`
- GitHub run: [#10260](https://github.com/28twagg-ops/TradingBot/actions/runs/35235662692)
- Run id: `35235662692`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`80s`
- Full logs: `logs/action_runs/20260917T144716Z_live_bot.log`, `logs/action_runs/20260917T144716Z_live_options.log`, `logs/action_runs/20260917T144716Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1285 | 48.4 | -24.1 | +38.0 | $+15,952 |
| TAINTED | 1869 | 33.4 | -39.0 | +13.0 | $-9,297 |
| KEEP-only | 659 | 62.4 | +51.0 | +61.4 | $+11,197 |
| KEEP-only recent | 462 | 60.2 | +53.3 | +69.8 | $+6,552 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T10:47:22.261331-04:00","date":"2026-09-17","mode":"entry+manage","header":"entry+manage (13 new)","elapsed_s":68.2,"phases_s":{"reconcile":0.18,"cancel":0.02,"manage":2.24,"protective_stops":0.41,"scan":53.53,"entries":4.52,"reconcile2":0.27},"signals":94,"placed":13,"equity":997117.33,"open_positions":21,"pending_orders":13,"open_lots":95,"submitted_today":40,"filled_today":33,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S350:CRWD","S351:CRWD","S352:CRWD"],"github_run":"10260","github_run_id":"35235662692","status":"ok","data_quality":{"clean":{"n":1285,"win":48.4,"med":-24.14,"avg":37.95,"pnl":15952.16},"tainted":{"n":1869,"win":33.44,"med":-38.98,"avg":13.02,"pnl":-9297.28},"keep_only":{"n":659,"win":62.37,"med":50.98,"avg":61.41,"pnl":11197.45},"keep_only_recent":{"n":462,"win":60.17,"med":53.33,"avg":69.8,"pnl":6552.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
14:47:18  INFO      Mode: exits
14:47:18  INFO        Daily log -> logs/daily/2026-09-17.md
14:47:18  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
14:47:18  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:47 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T10:47:19.328509-04:00 share=25% ===
2026-09-17 10:47:19,328 INFO === options_live_micro LIVE 2026-09-17T10:47:19.328509-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 10:47:19,374 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 10:47:19,452 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 10:47:19,467 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (209 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    24 | WARN | <<<
| Orphaned lots (post-stable) |  1389 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    95 | INFO |
| Total closed lots           |  2293 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1285 med=-24.1% | TAINTED n=1869 med=-39.0% | KEEP-only n=659 med=+51.0% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T145114Z

- UTC timestamp: `20260917T145114Z`
- GitHub run: [#10261](https://github.com/28twagg-ops/TradingBot/actions/runs/35236221094)
- Run id: `35236221094`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`75s`
- Full logs: `logs/action_runs/20260917T145114Z_live_bot.log`, `logs/action_runs/20260917T145114Z_live_options.log`, `logs/action_runs/20260917T145114Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1286 | 48.4 | -24.2 | +37.9 | $+15,912 |
| TAINTED | 1869 | 33.4 | -39.0 | +13.0 | $-9,297 |
| KEEP-only | 659 | 62.4 | +51.0 | +61.4 | $+11,197 |
| KEEP-only recent | 462 | 60.2 | +53.3 | +69.8 | $+6,552 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T10:51:20.084549-04:00","date":"2026-09-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":63.2,"phases_s":{"reconcile":0.15,"cancel":0.02,"manage":4.08,"protective_stops":0.45,"scan":54.4,"entries":2.98,"reconcile2":0.1},"signals":94,"placed":0,"equity":997119.69,"open_positions":21,"pending_orders":13,"open_lots":94,"submitted_today":40,"filled_today":33,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S350:CRWD","S351:CRWD","S352:CRWD"],"github_run":"10261","github_run_id":"35236221094","status":"ok","data_quality":{"clean":{"n":1286,"win":48.37,"med":-24.19,"avg":37.86,"pnl":15912.16},"tainted":{"n":1869,"win":33.44,"med":-38.98,"avg":13.02,"pnl":-9297.28},"keep_only":{"n":659,"win":62.37,"med":50.98,"avg":61.41,"pnl":11197.45},"keep_only_recent":{"n":462,"win":60.17,"med":53.33,"avg":69.8,"pnl":6552.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
14:51:15  INFO      Mode: exits
14:51:15  INFO        Daily log -> logs/daily/2026-09-17.md
14:51:15  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
14:51:15  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T10:51:17.191586-04:00 share=25% ===
2026-09-17 10:51:17,191 INFO === options_live_micro LIVE 2026-09-17T10:51:17.191586-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 10:51:17,233 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 10:51:17,287 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 10:51:17,301 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (271 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    23 | WARN | <<<
| Orphaned lots (post-stable) |  1388 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    94 | INFO |
| Total closed lots           |  2294 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1286 med=-24.2% | TAINTED n=1869 med=-39.0% | KEEP-only n=659 med=+51.0% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T145613Z

- UTC timestamp: `20260917T145613Z`
- GitHub run: [#10262](https://github.com/28twagg-ops/TradingBot/actions/runs/35236775473)
- Run id: `35236775473`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`57s`
- Full logs: `logs/action_runs/20260917T145613Z_live_bot.log`, `logs/action_runs/20260917T145613Z_live_options.log`, `logs/action_runs/20260917T145613Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1287 | 48.3 | -24.2 | +37.8 | $+15,873 |
| TAINTED | 1870 | 33.4 | -38.9 | +13.0 | $-9,300 |
| KEEP-only | 660 | 62.3 | +51.0 | +61.2 | $+11,158 |
| KEEP-only recent | 463 | 60.0 | +53.3 | +69.5 | $+6,513 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T10:56:18.785651-04:00","date":"2026-09-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":49.9,"phases_s":{"reconcile":0.52,"cancel":0.14,"manage":6.06,"protective_stops":2.74,"scan":23.24,"entries":13.58,"reconcile2":0.43},"signals":94,"placed":0,"equity":997170.07,"open_positions":23,"pending_orders":9,"open_lots":97,"submitted_today":40,"filled_today":37,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S350:CRWD","S351:CRWD","S352:CRWD"],"github_run":"10262","github_run_id":"35236775473","status":"ok","data_quality":{"clean":{"n":1287,"win":48.33,"med":-24.24,"avg":37.76,"pnl":15873.16},"tainted":{"n":1870,"win":33.42,"med":-38.9,"avg":13.01,"pnl":-9300.28},"keep_only":{"n":660,"win":62.27,"med":50.96,"avg":61.19,"pnl":11158.45},"keep_only_recent":{"n":463,"win":60.04,"med":53.33,"avg":69.47,"pnl":6513.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
14:56:14  INFO      Mode: exits
14:56:15  INFO        Daily log -> logs/daily/2026-09-17.md
14:56:15  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
14:56:15  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T10:56:16.195020-04:00 share=25% ===
2026-09-17 10:56:16,195 INFO === options_live_micro LIVE 2026-09-17T10:56:16.195020-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 10:56:16,395 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 10:56:16,564 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 10:56:16,674 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (204 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    22 | WARN | <<<
| Orphaned lots (post-stable) |  1387 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |    97 | INFO |
| Total closed lots           |  2296 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1287 med=-24.2% | TAINTED n=1870 med=-38.9% | KEEP-only n=660 med=+51.0% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T150133Z

- UTC timestamp: `20260917T150133Z`
- GitHub run: [#10263](https://github.com/28twagg-ops/TradingBot/actions/runs/35237324434)
- Run id: `35237324434`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`76s`
- Full logs: `logs/action_runs/20260917T150133Z_live_bot.log`, `logs/action_runs/20260917T150133Z_live_options.log`, `logs/action_runs/20260917T150133Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1287 | 48.3 | -24.2 | +37.8 | $+15,873 |
| TAINTED | 1871 | 33.4 | -39.0 | +13.0 | $-9,325 |
| KEEP-only | 660 | 62.3 | +51.0 | +61.2 | $+11,158 |
| KEEP-only recent | 463 | 60.0 | +53.3 | +69.5 | $+6,513 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T11:01:39.629692-04:00","date":"2026-09-17","mode":"entry+manage","header":"entry+manage (4 new)","elapsed_s":64.7,"phases_s":{"reconcile":0.11,"cancel":0.03,"manage":5.61,"protective_stops":0.74,"scan":52.34,"entries":4.4,"reconcile2":0.3},"signals":94,"placed":4,"equity":997005.55,"open_positions":23,"pending_orders":11,"open_lots":99,"submitted_today":44,"filled_today":39,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S350:CRWD","S351:CRWD","S352:CRWD"],"github_run":"10263","github_run_id":"35237324434","status":"ok","data_quality":{"clean":{"n":1287,"win":48.33,"med":-24.24,"avg":37.76,"pnl":15873.16},"tainted":{"n":1871,"win":33.4,"med":-38.98,"avg":12.98,"pnl":-9325.28},"keep_only":{"n":660,"win":62.27,"med":50.96,"avg":61.19,"pnl":11158.45},"keep_only_recent":{"n":463,"win":60.04,"med":53.33,"avg":69.47,"pnl":6513.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
15:01:34  INFO      Mode: exits
15:01:35  INFO        Daily log -> logs/daily/2026-09-17.md
15:01:35  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
15:01:35  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T11:01:36.622590-04:00 share=25% ===
2026-09-17 11:01:36,622 INFO === options_live_micro LIVE 2026-09-17T11:01:36.622590-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 11:01:36,683 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 11:01:36,772 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 11:01:36,795 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (273 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    22 | WARN | <<<
| Orphaned lots (post-stable) |  1387 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |    99 | INFO |
| Total closed lots           |  2297 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1287 med=-24.2% | TAINTED n=1871 med=-39.0% | KEEP-only n=660 med=+51.0% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T150627Z

- UTC timestamp: `20260917T150627Z`
- GitHub run: [#10264](https://github.com/28twagg-ops/TradingBot/actions/runs/35237886828)
- Run id: `35237886828`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`100s`
- Full logs: `logs/action_runs/20260917T150627Z_live_bot.log`, `logs/action_runs/20260917T150627Z_live_options.log`, `logs/action_runs/20260917T150627Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1287 | 48.3 | -24.2 | +37.8 | $+15,873 |
| TAINTED | 1871 | 33.4 | -39.0 | +13.0 | $-9,325 |
| KEEP-only | 660 | 62.3 | +51.0 | +61.2 | $+11,158 |
| KEEP-only recent | 463 | 60.0 | +53.3 | +69.5 | $+6,513 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T11:06:34.917800-04:00","date":"2026-09-17","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":89.0,"phases_s":{"reconcile":0.74,"cancel":0.13,"manage":15.63,"protective_stops":2.64,"scan":53.39,"entries":12.74,"reconcile2":0.42},"signals":94,"placed":1,"equity":996748.78,"open_positions":24,"pending_orders":5,"open_lots":106,"submitted_today":45,"filled_today":46,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S350:CRWD","S351:CRWD","S352:CRWD"],"github_run":"10264","github_run_id":"35237886828","status":"ok","data_quality":{"clean":{"n":1287,"win":48.33,"med":-24.24,"avg":37.76,"pnl":15873.16},"tainted":{"n":1871,"win":33.4,"med":-38.98,"avg":12.98,"pnl":-9325.28},"keep_only":{"n":660,"win":62.27,"med":50.96,"avg":61.19,"pnl":11158.45},"keep_only_recent":{"n":463,"win":60.04,"med":53.33,"avg":69.47,"pnl":6513.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
15:06:29  INFO      Mode: exits
15:06:30  INFO        Daily log -> logs/daily/2026-09-17.md
15:06:30  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
15:06:30  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T11:06:31.487589-04:00 share=25% ===
2026-09-17 11:06:31,487 INFO === options_live_micro LIVE 2026-09-17T11:06:31.487589-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 11:06:31,691 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 11:06:31,866 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 11:06:31,982 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (272 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    22 | WARN | <<<
| Orphaned lots (post-stable) |  1387 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   106 | INFO |
| Total closed lots           |  2297 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1287 med=-24.2% | TAINTED n=1871 med=-39.0% | KEEP-only n=660 med=+51.0% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T151105Z

- UTC timestamp: `20260917T151105Z`
- GitHub run: [#10265](https://github.com/28twagg-ops/TradingBot/actions/runs/35238433150)
- Run id: `35238433150`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`75s`
- Full logs: `logs/action_runs/20260917T151105Z_live_bot.log`, `logs/action_runs/20260917T151105Z_live_options.log`, `logs/action_runs/20260917T151105Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1287 | 48.3 | -24.2 | +37.8 | $+15,873 |
| TAINTED | 1871 | 33.4 | -39.0 | +13.0 | $-9,325 |
| KEEP-only | 660 | 62.3 | +51.0 | +61.2 | $+11,158 |
| KEEP-only recent | 463 | 60.0 | +53.3 | +69.5 | $+6,513 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T11:11:11.186745-04:00","date":"2026-09-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":63.1,"phases_s":{"reconcile":0.12,"cancel":0.03,"manage":5.3,"protective_stops":0.47,"scan":52.15,"entries":3.65,"reconcile2":0.21},"signals":94,"placed":0,"equity":996697.79,"open_positions":24,"pending_orders":5,"open_lots":106,"submitted_today":45,"filled_today":46,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S350:CRWD","S351:CRWD","S352:CRWD"],"github_run":"10265","github_run_id":"35238433150","status":"ok","data_quality":{"clean":{"n":1287,"win":48.33,"med":-24.24,"avg":37.76,"pnl":15873.16},"tainted":{"n":1871,"win":33.4,"med":-38.98,"avg":12.98,"pnl":-9325.28},"keep_only":{"n":660,"win":62.27,"med":50.96,"avg":61.19,"pnl":11158.45},"keep_only_recent":{"n":463,"win":60.04,"med":53.33,"avg":69.47,"pnl":6513.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
15:11:06  INFO      Mode: exits
15:11:06  INFO        Daily log -> logs/daily/2026-09-17.md
15:11:06  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
15:11:07  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T11:11:08.396722-04:00 share=25% ===
2026-09-17 11:11:08,396 INFO === options_live_micro LIVE 2026-09-17T11:11:08.396722-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 11:11:08,439 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 11:11:08,504 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 11:11:08,517 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (272 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    22 | WARN | <<<
| Orphaned lots (post-stable) |  1387 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   106 | INFO |
| Total closed lots           |  2297 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1287 med=-24.2% | TAINTED n=1871 med=-39.0% | KEEP-only n=660 med=+51.0% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T151608Z

- UTC timestamp: `20260917T151608Z`
- GitHub run: [#10266](https://github.com/28twagg-ops/TradingBot/actions/runs/35238985322)
- Run id: `35238985322`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`75s`
- Full logs: `logs/action_runs/20260917T151608Z_live_bot.log`, `logs/action_runs/20260917T151608Z_live_options.log`, `logs/action_runs/20260917T151608Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1288 | 48.3 | -24.6 | +37.7 | $+15,831 |
| TAINTED | 1871 | 33.4 | -39.0 | +13.0 | $-9,325 |
| KEEP-only | 624 | 63.0 | +51.2 | +62.5 | $+10,696 |
| KEEP-only recent | 435 | 61.6 | +53.3 | +74.0 | $+6,681 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T11:16:16.350660-04:00","date":"2026-09-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":63.0,"phases_s":{"reconcile":0.16,"cancel":0.02,"manage":4.04,"protective_stops":0.42,"scan":53.68,"entries":3.43,"reconcile2":0.15},"signals":94,"placed":0,"equity":996542.85,"open_positions":24,"pending_orders":5,"open_lots":105,"submitted_today":45,"filled_today":46,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S350:CRWD","S351:CRWD","S352:CRWD"],"github_run":"10266","github_run_id":"35238985322","status":"ok","data_quality":{"clean":{"n":1288,"win":48.29,"med":-24.62,"avg":37.67,"pnl":15831.16},"tainted":{"n":1871,"win":33.4,"med":-38.98,"avg":12.98,"pnl":-9325.28},"keep_only":{"n":624,"win":62.98,"med":51.18,"avg":62.53,"pnl":10696.45},"keep_only_recent":{"n":435,"win":61.61,"med":53.33,"avg":74.04,"pnl":6681.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
15:16:12  INFO      Mode: exits
15:16:12  INFO        Daily log -> logs/daily/2026-09-17.md
15:16:12  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
15:16:12  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T11:16:13.238302-04:00 share=25% ===
2026-09-17 11:16:13,238 INFO === options_live_micro LIVE 2026-09-17T11:16:13.238302-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 11:16:13,402 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 11:16:13,422 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 11:16:13,435 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (208 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    21 | WARN | <<<
| Orphaned lots (post-stable) |  1386 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   105 | INFO |
| Total closed lots           |  2298 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1288 med=-24.6% | TAINTED n=1871 med=-39.0% | KEEP-only n=624 med=+51.2% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T152109Z

- UTC timestamp: `20260917T152109Z`
- GitHub run: [#10267](https://github.com/28twagg-ops/TradingBot/actions/runs/35239537596)
- Run id: `35239537596`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`102s`
- Full logs: `logs/action_runs/20260917T152109Z_live_bot.log`, `logs/action_runs/20260917T152109Z_live_options.log`, `logs/action_runs/20260917T152109Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1288 | 48.3 | -24.6 | +37.7 | $+15,831 |
| TAINTED | 1871 | 33.4 | -39.0 | +13.0 | $-9,325 |
| KEEP-only | 624 | 63.0 | +51.2 | +62.5 | $+10,696 |
| KEEP-only recent | 435 | 61.6 | +53.3 | +74.0 | $+6,681 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T11:21:16.509201-04:00","date":"2026-09-17","mode":"entry+manage","header":"entry+manage (7 new)","elapsed_s":90.5,"phases_s":{"reconcile":0.52,"cancel":0.12,"manage":14.58,"protective_stops":2.61,"scan":53.54,"entries":14.82,"reconcile2":0.69},"signals":94,"placed":7,"equity":996647.7,"open_positions":26,"pending_orders":4,"open_lots":113,"submitted_today":52,"filled_today":54,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S350:CRWD","S351:CRWD","S352:CRWD"],"github_run":"10267","github_run_id":"35239537596","status":"ok","data_quality":{"clean":{"n":1288,"win":48.29,"med":-24.62,"avg":37.67,"pnl":15831.16},"tainted":{"n":1871,"win":33.4,"med":-38.98,"avg":12.98,"pnl":-9325.28},"keep_only":{"n":624,"win":62.98,"med":51.18,"avg":62.53,"pnl":10696.45},"keep_only_recent":{"n":435,"win":61.61,"med":53.33,"avg":74.04,"pnl":6681.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
15:21:10  INFO      Mode: exits
15:21:11  INFO        Daily log -> logs/daily/2026-09-17.md
15:21:11  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
15:21:11  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T11:21:12.962356-04:00 share=25% ===
2026-09-17 11:21:12,962 INFO === options_live_micro LIVE 2026-09-17T11:21:12.962356-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 11:21:13,172 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 11:21:13,347 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 11:21:13,462 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (283 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    21 | WARN | <<<
| Orphaned lots (post-stable) |  1386 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   113 | INFO |
| Total closed lots           |  2298 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1288 med=-24.6% | TAINTED n=1871 med=-39.0% | KEEP-only n=624 med=+51.2% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T152610Z

- UTC timestamp: `20260917T152610Z`
- GitHub run: [#10268](https://github.com/28twagg-ops/TradingBot/actions/runs/35240087215)
- Run id: `35240087215`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`72s`
- Full logs: `logs/action_runs/20260917T152610Z_live_bot.log`, `logs/action_runs/20260917T152610Z_live_options.log`, `logs/action_runs/20260917T152610Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1288 | 48.3 | -24.6 | +37.7 | $+15,831 |
| TAINTED | 1871 | 33.4 | -39.0 | +13.0 | $-9,325 |
| KEEP-only | 624 | 63.0 | +51.2 | +62.5 | $+10,696 |
| KEEP-only recent | 435 | 61.6 | +53.3 | +74.0 | $+6,681 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T11:26:18.655404-04:00","date":"2026-09-17","mode":"entry+manage","header":"entry+manage (7 new)","elapsed_s":59.2,"phases_s":{"reconcile":0.23,"cancel":0.05,"manage":5.07,"protective_stops":0.91,"scan":46.16,"entries":4.78,"reconcile2":0.25},"signals":94,"placed":7,"equity":996584.02,"open_positions":26,"pending_orders":11,"open_lots":113,"submitted_today":59,"filled_today":54,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S350:CRWD","S351:CRWD","S352:CRWD"],"github_run":"10268","github_run_id":"35240087215","status":"ok","data_quality":{"clean":{"n":1288,"win":48.29,"med":-24.62,"avg":37.67,"pnl":15831.16},"tainted":{"n":1871,"win":33.4,"med":-38.98,"avg":12.98,"pnl":-9325.28},"keep_only":{"n":624,"win":62.98,"med":51.18,"avg":62.53,"pnl":10696.45},"keep_only_recent":{"n":435,"win":61.61,"med":53.33,"avg":74.04,"pnl":6681.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
15:26:13  INFO      Mode: exits
15:26:13  INFO        Daily log -> logs/daily/2026-09-17.md
15:26:13  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
15:26:14  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T11:26:15.050364-04:00 share=25% ===
2026-09-17 11:26:15,050 INFO === options_live_micro LIVE 2026-09-17T11:26:15.050364-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 11:26:15,144 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 11:26:15,509 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 11:26:15,554 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (207 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    21 | WARN | <<<
| Orphaned lots (post-stable) |  1386 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   113 | INFO |
| Total closed lots           |  2298 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1288 med=-24.6% | TAINTED n=1871 med=-39.0% | KEEP-only n=624 med=+51.2% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T153110Z

- UTC timestamp: `20260917T153110Z`
- GitHub run: [#10269](https://github.com/28twagg-ops/TradingBot/actions/runs/35240638842)
- Run id: `35240638842`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`69s`
- Full logs: `logs/action_runs/20260917T153110Z_live_bot.log`, `logs/action_runs/20260917T153110Z_live_options.log`, `logs/action_runs/20260917T153110Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1289 | 48.3 | -25.0 | +37.6 | $+15,791 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 600 | 63.5 | +51.2 | +64.2 | $+10,475 |
| KEEP-only recent | 417 | 62.8 | +54.0 | +78.1 | $+6,865 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T11:31:16.925274-04:00","date":"2026-09-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":59.4,"phases_s":{"reconcile":1.36,"cancel":0.12,"manage":7.47,"protective_stops":2.5,"scan":35.05,"entries":9.22,"reconcile2":0.44},"signals":94,"placed":0,"equity":996510.28,"open_positions":26,"pending_orders":3,"open_lots":109,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S350:CRWD","S351:CRWD","S352:CRWD"],"github_run":"10269","github_run_id":"35240638842","status":"ok","data_quality":{"clean":{"n":1289,"win":48.25,"med":-25.0,"avg":37.57,"pnl":15791.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":600,"win":63.5,"med":51.18,"avg":64.17,"pnl":10475.45},"keep_only_recent":{"n":417,"win":62.83,"med":54.0,"avg":78.09,"pnl":6865.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
15:31:11  INFO      Mode: exits
15:31:12  INFO        Daily log -> logs/daily/2026-09-17.md
15:31:12  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
15:31:12  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T11:31:13.318187-04:00 share=25% ===
2026-09-17 11:31:13,318 INFO === options_live_micro LIVE 2026-09-17T11:31:13.318187-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 11:31:13,514 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-17 11:31:13,760 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-17 11:31:13,874 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (206 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    20 | WARN | <<<
| Orphaned lots (post-stable) |  1385 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   109 | INFO |
| Total closed lots           |  2301 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1289 med=-25.0% | TAINTED n=1873 med=-39.0% | KEEP-only n=600 med=+51.2% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T153616Z

- UTC timestamp: `20260917T153616Z`
- GitHub run: [#10270](https://github.com/28twagg-ops/TradingBot/actions/runs/35241185518)
- Run id: `35241185518`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260917T153616Z_live_bot.log`, `logs/action_runs/20260917T153616Z_live_options.log`, `logs/action_runs/20260917T153616Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1289 | 48.3 | -25.0 | +37.6 | $+15,791 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 600 | 63.5 | +51.2 | +64.2 | $+10,475 |
| KEEP-only recent | 417 | 62.8 | +54.0 | +78.1 | $+6,865 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T11:36:24.625957-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":11.2,"phases_s":{"reconcile":0.43,"cancel":0.76,"manage":6.76,"protective_stops":2.51},"signals":0,"placed":0,"equity":996696.99,"open_positions":26,"pending_orders":3,"open_lots":109,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10270","github_run_id":"35241185518","status":"ok","data_quality":{"clean":{"n":1289,"win":48.25,"med":-25.0,"avg":37.57,"pnl":15791.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":600,"win":63.5,"med":51.18,"avg":64.17,"pnl":10475.45},"keep_only_recent":{"n":417,"win":62.83,"med":54.0,"avg":78.09,"pnl":6865.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
15:36:18  INFO      Mode: exits
15:36:19  INFO        Daily log -> logs/daily/2026-09-17.md
15:36:19  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
15:36:20  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T11:36:20.807286-04:00 share=25% ===
2026-09-17 11:36:20,807 INFO === options_live_micro LIVE 2026-09-17T11:36:20.807286-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 11:36:21,140 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 11:36:21,390 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 11:36:21,448 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (197 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    20 | WARN | <<<
| Orphaned lots (post-stable) |  1385 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   109 | INFO |
| Total closed lots           |  2301 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1289 med=-25.0% | TAINTED n=1873 med=-39.0% | KEEP-only n=600 med=+51.2% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T154117Z

- UTC timestamp: `20260917T154117Z`
- GitHub run: [#10271](https://github.com/28twagg-ops/TradingBot/actions/runs/35241716463)
- Run id: `35241716463`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260917T154117Z_live_bot.log`, `logs/action_runs/20260917T154117Z_live_options.log`, `logs/action_runs/20260917T154117Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1290 | 48.2 | -25.0 | +37.5 | $+15,752 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 600 | 63.5 | +51.2 | +64.2 | $+10,475 |
| KEEP-only recent | 417 | 62.8 | +54.0 | +78.1 | $+6,865 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T11:41:24.273877-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.8,"phases_s":{"reconcile":0.14,"cancel":0.03,"manage":3.62,"protective_stops":0.47},"signals":0,"placed":0,"equity":996814.97,"open_positions":26,"pending_orders":0,"open_lots":108,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10271","github_run_id":"35241716463","status":"ok","data_quality":{"clean":{"n":1290,"win":48.22,"med":-25.0,"avg":37.48,"pnl":15752.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":600,"win":63.5,"med":51.18,"avg":64.17,"pnl":10475.45},"keep_only_recent":{"n":417,"win":62.83,"med":54.0,"avg":78.09,"pnl":6865.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
15:41:20  INFO      Mode: exits
15:41:20  INFO        Daily log -> logs/daily/2026-09-17.md
15:41:20  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
15:41:20  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T11:41:21.485198-04:00 share=25% ===
2026-09-17 11:41:21,485 INFO === options_live_micro LIVE 2026-09-17T11:41:21.485198-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 11:41:21,529 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 11:41:21,556 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 11:41:21,563 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (187 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    19 | WARN | <<<
| Orphaned lots (post-stable) |  1384 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   108 | INFO |
| Total closed lots           |  2302 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1290 med=-25.0% | TAINTED n=1873 med=-39.0% | KEEP-only n=600 med=+51.2% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T154610Z

- UTC timestamp: `20260917T154610Z`
- GitHub run: [#10272](https://github.com/28twagg-ops/TradingBot/actions/runs/35242253587)
- Run id: `35242253587`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`23s`
- Full logs: `logs/action_runs/20260917T154610Z_live_bot.log`, `logs/action_runs/20260917T154610Z_live_options.log`, `logs/action_runs/20260917T154610Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1291 | 48.2 | -25.0 | +37.4 | $+15,715 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 601 | 63.4 | +51.0 | +63.9 | $+10,438 |
| KEEP-only recent | 418 | 62.7 | +53.9 | +77.7 | $+6,828 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T11:46:17.382211-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":10.8,"phases_s":{"reconcile":0.58,"cancel":0.18,"manage":6.99,"protective_stops":2.25},"signals":0,"placed":0,"equity":996954.95,"open_positions":26,"pending_orders":0,"open_lots":107,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10272","github_run_id":"35242253587","status":"ok","data_quality":{"clean":{"n":1291,"win":48.18,"med":-25.0,"avg":37.39,"pnl":15715.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":601,"win":63.39,"med":50.98,"avg":63.93,"pnl":10438.45},"keep_only_recent":{"n":418,"win":62.68,"med":53.92,"avg":77.71,"pnl":6828.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
15:46:11  INFO      Mode: exits
15:46:12  INFO        Daily log -> logs/daily/2026-09-17.md
15:46:12  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
15:46:12  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T11:46:13.927020-04:00 share=25% ===
2026-09-17 11:46:13,927 INFO === options_live_micro LIVE 2026-09-17T11:46:13.927020-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 11:46:14,124 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 11:46:14,294 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 11:46:14,350 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (184 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    18 | WARN | <<<
| Orphaned lots (post-stable) |  1383 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   107 | INFO |
| Total closed lots           |  2303 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1291 med=-25.0% | TAINTED n=1873 med=-39.0% | KEEP-only n=601 med=+51.0% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T155128Z

- UTC timestamp: `20260917T155128Z`
- GitHub run: [#10273](https://github.com/28twagg-ops/TradingBot/actions/runs/35242788376)
- Run id: `35242788376`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`16s`
- Full logs: `logs/action_runs/20260917T155128Z_live_bot.log`, `logs/action_runs/20260917T155128Z_live_options.log`, `logs/action_runs/20260917T155128Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1292 | 48.1 | -25.6 | +37.3 | $+15,680 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 602 | 63.3 | +51.0 | +63.7 | $+10,403 |
| KEEP-only recent | 419 | 62.5 | +53.8 | +77.3 | $+6,793 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T11:51:34.236336-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.7,"phases_s":{"reconcile":0.23,"cancel":0.03,"manage":3.36,"protective_stops":0.52},"signals":0,"placed":0,"equity":997056.43,"open_positions":26,"pending_orders":0,"open_lots":106,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10273","github_run_id":"35242788376","status":"ok","data_quality":{"clean":{"n":1292,"win":48.14,"med":-25.61,"avg":37.3,"pnl":15680.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":602,"win":63.29,"med":50.96,"avg":63.7,"pnl":10403.45},"keep_only_recent":{"n":419,"win":62.53,"med":53.85,"avg":77.35,"pnl":6793.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
15:51:29  INFO      Mode: exits
15:51:29  INFO        Daily log -> logs/daily/2026-09-17.md
15:51:29  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
15:51:29  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T11:51:31.160803-04:00 share=25% ===
2026-09-17 11:51:31,160 INFO === options_live_micro LIVE 2026-09-17T11:51:31.160803-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 11:51:31,201 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 11:51:31,286 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 11:51:31,291 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (184 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    17 | WARN | <<<
| Orphaned lots (post-stable) |  1382 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   106 | INFO |
| Total closed lots           |  2304 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1292 med=-25.6% | TAINTED n=1873 med=-39.0% | KEEP-only n=602 med=+51.0% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T155600Z

- UTC timestamp: `20260917T155600Z`
- GitHub run: [#10274](https://github.com/28twagg-ops/TradingBot/actions/runs/35243314025)
- Run id: `35243314025`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260917T155600Z_live_bot.log`, `logs/action_runs/20260917T155600Z_live_options.log`, `logs/action_runs/20260917T155600Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1293 | 48.1 | -26.2 | +37.2 | $+15,645 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 603 | 63.2 | +50.9 | +63.5 | $+10,368 |
| KEEP-only recent | 420 | 62.4 | +53.7 | +77.0 | $+6,758 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T11:56:04.975768-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":8.9,"phases_s":{"reconcile":0.61,"cancel":0.1,"manage":6.31,"protective_stops":1.14},"signals":0,"placed":0,"equity":996903.91,"open_positions":26,"pending_orders":0,"open_lots":105,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10274","github_run_id":"35243314025","status":"ok","data_quality":{"clean":{"n":1293,"win":48.11,"med":-26.23,"avg":37.21,"pnl":15645.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":603,"win":63.18,"med":50.94,"avg":63.47,"pnl":10368.45},"keep_only_recent":{"n":420,"win":62.38,"med":53.71,"avg":76.99,"pnl":6758.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
15:56:01  INFO      Mode: exits
15:56:01  INFO        Daily log -> logs/daily/2026-09-17.md
15:56:01  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
15:56:01  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T11:56:02.373718-04:00 share=25% ===
2026-09-17 11:56:02,373 INFO === options_live_micro LIVE 2026-09-17T11:56:02.373718-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 11:56:02,522 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 11:56:02,650 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 11:56:02,691 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (186 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    16 | WARN | <<<
| Orphaned lots (post-stable) |  1381 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   105 | INFO |
| Total closed lots           |  2305 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1293 med=-26.2% | TAINTED n=1873 med=-39.0% | KEEP-only n=603 med=+50.9% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T160117Z

- UTC timestamp: `20260917T160117Z`
- GitHub run: [#10275](https://github.com/28twagg-ops/TradingBot/actions/runs/35243833233)
- Run id: `35243833233`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`16s`
- Full logs: `logs/action_runs/20260917T160117Z_live_bot.log`, `logs/action_runs/20260917T160117Z_live_options.log`, `logs/action_runs/20260917T160117Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1294 | 48.1 | -26.4 | +37.1 | $+15,635 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 604 | 63.1 | +50.9 | +63.3 | $+10,358 |
| KEEP-only recent | 421 | 62.2 | +53.6 | +76.7 | $+6,748 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T12:01:22.907941-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.9,"phases_s":{"reconcile":0.16,"cancel":0.03,"manage":3.84,"protective_stops":0.37},"signals":0,"placed":0,"equity":996882.89,"open_positions":26,"pending_orders":0,"open_lots":104,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10275","github_run_id":"35243833233","status":"ok","data_quality":{"clean":{"n":1294,"win":48.07,"med":-26.45,"avg":37.15,"pnl":15635.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":604,"win":63.08,"med":50.91,"avg":63.29,"pnl":10358.45},"keep_only_recent":{"n":421,"win":62.23,"med":53.57,"avg":76.69,"pnl":6748.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
16:01:18  INFO      Mode: exits
16:01:19  INFO        Daily log -> logs/daily/2026-09-17.md
16:01:19  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
16:01:19  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T12:01:20.004760-04:00 share=25% ===
2026-09-17 12:01:20,004 INFO === options_live_micro LIVE 2026-09-17T12:01:20.004760-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 12:01:20,047 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 12:01:20,068 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 12:01:20,075 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (186 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    16 | WARN | <<<
| Orphaned lots (post-stable) |  1381 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   104 | INFO |
| Total closed lots           |  2306 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1294 med=-26.4% | TAINTED n=1873 med=-39.0% | KEEP-only n=604 med=+50.9% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T160606Z

- UTC timestamp: `20260917T160606Z`
- GitHub run: [#10276](https://github.com/28twagg-ops/TradingBot/actions/runs/35244360224)
- Run id: `35244360224`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`19s`
- Full logs: `logs/action_runs/20260917T160606Z_live_bot.log`, `logs/action_runs/20260917T160606Z_live_options.log`, `logs/action_runs/20260917T160606Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1296 | 48.0 | -27.6 | +37.0 | $+15,577 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 605 | 63.0 | +50.9 | +63.1 | $+10,324 |
| KEEP-only recent | 422 | 62.1 | +53.4 | +76.3 | $+6,714 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T12:06:12.639464-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":8.9,"phases_s":{"reconcile":0.42,"cancel":0.15,"manage":5.74,"protective_stops":1.97},"signals":0,"placed":0,"equity":996870.55,"open_positions":26,"pending_orders":0,"open_lots":102,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10276","github_run_id":"35244360224","status":"ok","data_quality":{"clean":{"n":1296,"win":47.99,"med":-27.62,"avg":37.0,"pnl":15577.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":605,"win":62.98,"med":50.88,"avg":63.06,"pnl":10324.45},"keep_only_recent":{"n":422,"win":62.09,"med":53.45,"avg":76.33,"pnl":6714.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
16:06:07  INFO      Mode: exits
16:06:08  INFO        Daily log -> logs/daily/2026-09-17.md
16:06:08  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
16:06:08  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T12:06:09.473752-04:00 share=25% ===
2026-09-17 12:06:09,473 INFO === options_live_micro LIVE 2026-09-17T12:06:09.473752-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 12:06:09,618 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 12:06:09,833 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 12:06:09,872 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (185 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1380 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   102 | INFO |
| Total closed lots           |  2307 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1296 med=-27.6% | TAINTED n=1873 med=-39.0% | KEEP-only n=605 med=+50.9% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T161113Z

- UTC timestamp: `20260917T161113Z`
- GitHub run: [#10277](https://github.com/28twagg-ops/TradingBot/actions/runs/35244880720)
- Run id: `35244880720`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260917T161113Z_live_bot.log`, `logs/action_runs/20260917T161113Z_live_options.log`, `logs/action_runs/20260917T161113Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1297 | 48.0 | -28.6 | +36.9 | $+15,541 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 606 | 62.9 | +50.9 | +62.8 | $+10,288 |
| KEEP-only recent | 423 | 61.9 | +53.3 | +76.0 | $+6,678 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T12:11:19.114666-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":5.2,"phases_s":{"reconcile":0.18,"cancel":0.05,"manage":3.48,"protective_stops":0.69},"signals":0,"placed":0,"equity":996864.68,"open_positions":26,"pending_orders":0,"open_lots":101,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10277","github_run_id":"35244880720","status":"ok","data_quality":{"clean":{"n":1297,"win":47.96,"med":-28.57,"avg":36.91,"pnl":15541.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":606,"win":62.87,"med":50.87,"avg":62.83,"pnl":10288.45},"keep_only_recent":{"n":423,"win":61.94,"med":53.33,"avg":75.97,"pnl":6678.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
16:11:14  INFO      Mode: exits
16:11:14  INFO        Daily log -> logs/daily/2026-09-17.md
16:11:14  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
16:11:15  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T12:11:16.250024-04:00 share=25% ===
2026-09-17 12:11:16,250 INFO === options_live_micro LIVE 2026-09-17T12:11:16.250024-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 12:11:16,315 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 12:11:16,420 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 12:11:16,431 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (185 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    14 | WARN | <<<
| Orphaned lots (post-stable) |  1379 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   101 | INFO |
| Total closed lots           |  2308 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1297 med=-28.6% | TAINTED n=1873 med=-39.0% | KEEP-only n=606 med=+50.9% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T161610Z

- UTC timestamp: `20260917T161610Z`
- GitHub run: [#10278](https://github.com/28twagg-ops/TradingBot/actions/runs/35245404088)
- Run id: `35245404088`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`25s`
- Full logs: `logs/action_runs/20260917T161610Z_live_bot.log`, `logs/action_runs/20260917T161610Z_live_options.log`, `logs/action_runs/20260917T161610Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1298 | 47.9 | -29.8 | +36.8 | $+15,505 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 607 | 62.8 | +50.9 | +62.6 | $+10,252 |
| KEEP-only recent | 424 | 61.8 | +53.3 | +75.6 | $+6,642 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T12:16:17.978030-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":11.9,"phases_s":{"reconcile":0.59,"cancel":0.23,"manage":7.43,"protective_stops":2.81},"signals":0,"placed":0,"equity":997000.76,"open_positions":26,"pending_orders":0,"open_lots":100,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10278","github_run_id":"35245404088","status":"ok","data_quality":{"clean":{"n":1298,"win":47.92,"med":-29.8,"avg":36.83,"pnl":15505.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":607,"win":62.77,"med":50.85,"avg":62.61,"pnl":10252.45},"keep_only_recent":{"n":424,"win":61.79,"med":53.33,"avg":75.62,"pnl":6642.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
16:16:11  INFO      Mode: exits
16:16:12  INFO        Daily log -> logs/daily/2026-09-17.md
16:16:12  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
16:16:12  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T12:16:13.624090-04:00 share=25% ===
2026-09-17 12:16:13,624 INFO === options_live_micro LIVE 2026-09-17T12:16:13.624090-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 12:16:14,219 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 12:16:14,423 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 12:16:14,491 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (185 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    13 | WARN | <<<
| Orphaned lots (post-stable) |  1378 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   100 | INFO |
| Total closed lots           |  2309 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1298 med=-29.8% | TAINTED n=1873 med=-39.0% | KEEP-only n=607 med=+50.9% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T162108Z

- UTC timestamp: `20260917T162108Z`
- GitHub run: [#10279](https://github.com/28twagg-ops/TradingBot/actions/runs/35245923897)
- Run id: `35245923897`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260917T162108Z_live_bot.log`, `logs/action_runs/20260917T162108Z_live_options.log`, `logs/action_runs/20260917T162108Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1299 | 47.9 | -31.0 | +36.7 | $+15,468 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 607 | 62.8 | +50.9 | +62.6 | $+10,252 |
| KEEP-only recent | 424 | 61.8 | +53.3 | +75.6 | $+6,642 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T12:21:16.652624-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":12.0,"phases_s":{"reconcile":0.61,"cancel":0.25,"manage":6.97,"protective_stops":3.06},"signals":0,"placed":0,"equity":996991.74,"open_positions":26,"pending_orders":0,"open_lots":99,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10279","github_run_id":"35245923897","status":"ok","data_quality":{"clean":{"n":1299,"win":47.88,"med":-31.03,"avg":36.74,"pnl":15468.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":607,"win":62.77,"med":50.85,"avg":62.61,"pnl":10252.45},"keep_only_recent":{"n":424,"win":61.79,"med":53.33,"avg":75.62,"pnl":6642.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
16:21:10  INFO      Mode: exits
16:21:11  INFO        Daily log -> logs/daily/2026-09-17.md
16:21:11  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
16:21:11  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T12:21:12.720234-04:00 share=25% ===
2026-09-17 12:21:12,720 INFO === options_live_micro LIVE 2026-09-17T12:21:12.720234-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 12:21:12,954 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 12:21:13,170 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 12:21:13,242 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (185 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    12 | WARN | <<<
| Orphaned lots (post-stable) |  1377 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    99 | INFO |
| Total closed lots           |  2310 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1299 med=-31.0% | TAINTED n=1873 med=-39.0% | KEEP-only n=607 med=+50.9% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T162609Z

- UTC timestamp: `20260917T162609Z`
- GitHub run: [#10280](https://github.com/28twagg-ops/TradingBot/actions/runs/35246444395)
- Run id: `35246444395`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260917T162609Z_live_bot.log`, `logs/action_runs/20260917T162609Z_live_options.log`, `logs/action_runs/20260917T162609Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1300 | 47.8 | -32.2 | +36.7 | $+15,432 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 607 | 62.8 | +50.9 | +62.6 | $+10,252 |
| KEEP-only recent | 424 | 61.8 | +53.3 | +75.6 | $+6,642 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T12:26:18.305531-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":11.8,"phases_s":{"reconcile":0.59,"cancel":0.24,"manage":7.3,"protective_stops":2.87},"signals":0,"placed":0,"equity":996987.72,"open_positions":26,"pending_orders":0,"open_lots":98,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10280","github_run_id":"35246444395","status":"ok","data_quality":{"clean":{"n":1300,"win":47.85,"med":-32.18,"avg":36.65,"pnl":15432.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":607,"win":62.77,"med":50.85,"avg":62.61,"pnl":10252.45},"keep_only_recent":{"n":424,"win":61.79,"med":53.33,"avg":75.62,"pnl":6642.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
16:26:12  INFO      Mode: exits
16:26:13  INFO        Daily log -> logs/daily/2026-09-17.md
16:26:13  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
16:26:13  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T12:26:14.532614-04:00 share=25% ===
2026-09-17 12:26:14,532 INFO === options_live_micro LIVE 2026-09-17T12:26:14.532614-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 12:26:14,769 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 12:26:14,983 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 12:26:15,053 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (186 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    11 | WARN | <<<
| Orphaned lots (post-stable) |  1376 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    98 | INFO |
| Total closed lots           |  2311 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1300 med=-32.2% | TAINTED n=1873 med=-39.0% | KEEP-only n=607 med=+50.9% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T163128Z

- UTC timestamp: `20260917T163128Z`
- GitHub run: [#10281](https://github.com/28twagg-ops/TradingBot/actions/runs/35246956338)
- Run id: `35246956338`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260917T163128Z_live_bot.log`, `logs/action_runs/20260917T163128Z_live_options.log`, `logs/action_runs/20260917T163128Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1301 | 47.8 | -33.3 | +36.6 | $+15,395 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 607 | 62.8 | +50.9 | +62.6 | $+10,252 |
| KEEP-only recent | 424 | 61.8 | +53.3 | +75.6 | $+6,642 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T12:31:32.667925-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.1,"phases_s":{"reconcile":0.27,"cancel":0.11,"manage":4.11,"protective_stops":1.19},"signals":0,"placed":0,"equity":996979.2,"open_positions":26,"pending_orders":0,"open_lots":97,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10281","github_run_id":"35246956338","status":"ok","data_quality":{"clean":{"n":1301,"win":47.81,"med":-33.33,"avg":36.57,"pnl":15395.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":607,"win":62.77,"med":50.85,"avg":62.61,"pnl":10252.45},"keep_only_recent":{"n":424,"win":61.79,"med":53.33,"avg":75.62,"pnl":6642.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
16:31:29  INFO      Mode: exits
16:31:29  INFO        Daily log -> logs/daily/2026-09-17.md
16:31:29  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
16:31:29  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T12:31:30.252227-04:00 share=25% ===
2026-09-17 12:31:30,252 INFO === options_live_micro LIVE 2026-09-17T12:31:30.252227-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 12:31:30,420 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 12:31:30,557 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 12:31:30,600 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (184 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    10 | WARN | <<<
| Orphaned lots (post-stable) |  1375 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    97 | INFO |
| Total closed lots           |  2312 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1301 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=607 med=+50.9% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T163603Z

- UTC timestamp: `20260917T163603Z`
- GitHub run: [#10282](https://github.com/28twagg-ops/TradingBot/actions/runs/35247476485)
- Run id: `35247476485`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260917T163603Z_live_bot.log`, `logs/action_runs/20260917T163603Z_live_options.log`, `logs/action_runs/20260917T163603Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1303 | 47.8 | -33.3 | +36.5 | $+15,412 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 608 | 62.7 | +50.4 | +62.4 | $+10,243 |
| KEEP-only recent | 425 | 61.6 | +53.3 | +75.3 | $+6,633 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T12:36:08.890572-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":9.1,"phases_s":{"reconcile":1.4,"cancel":0.1,"manage":5.73,"protective_stops":1.23},"signals":0,"placed":0,"equity":997054.66,"open_positions":26,"pending_orders":0,"open_lots":95,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10282","github_run_id":"35247476485","status":"ok","data_quality":{"clean":{"n":1303,"win":47.81,"med":-33.33,"avg":36.53,"pnl":15412.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":608,"win":62.66,"med":50.43,"avg":62.43,"pnl":10243.45},"keep_only_recent":{"n":425,"win":61.65,"med":53.33,"avg":75.33,"pnl":6633.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
16:36:04  INFO      Mode: exits
16:36:04  INFO        Daily log -> logs/daily/2026-09-17.md
16:36:04  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
16:36:05  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T12:36:06.036509-04:00 share=25% ===
2026-09-17 12:36:06,036 INFO === options_live_micro LIVE 2026-09-17T12:36:06.036509-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 12:36:06,151 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 12:36:06,295 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 12:36:06,323 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (184 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    10 | WARN | <<<
| Orphaned lots (post-stable) |  1375 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    95 | INFO |
| Total closed lots           |  2314 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1303 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=608 med=+50.4% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T164108Z

- UTC timestamp: `20260917T164108Z`
- GitHub run: [#10283](https://github.com/28twagg-ops/TradingBot/actions/runs/35247990394)
- Run id: `35247990394`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260917T164108Z_live_bot.log`, `logs/action_runs/20260917T164108Z_live_options.log`, `logs/action_runs/20260917T164108Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1304 | 47.8 | -33.3 | +36.4 | $+15,377 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 608 | 62.7 | +50.4 | +62.4 | $+10,243 |
| KEEP-only recent | 425 | 61.6 | +53.3 | +75.3 | $+6,633 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T12:41:18.188903-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":12.4,"phases_s":{"reconcile":0.57,"cancel":0.26,"manage":7.6,"protective_stops":3.07},"signals":0,"placed":0,"equity":997013.14,"open_positions":26,"pending_orders":0,"open_lots":94,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10283","github_run_id":"35247990394","status":"ok","data_quality":{"clean":{"n":1304,"win":47.78,"med":-33.33,"avg":36.44,"pnl":15377.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":608,"win":62.66,"med":50.43,"avg":62.43,"pnl":10243.45},"keep_only_recent":{"n":425,"win":61.65,"med":53.33,"avg":75.33,"pnl":6633.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
16:41:12  INFO      Mode: exits
16:41:13  INFO        Daily log -> logs/daily/2026-09-17.md
16:41:13  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
16:41:13  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T12:41:14.424203-04:00 share=25% ===
2026-09-17 12:41:14,424 INFO === options_live_micro LIVE 2026-09-17T12:41:14.424203-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 12:41:14,659 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 12:41:14,874 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 12:41:14,946 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (184 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     9 | WARN | <<<
| Orphaned lots (post-stable) |  1374 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    94 | INFO |
| Total closed lots           |  2315 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1304 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=608 med=+50.4% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T164603Z

- UTC timestamp: `20260917T164603Z`
- GitHub run: [#10284](https://github.com/28twagg-ops/TradingBot/actions/runs/35248504156)
- Run id: `35248504156`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260917T164603Z_live_bot.log`, `logs/action_runs/20260917T164603Z_live_options.log`, `logs/action_runs/20260917T164603Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1305 | 47.7 | -33.3 | +36.4 | $+15,342 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 608 | 62.7 | +50.4 | +62.4 | $+10,243 |
| KEEP-only recent | 425 | 61.6 | +53.3 | +75.3 | $+6,633 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T12:46:07.980757-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":7.3,"phases_s":{"reconcile":0.3,"cancel":0.11,"manage":5.04,"protective_stops":1.43},"signals":0,"placed":0,"equity":997283.6,"open_positions":25,"pending_orders":0,"open_lots":92,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10284","github_run_id":"35248504156","status":"ok","data_quality":{"clean":{"n":1305,"win":47.74,"med":-33.33,"avg":36.36,"pnl":15342.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":608,"win":62.66,"med":50.43,"avg":62.43,"pnl":10243.45},"keep_only_recent":{"n":425,"win":61.65,"med":53.33,"avg":75.33,"pnl":6633.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
16:46:04  INFO      Mode: exits
16:46:05  INFO        Daily log -> logs/daily/2026-09-17.md
16:46:05  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
16:46:05  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T12:46:05.832981-04:00 share=25% ===
2026-09-17 12:46:05,833 INFO === options_live_micro LIVE 2026-09-17T12:46:05.832981-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 12:46:05,960 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 12:46:06,049 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 12:46:06,079 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (183 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     8 | WARN | <<<
| Orphaned lots (post-stable) |  1373 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    92 | INFO |
| Total closed lots           |  2316 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1305 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=608 med=+50.4% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T165101Z

- UTC timestamp: `20260917T165101Z`
- GitHub run: [#10285](https://github.com/28twagg-ops/TradingBot/actions/runs/35249006827)
- Run id: `35249006827`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260917T165101Z_live_bot.log`, `logs/action_runs/20260917T165101Z_live_options.log`, `logs/action_runs/20260917T165101Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1305 | 47.7 | -33.3 | +36.4 | $+15,342 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 608 | 62.7 | +50.4 | +62.4 | $+10,243 |
| KEEP-only recent | 425 | 61.6 | +53.3 | +75.3 | $+6,633 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T12:51:07.667576-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":10.6,"phases_s":{"reconcile":0.41,"cancel":0.2,"manage":6.7,"protective_stops":2.38},"signals":0,"placed":0,"equity":997226.63,"open_positions":25,"pending_orders":0,"open_lots":92,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10285","github_run_id":"35249006827","status":"ok","data_quality":{"clean":{"n":1305,"win":47.74,"med":-33.33,"avg":36.36,"pnl":15342.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":608,"win":62.66,"med":50.43,"avg":62.43,"pnl":10243.45},"keep_only_recent":{"n":425,"win":61.65,"med":53.33,"avg":75.33,"pnl":6633.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
16:51:02  INFO      Mode: exits
16:51:02  INFO        Daily log -> logs/daily/2026-09-17.md
16:51:02  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
16:51:03  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T12:51:04.173930-04:00 share=25% ===
2026-09-17 12:51:04,174 INFO === options_live_micro LIVE 2026-09-17T12:51:04.173930-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 12:51:04,374 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 12:51:04,583 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 12:51:04,638 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (183 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     8 | WARN | <<<
| Orphaned lots (post-stable) |  1373 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    92 | INFO |
| Total closed lots           |  2316 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1305 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=608 med=+50.4% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T165705Z

- UTC timestamp: `20260917T165705Z`
- GitHub run: [#10286](https://github.com/28twagg-ops/TradingBot/actions/runs/35249513018)
- Run id: `35249513018`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`23s`
- Full logs: `logs/action_runs/20260917T165705Z_live_bot.log`, `logs/action_runs/20260917T165705Z_live_options.log`, `logs/action_runs/20260917T165705Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1305 | 47.7 | -33.3 | +36.4 | $+15,342 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 608 | 62.7 | +50.4 | +62.4 | $+10,243 |
| KEEP-only recent | 425 | 61.6 | +53.3 | +75.3 | $+6,633 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T12:57:12.788876-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":11.0,"phases_s":{"reconcile":0.48,"cancel":0.23,"manage":6.28,"protective_stops":3.18},"signals":0,"placed":0,"equity":997131.6,"open_positions":25,"pending_orders":0,"open_lots":92,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10286","github_run_id":"35249513018","status":"ok","data_quality":{"clean":{"n":1305,"win":47.74,"med":-33.33,"avg":36.36,"pnl":15342.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":608,"win":62.66,"med":50.43,"avg":62.43,"pnl":10243.45},"keep_only_recent":{"n":425,"win":61.65,"med":53.33,"avg":75.33,"pnl":6633.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
16:57:06  INFO      Mode: exits
16:57:07  INFO        Daily log -> logs/daily/2026-09-17.md
16:57:07  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
16:57:08  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:57 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T12:57:09.213287-04:00 share=25% ===
2026-09-17 12:57:09,213 INFO === options_live_micro LIVE 2026-09-17T12:57:09.213287-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 12:57:09,439 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 12:57:09,644 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 12:57:09,712 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (182 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     8 | WARN | <<<
| Orphaned lots (post-stable) |  1373 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    92 | INFO |
| Total closed lots           |  2316 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1305 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=608 med=+50.4% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T170224Z

- UTC timestamp: `20260917T170224Z`
- GitHub run: [#10287](https://github.com/28twagg-ops/TradingBot/actions/runs/35250007750)
- Run id: `35250007750`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`20s`
- Full logs: `logs/action_runs/20260917T170224Z_live_bot.log`, `logs/action_runs/20260917T170224Z_live_options.log`, `logs/action_runs/20260917T170224Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1306 | 47.7 | -33.3 | +36.3 | $+15,323 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 608 | 62.7 | +50.4 | +62.4 | $+10,243 |
| KEEP-only recent | 425 | 61.6 | +53.3 | +75.3 | $+6,633 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T13:02:32.414955-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":9.9,"phases_s":{"reconcile":0.41,"cancel":0.18,"manage":6.17,"protective_stops":2.46},"signals":0,"placed":0,"equity":997386.58,"open_positions":25,"pending_orders":0,"open_lots":91,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10287","github_run_id":"35250007750","status":"ok","data_quality":{"clean":{"n":1306,"win":47.7,"med":-33.33,"avg":36.29,"pnl":15323.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":608,"win":62.66,"med":50.43,"avg":62.43,"pnl":10243.45},"keep_only_recent":{"n":425,"win":61.65,"med":53.33,"avg":75.33,"pnl":6633.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
17:02:26  INFO      Mode: exits
17:02:27  INFO        Daily log -> logs/daily/2026-09-17.md
17:02:27  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
17:02:28  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:02 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T13:02:29.090704-04:00 share=25% ===
2026-09-17 13:02:29,090 INFO === options_live_micro LIVE 2026-09-17T13:02:29.090704-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 13:02:29,295 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 13:02:29,541 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 13:02:29,596 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (181 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     8 | WARN | <<<
| Orphaned lots (post-stable) |  1373 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    91 | INFO |
| Total closed lots           |  2317 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1306 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=608 med=+50.4% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T170635Z

- UTC timestamp: `20260917T170635Z`
- GitHub run: [#10288](https://github.com/28twagg-ops/TradingBot/actions/runs/35250535226)
- Run id: `35250535226`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260917T170635Z_live_bot.log`, `logs/action_runs/20260917T170635Z_live_options.log`, `logs/action_runs/20260917T170635Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1306 | 47.7 | -33.3 | +36.3 | $+15,323 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 608 | 62.7 | +50.4 | +62.4 | $+10,243 |
| KEEP-only recent | 425 | 61.6 | +53.3 | +75.3 | $+6,633 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T13:06:41.357675-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":5.0,"phases_s":{"reconcile":0.16,"cancel":0.05,"manage":3.72,"protective_stops":0.55},"signals":0,"placed":0,"equity":997343.58,"open_positions":25,"pending_orders":0,"open_lots":91,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10288","github_run_id":"35250535226","status":"ok","data_quality":{"clean":{"n":1306,"win":47.7,"med":-33.33,"avg":36.29,"pnl":15323.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":608,"win":62.66,"med":50.43,"avg":62.43,"pnl":10243.45},"keep_only_recent":{"n":425,"win":61.65,"med":53.33,"avg":75.33,"pnl":6633.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
17:06:36  INFO      Mode: exits
17:06:36  INFO        Daily log -> logs/daily/2026-09-17.md
17:06:36  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
17:06:36  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T13:06:38.348331-04:00 share=25% ===
2026-09-17 13:06:38,348 INFO === options_live_micro LIVE 2026-09-17T13:06:38.348331-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 13:06:38,405 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 13:06:38,474 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 13:06:38,485 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (183 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     8 | WARN | <<<
| Orphaned lots (post-stable) |  1373 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    91 | INFO |
| Total closed lots           |  2317 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1306 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=608 med=+50.4% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T171106Z

- UTC timestamp: `20260917T171106Z`
- GitHub run: [#10289](https://github.com/28twagg-ops/TradingBot/actions/runs/35251053266)
- Run id: `35251053266`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`16s`
- Full logs: `logs/action_runs/20260917T171106Z_live_bot.log`, `logs/action_runs/20260917T171106Z_live_options.log`, `logs/action_runs/20260917T171106Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1306 | 47.7 | -33.3 | +36.3 | $+15,323 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 608 | 62.7 | +50.4 | +62.4 | $+10,243 |
| KEEP-only recent | 425 | 61.6 | +53.3 | +75.3 | $+6,633 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T13:11:12.335561-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.4,"phases_s":{"reconcile":0.18,"cancel":0.03,"manage":3.25,"protective_stops":0.38},"signals":0,"placed":0,"equity":997287.84,"open_positions":25,"pending_orders":0,"open_lots":91,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10289","github_run_id":"35251053266","status":"ok","data_quality":{"clean":{"n":1306,"win":47.7,"med":-33.33,"avg":36.29,"pnl":15323.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":608,"win":62.66,"med":50.43,"avg":62.43,"pnl":10243.45},"keep_only_recent":{"n":425,"win":61.65,"med":53.33,"avg":75.33,"pnl":6633.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
17:11:07  INFO      Mode: exits
17:11:08  INFO        Daily log -> logs/daily/2026-09-17.md
17:11:08  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
17:11:08  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T13:11:09.539198-04:00 share=25% ===
2026-09-17 13:11:09,539 INFO === options_live_micro LIVE 2026-09-17T13:11:09.539198-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 13:11:09,582 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 13:11:09,603 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 13:11:09,610 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (182 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     8 | WARN | <<<
| Orphaned lots (post-stable) |  1373 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    91 | INFO |
| Total closed lots           |  2317 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1306 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=608 med=+50.4% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T171611Z

- UTC timestamp: `20260917T171611Z`
- GitHub run: [#10290](https://github.com/28twagg-ops/TradingBot/actions/runs/35251565819)
- Run id: `35251565819`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260917T171611Z_live_bot.log`, `logs/action_runs/20260917T171611Z_live_options.log`, `logs/action_runs/20260917T171611Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1307 | 47.7 | -33.3 | +36.2 | $+15,317 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 609 | 62.6 | +50.0 | +62.3 | $+10,237 |
| KEEP-only recent | 426 | 61.5 | +53.3 | +75.1 | $+6,627 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T13:16:18.642145-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":7.6,"phases_s":{"reconcile":0.53,"cancel":0.1,"manage":4.66,"protective_stops":1.45},"signals":0,"placed":0,"equity":997210.06,"open_positions":25,"pending_orders":0,"open_lots":90,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10290","github_run_id":"35251565819","status":"ok","data_quality":{"clean":{"n":1307,"win":47.67,"med":-33.33,"avg":36.24,"pnl":15317.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":609,"win":62.56,"med":50.0,"avg":62.28,"pnl":10237.45},"keep_only_recent":{"n":426,"win":61.5,"med":53.33,"avg":75.09,"pnl":6627.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
17:16:13  INFO      Mode: exits
17:16:14  INFO        Daily log -> logs/daily/2026-09-17.md
17:16:14  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
17:16:14  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T13:16:15.169937-04:00 share=25% ===
2026-09-17 13:16:15,170 INFO === options_live_micro LIVE 2026-09-17T13:16:15.169937-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 13:16:15,290 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 13:16:15,440 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 13:16:15,470 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (182 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     8 | WARN | <<<
| Orphaned lots (post-stable) |  1373 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    90 | INFO |
| Total closed lots           |  2318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1307 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=609 med=+50.0% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T172109Z

- UTC timestamp: `20260917T172109Z`
- GitHub run: [#10291](https://github.com/28twagg-ops/TradingBot/actions/runs/35252082420)
- Run id: `35252082420`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260917T172109Z_live_bot.log`, `logs/action_runs/20260917T172109Z_live_options.log`, `logs/action_runs/20260917T172109Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1307 | 47.7 | -33.3 | +36.2 | $+15,317 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 609 | 62.6 | +50.0 | +62.3 | $+10,237 |
| KEEP-only recent | 426 | 61.5 | +53.3 | +75.1 | $+6,627 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T13:21:15.652358-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":5.7,"phases_s":{"reconcile":0.14,"cancel":0.03,"manage":4.5,"protective_stops":0.49},"signals":0,"placed":0,"equity":997299.56,"open_positions":25,"pending_orders":0,"open_lots":90,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10291","github_run_id":"35252082420","status":"ok","data_quality":{"clean":{"n":1307,"win":47.67,"med":-33.33,"avg":36.24,"pnl":15317.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":609,"win":62.56,"med":50.0,"avg":62.28,"pnl":10237.45},"keep_only_recent":{"n":426,"win":61.5,"med":53.33,"avg":75.09,"pnl":6627.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
17:21:11  INFO      Mode: exits
17:21:11  INFO        Daily log -> logs/daily/2026-09-17.md
17:21:11  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
17:21:12  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T13:21:12.835458-04:00 share=25% ===
2026-09-17 13:21:12,835 INFO === options_live_micro LIVE 2026-09-17T13:21:12.835458-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 13:21:12,880 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 13:21:12,903 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 13:21:12,910 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (182 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     8 | WARN | <<<
| Orphaned lots (post-stable) |  1373 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    90 | INFO |
| Total closed lots           |  2318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1307 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=609 med=+50.0% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T172608Z

- UTC timestamp: `20260917T172608Z`
- GitHub run: [#10292](https://github.com/28twagg-ops/TradingBot/actions/runs/35252600894)
- Run id: `35252600894`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`15s`
- Full logs: `logs/action_runs/20260917T172608Z_live_bot.log`, `logs/action_runs/20260917T172608Z_live_options.log`, `logs/action_runs/20260917T172608Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1307 | 47.7 | -33.3 | +36.2 | $+15,317 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 609 | 62.6 | +50.0 | +62.3 | $+10,237 |
| KEEP-only recent | 426 | 61.5 | +53.3 | +75.1 | $+6,627 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T13:26:14.853500-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":7.3,"phases_s":{"reconcile":0.28,"cancel":0.11,"manage":5.05,"protective_stops":1.45},"signals":0,"placed":0,"equity":997141.56,"open_positions":25,"pending_orders":0,"open_lots":90,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10292","github_run_id":"35252600894","status":"ok","data_quality":{"clean":{"n":1307,"win":47.67,"med":-33.33,"avg":36.24,"pnl":15317.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":609,"win":62.56,"med":50.0,"avg":62.28,"pnl":10237.45},"keep_only_recent":{"n":426,"win":61.5,"med":53.33,"avg":75.09,"pnl":6627.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
17:26:09  INFO      Mode: exits
17:26:10  INFO        Daily log -> logs/daily/2026-09-17.md
17:26:10  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
17:26:10  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T13:26:11.597899-04:00 share=25% ===
2026-09-17 13:26:11,597 INFO === options_live_micro LIVE 2026-09-17T13:26:11.597899-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 13:26:11,733 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 13:26:11,853 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 13:26:11,887 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (182 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     8 | WARN | <<<
| Orphaned lots (post-stable) |  1373 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    90 | INFO |
| Total closed lots           |  2318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1307 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=609 med=+50.0% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T173113Z

- UTC timestamp: `20260917T173113Z`
- GitHub run: [#10293](https://github.com/28twagg-ops/TradingBot/actions/runs/35253109133)
- Run id: `35253109133`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`15s`
- Full logs: `logs/action_runs/20260917T173113Z_live_bot.log`, `logs/action_runs/20260917T173113Z_live_options.log`, `logs/action_runs/20260917T173113Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1307 | 47.7 | -33.3 | +36.2 | $+15,317 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 609 | 62.6 | +50.0 | +62.3 | $+10,237 |
| KEEP-only recent | 426 | 61.5 | +53.3 | +75.1 | $+6,627 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T13:31:20.579687-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":7.2,"phases_s":{"reconcile":0.24,"cancel":0.09,"manage":5.06,"protective_stops":1.36},"signals":0,"placed":0,"equity":997183.56,"open_positions":25,"pending_orders":0,"open_lots":90,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10293","github_run_id":"35253109133","status":"ok","data_quality":{"clean":{"n":1307,"win":47.67,"med":-33.33,"avg":36.24,"pnl":15317.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":609,"win":62.56,"med":50.0,"avg":62.28,"pnl":10237.45},"keep_only_recent":{"n":426,"win":61.5,"med":53.33,"avg":75.09,"pnl":6627.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
17:31:15  INFO      Mode: exits
17:31:16  INFO        Daily log -> logs/daily/2026-09-17.md
17:31:16  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
17:31:16  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T13:31:17.569323-04:00 share=25% ===
2026-09-17 13:31:17,569 INFO === options_live_micro LIVE 2026-09-17T13:31:17.569323-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 13:31:17,700 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 13:31:17,863 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 13:31:17,898 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (184 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     8 | WARN | <<<
| Orphaned lots (post-stable) |  1373 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    90 | INFO |
| Total closed lots           |  2318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1307 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=609 med=+50.0% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T173608Z

- UTC timestamp: `20260917T173608Z`
- GitHub run: [#10294](https://github.com/28twagg-ops/TradingBot/actions/runs/35253621140)
- Run id: `35253621140`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260917T173608Z_live_bot.log`, `logs/action_runs/20260917T173608Z_live_options.log`, `logs/action_runs/20260917T173608Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1308 | 47.6 | -33.3 | +36.2 | $+15,296 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 609 | 62.6 | +50.0 | +62.3 | $+10,237 |
| KEEP-only recent | 426 | 61.5 | +53.3 | +75.1 | $+6,627 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T13:36:16.322613-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":12.1,"phases_s":{"reconcile":0.56,"cancel":0.22,"manage":7.32,"protective_stops":3.18},"signals":0,"placed":0,"equity":997191.54,"open_positions":25,"pending_orders":0,"open_lots":89,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10294","github_run_id":"35253621140","status":"ok","data_quality":{"clean":{"n":1308,"win":47.63,"med":-33.33,"avg":36.19,"pnl":15296.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":609,"win":62.56,"med":50.0,"avg":62.28,"pnl":10237.45},"keep_only_recent":{"n":426,"win":61.5,"med":53.33,"avg":75.09,"pnl":6627.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
17:36:09  INFO      Mode: exits
17:36:10  INFO        Daily log -> logs/daily/2026-09-17.md
17:36:10  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
17:36:11  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T13:36:12.590357-04:00 share=25% ===
2026-09-17 13:36:12,590 INFO === options_live_micro LIVE 2026-09-17T13:36:12.590357-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 13:36:12,811 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 13:36:13,010 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 13:36:13,077 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (181 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     8 | WARN | <<<
| Orphaned lots (post-stable) |  1373 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    89 | INFO |
| Total closed lots           |  2318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1308 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=609 med=+50.0% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T174128Z

- UTC timestamp: `20260917T174128Z`
- GitHub run: [#10295](https://github.com/28twagg-ops/TradingBot/actions/runs/35254112576)
- Run id: `35254112576`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`19s`
- Full logs: `logs/action_runs/20260917T174128Z_live_bot.log`, `logs/action_runs/20260917T174128Z_live_options.log`, `logs/action_runs/20260917T174128Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1308 | 47.6 | -33.3 | +36.2 | $+15,296 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 609 | 62.6 | +50.0 | +62.3 | $+10,237 |
| KEEP-only recent | 426 | 61.5 | +53.3 | +75.1 | $+6,627 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T13:41:35.717742-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":9.7,"phases_s":{"reconcile":0.5,"cancel":0.18,"manage":5.88,"protective_stops":2.41},"signals":0,"placed":0,"equity":997069.54,"open_positions":25,"pending_orders":0,"open_lots":89,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10295","github_run_id":"35254112576","status":"ok","data_quality":{"clean":{"n":1308,"win":47.63,"med":-33.33,"avg":36.19,"pnl":15296.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":609,"win":62.56,"med":50.0,"avg":62.28,"pnl":10237.45},"keep_only_recent":{"n":426,"win":61.5,"med":53.33,"avg":75.09,"pnl":6627.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
17:41:29  INFO      Mode: exits
17:41:30  INFO        Daily log -> logs/daily/2026-09-17.md
17:41:30  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
17:41:30  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T13:41:32.100394-04:00 share=25% ===
2026-09-17 13:41:32,100 INFO === options_live_micro LIVE 2026-09-17T13:41:32.100394-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 13:41:32,312 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 13:41:32,502 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 13:41:32,558 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (181 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     8 | WARN | <<<
| Orphaned lots (post-stable) |  1373 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    89 | INFO |
| Total closed lots           |  2318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1308 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=609 med=+50.0% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T174609Z

- UTC timestamp: `20260917T174609Z`
- GitHub run: [#10296](https://github.com/28twagg-ops/TradingBot/actions/runs/35254616912)
- Run id: `35254616912`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`23s`
- Full logs: `logs/action_runs/20260917T174609Z_live_bot.log`, `logs/action_runs/20260917T174609Z_live_options.log`, `logs/action_runs/20260917T174609Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1308 | 47.6 | -33.3 | +36.2 | $+15,296 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 609 | 62.6 | +50.0 | +62.3 | $+10,237 |
| KEEP-only recent | 426 | 61.5 | +53.3 | +75.1 | $+6,627 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T13:46:15.946442-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":10.1,"phases_s":{"reconcile":0.37,"cancel":0.17,"manage":6.44,"protective_stops":2.3},"signals":0,"placed":0,"equity":996947.19,"open_positions":25,"pending_orders":0,"open_lots":89,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10296","github_run_id":"35254616912","status":"ok","data_quality":{"clean":{"n":1308,"win":47.63,"med":-33.33,"avg":36.19,"pnl":15296.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":609,"win":62.56,"med":50.0,"avg":62.28,"pnl":10237.45},"keep_only_recent":{"n":426,"win":61.5,"med":53.33,"avg":75.09,"pnl":6627.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
17:46:10  INFO      Mode: exits
17:46:11  INFO        Daily log -> logs/daily/2026-09-17.md
17:46:11  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
17:46:11  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T13:46:12.479028-04:00 share=25% ===
2026-09-17 13:46:12,479 INFO === options_live_micro LIVE 2026-09-17T13:46:12.479028-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 13:46:12,673 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 13:46:12,829 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 13:46:12,881 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (183 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     8 | WARN | <<<
| Orphaned lots (post-stable) |  1373 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    89 | INFO |
| Total closed lots           |  2318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1308 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=609 med=+50.0% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T175110Z

- UTC timestamp: `20260917T175110Z`
- GitHub run: [#10297](https://github.com/28twagg-ops/TradingBot/actions/runs/35255123204)
- Run id: `35255123204`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`18s`
- Full logs: `logs/action_runs/20260917T175110Z_live_bot.log`, `logs/action_runs/20260917T175110Z_live_options.log`, `logs/action_runs/20260917T175110Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1309 | 47.6 | -33.3 | +36.1 | $+15,261 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 609 | 62.6 | +50.0 | +62.3 | $+10,237 |
| KEEP-only recent | 426 | 61.5 | +53.3 | +75.1 | $+6,627 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T13:51:15.881956-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":10.0,"phases_s":{"reconcile":0.46,"cancel":0.18,"manage":6.0,"protective_stops":2.55},"signals":0,"placed":0,"equity":997058.52,"open_positions":25,"pending_orders":0,"open_lots":88,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10297","github_run_id":"35255123204","status":"ok","data_quality":{"clean":{"n":1309,"win":47.59,"med":-33.33,"avg":36.1,"pnl":15261.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":609,"win":62.56,"med":50.0,"avg":62.28,"pnl":10237.45},"keep_only_recent":{"n":426,"win":61.5,"med":53.33,"avg":75.09,"pnl":6627.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
17:51:11  INFO      Mode: exits
17:51:12  INFO        Daily log -> logs/daily/2026-09-17.md
17:51:12  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
17:51:12  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T13:51:13.303905-04:00 share=25% ===
2026-09-17 13:51:13,303 INFO === options_live_micro LIVE 2026-09-17T13:51:13.303905-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 13:51:13,510 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 13:51:13,679 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 13:51:13,735 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (183 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     7 | WARN | <<<
| Orphaned lots (post-stable) |  1372 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    88 | INFO |
| Total closed lots           |  2319 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1309 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=609 med=+50.0% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260917T175606Z

- UTC timestamp: `20260917T175606Z`
- GitHub run: [#10298](https://github.com/28twagg-ops/TradingBot/actions/runs/35255628272)
- Run id: `35255628272`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`18s`
- Full logs: `logs/action_runs/20260917T175606Z_live_bot.log`, `logs/action_runs/20260917T175606Z_live_options.log`, `logs/action_runs/20260917T175606Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1310 | 47.6 | -33.3 | +36.0 | $+15,226 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 610 | 62.5 | +50.0 | +62.1 | $+10,202 |
| KEEP-only recent | 427 | 61.4 | +53.3 | +74.7 | $+6,592 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-17T13:56:13.398745-04:00","date":"2026-09-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.4,"phases_s":{"reconcile":0.27,"cancel":0.07,"manage":4.26,"protective_stops":1.25},"signals":0,"placed":0,"equity":997008.3,"open_positions":25,"pending_orders":0,"open_lots":87,"submitted_today":59,"filled_today":62,"unattributed_contracts":0,"top_signals":[],"github_run":"10298","github_run_id":"35255628272","status":"ok","data_quality":{"clean":{"n":1310,"win":47.56,"med":-33.33,"avg":36.02,"pnl":15226.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":610,"win":62.46,"med":50.0,"avg":62.06,"pnl":10202.45},"keep_only_recent":{"n":427,"win":61.36,"med":53.33,"avg":74.74,"pnl":6592.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
17:56:07  INFO      Mode: exits
17:56:08  INFO        Daily log -> logs/daily/2026-09-17.md
17:56:08  INFO        Daily log reconciled -> logs/daily/2026-09-17.md (5 ledger rows)
17:56:08  INFO        Daily log -> logs/daily/2026-09-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
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
=== options_live_micro LIVE 2026-09-17T13:56:10.033557-04:00 share=25% ===
2026-09-17 13:56:10,033 INFO === options_live_micro LIVE 2026-09-17T13:56:10.033557-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-17 13:56:10,115 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: manage/exits only
2026-09-17 13:56:10,246 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-17 13:56:10,266 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (183 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
| S167 | 293 | 20 |
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
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     6 | WARN | <<<
| Orphaned lots (post-stable) |  1371 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    87 | INFO |
| Total closed lots           |  2320 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-17_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1310 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=610 med=+50.0% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
