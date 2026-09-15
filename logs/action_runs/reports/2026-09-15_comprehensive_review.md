# Daily Comprehensive Action Review - 2026-09-15

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260915T130117Z

- UTC timestamp: `20260915T130117Z`
- GitHub run: [#9976](https://github.com/28twagg-ops/TradingBot/actions/runs/34972230743)
- Run id: `34972230743`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260915T130117Z_live_bot.log`, `logs/action_runs/20260915T130117Z_live_options.log`, `logs/action_runs/20260915T130117Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T09:01:22.738363-04:00","date":"2026-09-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.26},"signals":0,"placed":0,"equity":1000960.24,"open_positions":5,"pending_orders":0,"open_lots":37,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9976","github_run_id":"34972230743","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:01:18  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.26|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.26|
|  Cash                                                           $191.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $34.28|
|  Open P&L                                                        $+0.36|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ALLE     Pullback50      $34.28     $153.74  $155.39  +1.1%   $+0.36  |
|                                                                        |
|  Total invested                                                  $34.28|
|  Total open P&L                                                  $+0.36|
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
|  2026-09-14  SELL  AES  Pullback50  $33.91  P&L $+0.01                 |
|  2026-09-14  SELL  AMD  Pullback50  $33.90  P&L $-0.01                 |
|  2026-09-14  SELL  ALL  Pullback50  $33.72  P&L $-0.20                 |
|  2026-09-14  SELL  AES  Pullback50  $33.91  P&L $-0.02                 |
|  2026-09-11  SELL  RL  MomReversal  $33.81  P&L $-0.25                 |
|  2026-09-11  SELL  ADI  Pullback50  $34.06  P&L $-0.10                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-15T09:01:19.755406-04:00 share=25% ===
2026-09-15 09:01:19,755 INFO === options_live_micro LIVE 2026-09-15T09:01:19.755406-04:00 share=25% ===
Live account equity $226.26 cash $191.98 #225458845 options_level=3
2026-09-15 09:01:19,844 INFO Live account equity $226.26 cash $191.98 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-15 09:01:19,882 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-15 09:01:19,904 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (159 earlier lines - see full log file)
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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1245 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    37 | INFO |
| Total closed lots           |  2193 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1204 med=-10.1% | TAINTED n=1829 med=-38.8% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T130608Z

- UTC timestamp: `20260915T130608Z`
- GitHub run: [#9977](https://github.com/28twagg-ops/TradingBot/actions/runs/34972749530)
- Run id: `34972749530`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20260915T130608Z_live_bot.log`, `logs/action_runs/20260915T130608Z_live_options.log`, `logs/action_runs/20260915T130608Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T09:06:13.678845-04:00","date":"2026-09-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.47},"signals":0,"placed":0,"equity":1000946.24,"open_positions":5,"pending_orders":0,"open_lots":37,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9977","github_run_id":"34972749530","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:06:09  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.26|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.26|
|  Cash                                                           $191.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $34.28|
|  Open P&L                                                        $+0.36|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ALLE     Pullback50      $34.28     $153.74  $155.39  +1.1%   $+0.36  |
|                                                                        |
|  Total invested                                                  $34.28|
|  Total open P&L                                                  $+0.36|
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
|  2026-09-14  SELL  AES  Pullback50  $33.91  P&L $+0.01                 |
|  2026-09-14  SELL  AMD  Pullback50  $33.90  P&L $-0.01                 |
|  2026-09-14  SELL  ALL  Pullback50  $33.72  P&L $-0.20                 |
|  2026-09-14  SELL  AES  Pullback50  $33.91  P&L $-0.02                 |
|  2026-09-11  SELL  RL  MomReversal  $33.81  P&L $-0.25                 |
|  2026-09-11  SELL  ADI  Pullback50  $34.06  P&L $-0.10                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-15T09:06:10.687837-04:00 share=25% ===
2026-09-15 09:06:10,687 INFO === options_live_micro LIVE 2026-09-15T09:06:10.687837-04:00 share=25% ===
Live account equity $226.26 cash $191.98 #225458845 options_level=3
2026-09-15 09:06:10,880 INFO Live account equity $226.26 cash $191.98 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-15 09:06:10,935 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-15 09:06:11,003 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (156 earlier lines - see full log file)
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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1245 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    37 | INFO |
| Total closed lots           |  2193 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1204 med=-10.1% | TAINTED n=1829 med=-38.8% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T131108Z

- UTC timestamp: `20260915T131108Z`
- GitHub run: [#9978](https://github.com/28twagg-ops/TradingBot/actions/runs/34973270631)
- Run id: `34973270631`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260915T131108Z_live_bot.log`, `logs/action_runs/20260915T131108Z_live_options.log`, `logs/action_runs/20260915T131108Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T09:11:14.721317-04:00","date":"2026-09-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.55},"signals":0,"placed":0,"equity":1000947.75,"open_positions":5,"pending_orders":0,"open_lots":37,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9978","github_run_id":"34973270631","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
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
|  Equity                                                         $226.26|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.26|
|  Cash                                                           $191.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $34.28|
|  Open P&L                                                        $+0.36|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ALLE     Pullback50      $34.28     $153.74  $155.39  +1.1%   $+0.36  |
|                                                                        |
|  Total invested                                                  $34.28|
|  Total open P&L                                                  $+0.36|
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
|  2026-09-14  SELL  AES  Pullback50  $33.91  P&L $+0.01                 |
|  2026-09-14  SELL  AMD  Pullback50  $33.90  P&L $-0.01                 |
|  2026-09-14  SELL  ALL  Pullback50  $33.72  P&L $-0.20                 |
|  2026-09-14  SELL  AES  Pullback50  $33.91  P&L $-0.02                 |
|  2026-09-11  SELL  RL  MomReversal  $33.81  P&L $-0.25                 |
|  2026-09-11  SELL  ADI  Pullback50  $34.06  P&L $-0.10                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-15T09:11:10.977156-04:00 share=25% ===
2026-09-15 09:11:10,977 INFO === options_live_micro LIVE 2026-09-15T09:11:10.977156-04:00 share=25% ===
Live account equity $226.26 cash $191.98 #225458845 options_level=3
2026-09-15 09:11:11,214 INFO Live account equity $226.26 cash $191.98 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-15 09:11:11,283 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-15 09:11:11,351 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (156 earlier lines - see full log file)
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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1245 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    37 | INFO |
| Total closed lots           |  2193 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1204 med=-10.1% | TAINTED n=1829 med=-38.8% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T131608Z

- UTC timestamp: `20260915T131608Z`
- GitHub run: [#9979](https://github.com/28twagg-ops/TradingBot/actions/runs/34973788358)
- Run id: `34973788358`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260915T131608Z_live_bot.log`, `logs/action_runs/20260915T131608Z_live_options.log`, `logs/action_runs/20260915T131608Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T09:16:15.830628-04:00","date":"2026-09-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.5,"phases_s":{"reconcile":0.68},"signals":0,"placed":0,"equity":1000956.24,"open_positions":5,"pending_orders":0,"open_lots":37,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9979","github_run_id":"34973788358","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
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
|  Equity                                                         $226.26|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.26|
|  Cash                                                           $191.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $34.28|
|  Open P&L                                                        $+0.36|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ALLE     Pullback50      $34.28     $153.74  $155.39  +1.1%   $+0.36  |
|                                                                        |
|  Total invested                                                  $34.28|
|  Total open P&L                                                  $+0.36|
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
|  2026-09-14  SELL  AES  Pullback50  $33.91  P&L $+0.01                 |
|  2026-09-14  SELL  AMD  Pullback50  $33.90  P&L $-0.01                 |
|  2026-09-14  SELL  ALL  Pullback50  $33.72  P&L $-0.20                 |
|  2026-09-14  SELL  AES  Pullback50  $33.91  P&L $-0.02                 |
|  2026-09-11  SELL  RL  MomReversal  $33.81  P&L $-0.25                 |
|  2026-09-11  SELL  ADI  Pullback50  $34.06  P&L $-0.10                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-15T09:16:12.267859-04:00 share=25% ===
2026-09-15 09:16:12,267 INFO === options_live_micro LIVE 2026-09-15T09:16:12.267859-04:00 share=25% ===
Live account equity $226.26 cash $191.98 #225458845 options_level=3
2026-09-15 09:16:12,492 INFO Live account equity $226.26 cash $191.98 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-15 09:16:12,550 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-15 09:16:12,608 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (156 earlier lines - see full log file)
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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1245 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    37 | INFO |
| Total closed lots           |  2193 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1204 med=-10.1% | TAINTED n=1829 med=-38.8% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T132129Z

- UTC timestamp: `20260915T132129Z`
- GitHub run: [#9980](https://github.com/28twagg-ops/TradingBot/actions/runs/34974319225)
- Run id: `34974319225`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260915T132129Z_live_bot.log`, `logs/action_runs/20260915T132129Z_live_options.log`, `logs/action_runs/20260915T132129Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T09:21:36.001844-04:00","date":"2026-09-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.36},"signals":0,"placed":0,"equity":1001025.24,"open_positions":5,"pending_orders":0,"open_lots":37,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9980","github_run_id":"34974319225","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:21:30  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.26|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.26|
|  Cash                                                           $191.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $34.28|
|  Open P&L                                                        $+0.36|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ALLE     Pullback50      $34.28     $153.74  $155.39  +1.1%   $+0.36  |
|                                                                        |
|  Total invested                                                  $34.28|
|  Total open P&L                                                  $+0.36|
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
|  2026-09-14  SELL  AES  Pullback50  $33.91  P&L $+0.01                 |
|  2026-09-14  SELL  AMD  Pullback50  $33.90  P&L $-0.01                 |
|  2026-09-14  SELL  ALL  Pullback50  $33.72  P&L $-0.20                 |
|  2026-09-14  SELL  AES  Pullback50  $33.91  P&L $-0.02                 |
|  2026-09-11  SELL  RL  MomReversal  $33.81  P&L $-0.25                 |
|  2026-09-11  SELL  ADI  Pullback50  $34.06  P&L $-0.10                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-15T09:21:32.157654-04:00 share=25% ===
2026-09-15 09:21:32,157 INFO === options_live_micro LIVE 2026-09-15T09:21:32.157654-04:00 share=25% ===
Live account equity $226.26 cash $191.98 #225458845 options_level=3
2026-09-15 09:21:32,778 INFO Live account equity $226.26 cash $191.98 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-15 09:21:32,823 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-15 09:21:32,869 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (156 earlier lines - see full log file)
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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1245 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    37 | INFO |
| Total closed lots           |  2193 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1204 med=-10.1% | TAINTED n=1829 med=-38.8% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T132603Z

- UTC timestamp: `20260915T132603Z`
- GitHub run: [#9981](https://github.com/28twagg-ops/TradingBot/actions/runs/34974850745)
- Run id: `34974850745`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260915T132603Z_live_bot.log`, `logs/action_runs/20260915T132603Z_live_options.log`, `logs/action_runs/20260915T132603Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T09:26:09.377657-04:00","date":"2026-09-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":1000993.44,"open_positions":5,"pending_orders":0,"open_lots":37,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9981","github_run_id":"34974850745","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:26:04  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.26|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.26|
|  Cash                                                           $191.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $34.28|
|  Open P&L                                                        $+0.36|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ALLE     Pullback50      $34.28     $153.74  $155.39  +1.1%   $+0.36  |
|                                                                        |
|  Total invested                                                  $34.28|
|  Total open P&L                                                  $+0.36|
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
|  2026-09-14  SELL  AES  Pullback50  $33.91  P&L $+0.01                 |
|  2026-09-14  SELL  AMD  Pullback50  $33.90  P&L $-0.01                 |
|  2026-09-14  SELL  ALL  Pullback50  $33.72  P&L $-0.20                 |
|  2026-09-14  SELL  AES  Pullback50  $33.91  P&L $-0.02                 |
|  2026-09-11  SELL  RL  MomReversal  $33.81  P&L $-0.25                 |
|  2026-09-11  SELL  ADI  Pullback50  $34.06  P&L $-0.10                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-15T09:26:06.442271-04:00 share=25% ===
2026-09-15 09:26:06,442 INFO === options_live_micro LIVE 2026-09-15T09:26:06.442271-04:00 share=25% ===
Live account equity $226.26 cash $191.98 #225458845 options_level=3
2026-09-15 09:26:06,487 INFO Live account equity $226.26 cash $191.98 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-15 09:26:06,533 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-15 09:26:06,541 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (156 earlier lines - see full log file)
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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1245 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    37 | INFO |
| Total closed lots           |  2193 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1204 med=-10.1% | TAINTED n=1829 med=-38.8% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T133116Z

- UTC timestamp: `20260915T133116Z`
- GitHub run: [#9982](https://github.com/28twagg-ops/TradingBot/actions/runs/34975382288)
- Run id: `34975382288`
- Live bot: exit=`0`, duration=`215s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260915T133116Z_live_bot.log`, `logs/action_runs/20260915T133116Z_live_options.log`, `logs/action_runs/20260915T133116Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T09:26:09.377657-04:00","date":"2026-09-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":1000993.44,"open_positions":5,"pending_orders":0,"open_lots":37,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9981","github_run_id":"34974850745","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:31:17  INFO      Mode: morning_prep
13:31:18  INFO        [prep_positions] 3/3 (3 valid)
13:31:18  INFO      Fetching tickers (universe=both)...
13:31:18  INFO        S&P 500: 503
13:31:19  INFO        MidCap 400: 400
13:31:19  INFO        Total: 903 tickers
13:31:20  INFO        [prep_universe] 40/900 (40 valid)
13:31:21  INFO        [prep_universe] 80/900 (80 valid)
13:31:23  INFO        [prep_universe] 120/900 (120 valid)
13:31:24  INFO        [prep_universe] 160/900 (160 valid)
13:31:25  INFO        [prep_universe] 200/900 (199 valid)
13:31:32  INFO        [prep_universe] 240/900 (238 valid)
13:31:46  INFO        [prep_universe] 280/900 (278 valid)
13:31:56  INFO        [prep_universe] 320/900 (318 valid)
13:32:09  INFO        [prep_universe] 360/900 (358 valid)
13:32:19  INFO        [prep_universe] 400/900 (398 valid)
13:32:32  INFO        [prep_universe] 440/900 (438 valid)
13:32:45  INFO        [prep_universe] 480/900 (478 valid)
13:32:56  INFO        [prep_universe] 520/900 (518 valid)
13:33:09  INFO        [prep_universe] 560/900 (558 valid)
13:33:19  INFO        [prep_universe] 600/900 (598 valid)
13:33:32  INFO        [prep_universe] 640/900 (638 valid)
13:33:46  INFO        [prep_universe] 680/900 (678 valid)
13:33:56  INFO        [prep_universe] 720/900 (718 valid)
13:34:09  INFO        [prep_universe] 760/900 (758 valid)
13:34:19  INFO        [prep_universe] 800/900 (798 valid)
13:34:32  INFO        [prep_universe] 840/900 (838 valid)
13:34:45  INFO        [prep_universe] 880/900 (878 valid)
13:34:49  INFO        [prep_universe] 900/900 (898 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.74|
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
|  Invested                                                       $101.61|
|  Open P&L                                                        $-0.15|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAL      MomReversal     $33.80     $13.06   $13.02   -0.3%   $-0.12  |
|  ALLE     Pullback50      $34.11     $153.74  $154.61  +0.6%   $+0.19  |
|  ROL      MomReversal     $33.70     $35.14   $34.91   -0.7%   $-0.22  |
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
|  Signal candidates                                                   33|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-15T09:34:52.406623-04:00 share=25% ===
2026-09-15 09:34:52,406 INFO === options_live_micro LIVE 2026-09-15T09:34:52.406623-04:00 share=25% ===
Live account equity $225.57 cash $124.13 #225458845 options_level=3
2026-09-15 09:34:52,550 INFO Live account equity $225.57 cash $124.13 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 09:34:52,678 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 09:34:52,774 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=37 paper_keys=yes dry_run=False
  alpaca positions=5
  FLAG b180|S217|1cfeb793 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$1,000,878.94
  buying_power=$3,957,759.02 cash=$1,034,612.22
  open option orders: 3
    MARA260925C00012000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    MARA260925C00011000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    MARA260918C00011000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 4
    MARA260918C00012000 qty=33 mkt=$759.00
    MARA260925C00011500 qty=-1 mkt=$-65.00
    MARA260925C00012500 qty=3 mkt=$90.00
    PATH260925C00017000 qty=1 mkt=$0.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-15T09:34:55.698460-04:00 ===

[Run context]
Paper auth OK — equity $1000872.72, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-15 09:34:56,694 INFO   EXIT [b330|lab0330_s357_w2_1005_1045_r1|S357] stop_loss (-100.0%) SELL 1 PATH260925C00017000 @<= 0.01
2026-09-15 09:34:56,998 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-49.7%) SELL 1 MARA260918C00012000 @<= 0.20
Protective stops: placed=0 upgraded=0 already=2 failed=1 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260915T133650Z

- UTC timestamp: `20260915T133650Z`
- GitHub run: [#9983](https://github.com/28twagg-ops/TradingBot/actions/runs/34975926918)
- Run id: `34975926918`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260915T133650Z_live_bot.log`, `logs/action_runs/20260915T133650Z_live_options.log`, `logs/action_runs/20260915T133650Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T09:26:09.377657-04:00","date":"2026-09-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":1000993.44,"open_positions":5,"pending_orders":0,"open_lots":37,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9981","github_run_id":"34974850745","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:36:51  INFO      Mode: morning_prep
13:36:52  INFO        [prep_positions] 3/3 (3 valid)
13:36:52  INFO      Fetching tickers (universe=both)...
13:36:52  INFO        S&P 500: 503
13:36:52  INFO        MidCap 400: 400
13:36:52  INFO        Total: 903 tickers
13:36:53  INFO        [prep_universe] 40/900 (40 valid)
13:36:56  INFO        [prep_universe] 80/900 (80 valid)
13:36:57  INFO        [prep_universe] 120/900 (120 valid)
13:36:58  INFO        [prep_universe] 160/900 (160 valid)
13:36:59  INFO        [prep_universe] 200/900 (199 valid)
13:37:07  INFO        [prep_universe] 240/900 (238 valid)
13:37:20  INFO        [prep_universe] 280/900 (278 valid)
13:37:30  INFO        [prep_universe] 320/900 (318 valid)
13:37:43  INFO        [prep_universe] 360/900 (358 valid)
13:37:54  INFO        [prep_universe] 400/900 (398 valid)
13:38:07  INFO        [prep_universe] 440/900 (438 valid)
13:38:20  INFO        [prep_universe] 480/900 (478 valid)
13:38:30  INFO        [prep_universe] 520/900 (518 valid)
13:38:43  INFO        [prep_universe] 560/900 (558 valid)
13:38:53  INFO        [prep_universe] 600/900 (598 valid)
13:39:06  INFO        [prep_universe] 640/900 (638 valid)
13:39:19  INFO        [prep_universe] 680/900 (678 valid)
13:39:29  INFO        [prep_universe] 720/900 (718 valid)
13:39:42  INFO        [prep_universe] 760/900 (758 valid)
13:39:55  INFO        [prep_universe] 800/900 (798 valid)
13:40:06  INFO        [prep_universe] 840/900 (838 valid)
13:40:19  INFO        [prep_universe] 880/900 (878 valid)
13:40:25  INFO        [prep_universe] 900/900 (898 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.37|
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
|  Invested                                                       $101.24|
|  Open P&L                                                        $-0.52|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAL      MomReversal     $33.75     $13.06   $12.99   -0.5%   $-0.17  |
|  ALLE     Pullback50      $34.04     $153.74  $154.29  +0.4%   $+0.12  |
|  ROL      MomReversal     $33.45     $35.14   $34.65   -1.4%   $-0.47  |
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
|  Signal candidates                                                   18|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-15T09:40:28.611479-04:00 share=25% ===
2026-09-15 09:40:28,611 INFO === options_live_micro LIVE 2026-09-15T09:40:28.611479-04:00 share=25% ===
Live account equity $225.28 cash $124.13 #225458845 options_level=3
2026-09-15 09:40:28,944 INFO Live account equity $225.28 cash $124.13 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 09:40:29,055 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 09:40:29,150 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=37 paper_keys=yes dry_run=False
  alpaca positions=4
  FLAG b330|S357|4850d0ee missing from Alpaca
  FLAG b180|S217|1cfeb793 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$1,000,858.68
  buying_power=$3,957,576.92 cash=$1,034,637.18
  open option orders: 3
    MARA260925C00012000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    MARA260925C00011000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    MARA260918C00011000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 3
    MARA260918C00012000 qty=32 mkt=$768.00
    MARA260925C00011500 qty=-1 mkt=$-68.00
    MARA260925C00012500 qty=3 mkt=$93.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-15T09:40:32.116397-04:00 ===

[Run context]
Paper auth OK — equity $1000890.68, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-15 09:40:33,124 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-45.4%) SELL 1 MARA260918C00012000 @<= 0.26
Protective stops: placed=0 upgraded=0 already=1 failed=1 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260915T134218Z

- UTC timestamp: `20260915T134218Z`
- GitHub run: [#9984](https://github.com/28twagg-ops/TradingBot/actions/runs/34976473299)
- Run id: `34976473299`
- Live bot: exit=`0`, duration=`215s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260915T134218Z_live_bot.log`, `logs/action_runs/20260915T134218Z_live_options.log`, `logs/action_runs/20260915T134218Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T09:26:09.377657-04:00","date":"2026-09-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":1000993.44,"open_positions":5,"pending_orders":0,"open_lots":37,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9981","github_run_id":"34974850745","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:42:18  INFO      Mode: morning_prep
13:42:20  INFO        [prep_positions] 3/3 (3 valid)
13:42:20  INFO        Universe cache hit: 903 tickers (tickers_2026-09-15.json)
13:42:21  INFO        [prep_universe] 40/900 (40 valid)
13:42:22  INFO        [prep_universe] 80/900 (80 valid)
13:42:24  INFO        [prep_universe] 120/900 (120 valid)
13:42:25  INFO        [prep_universe] 160/900 (160 valid)
13:42:26  INFO        [prep_universe] 200/900 (199 valid)
13:42:33  INFO        [prep_universe] 240/900 (238 valid)
13:42:47  INFO        [prep_universe] 280/900 (278 valid)
13:42:57  INFO        [prep_universe] 320/900 (318 valid)
13:43:10  INFO        [prep_universe] 360/900 (358 valid)
13:43:20  INFO        [prep_universe] 400/900 (398 valid)
13:43:34  INFO        [prep_universe] 440/900 (438 valid)
13:43:47  INFO        [prep_universe] 480/900 (478 valid)
13:43:57  INFO        [prep_universe] 520/900 (518 valid)
13:44:10  INFO        [prep_universe] 560/900 (558 valid)
13:44:21  INFO        [prep_universe] 600/900 (598 valid)
13:44:34  INFO        [prep_universe] 640/900 (638 valid)
13:44:47  INFO        [prep_universe] 680/900 (678 valid)
13:44:57  INFO        [prep_universe] 720/900 (718 valid)
13:45:11  INFO        [prep_universe] 760/900 (758 valid)
13:45:21  INFO        [prep_universe] 800/900 (798 valid)
13:45:34  INFO        [prep_universe] 840/900 (838 valid)
13:45:47  INFO        [prep_universe] 880/900 (878 valid)
13:45:51  INFO        [prep_universe] 900/900 (898 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:42 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.20|
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
|  Invested                                                       $101.07|
|  Open P&L                                                        $-0.69|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAL      MomReversal     $33.75     $13.06   $12.99   -0.5%   $-0.17  |
|  ALLE     Pullback50      $33.98     $153.74  $154.03  +0.2%   $+0.06  |
|  ROL      MomReversal     $33.33     $35.14   $34.53   -1.7%   $-0.59  |
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
|  Signal candidates                                                   22|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-15T09:45:54.587505-04:00 share=25% ===
2026-09-15 09:45:54,587 INFO === options_live_micro LIVE 2026-09-15T09:45:54.587505-04:00 share=25% ===
Live account equity $225.26 cash $124.13 #225458845 options_level=3
2026-09-15 09:45:54,792 INFO Live account equity $225.26 cash $124.13 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 09:45:54,987 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 09:45:55,109 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=36 paper_keys=yes dry_run=False
  alpaca positions=4
  FLAG b330|S357|4850d0ee missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$1,000,890.68
  buying_power=$3,957,743.32 cash=$1,034,637.18
  open option orders: 4
    MARA260918C00012000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.26
    MARA260925C00012000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    MARA260925C00011000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    MARA260918C00011000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 3
    MARA260918C00012000 qty=32 mkt=$768.00
    MARA260925C00011500 qty=-1 mkt=$-68.00
    MARA260925C00012500 qty=3 mkt=$93.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-15T09:45:57.983116-04:00 ===

[Run context]
Paper auth OK — equity $1000921.18, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
Protective stops: placed=0 upgraded=0 already=1 failed=1 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260915T134757Z

- UTC timestamp: `20260915T134757Z`
- GitHub run: [#9985](https://github.com/28twagg-ops/TradingBot/actions/runs/34977027004)
- Run id: `34977027004`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260915T134757Z_live_bot.log`, `logs/action_runs/20260915T134757Z_live_options.log`, `logs/action_runs/20260915T134757Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T09:26:09.377657-04:00","date":"2026-09-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":1000993.44,"open_positions":5,"pending_orders":0,"open_lots":37,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9981","github_run_id":"34974850745","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:47:59  INFO      Mode: morning_scan
13:48:00  INFO        [positions] 3/3 (3 valid)
13:48:00  INFO        SELL MARKET [urgent] ROL closed
13:48:03  INFO        TX logged: SELL ROL  P&L -1.59%
13:48:03  INFO        SELL MARKET [urgent] AAL closed
13:48:05  INFO        TX logged: SELL AAL  P&L -0.54%
13:48:05  INFO        Universe cache hit: 903 tickers (tickers_2026-09-15.json)
13:48:06  INFO        [universe] 40/902 (40 valid)
13:48:08  INFO        [universe] 80/902 (80 valid)
13:48:09  INFO        [universe] 120/902 (120 valid)
13:48:10  INFO        [universe] 160/902 (160 valid)
13:48:12  INFO        [universe] 200/902 (199 valid)
13:48:19  INFO        [universe] 240/902 (238 valid)
13:48:32  INFO        [universe] 280/902 (278 valid)
13:48:43  INFO        [universe] 320/902 (318 valid)
13:48:56  INFO        [universe] 360/902 (358 valid)
13:49:06  INFO        [universe] 400/902 (398 valid)
13:49:20  INFO        [universe] 440/902 (438 valid)
13:49:30  INFO        [universe] 480/902 (478 valid)
13:49:43  INFO        [universe] 520/902 (518 valid)
13:49:54  INFO        [universe] 560/902 (558 valid)
13:50:07  INFO        [universe] 600/902 (598 valid)
13:50:20  INFO        [universe] 640/902 (638 valid)
13:50:31  INFO        [universe] 680/902 (678 valid)
13:50:44  INFO        [universe] 720/902 (718 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260915T135216Z

- UTC timestamp: `20260915T135216Z`
- GitHub run: [#9986](https://github.com/28twagg-ops/TradingBot/actions/runs/34977572365)
- Run id: `34977572365`
- Live bot: exit=`0`, duration=`237s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260915T135216Z_live_bot.log`, `logs/action_runs/20260915T135216Z_live_options.log`, `logs/action_runs/20260915T135216Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T09:26:09.377657-04:00","date":"2026-09-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":1000993.44,"open_positions":5,"pending_orders":0,"open_lots":37,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9981","github_run_id":"34974850745","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
... (128 earlier lines - see full log file)
|  CBSH     Pullback50      eq     $58.86   57.9   -3.07   50MA bounce (+|
|  CFR      Pullback50      eq     $163.72  51.2   -3.22   50MA bounce (+|
|  CVLT     Pullback50      eq     $138.70  57.7   -2.83   50MA bounce (+|
|  HOMB     Pullback50      eq     $30.18   55.1   -3.09   50MA bounce (-|
|  HWC      Pullback50      eq     $76.07   58.4   -2.79   50MA bounce (-|
|  KEX      Pullback50      eq     $139.25  54.6   -3.38   50MA bounce (-|
|  SIRI     Pullback50      eq     $29.58   57.6   -2.40   50MA bounce (-|
|  SLAB     Pullback50      eq     $219.60  58.5   -2.09   50MA bounce (+|
|  TOST     Pullback50      eq     $32.94   25.4   -2.43   50MA bounce (+|
|  UBSI     Pullback50      eq     $48.13   57.2   -3.33   50MA bounce (+|
|  ZION     Pullback50      eq     $69.59   61.9   -2.53   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] AMZN  Pullback50                                   $33.79|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|13:55:51  INFO        BUY  APO  $33.79  [Pullback50]  id=4979f33c-0eea-48b2-ae5c-a2f2833250ee
13:56:13  INFO        place_all_stops: checking 3 positions...
13:56:13  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
13:56:13  INFO        STOP skipped AMZN: fractional (0.1339 shares) — software exit will handle it
13:56:13  INFO        STOP skipped APO: fractional (0.2624 shares) — software exit will handle it
13:56:13  INFO        Daily log -> logs/daily/2026-09-15.md
13:56:13  INFO        Dashboard written → logs/dashboard.md

|    ENTER [eq] APO  Pullback50                                    $33.79|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] CFG  Pullback50                                      cap 3|
|    SKIP [eq] DHR  Pullback50                                      cap 3|
|    SKIP [eq] FDS  Pullback50                                      cap 3|
|    SKIP [eq] NVDA  Pullback50                                     cap 3|
|    SKIP [eq] STLD  Pullback50                                     cap 3|
|    SKIP [eq] TFC  Pullback50                                      cap 3|
|    SKIP [eq] USB  Pullback50                                      cap 3|
|    SKIP [eq] AN  Pullback50                                       cap 3|
|    SKIP [eq] CART  Pullback50                                     cap 3|
|    SKIP [eq] CBSH  Pullback50                                     cap 3|
|    SKIP [eq] CFR  Pullback50                                      cap 3|
|    SKIP [eq] CVLT  Pullback50                                     cap 3|
|    SKIP [eq] HOMB  Pullback50                                     cap 3|
|    SKIP [eq] HWC  Pullback50                                      cap 3|
|    SKIP [eq] KEX  Pullback50                                      cap 3|
|    SKIP [eq] SIRI  Pullback50                                     cap 3|
|    SKIP [eq] SLAB  Pullback50                                     cap 3|
|    SKIP [eq] TOST  Pullback50                                     cap 3|
|    SKIP [eq] UBSI  Pullback50                                     cap 3|
|    SKIP [eq] ZION  Pullback50                                     cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      2|
+------------------------------------------------------------------------+
|  AMZN                                                 still unconfirmed|
|  APO                                                  still unconfirmed|
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
|  Signals                                                             22|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  2 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $225.17|
|  Cash                                                           $123.67|
+========================================================================+
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260915T135735Z

- UTC timestamp: `20260915T135735Z`
- GitHub run: [#9987](https://github.com/28twagg-ops/TradingBot/actions/runs/34978127290)
- Run id: `34978127290`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260915T135735Z_live_bot.log`, `logs/action_runs/20260915T135735Z_live_options.log`, `logs/action_runs/20260915T135735Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T09:26:09.377657-04:00","date":"2026-09-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":1000993.44,"open_positions":5,"pending_orders":0,"open_lots":37,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9981","github_run_id":"34974850745","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:57:35  INFO      Mode: morning_scan
13:57:36  INFO        [positions] 3/3 (3 valid)
13:57:36  INFO        Universe cache hit: 903 tickers (tickers_2026-09-15.json)
13:57:37  INFO        [universe] 40/900 (40 valid)
13:57:39  INFO        [universe] 80/900 (80 valid)
13:57:40  INFO        [universe] 120/900 (120 valid)
13:57:42  INFO        [universe] 160/900 (160 valid)
13:57:43  INFO        [universe] 200/900 (199 valid)
13:57:50  INFO        [universe] 240/900 (238 valid)
13:58:03  INFO        [universe] 280/900 (278 valid)
13:58:16  INFO        [universe] 320/900 (318 valid)
13:58:26  INFO        [universe] 360/900 (358 valid)
13:58:38  INFO        [universe] 400/900 (398 valid)
13:58:51  INFO        [universe] 440/900 (438 valid)
13:59:01  INFO        [universe] 480/900 (478 valid)
13:59:14  INFO        [universe] 520/900 (518 valid)
13:59:27  INFO        [universe] 560/900 (558 valid)
13:59:37  INFO        [universe] 600/900 (598 valid)
13:59:50  INFO        [universe] 640/900 (638 valid)
14:00:03  INFO        [universe] 680/900 (678 valid)
14:00:13  INFO        [universe] 720/900 (718 valid)
14:00:26  INFO        [universe] 760/900 (758 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260915T140201Z

- UTC timestamp: `20260915T140201Z`
- GitHub run: [#9988](https://github.com/28twagg-ops/TradingBot/actions/runs/34978670979)
- Run id: `34978670979`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`156s`
- Full logs: `logs/action_runs/20260915T140201Z_live_bot.log`, `logs/action_runs/20260915T140201Z_live_options.log`, `logs/action_runs/20260915T140201Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1205 | 49.1 | -12.5 | +40.7 | $+15,790 |
| TAINTED | 1831 | 33.4 | -38.8 | +12.1 | $-9,013 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T10:02:07.654976-04:00","date":"2026-09-15","mode":"entry+manage","header":"entry+manage (51 new)","elapsed_s":146.5,"phases_s":{"reconcile":0.4,"cancel":0.12,"manage":0.5,"protective_stops":0.37,"scan":35.3,"entries":102.52,"reconcile2":2.11},"signals":304,"placed":51,"equity":1000827.51,"open_positions":9,"pending_orders":18,"open_lots":68,"submitted_today":51,"filled_today":33,"unattributed_contracts":0,"top_signals":["S403:AMD","S165:COIN","S164:COIN","S168:COIN","S167:COIN","S166:COIN","S163:COIN","S350:COIN"],"github_run":"9988","github_run_id":"34978670979","status":"ok","data_quality":{"clean":{"n":1205,"win":49.13,"med":-12.5,"avg":40.71,"pnl":15789.55},"tainted":{"n":1831,"win":33.42,"med":-38.81,"avg":12.06,"pnl":-9012.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:02:02  INFO      Mode: exits
14:02:03  INFO        Daily log -> logs/daily/2026-09-15.md
14:02:03  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (2 ledger rows)
14:02:03  INFO        place_all_stops: checking 3 positions...
14:02:03  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:02:03  INFO        STOP skipped AMZN: fractional (0.1339 shares) — software exit will handle it
14:02:03  INFO        STOP skipped APO: fractional (0.2624 shares) — software exit will handle it
14:02:03  INFO        [positions] 3/3 (3 valid)
14:02:03  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:02 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.07|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.4%  $-0.13                                           HOLD|
|  APO  P&L -0.3%  $-0.09                                            HOLD|
|  ALLE  P&L +0.4%  $+0.14                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T10:02:04.482786-04:00 share=25% ===
2026-09-15 10:02:04,482 INFO === options_live_micro LIVE 2026-09-15T10:02:04.482786-04:00 share=25% ===
Live account equity $225.07 cash $123.67 #225458845 options_level=3
2026-09-15 10:02:04,693 INFO Live account equity $225.07 cash $123.67 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 10:02:04,875 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 10:02:05,005 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (191 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 285 | 19 |
| S165 | 1721 | 31 |
| S166 | 135 | 9 |
| S167 | 279 | 18 |
| S168 | 210 | 15 |
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
| 2026-09-15 |    0 |    4 |    4 |    0 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    68 | INFO |
| Total closed lots           |  2195 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1205 med=-12.5% | TAINTED n=1831 med=-38.8% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.07 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T140615Z

- UTC timestamp: `20260915T140615Z`
- GitHub run: [#9989](https://github.com/28twagg-ops/TradingBot/actions/runs/34979239098)
- Run id: `34979239098`
- Live bot: exit=`0`, duration=`9s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`161s`
- Full logs: `logs/action_runs/20260915T140615Z_live_bot.log`, `logs/action_runs/20260915T140615Z_live_options.log`, `logs/action_runs/20260915T140615Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1205 | 49.1 | -12.5 | +40.7 | $+15,790 |
| TAINTED | 1834 | 33.4 | -38.9 | +11.9 | $-9,106 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T10:06:27.976686-04:00","date":"2026-09-15","mode":"entry+manage","header":"entry+manage (54 new)","elapsed_s":149.3,"phases_s":{"reconcile":0.27,"cancel":0.02,"manage":2.16,"protective_stops":0.17,"scan":52.13,"entries":82.35,"reconcile2":5.24},"signals":304,"placed":54,"equity":1000631.57,"open_positions":19,"pending_orders":24,"open_lots":116,"submitted_today":105,"filled_today":81,"unattributed_contracts":0,"top_signals":["S403:AMD","S165:COIN","S164:COIN","S168:COIN","S167:COIN","S166:COIN","S163:COIN","S350:COIN"],"github_run":"9989","github_run_id":"34979239098","status":"ok","data_quality":{"clean":{"n":1205,"win":49.13,"med":-12.5,"avg":40.71,"pnl":15789.55},"tainted":{"n":1834,"win":33.37,"med":-38.9,"avg":11.92,"pnl":-9105.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:06:19  INFO      Mode: exits
14:06:19  INFO        Daily log -> logs/daily/2026-09-15.md
14:06:19  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (2 ledger rows)
14:06:19  INFO        place_all_stops: checking 3 positions...
14:06:19  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:06:19  INFO        STOP skipped AMZN: fractional (0.1339 shares) — software exit will handle it
14:06:19  INFO        STOP skipped APO: fractional (0.2624 shares) — software exit will handle it
14:06:20  INFO        [positions] 3/3 (3 valid)
14:06:20  INFO        SELL MARKET [urgent] AMZN closed
14:06:22  INFO        TX logged: SELL AMZN  P&L -0.71%
14:06:22  INFO        SELL MARKET [urgent] APO closed
14:06:24  INFO        TX logged: SELL APO  P&L -0.58%
14:06:24  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.92|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.7%  $-0.24                        EXIT: stop_loss (-0.7%)|
|  APO  P&L -0.6%  $-0.20                         EXIT: stop_loss (-0.6%)|
|  ALLE  P&L +0.6%  $+0.21                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  2 attempted  |  2 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
|  Logged exits                                                         2|
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
|  AMZN                                        -0.71%  (threshold -0.50%)|
|  APO                                         -0.58%  (threshold -0.50%)|
|  Count                                                                2|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-15T10:06:25.136835-04:00 share=25% ===
2026-09-15 10:06:25,136 INFO === options_live_micro LIVE 2026-09-15T10:06:25.136835-04:00 share=25% ===
Live account equity $224.94 cash $190.81 #225458845 options_level=3
2026-09-15 10:06:25,182 INFO Live account equity $224.94 cash $190.81 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 10:06:25,206 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 10:06:25,220 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (201 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 263 | 15 |
| S164 | 289 | 20 |
| S165 | 1725 | 32 |
| S166 | 135 | 9 |
| S167 | 283 | 19 |
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
| 2026-09-15 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   116 | INFO |
| Total closed lots           |  2198 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1205 med=-12.5% | TAINTED n=1834 med=-38.9% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.94 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T141108Z

- UTC timestamp: `20260915T141108Z`
- GitHub run: [#9990](https://github.com/28twagg-ops/TradingBot/actions/runs/34979796660)
- Run id: `34979796660`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`90s`
- Full logs: `logs/action_runs/20260915T141108Z_live_bot.log`, `logs/action_runs/20260915T141108Z_live_options.log`, `logs/action_runs/20260915T141108Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1206 | 49.1 | -14.2 | +40.6 | $+15,772 |
| TAINTED | 1835 | 33.4 | -39.0 | +11.9 | $-9,124 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T10:11:14.671233-04:00","date":"2026-09-15","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":77.6,"phases_s":{"reconcile":0.48,"cancel":0.04,"manage":5.24,"protective_stops":0.5,"scan":46.05,"entries":12.1,"reconcile2":3.19},"signals":304,"placed":0,"equity":1000329.57,"open_positions":21,"pending_orders":18,"open_lots":121,"submitted_today":105,"filled_today":87,"unattributed_contracts":0,"top_signals":["S403:AMD","S165:COIN","S164:COIN","S168:COIN","S167:COIN","S166:COIN","S163:COIN","S350:COIN"],"github_run":"9990","github_run_id":"34979796660","status":"ok","data_quality":{"clean":{"n":1206,"win":49.09,"med":-14.18,"avg":40.64,"pnl":15771.55},"tainted":{"n":1835,"win":33.35,"med":-38.98,"avg":11.88,"pnl":-9123.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:11:09  INFO      Mode: exits
14:11:10  INFO        Daily log -> logs/daily/2026-09-15.md
14:11:10  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
14:11:10  INFO        place_all_stops: checking 1 positions...
14:11:10  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:11:10  INFO        [positions] 1/1 (1 valid)
14:11:10  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.91|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.5%  $+0.18                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T10:11:11.333335-04:00 share=25% ===
2026-09-15 10:11:11,333 INFO === options_live_micro LIVE 2026-09-15T10:11:11.333335-04:00 share=25% ===
Live account equity $224.91 cash $190.81 #225458845 options_level=3
2026-09-15 10:11:11,403 INFO Live account equity $224.91 cash $190.81 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 10:11:11,436 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 10:11:11,479 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (192 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 263 | 15 |
| S164 | 289 | 20 |
| S165 | 1725 | 32 |
| S166 | 135 | 9 |
| S167 | 283 | 19 |
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
| 2026-09-15 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2199 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1206 med=-14.2% | TAINTED n=1835 med=-39.0% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.91 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T141607Z

- UTC timestamp: `20260915T141607Z`
- GitHub run: [#9991](https://github.com/28twagg-ops/TradingBot/actions/runs/34980352264)
- Run id: `34980352264`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`119s`
- Full logs: `logs/action_runs/20260915T141607Z_live_bot.log`, `logs/action_runs/20260915T141607Z_live_options.log`, `logs/action_runs/20260915T141607Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1206 | 49.1 | -14.2 | +40.6 | $+15,772 |
| TAINTED | 1836 | 33.4 | -38.9 | +11.9 | $-9,120 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T10:16:15.705910-04:00","date":"2026-09-15","mode":"entry+manage","header":"entry+manage (4 new)","elapsed_s":105.7,"phases_s":{"reconcile":0.61,"cancel":0.18,"manage":10.38,"protective_stops":2.45,"scan":55.13,"entries":32.48,"reconcile2":0.7},"signals":304,"placed":4,"equity":1000442.72,"open_positions":23,"pending_orders":19,"open_lots":124,"submitted_today":109,"filled_today":90,"unattributed_contracts":0,"top_signals":["S403:AMD","S165:COIN","S164:COIN","S168:COIN","S167:COIN","S166:COIN","S163:COIN","S350:COIN"],"github_run":"9991","github_run_id":"34980352264","status":"ok","data_quality":{"clean":{"n":1206,"win":49.09,"med":-14.18,"avg":40.64,"pnl":15771.55},"tainted":{"n":1836,"win":33.39,"med":-38.9,"avg":11.88,"pnl":-9119.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:16:08  INFO      Mode: exits
14:16:09  INFO        Daily log -> logs/daily/2026-09-15.md
14:16:09  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
14:16:09  INFO        place_all_stops: checking 1 positions...
14:16:09  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:16:09  INFO        [positions] 1/1 (1 valid)
14:16:09  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.89|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.5%  $+0.16                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T10:16:11.355687-04:00 share=25% ===
2026-09-15 10:16:11,355 INFO === options_live_micro LIVE 2026-09-15T10:16:11.355687-04:00 share=25% ===
Live account equity $224.89 cash $190.81 #225458845 options_level=3
2026-09-15 10:16:11,615 INFO Live account equity $224.89 cash $190.81 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 10:16:11,946 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 10:16:12,102 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (191 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 263 | 15 |
| S164 | 289 | 20 |
| S165 | 1725 | 32 |
| S166 | 135 | 9 |
| S167 | 283 | 19 |
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
| 2026-09-15 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   124 | INFO |
| Total closed lots           |  2200 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1206 med=-14.2% | TAINTED n=1836 med=-38.9% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.89 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T142107Z

- UTC timestamp: `20260915T142107Z`
- GitHub run: [#9992](https://github.com/28twagg-ops/TradingBot/actions/runs/34980909045)
- Run id: `34980909045`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`88s`
- Full logs: `logs/action_runs/20260915T142107Z_live_bot.log`, `logs/action_runs/20260915T142107Z_live_options.log`, `logs/action_runs/20260915T142107Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1206 | 49.1 | -14.2 | +40.6 | $+15,772 |
| TAINTED | 1836 | 33.4 | -38.9 | +11.9 | $-9,120 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T10:21:13.778065-04:00","date":"2026-09-15","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":75.7,"phases_s":{"reconcile":0.38,"cancel":0.05,"manage":6.9,"protective_stops":1.04,"scan":55.92,"entries":9.71,"reconcile2":0.31},"signals":304,"placed":0,"equity":1000353.4,"open_positions":24,"pending_orders":15,"open_lots":128,"submitted_today":109,"filled_today":94,"unattributed_contracts":0,"top_signals":["S403:AMD","S165:COIN","S164:COIN","S168:COIN","S167:COIN","S166:COIN","S163:COIN","S350:COIN"],"github_run":"9992","github_run_id":"34980909045","status":"ok","data_quality":{"clean":{"n":1206,"win":49.09,"med":-14.18,"avg":40.64,"pnl":15771.55},"tainted":{"n":1836,"win":33.39,"med":-38.9,"avg":11.88,"pnl":-9119.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:21:08  INFO      Mode: exits
14:21:08  INFO        Daily log -> logs/daily/2026-09-15.md
14:21:08  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
14:21:09  INFO        place_all_stops: checking 1 positions...
14:21:09  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:21:09  INFO        [positions] 1/1 (1 valid)
14:21:09  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.95|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.7%  $+0.22                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T10:21:10.552374-04:00 share=25% ===
2026-09-15 10:21:10,552 INFO === options_live_micro LIVE 2026-09-15T10:21:10.552374-04:00 share=25% ===
Live account equity $224.95 cash $190.81 #225458845 options_level=3
2026-09-15 10:21:10,649 INFO Live account equity $224.95 cash $190.81 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 10:21:10,774 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 10:21:10,825 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (187 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 263 | 15 |
| S164 | 289 | 20 |
| S165 | 1725 | 32 |
| S166 | 135 | 9 |
| S167 | 283 | 19 |
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
| 2026-09-15 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   128 | INFO |
| Total closed lots           |  2200 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1206 med=-14.2% | TAINTED n=1836 med=-38.9% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.95 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T142612Z

- UTC timestamp: `20260915T142612Z`
- GitHub run: [#9993](https://github.com/28twagg-ops/TradingBot/actions/runs/34981481488)
- Run id: `34981481488`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`70s`
- Full logs: `logs/action_runs/20260915T142612Z_live_bot.log`, `logs/action_runs/20260915T142612Z_live_options.log`, `logs/action_runs/20260915T142612Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1206 | 49.1 | -14.2 | +40.6 | $+15,772 |
| TAINTED | 1836 | 33.4 | -38.9 | +11.9 | $-9,120 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T10:26:18.184380-04:00","date":"2026-09-15","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":59.6,"phases_s":{"reconcile":0.84,"cancel":0.06,"manage":5.48,"protective_stops":0.75,"scan":41.27,"entries":9.52,"reconcile2":0.21},"signals":304,"placed":0,"equity":1000298.2,"open_positions":24,"pending_orders":11,"open_lots":131,"submitted_today":109,"filled_today":98,"unattributed_contracts":0,"top_signals":["S403:AMD","S165:COIN","S164:COIN","S168:COIN","S167:COIN","S166:COIN","S163:COIN","S350:COIN"],"github_run":"9993","github_run_id":"34981481488","status":"ok","data_quality":{"clean":{"n":1206,"win":49.09,"med":-14.18,"avg":40.64,"pnl":15771.55},"tainted":{"n":1836,"win":33.39,"med":-38.9,"avg":11.88,"pnl":-9119.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:26:13  INFO      Mode: exits
14:26:13  INFO        Daily log -> logs/daily/2026-09-15.md
14:26:13  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
14:26:13  INFO        place_all_stops: checking 1 positions...
14:26:13  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:26:13  INFO        [positions] 1/1 (1 valid)
14:26:13  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.93|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.6%  $+0.20                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T10:26:14.716612-04:00 share=25% ===
2026-09-15 10:26:14,716 INFO === options_live_micro LIVE 2026-09-15T10:26:14.716612-04:00 share=25% ===
Live account equity $224.93 cash $190.81 #225458845 options_level=3
2026-09-15 10:26:14,827 INFO Live account equity $224.93 cash $190.81 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 10:26:14,959 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 10:26:15,013 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (195 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 263 | 15 |
| S164 | 289 | 20 |
| S165 | 1725 | 32 |
| S166 | 135 | 9 |
| S167 | 283 | 19 |
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
| 2026-09-15 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   131 | INFO |
| Total closed lots           |  2200 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1206 med=-14.2% | TAINTED n=1836 med=-38.9% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.93 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T143217Z

- UTC timestamp: `20260915T143217Z`
- GitHub run: [#9994](https://github.com/28twagg-ops/TradingBot/actions/runs/34982053833)
- Run id: `34982053833`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`66s`
- Full logs: `logs/action_runs/20260915T143217Z_live_bot.log`, `logs/action_runs/20260915T143217Z_live_options.log`, `logs/action_runs/20260915T143217Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1207 | 49.0 | -15.9 | +40.6 | $+15,767 |
| TAINTED | 1836 | 33.4 | -38.9 | +11.9 | $-9,120 |
| KEEP-only | 627 | 63.2 | +51.4 | +64.0 | $+10,729 |
| KEEP-only recent | 430 | 61.2 | +53.3 | +74.2 | $+6,084 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T10:32:23.190961-04:00","date":"2026-09-15","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":56.4,"phases_s":{"reconcile":0.34,"cancel":0.1,"manage":5.72,"protective_stops":1.7,"scan":28.41,"entries":17.5,"reconcile2":0.45},"signals":304,"placed":2,"equity":1000103.2,"open_positions":25,"pending_orders":11,"open_lots":132,"submitted_today":111,"filled_today":100,"unattributed_contracts":0,"top_signals":["S403:AMD","S165:COIN","S164:COIN","S168:COIN","S167:COIN","S166:COIN","S163:COIN","S350:COIN"],"github_run":"9994","github_run_id":"34982053833","status":"ok","data_quality":{"clean":{"n":1207,"win":49.05,"med":-15.87,"avg":40.56,"pnl":15766.55},"tainted":{"n":1836,"win":33.39,"med":-38.9,"avg":11.88,"pnl":-9119.84},"keep_only":{"n":627,"win":63.16,"med":51.39,"avg":64.01,"pnl":10729.45},"keep_only_recent":{"n":430,"win":61.16,"med":53.33,"avg":74.2,"pnl":6084.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:32:18  INFO      Mode: exits
14:32:19  INFO        Daily log -> logs/daily/2026-09-15.md
14:32:19  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
14:32:19  INFO        place_all_stops: checking 1 positions...
14:32:19  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:32:19  INFO        [positions] 1/1 (1 valid)
14:32:19  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:32 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.79|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.2%  $+0.06                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T10:32:20.341503-04:00 share=25% ===
2026-09-15 10:32:20,341 INFO === options_live_micro LIVE 2026-09-15T10:32:20.341503-04:00 share=25% ===
Live account equity $224.79 cash $190.81 #225458845 options_level=3
2026-09-15 10:32:20,484 INFO Live account equity $224.79 cash $190.81 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 10:32:20,604 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 10:32:20,679 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (193 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 263 | 15 |
| S164 | 289 | 20 |
| S165 | 1725 | 32 |
| S166 | 135 | 9 |
| S167 | 283 | 19 |
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
| 2026-09-15 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   132 | INFO |
| Total closed lots           |  2201 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1207 med=-15.9% | TAINTED n=1836 med=-38.9% | KEEP-only n=627 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.79 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T143643Z

- UTC timestamp: `20260915T143643Z`
- GitHub run: [#9995](https://github.com/28twagg-ops/TradingBot/actions/runs/34982619112)
- Run id: `34982619112`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`59s`
- Full logs: `logs/action_runs/20260915T143643Z_live_bot.log`, `logs/action_runs/20260915T143643Z_live_options.log`, `logs/action_runs/20260915T143643Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1208 | 49.0 | -15.9 | +40.5 | $+15,762 |
| TAINTED | 1836 | 33.4 | -38.9 | +11.9 | $-9,120 |
| KEEP-only | 628 | 63.1 | +51.2 | +63.8 | $+10,724 |
| KEEP-only recent | 431 | 61.0 | +53.3 | +73.9 | $+6,079 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T10:36:49.239174-04:00","date":"2026-09-15","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":50.9,"phases_s":{"reconcile":0.29,"cancel":0.11,"manage":5.76,"protective_stops":1.4,"scan":28.84,"entries":12.36,"reconcile2":0.3},"signals":304,"placed":0,"equity":1000066.12,"open_positions":25,"pending_orders":11,"open_lots":131,"submitted_today":111,"filled_today":100,"unattributed_contracts":0,"top_signals":["S403:AMD","S165:COIN","S164:COIN","S168:COIN","S167:COIN","S166:COIN","S163:COIN","S350:COIN"],"github_run":"9995","github_run_id":"34982619112","status":"ok","data_quality":{"clean":{"n":1208,"win":49.01,"med":-15.93,"avg":40.49,"pnl":15761.55},"tainted":{"n":1836,"win":33.39,"med":-38.9,"avg":11.88,"pnl":-9119.84},"keep_only":{"n":628,"win":63.06,"med":51.18,"avg":63.83,"pnl":10724.45},"keep_only_recent":{"n":431,"win":61.02,"med":53.33,"avg":73.91,"pnl":6079.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:36:45  INFO      Mode: exits
14:36:45  INFO        Daily log -> logs/daily/2026-09-15.md
14:36:45  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
14:36:45  INFO        place_all_stops: checking 1 positions...
14:36:45  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:36:45  INFO        [positions] 1/1 (1 valid)
14:36:46  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.83|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.3%  $+0.10                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T10:36:46.753833-04:00 share=25% ===
2026-09-15 10:36:46,753 INFO === options_live_micro LIVE 2026-09-15T10:36:46.753833-04:00 share=25% ===
Live account equity $224.83 cash $190.81 #225458845 options_level=3
2026-09-15 10:36:46,885 INFO Live account equity $224.83 cash $190.81 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 10:36:46,983 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 10:36:47,060 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (193 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 263 | 15 |
| S164 | 289 | 20 |
| S165 | 1725 | 32 |
| S166 | 135 | 9 |
| S167 | 283 | 19 |
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
| 2026-09-15 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   131 | INFO |
| Total closed lots           |  2202 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1208 med=-15.9% | TAINTED n=1836 med=-38.9% | KEEP-only n=628 med=+51.2% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.83 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T144104Z

- UTC timestamp: `20260915T144104Z`
- GitHub run: [#9996](https://github.com/28twagg-ops/TradingBot/actions/runs/34983181420)
- Run id: `34983181420`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`85s`
- Full logs: `logs/action_runs/20260915T144104Z_live_bot.log`, `logs/action_runs/20260915T144104Z_live_options.log`, `logs/action_runs/20260915T144104Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1210 | 48.9 | -16.6 | +40.3 | $+15,737 |
| TAINTED | 1837 | 33.4 | -38.8 | +11.9 | $-9,112 |
| KEEP-only | 628 | 63.1 | +51.2 | +63.8 | $+10,724 |
| KEEP-only recent | 431 | 61.0 | +53.3 | +73.9 | $+6,079 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T10:41:11.336761-04:00","date":"2026-09-15","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":73.4,"phases_s":{"reconcile":0.64,"cancel":0.06,"manage":6.37,"protective_stops":1.11,"scan":53.82,"entries":9.5,"reconcile2":0.34},"signals":304,"placed":0,"equity":999860.89,"open_positions":25,"pending_orders":4,"open_lots":135,"submitted_today":111,"filled_today":107,"unattributed_contracts":0,"top_signals":["S403:AMD","S165:COIN","S164:COIN","S168:COIN","S167:COIN","S166:COIN","S163:COIN","S350:COIN"],"github_run":"9996","github_run_id":"34983181420","status":"ok","data_quality":{"clean":{"n":1210,"win":48.93,"med":-16.6,"avg":40.34,"pnl":15736.55},"tainted":{"n":1837,"win":33.42,"med":-38.81,"avg":11.89,"pnl":-9111.84},"keep_only":{"n":628,"win":63.06,"med":51.18,"avg":63.83,"pnl":10724.45},"keep_only_recent":{"n":431,"win":61.02,"med":53.33,"avg":73.91,"pnl":6079.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:41:05  INFO      Mode: exits
14:41:06  INFO        Daily log -> logs/daily/2026-09-15.md
14:41:06  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
14:41:06  INFO        place_all_stops: checking 1 positions...
14:41:06  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:41:06  INFO        [positions] 1/1 (1 valid)
14:41:06  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.84|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.3%  $+0.11                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T10:41:07.876445-04:00 share=25% ===
2026-09-15 10:41:07,876 INFO === options_live_micro LIVE 2026-09-15T10:41:07.876445-04:00 share=25% ===
Live account equity $224.84 cash $190.81 #225458845 options_level=3
2026-09-15 10:41:07,972 INFO Live account equity $224.84 cash $190.81 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 10:41:08,113 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 10:41:08,169 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (195 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 263 | 15 |
| S164 | 289 | 20 |
| S165 | 1725 | 32 |
| S166 | 135 | 9 |
| S167 | 283 | 19 |
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
| 2026-09-15 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   135 | INFO |
| Total closed lots           |  2204 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1210 med=-16.6% | TAINTED n=1837 med=-38.8% | KEEP-only n=628 med=+51.2% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.84 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T144610Z

- UTC timestamp: `20260915T144610Z`
- GitHub run: [#9997](https://github.com/28twagg-ops/TradingBot/actions/runs/34983743772)
- Run id: `34983743772`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`170s`
- Full logs: `logs/action_runs/20260915T144610Z_live_bot.log`, `logs/action_runs/20260915T144610Z_live_options.log`, `logs/action_runs/20260915T144610Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1211 | 48.9 | -17.2 | +40.3 | $+15,727 |
| TAINTED | 1840 | 33.5 | -38.8 | +12.3 | $-9,122 |
| KEEP-only | 629 | 63.0 | +51.0 | +63.6 | $+10,714 |
| KEEP-only recent | 432 | 60.9 | +53.3 | +73.6 | $+6,069 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T10:46:18.329712-04:00","date":"2026-09-15","mode":"entry+manage","header":"entry+manage (36 new)","elapsed_s":157.9,"phases_s":{"reconcile":0.5,"cancel":0.14,"manage":9.58,"protective_stops":2.13,"scan":54.14,"entries":77.83,"reconcile2":1.07},"signals":304,"placed":36,"equity":999842.85,"open_positions":28,"pending_orders":32,"open_lots":141,"submitted_today":147,"filled_today":115,"unattributed_contracts":0,"top_signals":["S403:AMD","S165:COIN","S164:COIN","S168:COIN","S167:COIN","S166:COIN","S163:COIN","S350:COIN"],"github_run":"9997","github_run_id":"34983743772","status":"ok","data_quality":{"clean":{"n":1211,"win":48.89,"med":-17.19,"avg":40.27,"pnl":15726.55},"tainted":{"n":1840,"win":33.48,"med":-38.81,"avg":12.32,"pnl":-9121.84},"keep_only":{"n":629,"win":62.96,"med":50.98,"avg":63.64,"pnl":10714.45},"keep_only_recent":{"n":432,"win":60.88,"med":53.33,"avg":73.63,"pnl":6069.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:46:11  INFO      Mode: exits
14:46:12  INFO        Daily log -> logs/daily/2026-09-15.md
14:46:12  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
14:46:12  INFO        place_all_stops: checking 1 positions...
14:46:12  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:46:12  INFO        [positions] 1/1 (1 valid)
14:46:13  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.84|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.3%  $+0.11                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T10:46:14.385518-04:00 share=25% ===
2026-09-15 10:46:14,385 INFO === options_live_micro LIVE 2026-09-15T10:46:14.385518-04:00 share=25% ===
Live account equity $224.84 cash $190.81 #225458845 options_level=3
2026-09-15 10:46:14,615 INFO Live account equity $224.84 cash $190.81 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 10:46:14,840 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 10:46:14,984 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (240 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 263 | 15 |
| S164 | 291 | 20 |
| S165 | 1727 | 32 |
| S166 | 135 | 9 |
| S167 | 285 | 19 |
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
| 2026-09-15 |    4 |   10 |   10 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    42 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   141 | INFO |
| Total closed lots           |  2208 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1211 med=-17.2% | TAINTED n=1840 med=-38.8% | KEEP-only n=629 med=+51.0% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.84 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T145105Z

- UTC timestamp: `20260915T145105Z`
- GitHub run: [#9998](https://github.com/28twagg-ops/TradingBot/actions/runs/34984308887)
- Run id: `34984308887`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`113s`
- Full logs: `logs/action_runs/20260915T145105Z_live_bot.log`, `logs/action_runs/20260915T145105Z_live_options.log`, `logs/action_runs/20260915T145105Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1212 | 48.8 | -17.2 | +40.2 | $+15,717 |
| TAINTED | 1841 | 33.5 | -38.8 | +12.3 | $-9,116 |
| KEEP-only | 630 | 62.9 | +51.0 | +63.5 | $+10,704 |
| KEEP-only recent | 433 | 60.7 | +53.3 | +73.3 | $+6,059 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T10:51:12.375793-04:00","date":"2026-09-15","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":101.6,"phases_s":{"reconcile":0.36,"cancel":0.07,"manage":8.34,"protective_stops":1.22,"scan":48.38,"entries":31.83,"reconcile2":0.65},"signals":304,"placed":2,"equity":999757.42,"open_positions":29,"pending_orders":24,"open_lots":149,"submitted_today":149,"filled_today":125,"unattributed_contracts":0,"top_signals":["S403:AMD","S165:COIN","S164:COIN","S168:COIN","S167:COIN","S166:COIN","S163:COIN","S350:COIN"],"github_run":"9998","github_run_id":"34984308887","status":"ok","data_quality":{"clean":{"n":1212,"win":48.84,"med":-17.22,"avg":40.19,"pnl":15716.55},"tainted":{"n":1841,"win":33.51,"med":-38.81,"avg":12.31,"pnl":-9115.84},"keep_only":{"n":630,"win":62.86,"med":50.96,"avg":63.46,"pnl":10704.45},"keep_only_recent":{"n":433,"win":60.74,"med":53.33,"avg":73.34,"pnl":6059.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:51:06  INFO      Mode: exits
14:51:07  INFO        Daily log -> logs/daily/2026-09-15.md
14:51:07  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
14:51:07  INFO        place_all_stops: checking 1 positions...
14:51:07  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:51:07  INFO        [positions] 1/1 (1 valid)
14:51:07  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.89|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.5%  $+0.16                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T10:51:09.118867-04:00 share=25% ===
2026-09-15 10:51:09,118 INFO === options_live_micro LIVE 2026-09-15T10:51:09.118867-04:00 share=25% ===
Live account equity $224.90 cash $190.81 #225458845 options_level=3
2026-09-15 10:51:09,269 INFO Live account equity $224.90 cash $190.81 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 10:51:09,496 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 10:51:09,580 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (221 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 263 | 15 |
| S164 | 291 | 20 |
| S165 | 1727 | 32 |
| S166 | 135 | 9 |
| S167 | 285 | 19 |
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
| 2026-09-15 |    4 |   10 |   10 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    42 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |   149 | INFO |
| Total closed lots           |  2210 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1212 med=-17.2% | TAINTED n=1841 med=-38.8% | KEEP-only n=630 med=+51.0% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.89 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T145605Z

- UTC timestamp: `20260915T145605Z`
- GitHub run: [#9999](https://github.com/28twagg-ops/TradingBot/actions/runs/34984873772)
- Run id: `34984873772`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`103s`
- Full logs: `logs/action_runs/20260915T145605Z_live_bot.log`, `logs/action_runs/20260915T145605Z_live_options.log`, `logs/action_runs/20260915T145605Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1212 | 48.8 | -17.2 | +40.2 | $+15,717 |
| TAINTED | 1842 | 33.5 | -38.8 | +12.3 | $-9,127 |
| KEEP-only | 630 | 62.9 | +51.0 | +63.5 | $+10,704 |
| KEEP-only recent | 433 | 60.7 | +53.3 | +73.3 | $+6,059 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T10:56:11.839692-04:00","date":"2026-09-15","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":90.0,"phases_s":{"reconcile":0.14,"cancel":0.03,"manage":6.71,"protective_stops":0.41,"scan":46.65,"entries":25.72,"reconcile2":0.33},"signals":304,"placed":2,"equity":999838.25,"open_positions":30,"pending_orders":24,"open_lots":151,"submitted_today":151,"filled_today":127,"unattributed_contracts":0,"top_signals":["S403:AMD","S165:COIN","S164:COIN","S168:COIN","S167:COIN","S166:COIN","S163:COIN","S350:COIN"],"github_run":"9999","github_run_id":"34984873772","status":"ok","data_quality":{"clean":{"n":1212,"win":48.84,"med":-17.22,"avg":40.19,"pnl":15716.55},"tainted":{"n":1842,"win":33.5,"med":-38.81,"avg":12.27,"pnl":-9126.84},"keep_only":{"n":630,"win":62.86,"med":50.96,"avg":63.46,"pnl":10704.45},"keep_only_recent":{"n":433,"win":60.74,"med":53.33,"avg":73.34,"pnl":6059.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:56:06  INFO      Mode: exits
14:56:06  INFO        Daily log -> logs/daily/2026-09-15.md
14:56:06  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
14:56:06  INFO        place_all_stops: checking 1 positions...
14:56:06  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:56:06  INFO        [positions] 1/1 (1 valid)
14:56:07  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.91|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.5%  $+0.18                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T10:56:08.618839-04:00 share=25% ===
2026-09-15 10:56:08,618 INFO === options_live_micro LIVE 2026-09-15T10:56:08.618839-04:00 share=25% ===
Live account equity $224.91 cash $190.81 #225458845 options_level=3
2026-09-15 10:56:08,679 INFO Live account equity $224.91 cash $190.81 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 10:56:08,793 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 10:56:08,818 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (215 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 263 | 15 |
| S164 | 291 | 20 |
| S165 | 1727 | 32 |
| S166 | 135 | 9 |
| S167 | 285 | 19 |
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
| 2026-09-15 |    4 |   10 |   10 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    42 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |    10 | WARN | <<<
| Total open lots             |   151 | INFO |
| Total closed lots           |  2211 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1212 med=-17.2% | TAINTED n=1842 med=-38.8% | KEEP-only n=630 med=+51.0% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.91 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T150112Z

- UTC timestamp: `20260915T150112Z`
- GitHub run: [#10000](https://github.com/28twagg-ops/TradingBot/actions/runs/34985440423)
- Run id: `34985440423`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`108s`
- Full logs: `logs/action_runs/20260915T150112Z_live_bot.log`, `logs/action_runs/20260915T150112Z_live_options.log`, `logs/action_runs/20260915T150112Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1213 | 48.8 | -17.2 | +40.1 | $+15,687 |
| TAINTED | 1842 | 33.5 | -38.8 | +12.3 | $-9,127 |
| KEEP-only | 631 | 62.8 | +50.9 | +63.3 | $+10,674 |
| KEEP-only recent | 434 | 60.6 | +53.3 | +73.1 | $+6,029 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T11:01:19.479344-04:00","date":"2026-09-15","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":96.8,"phases_s":{"reconcile":0.46,"cancel":0.13,"manage":11.26,"protective_stops":1.93,"scan":47.6,"entries":26.32,"reconcile2":0.4},"signals":304,"placed":0,"equity":999961.67,"open_positions":30,"pending_orders":24,"open_lots":150,"submitted_today":151,"filled_today":127,"unattributed_contracts":0,"top_signals":["S403:AMD","S165:COIN","S164:COIN","S168:COIN","S167:COIN","S166:COIN","S163:COIN","S350:COIN"],"github_run":"10000","github_run_id":"34985440423","status":"ok","data_quality":{"clean":{"n":1213,"win":48.8,"med":-17.24,"avg":40.12,"pnl":15686.55},"tainted":{"n":1842,"win":33.5,"med":-38.81,"avg":12.27,"pnl":-9126.84},"keep_only":{"n":631,"win":62.76,"med":50.94,"avg":63.29,"pnl":10674.45},"keep_only_recent":{"n":434,"win":60.6,"med":53.33,"avg":73.06,"pnl":6029.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:01:13  INFO      Mode: exits
15:01:14  INFO        Daily log -> logs/daily/2026-09-15.md
15:01:14  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
15:01:14  INFO        place_all_stops: checking 1 positions...
15:01:14  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:01:14  INFO        [positions] 1/1 (1 valid)
15:01:15  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.94|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.6%  $+0.21                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T11:01:16.148026-04:00 share=25% ===
2026-09-15 11:01:16,148 INFO === options_live_micro LIVE 2026-09-15T11:01:16.148026-04:00 share=25% ===
Live account equity $224.92 cash $190.81 #225458845 options_level=3
2026-09-15 11:01:16,345 INFO Live account equity $224.92 cash $190.81 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 11:01:16,513 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 11:01:16,660 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (214 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 263 | 15 |
| S164 | 291 | 20 |
| S165 | 1727 | 32 |
| S166 | 135 | 9 |
| S167 | 285 | 19 |
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
| 2026-09-15 |    4 |   10 |   10 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    42 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |    10 | WARN | <<<
| Total open lots             |   150 | INFO |
| Total closed lots           |  2212 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1213 med=-17.2% | TAINTED n=1842 med=-38.8% | KEEP-only n=631 med=+50.9% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.92 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T150607Z

- UTC timestamp: `20260915T150607Z`
- GitHub run: [#10001](https://github.com/28twagg-ops/TradingBot/actions/runs/34986018589)
- Run id: `34986018589`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`114s`
- Full logs: `logs/action_runs/20260915T150607Z_live_bot.log`, `logs/action_runs/20260915T150607Z_live_options.log`, `logs/action_runs/20260915T150607Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1213 | 48.8 | -17.2 | +40.1 | $+15,687 |
| TAINTED | 1842 | 33.5 | -38.8 | +12.3 | $-9,127 |
| KEEP-only | 631 | 62.8 | +50.9 | +63.3 | $+10,674 |
| KEEP-only recent | 434 | 60.6 | +53.3 | +73.1 | $+6,029 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T11:06:14.864481-04:00","date":"2026-09-15","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":101.4,"phases_s":{"reconcile":0.42,"cancel":0.12,"manage":10.0,"protective_stops":1.81,"scan":52.93,"entries":24.08,"reconcile2":0.39},"signals":304,"placed":0,"equity":1000386.15,"open_positions":29,"pending_orders":24,"open_lots":149,"submitted_today":151,"filled_today":127,"unattributed_contracts":0,"top_signals":["S403:AMD","S165:COIN","S164:COIN","S168:COIN","S167:COIN","S166:COIN","S163:COIN","S350:COIN"],"github_run":"10001","github_run_id":"34986018589","status":"ok","data_quality":{"clean":{"n":1213,"win":48.8,"med":-17.24,"avg":40.12,"pnl":15686.55},"tainted":{"n":1842,"win":33.5,"med":-38.81,"avg":12.27,"pnl":-9126.84},"keep_only":{"n":631,"win":62.76,"med":50.94,"avg":63.29,"pnl":10674.45},"keep_only_recent":{"n":434,"win":60.6,"med":53.33,"avg":73.06,"pnl":6029.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:06:08  INFO      Mode: exits
15:06:09  INFO        Daily log -> logs/daily/2026-09-15.md
15:06:09  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
15:06:09  INFO        place_all_stops: checking 1 positions...
15:06:09  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:06:09  INFO        [positions] 1/1 (1 valid)
15:06:10  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.87|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.14                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T11:06:11.313083-04:00 share=25% ===
2026-09-15 11:06:11,313 INFO === options_live_micro LIVE 2026-09-15T11:06:11.313083-04:00 share=25% ===
Live account equity $224.87 cash $190.81 #225458845 options_level=3
2026-09-15 11:06:11,508 INFO Live account equity $224.87 cash $190.81 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 11:06:11,729 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 11:06:11,847 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (212 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 263 | 15 |
| S164 | 291 | 20 |
| S165 | 1727 | 32 |
| S166 | 135 | 9 |
| S167 | 285 | 19 |
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
| 2026-09-15 |    4 |   10 |   10 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    42 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |    10 | WARN | <<<
| Total open lots             |   149 | INFO |
| Total closed lots           |  2212 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1213 med=-17.2% | TAINTED n=1842 med=-38.8% | KEEP-only n=631 med=+50.9% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.87 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T151105Z

- UTC timestamp: `20260915T151105Z`
- GitHub run: [#10002](https://github.com/28twagg-ops/TradingBot/actions/runs/34986588843)
- Run id: `34986588843`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`92s`
- Full logs: `logs/action_runs/20260915T151105Z_live_bot.log`, `logs/action_runs/20260915T151105Z_live_options.log`, `logs/action_runs/20260915T151105Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1213 | 48.8 | -17.2 | +40.1 | $+15,687 |
| TAINTED | 1842 | 33.5 | -38.8 | +12.3 | $-9,127 |
| KEEP-only | 631 | 62.8 | +50.9 | +63.3 | $+10,674 |
| KEEP-only recent | 434 | 60.6 | +53.3 | +73.1 | $+6,029 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T11:11:13.095278-04:00","date":"2026-09-15","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":82.9,"phases_s":{"reconcile":0.81,"cancel":0.13,"manage":11.05,"protective_stops":1.99,"scan":34.99,"entries":24.89,"reconcile2":0.42},"signals":304,"placed":0,"equity":1000461.09,"open_positions":30,"pending_orders":22,"open_lots":151,"submitted_today":151,"filled_today":129,"unattributed_contracts":0,"top_signals":["S403:AMD","S165:COIN","S164:COIN","S168:COIN","S167:COIN","S166:COIN","S163:COIN","S350:COIN"],"github_run":"10002","github_run_id":"34986588843","status":"ok","data_quality":{"clean":{"n":1213,"win":48.8,"med":-17.24,"avg":40.12,"pnl":15686.55},"tainted":{"n":1842,"win":33.5,"med":-38.81,"avg":12.27,"pnl":-9126.84},"keep_only":{"n":631,"win":62.76,"med":50.94,"avg":63.29,"pnl":10674.45},"keep_only_recent":{"n":434,"win":60.6,"med":53.33,"avg":73.06,"pnl":6029.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:11:07  INFO      Mode: exits
15:11:07  INFO        Daily log -> logs/daily/2026-09-15.md
15:11:07  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
15:11:08  INFO        place_all_stops: checking 1 positions...
15:11:08  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:11:08  INFO        [positions] 1/1 (1 valid)
15:11:08  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.85|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.12                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T11:11:09.793045-04:00 share=25% ===
2026-09-15 11:11:09,793 INFO === options_live_micro LIVE 2026-09-15T11:11:09.793045-04:00 share=25% ===
Live account equity $224.85 cash $190.81 #225458845 options_level=3
2026-09-15 11:11:10,003 INFO Live account equity $224.85 cash $190.81 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 11:11:10,217 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 11:11:10,345 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (211 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 263 | 15 |
| S164 | 291 | 20 |
| S165 | 1727 | 32 |
| S166 | 135 | 9 |
| S167 | 285 | 19 |
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
| 2026-09-15 |    4 |   10 |   10 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    42 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |    10 | WARN | <<<
| Total open lots             |   151 | INFO |
| Total closed lots           |  2212 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1213 med=-17.2% | TAINTED n=1842 med=-38.8% | KEEP-only n=631 med=+50.9% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.85 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T151607Z

- UTC timestamp: `20260915T151607Z`
- GitHub run: [#10003](https://github.com/28twagg-ops/TradingBot/actions/runs/34987155664)
- Run id: `34987155664`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`108s`
- Full logs: `logs/action_runs/20260915T151607Z_live_bot.log`, `logs/action_runs/20260915T151607Z_live_options.log`, `logs/action_runs/20260915T151607Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1214 | 48.8 | -18.7 | +40.1 | $+15,663 |
| TAINTED | 1842 | 33.5 | -38.8 | +12.3 | $-9,127 |
| KEEP-only | 631 | 62.8 | +50.9 | +63.3 | $+10,674 |
| KEEP-only recent | 434 | 60.6 | +53.3 | +73.1 | $+6,029 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T11:16:12.951745-04:00","date":"2026-09-15","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":96.2,"phases_s":{"reconcile":0.12,"cancel":0.03,"manage":6.78,"protective_stops":0.37,"scan":54.41,"entries":21.49,"reconcile2":0.15},"signals":304,"placed":0,"equity":1000617.59,"open_positions":30,"pending_orders":22,"open_lots":150,"submitted_today":151,"filled_today":129,"unattributed_contracts":0,"top_signals":["S403:AMD","S165:COIN","S164:COIN","S168:COIN","S167:COIN","S166:COIN","S163:COIN","S350:COIN"],"github_run":"10003","github_run_id":"34987155664","status":"ok","data_quality":{"clean":{"n":1214,"win":48.76,"med":-18.7,"avg":40.06,"pnl":15662.55},"tainted":{"n":1842,"win":33.5,"med":-38.81,"avg":12.27,"pnl":-9126.84},"keep_only":{"n":631,"win":62.76,"med":50.94,"avg":63.29,"pnl":10674.45},"keep_only_recent":{"n":434,"win":60.6,"med":53.33,"avg":73.06,"pnl":6029.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:16:09  INFO      Mode: exits
15:16:09  INFO        Daily log -> logs/daily/2026-09-15.md
15:16:09  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
15:16:09  INFO        place_all_stops: checking 1 positions...
15:16:09  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:16:09  INFO        [positions] 1/1 (1 valid)
15:16:09  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.88|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.15                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T11:16:10.211666-04:00 share=25% ===
2026-09-15 11:16:10,211 INFO === options_live_micro LIVE 2026-09-15T11:16:10.211666-04:00 share=25% ===
Live account equity $224.88 cash $190.81 #225458845 options_level=3
2026-09-15 11:16:10,251 INFO Live account equity $224.88 cash $190.81 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 11:16:10,273 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 11:16:10,302 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (206 earlier lines - see full log file)

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 263 | 15 |
| S164 | 291 | 20 |
| S165 | 1727 | 32 |
| S166 | 135 | 9 |
| S167 | 285 | 19 |
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
| 2026-09-15 |    4 |   10 |   10 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    42 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |   150 | INFO |
| Total closed lots           |  2212 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1214 med=-18.7% | TAINTED n=1842 med=-38.8% | KEEP-only n=631 med=+50.9% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.88 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T152108Z

- UTC timestamp: `20260915T152108Z`
- GitHub run: [#10004](https://github.com/28twagg-ops/TradingBot/actions/runs/34987727230)
- Run id: `34987727230`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`146s`
- Full logs: `logs/action_runs/20260915T152108Z_live_bot.log`, `logs/action_runs/20260915T152108Z_live_options.log`, `logs/action_runs/20260915T152108Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1215 | 48.8 | -17.2 | +40.1 | $+15,702 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 632 | 62.8 | +51.0 | +63.3 | $+10,713 |
| KEEP-only recent | 435 | 60.7 | +53.3 | +73.1 | $+6,068 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T11:21:14.113891-04:00","date":"2026-09-15","mode":"entry+manage","header":"entry+manage (30 new)","elapsed_s":138.8,"phases_s":{"reconcile":0.37,"cancel":0.08,"manage":7.78,"protective_stops":1.28,"scan":28.43,"entries":88.48,"reconcile2":1.33},"signals":304,"placed":30,"equity":1000918.07,"open_positions":32,"pending_orders":26,"open_lots":174,"submitted_today":181,"filled_today":155,"unattributed_contracts":0,"top_signals":["S403:AMD","S165:COIN","S164:COIN","S168:COIN","S167:COIN","S166:COIN","S163:COIN","S350:COIN"],"github_run":"10004","github_run_id":"34987727230","status":"ok","data_quality":{"clean":{"n":1215,"win":48.81,"med":-17.24,"avg":40.08,"pnl":15701.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":632,"win":62.82,"med":50.96,"avg":63.3,"pnl":10713.45},"keep_only_recent":{"n":435,"win":60.69,"med":53.33,"avg":73.06,"pnl":6068.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:21:10  INFO      Mode: exits
15:21:10  INFO        Daily log -> logs/daily/2026-09-15.md
15:21:10  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
15:21:10  INFO        place_all_stops: checking 1 positions...
15:21:10  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:21:10  INFO        [positions] 1/1 (1 valid)
15:21:11  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.91|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.5%  $+0.18                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T11:21:11.665132-04:00 share=25% ===
2026-09-15 11:21:11,665 INFO === options_live_micro LIVE 2026-09-15T11:21:11.665132-04:00 share=25% ===
Live account equity $224.91 cash $190.81 #225458845 options_level=3
2026-09-15 11:21:11,804 INFO Live account equity $224.91 cash $190.81 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 11:21:11,920 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 11:21:11,993 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (227 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |    10 | WARN | <<<
| Total open lots             |   174 | INFO |
| Total closed lots           |  2215 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1215 med=-17.2% | TAINTED n=1844 med=-38.8% | KEEP-only n=632 med=+51.0% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.91 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T152604Z

- UTC timestamp: `20260915T152604Z`
- GitHub run: [#10005](https://github.com/28twagg-ops/TradingBot/actions/runs/34988295768)
- Run id: `34988295768`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`110s`
- Full logs: `logs/action_runs/20260915T152604Z_live_bot.log`, `logs/action_runs/20260915T152604Z_live_options.log`, `logs/action_runs/20260915T152604Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1219 | 48.9 | -17.2 | +40.1 | $+15,784 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 634 | 62.8 | +51.0 | +63.1 | $+10,734 |
| KEEP-only recent | 437 | 60.6 | +53.3 | +72.8 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T11:26:11.382610-04:00","date":"2026-09-15","mode":"entry+manage","header":"entry+manage (4 new)","elapsed_s":99.9,"phases_s":{"reconcile":0.39,"cancel":0.12,"manage":11.01,"protective_stops":2.93,"scan":34.87,"entries":37.46,"reconcile2":0.68},"signals":304,"placed":4,"equity":1001459.77,"open_positions":34,"pending_orders":26,"open_lots":174,"submitted_today":185,"filled_today":159,"unattributed_contracts":0,"top_signals":["S403:AMD","S165:COIN","S164:COIN","S168:COIN","S167:COIN","S166:COIN","S163:COIN","S350:COIN"],"github_run":"10005","github_run_id":"34988295768","status":"ok","data_quality":{"clean":{"n":1219,"win":48.89,"med":-17.19,"avg":40.05,"pnl":15783.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":634,"win":62.78,"med":50.96,"avg":63.13,"pnl":10734.45},"keep_only_recent":{"n":437,"win":60.64,"med":53.33,"avg":72.76,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:26:05  INFO      Mode: exits
15:26:06  INFO        Daily log -> logs/daily/2026-09-15.md
15:26:06  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
15:26:06  INFO        place_all_stops: checking 1 positions...
15:26:06  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:26:06  INFO        [positions] 1/1 (1 valid)
15:26:07  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.92|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.6%  $+0.19                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T11:26:07.919294-04:00 share=25% ===
2026-09-15 11:26:07,919 INFO === options_live_micro LIVE 2026-09-15T11:26:07.919294-04:00 share=25% ===
Live account equity $224.92 cash $190.81 #225458845 options_level=3
2026-09-15 11:26:08,144 INFO Live account equity $224.92 cash $190.81 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 11:26:08,433 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 11:26:08,567 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (210 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |    10 | WARN | <<<
| Total open lots             |   174 | INFO |
| Total closed lots           |  2219 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1219 med=-17.2% | TAINTED n=1844 med=-38.8% | KEEP-only n=634 med=+51.0% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.92 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T153119Z

- UTC timestamp: `20260915T153119Z`
- GitHub run: [#10006](https://github.com/28twagg-ops/TradingBot/actions/runs/34988858168)
- Run id: `34988858168`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`95s`
- Full logs: `logs/action_runs/20260915T153119Z_live_bot.log`, `logs/action_runs/20260915T153119Z_live_options.log`, `logs/action_runs/20260915T153119Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1222 | 49.0 | -15.9 | +40.1 | $+15,911 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 636 | 62.9 | +51.2 | +63.1 | $+10,819 |
| KEEP-only recent | 439 | 60.8 | +53.3 | +72.7 | $+6,174 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T11:31:24.994835-04:00","date":"2026-09-15","mode":"entry+manage","header":"entry+manage (4 new)","elapsed_s":86.2,"phases_s":{"reconcile":0.24,"cancel":0.08,"manage":12.3,"protective_stops":1.63,"scan":29.36,"entries":31.47,"reconcile2":0.36},"signals":304,"placed":4,"equity":1001000.07,"open_positions":33,"pending_orders":30,"open_lots":171,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":["S403:AMD","S165:COIN","S164:COIN","S168:COIN","S167:COIN","S166:COIN","S163:COIN","S350:COIN"],"github_run":"10006","github_run_id":"34988858168","status":"ok","data_quality":{"clean":{"n":1222,"win":49.02,"med":-15.93,"avg":40.11,"pnl":15910.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":636,"win":62.89,"med":51.18,"avg":63.15,"pnl":10819.45},"keep_only_recent":{"n":439,"win":60.82,"med":53.33,"avg":72.75,"pnl":6174.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:31:20  INFO      Mode: exits
15:31:21  INFO        Daily log -> logs/daily/2026-09-15.md
15:31:21  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
15:31:21  INFO        place_all_stops: checking 1 positions...
15:31:21  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:31:21  INFO        [positions] 1/1 (1 valid)
15:31:22  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.94|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.6%  $+0.21                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T11:31:22.560757-04:00 share=25% ===
2026-09-15 11:31:22,560 INFO === options_live_micro LIVE 2026-09-15T11:31:22.560757-04:00 share=25% ===
Live account equity $224.94 cash $190.81 #225458845 options_level=3
2026-09-15 11:31:22,699 INFO Live account equity $224.94 cash $190.81 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-15 11:31:22,807 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-15 11:31:22,882 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (212 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |   171 | INFO |
| Total closed lots           |  2221 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1222 med=-15.9% | TAINTED n=1844 med=-38.8% | KEEP-only n=636 med=+51.2% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.94 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T153609Z

- UTC timestamp: `20260915T153609Z`
- GitHub run: [#10007](https://github.com/28twagg-ops/TradingBot/actions/runs/34989419424)
- Run id: `34989419424`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`35s`
- Full logs: `logs/action_runs/20260915T153609Z_live_bot.log`, `logs/action_runs/20260915T153609Z_live_options.log`, `logs/action_runs/20260915T153609Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1222 | 49.0 | -15.9 | +40.1 | $+15,911 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 636 | 62.9 | +51.2 | +63.1 | $+10,819 |
| KEEP-only recent | 439 | 60.8 | +53.3 | +72.7 | $+6,174 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T11:36:17.851679-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":22.3,"phases_s":{"reconcile":0.54,"cancel":2.58,"manage":14.78,"protective_stops":3.6},"signals":0,"placed":0,"equity":1001112.89,"open_positions":31,"pending_orders":30,"open_lots":170,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10007","github_run_id":"34989419424","status":"ok","data_quality":{"clean":{"n":1222,"win":49.02,"med":-15.93,"avg":40.11,"pnl":15910.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":636,"win":62.89,"med":51.18,"avg":63.15,"pnl":10819.45},"keep_only_recent":{"n":439,"win":60.82,"med":53.33,"avg":72.75,"pnl":6174.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:36:10  INFO      Mode: exits
15:36:12  INFO        Daily log -> logs/daily/2026-09-15.md
15:36:12  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
15:36:12  INFO        place_all_stops: checking 1 positions...
15:36:12  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:36:12  INFO        [positions] 1/1 (1 valid)
15:36:12  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.91|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.5%  $+0.18                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T11:36:13.787822-04:00 share=25% ===
2026-09-15 11:36:13,787 INFO === options_live_micro LIVE 2026-09-15T11:36:13.787822-04:00 share=25% ===
Live account equity $224.91 cash $190.81 #225458845 options_level=3
2026-09-15 11:36:14,035 INFO Live account equity $224.91 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 11:36:14,260 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 11:36:14,335 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (198 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |   170 | INFO |
| Total closed lots           |  2221 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1222 med=-15.9% | TAINTED n=1844 med=-38.8% | KEEP-only n=636 med=+51.2% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.91 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T154204Z

- UTC timestamp: `20260915T154204Z`
- GitHub run: [#10008](https://github.com/28twagg-ops/TradingBot/actions/runs/34989966983)
- Run id: `34989966983`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`20s`
- Full logs: `logs/action_runs/20260915T154204Z_live_bot.log`, `logs/action_runs/20260915T154204Z_live_options.log`, `logs/action_runs/20260915T154204Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1226 | 49.2 | -10.1 | +40.2 | $+16,051 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 638 | 63.0 | +51.4 | +63.1 | $+10,905 |
| KEEP-only recent | 441 | 61.0 | +53.3 | +72.7 | $+6,260 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T11:42:10.199294-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":8.4,"phases_s":{"reconcile":0.56,"cancel":0.04,"manage":6.75,"protective_stops":0.44},"signals":0,"placed":0,"equity":1001009.89,"open_positions":28,"pending_orders":0,"open_lots":165,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10008","github_run_id":"34989966983","status":"ok","data_quality":{"clean":{"n":1226,"win":49.18,"med":-10.1,"avg":40.19,"pnl":16050.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":638,"win":63.01,"med":51.39,"avg":63.15,"pnl":10905.45},"keep_only_recent":{"n":441,"win":61.0,"med":53.33,"avg":72.7,"pnl":6260.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:42:05  INFO      Mode: exits
15:42:06  INFO        Daily log -> logs/daily/2026-09-15.md
15:42:06  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
15:42:06  INFO        place_all_stops: checking 1 positions...
15:42:06  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:42:06  INFO        [positions] 1/1 (1 valid)
15:42:06  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:42 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.98|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.7%  $+0.25                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T11:42:07.139872-04:00 share=25% ===
2026-09-15 11:42:07,139 INFO === options_live_micro LIVE 2026-09-15T11:42:07.139872-04:00 share=25% ===
Live account equity $224.98 cash $190.81 #225458845 options_level=3
2026-09-15 11:42:07,183 INFO Live account equity $224.98 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 11:42:07,206 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 11:42:07,213 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (182 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   165 | INFO |
| Total closed lots           |  2224 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1226 med=-10.1% | TAINTED n=1844 med=-38.8% | KEEP-only n=638 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.98 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T154611Z

- UTC timestamp: `20260915T154611Z`
- GitHub run: [#10009](https://github.com/28twagg-ops/TradingBot/actions/runs/34990518378)
- Run id: `34990518378`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`19s`
- Full logs: `logs/action_runs/20260915T154611Z_live_bot.log`, `logs/action_runs/20260915T154611Z_live_options.log`, `logs/action_runs/20260915T154611Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1227 | 49.2 | -7.7 | +40.2 | $+16,067 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 638 | 63.0 | +51.4 | +63.1 | $+10,905 |
| KEEP-only recent | 441 | 61.0 | +53.3 | +72.7 | $+6,260 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T11:46:17.582293-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.7,"phases_s":{"reconcile":0.2,"cancel":0.03,"manage":5.66,"protective_stops":0.29},"signals":0,"placed":0,"equity":1001213.8,"open_positions":27,"pending_orders":0,"open_lots":161,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10009","github_run_id":"34990518378","status":"ok","data_quality":{"clean":{"n":1227,"win":49.23,"med":-7.69,"avg":40.2,"pnl":16066.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":638,"win":63.01,"med":51.39,"avg":63.15,"pnl":10905.45},"keep_only_recent":{"n":441,"win":61.0,"med":53.33,"avg":72.7,"pnl":6260.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:46:12  INFO      Mode: exits
15:46:12  INFO        Daily log -> logs/daily/2026-09-15.md
15:46:12  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
15:46:12  INFO        place_all_stops: checking 1 positions...
15:46:12  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:46:13  INFO        [positions] 1/1 (1 valid)
15:46:13  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.99|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.8%  $+0.26                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T11:46:14.151231-04:00 share=25% ===
2026-09-15 11:46:14,151 INFO === options_live_micro LIVE 2026-09-15T11:46:14.151231-04:00 share=25% ===
Live account equity $224.99 cash $190.81 #225458845 options_level=3
2026-09-15 11:46:14,204 INFO Live account equity $224.99 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 11:46:14,273 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 11:46:14,283 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (179 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   161 | INFO |
| Total closed lots           |  2224 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1227 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=638 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.99 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T155119Z

- UTC timestamp: `20260915T155119Z`
- GitHub run: [#10010](https://github.com/28twagg-ops/TradingBot/actions/runs/34991068432)
- Run id: `34991068432`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`20s`
- Full logs: `logs/action_runs/20260915T155119Z_live_bot.log`, `logs/action_runs/20260915T155119Z_live_options.log`, `logs/action_runs/20260915T155119Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1227 | 49.2 | -7.7 | +40.2 | $+16,067 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 638 | 63.0 | +51.4 | +63.1 | $+10,905 |
| KEEP-only recent | 441 | 61.0 | +53.3 | +72.7 | $+6,260 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T11:51:27.346715-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":10.3,"phases_s":{"reconcile":0.49,"cancel":0.14,"manage":7.69,"protective_stops":1.25},"signals":0,"placed":0,"equity":1001589.3,"open_positions":27,"pending_orders":0,"open_lots":161,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10010","github_run_id":"34991068432","status":"ok","data_quality":{"clean":{"n":1227,"win":49.23,"med":-7.69,"avg":40.2,"pnl":16066.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":638,"win":63.01,"med":51.39,"avg":63.15,"pnl":10905.45},"keep_only_recent":{"n":441,"win":61.0,"med":53.33,"avg":72.7,"pnl":6260.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:51:22  INFO      Mode: exits
15:51:22  INFO        Daily log -> logs/daily/2026-09-15.md
15:51:22  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
15:51:22  INFO        place_all_stops: checking 1 positions...
15:51:22  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:51:23  INFO        [positions] 1/1 (1 valid)
15:51:23  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.93|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.6%  $+0.20                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T11:51:24.239661-04:00 share=25% ===
2026-09-15 11:51:24,239 INFO === options_live_micro LIVE 2026-09-15T11:51:24.239661-04:00 share=25% ===
Live account equity $224.93 cash $190.81 #225458845 options_level=3
2026-09-15 11:51:24,571 INFO Live account equity $224.93 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 11:51:24,784 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 11:51:24,821 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (176 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   161 | INFO |
| Total closed lots           |  2224 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1227 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=638 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.93 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T155611Z

- UTC timestamp: `20260915T155611Z`
- GitHub run: [#10011](https://github.com/28twagg-ops/TradingBot/actions/runs/34991618370)
- Run id: `34991618370`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`26s`
- Full logs: `logs/action_runs/20260915T155611Z_live_bot.log`, `logs/action_runs/20260915T155611Z_live_options.log`, `logs/action_runs/20260915T155611Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1228 | 49.3 | -7.7 | +40.2 | $+16,089 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 639 | 63.1 | +51.4 | +63.1 | $+10,927 |
| KEEP-only recent | 442 | 61.1 | +53.3 | +72.7 | $+6,282 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T11:56:19.427206-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":13.9,"phases_s":{"reconcile":0.53,"cancel":0.22,"manage":10.24,"protective_stops":2.16},"signals":0,"placed":0,"equity":1001719.78,"open_positions":27,"pending_orders":0,"open_lots":160,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10011","github_run_id":"34991618370","status":"ok","data_quality":{"clean":{"n":1228,"win":49.27,"med":-7.69,"avg":40.21,"pnl":16088.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":639,"win":63.07,"med":51.39,"avg":63.14,"pnl":10927.45},"keep_only_recent":{"n":442,"win":61.09,"med":53.33,"avg":72.67,"pnl":6282.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:56:12  INFO      Mode: exits
15:56:13  INFO        Daily log -> logs/daily/2026-09-15.md
15:56:13  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
15:56:14  INFO        place_all_stops: checking 1 positions...
15:56:14  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:56:14  INFO        [positions] 1/1 (1 valid)
15:56:14  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.87|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.14                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T11:56:15.637785-04:00 share=25% ===
2026-09-15 11:56:15,637 INFO === options_live_micro LIVE 2026-09-15T11:56:15.637785-04:00 share=25% ===
Live account equity $224.87 cash $190.81 #225458845 options_level=3
2026-09-15 11:56:15,873 INFO Live account equity $224.87 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 11:56:16,102 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 11:56:16,315 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   160 | INFO |
| Total closed lots           |  2225 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1228 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=639 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.87 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T160107Z

- UTC timestamp: `20260915T160107Z`
- GitHub run: [#10012](https://github.com/28twagg-ops/TradingBot/actions/runs/34992158722)
- Run id: `34992158722`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`25s`
- Full logs: `logs/action_runs/20260915T160107Z_live_bot.log`, `logs/action_runs/20260915T160107Z_live_options.log`, `logs/action_runs/20260915T160107Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1228 | 49.3 | -7.7 | +40.2 | $+16,089 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 639 | 63.1 | +51.4 | +63.1 | $+10,927 |
| KEEP-only recent | 442 | 61.1 | +53.3 | +72.7 | $+6,282 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T12:01:14.051030-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":13.4,"phases_s":{"reconcile":0.42,"cancel":0.19,"manage":10.26,"protective_stops":1.71},"signals":0,"placed":0,"equity":1001914.78,"open_positions":27,"pending_orders":0,"open_lots":160,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10012","github_run_id":"34992158722","status":"ok","data_quality":{"clean":{"n":1228,"win":49.27,"med":-7.69,"avg":40.21,"pnl":16088.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":639,"win":63.07,"med":51.39,"avg":63.14,"pnl":10927.45},"keep_only_recent":{"n":442,"win":61.09,"med":53.33,"avg":72.67,"pnl":6282.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:01:08  INFO      Mode: exits
16:01:08  INFO        Daily log -> logs/daily/2026-09-15.md
16:01:08  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
16:01:08  INFO        place_all_stops: checking 1 positions...
16:01:08  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:01:09  INFO        [positions] 1/1 (1 valid)
16:01:09  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.85|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.12                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T12:01:10.611718-04:00 share=25% ===
2026-09-15 12:01:10,611 INFO === options_live_micro LIVE 2026-09-15T12:01:10.611718-04:00 share=25% ===
Live account equity $224.85 cash $190.81 #225458845 options_level=3
2026-09-15 12:01:10,821 INFO Live account equity $224.85 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 12:01:11,034 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 12:01:11,096 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (176 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   160 | INFO |
| Total closed lots           |  2225 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1228 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=639 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.85 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T160606Z

- UTC timestamp: `20260915T160606Z`
- GitHub run: [#10013](https://github.com/28twagg-ops/TradingBot/actions/runs/34992712378)
- Run id: `34992712378`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`20s`
- Full logs: `logs/action_runs/20260915T160606Z_live_bot.log`, `logs/action_runs/20260915T160606Z_live_options.log`, `logs/action_runs/20260915T160606Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1228 | 49.3 | -7.7 | +40.2 | $+16,089 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 639 | 63.1 | +51.4 | +63.1 | $+10,927 |
| KEEP-only recent | 442 | 61.1 | +53.3 | +72.7 | $+6,282 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T12:06:12.306906-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":7.6,"phases_s":{"reconcile":0.18,"cancel":0.04,"manage":6.37,"protective_stops":0.42},"signals":0,"placed":0,"equity":1001910.78,"open_positions":27,"pending_orders":0,"open_lots":160,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10013","github_run_id":"34992712378","status":"ok","data_quality":{"clean":{"n":1228,"win":49.27,"med":-7.69,"avg":40.21,"pnl":16088.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":639,"win":63.07,"med":51.39,"avg":63.14,"pnl":10927.45},"keep_only_recent":{"n":442,"win":61.09,"med":53.33,"avg":72.67,"pnl":6282.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:06:07  INFO      Mode: exits
16:06:08  INFO        Daily log -> logs/daily/2026-09-15.md
16:06:08  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
16:06:08  INFO        place_all_stops: checking 1 positions...
16:06:08  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:06:08  INFO        [positions] 1/1 (1 valid)
16:06:08  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.82|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.3%  $+0.09                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T12:06:09.097461-04:00 share=25% ===
2026-09-15 12:06:09,097 INFO === options_live_micro LIVE 2026-09-15T12:06:09.097461-04:00 share=25% ===
Live account equity $224.82 cash $190.81 #225458845 options_level=3
2026-09-15 12:06:09,310 INFO Live account equity $224.82 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 12:06:09,343 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 12:06:09,355 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (175 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   160 | INFO |
| Total closed lots           |  2225 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1228 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=639 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.82 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T161110Z

- UTC timestamp: `20260915T161110Z`
- GitHub run: [#10014](https://github.com/28twagg-ops/TradingBot/actions/runs/34993251316)
- Run id: `34993251316`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260915T161110Z_live_bot.log`, `logs/action_runs/20260915T161110Z_live_options.log`, `logs/action_runs/20260915T161110Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T12:11:16.122431-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":11.6,"phases_s":{"reconcile":0.86,"cancel":0.13,"manage":8.72,"protective_stops":1.1},"signals":0,"placed":0,"equity":1001896.76,"open_positions":27,"pending_orders":0,"open_lots":159,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10014","github_run_id":"34993251316","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:11:11  INFO      Mode: exits
16:11:11  INFO        Daily log -> logs/daily/2026-09-15.md
16:11:11  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
16:11:11  INFO        place_all_stops: checking 1 positions...
16:11:11  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:11:12  INFO        [positions] 1/1 (1 valid)
16:11:12  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.82|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.3%  $+0.09                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T12:11:12.955963-04:00 share=25% ===
2026-09-15 12:11:12,956 INFO === options_live_micro LIVE 2026-09-15T12:11:12.955963-04:00 share=25% ===
Live account equity $224.82 cash $190.81 #225458845 options_level=3
2026-09-15 12:11:13,101 INFO Live account equity $224.82 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 12:11:13,241 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 12:11:13,279 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (176 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   159 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.82 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T161609Z

- UTC timestamp: `20260915T161609Z`
- GitHub run: [#10015](https://github.com/28twagg-ops/TradingBot/actions/runs/34993790404)
- Run id: `34993790404`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`18s`
- Full logs: `logs/action_runs/20260915T161609Z_live_bot.log`, `logs/action_runs/20260915T161609Z_live_options.log`, `logs/action_runs/20260915T161609Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T12:16:14.602592-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":9.4,"phases_s":{"reconcile":0.3,"cancel":0.11,"manage":7.4,"protective_stops":0.99},"signals":0,"placed":0,"equity":1001898.73,"open_positions":26,"pending_orders":0,"open_lots":158,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10015","github_run_id":"34993790404","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:16:10  INFO      Mode: exits
16:16:10  INFO        Daily log -> logs/daily/2026-09-15.md
16:16:10  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
16:16:10  INFO        place_all_stops: checking 1 positions...
16:16:10  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:16:11  INFO        [positions] 1/1 (1 valid)
16:16:11  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.79|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.2%  $+0.06                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T12:16:11.972786-04:00 share=25% ===
2026-09-15 12:16:11,972 INFO === options_live_micro LIVE 2026-09-15T12:16:11.972786-04:00 share=25% ===
Live account equity $224.79 cash $190.81 #225458845 options_level=3
2026-09-15 12:16:12,108 INFO Live account equity $224.79 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 12:16:12,225 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 12:16:12,263 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (176 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   158 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.79 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T162109Z

- UTC timestamp: `20260915T162109Z`
- GitHub run: [#10016](https://github.com/28twagg-ops/TradingBot/actions/runs/34994321226)
- Run id: `34994321226`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`23s`
- Full logs: `logs/action_runs/20260915T162109Z_live_bot.log`, `logs/action_runs/20260915T162109Z_live_options.log`, `logs/action_runs/20260915T162109Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T12:21:17.082197-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":11.4,"phases_s":{"reconcile":0.41,"cancel":0.18,"manage":8.54,"protective_stops":1.59},"signals":0,"placed":0,"equity":1002009.74,"open_positions":26,"pending_orders":0,"open_lots":158,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10016","github_run_id":"34994321226","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:21:10  INFO      Mode: exits
16:21:11  INFO        Daily log -> logs/daily/2026-09-15.md
16:21:11  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
16:21:11  INFO        place_all_stops: checking 1 positions...
16:21:11  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:21:11  INFO        [positions] 1/1 (1 valid)
16:21:12  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.77|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.1%  $+0.04                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T12:21:13.493647-04:00 share=25% ===
2026-09-15 12:21:13,493 INFO === options_live_micro LIVE 2026-09-15T12:21:13.493647-04:00 share=25% ===
Live account equity $224.77 cash $190.81 #225458845 options_level=3
2026-09-15 12:21:13,699 INFO Live account equity $224.77 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 12:21:13,870 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 12:21:13,927 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   158 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.77 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T162605Z

- UTC timestamp: `20260915T162605Z`
- GitHub run: [#10017](https://github.com/28twagg-ops/TradingBot/actions/runs/34994851346)
- Run id: `34994851346`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`22s`
- Full logs: `logs/action_runs/20260915T162605Z_live_bot.log`, `logs/action_runs/20260915T162605Z_live_options.log`, `logs/action_runs/20260915T162605Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T12:26:11.558979-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":11.7,"phases_s":{"reconcile":0.44,"cancel":0.19,"manage":8.53,"protective_stops":1.69},"signals":0,"placed":0,"equity":1002254.74,"open_positions":26,"pending_orders":0,"open_lots":158,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10017","github_run_id":"34994851346","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:26:06  INFO      Mode: exits
16:26:06  INFO        Daily log -> logs/daily/2026-09-15.md
16:26:06  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
16:26:07  INFO        place_all_stops: checking 1 positions...
16:26:07  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:26:07  INFO        [positions] 1/1 (1 valid)
16:26:07  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.83|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.3%  $+0.10                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T12:26:08.221378-04:00 share=25% ===
2026-09-15 12:26:08,221 INFO === options_live_micro LIVE 2026-09-15T12:26:08.221378-04:00 share=25% ===
Live account equity $224.83 cash $190.81 #225458845 options_level=3
2026-09-15 12:26:08,404 INFO Live account equity $224.83 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 12:26:08,603 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 12:26:08,660 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   158 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.83 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T163123Z

- UTC timestamp: `20260915T163123Z`
- GitHub run: [#10018](https://github.com/28twagg-ops/TradingBot/actions/runs/34995379345)
- Run id: `34995379345`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`22s`
- Full logs: `logs/action_runs/20260915T163123Z_live_bot.log`, `logs/action_runs/20260915T163123Z_live_options.log`, `logs/action_runs/20260915T163123Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T12:31:31.060552-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":12.1,"phases_s":{"reconcile":0.67,"cancel":0.19,"manage":8.7,"protective_stops":1.7},"signals":0,"placed":0,"equity":1002296.74,"open_positions":26,"pending_orders":0,"open_lots":158,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10018","github_run_id":"34995379345","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:31:25  INFO      Mode: exits
16:31:25  INFO        Daily log -> logs/daily/2026-09-15.md
16:31:25  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
16:31:26  INFO        place_all_stops: checking 1 positions...
16:31:26  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:31:26  INFO        [positions] 1/1 (1 valid)
16:31:26  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.87|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.14                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T12:31:27.736886-04:00 share=25% ===
2026-09-15 12:31:27,736 INFO === options_live_micro LIVE 2026-09-15T12:31:27.736886-04:00 share=25% ===
Live account equity $224.87 cash $190.81 #225458845 options_level=3
2026-09-15 12:31:27,941 INFO Live account equity $224.87 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 12:31:28,198 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 12:31:28,257 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   158 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.87 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T163653Z

- UTC timestamp: `20260915T163653Z`
- GitHub run: [#10019](https://github.com/28twagg-ops/TradingBot/actions/runs/34995913298)
- Run id: `34995913298`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`22s`
- Full logs: `logs/action_runs/20260915T163653Z_live_bot.log`, `logs/action_runs/20260915T163653Z_live_options.log`, `logs/action_runs/20260915T163653Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T12:36:59.637654-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":9.8,"phases_s":{"reconcile":0.17,"cancel":0.08,"manage":8.31,"protective_stops":0.68},"signals":0,"placed":0,"equity":1002300.24,"open_positions":26,"pending_orders":0,"open_lots":158,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10019","github_run_id":"34995913298","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:36:54  INFO      Mode: exits
16:36:54  INFO        Daily log -> logs/daily/2026-09-15.md
16:36:54  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
16:36:54  INFO        place_all_stops: checking 1 positions...
16:36:54  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:36:54  INFO        [positions] 1/1 (1 valid)
16:36:55  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.83|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.3%  $+0.10                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T12:36:56.503678-04:00 share=25% ===
2026-09-15 12:36:56,503 INFO === options_live_micro LIVE 2026-09-15T12:36:56.503678-04:00 share=25% ===
Live account equity $224.83 cash $190.81 #225458845 options_level=3
2026-09-15 12:36:56,606 INFO Live account equity $224.83 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 12:36:56,714 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 12:36:56,753 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   158 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.83 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T164138Z

- UTC timestamp: `20260915T164138Z`
- GitHub run: [#10020](https://github.com/28twagg-ops/TradingBot/actions/runs/34996428705)
- Run id: `34996428705`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`18s`
- Full logs: `logs/action_runs/20260915T164138Z_live_bot.log`, `logs/action_runs/20260915T164138Z_live_options.log`, `logs/action_runs/20260915T164138Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T12:41:43.431729-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.2,"phases_s":{"reconcile":0.09,"cancel":0.04,"manage":5.21,"protective_stops":0.25},"signals":0,"placed":0,"equity":1002190.74,"open_positions":26,"pending_orders":0,"open_lots":158,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10020","github_run_id":"34996428705","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:41:39  INFO      Mode: exits
16:41:39  INFO        Daily log -> logs/daily/2026-09-15.md
16:41:39  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
16:41:39  INFO        place_all_stops: checking 1 positions...
16:41:39  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:41:39  INFO        [positions] 1/1 (1 valid)
16:41:39  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.79|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.2%  $+0.06                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T12:41:40.274493-04:00 share=25% ===
2026-09-15 12:41:40,274 INFO === options_live_micro LIVE 2026-09-15T12:41:40.274493-04:00 share=25% ===
Live account equity $224.79 cash $190.81 #225458845 options_level=3
2026-09-15 12:41:40,328 INFO Live account equity $224.79 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 12:41:40,393 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 12:41:40,403 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   158 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.79 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T164608Z

- UTC timestamp: `20260915T164608Z`
- GitHub run: [#10021](https://github.com/28twagg-ops/TradingBot/actions/runs/34996954412)
- Run id: `34996954412`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`20s`
- Full logs: `logs/action_runs/20260915T164608Z_live_bot.log`, `logs/action_runs/20260915T164608Z_live_options.log`, `logs/action_runs/20260915T164608Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T12:46:13.540514-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":8.5,"phases_s":{"reconcile":0.23,"cancel":0.09,"manage":6.35,"protective_stops":0.81},"signals":0,"placed":0,"equity":1002038.74,"open_positions":26,"pending_orders":0,"open_lots":158,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10021","github_run_id":"34996954412","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:46:09  INFO      Mode: exits
16:46:09  INFO        Daily log -> logs/daily/2026-09-15.md
16:46:09  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
16:46:09  INFO        place_all_stops: checking 1 positions...
16:46:09  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:46:09  INFO        [positions] 1/1 (1 valid)
16:46:09  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.85|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.12                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T12:46:10.608763-04:00 share=25% ===
2026-09-15 12:46:10,608 INFO === options_live_micro LIVE 2026-09-15T12:46:10.608763-04:00 share=25% ===
Live account equity $224.85 cash $190.81 #225458845 options_level=3
2026-09-15 12:46:10,705 INFO Live account equity $224.85 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 12:46:10,767 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 12:46:10,817 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   158 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.85 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T165102Z

- UTC timestamp: `20260915T165102Z`
- GitHub run: [#10022](https://github.com/28twagg-ops/TradingBot/actions/runs/34997472554)
- Run id: `34997472554`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`16s`
- Full logs: `logs/action_runs/20260915T165102Z_live_bot.log`, `logs/action_runs/20260915T165102Z_live_options.log`, `logs/action_runs/20260915T165102Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T12:51:06.683110-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.2,"phases_s":{"reconcile":0.1,"cancel":0.04,"manage":5.4,"protective_stops":0.25},"signals":0,"placed":0,"equity":1002040.74,"open_positions":26,"pending_orders":0,"open_lots":158,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10022","github_run_id":"34997472554","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:51:03  INFO      Mode: exits
16:51:03  INFO        Daily log -> logs/daily/2026-09-15.md
16:51:03  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
16:51:03  INFO        place_all_stops: checking 1 positions...
16:51:03  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:51:03  INFO        [positions] 1/1 (1 valid)
16:51:03  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.83|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.3%  $+0.10                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T12:51:04.496214-04:00 share=25% ===
2026-09-15 12:51:04,496 INFO === options_live_micro LIVE 2026-09-15T12:51:04.496214-04:00 share=25% ===
Live account equity $224.83 cash $190.81 #225458845 options_level=3
2026-09-15 12:51:04,540 INFO Live account equity $224.83 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 12:51:04,562 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 12:51:04,569 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   158 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.83 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T165644Z

- UTC timestamp: `20260915T165644Z`
- GitHub run: [#10023](https://github.com/28twagg-ops/TradingBot/actions/runs/34997984134)
- Run id: `34997984134`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`20s`
- Full logs: `logs/action_runs/20260915T165644Z_live_bot.log`, `logs/action_runs/20260915T165644Z_live_options.log`, `logs/action_runs/20260915T165644Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T12:56:50.133950-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":7.8,"phases_s":{"reconcile":0.22,"cancel":0.08,"manage":6.24,"protective_stops":0.66},"signals":0,"placed":0,"equity":1001999.74,"open_positions":26,"pending_orders":0,"open_lots":158,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10023","github_run_id":"34997984134","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:56:45  INFO      Mode: exits
16:56:45  INFO        Daily log -> logs/daily/2026-09-15.md
16:56:45  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
16:56:45  INFO        place_all_stops: checking 1 positions...
16:56:45  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:56:45  INFO        [positions] 1/1 (1 valid)
16:56:45  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.88|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.15                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T12:56:46.813943-04:00 share=25% ===
2026-09-15 12:56:46,814 INFO === options_live_micro LIVE 2026-09-15T12:56:46.813943-04:00 share=25% ===
Live account equity $224.88 cash $190.81 #225458845 options_level=3
2026-09-15 12:56:46,911 INFO Live account equity $224.88 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 12:56:46,980 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 12:56:47,002 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   158 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.88 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T170110Z

- UTC timestamp: `20260915T170110Z`
- GitHub run: [#10024](https://github.com/28twagg-ops/TradingBot/actions/runs/34998491033)
- Run id: `34998491033`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`22s`
- Full logs: `logs/action_runs/20260915T170110Z_live_bot.log`, `logs/action_runs/20260915T170110Z_live_options.log`, `logs/action_runs/20260915T170110Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T13:01:17.889522-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":11.0,"phases_s":{"reconcile":0.31,"cancel":0.13,"manage":8.65,"protective_stops":1.22},"signals":0,"placed":0,"equity":1001962.24,"open_positions":26,"pending_orders":0,"open_lots":158,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10024","github_run_id":"34998491033","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:01:12  INFO      Mode: exits
17:01:12  INFO        Daily log -> logs/daily/2026-09-15.md
17:01:12  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
17:01:12  INFO        place_all_stops: checking 1 positions...
17:01:12  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:01:12  INFO        [positions] 1/1 (1 valid)
17:01:13  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.90|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.5%  $+0.17                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T13:01:14.292228-04:00 share=25% ===
2026-09-15 13:01:14,292 INFO === options_live_micro LIVE 2026-09-15T13:01:14.292228-04:00 share=25% ===
Live account equity $224.90 cash $190.81 #225458845 options_level=3
2026-09-15 13:01:14,452 INFO Live account equity $224.90 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 13:01:14,648 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 13:01:14,689 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   158 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.9 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T170608Z

- UTC timestamp: `20260915T170608Z`
- GitHub run: [#10025](https://github.com/28twagg-ops/TradingBot/actions/runs/34999018326)
- Run id: `34999018326`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`20s`
- Full logs: `logs/action_runs/20260915T170608Z_live_bot.log`, `logs/action_runs/20260915T170608Z_live_options.log`, `logs/action_runs/20260915T170608Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T13:06:14.826865-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":8.8,"phases_s":{"reconcile":0.23,"cancel":0.04,"manage":7.54,"protective_stops":0.39},"signals":0,"placed":0,"equity":1001976.74,"open_positions":26,"pending_orders":0,"open_lots":158,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10025","github_run_id":"34999018326","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:06:09  INFO      Mode: exits
17:06:10  INFO        Daily log -> logs/daily/2026-09-15.md
17:06:10  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
17:06:10  INFO        place_all_stops: checking 1 positions...
17:06:10  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:06:10  INFO        [positions] 1/1 (1 valid)
17:06:10  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.88|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.15                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T13:06:11.923168-04:00 share=25% ===
2026-09-15 13:06:11,923 INFO === options_live_micro LIVE 2026-09-15T13:06:11.923168-04:00 share=25% ===
Live account equity $224.88 cash $190.81 #225458845 options_level=3
2026-09-15 13:06:11,984 INFO Live account equity $224.88 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 13:06:12,101 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 13:06:12,114 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   158 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.88 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T171111Z

- UTC timestamp: `20260915T171111Z`
- GitHub run: [#10026](https://github.com/28twagg-ops/TradingBot/actions/runs/34999540776)
- Run id: `34999540776`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`18s`
- Full logs: `logs/action_runs/20260915T171111Z_live_bot.log`, `logs/action_runs/20260915T171111Z_live_options.log`, `logs/action_runs/20260915T171111Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T13:11:17.038378-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.6,"phases_s":{"reconcile":0.25,"cancel":0.03,"manage":5.48,"protective_stops":0.33},"signals":0,"placed":0,"equity":1001793.78,"open_positions":25,"pending_orders":0,"open_lots":156,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10026","github_run_id":"34999540776","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:11:12  INFO      Mode: exits
17:11:12  INFO        Daily log -> logs/daily/2026-09-15.md
17:11:12  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
17:11:12  INFO        place_all_stops: checking 1 positions...
17:11:12  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:11:12  INFO        [positions] 1/1 (1 valid)
17:11:12  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.84|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.3%  $+0.11                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T13:11:14.077496-04:00 share=25% ===
2026-09-15 13:11:14,077 INFO === options_live_micro LIVE 2026-09-15T13:11:14.077496-04:00 share=25% ===
Live account equity $224.84 cash $190.81 #225458845 options_level=3
2026-09-15 13:11:14,121 INFO Live account equity $224.84 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 13:11:14,190 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 13:11:14,198 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (177 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.84 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T171613Z

- UTC timestamp: `20260915T171613Z`
- GitHub run: [#10027](https://github.com/28twagg-ops/TradingBot/actions/runs/35000068611)
- Run id: `35000068611`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`18s`
- Full logs: `logs/action_runs/20260915T171613Z_live_bot.log`, `logs/action_runs/20260915T171613Z_live_options.log`, `logs/action_runs/20260915T171613Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T13:16:19.551600-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.5,"phases_s":{"reconcile":0.17,"cancel":0.03,"manage":5.47,"protective_stops":0.24},"signals":0,"placed":0,"equity":1001729.7,"open_positions":25,"pending_orders":0,"open_lots":156,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10027","github_run_id":"35000068611","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:16:14  INFO      Mode: exits
17:16:15  INFO        Daily log -> logs/daily/2026-09-15.md
17:16:15  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
17:16:15  INFO        place_all_stops: checking 1 positions...
17:16:15  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:16:15  INFO        [positions] 1/1 (1 valid)
17:16:15  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.79|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.2%  $+0.06                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T13:16:16.581805-04:00 share=25% ===
2026-09-15 13:16:16,581 INFO === options_live_micro LIVE 2026-09-15T13:16:16.581805-04:00 share=25% ===
Live account equity $224.79 cash $190.81 #225458845 options_level=3
2026-09-15 13:16:16,625 INFO Live account equity $224.79 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 13:16:16,693 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 13:16:16,724 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.79 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T172120Z

- UTC timestamp: `20260915T172120Z`
- GitHub run: [#10028](https://github.com/28twagg-ops/TradingBot/actions/runs/35000599065)
- Run id: `35000599065`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`25s`
- Full logs: `logs/action_runs/20260915T172120Z_live_bot.log`, `logs/action_runs/20260915T172120Z_live_options.log`, `logs/action_runs/20260915T172120Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T13:21:30.078067-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":13.2,"phases_s":{"reconcile":0.52,"cancel":0.22,"manage":9.74,"protective_stops":1.9},"signals":0,"placed":0,"equity":1001424.7,"open_positions":25,"pending_orders":0,"open_lots":156,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10028","github_run_id":"35000599065","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:21:22  INFO      Mode: exits
17:21:24  INFO        Daily log -> logs/daily/2026-09-15.md
17:21:24  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
17:21:24  INFO        place_all_stops: checking 1 positions...
17:21:24  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:21:24  INFO        [positions] 1/1 (1 valid)
17:21:25  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.79|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.2%  $+0.06                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T13:21:26.140070-04:00 share=25% ===
2026-09-15 13:21:26,140 INFO === options_live_micro LIVE 2026-09-15T13:21:26.140070-04:00 share=25% ===
Live account equity $224.79 cash $190.81 #225458845 options_level=3
2026-09-15 13:21:26,646 INFO Live account equity $224.79 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 13:21:26,891 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 13:21:26,962 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.79 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T172621Z

- UTC timestamp: `20260915T172621Z`
- GitHub run: [#10029](https://github.com/28twagg-ops/TradingBot/actions/runs/35001125605)
- Run id: `35001125605`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`22s`
- Full logs: `logs/action_runs/20260915T172621Z_live_bot.log`, `logs/action_runs/20260915T172621Z_live_options.log`, `logs/action_runs/20260915T172621Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T13:26:28.247200-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":11.3,"phases_s":{"reconcile":0.41,"cancel":0.19,"manage":8.39,"protective_stops":1.62},"signals":0,"placed":0,"equity":1001272.7,"open_positions":25,"pending_orders":0,"open_lots":156,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10029","github_run_id":"35001125605","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:26:22  INFO      Mode: exits
17:26:23  INFO        Daily log -> logs/daily/2026-09-15.md
17:26:23  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
17:26:23  INFO        place_all_stops: checking 1 positions...
17:26:23  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:26:23  INFO        [positions] 1/1 (1 valid)
17:26:24  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.84|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.3%  $+0.11                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T13:26:24.927927-04:00 share=25% ===
2026-09-15 13:26:24,927 INFO === options_live_micro LIVE 2026-09-15T13:26:24.927927-04:00 share=25% ===
Live account equity $224.84 cash $190.81 #225458845 options_level=3
2026-09-15 13:26:25,132 INFO Live account equity $224.84 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 13:26:25,306 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 13:26:25,366 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.84 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T173110Z

- UTC timestamp: `20260915T173110Z`
- GitHub run: [#10030](https://github.com/28twagg-ops/TradingBot/actions/runs/35001651806)
- Run id: `35001651806`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`18s`
- Full logs: `logs/action_runs/20260915T173110Z_live_bot.log`, `logs/action_runs/20260915T173110Z_live_options.log`, `logs/action_runs/20260915T173110Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T13:31:16.192572-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.9,"phases_s":{"reconcile":0.2,"cancel":0.03,"manage":5.91,"protective_stops":0.24},"signals":0,"placed":0,"equity":1001143.45,"open_positions":25,"pending_orders":0,"open_lots":156,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10030","github_run_id":"35001651806","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:31:11  INFO      Mode: exits
17:31:11  INFO        Daily log -> logs/daily/2026-09-15.md
17:31:11  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
17:31:11  INFO        place_all_stops: checking 1 positions...
17:31:11  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:31:12  INFO        [positions] 1/1 (1 valid)
17:31:12  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.84|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.3%  $+0.11                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T13:31:13.007782-04:00 share=25% ===
2026-09-15 13:31:13,007 INFO === options_live_micro LIVE 2026-09-15T13:31:13.007782-04:00 share=25% ===
Live account equity $224.84 cash $190.81 #225458845 options_level=3
2026-09-15 13:31:13,153 INFO Live account equity $224.84 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 13:31:13,188 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 13:31:13,196 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.84 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T173611Z

- UTC timestamp: `20260915T173611Z`
- GitHub run: [#10031](https://github.com/28twagg-ops/TradingBot/actions/runs/35002175791)
- Run id: `35002175791`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260915T173611Z_live_bot.log`, `logs/action_runs/20260915T173611Z_live_options.log`, `logs/action_runs/20260915T173611Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T13:36:18.055445-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":7.3,"phases_s":{"reconcile":0.14,"cancel":0.04,"manage":6.12,"protective_stops":0.38},"signals":0,"placed":0,"equity":1001589.71,"open_positions":25,"pending_orders":0,"open_lots":156,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10031","github_run_id":"35002175791","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:36:12  INFO      Mode: exits
17:36:13  INFO        Daily log -> logs/daily/2026-09-15.md
17:36:13  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
17:36:13  INFO        place_all_stops: checking 1 positions...
17:36:13  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:36:13  INFO        [positions] 1/1 (1 valid)
17:36:13  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.87|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.14                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T13:36:14.588292-04:00 share=25% ===
2026-09-15 13:36:14,588 INFO === options_live_micro LIVE 2026-09-15T13:36:14.588292-04:00 share=25% ===
Live account equity $224.87 cash $190.81 #225458845 options_level=3
2026-09-15 13:36:14,649 INFO Live account equity $224.87 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 13:36:14,698 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 13:36:14,710 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.87 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T174111Z

- UTC timestamp: `20260915T174111Z`
- GitHub run: [#10032](https://github.com/28twagg-ops/TradingBot/actions/runs/35002687659)
- Run id: `35002687659`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`18s`
- Full logs: `logs/action_runs/20260915T174111Z_live_bot.log`, `logs/action_runs/20260915T174111Z_live_options.log`, `logs/action_runs/20260915T174111Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T13:41:16.649900-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":8.6,"phases_s":{"reconcile":0.4,"cancel":0.13,"manage":6.34,"protective_stops":1.12},"signals":0,"placed":0,"equity":1001426.2,"open_positions":25,"pending_orders":0,"open_lots":156,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10032","github_run_id":"35002687659","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:41:12  INFO      Mode: exits
17:41:12  INFO        Daily log -> logs/daily/2026-09-15.md
17:41:12  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
17:41:12  INFO        place_all_stops: checking 1 positions...
17:41:12  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:41:12  INFO        [positions] 1/1 (1 valid)
17:41:13  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.87|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.14                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T13:41:13.794983-04:00 share=25% ===
2026-09-15 13:41:13,795 INFO === options_live_micro LIVE 2026-09-15T13:41:13.794983-04:00 share=25% ===
Live account equity $224.87 cash $190.81 #225458845 options_level=3
2026-09-15 13:41:13,972 INFO Live account equity $224.87 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 13:41:14,114 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 13:41:14,162 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.87 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T174624Z

- UTC timestamp: `20260915T174624Z`
- GitHub run: [#10033](https://github.com/28twagg-ops/TradingBot/actions/runs/35003198264)
- Run id: `35003198264`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`25s`
- Full logs: `logs/action_runs/20260915T174624Z_live_bot.log`, `logs/action_runs/20260915T174624Z_live_options.log`, `logs/action_runs/20260915T174624Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T13:46:32.708966-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":13.2,"phases_s":{"reconcile":0.49,"cancel":0.23,"manage":9.66,"protective_stops":2.02},"signals":0,"placed":0,"equity":1001452.7,"open_positions":25,"pending_orders":0,"open_lots":156,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10033","github_run_id":"35003198264","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:46:25  INFO      Mode: exits
17:46:26  INFO        Daily log -> logs/daily/2026-09-15.md
17:46:26  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
17:46:26  INFO        place_all_stops: checking 1 positions...
17:46:26  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:46:26  INFO        [positions] 1/1 (1 valid)
17:46:27  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.84|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.3%  $+0.11                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T13:46:29.024773-04:00 share=25% ===
2026-09-15 13:46:29,024 INFO === options_live_micro LIVE 2026-09-15T13:46:29.024773-04:00 share=25% ===
Live account equity $224.84 cash $190.81 #225458845 options_level=3
2026-09-15 13:46:29,251 INFO Live account equity $224.84 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 13:46:29,468 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 13:46:29,538 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.84 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T175119Z

- UTC timestamp: `20260915T175119Z`
- GitHub run: [#10034](https://github.com/28twagg-ops/TradingBot/actions/runs/35003713732)
- Run id: `35003713732`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`23s`
- Full logs: `logs/action_runs/20260915T175119Z_live_bot.log`, `logs/action_runs/20260915T175119Z_live_options.log`, `logs/action_runs/20260915T175119Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T13:51:26.561751-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":14.2,"phases_s":{"reconcile":0.54,"cancel":0.23,"manage":10.54,"protective_stops":2.04},"signals":0,"placed":0,"equity":1001365.2,"open_positions":25,"pending_orders":0,"open_lots":156,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10034","github_run_id":"35003713732","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:51:20  INFO      Mode: exits
17:51:21  INFO        Daily log -> logs/daily/2026-09-15.md
17:51:21  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
17:51:21  INFO        place_all_stops: checking 1 positions...
17:51:21  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:51:22  INFO        [positions] 1/1 (1 valid)
17:51:22  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.85|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.12                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T13:51:23.194972-04:00 share=25% ===
2026-09-15 13:51:23,195 INFO === options_live_micro LIVE 2026-09-15T13:51:23.194972-04:00 share=25% ===
Live account equity $224.85 cash $190.81 #225458845 options_level=3
2026-09-15 13:51:23,445 INFO Live account equity $224.85 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 13:51:23,692 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 13:51:23,770 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.85 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T175729Z

- UTC timestamp: `20260915T175729Z`
- GitHub run: [#10035](https://github.com/28twagg-ops/TradingBot/actions/runs/35004215187)
- Run id: `35004215187`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`19s`
- Full logs: `logs/action_runs/20260915T175729Z_live_bot.log`, `logs/action_runs/20260915T175729Z_live_options.log`, `logs/action_runs/20260915T175729Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T13:57:34.242891-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":9.3,"phases_s":{"reconcile":0.43,"cancel":0.13,"manage":7.07,"protective_stops":1.11},"signals":0,"placed":0,"equity":1001273.7,"open_positions":25,"pending_orders":0,"open_lots":156,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10035","github_run_id":"35004215187","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:57:29  INFO      Mode: exits
17:57:30  INFO        Daily log -> logs/daily/2026-09-15.md
17:57:30  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
17:57:30  INFO        place_all_stops: checking 1 positions...
17:57:30  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:57:30  INFO        [positions] 1/1 (1 valid)
17:57:30  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:57 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.86|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.13                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T13:57:31.481290-04:00 share=25% ===
2026-09-15 13:57:31,481 INFO === options_live_micro LIVE 2026-09-15T13:57:31.481290-04:00 share=25% ===
Live account equity $224.86 cash $190.81 #225458845 options_level=3
2026-09-15 13:57:31,655 INFO Live account equity $224.86 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 13:57:31,797 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 13:57:31,844 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.86 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T180104Z

- UTC timestamp: `20260915T180104Z`
- GitHub run: [#10036](https://github.com/28twagg-ops/TradingBot/actions/runs/35004717922)
- Run id: `35004717922`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`19s`
- Full logs: `logs/action_runs/20260915T180104Z_live_bot.log`, `logs/action_runs/20260915T180104Z_live_options.log`, `logs/action_runs/20260915T180104Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1229 | 49.2 | -7.7 | +40.2 | $+16,085 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T14:01:10.471932-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":7.8,"phases_s":{"reconcile":0.27,"cancel":0.04,"manage":6.4,"protective_stops":0.41},"signals":0,"placed":0,"equity":1001077.2,"open_positions":25,"pending_orders":0,"open_lots":156,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10036","github_run_id":"35004717922","status":"ok","data_quality":{"clean":{"n":1229,"win":49.23,"med":-7.69,"avg":40.16,"pnl":16084.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:01:05  INFO      Mode: exits
18:01:06  INFO        Daily log -> logs/daily/2026-09-15.md
18:01:06  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
18:01:06  INFO        place_all_stops: checking 1 positions...
18:01:06  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
18:01:06  INFO        [positions] 1/1 (1 valid)
18:01:06  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.86|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.13                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T14:01:07.197732-04:00 share=25% ===
2026-09-15 14:01:07,197 INFO === options_live_micro LIVE 2026-09-15T14:01:07.197732-04:00 share=25% ===
Live account equity $224.86 cash $190.81 #225458845 options_level=3
2026-09-15 14:01:07,237 INFO Live account equity $224.86 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 14:01:07,261 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 14:01:07,267 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (179 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  2226 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1229 med=-7.7% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.86 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T180618Z

- UTC timestamp: `20260915T180618Z`
- GitHub run: [#10037](https://github.com/28twagg-ops/TradingBot/actions/runs/35005246842)
- Run id: `35005246842`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`18s`
- Full logs: `logs/action_runs/20260915T180618Z_live_bot.log`, `logs/action_runs/20260915T180618Z_live_options.log`, `logs/action_runs/20260915T180618Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1231 | 49.1 | -12.5 | +40.0 | $+16,030 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T14:06:23.934936-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":9.7,"phases_s":{"reconcile":0.49,"cancel":0.14,"manage":6.99,"protective_stops":1.38},"signals":0,"placed":0,"equity":1001023.66,"open_positions":25,"pending_orders":0,"open_lots":154,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10037","github_run_id":"35005246842","status":"ok","data_quality":{"clean":{"n":1231,"win":49.15,"med":-12.5,"avg":40.01,"pnl":16029.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:06:19  INFO      Mode: exits
18:06:20  INFO        Daily log -> logs/daily/2026-09-15.md
18:06:20  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
18:06:20  INFO        place_all_stops: checking 1 positions...
18:06:20  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
18:06:20  INFO        [positions] 1/1 (1 valid)
18:06:20  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.91|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.5%  $+0.18                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T14:06:21.280723-04:00 share=25% ===
2026-09-15 14:06:21,280 INFO === options_live_micro LIVE 2026-09-15T14:06:21.280723-04:00 share=25% ===
Live account equity $224.91 cash $190.81 #225458845 options_level=3
2026-09-15 14:06:21,429 INFO Live account equity $224.91 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 14:06:21,539 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 14:06:21,570 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   154 | INFO |
| Total closed lots           |  2227 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1231 med=-12.5% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.91 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T181131Z

- UTC timestamp: `20260915T181131Z`
- GitHub run: [#10038](https://github.com/28twagg-ops/TradingBot/actions/runs/35005767438)
- Run id: `35005767438`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260915T181131Z_live_bot.log`, `logs/action_runs/20260915T181131Z_live_options.log`, `logs/action_runs/20260915T181131Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1231 | 49.1 | -12.5 | +40.0 | $+16,030 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T14:11:36.924432-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":5.8,"phases_s":{"reconcile":0.1,"cancel":0.04,"manage":4.85,"protective_stops":0.29},"signals":0,"placed":0,"equity":1000912.16,"open_positions":25,"pending_orders":0,"open_lots":154,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10038","github_run_id":"35005767438","status":"ok","data_quality":{"clean":{"n":1231,"win":49.15,"med":-12.5,"avg":40.01,"pnl":16029.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:11:32  INFO      Mode: exits
18:11:32  INFO        Daily log -> logs/daily/2026-09-15.md
18:11:32  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
18:11:32  INFO        place_all_stops: checking 1 positions...
18:11:32  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
18:11:32  INFO        [positions] 1/1 (1 valid)
18:11:32  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.89|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.5%  $+0.16                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T14:11:34.063942-04:00 share=25% ===
2026-09-15 14:11:34,064 INFO === options_live_micro LIVE 2026-09-15T14:11:34.063942-04:00 share=25% ===
Live account equity $224.90 cash $190.81 #225458845 options_level=3
2026-09-15 14:11:34,140 INFO Live account equity $224.90 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 14:11:34,212 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 14:11:34,219 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   154 | INFO |
| Total closed lots           |  2227 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1231 med=-12.5% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.9 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T181602Z

- UTC timestamp: `20260915T181602Z`
- GitHub run: [#10039](https://github.com/28twagg-ops/TradingBot/actions/runs/35006293600)
- Run id: `35006293600`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`18s`
- Full logs: `logs/action_runs/20260915T181602Z_live_bot.log`, `logs/action_runs/20260915T181602Z_live_options.log`, `logs/action_runs/20260915T181602Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1231 | 49.1 | -12.5 | +40.0 | $+16,030 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T14:16:07.952924-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.8,"phases_s":{"reconcile":0.11,"cancel":0.03,"manage":5.88,"protective_stops":0.27},"signals":0,"placed":0,"equity":1001050.16,"open_positions":25,"pending_orders":0,"open_lots":154,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10039","github_run_id":"35006293600","status":"ok","data_quality":{"clean":{"n":1231,"win":49.15,"med":-12.5,"avg":40.01,"pnl":16029.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:16:03  INFO      Mode: exits
18:16:03  INFO        Daily log -> logs/daily/2026-09-15.md
18:16:03  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
18:16:03  INFO        place_all_stops: checking 1 positions...
18:16:03  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
18:16:03  INFO        [positions] 1/1 (1 valid)
18:16:03  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.89|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.5%  $+0.16                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T14:16:05.049265-04:00 share=25% ===
2026-09-15 14:16:05,049 INFO === options_live_micro LIVE 2026-09-15T14:16:05.049265-04:00 share=25% ===
Live account equity $224.90 cash $190.81 #225458845 options_level=3
2026-09-15 14:16:05,094 INFO Live account equity $224.90 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 14:16:05,186 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 14:16:05,193 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   154 | INFO |
| Total closed lots           |  2227 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1231 med=-12.5% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.89 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T182106Z

- UTC timestamp: `20260915T182106Z`
- GitHub run: [#10040](https://github.com/28twagg-ops/TradingBot/actions/runs/35006811932)
- Run id: `35006811932`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`19s`
- Full logs: `logs/action_runs/20260915T182106Z_live_bot.log`, `logs/action_runs/20260915T182106Z_live_options.log`, `logs/action_runs/20260915T182106Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1231 | 49.1 | -12.5 | +40.0 | $+16,030 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T14:21:12.893996-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.4,"phases_s":{"reconcile":0.14,"cancel":0.03,"manage":5.44,"protective_stops":0.29},"signals":0,"placed":0,"equity":1000901.66,"open_positions":25,"pending_orders":0,"open_lots":154,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10040","github_run_id":"35006811932","status":"ok","data_quality":{"clean":{"n":1231,"win":49.15,"med":-12.5,"avg":40.01,"pnl":16029.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:21:07  INFO      Mode: exits
18:21:08  INFO        Daily log -> logs/daily/2026-09-15.md
18:21:08  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
18:21:08  INFO        place_all_stops: checking 1 positions...
18:21:08  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
18:21:08  INFO        [positions] 1/1 (1 valid)
18:21:08  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.89|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.5%  $+0.16                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T14:21:09.726425-04:00 share=25% ===
2026-09-15 14:21:09,726 INFO === options_live_micro LIVE 2026-09-15T14:21:09.726425-04:00 share=25% ===
Live account equity $224.89 cash $190.81 #225458845 options_level=3
2026-09-15 14:21:09,777 INFO Live account equity $224.89 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 14:21:09,930 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 14:21:09,938 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   154 | INFO |
| Total closed lots           |  2227 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1231 med=-12.5% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.89 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T182602Z

- UTC timestamp: `20260915T182602Z`
- GitHub run: [#10041](https://github.com/28twagg-ops/TradingBot/actions/runs/35007333667)
- Run id: `35007333667`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`19s`
- Full logs: `logs/action_runs/20260915T182602Z_live_bot.log`, `logs/action_runs/20260915T182602Z_live_options.log`, `logs/action_runs/20260915T182602Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1231 | 49.1 | -12.5 | +40.0 | $+16,030 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T14:26:07.897994-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.5,"phases_s":{"reconcile":0.12,"cancel":0.04,"manage":5.57,"protective_stops":0.3},"signals":0,"placed":0,"equity":1000744.66,"open_positions":25,"pending_orders":0,"open_lots":154,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10041","github_run_id":"35007333667","status":"ok","data_quality":{"clean":{"n":1231,"win":49.15,"med":-12.5,"avg":40.01,"pnl":16029.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:26:03  INFO      Mode: exits
18:26:03  INFO        Daily log -> logs/daily/2026-09-15.md
18:26:03  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
18:26:03  INFO        place_all_stops: checking 1 positions...
18:26:03  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
18:26:03  INFO        [positions] 1/1 (1 valid)
18:26:03  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.87|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.14                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T14:26:04.616913-04:00 share=25% ===
2026-09-15 14:26:04,616 INFO === options_live_micro LIVE 2026-09-15T14:26:04.616913-04:00 share=25% ===
Live account equity $224.87 cash $190.81 #225458845 options_level=3
2026-09-15 14:26:04,661 INFO Live account equity $224.87 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 14:26:04,754 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 14:26:04,771 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   154 | INFO |
| Total closed lots           |  2227 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1231 med=-12.5% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.87 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T183132Z

- UTC timestamp: `20260915T183132Z`
- GitHub run: [#10042](https://github.com/28twagg-ops/TradingBot/actions/runs/35007860278)
- Run id: `35007860278`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`25s`
- Full logs: `logs/action_runs/20260915T183132Z_live_bot.log`, `logs/action_runs/20260915T183132Z_live_options.log`, `logs/action_runs/20260915T183132Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1231 | 49.1 | -12.5 | +40.0 | $+16,030 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T14:31:40.063624-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":13.3,"phases_s":{"reconcile":0.48,"cancel":0.22,"manage":9.92,"protective_stops":1.9},"signals":0,"placed":0,"equity":1000941.66,"open_positions":25,"pending_orders":0,"open_lots":154,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10042","github_run_id":"35007860278","status":"ok","data_quality":{"clean":{"n":1231,"win":49.15,"med":-12.5,"avg":40.01,"pnl":16029.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:31:33  INFO      Mode: exits
18:31:34  INFO        Daily log -> logs/daily/2026-09-15.md
18:31:34  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
18:31:34  INFO        place_all_stops: checking 1 positions...
18:31:34  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
18:31:35  INFO        [positions] 1/1 (1 valid)
18:31:35  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.86|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.13                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T14:31:36.455253-04:00 share=25% ===
2026-09-15 14:31:36,455 INFO === options_live_micro LIVE 2026-09-15T14:31:36.455253-04:00 share=25% ===
Live account equity $224.86 cash $190.81 #225458845 options_level=3
2026-09-15 14:31:36,678 INFO Live account equity $224.86 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 14:31:36,884 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 14:31:36,952 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   154 | INFO |
| Total closed lots           |  2227 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1231 med=-12.5% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.86 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T183607Z

- UTC timestamp: `20260915T183607Z`
- GitHub run: [#10043](https://github.com/28twagg-ops/TradingBot/actions/runs/35008377568)
- Run id: `35008377568`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`19s`
- Full logs: `logs/action_runs/20260915T183607Z_live_bot.log`, `logs/action_runs/20260915T183607Z_live_options.log`, `logs/action_runs/20260915T183607Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1231 | 49.1 | -12.5 | +40.0 | $+16,030 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T14:36:13.299418-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":7.2,"phases_s":{"reconcile":0.1,"cancel":0.03,"manage":6.26,"protective_stops":0.23},"signals":0,"placed":0,"equity":1000702.16,"open_positions":25,"pending_orders":0,"open_lots":154,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10043","github_run_id":"35008377568","status":"ok","data_quality":{"clean":{"n":1231,"win":49.15,"med":-12.5,"avg":40.01,"pnl":16029.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:36:08  INFO      Mode: exits
18:36:09  INFO        Daily log -> logs/daily/2026-09-15.md
18:36:09  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
18:36:09  INFO        place_all_stops: checking 1 positions...
18:36:09  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
18:36:09  INFO        [positions] 1/1 (1 valid)
18:36:09  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.86|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.13                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T14:36:10.117963-04:00 share=25% ===
2026-09-15 14:36:10,118 INFO === options_live_micro LIVE 2026-09-15T14:36:10.117963-04:00 share=25% ===
Live account equity $224.86 cash $190.81 #225458845 options_level=3
2026-09-15 14:36:10,167 INFO Live account equity $224.86 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 14:36:10,218 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 14:36:10,225 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   154 | INFO |
| Total closed lots           |  2227 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1231 med=-12.5% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.86 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T184134Z

- UTC timestamp: `20260915T184134Z`
- GitHub run: [#10044](https://github.com/28twagg-ops/TradingBot/actions/runs/35008887813)
- Run id: `35008887813`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260915T184134Z_live_bot.log`, `logs/action_runs/20260915T184134Z_live_options.log`, `logs/action_runs/20260915T184134Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1231 | 49.1 | -12.5 | +40.0 | $+16,030 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T14:41:41.665134-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":11.3,"phases_s":{"reconcile":0.4,"cancel":0.17,"manage":8.58,"protective_stops":1.39},"signals":0,"placed":0,"equity":1000248.59,"open_positions":23,"pending_orders":0,"open_lots":151,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10044","github_run_id":"35008887813","status":"ok","data_quality":{"clean":{"n":1231,"win":49.15,"med":-12.5,"avg":40.01,"pnl":16029.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:41:35  INFO      Mode: exits
18:41:36  INFO        Daily log -> logs/daily/2026-09-15.md
18:41:36  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
18:41:36  INFO        place_all_stops: checking 1 positions...
18:41:36  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
18:41:36  INFO        [positions] 1/1 (1 valid)
18:41:37  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.87|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.14                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T14:41:38.091801-04:00 share=25% ===
2026-09-15 14:41:38,091 INFO === options_live_micro LIVE 2026-09-15T14:41:38.091801-04:00 share=25% ===
Live account equity $224.87 cash $190.81 #225458845 options_level=3
2026-09-15 14:41:38,288 INFO Live account equity $224.87 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 14:41:38,468 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 14:41:38,555 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (183 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   151 | INFO |
| Total closed lots           |  2227 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1231 med=-12.5% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.87 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T184602Z

- UTC timestamp: `20260915T184602Z`
- GitHub run: [#10045](https://github.com/28twagg-ops/TradingBot/actions/runs/35009403066)
- Run id: `35009403066`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`19s`
- Full logs: `logs/action_runs/20260915T184602Z_live_bot.log`, `logs/action_runs/20260915T184602Z_live_options.log`, `logs/action_runs/20260915T184602Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1232 | 49.1 | -14.2 | +39.9 | $+16,006 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 640 | 63.0 | +51.4 | +63.0 | $+10,923 |
| KEEP-only recent | 443 | 60.9 | +53.3 | +72.4 | $+6,278 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T14:46:08.581082-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.6,"phases_s":{"reconcile":0.15,"cancel":0.03,"manage":5.73,"protective_stops":0.24},"signals":0,"placed":0,"equity":1000001.57,"open_positions":23,"pending_orders":0,"open_lots":150,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10045","github_run_id":"35009403066","status":"ok","data_quality":{"clean":{"n":1232,"win":49.11,"med":-14.18,"avg":39.94,"pnl":16005.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":640,"win":62.97,"med":51.39,"avg":63.0,"pnl":10923.45},"keep_only_recent":{"n":443,"win":60.95,"med":53.33,"avg":72.44,"pnl":6278.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:46:03  INFO      Mode: exits
18:46:04  INFO        Daily log -> logs/daily/2026-09-15.md
18:46:04  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
18:46:04  INFO        place_all_stops: checking 1 positions...
18:46:04  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
18:46:04  INFO        [positions] 1/1 (1 valid)
18:46:04  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.87|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.14                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T14:46:05.066949-04:00 share=25% ===
2026-09-15 14:46:05,067 INFO === options_live_micro LIVE 2026-09-15T14:46:05.066949-04:00 share=25% ===
Live account equity $224.87 cash $190.81 #225458845 options_level=3
2026-09-15 14:46:05,287 INFO Live account equity $224.87 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 14:46:05,317 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 14:46:05,323 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (181 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   150 | INFO |
| Total closed lots           |  2228 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1232 med=-14.2% | TAINTED n=1844 med=-38.8% | KEEP-only n=640 med=+51.4% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.87 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T185102Z

- UTC timestamp: `20260915T185102Z`
- GitHub run: [#10046](https://github.com/28twagg-ops/TradingBot/actions/runs/35009917521)
- Run id: `35009917521`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`20s`
- Full logs: `logs/action_runs/20260915T185102Z_live_bot.log`, `logs/action_runs/20260915T185102Z_live_options.log`, `logs/action_runs/20260915T185102Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1234 | 49.0 | -15.9 | +39.8 | $+15,949 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 642 | 62.8 | +51.2 | +62.6 | $+10,866 |
| KEEP-only recent | 445 | 60.7 | +53.3 | +71.9 | $+6,221 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T14:51:09.649819-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":11.3,"phases_s":{"reconcile":0.63,"cancel":0.19,"manage":8.03,"protective_stops":1.84},"signals":0,"placed":0,"equity":999853.99,"open_positions":22,"pending_orders":0,"open_lots":147,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10046","github_run_id":"35009917521","status":"ok","data_quality":{"clean":{"n":1234,"win":49.03,"med":-15.93,"avg":39.79,"pnl":15948.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":642,"win":62.77,"med":51.18,"avg":62.64,"pnl":10866.45},"keep_only_recent":{"n":445,"win":60.67,"med":53.33,"avg":71.89,"pnl":6221.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:51:03  INFO      Mode: exits
18:51:04  INFO        Daily log -> logs/daily/2026-09-15.md
18:51:04  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
18:51:04  INFO        place_all_stops: checking 1 positions...
18:51:04  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
18:51:04  INFO        [positions] 1/1 (1 valid)
18:51:05  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.84|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.3%  $+0.11                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T14:51:06.248055-04:00 share=25% ===
2026-09-15 14:51:06,248 INFO === options_live_micro LIVE 2026-09-15T14:51:06.248055-04:00 share=25% ===
Live account equity $224.84 cash $190.81 #225458845 options_level=3
2026-09-15 14:51:06,465 INFO Live account equity $224.84 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 14:51:06,734 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 14:51:06,791 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (181 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   147 | INFO |
| Total closed lots           |  2230 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1234 med=-15.9% | TAINTED n=1844 med=-38.8% | KEEP-only n=642 med=+51.2% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.84 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T185616Z

- UTC timestamp: `20260915T185616Z`
- GitHub run: [#10047](https://github.com/28twagg-ops/TradingBot/actions/runs/35010439798)
- Run id: `35010439798`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260915T185616Z_live_bot.log`, `logs/action_runs/20260915T185616Z_live_options.log`, `logs/action_runs/20260915T185616Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1234 | 49.0 | -15.9 | +39.8 | $+15,949 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 642 | 62.8 | +51.2 | +62.6 | $+10,866 |
| KEEP-only recent | 445 | 60.7 | +53.3 | +71.9 | $+6,221 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T14:56:22.214657-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":5.0,"phases_s":{"reconcile":0.14,"cancel":0.03,"manage":3.81,"protective_stops":0.23},"signals":0,"placed":0,"equity":1000127.46,"open_positions":22,"pending_orders":0,"open_lots":146,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10047","github_run_id":"35010439798","status":"ok","data_quality":{"clean":{"n":1234,"win":49.03,"med":-15.93,"avg":39.79,"pnl":15948.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":642,"win":62.77,"med":51.18,"avg":62.64,"pnl":10866.45},"keep_only_recent":{"n":445,"win":60.67,"med":53.33,"avg":71.89,"pnl":6221.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:56:17  INFO      Mode: exits
18:56:17  INFO        Daily log -> logs/daily/2026-09-15.md
18:56:17  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
18:56:17  INFO        place_all_stops: checking 1 positions...
18:56:17  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
18:56:17  INFO        [positions] 1/1 (1 valid)
18:56:17  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.86|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.13                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T14:56:19.021723-04:00 share=25% ===
2026-09-15 14:56:19,021 INFO === options_live_micro LIVE 2026-09-15T14:56:19.021723-04:00 share=25% ===
Live account equity $224.86 cash $190.81 #225458845 options_level=3
2026-09-15 14:56:19,081 INFO Live account equity $224.86 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 14:56:19,386 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 14:56:19,402 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (179 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   146 | INFO |
| Total closed lots           |  2230 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1234 med=-15.9% | TAINTED n=1844 med=-38.8% | KEEP-only n=642 med=+51.2% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.86 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T190137Z

- UTC timestamp: `20260915T190137Z`
- GitHub run: [#10048](https://github.com/28twagg-ops/TradingBot/actions/runs/35010948499)
- Run id: `35010948499`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`23s`
- Full logs: `logs/action_runs/20260915T190137Z_live_bot.log`, `logs/action_runs/20260915T190137Z_live_options.log`, `logs/action_runs/20260915T190137Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1234 | 49.0 | -15.9 | +39.8 | $+15,949 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 642 | 62.8 | +51.2 | +62.6 | $+10,866 |
| KEEP-only recent | 445 | 60.7 | +53.3 | +71.9 | $+6,221 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T15:01:45.036321-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":11.3,"phases_s":{"reconcile":0.54,"cancel":0.22,"manage":8.21,"protective_stops":1.63},"signals":0,"placed":0,"equity":1000256.47,"open_positions":22,"pending_orders":0,"open_lots":146,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10048","github_run_id":"35010948499","status":"ok","data_quality":{"clean":{"n":1234,"win":49.03,"med":-15.93,"avg":39.79,"pnl":15948.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":642,"win":62.77,"med":51.18,"avg":62.64,"pnl":10866.45},"keep_only_recent":{"n":445,"win":60.67,"med":53.33,"avg":71.89,"pnl":6221.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
19:01:38  INFO      Mode: exits
19:01:39  INFO        Daily log -> logs/daily/2026-09-15.md
19:01:39  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
19:01:39  INFO        place_all_stops: checking 1 positions...
19:01:39  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
19:01:40  INFO        [positions] 1/1 (1 valid)
19:01:40  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.86|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.13                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T15:01:41.470227-04:00 share=25% ===
2026-09-15 15:01:41,470 INFO === options_live_micro LIVE 2026-09-15T15:01:41.470227-04:00 share=25% ===
Live account equity $224.86 cash $190.81 #225458845 options_level=3
2026-09-15 15:01:41,694 INFO Live account equity $224.86 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 15:01:41,899 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 15:01:41,967 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (177 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   146 | INFO |
| Total closed lots           |  2230 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1234 med=-15.9% | TAINTED n=1844 med=-38.8% | KEEP-only n=642 med=+51.2% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.86 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T190604Z

- UTC timestamp: `20260915T190604Z`
- GitHub run: [#10049](https://github.com/28twagg-ops/TradingBot/actions/runs/35011469026)
- Run id: `35011469026`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`18s`
- Full logs: `logs/action_runs/20260915T190604Z_live_bot.log`, `logs/action_runs/20260915T190604Z_live_options.log`, `logs/action_runs/20260915T190604Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1234 | 49.0 | -15.9 | +39.8 | $+15,949 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 642 | 62.8 | +51.2 | +62.6 | $+10,866 |
| KEEP-only recent | 445 | 60.7 | +53.3 | +71.9 | $+6,221 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T15:06:10.329382-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":7.9,"phases_s":{"reconcile":0.3,"cancel":0.1,"manage":6.2,"protective_stops":0.79},"signals":0,"placed":0,"equity":1000392.97,"open_positions":22,"pending_orders":0,"open_lots":146,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10049","github_run_id":"35011469026","status":"ok","data_quality":{"clean":{"n":1234,"win":49.03,"med":-15.93,"avg":39.79,"pnl":15948.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":642,"win":62.77,"med":51.18,"avg":62.64,"pnl":10866.45},"keep_only_recent":{"n":445,"win":60.67,"med":53.33,"avg":71.89,"pnl":6221.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
19:06:05  INFO      Mode: exits
19:06:05  INFO        Daily log -> logs/daily/2026-09-15.md
19:06:05  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
19:06:05  INFO        place_all_stops: checking 1 positions...
19:06:05  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
19:06:05  INFO        [positions] 1/1 (1 valid)
19:06:06  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.86|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.13                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T15:06:07.205161-04:00 share=25% ===
2026-09-15 15:06:07,205 INFO === options_live_micro LIVE 2026-09-15T15:06:07.205161-04:00 share=25% ===
Live account equity $224.86 cash $190.81 #225458845 options_level=3
2026-09-15 15:06:07,349 INFO Live account equity $224.86 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 15:06:07,516 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 15:06:07,554 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (177 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   146 | INFO |
| Total closed lots           |  2230 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1234 med=-15.9% | TAINTED n=1844 med=-38.8% | KEEP-only n=642 med=+51.2% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.86 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T191116Z

- UTC timestamp: `20260915T191116Z`
- GitHub run: [#10050](https://github.com/28twagg-ops/TradingBot/actions/runs/35011976074)
- Run id: `35011976074`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`15s`
- Full logs: `logs/action_runs/20260915T191116Z_live_bot.log`, `logs/action_runs/20260915T191116Z_live_options.log`, `logs/action_runs/20260915T191116Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1234 | 49.0 | -15.9 | +39.8 | $+15,949 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 642 | 62.8 | +51.2 | +62.6 | $+10,866 |
| KEEP-only recent | 445 | 60.7 | +53.3 | +71.9 | $+6,221 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T15:11:23.043125-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":7.4,"phases_s":{"reconcile":0.36,"cancel":0.18,"manage":5.53,"protective_stops":0.82},"signals":0,"placed":0,"equity":1000310.47,"open_positions":22,"pending_orders":0,"open_lots":146,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10050","github_run_id":"35011976074","status":"ok","data_quality":{"clean":{"n":1234,"win":49.03,"med":-15.93,"avg":39.79,"pnl":15948.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":642,"win":62.77,"med":51.18,"avg":62.64,"pnl":10866.45},"keep_only_recent":{"n":445,"win":60.67,"med":53.33,"avg":71.89,"pnl":6221.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
19:11:17  INFO      Mode: exits
19:11:18  INFO        Daily log -> logs/daily/2026-09-15.md
19:11:18  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
19:11:18  INFO        place_all_stops: checking 1 positions...
19:11:18  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
19:11:18  INFO        [positions] 1/1 (1 valid)
19:11:18  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.84|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.3%  $+0.11                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T15:11:19.693400-04:00 share=25% ===
2026-09-15 15:11:19,693 INFO === options_live_micro LIVE 2026-09-15T15:11:19.693400-04:00 share=25% ===
Live account equity $224.84 cash $190.81 #225458845 options_level=3
2026-09-15 15:11:19,847 INFO Live account equity $224.84 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 15:11:20,063 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 15:11:20,115 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (177 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   146 | INFO |
| Total closed lots           |  2230 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1234 med=-15.9% | TAINTED n=1844 med=-38.8% | KEEP-only n=642 med=+51.2% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.84 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T191605Z

- UTC timestamp: `20260915T191605Z`
- GitHub run: [#10051](https://github.com/28twagg-ops/TradingBot/actions/runs/35012487432)
- Run id: `35012487432`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260915T191605Z_live_bot.log`, `logs/action_runs/20260915T191605Z_live_options.log`, `logs/action_runs/20260915T191605Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1234 | 49.0 | -15.9 | +39.8 | $+15,949 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 642 | 62.8 | +51.2 | +62.6 | $+10,866 |
| KEEP-only recent | 445 | 60.7 | +53.3 | +71.9 | $+6,221 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T15:16:12.195266-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":5.2,"phases_s":{"reconcile":0.19,"cancel":0.04,"manage":4.16,"protective_stops":0.21},"signals":0,"placed":0,"equity":1000496.47,"open_positions":22,"pending_orders":0,"open_lots":146,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10051","github_run_id":"35012487432","status":"ok","data_quality":{"clean":{"n":1234,"win":49.03,"med":-15.93,"avg":39.79,"pnl":15948.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":642,"win":62.77,"med":51.18,"avg":62.64,"pnl":10866.45},"keep_only_recent":{"n":445,"win":60.67,"med":53.33,"avg":71.89,"pnl":6221.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
19:16:07  INFO      Mode: exits
19:16:07  INFO        Daily log -> logs/daily/2026-09-15.md
19:16:07  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
19:16:07  INFO        place_all_stops: checking 1 positions...
19:16:07  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
19:16:07  INFO        [positions] 1/1 (1 valid)
19:16:07  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.84|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.3%  $+0.11                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T15:16:09.148941-04:00 share=25% ===
2026-09-15 15:16:09,149 INFO === options_live_micro LIVE 2026-09-15T15:16:09.148941-04:00 share=25% ===
Live account equity $224.84 cash $190.81 #225458845 options_level=3
2026-09-15 15:16:09,193 INFO Live account equity $224.84 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 15:16:09,276 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 15:16:09,283 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   146 | INFO |
| Total closed lots           |  2230 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1234 med=-15.9% | TAINTED n=1844 med=-38.8% | KEEP-only n=642 med=+51.2% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.84 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T192102Z

- UTC timestamp: `20260915T192102Z`
- GitHub run: [#10052](https://github.com/28twagg-ops/TradingBot/actions/runs/35012988687)
- Run id: `35012988687`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`18s`
- Full logs: `logs/action_runs/20260915T192102Z_live_bot.log`, `logs/action_runs/20260915T192102Z_live_options.log`, `logs/action_runs/20260915T192102Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1234 | 49.0 | -15.9 | +39.8 | $+15,949 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 642 | 62.8 | +51.2 | +62.6 | $+10,866 |
| KEEP-only recent | 445 | 60.7 | +53.3 | +71.9 | $+6,221 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T15:21:08.976985-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.3,"phases_s":{"reconcile":0.13,"cancel":0.07,"manage":5.07,"protective_stops":0.36},"signals":0,"placed":0,"equity":1000425.47,"open_positions":22,"pending_orders":0,"open_lots":146,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10052","github_run_id":"35012988687","status":"ok","data_quality":{"clean":{"n":1234,"win":49.03,"med":-15.93,"avg":39.79,"pnl":15948.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":642,"win":62.77,"med":51.18,"avg":62.64,"pnl":10866.45},"keep_only_recent":{"n":445,"win":60.67,"med":53.33,"avg":71.89,"pnl":6221.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
19:21:03  INFO      Mode: exits
19:21:04  INFO        Daily log -> logs/daily/2026-09-15.md
19:21:04  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
19:21:04  INFO        place_all_stops: checking 1 positions...
19:21:04  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
19:21:04  INFO        [positions] 1/1 (1 valid)
19:21:04  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.81|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.2%  $+0.08                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T15:21:05.564486-04:00 share=25% ===
2026-09-15 15:21:05,564 INFO === options_live_micro LIVE 2026-09-15T15:21:05.564486-04:00 share=25% ===
Live account equity $224.81 cash $190.81 #225458845 options_level=3
2026-09-15 15:21:05,627 INFO Live account equity $224.81 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 15:21:05,896 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 15:21:05,911 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   146 | INFO |
| Total closed lots           |  2230 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1234 med=-15.9% | TAINTED n=1844 med=-38.8% | KEEP-only n=642 med=+51.2% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.81 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T192611Z

- UTC timestamp: `20260915T192611Z`
- GitHub run: [#10053](https://github.com/28twagg-ops/TradingBot/actions/runs/35013490428)
- Run id: `35013490428`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`16s`
- Full logs: `logs/action_runs/20260915T192611Z_live_bot.log`, `logs/action_runs/20260915T192611Z_live_options.log`, `logs/action_runs/20260915T192611Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1234 | 49.0 | -15.9 | +39.8 | $+15,949 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 642 | 62.8 | +51.2 | +62.6 | $+10,866 |
| KEEP-only recent | 445 | 60.7 | +53.3 | +71.9 | $+6,221 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T15:26:18.157336-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.8,"phases_s":{"reconcile":0.13,"cancel":0.07,"manage":3.78,"protective_stops":0.31},"signals":0,"placed":0,"equity":1000458.97,"open_positions":22,"pending_orders":0,"open_lots":146,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10053","github_run_id":"35013490428","status":"ok","data_quality":{"clean":{"n":1234,"win":49.03,"med":-15.93,"avg":39.79,"pnl":15948.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":642,"win":62.77,"med":51.18,"avg":62.64,"pnl":10866.45},"keep_only_recent":{"n":445,"win":60.67,"med":53.33,"avg":71.89,"pnl":6221.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
19:26:14  INFO      Mode: exits
19:26:14  INFO        Daily log -> logs/daily/2026-09-15.md
19:26:14  INFO        Daily log reconciled -> logs/daily/2026-09-15.md (4 ledger rows)
19:26:14  INFO        place_all_stops: checking 1 positions...
19:26:14  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
19:26:14  INFO        [positions] 1/1 (1 valid)
19:26:14  INFO        Daily log -> logs/daily/2026-09-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.78|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.2%  $+0.05                                           HOLD|
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
=== options_live_micro LIVE 2026-09-15T15:26:15.423748-04:00 share=25% ===
2026-09-15 15:26:15,423 INFO === options_live_micro LIVE 2026-09-15T15:26:15.423748-04:00 share=25% ===
Live account equity $224.78 cash $190.81 #225458845 options_level=3
2026-09-15 15:26:15,500 INFO Live account equity $224.78 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 15:26:15,558 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 15:26:15,568 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   146 | INFO |
| Total closed lots           |  2230 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1234 med=-15.9% | TAINTED n=1844 med=-38.8% | KEEP-only n=642 med=+51.2% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.78 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260915T193109Z

- UTC timestamp: `20260915T193109Z`
- GitHub run: [#10054](https://github.com/28twagg-ops/TradingBot/actions/runs/35013989455)
- Run id: `35013989455`
- Live bot: exit=`0`, duration=`218s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260915T193109Z_live_bot.log`, `logs/action_runs/20260915T193109Z_live_options.log`, `logs/action_runs/20260915T193109Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1234 | 49.0 | -15.9 | +39.8 | $+15,949 |
| TAINTED | 1844 | 33.5 | -38.8 | +12.2 | $-9,169 |
| KEEP-only | 642 | 62.8 | +51.2 | +62.6 | $+10,866 |
| KEEP-only recent | 445 | 60.7 | +53.3 | +71.9 | $+6,221 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S359, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-15T15:34:51.309914-04:00","date":"2026-09-15","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":12.2,"phases_s":{"reconcile":0.46,"cancel":0.21,"manage":8.82,"protective_stops":1.93},"signals":0,"placed":0,"equity":1000241.47,"open_positions":22,"pending_orders":0,"open_lots":146,"submitted_today":189,"filled_today":159,"unattributed_contracts":0,"top_signals":[],"github_run":"10054","github_run_id":"35013989455","status":"ok","data_quality":{"clean":{"n":1234,"win":49.03,"med":-15.93,"avg":39.79,"pnl":15948.55},"tainted":{"n":1844,"win":33.46,"med":-38.81,"avg":12.21,"pnl":-9168.84},"keep_only":{"n":642,"win":62.77,"med":51.18,"avg":62.64,"pnl":10866.45},"keep_only_recent":{"n":445,"win":60.67,"med":53.33,"avg":71.89,"pnl":6221.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S359","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
19:31:10  INFO      Mode: evening_prep
19:31:11  INFO        [prep_positions] 1/1 (1 valid)
19:31:11  INFO        Universe cache hit: 903 tickers (tickers_2026-09-15.json)
19:31:13  INFO        [prep_universe] 40/902 (40 valid)
19:31:14  INFO        [prep_universe] 80/902 (80 valid)
19:31:15  INFO        [prep_universe] 120/902 (120 valid)
19:31:16  INFO        [prep_universe] 160/902 (160 valid)
19:31:18  INFO        [prep_universe] 200/902 (199 valid)
19:31:25  INFO        [prep_universe] 240/902 (238 valid)
19:31:38  INFO        [prep_universe] 280/902 (278 valid)
19:31:49  INFO        [prep_universe] 320/902 (318 valid)
19:32:02  INFO        [prep_universe] 360/902 (358 valid)
19:32:12  INFO        [prep_universe] 400/902 (398 valid)
19:32:26  INFO        [prep_universe] 440/902 (438 valid)
19:32:36  INFO        [prep_universe] 480/902 (478 valid)
19:32:49  INFO        [prep_universe] 520/902 (518 valid)
19:33:02  INFO        [prep_universe] 560/902 (558 valid)
19:33:13  INFO        [prep_universe] 600/902 (598 valid)
19:33:26  INFO        [prep_universe] 640/902 (638 valid)
19:33:36  INFO        [prep_universe] 680/902 (678 valid)
19:33:50  INFO        [prep_universe] 720/902 (718 valid)
19:34:00  INFO        [prep_universe] 760/902 (758 valid)
19:34:13  INFO        [prep_universe] 800/902 (798 valid)
19:34:24  INFO        [prep_universe] 840/902 (838 valid)
19:34:37  INFO        [prep_universe] 880/902 (878 valid)
19:34:44  INFO        [prep_universe] 902/902 (900 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      EVENING_PREP|
|  Time                                                         19:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.74|
+========================================================================+

+========================================================================+
|                              EVENING PREP                              |
+========================================================================+
|  Goal                   Precompute exits/signals for next execution run|
|  Plan file                                 logs/plans/evening_plan.json|
|  Regime                                                            BULL|
+========================================================================+

+========================================================================+
|                       OPEN POSITION P&L SNAPSHOT                       |
+========================================================================+
|  Open positions                                                       1|
|  Invested                                                        $33.93|
|  Open P&L                                                        $+0.01|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ALLE     Pullback50      $33.93     $153.74  $153.80  +0.0%   $+0.01  |
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
|  Signal candidates                                                   24|
|  Universe scanned                                                   902|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-15T15:34:47.714581-04:00 share=25% ===
2026-09-15 15:34:47,714 INFO === options_live_micro LIVE 2026-09-15T15:34:47.714581-04:00 share=25% ===
Live account equity $224.79 cash $190.81 #225458845 options_level=3
2026-09-15 15:34:47,938 INFO Live account equity $224.79 cash $190.81 #225458845 options_level=3
Live micro: manage/exits only
2026-09-15 15:34:48,143 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-15 15:34:48,236 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (177 earlier lines - see full log file)

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
## Ledger health — 2026-09-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1249 | WARN | <<<
| Missing exit records (post) |  1246 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   146 | INFO |
| Total closed lots           |  2230 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1234 med=-15.9% | TAINTED n=1844 med=-38.8% | KEEP-only n=642 med=+51.2% | KILL=20 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.78 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
