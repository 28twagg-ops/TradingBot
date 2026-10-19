# Daily Comprehensive Action Review - 2026-10-19

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20261019T130141Z

- UTC timestamp: `20261019T130141Z`
- GitHub run: [#13137](https://github.com/28twagg-ops/TradingBot/actions/runs/39256461336)
- Run id: `39256461336`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20261019T130141Z_live_bot.log`, `logs/action_runs/20261019T130141Z_live_options.log`, `logs/action_runs/20261019T130141Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1697 | 48.1 | -28.6 | +36.9 | $+18,429 |
| TAINTED | 2007 | 32.3 | -40.5 | +10.7 | $-11,066 |
| KEEP-only | 836 | 60.4 | +50.7 | +54.3 | $+12,642 |
| KEEP-only recent | 643 | 58.8 | +52.9 | +59.9 | $+8,581 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-19T09:01:47.730480-04:00","date":"2026-10-19","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.52},"signals":0,"placed":0,"equity":992500.42,"open_positions":2,"pending_orders":0,"open_lots":2,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13137","github_run_id":"39256461336","status":"ok","data_quality":{"clean":{"n":1697,"win":48.14,"med":-28.57,"avg":36.89,"pnl":18428.83},"tainted":{"n":2007,"win":32.29,"med":-40.54,"avg":10.69,"pnl":-11066.28},"keep_only":{"n":836,"win":60.41,"med":50.71,"avg":54.26,"pnl":12642.45},"keep_only_recent":{"n":643,"win":58.79,"med":52.94,"avg":59.95,"pnl":8581.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:01:42  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.35|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.35|
|  Cash                                                           $123.13|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $102.22|
|  Open P&L                                                        $+1.16|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CFG      MomReversal     $33.98     $62.90   $63.36   +0.7%   $+0.25  |
|  MTB      MomReversal     $33.74     $215.23  $215.28  +0.0%   $+0.01  |
|  PNC      MomReversal     $34.50     $211.72  $217.39  +2.7%   $+0.90  |
|                                                                        |
|  Total invested                                                 $102.22|
|  Total open P&L                                                  $+1.16|
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
|  2026-10-16  SELL  AMCR  Pullback50  $33.62  P&L $-0.25                |
|  2026-10-16  SELL  ALLE  Pullback50  $33.62  P&L $-0.25                |
|  2026-10-16  SELL  KEY  MomReversal  $34.62  P&L $+1.11                |
|  2026-10-16  SELL  APD  Pullback50  $33.96  P&L $+0.34                 |
|  2026-10-15  SELL  APD  Pullback50  $33.60  P&L $-0.01                 |
|  2026-10-15  SELL  GS  MomReversal  $33.10  P&L $-0.47                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-19T09:01:44.017945-04:00 share=25% ===
2026-10-19 09:01:44,018 INFO === options_live_micro LIVE 2026-10-19T09:01:44.017945-04:00 share=25% ===
Live account equity $225.35 cash $123.13 #225458845 options_level=3
2026-10-19 09:01:44,238 INFO Live account equity $225.35 cash $123.13 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-19 09:01:44,306 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-19 09:01:44,373 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (190 earlier lines - see full log file)
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
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1914 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     2 | INFO |
| Total closed lots           |  2815 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1697 med=-28.6% | TAINTED n=2007 med=-40.5% | KEEP-only n=836 med=+50.7% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.35 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261019T130635Z

- UTC timestamp: `20261019T130635Z`
- GitHub run: [#13138](https://github.com/28twagg-ops/TradingBot/actions/runs/39257143323)
- Run id: `39257143323`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20261019T130635Z_live_bot.log`, `logs/action_runs/20261019T130635Z_live_options.log`, `logs/action_runs/20261019T130635Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1697 | 48.1 | -28.6 | +36.9 | $+18,429 |
| TAINTED | 2007 | 32.3 | -40.5 | +10.7 | $-11,066 |
| KEEP-only | 836 | 60.4 | +50.7 | +54.3 | $+12,642 |
| KEEP-only recent | 643 | 58.8 | +52.9 | +59.9 | $+8,581 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-19T09:06:40.738642-04:00","date":"2026-10-19","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.43},"signals":0,"placed":0,"equity":992474.89,"open_positions":2,"pending_orders":0,"open_lots":2,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13138","github_run_id":"39257143323","status":"ok","data_quality":{"clean":{"n":1697,"win":48.14,"med":-28.57,"avg":36.89,"pnl":18428.83},"tainted":{"n":2007,"win":32.29,"med":-40.54,"avg":10.69,"pnl":-11066.28},"keep_only":{"n":836,"win":60.41,"med":50.71,"avg":54.26,"pnl":12642.45},"keep_only_recent":{"n":643,"win":58.79,"med":52.94,"avg":59.95,"pnl":8581.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:06:36  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.35|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.35|
|  Cash                                                           $123.13|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $102.22|
|  Open P&L                                                        $+1.16|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CFG      MomReversal     $33.98     $62.90   $63.36   +0.7%   $+0.25  |
|  MTB      MomReversal     $33.74     $215.23  $215.28  +0.0%   $+0.01  |
|  PNC      MomReversal     $34.50     $211.72  $217.39  +2.7%   $+0.90  |
|                                                                        |
|  Total invested                                                 $102.22|
|  Total open P&L                                                  $+1.16|
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
|  2026-10-16  SELL  AMCR  Pullback50  $33.62  P&L $-0.25                |
|  2026-10-16  SELL  ALLE  Pullback50  $33.62  P&L $-0.25                |
|  2026-10-16  SELL  KEY  MomReversal  $34.62  P&L $+1.11                |
|  2026-10-16  SELL  APD  Pullback50  $33.96  P&L $+0.34                 |
|  2026-10-15  SELL  APD  Pullback50  $33.60  P&L $-0.01                 |
|  2026-10-15  SELL  GS  MomReversal  $33.10  P&L $-0.47                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-19T09:06:37.685632-04:00 share=25% ===
2026-10-19 09:06:37,685 INFO === options_live_micro LIVE 2026-10-19T09:06:37.685632-04:00 share=25% ===
Live account equity $225.35 cash $123.13 #225458845 options_level=3
2026-10-19 09:06:37,884 INFO Live account equity $225.35 cash $123.13 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-19 09:06:37,941 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-19 09:06:37,997 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (181 earlier lines - see full log file)
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
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1914 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     2 | INFO |
| Total closed lots           |  2815 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1697 med=-28.6% | TAINTED n=2007 med=-40.5% | KEEP-only n=836 med=+50.7% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.35 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261019T131130Z

- UTC timestamp: `20261019T131130Z`
- GitHub run: [#13139](https://github.com/28twagg-ops/TradingBot/actions/runs/39257840755)
- Run id: `39257840755`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20261019T131130Z_live_bot.log`, `logs/action_runs/20261019T131130Z_live_options.log`, `logs/action_runs/20261019T131130Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1697 | 48.1 | -28.6 | +36.9 | $+18,429 |
| TAINTED | 2007 | 32.3 | -40.5 | +10.7 | $-11,066 |
| KEEP-only | 836 | 60.4 | +50.7 | +54.3 | $+12,642 |
| KEEP-only recent | 643 | 58.8 | +52.9 | +59.9 | $+8,581 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-19T09:11:35.393289-04:00","date":"2026-10-19","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.44},"signals":0,"placed":0,"equity":992395.89,"open_positions":2,"pending_orders":0,"open_lots":2,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13139","github_run_id":"39257840755","status":"ok","data_quality":{"clean":{"n":1697,"win":48.14,"med":-28.57,"avg":36.89,"pnl":18428.83},"tainted":{"n":2007,"win":32.29,"med":-40.54,"avg":10.69,"pnl":-11066.28},"keep_only":{"n":836,"win":60.41,"med":50.71,"avg":54.26,"pnl":12642.45},"keep_only_recent":{"n":643,"win":58.79,"med":52.94,"avg":59.95,"pnl":8581.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:11:31  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.20|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.20|
|  Cash                                                           $123.13|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $102.07|
|  Open P&L                                                        $+1.01|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CFG      MomReversal     $33.98     $62.90   $63.36   +0.7%   $+0.25  |
|  MTB      MomReversal     $33.74     $215.23  $215.28  +0.0%   $+0.01  |
|  PNC      MomReversal     $34.36     $211.72  $216.50  +2.3%   $+0.76  |
|                                                                        |
|  Total invested                                                 $102.07|
|  Total open P&L                                                  $+1.01|
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
|  2026-10-16  SELL  AMCR  Pullback50  $33.62  P&L $-0.25                |
|  2026-10-16  SELL  ALLE  Pullback50  $33.62  P&L $-0.25                |
|  2026-10-16  SELL  KEY  MomReversal  $34.62  P&L $+1.11                |
|  2026-10-16  SELL  APD  Pullback50  $33.96  P&L $+0.34                 |
|  2026-10-15  SELL  APD  Pullback50  $33.60  P&L $-0.01                 |
|  2026-10-15  SELL  GS  MomReversal  $33.10  P&L $-0.47                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-19T09:11:32.955127-04:00 share=25% ===
2026-10-19 09:11:32,955 INFO === options_live_micro LIVE 2026-10-19T09:11:32.955127-04:00 share=25% ===
Live account equity $225.20 cash $123.13 #225458845 options_level=3
2026-10-19 09:11:33,153 INFO Live account equity $225.20 cash $123.13 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-19 09:11:33,212 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-19 09:11:33,271 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (181 earlier lines - see full log file)
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
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1914 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     2 | INFO |
| Total closed lots           |  2815 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1697 med=-28.6% | TAINTED n=2007 med=-40.5% | KEEP-only n=836 med=+50.7% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.2 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261019T131652Z

- UTC timestamp: `20261019T131652Z`
- GitHub run: [#13140](https://github.com/28twagg-ops/TradingBot/actions/runs/39258538237)
- Run id: `39258538237`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20261019T131652Z_live_bot.log`, `logs/action_runs/20261019T131652Z_live_options.log`, `logs/action_runs/20261019T131652Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1697 | 48.1 | -28.6 | +36.9 | $+18,429 |
| TAINTED | 2007 | 32.3 | -40.5 | +10.7 | $-11,066 |
| KEEP-only | 836 | 60.4 | +50.7 | +54.3 | $+12,642 |
| KEEP-only recent | 643 | 58.8 | +52.9 | +59.9 | $+8,581 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-19T09:16:58.322110-04:00","date":"2026-10-19","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":992412.16,"open_positions":2,"pending_orders":0,"open_lots":2,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13140","github_run_id":"39258538237","status":"ok","data_quality":{"clean":{"n":1697,"win":48.14,"med":-28.57,"avg":36.89,"pnl":18428.83},"tainted":{"n":2007,"win":32.29,"med":-40.54,"avg":10.69,"pnl":-11066.28},"keep_only":{"n":836,"win":60.41,"med":50.71,"avg":54.26,"pnl":12642.45},"keep_only_recent":{"n":643,"win":58.79,"med":52.94,"avg":59.95,"pnl":8581.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:16:54  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.20|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.20|
|  Cash                                                           $123.13|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $102.07|
|  Open P&L                                                        $+1.01|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CFG      MomReversal     $33.98     $62.90   $63.36   +0.7%   $+0.25  |
|  MTB      MomReversal     $33.74     $215.23  $215.28  +0.0%   $+0.01  |
|  PNC      MomReversal     $34.36     $211.72  $216.50  +2.3%   $+0.76  |
|                                                                        |
|  Total invested                                                 $102.07|
|  Total open P&L                                                  $+1.01|
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
|  2026-10-16  SELL  AMCR  Pullback50  $33.62  P&L $-0.25                |
|  2026-10-16  SELL  ALLE  Pullback50  $33.62  P&L $-0.25                |
|  2026-10-16  SELL  KEY  MomReversal  $34.62  P&L $+1.11                |
|  2026-10-16  SELL  APD  Pullback50  $33.96  P&L $+0.34                 |
|  2026-10-15  SELL  APD  Pullback50  $33.60  P&L $-0.01                 |
|  2026-10-15  SELL  GS  MomReversal  $33.10  P&L $-0.47                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-19T09:16:55.416602-04:00 share=25% ===
2026-10-19 09:16:55,416 INFO === options_live_micro LIVE 2026-10-19T09:16:55.416602-04:00 share=25% ===
Live account equity $225.20 cash $123.13 #225458845 options_level=3
2026-10-19 09:16:55,475 INFO Live account equity $225.20 cash $123.13 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-19 09:16:55,488 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-19 09:16:55,501 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (181 earlier lines - see full log file)
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
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1914 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     2 | INFO |
| Total closed lots           |  2815 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1697 med=-28.6% | TAINTED n=2007 med=-40.5% | KEEP-only n=836 med=+50.7% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.2 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261019T132152Z

- UTC timestamp: `20261019T132152Z`
- GitHub run: [#13141](https://github.com/28twagg-ops/TradingBot/actions/runs/39259246766)
- Run id: `39259246766`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20261019T132152Z_live_bot.log`, `logs/action_runs/20261019T132152Z_live_options.log`, `logs/action_runs/20261019T132152Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1697 | 48.1 | -28.6 | +36.9 | $+18,429 |
| TAINTED | 2007 | 32.3 | -40.5 | +10.7 | $-11,066 |
| KEEP-only | 836 | 60.4 | +50.7 | +54.3 | $+12,642 |
| KEEP-only recent | 643 | 58.8 | +52.9 | +59.9 | $+8,581 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-19T09:21:58.648599-04:00","date":"2026-10-19","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.44},"signals":0,"placed":0,"equity":992450.93,"open_positions":2,"pending_orders":0,"open_lots":2,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13141","github_run_id":"39259246766","status":"ok","data_quality":{"clean":{"n":1697,"win":48.14,"med":-28.57,"avg":36.89,"pnl":18428.83},"tainted":{"n":2007,"win":32.29,"med":-40.54,"avg":10.69,"pnl":-11066.28},"keep_only":{"n":836,"win":60.41,"med":50.71,"avg":54.26,"pnl":12642.45},"keep_only_recent":{"n":643,"win":58.79,"med":52.94,"avg":59.95,"pnl":8581.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:21:53  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.20|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.20|
|  Cash                                                           $123.13|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $102.07|
|  Open P&L                                                        $+1.01|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CFG      MomReversal     $33.98     $62.90   $63.36   +0.7%   $+0.25  |
|  MTB      MomReversal     $33.74     $215.23  $215.28  +0.0%   $+0.01  |
|  PNC      MomReversal     $34.36     $211.72  $216.50  +2.3%   $+0.76  |
|                                                                        |
|  Total invested                                                 $102.07|
|  Total open P&L                                                  $+1.01|
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
|  2026-10-16  SELL  AMCR  Pullback50  $33.62  P&L $-0.25                |
|  2026-10-16  SELL  ALLE  Pullback50  $33.62  P&L $-0.25                |
|  2026-10-16  SELL  KEY  MomReversal  $34.62  P&L $+1.11                |
|  2026-10-16  SELL  APD  Pullback50  $33.96  P&L $+0.34                 |
|  2026-10-15  SELL  APD  Pullback50  $33.60  P&L $-0.01                 |
|  2026-10-15  SELL  GS  MomReversal  $33.10  P&L $-0.47                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-19T09:21:55.335118-04:00 share=25% ===
2026-10-19 09:21:55,335 INFO === options_live_micro LIVE 2026-10-19T09:21:55.335118-04:00 share=25% ===
Live account equity $225.20 cash $123.13 #225458845 options_level=3
2026-10-19 09:21:55,523 INFO Live account equity $225.20 cash $123.13 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-19 09:21:55,574 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-19 09:21:55,625 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (181 earlier lines - see full log file)
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
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1914 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     2 | INFO |
| Total closed lots           |  2815 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1697 med=-28.6% | TAINTED n=2007 med=-40.5% | KEEP-only n=836 med=+50.7% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.2 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261019T132637Z

- UTC timestamp: `20261019T132637Z`
- GitHub run: [#13142](https://github.com/28twagg-ops/TradingBot/actions/runs/39259961151)
- Run id: `39259961151`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20261019T132637Z_live_bot.log`, `logs/action_runs/20261019T132637Z_live_options.log`, `logs/action_runs/20261019T132637Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1697 | 48.1 | -28.6 | +36.9 | $+18,429 |
| TAINTED | 2007 | 32.3 | -40.5 | +10.7 | $-11,066 |
| KEEP-only | 836 | 60.4 | +50.7 | +54.3 | $+12,642 |
| KEEP-only recent | 643 | 58.8 | +52.9 | +59.9 | $+8,581 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-19T09:26:41.762479-04:00","date":"2026-10-19","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.3},"signals":0,"placed":0,"equity":992467.39,"open_positions":2,"pending_orders":0,"open_lots":2,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13142","github_run_id":"39259961151","status":"ok","data_quality":{"clean":{"n":1697,"win":48.14,"med":-28.57,"avg":36.89,"pnl":18428.83},"tainted":{"n":2007,"win":32.29,"med":-40.54,"avg":10.69,"pnl":-11066.28},"keep_only":{"n":836,"win":60.41,"med":50.71,"avg":54.26,"pnl":12642.45},"keep_only_recent":{"n":643,"win":58.79,"med":52.94,"avg":59.95,"pnl":8581.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:26:38  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.20|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.20|
|  Cash                                                           $123.13|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $102.07|
|  Open P&L                                                        $+1.01|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CFG      MomReversal     $33.98     $62.90   $63.36   +0.7%   $+0.25  |
|  MTB      MomReversal     $33.74     $215.23  $215.28  +0.0%   $+0.01  |
|  PNC      MomReversal     $34.36     $211.72  $216.50  +2.3%   $+0.76  |
|                                                                        |
|  Total invested                                                 $102.07|
|  Total open P&L                                                  $+1.01|
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
|  2026-10-16  SELL  AMCR  Pullback50  $33.62  P&L $-0.25                |
|  2026-10-16  SELL  ALLE  Pullback50  $33.62  P&L $-0.25                |
|  2026-10-16  SELL  KEY  MomReversal  $34.62  P&L $+1.11                |
|  2026-10-16  SELL  APD  Pullback50  $33.96  P&L $+0.34                 |
|  2026-10-15  SELL  APD  Pullback50  $33.60  P&L $-0.01                 |
|  2026-10-15  SELL  GS  MomReversal  $33.10  P&L $-0.47                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-19T09:26:39.692414-04:00 share=25% ===
2026-10-19 09:26:39,692 INFO === options_live_micro LIVE 2026-10-19T09:26:39.692414-04:00 share=25% ===
Live account equity $225.20 cash $123.13 #225458845 options_level=3
2026-10-19 09:26:39,805 INFO Live account equity $225.20 cash $123.13 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-19 09:26:39,835 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-19 09:26:39,865 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (181 earlier lines - see full log file)
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
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1914 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     2 | INFO |
| Total closed lots           |  2815 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1697 med=-28.6% | TAINTED n=2007 med=-40.5% | KEEP-only n=836 med=+50.7% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.2 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261019T133147Z

- UTC timestamp: `20261019T133147Z`
- GitHub run: [#13143](https://github.com/28twagg-ops/TradingBot/actions/runs/39260679321)
- Run id: `39260679321`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261019T133147Z_live_bot.log`, `logs/action_runs/20261019T133147Z_live_options.log`, `logs/action_runs/20261019T133147Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1697 | 48.1 | -28.6 | +36.9 | $+18,429 |
| TAINTED | 2007 | 32.3 | -40.5 | +10.7 | $-11,066 |
| KEEP-only | 836 | 60.4 | +50.7 | +54.3 | $+12,642 |
| KEEP-only recent | 643 | 58.8 | +52.9 | +59.9 | $+8,581 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-19T09:26:41.762479-04:00","date":"2026-10-19","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.3},"signals":0,"placed":0,"equity":992467.39,"open_positions":2,"pending_orders":0,"open_lots":2,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13142","github_run_id":"39259961151","status":"ok","data_quality":{"clean":{"n":1697,"win":48.14,"med":-28.57,"avg":36.89,"pnl":18428.83},"tainted":{"n":2007,"win":32.29,"med":-40.54,"avg":10.69,"pnl":-11066.28},"keep_only":{"n":836,"win":60.41,"med":50.71,"avg":54.26,"pnl":12642.45},"keep_only_recent":{"n":643,"win":58.79,"med":52.94,"avg":59.95,"pnl":8581.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:31:48  INFO      Mode: morning_prep
13:31:49  INFO        [prep_positions] 3/3 (3 valid)
13:31:49  INFO      Fetching tickers (universe=both)...
13:31:49  INFO        S&P 500: 503
13:31:49  INFO        MidCap 400: 400
13:31:49  INFO        Total: 903 tickers
13:31:50  INFO        [prep_universe] 40/900 (40 valid)
13:31:51  INFO        [prep_universe] 80/900 (80 valid)
13:31:52  INFO        [prep_universe] 120/900 (120 valid)
13:31:53  INFO        [prep_universe] 160/900 (160 valid)
13:31:54  INFO        [prep_universe] 200/900 (199 valid)
13:32:04  INFO        [prep_universe] 240/900 (238 valid)
13:32:14  INFO        [prep_universe] 280/900 (278 valid)
13:32:27  INFO        [prep_universe] 320/900 (318 valid)
13:32:40  INFO        [prep_universe] 360/900 (358 valid)
13:32:50  INFO        [prep_universe] 400/900 (398 valid)
13:33:03  INFO        [prep_universe] 440/900 (438 valid)
13:33:16  INFO        [prep_universe] 480/900 (477 valid)
13:33:26  INFO        [prep_universe] 520/900 (517 valid)
13:33:39  INFO        [prep_universe] 560/900 (557 valid)
13:33:52  INFO        [prep_universe] 600/900 (597 valid)
13:34:02  INFO        [prep_universe] 640/900 (637 valid)
13:34:15  INFO        [prep_universe] 680/900 (677 valid)
13:34:28  INFO        [prep_universe] 720/900 (717 valid)
13:34:38  INFO        [prep_universe] 760/900 (757 valid)
13:34:51  INFO        [prep_universe] 800/900 (797 valid)
13:35:04  INFO        [prep_universe] 840/900 (837 valid)
13:35:14  INFO        [prep_universe] 880/900 (877 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261019T133717Z

- UTC timestamp: `20261019T133717Z`
- GitHub run: [#13144](https://github.com/28twagg-ops/TradingBot/actions/runs/39261391829)
- Run id: `39261391829`
- Live bot: exit=`0`, duration=`215s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261019T133717Z_live_bot.log`, `logs/action_runs/20261019T133717Z_live_options.log`, `logs/action_runs/20261019T133717Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1697 | 48.1 | -28.6 | +36.9 | $+18,429 |
| TAINTED | 2007 | 32.3 | -40.5 | +10.7 | $-11,066 |
| KEEP-only | 836 | 60.4 | +50.7 | +54.3 | $+12,642 |
| KEEP-only recent | 643 | 58.8 | +52.9 | +59.9 | $+8,581 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-19T09:26:41.762479-04:00","date":"2026-10-19","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.3},"signals":0,"placed":0,"equity":992467.39,"open_positions":2,"pending_orders":0,"open_lots":2,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13142","github_run_id":"39259961151","status":"ok","data_quality":{"clean":{"n":1697,"win":48.14,"med":-28.57,"avg":36.89,"pnl":18428.83},"tainted":{"n":2007,"win":32.29,"med":-40.54,"avg":10.69,"pnl":-11066.28},"keep_only":{"n":836,"win":60.41,"med":50.71,"avg":54.26,"pnl":12642.45},"keep_only_recent":{"n":643,"win":58.79,"med":52.94,"avg":59.95,"pnl":8581.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:37:18  INFO      Mode: morning_prep
13:37:18  INFO        [prep_positions] 3/3 (3 valid)
13:37:18  INFO      Fetching tickers (universe=both)...
13:37:19  INFO        S&P 500: 503
13:37:19  INFO        MidCap 400: 400
13:37:19  INFO        Total: 903 tickers
13:37:20  INFO        [prep_universe] 40/900 (40 valid)
13:37:22  INFO        [prep_universe] 80/900 (80 valid)
13:37:23  INFO        [prep_universe] 120/900 (120 valid)
13:37:24  INFO        [prep_universe] 160/900 (160 valid)
13:37:26  INFO        [prep_universe] 200/900 (199 valid)
13:37:33  INFO        [prep_universe] 240/900 (238 valid)
13:37:46  INFO        [prep_universe] 280/900 (278 valid)
13:37:56  INFO        [prep_universe] 320/900 (318 valid)
13:38:09  INFO        [prep_universe] 360/900 (358 valid)
13:38:20  INFO        [prep_universe] 400/900 (398 valid)
13:38:33  INFO        [prep_universe] 440/900 (438 valid)
13:38:46  INFO        [prep_universe] 480/900 (477 valid)
13:38:56  INFO        [prep_universe] 520/900 (517 valid)
13:39:10  INFO        [prep_universe] 560/900 (557 valid)
13:39:20  INFO        [prep_universe] 600/900 (597 valid)
13:39:33  INFO        [prep_universe] 640/900 (637 valid)
13:39:46  INFO        [prep_universe] 680/900 (677 valid)
13:39:56  INFO        [prep_universe] 720/900 (717 valid)
13:40:09  INFO        [prep_universe] 760/900 (757 valid)
13:40:20  INFO        [prep_universe] 800/900 (797 valid)
13:40:33  INFO        [prep_universe] 840/900 (837 valid)
13:40:46  INFO        [prep_universe] 880/900 (877 valid)
13:40:50  INFO        [prep_universe] 900/900 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:37 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.74|
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
|  Open P&L                                                        $+0.55|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CFG      MomReversal     $33.78     $62.90   $63.00   +0.2%   $+0.05  |
|  MTB      MomReversal     $33.38     $215.23  $212.99  -1.0%   $-0.35  |
|  PNC      MomReversal     $34.44     $211.72  $217.02  +2.5%   $+0.84  |
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
|  Signal candidates                                                   39|
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

## Run 20261019T134256Z

- UTC timestamp: `20261019T134256Z`
- GitHub run: [#13145](https://github.com/28twagg-ops/TradingBot/actions/runs/39262090243)
- Run id: `39262090243`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261019T134256Z_live_bot.log`, `logs/action_runs/20261019T134256Z_live_options.log`, `logs/action_runs/20261019T134256Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1697 | 48.1 | -28.6 | +36.9 | $+18,429 |
| TAINTED | 2007 | 32.3 | -40.5 | +10.7 | $-11,066 |
| KEEP-only | 836 | 60.4 | +50.7 | +54.3 | $+12,642 |
| KEEP-only recent | 643 | 58.8 | +52.9 | +59.9 | $+8,581 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-19T09:26:41.762479-04:00","date":"2026-10-19","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.3},"signals":0,"placed":0,"equity":992467.39,"open_positions":2,"pending_orders":0,"open_lots":2,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13142","github_run_id":"39259961151","status":"ok","data_quality":{"clean":{"n":1697,"win":48.14,"med":-28.57,"avg":36.89,"pnl":18428.83},"tainted":{"n":2007,"win":32.29,"med":-40.54,"avg":10.69,"pnl":-11066.28},"keep_only":{"n":836,"win":60.41,"med":50.71,"avg":54.26,"pnl":12642.45},"keep_only_recent":{"n":643,"win":58.79,"med":52.94,"avg":59.95,"pnl":8581.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:42:58  INFO      Mode: morning_prep
13:42:58  INFO        [prep_positions] 3/3 (3 valid)
13:42:58  INFO        Universe cache hit: 903 tickers (tickers_2026-10-19.json)
13:42:59  INFO        [prep_universe] 40/900 (40 valid)
13:43:00  INFO        [prep_universe] 80/900 (80 valid)
13:43:02  INFO        [prep_universe] 120/900 (120 valid)
13:43:03  INFO        [prep_universe] 160/900 (160 valid)
13:43:04  INFO        [prep_universe] 200/900 (199 valid)
13:43:12  INFO        [prep_universe] 240/900 (238 valid)
13:43:25  INFO        [prep_universe] 280/900 (278 valid)
13:43:38  INFO        [prep_universe] 320/900 (318 valid)
13:43:48  INFO        [prep_universe] 360/900 (358 valid)
13:44:01  INFO        [prep_universe] 400/900 (398 valid)
13:44:11  INFO        [prep_universe] 440/900 (438 valid)
13:44:24  INFO        [prep_universe] 480/900 (477 valid)
13:44:37  INFO        [prep_universe] 520/900 (517 valid)
13:44:47  INFO        [prep_universe] 560/900 (557 valid)
13:45:00  INFO        [prep_universe] 600/900 (597 valid)
13:45:14  INFO        [prep_universe] 640/900 (637 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261019T134726Z

- UTC timestamp: `20261019T134726Z`
- GitHub run: [#13146](https://github.com/28twagg-ops/TradingBot/actions/runs/39262806677)
- Run id: `39262806677`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261019T134726Z_live_bot.log`, `logs/action_runs/20261019T134726Z_live_options.log`, `logs/action_runs/20261019T134726Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1697 | 48.1 | -28.6 | +36.9 | $+18,429 |
| TAINTED | 2007 | 32.3 | -40.5 | +10.7 | $-11,066 |
| KEEP-only | 836 | 60.4 | +50.7 | +54.3 | $+12,642 |
| KEEP-only recent | 643 | 58.8 | +52.9 | +59.9 | $+8,581 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-19T09:26:41.762479-04:00","date":"2026-10-19","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.3},"signals":0,"placed":0,"equity":992467.39,"open_positions":2,"pending_orders":0,"open_lots":2,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13142","github_run_id":"39259961151","status":"ok","data_quality":{"clean":{"n":1697,"win":48.14,"med":-28.57,"avg":36.89,"pnl":18428.83},"tainted":{"n":2007,"win":32.29,"med":-40.54,"avg":10.69,"pnl":-11066.28},"keep_only":{"n":836,"win":60.41,"med":50.71,"avg":54.26,"pnl":12642.45},"keep_only_recent":{"n":643,"win":58.79,"med":52.94,"avg":59.95,"pnl":8581.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:47:27  INFO      Mode: morning_scan
13:47:28  INFO        [positions] 3/3 (3 valid)
13:47:28  INFO        SELL MARKET [urgent] MTB closed
13:47:30  INFO        TX logged: SELL MTB  P&L -1.12%
13:47:30  INFO        SELL LIMIT CFG  qty=0.536265064  limit=$63.00  id=a0e09d73-5cb0-432f-a6cd-718f31b27c19
13:47:51  INFO        SELL LIMIT filled CFG (confirmed by position check)
13:47:51  INFO        TX logged: SELL CFG  P&L 0.35%
13:47:51  INFO        SELL LIMIT PNC  qty=0.15870017  limit=$217.10  id=8eb3a7e1-7843-4c17-bc29-829eea8a6449
13:48:11  INFO        SELL LIMIT filled PNC (confirmed by position check)
13:48:12  INFO        TX logged: SELL PNC  P&L 2.79%
13:48:12  INFO        Universe cache hit: 903 tickers (tickers_2026-10-19.json)
13:48:12  INFO        [universe] 40/903 (40 valid)
13:48:14  INFO        [universe] 80/903 (80 valid)
13:48:15  INFO        [universe] 120/903 (120 valid)
13:48:16  INFO        [universe] 160/903 (160 valid)
13:48:17  INFO        [universe] 200/903 (199 valid)
13:48:24  INFO        [universe] 240/903 (238 valid)
13:48:37  INFO        [universe] 280/903 (278 valid)
13:48:50  INFO        [universe] 320/903 (318 valid)
13:49:00  INFO        [universe] 360/903 (358 valid)
13:49:13  INFO        [universe] 400/903 (398 valid)
13:49:26  INFO        [universe] 440/903 (438 valid)
13:49:37  INFO        [universe] 480/903 (477 valid)
13:49:49  INFO        [universe] 520/903 (517 valid)
13:50:02  INFO        [universe] 560/903 (557 valid)
13:50:13  INFO        [universe] 600/903 (597 valid)
13:50:26  INFO        [universe] 640/903 (637 valid)
13:50:36  INFO        [universe] 680/903 (677 valid)
13:50:49  INFO        [universe] 720/903 (717 valid)
13:51:02  INFO        [universe] 760/903 (757 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261019T135313Z

- UTC timestamp: `20261019T135313Z`
- GitHub run: [#13147](https://github.com/28twagg-ops/TradingBot/actions/runs/39263529967)
- Run id: `39263529967`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261019T135313Z_live_bot.log`, `logs/action_runs/20261019T135313Z_live_options.log`, `logs/action_runs/20261019T135313Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1697 | 48.1 | -28.6 | +36.9 | $+18,429 |
| TAINTED | 2007 | 32.3 | -40.5 | +10.7 | $-11,066 |
| KEEP-only | 836 | 60.4 | +50.7 | +54.3 | $+12,642 |
| KEEP-only recent | 643 | 58.8 | +52.9 | +59.9 | $+8,581 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-19T09:26:41.762479-04:00","date":"2026-10-19","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.3},"signals":0,"placed":0,"equity":992467.39,"open_positions":2,"pending_orders":0,"open_lots":2,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13142","github_run_id":"39259961151","status":"ok","data_quality":{"clean":{"n":1697,"win":48.14,"med":-28.57,"avg":36.89,"pnl":18428.83},"tainted":{"n":2007,"win":32.29,"med":-40.54,"avg":10.69,"pnl":-11066.28},"keep_only":{"n":836,"win":60.41,"med":50.71,"avg":54.26,"pnl":12642.45},"keep_only_recent":{"n":643,"win":58.79,"med":52.94,"avg":59.95,"pnl":8581.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:53:14  INFO      Mode: morning_scan
13:53:15  INFO        Universe cache hit: 903 tickers (tickers_2026-10-19.json)
13:53:16  INFO        [universe] 40/903 (40 valid)
13:53:17  INFO        [universe] 80/903 (80 valid)
13:53:18  INFO        [universe] 120/903 (120 valid)
13:53:19  INFO        [universe] 160/903 (160 valid)
13:53:20  INFO        [universe] 200/903 (199 valid)
13:53:30  INFO        [universe] 240/903 (238 valid)
13:53:40  INFO        [universe] 280/903 (278 valid)
13:53:52  INFO        [universe] 320/903 (318 valid)
13:54:06  INFO        [universe] 360/903 (358 valid)
13:54:16  INFO        [universe] 400/903 (398 valid)
13:54:28  INFO        [universe] 440/903 (438 valid)
13:54:42  INFO        [universe] 480/903 (477 valid)
13:54:52  INFO        [universe] 520/903 (517 valid)
13:55:05  INFO        [universe] 560/903 (557 valid)
13:55:18  INFO        [universe] 600/903 (597 valid)
13:55:28  INFO        [universe] 640/903 (637 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261019T135732Z

- UTC timestamp: `20261019T135732Z`
- GitHub run: [#13148](https://github.com/28twagg-ops/TradingBot/actions/runs/39264264761)
- Run id: `39264264761`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261019T135732Z_live_bot.log`, `logs/action_runs/20261019T135732Z_live_options.log`, `logs/action_runs/20261019T135732Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1697 | 48.1 | -28.6 | +36.9 | $+18,429 |
| TAINTED | 2007 | 32.3 | -40.5 | +10.7 | $-11,066 |
| KEEP-only | 836 | 60.4 | +50.7 | +54.3 | $+12,642 |
| KEEP-only recent | 643 | 58.8 | +52.9 | +59.9 | $+8,581 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-19T09:26:41.762479-04:00","date":"2026-10-19","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.3},"signals":0,"placed":0,"equity":992467.39,"open_positions":2,"pending_orders":0,"open_lots":2,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13142","github_run_id":"39259961151","status":"ok","data_quality":{"clean":{"n":1697,"win":48.14,"med":-28.57,"avg":36.89,"pnl":18428.83},"tainted":{"n":2007,"win":32.29,"med":-40.54,"avg":10.69,"pnl":-11066.28},"keep_only":{"n":836,"win":60.41,"med":50.71,"avg":54.26,"pnl":12642.45},"keep_only_recent":{"n":643,"win":58.79,"med":52.94,"avg":59.95,"pnl":8581.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
... (66 earlier lines - see full log file)
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
|  Buys today: 0  |  entry cap: 3  |  max open: 3                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (30257.1m))|
+========================================================================+

+========================================================================+
|                             DATA DOWNLOAD                              |
+========================================================================+
|  Universe: both  |  Alpaca primary / yfinance fallback                 |
+========================================================================+

+========================================================================+
|                              SIGNAL SCAN                               |
+========================================================================+
|  Month: Oct  |  Regime: BULL                                           |
|  Primary: RubberBand  |  Secondary: GapDown (display only — schedule n~|
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  24                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  ALL      Pullback50      eq     $246.31  78.3   -1.85   50MA bounce (-|
|  AMZN     Pullback50      eq     $256.43  59.8   -3.47   50MA bounce (-|
|  BAX      Pullback50      eq     $25.14   66.5   -2.45   50MA bounce (+|
|  LH       Pullback50      eq     $317.83  61.3   -1.88   50MA bounce (-|
|  MRK      Pullback50      eq     $146.54  45.5   -3.15   50MA bounce (+|
|  NWS      Pullback50      eq     $32.82   68.5   -2.86   50MA bounce (-|
|  PYPL     Pullback50      eq     $56.57   68.5   -1.83   50MA bounce (+|
|  QCOM     Pullback50      eq     $176.06  39.5   -2.57   50MA bounce (+|
|  TWLO     Pullback50      eq     $251.66  34.3   -0.59   50MA bounce (-|
|  WDAY     Pullback50      eq     $191.57  53.1   -2.70   50MA bounce (-|
|  WELL     Pullback50      eq     $234.59  52.7   -2.99   50MA bounce (+|
|  ZBH      Pullback50      eq     $94.67   59.5   -3.16   50MA bounce (-|
|  APPF     Pullback50      eq     $211.99  65.3   -2.38   50MA bounce (+|
|  CCK      Pullback50      eq     $113.84  79.5   -2.70   50MA bounce (+|
|  CNO      Pullback50      eq     $54.70   63.0   -2.03   50MA bounce (+|
|  LAMR     Pullback50      eq     $149.56  61.3   -2.80   50MA bounce (+|
|  LNTH     Pullback50      eq     $99.97   61.7   -2.10   50MA bounce (-|
|  PAG      Pullback50      eq     $212.43  62.8   -0.91   50MA bounce (+|
|  RYAN     Pullback50      eq     $40.34   63.2   -2.41   50MA bounce (+|
|  SCI      Pullback50      eq     $81.05   71.8   -2.70   50MA bounce (+|
|  SLAB     Pullback50      eq     $221.31  51.6   -2.10   50MA bounce (+|
|  SIGI     Pullback50      eq     $88.91   67.5   -2.70   50MA bounce (-|
|  TXNM     Pullback50      eq     $58.59   53.6   -1.99   50MA bounce (+|
|  UNM      Pullback50      eq     $92.65   70.1   -2.73   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] ALL  Pullback50                                    $33.72|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] AMZN  Pullback50                                   $33.72|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] BAX  Pullback50                                    $33.72|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] LH  Pullback50                                       cap 3|
|    SKIP [eq] MRK  Pullback50                                      cap 3|
|    SKIP [eq] NWS  Pullback50                                      cap 3|
|    SKIP [eq] PYPL  Pullback50                                     cap 3|
|    SKIP [eq] QCOM  Pullback50                                     cap 3|
|    SKIP [eq] TWLO  Pullback50                                     cap 3|
|    SKIP [eq] WDAY  Pullback50                                     cap 3|
|    SKIP [eq] WELL  Pullback50                                     cap 3|
|    SKIP [eq] ZBH  Pullback50                                      cap 3|
|    SKIP [eq] APPF  Pullback50                                     cap 3|
|    SKIP [eq] CCK  Pullback50                                      cap 3|
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261019T140310Z

- UTC timestamp: `20261019T140310Z`
- GitHub run: [#13149](https://github.com/28twagg-ops/TradingBot/actions/runs/39265004465)
- Run id: `39265004465`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`46s`
- Full logs: `logs/action_runs/20261019T140310Z_live_bot.log`, `logs/action_runs/20261019T140310Z_live_options.log`, `logs/action_runs/20261019T140310Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1698 | 48.1 | -28.6 | +36.8 | $+18,373 |
| TAINTED | 2008 | 32.3 | -40.6 | +10.7 | $-11,098 |
| KEEP-only | 837 | 60.3 | +50.7 | +54.1 | $+12,586 |
| KEEP-only recent | 644 | 58.7 | +52.9 | +59.7 | $+8,525 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-19T10:03:16.470610-04:00","date":"2026-10-19","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":37.3,"phases_s":{"reconcile":0.28,"cancel":0.1,"manage":0.09,"protective_stops":0.05,"scan":35.61,"entries":0.65},"signals":58,"placed":0,"equity":992672.01,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S430:TSLA","S432:TSLA","S430:PLTR","S432:PLTR","S430:AMZN","S432:AMZN","S430:SNOW","S432:SNOW"],"github_run":"13149","github_run_id":"39265004465","status":"ok","data_quality":{"clean":{"n":1698,"win":48.12,"med":-28.57,"avg":36.81,"pnl":18372.83},"tainted":{"n":2008,"win":32.27,"med":-40.61,"avg":10.66,"pnl":-11098.28},"keep_only":{"n":837,"win":60.33,"med":50.7,"avg":54.07,"pnl":12586.45},"keep_only_recent":{"n":644,"win":58.7,"med":52.94,"avg":59.7,"pnl":8525.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:03:12  INFO      Mode: exits
14:03:12  INFO        Daily log -> logs/daily/2026-10-19.md
14:03:12  INFO        Daily log reconciled -> logs/daily/2026-10-19.md (3 ledger rows)
14:03:12  INFO        place_all_stops: checking 3 positions...
14:03:12  INFO        STOP skipped ALL: fractional (0.1368 shares) — software exit will handle it
14:03:12  INFO        STOP skipped AMZN: fractional (0.1313 shares) — software exit will handle it
14:03:12  INFO        STOP already live BAX @ $24.94
14:03:13  INFO        [positions] 3/3 (3 valid)
14:03:13  INFO        Daily log -> logs/daily/2026-10-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:03 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.82|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALL  P&L -0.0%  $-0.00                                            HOLD|
|  AMZN  P&L +0.0%  $+0.01                                           HOLD|
|  BAX  P&L +0.0%  $+0.01                                            HOLD|
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
=== options_live_micro LIVE 2026-10-19T10:03:13.947166-04:00 share=25% ===
2026-10-19 10:03:13,947 INFO === options_live_micro LIVE 2026-10-19T10:03:13.947166-04:00 share=25% ===
Live account equity $224.82 cash $123.67 #225458845 options_level=3
2026-10-19 10:03:14,085 INFO Live account equity $224.82 cash $123.67 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-19 10:03:14,204 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-19 10:03:14,283 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (186 earlier lines - see full log file)
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
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1914 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |  2817 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1698 med=-28.6% | TAINTED n=2008 med=-40.6% | KEEP-only n=837 med=+50.7% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.82 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261019T140649Z

- UTC timestamp: `20261019T140649Z`
- GitHub run: [#13150](https://github.com/28twagg-ops/TradingBot/actions/runs/39265743387)
- Run id: `39265743387`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`77s`
- Full logs: `logs/action_runs/20261019T140649Z_live_bot.log`, `logs/action_runs/20261019T140649Z_live_options.log`, `logs/action_runs/20261019T140649Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1698 | 48.1 | -28.6 | +36.8 | $+18,373 |
| TAINTED | 2008 | 32.3 | -40.6 | +10.7 | $-11,098 |
| KEEP-only | 837 | 60.3 | +50.7 | +54.1 | $+12,586 |
| KEEP-only recent | 644 | 58.7 | +52.9 | +59.7 | $+8,525 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-19T10:06:56.413997-04:00","date":"2026-10-19","mode":"entry+manage","header":"entry+manage (3 new)","elapsed_s":63.8,"phases_s":{"reconcile":0.44,"cancel":0.14,"manage":0.14,"protective_stops":0.07,"scan":55.32,"entries":6.31,"reconcile2":0.44},"signals":58,"placed":3,"equity":992809.85,"open_positions":1,"pending_orders":2,"open_lots":1,"submitted_today":3,"filled_today":1,"unattributed_contracts":0,"top_signals":["S430:TSLA","S432:TSLA","S430:PLTR","S432:PLTR","S430:AMZN","S432:AMZN","S430:SNOW","S432:SNOW"],"github_run":"13150","github_run_id":"39265743387","status":"ok","data_quality":{"clean":{"n":1698,"win":48.12,"med":-28.57,"avg":36.81,"pnl":18372.83},"tainted":{"n":2008,"win":32.27,"med":-40.61,"avg":10.66,"pnl":-11098.28},"keep_only":{"n":837,"win":60.33,"med":50.7,"avg":54.07,"pnl":12586.45},"keep_only_recent":{"n":644,"win":58.7,"med":52.94,"avg":59.7,"pnl":8525.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:06:50  INFO      Mode: exits
14:06:51  INFO        Daily log -> logs/daily/2026-10-19.md
14:06:51  INFO        Daily log reconciled -> logs/daily/2026-10-19.md (3 ledger rows)
14:06:51  INFO        place_all_stops: checking 3 positions...
14:06:51  INFO        STOP skipped ALL: fractional (0.1368 shares) — software exit will handle it
14:06:51  INFO        STOP skipped AMZN: fractional (0.1313 shares) — software exit will handle it
14:06:51  INFO        STOP already live BAX @ $24.94
14:06:51  INFO        [positions] 3/3 (3 valid)
14:06:52  INFO        Daily log -> logs/daily/2026-10-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.85|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALL  P&L -0.2%  $-0.06                                            HOLD|
|  AMZN  P&L +0.0%  $+0.01                                           HOLD|
|  BAX  P&L +0.3%  $+0.10                                            HOLD|
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
=== options_live_micro LIVE 2026-10-19T10:06:52.877416-04:00 share=25% ===
2026-10-19 10:06:52,877 INFO === options_live_micro LIVE 2026-10-19T10:06:52.877416-04:00 share=25% ===
Live account equity $224.86 cash $123.67 #225458845 options_level=3
2026-10-19 10:06:53,103 INFO Live account equity $224.86 cash $123.67 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-19 10:06:53,309 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-19 10:06:53,450 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (192 earlier lines - see full log file)
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
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1914 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  2817 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1698 med=-28.6% | TAINTED n=2008 med=-40.6% | KEEP-only n=837 med=+50.7% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.86 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261019T141131Z

- UTC timestamp: `20261019T141131Z`
- GitHub run: [#13151](https://github.com/28twagg-ops/TradingBot/actions/runs/39266494477)
- Run id: `39266494477`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`71s`
- Full logs: `logs/action_runs/20261019T141131Z_live_bot.log`, `logs/action_runs/20261019T141131Z_live_options.log`, `logs/action_runs/20261019T141131Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1698 | 48.1 | -28.6 | +36.8 | $+18,373 |
| TAINTED | 2008 | 32.3 | -40.6 | +10.7 | $-11,098 |
| KEEP-only | 837 | 60.3 | +50.7 | +54.1 | $+12,586 |
| KEEP-only recent | 644 | 58.7 | +52.9 | +59.7 | $+8,525 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-19T10:11:38.678152-04:00","date":"2026-10-19","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":58.7,"phases_s":{"reconcile":0.09,"cancel":0.03,"manage":0.28,"protective_stops":0.02,"scan":56.68,"entries":0.91,"reconcile2":0.09},"signals":58,"placed":0,"equity":992776.63,"open_positions":1,"pending_orders":2,"open_lots":1,"submitted_today":3,"filled_today":1,"unattributed_contracts":0,"top_signals":["S430:TSLA","S432:TSLA","S430:PLTR","S432:PLTR","S430:AMZN","S432:AMZN","S430:SNOW","S432:SNOW"],"github_run":"13151","github_run_id":"39266494477","status":"ok","data_quality":{"clean":{"n":1698,"win":48.12,"med":-28.57,"avg":36.81,"pnl":18372.83},"tainted":{"n":2008,"win":32.27,"med":-40.61,"avg":10.66,"pnl":-11098.28},"keep_only":{"n":837,"win":60.33,"med":50.7,"avg":54.07,"pnl":12586.45},"keep_only_recent":{"n":644,"win":58.7,"med":52.94,"avg":59.7,"pnl":8525.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:11:32  INFO      Mode: exits
14:11:32  INFO        Daily log -> logs/daily/2026-10-19.md
14:11:32  INFO        Daily log reconciled -> logs/daily/2026-10-19.md (3 ledger rows)
14:11:32  INFO        place_all_stops: checking 3 positions...
14:11:32  INFO        STOP skipped ALL: fractional (0.1368 shares) — software exit will handle it
14:11:32  INFO        STOP skipped AMZN: fractional (0.1313 shares) — software exit will handle it
14:11:32  INFO        STOP already live BAX @ $24.94
14:11:33  INFO        [positions] 3/3 (3 valid)
14:11:33  INFO        SELL MARKET [urgent] ALL closed
14:11:35  INFO        TX logged: SELL ALL  P&L -0.51%
14:11:35  INFO        Daily log -> logs/daily/2026-10-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.98|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALL  P&L -0.5%  $-0.17                         EXIT: stop_loss (-0.5%)|
|  BAX  P&L +0.4%  $+0.13                                            HOLD|
|  AMZN  P&L +0.7%  $+0.22                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  1 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
|  ALL                                         -0.51%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-19T10:11:36.062417-04:00 share=25% ===
2026-10-19 10:11:36,062 INFO === options_live_micro LIVE 2026-10-19T10:11:36.062417-04:00 share=25% ===
Live account equity $224.98 cash $157.21 #225458845 options_level=3
2026-10-19 10:11:36,104 INFO Live account equity $224.98 cash $157.21 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-19 10:11:36,143 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-19 10:11:36,162 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (195 earlier lines - see full log file)
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
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1914 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  2817 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1698 med=-28.6% | TAINTED n=2008 med=-40.6% | KEEP-only n=837 med=+50.7% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.99 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261019T141652Z

- UTC timestamp: `20261019T141652Z`
- GitHub run: [#13152](https://github.com/28twagg-ops/TradingBot/actions/runs/39267243324)
- Run id: `39267243324`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`55s`
- Full logs: `logs/action_runs/20261019T141652Z_live_bot.log`, `logs/action_runs/20261019T141652Z_live_options.log`, `logs/action_runs/20261019T141652Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1698 | 48.1 | -28.6 | +36.8 | $+18,373 |
| TAINTED | 2008 | 32.3 | -40.6 | +10.7 | $-11,098 |
| KEEP-only | 837 | 60.3 | +50.7 | +54.1 | $+12,586 |
| KEEP-only recent | 644 | 58.7 | +52.9 | +59.7 | $+8,525 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-19T10:16:57.865732-04:00","date":"2026-10-19","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":43.9,"phases_s":{"reconcile":0.09,"cancel":0.03,"manage":0.5,"protective_stops":0.05,"scan":41.57,"entries":1.04,"reconcile2":0.1},"signals":58,"placed":0,"equity":992662.29,"open_positions":2,"pending_orders":1,"open_lots":2,"submitted_today":3,"filled_today":2,"unattributed_contracts":0,"top_signals":["S430:TSLA","S432:TSLA","S430:PLTR","S432:PLTR","S430:AMZN","S432:AMZN","S430:SNOW","S432:SNOW"],"github_run":"13152","github_run_id":"39267243324","status":"ok","data_quality":{"clean":{"n":1698,"win":48.12,"med":-28.57,"avg":36.81,"pnl":18372.83},"tainted":{"n":2008,"win":32.27,"med":-40.61,"avg":10.66,"pnl":-11098.28},"keep_only":{"n":837,"win":60.33,"med":50.7,"avg":54.07,"pnl":12586.45},"keep_only_recent":{"n":644,"win":58.7,"med":52.94,"avg":59.7,"pnl":8525.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:16:54  INFO      Mode: exits
14:16:54  INFO        Daily log -> logs/daily/2026-10-19.md
14:16:54  INFO        Daily log reconciled -> logs/daily/2026-10-19.md (4 ledger rows)
14:16:54  INFO        place_all_stops: checking 2 positions...
14:16:54  INFO        STOP skipped AMZN: fractional (0.1313 shares) — software exit will handle it
14:16:54  INFO        STOP already live BAX @ $24.94
14:16:54  INFO        [positions] 2/2 (2 valid)
14:16:54  INFO        Daily log -> logs/daily/2026-10-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.14|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  BAX  P&L +0.6%  $+0.20                                            HOLD|
|  AMZN  P&L +0.9%  $+0.31                                           HOLD|
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
=== options_live_micro LIVE 2026-10-19T10:16:55.379588-04:00 share=25% ===
2026-10-19 10:16:55,379 INFO === options_live_micro LIVE 2026-10-19T10:16:55.379588-04:00 share=25% ===
Live account equity $225.14 cash $157.21 #225458845 options_level=3
2026-10-19 10:16:55,428 INFO Live account equity $225.14 cash $157.21 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-19 10:16:55,451 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-19 10:16:55,464 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (196 earlier lines - see full log file)
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
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-19
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1914 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     2 | INFO |
| Total closed lots           |  2817 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-19_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-19_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1698 med=-28.6% | TAINTED n=2008 med=-40.6% | KEEP-only n=837 med=+50.7% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.14 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
