# Daily Comprehensive Action Review - 2026-09-14

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260914T130114Z

- UTC timestamp: `20260914T130114Z`
- GitHub run: [#9844](https://github.com/28twagg-ops/TradingBot/actions/runs/34846557144)
- Run id: `34846557144`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260914T130114Z_live_bot.log`, `logs/action_runs/20260914T130114Z_live_options.log`, `logs/action_runs/20260914T130114Z_options_bot.log`


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
{"ts_et":"2026-09-14T09:01:20.773745-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.6,"phases_s":{"reconcile":4.65},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9844","github_run_id":"34846557144","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:01:15  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.44|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.44|
|  Cash                                                           $158.78|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.66|
|  Open P&L                                                        $-0.61|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $33.85     $256.11  $253.61  -1.0%   $-0.33  |
|  TKR      MomReversal     $33.82     $119.14  $118.18  -0.8%   $-0.27  |
|                                                                        |
|  Total invested                                                  $67.66|
|  Total open P&L                                                  $-0.61|
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
|  2026-09-11  SELL  RL  MomReversal  $33.81  P&L $-0.25                 |
|  2026-09-11  SELL  ADI  Pullback50  $34.06  P&L $-0.10                 |
|  2026-09-11  SELL  ABBV  Pullback50  $34.61  P&L $+0.61                |
|  2026-09-10  SELL  AES  Pullback50  $34.05  P&L $-0.00                 |
|  2026-09-10  SELL  ABBV  Pullback50  $33.90  P&L $-0.20                |
|  2026-09-10  SELL  AES  Pullback50  $34.09  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-14T09:01:17.291782-04:00 share=25% ===
2026-09-14 09:01:17,291 INFO === options_live_micro LIVE 2026-09-14T09:01:17.291782-04:00 share=25% ===
Live account equity $226.44 cash $158.78 #225458845 options_level=3
2026-09-14 09:01:17,488 INFO Live account equity $226.44 cash $158.78 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-14 09:01:17,552 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-14 09:01:17,615 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (161 earlier lines - see full log file)
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
## Ledger health — 2026-09-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1235 | WARN | <<<
| Missing exit records (post) |  1231 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    41 | INFO |
| Total closed lots           |  2193 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1204 med=-10.1% | TAINTED n=1829 med=-38.8% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.44 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T130608Z

- UTC timestamp: `20260914T130608Z`
- GitHub run: [#9845](https://github.com/28twagg-ops/TradingBot/actions/runs/34847041058)
- Run id: `34847041058`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260914T130608Z_live_bot.log`, `logs/action_runs/20260914T130608Z_live_options.log`, `logs/action_runs/20260914T130608Z_options_bot.log`


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
{"ts_et":"2026-09-14T09:06:14.655371-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.4,"phases_s":{"reconcile":4.48},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9845","github_run_id":"34847041058","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
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
|  Equity                                                         $226.40|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.40|
|  Cash                                                           $158.78|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.62|
|  Open P&L                                                        $-0.65|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $33.80     $256.11  $253.25  -1.1%   $-0.38  |
|  TKR      MomReversal     $33.82     $119.14  $118.18  -0.8%   $-0.27  |
|                                                                        |
|  Total invested                                                  $67.62|
|  Total open P&L                                                  $-0.65|
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
|  2026-09-11  SELL  RL  MomReversal  $33.81  P&L $-0.25                 |
|  2026-09-11  SELL  ADI  Pullback50  $34.06  P&L $-0.10                 |
|  2026-09-11  SELL  ABBV  Pullback50  $34.61  P&L $+0.61                |
|  2026-09-10  SELL  AES  Pullback50  $34.05  P&L $-0.00                 |
|  2026-09-10  SELL  ABBV  Pullback50  $33.90  P&L $-0.20                |
|  2026-09-10  SELL  AES  Pullback50  $34.09  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-14T09:06:11.128847-04:00 share=25% ===
2026-09-14 09:06:11,128 INFO === options_live_micro LIVE 2026-09-14T09:06:11.128847-04:00 share=25% ===
Live account equity $226.40 cash $158.78 #225458845 options_level=3
2026-09-14 09:06:11,253 INFO Live account equity $226.40 cash $158.78 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-14 09:06:11,360 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-14 09:06:11,392 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (155 earlier lines - see full log file)
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
## Ledger health — 2026-09-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1235 | WARN | <<<
| Missing exit records (post) |  1231 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    41 | INFO |
| Total closed lots           |  2193 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1204 med=-10.1% | TAINTED n=1829 med=-38.8% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.4 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T131105Z

- UTC timestamp: `20260914T131105Z`
- GitHub run: [#9846](https://github.com/28twagg-ops/TradingBot/actions/runs/34847544795)
- Run id: `34847544795`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`23s`
- Full logs: `logs/action_runs/20260914T131105Z_live_bot.log`, `logs/action_runs/20260914T131105Z_live_options.log`, `logs/action_runs/20260914T131105Z_options_bot.log`


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
{"ts_et":"2026-09-14T09:11:10.439498-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":10.9,"phases_s":{"reconcile":4.18},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9846","github_run_id":"34847544795","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:11:06  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.38|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.38|
|  Cash                                                           $158.78|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.60|
|  Open P&L                                                        $-0.67|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $33.79     $256.11  $253.15  -1.2%   $-0.39  |
|  TKR      MomReversal     $33.82     $119.14  $118.18  -0.8%   $-0.27  |
|                                                                        |
|  Total invested                                                  $67.60|
|  Total open P&L                                                  $-0.67|
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
|  2026-09-11  SELL  RL  MomReversal  $33.81  P&L $-0.25                 |
|  2026-09-11  SELL  ADI  Pullback50  $34.06  P&L $-0.10                 |
|  2026-09-11  SELL  ABBV  Pullback50  $34.61  P&L $+0.61                |
|  2026-09-10  SELL  AES  Pullback50  $34.05  P&L $-0.00                 |
|  2026-09-10  SELL  ABBV  Pullback50  $33.90  P&L $-0.20                |
|  2026-09-10  SELL  AES  Pullback50  $34.09  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-14T09:11:07.302267-04:00 share=25% ===
2026-09-14 09:11:07,302 INFO === options_live_micro LIVE 2026-09-14T09:11:07.302267-04:00 share=25% ===
Live account equity $226.38 cash $158.78 #225458845 options_level=3
2026-09-14 09:11:07,353 INFO Live account equity $226.38 cash $158.78 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-14 09:11:07,361 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-14 09:11:07,368 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (155 earlier lines - see full log file)
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
## Ledger health — 2026-09-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1235 | WARN | <<<
| Missing exit records (post) |  1231 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    41 | INFO |
| Total closed lots           |  2193 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1204 med=-10.1% | TAINTED n=1829 med=-38.8% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.38 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T131605Z

- UTC timestamp: `20260914T131605Z`
- GitHub run: [#9847](https://github.com/28twagg-ops/TradingBot/actions/runs/34848076249)
- Run id: `34848076249`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260914T131605Z_live_bot.log`, `logs/action_runs/20260914T131605Z_live_options.log`, `logs/action_runs/20260914T131605Z_options_bot.log`


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
{"ts_et":"2026-09-14T09:16:13.546727-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.9,"phases_s":{"reconcile":4.81},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9847","github_run_id":"34848076249","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
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
|  Equity                                                         $226.36|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.36|
|  Cash                                                           $158.78|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.58|
|  Open P&L                                                        $-0.69|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $33.77     $256.11  $253.00  -1.2%   $-0.41  |
|  TKR      MomReversal     $33.82     $119.14  $118.18  -0.8%   $-0.27  |
|                                                                        |
|  Total invested                                                  $67.58|
|  Total open P&L                                                  $-0.69|
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
|  2026-09-11  SELL  RL  MomReversal  $33.81  P&L $-0.25                 |
|  2026-09-11  SELL  ADI  Pullback50  $34.06  P&L $-0.10                 |
|  2026-09-11  SELL  ABBV  Pullback50  $34.61  P&L $+0.61                |
|  2026-09-10  SELL  AES  Pullback50  $34.05  P&L $-0.00                 |
|  2026-09-10  SELL  ABBV  Pullback50  $33.90  P&L $-0.20                |
|  2026-09-10  SELL  AES  Pullback50  $34.09  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-14T09:16:10.100563-04:00 share=25% ===
2026-09-14 09:16:10,100 INFO === options_live_micro LIVE 2026-09-14T09:16:10.100563-04:00 share=25% ===
Live account equity $226.36 cash $158.78 #225458845 options_level=3
2026-09-14 09:16:10,326 INFO Live account equity $226.36 cash $158.78 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-14 09:16:10,396 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-14 09:16:10,466 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (155 earlier lines - see full log file)
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
## Ledger health — 2026-09-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1235 | WARN | <<<
| Missing exit records (post) |  1231 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    41 | INFO |
| Total closed lots           |  2193 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1204 med=-10.1% | TAINTED n=1829 med=-38.8% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.36 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T132109Z

- UTC timestamp: `20260914T132109Z`
- GitHub run: [#9848](https://github.com/28twagg-ops/TradingBot/actions/runs/34848591706)
- Run id: `34848591706`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`23s`
- Full logs: `logs/action_runs/20260914T132109Z_live_bot.log`, `logs/action_runs/20260914T132109Z_live_options.log`, `logs/action_runs/20260914T132109Z_options_bot.log`


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
{"ts_et":"2026-09-14T09:21:15.192890-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":10.9,"phases_s":{"reconcile":4.17},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9848","github_run_id":"34848591706","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:21:10  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.37|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.37|
|  Cash                                                           $158.78|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.59|
|  Open P&L                                                        $-0.68|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $33.77     $256.11  $253.04  -1.2%   $-0.41  |
|  TKR      MomReversal     $33.82     $119.14  $118.18  -0.8%   $-0.27  |
|                                                                        |
|  Total invested                                                  $67.59|
|  Total open P&L                                                  $-0.68|
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
|  2026-09-11  SELL  RL  MomReversal  $33.81  P&L $-0.25                 |
|  2026-09-11  SELL  ADI  Pullback50  $34.06  P&L $-0.10                 |
|  2026-09-11  SELL  ABBV  Pullback50  $34.61  P&L $+0.61                |
|  2026-09-10  SELL  AES  Pullback50  $34.05  P&L $-0.00                 |
|  2026-09-10  SELL  ABBV  Pullback50  $33.90  P&L $-0.20                |
|  2026-09-10  SELL  AES  Pullback50  $34.09  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-14T09:21:12.132464-04:00 share=25% ===
2026-09-14 09:21:12,132 INFO === options_live_micro LIVE 2026-09-14T09:21:12.132464-04:00 share=25% ===
Live account equity $226.37 cash $158.78 #225458845 options_level=3
2026-09-14 09:21:12,190 INFO Live account equity $226.37 cash $158.78 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-14 09:21:12,216 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-14 09:21:12,228 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (155 earlier lines - see full log file)
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
## Ledger health — 2026-09-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1235 | WARN | <<<
| Missing exit records (post) |  1231 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    41 | INFO |
| Total closed lots           |  2193 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1204 med=-10.1% | TAINTED n=1829 med=-38.8% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.37 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T132614Z

- UTC timestamp: `20260914T132614Z`
- GitHub run: [#9849](https://github.com/28twagg-ops/TradingBot/actions/runs/34849104508)
- Run id: `34849104508`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260914T132614Z_live_bot.log`, `logs/action_runs/20260914T132614Z_live_options.log`, `logs/action_runs/20260914T132614Z_options_bot.log`


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
{"ts_et":"2026-09-14T09:26:21.164064-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.8,"phases_s":{"reconcile":4.75},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9849","github_run_id":"34849104508","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:26:15  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.40|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.40|
|  Cash                                                           $158.78|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.62|
|  Open P&L                                                        $-0.65|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $33.80     $256.11  $253.25  -1.1%   $-0.38  |
|  TKR      MomReversal     $33.82     $119.14  $118.18  -0.8%   $-0.27  |
|                                                                        |
|  Total invested                                                  $67.62|
|  Total open P&L                                                  $-0.65|
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
|  2026-09-11  SELL  RL  MomReversal  $33.81  P&L $-0.25                 |
|  2026-09-11  SELL  ADI  Pullback50  $34.06  P&L $-0.10                 |
|  2026-09-11  SELL  ABBV  Pullback50  $34.61  P&L $+0.61                |
|  2026-09-10  SELL  AES  Pullback50  $34.05  P&L $-0.00                 |
|  2026-09-10  SELL  ABBV  Pullback50  $33.90  P&L $-0.20                |
|  2026-09-10  SELL  AES  Pullback50  $34.09  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-14T09:26:17.718407-04:00 share=25% ===
2026-09-14 09:26:17,718 INFO === options_live_micro LIVE 2026-09-14T09:26:17.718407-04:00 share=25% ===
Live account equity $226.40 cash $158.78 #225458845 options_level=3
2026-09-14 09:26:17,942 INFO Live account equity $226.40 cash $158.78 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-14 09:26:18,014 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-14 09:26:18,081 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (155 earlier lines - see full log file)
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
## Ledger health — 2026-09-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1235 | WARN | <<<
| Missing exit records (post) |  1231 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    41 | INFO |
| Total closed lots           |  2193 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1204 med=-10.1% | TAINTED n=1829 med=-38.8% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.4 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T133107Z

- UTC timestamp: `20260914T133107Z`
- GitHub run: [#9850](https://github.com/28twagg-ops/TradingBot/actions/runs/34849617457)
- Run id: `34849617457`
- Live bot: exit=`0`, duration=`216s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T133107Z_live_bot.log`, `logs/action_runs/20260914T133107Z_live_options.log`, `logs/action_runs/20260914T133107Z_options_bot.log`


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
{"ts_et":"2026-09-14T09:26:21.164064-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.8,"phases_s":{"reconcile":4.75},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9849","github_run_id":"34849104508","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:31:09  INFO      Mode: morning_prep
13:31:09  INFO        [prep_positions] 2/2 (2 valid)
13:31:09  INFO      Fetching tickers (universe=both)...
13:31:09  INFO        S&P 500: 503
13:31:09  INFO        MidCap 400: 400
13:31:09  INFO        Total: 903 tickers
13:31:10  INFO        [prep_universe] 40/901 (40 valid)
13:31:12  INFO        [prep_universe] 80/901 (80 valid)
13:31:13  INFO        [prep_universe] 120/901 (120 valid)
13:31:14  INFO        [prep_universe] 160/901 (160 valid)
13:31:15  INFO        [prep_universe] 200/901 (199 valid)
13:31:23  INFO        [prep_universe] 240/901 (238 valid)
13:31:36  INFO        [prep_universe] 280/901 (278 valid)
13:31:48  INFO        [prep_universe] 320/901 (318 valid)
13:31:58  INFO        [prep_universe] 360/901 (358 valid)
13:32:11  INFO        [prep_universe] 400/901 (398 valid)
13:32:24  INFO        [prep_universe] 440/901 (438 valid)
13:32:34  INFO        [prep_universe] 480/901 (478 valid)
13:32:47  INFO        [prep_universe] 520/901 (518 valid)
13:33:00  INFO        [prep_universe] 560/901 (558 valid)
13:33:13  INFO        [prep_universe] 600/901 (598 valid)
13:33:23  INFO        [prep_universe] 640/901 (638 valid)
13:33:36  INFO        [prep_universe] 680/901 (678 valid)
13:33:49  INFO        [prep_universe] 720/901 (718 valid)
13:33:59  INFO        [prep_universe] 760/901 (758 valid)
13:34:11  INFO        [prep_universe] 800/901 (798 valid)
13:34:24  INFO        [prep_universe] 840/901 (838 valid)
13:34:34  INFO        [prep_universe] 880/901 (878 valid)
13:34:41  INFO        [prep_universe] 901/901 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.53|
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
|  Invested                                                        $66.76|
|  Open P&L                                                        $-1.51|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $33.54     $256.11  $251.33  -1.9%   $-0.64  |
|  TKR      MomReversal     $33.21     $119.14  $116.08  -2.6%   $-0.88  |
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
|  Signal candidates                                                   39|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-14T09:34:44.515468-04:00 share=25% ===
2026-09-14 09:34:44,515 INFO === options_live_micro LIVE 2026-09-14T09:34:44.515468-04:00 share=25% ===
Live account equity $225.62 cash $158.78 #225458845 options_level=3
2026-09-14 09:34:44,736 INFO Live account equity $225.62 cash $158.78 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-14 09:34:44,781 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-14 09:34:44,798 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=41 paper_keys=yes dry_run=False
  alpaca positions=9
  FLAG b193|S218|235f18c1 missing from Alpaca
  FLAG b192|S218|0277ef32 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE FAIL: {"code":50010000,"message":"internal server error occurred"}
paper probe failed (non-fatal)
=== options_morning_bot (PAPER) 2026-09-14T09:34:47.447630-04:00 ===

[Run context]
2026-09-14 09:34:47,509 WARNING paper get_account failed attempt 1/3 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 2s
2026-09-14 09:34:49,584 WARNING paper get_account failed attempt 2/3 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 4s
2026-09-14 09:34:53,601 ERROR paper get_account failed after 3 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=9). Keys are fine; Alpaca account endpoint is flaky. Using cached equity $1000241.84.
2026-09-14 09:34:53,630 WARNING paper get_account failed attempt 1/2 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 2s
2026-09-14 09:34:55,654 ERROR paper get_account failed after 2 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: using cached paper equity $1000241.84 (get_account: {"code":50010000,"message":"internal server error occurred"})
2026-09-14 09:34:55,721 WARNING lab get_account failed attempt 1/2: {"code":50010000,"message":"internal server error occurred"}
2026-09-14 09:34:57,747 ERROR lab get_account failed after 2 attempts: {"code":50010000,"message":"internal server error occurred"}

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b330|lab0330_s357_w2_1005_1045_r1|S357] stop_loss (-100.0%) SELL failed PATH260925C00017000: {"code":50010000,"message":"internal server error occurred"}
  EXIT [b802|lab0802_s404_w2_1005_1045_r1|S404] stop_loss (-100.0%) SELL failed AMD260914C00550000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b779|lab0779_s397_w2_1005_1045_r2|S397] stop_loss (-100.0%) SELL failed AMD260914C00550000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 upgraded=0 already=1 failed=4 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---
