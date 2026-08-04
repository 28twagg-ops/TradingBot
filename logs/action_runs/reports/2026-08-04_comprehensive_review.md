# Daily Comprehensive Action Review — 2026-08-04

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260804T011115Z

- UTC timestamp: `20260804T011115Z`
- GitHub run: [#5958](https://github.com/28twagg-ops/TradingBot/actions/runs/30867937854)
- Run id: `30867937854`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T21:11:20.271546-04:00","date":"2026-08-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.4,"phases_s":{"reconcile":0.1},"signals":0,"placed":0,"equity":134703.67,"open_positions":20,"pending_orders":0,"open_lots":105,"submitted_today":192,"filled_today":161,"unattributed_contracts":1,"top_signals":[],"github_run":"5958","github_run_id":"30867937854","status":"ok"}
```

### Live bot full output

```text
01:11:16  INFO      Mode: summary
01:11:17  INFO        Daily log -> logs/daily/2026-08-04.md
01:11:17  INFO        Daily log reconciled -> logs/daily/2026-08-04.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         01:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.88|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $467.88|
|  Cash                                                           $210.17|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $257.71|
|  Open P&L                                                        $+1.25|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.73     $14.70   $14.71   +0.1%   $+0.09  |
|  AVB      Pullback50      $94.41     $187.24  $188.78  +0.8%   $+0.77  |
|  ECHO     MomReversal     $69.57     $85.51   $85.99   +0.6%   $+0.39  |
|                                                                        |
|  Total invested                                                 $257.71|
|  Total open P&L                                                  $+1.25|
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
|  2026-08-03  SELL  TSN  EarningsDrift  $93.73  P&L $+0.23              |
|  2026-08-03  SELL  FSLR  EarningsDrift  $93.03  P&L $-0.50             |
|  2026-08-03  SELL  ED  Pullback50  $69.86  P&L $-0.37                  |
|  2026-08-03  SELL  CPT  Pullback50  $93.14  P&L $-0.50                 |
|  2026-08-03  SELL  ALGN  Pullback50  $93.13  P&L $-0.51                |
|  2026-08-03  SELL  CINF  Pullback50  $95.73  P&L $+1.79                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=123 paper_keys=yes dry_run=False
  alpaca positions=22
  FLAG b23|S202|17807b63 missing from Alpaca
  FLAG b22|S202|80ba265b missing from Alpaca
  FLAG b303|S353|b7591acb missing from Alpaca
  FLAG b302|S353|0ef361fc missing from Alpaca
  FLAG b285|S351|8ff9fa2d missing from Alpaca
  FLAG b284|S351|312ff617 missing from Alpaca
  FLAG b299|S353|75bb1a96 missing from Alpaca
  FLAG b298|S353|1a6ef9f6 missing from Alpaca
  FLAG b291|S352|c39410bb missing from Alpaca
  FLAG b290|S352|bae3b16d missing from Alpaca
  FLAG b19|S202|2982e0e8 missing from Alpaca
  FLAG b18|S202|1fec4967 missing from Alpaca
  FLAG b297|S353|3d05ce37 missing from Alpaca
  FLAG b296|S353|90cfdfe0 missing from Alpaca
  FLAG b289|S352|8f807d06 missing from Alpaca
  FLAG b288|S352|c92766f6 missing from Alpaca
  FLAG b17|S202|77ac718e missing from Alpaca
  FLAG b16|S202|a053d354 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-03T21:11:20.271546-04:00 ===

[Run context]
After hours (21:11 ET) — exit summary only.
Paper auth OK — equity $134703.67, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $134,703.67                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    192                                     |
|  Orders filled today (ledger)  161                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             105                                     |
|  Broker option positions       20                                      |
|  Unattributed contracts        1 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=456  buckets=188  win=47%                            |
|  Returns   avg=+27.0%  med=-7.7%  p10=-64.9%  p90=+142.5%              |
|  Realized  $+9,411.13                                                  |
|  Raw incl dropped  trades=990  real=$+7,815.58                         |
|  Today     trades=88  avg=+85.7%  med=+55.9%  real=$+1,860.00          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  1 100% +906.2 +906.2 +906.2 $   +145         |
|  b197 lab0197_s218_w3_10  1 100% +737.5 +737.5 +737.5 $   +118         |
|  b181 lab0181_s217_w2_10  2 100% +538.4 +538.4 +1007.1 $   +173        |
|  b180 lab0180_s217_w2_10  2 100% +469.8 +469.8 +885.7 $   +152         |
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 180 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  1   0% -95.9 -95.9 -95.9 $    -47       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b863 S408 NVDA260805C00222500 x1 stop_loss (-53.3%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (20)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  OXY260807C00058000           23    -25.5%   $   -402.00               |
|  NVDA260805C00217500          18    -22.5%   $   -115.00               |
|  AAPL260814C00330000           6    -29.7%   $   -106.50               |
|  OXY260807C00059000            4    -30.5%   $    -58.00               |
|  T260807C00023000              6    +11.1%   $    +42.00               |
|  AAPL260821C00335000           4    -14.1%   $    -36.00               |
|  NVDA260810C00225000           4    -24.6%   $    -34.00               |
|  DKNG260807C00025500           4    -17.6%   $    -30.00               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-03.log
elapsed=0.4s reconcile=0.1s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.4s. run=#5958 https://github.com/28twagg-ops/TradingBot/actions/runs/30867937854
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.csv
Summary: 79 buckets closed trades, $+1,860.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.6% (26/990)
# Options signal frequency

_Generated 2026-08-03T21:11:26.159036_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-03
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   327 | WARN | <<<
| Missing exit records (post) |   327 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   105 | INFO |
| Total closed lots           |   497 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=467.88 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260804T014344Z

- UTC timestamp: `20260804T014344Z`
- GitHub run: [#5959](https://github.com/28twagg-ops/TradingBot/actions/runs/30869597965)
- Run id: `30869597965`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T21:43:48.282878-04:00","date":"2026-08-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.53},"signals":0,"placed":0,"equity":135335.67,"open_positions":20,"pending_orders":0,"open_lots":105,"submitted_today":192,"filled_today":161,"unattributed_contracts":1,"top_signals":[],"github_run":"5959","github_run_id":"30869597965","status":"ok"}
```

### Live bot full output

```text
01:43:45  INFO      Mode: summary
01:43:46  INFO        Daily log -> logs/daily/2026-08-04.md
01:43:46  INFO        Daily log reconciled -> logs/daily/2026-08-04.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         01:43 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.88|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $467.88|
|  Cash                                                           $210.17|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $257.71|
|  Open P&L                                                        $+1.25|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.73     $14.70   $14.71   +0.1%   $+0.09  |
|  AVB      Pullback50      $94.41     $187.24  $188.78  +0.8%   $+0.77  |
|  ECHO     MomReversal     $69.57     $85.51   $85.99   +0.6%   $+0.39  |
|                                                                        |
|  Total invested                                                 $257.71|
|  Total open P&L                                                  $+1.25|
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
|  2026-08-03  SELL  TSN  EarningsDrift  $93.73  P&L $+0.23              |
|  2026-08-03  SELL  FSLR  EarningsDrift  $93.03  P&L $-0.50             |
|  2026-08-03  SELL  ED  Pullback50  $69.86  P&L $-0.37                  |
|  2026-08-03  SELL  CPT  Pullback50  $93.14  P&L $-0.50                 |
|  2026-08-03  SELL  ALGN  Pullback50  $93.13  P&L $-0.51                |
|  2026-08-03  SELL  CINF  Pullback50  $95.73  P&L $+1.79                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=105 paper_keys=yes dry_run=False
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-03T21:43:48.282878-04:00 ===

[Run context]
After hours (21:43 ET) — exit summary only.
Paper auth OK — equity $135335.67, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $135,335.67                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    192                                     |
|  Orders filled today (ledger)  161                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             105                                     |
|  Broker option positions       20                                      |
|  Unattributed contracts        1 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=456  buckets=188  win=47%                            |
|  Returns   avg=+27.0%  med=-7.7%  p10=-64.9%  p90=+142.5%              |
|  Realized  $+9,411.13                                                  |
|  Raw incl dropped  trades=990  real=$+7,815.58                         |
|  Today     trades=88  avg=+85.7%  med=+55.9%  real=$+1,860.00          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  1 100% +906.2 +906.2 +906.2 $   +145         |
|  b197 lab0197_s218_w3_10  1 100% +737.5 +737.5 +737.5 $   +118         |
|  b181 lab0181_s217_w2_10  2 100% +538.4 +538.4 +1007.1 $   +173        |
|  b180 lab0180_s217_w2_10  2 100% +469.8 +469.8 +885.7 $   +152         |
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 180 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  1   0% -95.9 -95.9 -95.9 $    -47       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b863 S408 NVDA260805C00222500 x1 stop_loss (-53.3%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (20)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  OXY260807C00058000           23    -25.5%   $   -402.00               |
|  NVDA260805C00217500          18    -22.5%   $   -115.00               |
|  AAPL260814C00330000           6    -29.7%   $   -106.50               |
|  OXY260807C00059000            4    -30.5%   $    -58.00               |
|  T260807C00023000              6    +11.1%   $    +42.00               |
|  AAPL260821C00335000           4    -14.1%   $    -36.00               |
|  NVDA260810C00225000           4    -24.6%   $    -34.00               |
|  DKNG260807C00025500           4    -17.6%   $    -30.00               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-03.log
elapsed=1.0s reconcile=0.53s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.0s. run=#5959 https://github.com/28twagg-ops/TradingBot/actions/runs/30869597965
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.csv
Summary: 79 buckets closed trades, $+1,860.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.6% (26/990)
# Options signal frequency

_Generated 2026-08-03T21:43:54.774394_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-03
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   327 | WARN | <<<
| Missing exit records (post) |   327 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   105 | INFO |
| Total closed lots           |   497 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=467.88 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260804T044855Z

- UTC timestamp: `20260804T044855Z`
- GitHub run: [#5960](https://github.com/28twagg-ops/TradingBot/actions/runs/30878739132)
- Run id: `30878739132`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-04T00:48:58.935159-04:00","date":"2026-08-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.56},"signals":0,"placed":0,"equity":136039.67,"open_positions":20,"pending_orders":0,"open_lots":105,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"5960","github_run_id":"30878739132","status":"ok"}
```

### Live bot full output

```text
04:48:55  INFO      Mode: summary
04:48:56  INFO        Daily log -> logs/daily/2026-08-04.md
04:48:56  INFO        Daily log reconciled -> logs/daily/2026-08-04.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         04:48 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $468.33|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $468.33|
|  Cash                                                           $210.17|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $258.16|
|  Open P&L                                                        $+1.70|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.73     $14.70   $14.71   +0.1%   $+0.09  |
|  AVB      Pullback50      $94.41     $187.24  $188.78  +0.8%   $+0.77  |
|  ECHO     MomReversal     $70.02     $85.51   $86.55   +1.2%   $+0.84  |
|                                                                        |
|  Total invested                                                 $258.16|
|  Total open P&L                                                  $+1.70|
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
|  2026-08-03  SELL  TSN  EarningsDrift  $93.73  P&L $+0.23              |
|  2026-08-03  SELL  FSLR  EarningsDrift  $93.03  P&L $-0.50             |
|  2026-08-03  SELL  ED  Pullback50  $69.86  P&L $-0.37                  |
|  2026-08-03  SELL  CPT  Pullback50  $93.14  P&L $-0.50                 |
|  2026-08-03  SELL  ALGN  Pullback50  $93.13  P&L $-0.51                |
|  2026-08-03  SELL  CINF  Pullback50  $95.73  P&L $+1.79                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=105 paper_keys=yes dry_run=False
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-04T00:48:58.935159-04:00 ===

[Run context]
After hours (00:48 ET) — exit summary only.
Paper auth OK — equity $136039.67, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $136,039.67                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             105                                     |
|  Broker option positions       20                                      |
|  Unattributed contracts        1 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=456  buckets=188  win=47%                            |
|  Returns   avg=+27.0%  med=-7.7%  p10=-64.9%  p90=+142.5%              |
|  Realized  $+9,411.13                                                  |
|  Raw incl dropped  trades=990  real=$+7,815.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  1 100% +906.2 +906.2 +906.2 $   +145         |
|  b197 lab0197_s218_w3_10  1 100% +737.5 +737.5 +737.5 $   +118         |
|  b181 lab0181_s217_w2_10  2 100% +538.4 +538.4 +1007.1 $   +173        |
|  b180 lab0180_s217_w2_10  2 100% +469.8 +469.8 +885.7 $   +152         |
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 180 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  1   0% -95.9 -95.9 -95.9 $    -47       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b863 S408 NVDA260805C00222500 x1 stop_loss (-53.3%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (20)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  OXY260807C00058000           23    -25.5%   $   -402.00               |
|  NVDA260805C00217500          18    -22.5%   $   -115.00               |
|  AAPL260814C00330000           6    -29.7%   $   -106.50               |
|  OXY260807C00059000            4    -30.5%   $    -58.00               |
|  T260807C00023000              6    +11.1%   $    +42.00               |
|  AAPL260821C00335000           4    -14.1%   $    -36.00               |
|  NVDA260810C00225000           4    -24.6%   $    -34.00               |
|  DKNG260807C00025500           4    -17.6%   $    -30.00               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-04.log
elapsed=1.4s reconcile=0.56s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.4s. run=#5960 https://github.com/28twagg-ops/TradingBot/actions/runs/30878739132
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.6% (26/990)
# Options signal frequency

_Generated 2026-08-04T00:49:05.007350_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-04
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN | <<<
| Missing exit records (post) |   398 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   105 | INFO |
| Total closed lots           |   497 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=468.33 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260804T130054Z

- UTC timestamp: `20260804T130054Z`
- GitHub run: [#5961](https://github.com/28twagg-ops/TradingBot/actions/runs/30911666840)
- Run id: `30911666840`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-04T09:00:59.722535-04:00","date":"2026-08-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.63},"signals":0,"placed":0,"equity":139924.97,"open_positions":20,"pending_orders":0,"open_lots":105,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"5961","github_run_id":"30911666840","status":"ok"}
```

### Live bot full output

```text
13:00:56  INFO      Mode: summary
13:00:57  INFO        Daily log -> logs/daily/2026-08-04.md
13:00:57  INFO        Daily log reconciled -> logs/daily/2026-08-04.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $469.26|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $469.26|
|  Cash                                                           $210.17|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $259.09|
|  Open P&L                                                        $+2.63|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.73     $14.70   $14.71   +0.1%   $+0.09  |
|  AVB      Pullback50      $94.41     $187.24  $188.78  +0.8%   $+0.77  |
|  ECHO     MomReversal     $70.96     $85.51   $87.70   +2.6%   $+1.78  |
|                                                                        |
|  Total invested                                                 $259.09|
|  Total open P&L                                                  $+2.63|
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
|  2026-08-03  SELL  TSN  EarningsDrift  $93.73  P&L $+0.23              |
|  2026-08-03  SELL  FSLR  EarningsDrift  $93.03  P&L $-0.50             |
|  2026-08-03  SELL  ED  Pullback50  $69.86  P&L $-0.37                  |
|  2026-08-03  SELL  CPT  Pullback50  $93.14  P&L $-0.50                 |
|  2026-08-03  SELL  ALGN  Pullback50  $93.13  P&L $-0.51                |
|  2026-08-03  SELL  CINF  Pullback50  $95.73  P&L $+1.79                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=105 paper_keys=yes dry_run=False
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-04T09:00:59.722535-04:00 ===

[Run context]
After hours (09:00 ET) — exit summary only.
Paper auth OK — equity $139924.97, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $139,924.97                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             105                                     |
|  Broker option positions       20                                      |
|  Unattributed contracts        1 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=456  buckets=188  win=47%                            |
|  Returns   avg=+27.0%  med=-7.7%  p10=-64.9%  p90=+142.5%              |
|  Realized  $+9,411.13                                                  |
|  Raw incl dropped  trades=990  real=$+7,815.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  1 100% +906.2 +906.2 +906.2 $   +145         |
|  b197 lab0197_s218_w3_10  1 100% +737.5 +737.5 +737.5 $   +118         |
|  b181 lab0181_s217_w2_10  2 100% +538.4 +538.4 +1007.1 $   +173        |
|  b180 lab0180_s217_w2_10  2 100% +469.8 +469.8 +885.7 $   +152         |
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 180 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  1   0% -95.9 -95.9 -95.9 $    -47       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b863 S408 NVDA260805C00222500 x1 stop_loss (-53.3%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (20)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  OXY260807C00058000           23    -25.5%   $   -402.00               |
|  NVDA260805C00217500          18    -22.5%   $   -115.00               |
|  AAPL260814C00330000           6    -29.7%   $   -106.50               |
|  OXY260807C00059000            4    -30.5%   $    -58.00               |
|  T260807C00023000              6    +11.1%   $    +42.00               |
|  AAPL260821C00335000           4    -14.1%   $    -36.00               |
|  NVDA260810C00225000           4    -24.6%   $    -34.00               |
|  DKNG260807C00025500           4    -17.6%   $    -30.00               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-04.log
elapsed=1.2s reconcile=0.63s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.2s. run=#5961 https://github.com/28twagg-ops/TradingBot/actions/runs/30911666840
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.6% (26/990)
# Options signal frequency

_Generated 2026-08-04T09:01:06.751593_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-04
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN | <<<
| Missing exit records (post) |   398 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   105 | INFO |
| Total closed lots           |   497 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=469.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260804T130549Z

- UTC timestamp: `20260804T130549Z`
- GitHub run: [#5962](https://github.com/28twagg-ops/TradingBot/actions/runs/30912076735)
- Run id: `30912076735`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-04T09:05:54.351117-04:00","date":"2026-08-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":139962.53,"open_positions":20,"pending_orders":0,"open_lots":105,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"5962","github_run_id":"30912076735","status":"ok"}
```

### Live bot full output

```text
13:05:50  INFO      Mode: summary
13:05:52  INFO        Daily log -> logs/daily/2026-08-04.md
13:05:52  INFO        Daily log reconciled -> logs/daily/2026-08-04.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $469.30|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $469.30|
|  Cash                                                           $210.17|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $259.13|
|  Open P&L                                                        $+2.67|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.73     $14.70   $14.71   +0.1%   $+0.09  |
|  AVB      Pullback50      $94.41     $187.24  $188.78  +0.8%   $+0.77  |
|  ECHO     MomReversal     $71.00     $85.51   $87.75   +2.6%   $+1.82  |
|                                                                        |
|  Total invested                                                 $259.13|
|  Total open P&L                                                  $+2.67|
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
|  2026-08-03  SELL  TSN  EarningsDrift  $93.73  P&L $+0.23              |
|  2026-08-03  SELL  FSLR  EarningsDrift  $93.03  P&L $-0.50             |
|  2026-08-03  SELL  ED  Pullback50  $69.86  P&L $-0.37                  |
|  2026-08-03  SELL  CPT  Pullback50  $93.14  P&L $-0.50                 |
|  2026-08-03  SELL  ALGN  Pullback50  $93.13  P&L $-0.51                |
|  2026-08-03  SELL  CINF  Pullback50  $95.73  P&L $+1.79                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=105 paper_keys=yes dry_run=False
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-04T09:05:54.351117-04:00 ===

[Run context]
After hours (09:05 ET) — exit summary only.
Paper auth OK — equity $139962.53, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $139,962.53                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             105                                     |
|  Broker option positions       20                                      |
|  Unattributed contracts        1 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=456  buckets=188  win=47%                            |
|  Returns   avg=+27.0%  med=-7.7%  p10=-64.9%  p90=+142.5%              |
|  Realized  $+9,411.13                                                  |
|  Raw incl dropped  trades=990  real=$+7,815.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  1 100% +906.2 +906.2 +906.2 $   +145         |
|  b197 lab0197_s218_w3_10  1 100% +737.5 +737.5 +737.5 $   +118         |
|  b181 lab0181_s217_w2_10  2 100% +538.4 +538.4 +1007.1 $   +173        |
|  b180 lab0180_s217_w2_10  2 100% +469.8 +469.8 +885.7 $   +152         |
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 180 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  1   0% -95.9 -95.9 -95.9 $    -47       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b863 S408 NVDA260805C00222500 x1 stop_loss (-53.3%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (20)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  OXY260807C00058000           23    -25.5%   $   -402.00               |
|  NVDA260805C00217500          18    -22.5%   $   -115.00               |
|  AAPL260814C00330000           6    -29.7%   $   -106.50               |
|  OXY260807C00059000            4    -30.5%   $    -58.00               |
|  T260807C00023000              6    +11.1%   $    +42.00               |
|  AAPL260821C00335000           4    -14.1%   $    -36.00               |
|  NVDA260810C00225000           4    -24.6%   $    -34.00               |
|  DKNG260807C00025500           4    -17.6%   $    -30.00               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-04.log
elapsed=1.1s reconcile=0.6s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.1s. run=#5962 https://github.com/28twagg-ops/TradingBot/actions/runs/30912076735
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.6% (26/990)
# Options signal frequency

_Generated 2026-08-04T09:06:01.016546_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-04
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN | <<<
| Missing exit records (post) |   398 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   105 | INFO |
| Total closed lots           |   497 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=469.3 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260804T131042Z

- UTC timestamp: `20260804T131042Z`
- GitHub run: [#5963](https://github.com/28twagg-ops/TradingBot/actions/runs/30912480962)
- Run id: `30912480962`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-04T09:10:46.630035-04:00","date":"2026-08-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.5},"signals":0,"placed":0,"equity":140061.81,"open_positions":20,"pending_orders":0,"open_lots":105,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"5963","github_run_id":"30912480962","status":"ok"}
```

### Live bot full output

```text
13:10:43  INFO      Mode: summary
13:10:44  INFO        Daily log -> logs/daily/2026-08-04.md
13:10:44  INFO        Daily log reconciled -> logs/daily/2026-08-04.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $469.26|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $469.26|
|  Cash                                                           $210.17|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $259.09|
|  Open P&L                                                        $+2.63|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.73     $14.70   $14.71   +0.1%   $+0.09  |
|  AVB      Pullback50      $94.41     $187.24  $188.78  +0.8%   $+0.77  |
|  ECHO     MomReversal     $70.95     $85.51   $87.70   +2.6%   $+1.77  |
|                                                                        |
|  Total invested                                                 $259.09|
|  Total open P&L                                                  $+2.63|
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
|  2026-08-03  SELL  TSN  EarningsDrift  $93.73  P&L $+0.23              |
|  2026-08-03  SELL  FSLR  EarningsDrift  $93.03  P&L $-0.50             |
|  2026-08-03  SELL  ED  Pullback50  $69.86  P&L $-0.37                  |
|  2026-08-03  SELL  CPT  Pullback50  $93.14  P&L $-0.50                 |
|  2026-08-03  SELL  ALGN  Pullback50  $93.13  P&L $-0.51                |
|  2026-08-03  SELL  CINF  Pullback50  $95.73  P&L $+1.79                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=105 paper_keys=yes dry_run=False
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-04T09:10:46.630035-04:00 ===

[Run context]
After hours (09:10 ET) — exit summary only.
Paper auth OK — equity $140061.81, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $140,061.81                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             105                                     |
|  Broker option positions       20                                      |
|  Unattributed contracts        1 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=456  buckets=188  win=47%                            |
|  Returns   avg=+27.0%  med=-7.7%  p10=-64.9%  p90=+142.5%              |
|  Realized  $+9,411.13                                                  |
|  Raw incl dropped  trades=990  real=$+7,815.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  1 100% +906.2 +906.2 +906.2 $   +145         |
|  b197 lab0197_s218_w3_10  1 100% +737.5 +737.5 +737.5 $   +118         |
|  b181 lab0181_s217_w2_10  2 100% +538.4 +538.4 +1007.1 $   +173        |
|  b180 lab0180_s217_w2_10  2 100% +469.8 +469.8 +885.7 $   +152         |
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 180 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  1   0% -95.9 -95.9 -95.9 $    -47       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b863 S408 NVDA260805C00222500 x1 stop_loss (-53.3%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (20)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  OXY260807C00058000           23    -25.5%   $   -402.00               |
|  NVDA260805C00217500          18    -22.5%   $   -115.00               |
|  AAPL260814C00330000           6    -29.7%   $   -106.50               |
|  OXY260807C00059000            4    -30.5%   $    -58.00               |
|  T260807C00023000              6    +11.1%   $    +42.00               |
|  AAPL260821C00335000           4    -14.1%   $    -36.00               |
|  NVDA260810C00225000           4    -24.6%   $    -34.00               |
|  DKNG260807C00025500           4    -17.6%   $    -30.00               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-04.log
elapsed=1.0s reconcile=0.5s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.0s. run=#5963 https://github.com/28twagg-ops/TradingBot/actions/runs/30912480962
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.6% (26/990)
# Options signal frequency

_Generated 2026-08-04T09:10:53.102009_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-04
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN | <<<
| Missing exit records (post) |   398 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   105 | INFO |
| Total closed lots           |   497 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=469.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260804T131545Z

- UTC timestamp: `20260804T131545Z`
- GitHub run: [#5964](https://github.com/28twagg-ops/TradingBot/actions/runs/30912886269)
- Run id: `30912886269`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-04T09:15:51.645983-04:00","date":"2026-08-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.5,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":140278.89,"open_positions":20,"pending_orders":0,"open_lots":105,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"5964","github_run_id":"30912886269","status":"ok"}
```

### Live bot full output

```text
13:15:46  INFO      Mode: summary
13:15:49  INFO        Daily log -> logs/daily/2026-08-04.md
13:15:49  INFO        Daily log reconciled -> logs/daily/2026-08-04.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $469.26|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $469.26|
|  Cash                                                           $210.17|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $259.09|
|  Open P&L                                                        $+2.63|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.73     $14.70   $14.71   +0.1%   $+0.09  |
|  AVB      Pullback50      $94.41     $187.24  $188.78  +0.8%   $+0.77  |
|  ECHO     MomReversal     $70.96     $85.51   $87.70   +2.6%   $+1.78  |
|                                                                        |
|  Total invested                                                 $259.09|
|  Total open P&L                                                  $+2.63|
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
|  2026-08-03  SELL  TSN  EarningsDrift  $93.73  P&L $+0.23              |
|  2026-08-03  SELL  FSLR  EarningsDrift  $93.03  P&L $-0.50             |
|  2026-08-03  SELL  ED  Pullback50  $69.86  P&L $-0.37                  |
|  2026-08-03  SELL  CPT  Pullback50  $93.14  P&L $-0.50                 |
|  2026-08-03  SELL  ALGN  Pullback50  $93.13  P&L $-0.51                |
|  2026-08-03  SELL  CINF  Pullback50  $95.73  P&L $+1.79                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=105 paper_keys=yes dry_run=False
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-04T09:15:51.645983-04:00 ===

[Run context]
After hours (09:15 ET) — exit summary only.
Paper auth OK — equity $140278.89, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $140,278.89                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             105                                     |
|  Broker option positions       20                                      |
|  Unattributed contracts        1 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=456  buckets=188  win=47%                            |
|  Returns   avg=+27.0%  med=-7.7%  p10=-64.9%  p90=+142.5%              |
|  Realized  $+9,411.13                                                  |
|  Raw incl dropped  trades=990  real=$+7,815.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  1 100% +906.2 +906.2 +906.2 $   +145         |
|  b197 lab0197_s218_w3_10  1 100% +737.5 +737.5 +737.5 $   +118         |
|  b181 lab0181_s217_w2_10  2 100% +538.4 +538.4 +1007.1 $   +173        |
|  b180 lab0180_s217_w2_10  2 100% +469.8 +469.8 +885.7 $   +152         |
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 180 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  1   0% -95.9 -95.9 -95.9 $    -47       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b863 S408 NVDA260805C00222500 x1 stop_loss (-53.3%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (20)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  OXY260807C00058000           23    -25.5%   $   -402.00               |
|  NVDA260805C00217500          18    -22.5%   $   -115.00               |
|  AAPL260814C00330000           6    -29.7%   $   -106.50               |
|  OXY260807C00059000            4    -30.5%   $    -58.00               |
|  T260807C00023000              6    +11.1%   $    +42.00               |
|  AAPL260821C00335000           4    -14.1%   $    -36.00               |
|  NVDA260810C00225000           4    -24.6%   $    -34.00               |
|  DKNG260807C00025500           4    -17.6%   $    -30.00               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-04.log
elapsed=0.5s reconcile=0.12s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.5s. run=#5964 https://github.com/28twagg-ops/TradingBot/actions/runs/30912886269
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.6% (26/990)
# Options signal frequency

_Generated 2026-08-04T09:15:57.548350_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-04
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN | <<<
| Missing exit records (post) |   398 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   105 | INFO |
| Total closed lots           |   497 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=469.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260804T132049Z

- UTC timestamp: `20260804T132049Z`
- GitHub run: [#5965](https://github.com/28twagg-ops/TradingBot/actions/runs/30913290532)
- Run id: `30913290532`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-04T09:20:53.374006-04:00","date":"2026-08-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.4,"phases_s":{"reconcile":0.1},"signals":0,"placed":0,"equity":140606.53,"open_positions":20,"pending_orders":0,"open_lots":105,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"5965","github_run_id":"30913290532","status":"ok"}
```

### Live bot full output

```text
13:20:50  INFO      Mode: summary
13:20:51  INFO        Daily log -> logs/daily/2026-08-04.md
13:20:51  INFO        Daily log reconciled -> logs/daily/2026-08-04.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $469.26|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $469.26|
|  Cash                                                           $210.17|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $259.09|
|  Open P&L                                                        $+2.63|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.73     $14.70   $14.71   +0.1%   $+0.09  |
|  AVB      Pullback50      $94.41     $187.24  $188.78  +0.8%   $+0.77  |
|  ECHO     MomReversal     $70.96     $85.51   $87.70   +2.6%   $+1.78  |
|                                                                        |
|  Total invested                                                 $259.09|
|  Total open P&L                                                  $+2.63|
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
|  2026-08-03  SELL  TSN  EarningsDrift  $93.73  P&L $+0.23              |
|  2026-08-03  SELL  FSLR  EarningsDrift  $93.03  P&L $-0.50             |
|  2026-08-03  SELL  ED  Pullback50  $69.86  P&L $-0.37                  |
|  2026-08-03  SELL  CPT  Pullback50  $93.14  P&L $-0.50                 |
|  2026-08-03  SELL  ALGN  Pullback50  $93.13  P&L $-0.51                |
|  2026-08-03  SELL  CINF  Pullback50  $95.73  P&L $+1.79                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=105 paper_keys=yes dry_run=False
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-04T09:20:53.374006-04:00 ===

[Run context]
After hours (09:20 ET) — exit summary only.
Paper auth OK — equity $140606.53, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $140,606.53                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             105                                     |
|  Broker option positions       20                                      |
|  Unattributed contracts        1 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=456  buckets=188  win=47%                            |
|  Returns   avg=+27.0%  med=-7.7%  p10=-64.9%  p90=+142.5%              |
|  Realized  $+9,411.13                                                  |
|  Raw incl dropped  trades=990  real=$+7,815.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  1 100% +906.2 +906.2 +906.2 $   +145         |
|  b197 lab0197_s218_w3_10  1 100% +737.5 +737.5 +737.5 $   +118         |
|  b181 lab0181_s217_w2_10  2 100% +538.4 +538.4 +1007.1 $   +173        |
|  b180 lab0180_s217_w2_10  2 100% +469.8 +469.8 +885.7 $   +152         |
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 180 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  1   0% -95.9 -95.9 -95.9 $    -47       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b863 S408 NVDA260805C00222500 x1 stop_loss (-53.3%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (20)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  OXY260807C00058000           23    -25.5%   $   -402.00               |
|  NVDA260805C00217500          18    -22.5%   $   -115.00               |
|  AAPL260814C00330000           6    -29.7%   $   -106.50               |
|  OXY260807C00059000            4    -30.5%   $    -58.00               |
|  T260807C00023000              6    +11.1%   $    +42.00               |
|  AAPL260821C00335000           4    -14.1%   $    -36.00               |
|  NVDA260810C00225000           4    -24.6%   $    -34.00               |
|  DKNG260807C00025500           4    -17.6%   $    -30.00               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-04.log
elapsed=0.4s reconcile=0.1s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.4s. run=#5965 https://github.com/28twagg-ops/TradingBot/actions/runs/30913290532
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.6% (26/990)
# Options signal frequency

_Generated 2026-08-04T09:20:59.291469_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-04
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN | <<<
| Missing exit records (post) |   398 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   105 | INFO |
| Total closed lots           |   497 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=469.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260804T132552Z

- UTC timestamp: `20260804T132552Z`
- GitHub run: [#5966](https://github.com/28twagg-ops/TradingBot/actions/runs/30913705560)
- Run id: `30913705560`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`11s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-04T09:25:57.522488-04:00","date":"2026-08-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":140096.13,"open_positions":20,"pending_orders":0,"open_lots":105,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"5966","github_run_id":"30913705560","status":"ok"}
```

### Live bot full output

```text
13:25:53  INFO      Mode: summary
13:25:54  INFO        Daily log -> logs/daily/2026-08-04.md
13:25:54  INFO        Daily log reconciled -> logs/daily/2026-08-04.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $469.26|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $469.26|
|  Cash                                                           $210.17|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $259.09|
|  Open P&L                                                        $+2.63|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.73     $14.70   $14.71   +0.1%   $+0.09  |
|  AVB      Pullback50      $94.41     $187.24  $188.78  +0.8%   $+0.77  |
|  ECHO     MomReversal     $70.96     $85.51   $87.70   +2.6%   $+1.78  |
|                                                                        |
|  Total invested                                                 $259.09|
|  Total open P&L                                                  $+2.63|
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
|  2026-08-03  SELL  TSN  EarningsDrift  $93.73  P&L $+0.23              |
|  2026-08-03  SELL  FSLR  EarningsDrift  $93.03  P&L $-0.50             |
|  2026-08-03  SELL  ED  Pullback50  $69.86  P&L $-0.37                  |
|  2026-08-03  SELL  CPT  Pullback50  $93.14  P&L $-0.50                 |
|  2026-08-03  SELL  ALGN  Pullback50  $93.13  P&L $-0.51                |
|  2026-08-03  SELL  CINF  Pullback50  $95.73  P&L $+1.79                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=105 paper_keys=yes dry_run=False
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-04T09:25:57.522488-04:00 ===

[Run context]
After hours (09:25 ET) — exit summary only.
Paper auth OK — equity $140096.13, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $140,096.13                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             105                                     |
|  Broker option positions       20                                      |
|  Unattributed contracts        1 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=456  buckets=188  win=47%                            |
|  Returns   avg=+27.0%  med=-7.7%  p10=-64.9%  p90=+142.5%              |
|  Realized  $+9,411.13                                                  |
|  Raw incl dropped  trades=990  real=$+7,815.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  1 100% +906.2 +906.2 +906.2 $   +145         |
|  b197 lab0197_s218_w3_10  1 100% +737.5 +737.5 +737.5 $   +118         |
|  b181 lab0181_s217_w2_10  2 100% +538.4 +538.4 +1007.1 $   +173        |
|  b180 lab0180_s217_w2_10  2 100% +469.8 +469.8 +885.7 $   +152         |
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 180 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  1   0% -95.9 -95.9 -95.9 $    -47       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b863 S408 NVDA260805C00222500 x1 stop_loss (-53.3%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (20)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  OXY260807C00058000           23    -25.5%   $   -402.00               |
|  NVDA260805C00217500          18    -22.5%   $   -115.00               |
|  AAPL260814C00330000           6    -29.7%   $   -106.50               |
|  OXY260807C00059000            4    -30.5%   $    -58.00               |
|  T260807C00023000              6    +11.1%   $    +42.00               |
|  AAPL260821C00335000           4    -14.1%   $    -36.00               |
|  NVDA260810C00225000           4    -24.6%   $    -34.00               |
|  DKNG260807C00025500           4    -17.6%   $    -30.00               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-04.log
elapsed=1.2s reconcile=0.6s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.2s. run=#5966 https://github.com/28twagg-ops/TradingBot/actions/runs/30913705560
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.6% (26/990)
# Options signal frequency

_Generated 2026-08-04T09:26:04.689304_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-04
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN | <<<
| Missing exit records (post) |   398 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   105 | INFO |
| Total closed lots           |   497 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=469.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260804T133045Z

- UTC timestamp: `20260804T133045Z`
- GitHub run: [#5967](https://github.com/28twagg-ops/TradingBot/actions/runs/30914117727)
- Run id: `30914117727`
- Live bot: exit=`0`, duration=`217s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-04T09:25:57.522488-04:00","date":"2026-08-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":140096.13,"open_positions":20,"pending_orders":0,"open_lots":105,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"5966","github_run_id":"30913705560","status":"ok"}
```

### Live bot full output

```text
13:30:45  INFO      Mode: morning_prep
13:30:46  INFO        [prep_positions] 3/3 (3 valid)
13:30:46  INFO      Fetching tickers (universe=both)...
13:30:46  INFO        S&P 500: 503
13:30:46  INFO        MidCap 400: 400
13:30:46  INFO        Total: 903 tickers
13:30:48  INFO        [prep_universe] 40/900 (40 valid)
13:30:49  INFO        [prep_universe] 80/900 (80 valid)
13:30:51  INFO        [prep_universe] 120/900 (120 valid)
13:30:52  INFO        [prep_universe] 160/900 (160 valid)
13:30:54  INFO        [prep_universe] 200/900 (199 valid)
13:31:01  INFO        [prep_universe] 240/900 (238 valid)
13:31:12  INFO        [prep_universe] 280/900 (278 valid)
13:31:25  INFO        [prep_universe] 320/900 (318 valid)
13:31:37  INFO        [prep_universe] 360/900 (358 valid)
13:31:50  INFO        [prep_universe] 400/900 (397 valid)
13:32:00  INFO        [prep_universe] 440/900 (437 valid)
13:32:14  INFO        [prep_universe] 480/900 (477 valid)
13:32:25  INFO        [prep_universe] 520/900 (517 valid)
13:32:38  INFO        [prep_universe] 560/900 (557 valid)
13:32:48  INFO        [prep_universe] 600/900 (597 valid)
13:33:02  INFO        [prep_universe] 640/900 (637 valid)
13:33:12  INFO        [prep_universe] 680/900 (677 valid)
13:33:25  INFO        [prep_universe] 720/900 (717 valid)
13:33:36  INFO        [prep_universe] 760/900 (757 valid)
13:33:49  INFO        [prep_universe] 800/900 (797 valid)
13:34:02  INFO        [prep_universe] 840/900 (836 valid)
13:34:13  INFO        [prep_universe] 880/900 (876 valid)
13:34:19  INFO        [prep_universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $468.77|
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
|  Invested                                                       $258.60|
|  Open P&L                                                        $+2.14|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.60     $14.70   $14.69   -0.0%   $-0.04  |
|  AVB      Pullback50      $93.59     $187.24  $187.15  -0.1%   $-0.05  |
|  ECHO     MomReversal     $71.41     $85.51   $88.26   +3.2%   $+2.23  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  AES       OrderType.STOP    6         None        14.62               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      0|
|  Signal candidates                                                   40|
|  Universe scanned                                                   900|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=105 paper_keys=yes dry_run=False
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-04T09:34:24.295586-04:00 ===

[Run context]
Paper auth OK — equity $141666.51, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-04 09:34:25,381 INFO   EXIT [b817|lab0817_s405_w2_1005_1045_r2|S405] stop_loss (-67.9%) SELL 1 OXY260807C00058000 @<= 0.23
2026-08-04 09:34:25,537 INFO   EXIT [b167|lab0167_s216_w2_1005_1045_r2|S216] stop_loss (-81.2%) SELL 1 DKNG260807C00025500 @<= 0.05
2026-08-04 09:34:26,129 INFO   EXIT [b797|lab0797_s399_w3_1045_1120_r2|S399] stop_loss (-76.8%) SELL 1 OXY260807C00059000 @<= 0.12
2026-08-04 09:34:30,329 INFO   EXIT [b409|lab0409_s364_w3_1045_1120_r2|S364] take_profit (+56.5%) SELL 1 NVDA260810C00225000 @<= 0.50
2026-08-04 09:34:30,752 INFO   EXIT [b861|lab0861_s408_w3_1045_1120_r2|S408] take_profit (+56.8%) SELL 1 NVDA260805C00220000 @<= 0.27
2026-08-04 09:34:34,184 INFO   EXIT [b381|lab0381_s362_w3_1045_1120_r2|S362] take_profit (+147.7%) SELL 1 NVDA260807C00217500 @<= 1.22
2026-08-04 09:34:34,312 INFO   EXIT [b793|lab0793_s399_w1_0928_1005_r2|S399] stop_loss (-76.0%) SELL 1 OXY260807C00060000 @<= 0.07
2026-08-04 09:34:34,664 INFO   EXIT [b831|lab0831_s406_w2_1005_1045_r2|S406] take_profit (+83.2%) SELL 1 NVDA260805C00217500 @<= 0.51
2026-08-04 09:34:35,090 INFO   EXIT [b849|lab0849_s407_w4_1120_1135_r2|S407] take_profit (+116.7%) SELL 1 NVDA260807C00220000 @<= 0.77

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260804T133606Z

- UTC timestamp: `20260804T133606Z`
- GitHub run: [#5968](https://github.com/28twagg-ops/TradingBot/actions/runs/30914542972)
- Run id: `30914542972`
- Live bot: exit=`0`, duration=`218s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-04T09:25:57.522488-04:00","date":"2026-08-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":140096.13,"open_positions":20,"pending_orders":0,"open_lots":105,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"5966","github_run_id":"30913705560","status":"ok"}
```

### Live bot full output

```text
13:36:07  INFO      Mode: morning_prep
13:36:08  INFO        [prep_positions] 3/3 (3 valid)
13:36:08  INFO      Fetching tickers (universe=both)...
13:36:08  INFO        S&P 500: 503
13:36:08  INFO        MidCap 400: 400
13:36:08  INFO        Total: 903 tickers
13:36:09  INFO        [prep_universe] 40/900 (40 valid)
13:36:10  INFO        [prep_universe] 80/900 (80 valid)
13:36:12  INFO        [prep_universe] 120/900 (120 valid)
13:36:14  INFO        [prep_universe] 160/900 (160 valid)
13:36:16  INFO        [prep_universe] 200/900 (199 valid)
13:36:21  INFO        [prep_universe] 240/900 (238 valid)
13:36:34  INFO        [prep_universe] 280/900 (278 valid)
13:36:47  INFO        [prep_universe] 320/900 (318 valid)
13:36:57  INFO        [prep_universe] 360/900 (358 valid)
13:37:10  INFO        [prep_universe] 400/900 (397 valid)
13:37:23  INFO        [prep_universe] 440/900 (437 valid)
13:37:34  INFO        [prep_universe] 480/900 (477 valid)
13:37:47  INFO        [prep_universe] 520/900 (517 valid)
13:37:57  INFO        [prep_universe] 560/900 (557 valid)
13:38:10  INFO        [prep_universe] 600/900 (597 valid)
13:38:23  INFO        [prep_universe] 640/900 (637 valid)
13:38:33  INFO        [prep_universe] 680/900 (677 valid)
13:38:46  INFO        [prep_universe] 720/900 (717 valid)
13:38:59  INFO        [prep_universe] 760/900 (757 valid)
13:39:09  INFO        [prep_universe] 800/900 (797 valid)
13:39:22  INFO        [prep_universe] 840/900 (836 valid)
13:39:35  INFO        [prep_universe] 880/900 (876 valid)
13:39:41  INFO        [prep_universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $469.60|
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
|  Invested                                                       $259.43|
|  Open P&L                                                        $+2.97|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.57     $14.70   $14.69   -0.1%   $-0.07  |
|  AVB      Pullback50      $93.69     $187.24  $187.35  +0.1%   $+0.05  |
|  ECHO     MomReversal     $72.17     $85.51   $89.20   +4.3%   $+2.99  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  AES       OrderType.STOP    6         None        14.62               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      0|
|  Signal candidates                                                   17|
|  Universe scanned                                                   900|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=105 paper_keys=yes dry_run=False
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-04T09:39:46.820013-04:00 ===

[Run context]
Paper auth OK — equity $142438.99, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-04 09:39:51,957 INFO   EXIT [b380|lab0380_s362_w3_1045_1120_r1|S362] take_profit (+145.6%) SELL 1 NVDA260807C00217500 @<= 1.19
2026-08-04 09:39:53,208 INFO   EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+111.1%) SELL 1 NVDA260807C00220000 @<= 0.77
2026-08-04 09:39:55,784 INFO   EXIT [b830|lab0830_s406_w2_1005_1045_r1|S406] take_profit (+65.6%) SELL 1 NVDA260805C00217500 @<= 0.50
2026-08-04 09:39:59,790 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-68.0%) SELL 2 OXY260807C00060000 @<= 0.05
2026-08-04 09:39:59,943 INFO   EXIT [b114|lab0114_s212_w4_1120_1135_r1|S212] stop_loss (-76.8%) SELL 1 OXY260807C00059000 @<= 0.12

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260804T134103Z

- UTC timestamp: `20260804T134103Z`
- GitHub run: [#5969](https://github.com/28twagg-ops/TradingBot/actions/runs/30914958570)
- Run id: `30914958570`
- Live bot: exit=`0`, duration=`217s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-04T09:25:57.522488-04:00","date":"2026-08-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":140096.13,"open_positions":20,"pending_orders":0,"open_lots":105,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"5966","github_run_id":"30913705560","status":"ok"}
```

### Live bot full output

```text
13:41:04  INFO      Mode: morning_prep
13:41:05  INFO        [prep_positions] 3/3 (3 valid)
13:41:05  INFO        Universe cache hit: 903 tickers (tickers_2026-08-04.json)
13:41:07  INFO        [prep_universe] 40/900 (40 valid)
13:41:08  INFO        [prep_universe] 80/900 (80 valid)
13:41:10  INFO        [prep_universe] 120/900 (120 valid)
13:41:11  INFO        [prep_universe] 160/900 (160 valid)
13:41:13  INFO        [prep_universe] 200/900 (199 valid)
13:41:20  INFO        [prep_universe] 240/900 (238 valid)
13:41:31  INFO        [prep_universe] 280/900 (278 valid)
13:41:44  INFO        [prep_universe] 320/900 (318 valid)
13:41:55  INFO        [prep_universe] 360/900 (358 valid)
13:42:08  INFO        [prep_universe] 400/900 (397 valid)
13:42:19  INFO        [prep_universe] 440/900 (437 valid)
13:42:32  INFO        [prep_universe] 480/900 (477 valid)
13:42:43  INFO        [prep_universe] 520/900 (517 valid)
13:42:56  INFO        [prep_universe] 560/900 (557 valid)
13:43:07  INFO        [prep_universe] 600/900 (597 valid)
13:43:21  INFO        [prep_universe] 640/900 (637 valid)
13:43:31  INFO        [prep_universe] 680/900 (677 valid)
13:43:45  INFO        [prep_universe] 720/900 (717 valid)
13:43:55  INFO        [prep_universe] 760/900 (757 valid)
13:44:09  INFO        [prep_universe] 800/900 (797 valid)
13:44:19  INFO        [prep_universe] 840/900 (836 valid)
13:44:33  INFO        [prep_universe] 880/900 (876 valid)
13:44:37  INFO        [prep_universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $468.85|
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
|  Invested                                                       $258.68|
|  Open P&L                                                        $+2.22|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.60     $14.70   $14.69   -0.0%   $-0.04  |
|  AVB      Pullback50      $93.80     $187.24  $187.56  +0.2%   $+0.16  |
|  ECHO     MomReversal     $71.28     $85.51   $88.10   +3.0%   $+2.10  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  AES       OrderType.STOP    6         None        14.62               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      0|
|  Signal candidates                                                   18|
|  Universe scanned                                                   900|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=104 paper_keys=yes dry_run=False
  alpaca positions=20
  FLAG b381|S362|b38a6d23 missing from Alpaca
  FLAG b380|S362|4cda3507 missing from Alpaca
  FLAG b849|S407|132f29e0 missing from Alpaca
  FLAG b0|ORPHAN|0770a149 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-04T09:44:42.802400-04:00 ===

[Run context]
Paper auth OK — equity $142984.22, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-04 09:44:49,672 INFO   EXIT [b185|lab0185_s217_w4_1120_1135_r2|S217] stop_loss (-55.6%) SELL 1 TSLA260805C00350000 @<= 0.17
2026-08-04 09:44:52,762 INFO   EXIT [b397|lab0397_s363_w4_1120_1135_r2|S363] take_profit (+50.0%) SELL 1 NVDA260807C00222500 @<= 0.49
2026-08-04 09:44:53,554 INFO   EXIT [b98|lab0098_s211_w3_1045_1120_r1|S211] stop_loss (-62.3%) SELL 1 MSFT260807C00520000 @<= 0.17
2026-08-04 09:44:54,325 INFO   EXIT [b408|lab0408_s364_w3_1045_1120_r1|S364] take_profit (+56.5%) SELL 1 NVDA260810C00225000 @<= 0.55
2026-08-04 09:44:54,538 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-68.0%) SELL 1 OXY260807C00060000 @<= 0.05
2026-08-04 09:44:54,895 INFO   EXIT [b113|lab0113_s212_w3_1045_1120_r2|S212] stop_loss (-72.6%) SELL 1 OXY260807C00059000 @<= 0.10
2026-08-04 09:44:55,805 INFO   EXIT [b916|lab0916_s412_w3_1045_1120_r1|S412] take_profit (+83.2%) SELL 1 NVDA260805C00217500 @<= 0.49

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260804T134612Z

- UTC timestamp: `20260804T134612Z`
- GitHub run: [#5970](https://github.com/28twagg-ops/TradingBot/actions/runs/30915370520)
- Run id: `30915370520`
- Live bot: exit=`0`, duration=`240s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-04T09:25:57.522488-04:00","date":"2026-08-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":140096.13,"open_positions":20,"pending_orders":0,"open_lots":105,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"5966","github_run_id":"30913705560","status":"ok"}
```

### Live bot full output

```text
13:46:13  INFO      Mode: morning_scan
13:46:15  INFO        [positions] 3/3 (3 valid)
13:46:15  INFO        Universe cache hit: 903 tickers (tickers_2026-08-04.json)
13:46:16  INFO        [universe] 40/900 (40 valid)
13:46:18  INFO        [universe] 80/900 (80 valid)
13:46:20  INFO        [universe] 120/900 (120 valid)
13:46:21  INFO        [universe] 160/900 (160 valid)
13:46:22  INFO        [universe] 200/900 (199 valid)
13:46:30  INFO        [universe] 240/900 (238 valid)
13:46:41  INFO        [universe] 280/900 (278 valid)
13:46:54  INFO        [universe] 320/900 (318 valid)
13:47:05  INFO        [universe] 360/900 (358 valid)
13:47:18  INFO        [universe] 400/900 (397 valid)
13:47:29  INFO        [universe] 440/900 (437 valid)
13:47:42  INFO        [universe] 480/900 (477 valid)
13:47:53  INFO        [universe] 520/900 (517 valid)
13:48:06  INFO        [universe] 560/900 (557 valid)
13:48:16  INFO        [universe] 600/900 (597 valid)
13:48:30  INFO        [universe] 640/900 (637 valid)
13:48:41  INFO        [universe] 680/900 (677 valid)
13:48:54  INFO        [universe] 720/900 (717 valid)
13:49:04  INFO        [universe] 760/900 (757 valid)
13:49:18  INFO        [universe] 800/900 (797 valid)
13:49:29  INFO        [universe] 840/900 (836 valid)
13:49:42  INFO        [universe] 880/900 (876 valid)
13:49:46  INFO        [universe] 900/900 (896 valid)
13:49:49  INFO        BUY  AMD  $93.57  [Pullback50]  id=f36940b5-b710-45ee-93f1-f9332f8c4946
13:49:49  INFO        BUY  ALGN  $93.20  [Pullback50]  id=40426c37-e437-49a4-9e6f-6eee4002cda3

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.86|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-08-04|
|  Universe                                                          both|
|  Mo~  Aug: VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Disabled                GapDown, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $467.86|
|  Cash                                                           $210.17|
|  Reserve                                          $23.39  (always kept)|
|  Available                                    $186.78  (for new trades)|
|  Trade size             $93.57  (20% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (3 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.60     $14.70   $14.69   -0.0%   $-0.04  |
|  AVB      Pullback50      $93.89     $187.24  $187.75  +0.3%   $+0.25  |
|  ECHO     MomReversal     $70.19     $85.51   $86.76   +1.5%   $+1.01  |
|                                                                        |
|  Total invested                                                 $257.69|
|  Total open P&L                                                  $+1.23|
|  Buys today: 0  |  entry cap: 2  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (37440.8m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  AES  P&L -0.0%  $-0.04                                            HOLD|
|  AVB  P&L +0.3%  $+0.25                                            HOLD|
|  ECHO  P&L +1.5%  $+1.01                                           HOLD|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 0 | filled 0 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 3|
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
|  Month: Aug  |  Regime: BULL                                           |
|  Primary: VolumeSpike  |  Secondary: 52wkLow (display only — schedule ~|
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  17                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AMD      Pullback50      eq     $514.24  47.6   -3.17   50MA bounce (-|
|  ALGN     Pullback50      eq     $173.04  41.3   -2.07   50MA bounce (-|
|  BIIB     Pullback50      eq     $201.35  53.9   -1.58   50MA bounce (+|
|  C        Pullback50      eq     $135.34  50.8   -1.98   50MA bounce (-|
|  FANG     Pullback50      eq     $192.21  52.2   -2.68   50MA bounce (+|
|  GS       Pullback50      eq     $1051.~  35.3   -2.24   50MA bounce (+|
|  HBAN     Pullback50      eq     $17.38   39.4   -1.74   50MA bounce (+|
|  PPG      Pullback50      eq     $115.66  50.6   -1.89   50MA bounce (-|
|  ALLY     Pullback50      eq     $44.27   38.2   -2.07   50MA bounce (-|
|  FTI      Pullback50      eq     $69.23   41.6   -2.37   50MA bounce (-|
|  LAMR     Pullback50      eq     $157.00  42.1   -1.86   50MA bounce (+|
|  NBIX     Pullback50      eq     $168.14  46.4   -1.45   50MA bounce (+|
|  NOV      Pullback50      eq     $19.49   51.3   -2.24   50MA bounce (-|
|  SLAB     Pullback50      eq     $218.85  55.8   -2.70   50MA bounce (+|
|  SNX      Pullback50      eq     $260.32  59.0   -2.10   50MA bounce (+|
|  SSD      Pullback50      eq     $194.38  55.2   -2.40   50MA bounce (+|
|  TCBI     Pullback50      eq     $101.42  43.1   -2.08   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] AMD  Pullback50                                    $93.57|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] ALGN  Pullback50                                   $93.20|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] BIIB  Pullback50                                     cap 5|13:50:11  INFO        place_all_stops: checking 5 positions...
13:50:12  INFO        STOP already live AES @ $14.62
13:50:12  INFO        STOP skipped ALGN: fractional (0.5404 shares) — software exit will handle it
13:50:12  INFO        STOP skipped AMD: fractional (0.1831 shares) — software exit will handle it
13:50:12  INFO        STOP skipped AVB: fractional (0.5001 shares) — software exit will handle it
13:50:12  INFO        STOP skipped ECHO: fractional (0.8091 shares) — software exit will handle it
13:50:12  INFO        Daily log -> logs/daily/2026-08-04.md
13:50:12  INFO        Dashboard written → logs/dashboard.md

|    SKIP [eq] C  Pullback50                                        cap 5|
|    SKIP [eq] FANG  Pullback50                                     cap 5|
|    SKIP [eq] GS  Pullback50                                       cap 5|
|    SKIP [eq] HBAN  Pullback50                                     cap 5|
|    SKIP [eq] PPG  Pullback50                                      cap 5|
|    SKIP [eq] ALLY  Pullback50                                     cap 5|
|    SKIP [eq] FTI  Pullback50                                      cap 5|
|    SKIP [eq] LAMR  Pullback50                                     cap 5|
|    SKIP [eq] NBIX  Pullback50                                     cap 5|
|    SKIP [eq] NOV  Pullback50                                      cap 5|
|    SKIP [eq] SLAB  Pullback50                                     cap 5|
|    SKIP [eq] SNX  Pullback50                                      cap 5|
|    SKIP [eq] SSD  Pullback50                                      cap 5|
|    SKIP [eq] TCBI  Pullback50                                     cap 5|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      2|
+------------------------------------------------------------------------+
|  AMD                                                  still unconfirmed|
|  ALGN                                                 still unconfirmed|
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
|  Strategy  VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Scanned                                                            896|
|  Signals                                                             17|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  2 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             5|
|  Equity                                                         $467.70|
|  Cash                                                            $23.41|
+========================================================================+
```

### Options bot full output

```text

## Run 20260804T135100Z

- UTC timestamp: `20260804T135100Z`
- GitHub run: [#5971](https://github.com/28twagg-ops/TradingBot/actions/runs/30915786675)
- Run id: `30915786675`
- Live bot: exit=`0`, duration=`218s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-04T09:25:57.522488-04:00","date":"2026-08-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":140096.13,"open_positions":20,"pending_orders":0,"open_lots":105,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"5966","github_run_id":"30913705560","status":"ok"}
```

### Live bot full output

```text
13:51:01  INFO      Mode: morning_scan
13:51:02  INFO        [positions] 5/5 (5 valid)
13:51:02  INFO        Universe cache hit: 903 tickers (tickers_2026-08-04.json)
13:51:03  INFO        [universe] 40/898 (40 valid)
13:51:04  INFO        [universe] 80/898 (80 valid)
13:51:05  INFO        [universe] 120/898 (120 valid)
13:51:07  INFO        [universe] 160/898 (160 valid)
13:51:08  INFO        [universe] 200/898 (199 valid)
13:51:18  INFO        [universe] 240/898 (238 valid)
13:51:28  INFO        [universe] 280/898 (278 valid)
13:51:41  INFO        [universe] 320/898 (318 valid)
13:51:54  INFO        [universe] 360/898 (358 valid)
13:52:04  INFO        [universe] 400/898 (397 valid)
13:52:18  INFO        [universe] 440/898 (437 valid)
13:52:31  INFO        [universe] 480/898 (477 valid)
13:52:41  INFO        [universe] 520/898 (517 valid)
13:52:54  INFO        [universe] 560/898 (557 valid)
13:53:04  INFO        [universe] 600/898 (597 valid)
13:53:17  INFO        [universe] 640/898 (637 valid)
13:53:30  INFO        [universe] 680/898 (677 valid)
13:53:43  INFO        [universe] 720/898 (717 valid)
13:53:53  INFO        [universe] 760/898 (757 valid)
13:54:05  INFO        [universe] 800/898 (797 valid)
13:54:16  INFO        [universe] 840/898 (836 valid)
13:54:29  INFO        [universe] 880/898 (876 valid)
13:54:35  INFO        [universe] 898/898 (894 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.71|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-08-04|
|  Universe                                                          both|
|  Mo~  Aug: VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Disabled                GapDown, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $467.71|
|  Cash                                                            $23.41|
|  Reserve                                          $23.39  (always kept)|
|  Available                                      $0.02  (for new trades)|
|  Trade size             $93.54  (20% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (5 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.62     $14.70   $14.69   -0.0%   $-0.02  |
|  ALGN     Pullback50      $93.02     $172.45  $172.13  -0.2%   $-0.17  |
|  AMD      Pullback50      $93.88     $510.87  $512.63  +0.3%   $+0.32  |
|  AVB      Pullback50      $93.59     $187.24  $187.15  -0.1%   $-0.05  |
|  ECHO     MomReversal     $70.18     $85.51   $86.75   +1.4%   $+1.00  |
|                                                                        |
|  Total invested                                                 $444.30|
|  Total open P&L                                                  $+1.09|
|  Buys today: 0  |  entry cap: 0  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (37445.6m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  ALGN  P&L -0.2%  $-0.17                                           HOLD|
|  AVB  P&L -0.1%  $-0.05                                            HOLD|
|  AES  P&L -0.0%  $-0.02                                            HOLD|
|  AMD  P&L +0.3%  $+0.32                                            HOLD|
|  ECHO  P&L +1.4%  $+1.00                                           HOLD|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 0 | filled 0 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 5|
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
|  Month: Aug  |  Regime: BULL                                           |
|  Primary: VolumeSpike  |  Secondary: 52wkLow (display only — schedule ~|
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  19                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  BIIB     Pullback50      eq     $201.82  54.4   -1.58   50MA bounce (+|
|  C        Pullback50      eq     $135.12  50.4   -1.96   50MA bounce (-|
|  FANG     Pullback50      eq     $192.85  52.9   -2.62   50MA bounce (+|
|  HBAN     Pullback50      eq     $17.34   38.8   -1.73   50MA bounce (+|
|  OXY      Pullback50      eq     $54.35   52.1   -2.12   50MA bounce (-|
|  PPG      Pullback50      eq     $115.66  50.6   -1.89   50MA bounce (-|
|  ALLY     Pullback50      eq     $44.27   38.2   -2.06   50MA bounce (-|
|  BYD      Pullback50      eq     $85.91   45.3   -2.56   50MA bounce (-|
|  CVLT     Pullback50      eq     $131.14  39.4   -1.43   50MA bounce (-|
|  FTI      Pullback50      eq     $69.74   43.2   -2.36   50MA bounce (+|
|  HIMS     Pullback50      eq     $31.20   38.0   -1.65   50MA bounce (+|
|  LAMR     Pullback50      eq     $156.90  41.8   -1.85   50MA bounce (+|
|  NOV      Pullback50      eq     $19.66   53.3   -2.23   50MA bounce (+|
|  NBIX     Pullback50      eq     $167.39  45.6   -1.44   50MA bounce (-|
|  NOVT     Pullback50      eq     $153.47  59.0   -2.98   50MA bounce (-|
|  SLAB     Pullback50      eq     $219.11  57.8   -2.68   50MA bounce (+|
|  SNX      Pullback50      eq     $262.26  60.4   -2.09   50MA bounce (+|
|  SSD      Pullback50      eq     $193.77  54.6   -2.39   50MA bounce (+|
|  TCBI     Pullback50      eq     $101.61  43.7   -2.07   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
13:54:38  INFO        place_all_stops: checking 5 positions...
13:54:38  INFO        STOP already live AES @ $14.62
13:54:38  INFO        STOP skipped ALGN: fractional (0.5404 shares) — software exit will handle it
13:54:38  INFO        STOP skipped AMD: fractional (0.1831 shares) — software exit will handle it
13:54:38  INFO        STOP skipped AVB: fractional (0.5001 shares) — software exit will handle it
13:54:38  INFO        STOP skipped ECHO: fractional (0.8091 shares) — software exit will handle it
13:54:38  INFO        Daily log -> logs/daily/2026-08-04.md
13:54:38  INFO        Dashboard written → logs/dashboard.md
+========================================================================+
|  Skipped                                  no entry slots (max_trades=0)|
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |
+========================================================================+
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Strategy  VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Scanned                                                            894|
|  Signals                                                             19|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             5|
|  Equity                                                         $468.31|
|  Cash                                                            $23.41|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=91 paper_keys=yes dry_run=False
  alpaca positions=18
  FLAG b98|S211|6b8fe1e4 missing from Alpaca
  FLAG b0|ORPHAN|9061b2cf missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-04T09:54:40.346064-04:00 ===

[Run context]
Paper auth OK — equity $143420.06, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-04 09:54:42,988 INFO   EXIT [b112|lab0112_s212_w3_1045_1120_r1|S212] stop_loss (-68.4%) SELL 1 OXY260807C00059000 @<= 0.12
2026-08-04 09:54:44,678 INFO   EXIT [b833|lab0833_s406_w3_1045_1120_r2|S406] take_profit (+51.5%) SELL 1 NVDA260805C00217500 @<= 0.45
2026-08-04 09:54:46,198 INFO   EXIT [b184|lab0184_s217_w4_1120_1135_r1|S217] stop_loss (-51.1%) SELL 1 TSLA260805C00350000 @<= 0.19
2026-08-04 09:54:50,059 INFO   EXIT [b59|lab0059_s207_w2_1005_1045_r2|S207] stop_loss (-65.0%) SELL 1 OXY260807C00058000 @<= 0.25

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260804T135600Z

- UTC timestamp: `20260804T135600Z`
- GitHub run: [#5972](https://github.com/28twagg-ops/TradingBot/actions/runs/30916211902)
- Run id: `30916211902`
- Live bot: exit=`0`, duration=`218s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-04T09:25:57.522488-04:00","date":"2026-08-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":140096.13,"open_positions":20,"pending_orders":0,"open_lots":105,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"5966","github_run_id":"30913705560","status":"ok"}
```

### Live bot full output

```text
13:56:01  INFO      Mode: morning_scan
13:56:02  INFO        [positions] 5/5 (5 valid)
13:56:02  INFO        Universe cache hit: 903 tickers (tickers_2026-08-04.json)
13:56:03  INFO        [universe] 40/898 (40 valid)
13:56:04  INFO        [universe] 80/898 (80 valid)
13:56:05  INFO        [universe] 120/898 (120 valid)
13:56:06  INFO        [universe] 160/898 (160 valid)
13:56:08  INFO        [universe] 200/898 (199 valid)
13:56:18  INFO        [universe] 240/898 (238 valid)
13:56:28  INFO        [universe] 280/898 (278 valid)
13:56:41  INFO        [universe] 320/898 (318 valid)
13:56:54  INFO        [universe] 360/898 (358 valid)
13:57:04  INFO        [universe] 400/898 (397 valid)
13:57:17  INFO        [universe] 440/898 (437 valid)
13:57:28  INFO        [universe] 480/898 (477 valid)
13:57:41  INFO        [universe] 520/898 (517 valid)
13:57:54  INFO        [universe] 560/898 (557 valid)
13:58:04  INFO        [universe] 600/898 (597 valid)
13:58:17  INFO        [universe] 640/898 (637 valid)
13:58:29  INFO        [universe] 680/898 (677 valid)
13:58:39  INFO        [universe] 720/898 (717 valid)
13:58:52  INFO        [universe] 760/898 (757 valid)
13:59:05  INFO        [universe] 800/898 (797 valid)
13:59:18  INFO        [universe] 840/898 (836 valid)
13:59:29  INFO        [universe] 880/898 (876 valid)
13:59:35  INFO        [universe] 898/898 (894 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $468.42|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-08-04|
|  Universe                                                          both|
|  Mo~  Aug: VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Disabled                GapDown, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $468.42|
|  Cash                                                            $23.41|
|  Reserve                                          $23.42  (always kept)|
|  Available                                      $0.00  (for new trades)|
|  Trade size             $93.68  (20% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (5 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.63     $14.70   $14.70   -0.0%   $-0.01  |
|  ALGN     Pullback50      $93.76     $172.45  $173.50  +0.6%   $+0.57  |
|  AMD      Pullback50      $93.50     $510.87  $510.56  -0.1%   $-0.06  |
|  AVB      Pullback50      $94.33     $187.24  $188.62  +0.7%   $+0.69  |
|  ECHO     MomReversal     $69.77     $85.51   $86.23   +0.8%   $+0.59  |
|                                                                        |
|  Total invested                                                 $444.99|
|  Total open P&L                                                  $+1.78|
|  Buys today: 0  |  entry cap: 0  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (37450.5m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  AMD  P&L -0.1%  $-0.06                                            HOLD|
|  AES  P&L -0.0%  $-0.01                                            HOLD|
|  ALGN  P&L +0.6%  $+0.57                                           HOLD|
|  AVB  P&L +0.7%  $+0.69                                            HOLD|
|  ECHO  P&L +0.8%  $+0.59                                           HOLD|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 0 | filled 0 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 5|
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
|  Month: Aug  |  Regime: BULL                                           |
|  Primary: VolumeSpike  |  Secondary: 52wkLow (display only — schedule ~|
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  26                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AMAT     Pullback50      eq     $545.23  45.1   -2.41   50MA bounce (-|
|  BIIB     Pullback50      eq     $202.27  54.8   -1.56   50MA bounce (+|
|  CINF     Pullback50      eq     $175.82  55.6   -2.07   50MA bounce (+|
|  C        Pullback50      eq     $135.29  50.8   -1.95   50MA bounce (-|
|  FANG     Pullback50      eq     $192.62  52.6   -2.55   50MA bounce (+|
|  EQR      Pullback50      eq     $67.58   46.4   -2.42   50MA bounce (+|
|  ESS      Pullback50      eq     $285.22  40.5   -2.74   50MA bounce (-|
|  HBAN     Pullback50      eq     $17.41   40.0   -1.72   50MA bounce (+|
|  KDP      Pullback50      eq     $30.78   54.5   -2.85   50MA bounce (-|
|  KEYS     Pullback50      eq     $335.07  56.3   -3.18   50MA bounce (+|
|  MAS      Pullback50      eq     $75.53   45.1   -1.31   50MA bounce (+|
|  OXY      Pullback50      eq     $54.33   52.0   -2.11   50MA bounce (-|
|  PPG      Pullback50      eq     $116.19  51.4   -1.88   50MA bounce (-|
|  ALLY     Pullback50      eq     $44.38   39.0   -2.05   50MA bounce (-|
|  AM       Pullback50      eq     $21.82   41.2   -2.81   50MA bounce (-|
|  BC       Pullback50      eq     $80.79   54.8   -2.31   50MA bounce (-|
|  BYD      Pullback50      eq     $86.64   47.4   -2.54   50MA bounce (-|
|  CVLT     Pullback50      eq     $131.43  39.7   -1.42   50MA bounce (-|
|  FTI      Pullback50      eq     $69.71   43.1   -2.35   50MA bounce (+|
|  NBIX     Pullback50      eq     $168.09  46.3   -1.44   50MA bounce (+|
|  NOV      Pullback50      eq     $19.64   53.1   -2.22   50MA bounce (-|
|  NOVT     Pullback50      eq     $154.39  60.0   -2.98   50MA bounce (+|
|  SNX      Pullback50      eq     $261.62  60.0   -2.06   50MA bounce (+|
|  SLAB     Pullback50      eq     $219.19  58.3   -2.66   50MA bounce (+|13:59:38  INFO        place_all_stops: checking 5 positions...
13:59:38  INFO        STOP already live AES @ $14.62
13:59:38  INFO        STOP skipped ALGN: fractional (0.5404 shares) — software exit will handle it
13:59:38  INFO        STOP skipped AMD: fractional (0.1831 shares) — software exit will handle it
13:59:38  INFO        STOP skipped AVB: fractional (0.5001 shares) — software exit will handle it
13:59:38  INFO        STOP skipped ECHO: fractional (0.8091 shares) — software exit will handle it
13:59:38  INFO        Daily log -> logs/daily/2026-08-04.md
13:59:38  INFO        Dashboard written → logs/dashboard.md

|  TCBI     Pullback50      eq     $101.65  43.8   -2.07   50MA bounce (+|
|  SSD      Pullback50      eq     $194.69  55.5   -2.38   50MA bounce (+|
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
|  Strategy  VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Scanned                                                            894|
|  Signals                                                             26|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             5|
|  Equity                                                         $468.37|
|  Cash                                                            $23.41|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=95 paper_keys=yes dry_run=False
  alpaca positions=16
  FLAG b0|ORPHAN|8a36990f missing from Alpaca
  FLAG b380|S362|4cda3507 missing from Alpaca
  FLAG b98|S211|6b8fe1e4 missing from Alpaca
  FLAG b0|ORPHAN|0770a149 missing from Alpaca
  FLAG b185|S217|dd939679 missing from Alpaca
  FLAG b184|S217|15e073be missing from Alpaca
  FLAG b114|S212|7df43d06 missing from Alpaca
  FLAG b113|S212|366cf611 missing from Alpaca
  FLAG b112|S212|39fcdbf3 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-04T09:59:40.558330-04:00 ===

[Run context]
Paper auth OK — equity $142357.00, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260804T140105Z

- UTC timestamp: `20260804T140105Z`
- GitHub run: [#5973](https://github.com/28twagg-ops/TradingBot/actions/runs/30916647493)
- Run id: `30916647493`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`204s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-04T10:01:11.939653-04:00","date":"2026-08-04","mode":"entry+manage","header":"entry+manage (48 new)","elapsed_s":194.7,"phases_s":{"reconcile":0.53,"cancel":0.15,"manage":20.34,"scan":68.8,"entries":102.13,"reconcile2":1.69},"signals":384,"placed":48,"equity":142681.0,"open_positions":22,"pending_orders":20,"open_lots":85,"submitted_today":48,"filled_today":28,"unattributed_contracts":17,"top_signals":["S165:AMZN","S165:DOCN","S165:GTLB","S165:NKE","S165:XOM","S165:OXY","S164:AMZN","S164:DOCN"],"github_run":"5973","github_run_id":"30916647493","status":"ok"}
```

### Live bot full output

```text
14:01:06  INFO      Mode: exits
14:01:08  INFO        Daily log -> logs/daily/2026-08-04.md
14:01:08  INFO        Daily log reconciled -> logs/daily/2026-08-04.md (0 ledger rows)
14:01:08  INFO        place_all_stops: checking 5 positions...
14:01:08  INFO        STOP already live AES @ $14.62
14:01:08  INFO        STOP skipped ALGN: fractional (0.5404 shares) — software exit will handle it
14:01:08  INFO        STOP skipped AMD: fractional (0.1831 shares) — software exit will handle it
14:01:08  INFO        STOP skipped AVB: fractional (0.5001 shares) — software exit will handle it
14:01:08  INFO        STOP skipped ECHO: fractional (0.8091 shares) — software exit will handle it
14:01:09  INFO        [positions] 5/5 (5 valid)
14:01:09  INFO        Daily log -> logs/daily/2026-08-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $468.63|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMD  P&L -0.3%  $-0.30                                            HOLD|
|  AES  P&L +0.0%  $+0.03                                            HOLD|
|  AVB  P&L +0.7%  $+0.65                                            HOLD|
|  ECHO  P&L +0.8%  $+0.53                                           HOLD|
|  ALGN  P&L +1.1%  $+1.01                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
|  Logged exits                                                         0|
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

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=62 paper_keys=yes dry_run=False
  alpaca positions=16
  FLAG b184|S217|15e073be missing from Alpaca
  FLAG b112|S212|50af75bf missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-04T10:01:11.939653-04:00 ===

[Run context]
Paper auth OK — equity $142681.00, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 384 signal(s); top: ['S165:AMZN', 'S165:DOCN', 'S165:GTLB', 'S165:NKE', 'S165:XOM', 'S165:OXY', 'S164:AMZN', 'S164:DOCN']
Paper lab: $142748 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 326 no tradeable call, 298 pending order
Placed 48 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $142,681.00                             |
|  Signals this run              384                                     |
|  Orders submitted (session)    48                                      |
|  Orders filled today (ledger)  28                                      |
|  Entries placed this run       48                                      |
|  Open virtual lots             85                                      |
|  Broker option positions       22                                      |
|  Unattributed contracts        17 (orphan reconcile)                   |
|  Pending orders                20                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=507  buckets=200  win=49%                            |
|  Returns   avg=+28.5%  med=+0.0%  p10=-65.8%  p90=+140.1%              |
|  Realized  $+10,446.24                                                 |
|  Raw incl dropped  trades=1041  real=$+8,850.69                        |
|  Today     trades=19  avg=+11.7%  med=+0.0%  real=$-71.89              |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  1 100% +906.2 +906.2 +906.2 $   +145         |
|  b197 lab0197_s218_w3_10  1 100% +737.5 +737.5 +737.5 $   +118         |
|  b181 lab0181_s217_w2_10  2 100% +538.4 +538.4 +1007.1 $   +173        |
|  b180 lab0180_s217_w2_10  2 100% +469.8 +469.8 +885.7 $   +152         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  1 100% +273.1 +273.1 +273.1 $    +71         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  ... 192 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  1   0% -95.9 -95.9 -95.9 $    -47       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (20)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S203:SMCI(2), S366:NKE(2), S397:AMZN(2) |
+------------------------------------------------------------------------+
|  b24  S203 SMCI     limit=0.44                                         |
|  b25  S203 SMCI     limit=0.44                                         |
|  b432 S366 NKE      limit=0.66                                         |
|  b433 S366 NKE      limit=0.66                                         |
|  b776 S397 AMZN     limit=0.48                                         |
|  ... 15 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b59  S207 OXY260807C00058000 x1 stop_loss (-65.0%)                    |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (22)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  OXY260807C00058000           22    -65.0%   $   -978.52               |
|  T260807C00023000              6    -34.9%   $   -132.00               |
|  AAPL260814C00330000           6    -31.4%   $   -112.50               |
|  PATH260807C00013500           8    +40.7%   $    +88.00               |
|  NVDA260805C00217500          14    +19.8%   $    +78.56               |
|  NKE260807C00042000            6    -19.4%   $    -78.00               |
|  TTD260807P00017000            4    -25.5%   $    -56.00               |
|  NKE260821C00044000            4    -19.4%   $    -52.00               |
|  ... 14 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-04.log
elapsed=194.7s reconcile=0.53s cancel=0.15s manage=20.34s scan=68.8s entries=102.13s
STATUS: options_morning_bot run complete (PAPER) elapsed=194.7s. run=#5973 https://github.com/28twagg-ops/TradingBot/actions/runs/30916647493
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.csv
Summary: 17 buckets closed trades, $-71.89 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.8% (29/1041)
# Options signal frequency

_Generated 2026-08-04T10:04:32.222426_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-04
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN | <<<
| Missing exit records (post) |   398 | WARN | <<<
| State/ledger mismatches     |    10 | WARN | <<<
| Total open lots             |    85 | INFO |
| Total closed lots           |   545 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=468.55 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260804T140805Z

- UTC timestamp: `20260804T140805Z`
- GitHub run: [#5974](https://github.com/28twagg-ops/TradingBot/actions/runs/30917090113)
- Run id: `30917090113`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-04T10:01:11.939653-04:00","date":"2026-08-04","mode":"entry+manage","header":"entry+manage (48 new)","elapsed_s":194.7,"phases_s":{"reconcile":0.53,"cancel":0.15,"manage":20.34,"scan":68.8,"entries":102.13,"reconcile2":1.69},"signals":384,"placed":48,"equity":142681.0,"open_positions":22,"pending_orders":20,"open_lots":85,"submitted_today":48,"filled_today":28,"unattributed_contracts":17,"top_signals":["S165:AMZN","S165:DOCN","S165:GTLB","S165:NKE","S165:XOM","S165:OXY","S164:AMZN","S164:DOCN"],"github_run":"5973","github_run_id":"30916647493","status":"ok"}
```

### Live bot full output

```text
14:08:06  INFO      Mode: exits
14:08:07  INFO        Daily log -> logs/daily/2026-08-04.md
14:08:07  INFO        Daily log reconciled -> logs/daily/2026-08-04.md (0 ledger rows)
14:08:07  INFO        place_all_stops: checking 5 positions...
14:08:07  INFO        STOP already live AES @ $14.62
14:08:07  INFO        STOP skipped ALGN: fractional (0.5404 shares) — software exit will handle it
14:08:07  INFO        STOP skipped AMD: fractional (0.1831 shares) — software exit will handle it
14:08:07  INFO        STOP skipped AVB: fractional (0.5001 shares) — software exit will handle it
14:08:07  INFO        STOP skipped ECHO: fractional (0.8091 shares) — software exit will handle it
14:08:08  INFO        [positions] 5/5 (5 valid)
14:08:08  INFO        Daily log -> logs/daily/2026-08-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:08 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.11|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALGN  P&L -0.1%  $-0.14                                           HOLD|
|  AES  P&L -0.0%  $-0.04                                            HOLD|
|  AVB  P&L +0.7%  $+0.65                                            HOLD|
|  AMD  P&L +1.2%  $+1.08                                            HOLD|
|  ECHO  P&L +2.9%  $+1.99                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
|  Logged exits                                                         0|
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

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=85 paper_keys=yes dry_run=False
  alpaca positions=24
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-04T10:08:10.283400-04:00 ===

[Run context]
Paper auth OK — equity $143497.16, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-04 10:08:13,799 INFO   EXIT [b832|lab0832_s406_w3_1045_1120_r1|S406] take_profit (+51.5%) SELL 1 NVDA260805C00217500 @<= 0.44

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 402 signal(s); top: ['S165:AMZN', 'S165:DOCN', 'S165:GTLB', 'S165:NKE', 'S165:XOM', 'S165:OXY', 'S164:AMZN', 'S164:DOCN']
Paper lab: $143221 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260804T141340Z

- UTC timestamp: `20260804T141340Z`
- GitHub run: [#5976](https://github.com/28twagg-ops/TradingBot/actions/runs/30917599618)
- Run id: `30917599618`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`101s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-04T10:13:43.600722-04:00","date":"2026-08-04","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":91.9,"phases_s":{"reconcile":5.62,"cancel":0.03,"manage":5.46,"scan":59.58,"entries":17.59,"reconcile2":3.14},"signals":386,"placed":1,"equity":143231.45,"open_positions":27,"pending_orders":42,"open_lots":106,"submitted_today":100,"filled_today":58,"unattributed_contracts":12,"top_signals":["S165:AMZN","S165:DOCN","S165:GTLB","S165:NKE","S165:XOM","S165:OXY","S164:AMZN","S164:DOCN"],"github_run":"5976","github_run_id":"30917599618","status":"ok"}
```

### Live bot full output

```text
14:13:41  INFO      Mode: exits
14:13:41  INFO        Daily log -> logs/daily/2026-08-04.md
14:13:41  INFO        Daily log reconciled -> logs/daily/2026-08-04.md (0 ledger rows)
14:13:41  INFO        place_all_stops: checking 5 positions...
14:13:41  INFO        STOP already live AES @ $14.62
14:13:41  INFO        STOP skipped ALGN: fractional (0.5404 shares) — software exit will handle it
14:13:41  INFO        STOP skipped AMD: fractional (0.1831 shares) — software exit will handle it
14:13:41  INFO        STOP skipped AVB: fractional (0.5001 shares) — software exit will handle it
14:13:41  INFO        STOP skipped ECHO: fractional (0.8091 shares) — software exit will handle it
14:13:41  INFO        [positions] 5/5 (5 valid)
14:13:41  INFO        Daily log -> logs/daily/2026-08-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:13 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $469.35|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALGN  P&L -0.3%  $-0.31                                           HOLD|
|  AES  P&L -0.1%  $-0.07                                            HOLD|
|  AVB  P&L +0.5%  $+0.47                                            HOLD|
|  AMD  P&L +0.8%  $+0.71                                            HOLD|
|  ECHO  P&L +2.8%  $+1.94                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
|  Logged exits                                                         0|
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

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=85 paper_keys=yes dry_run=False
  alpaca positions=29
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-04T10:13:43.600722-04:00 ===

[Run context]
Paper auth OK — equity $143231.45, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-04 10:13:50,044 INFO   EXIT [b280|lab0280_s351_w1_0928_1005_r1|S351] take_profit (+163.6%) SELL 1 AMZN260805C00287500 @<= 0.84
2026-08-04 10:13:51,652 INFO   EXIT [b844|lab0844_s407_w2_1005_1045_r1|S407] take_profit (+76.9%) SELL 1 AMZN260807C00302500 @<= 0.24
2026-08-04 10:13:51,908 INFO   EXIT [b379|lab0379_s362_w2_1005_1045_r2|S362] take_profit (+60.9%) SELL 1 AMZN260807C00295000 @<= 0.68
2026-08-04 10:13:53,161 INFO   EXIT [b365|lab0365_s361_w2_1005_1045_r2|S361] take_profit (+86.8%) SELL 1 AMZN260805C00290000 @<= 0.53
2026-08-04 10:13:54,836 INFO   EXIT [b793|lab0793_s399_w1_0928_1005_r2|S399] take_profit (+68.3%) SELL 1 AMZN260807C00297500 @<= 0.48
2026-08-04 10:13:54,927 INFO   EXIT [b83|lab0083_s210_w2_1005_1045_r2|S210] take_profit (+55.6%) SELL 1 PATH260807C00013500 @<= 0.39

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 386 signal(s); top: ['S165:AMZN', 'S165:DOCN', 'S165:GTLB', 'S165:NKE', 'S165:XOM', 'S165:OXY', 'S164:AMZN', 'S164:DOCN']
Paper lab: $143540 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 188 no tradeable call, 74 already attempted today, 209 pending order
Placed 1 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $143,231.45                             |
|  Signals this run              386                                     |
|  Orders submitted (session)    100                                     |
|  Orders filled today (ledger)  58                                      |
|  Entries placed this run       1                                       |
|  Open virtual lots             106                                     |
|  Broker option positions       27                                      |
|  Unattributed contracts        12 (orphan reconcile)                   |
|  Pending orders                42                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=571  buckets=202  win=50%                            |
|  Returns   avg=+31.5%  med=+5.6%  p10=-66.2%  p90=+150.0%              |
|  Realized  $+11,571.99                                                 |
|  Raw incl dropped  trades=1105  real=$+9,976.44                        |
|  Today     trades=25  avg=+24.8%  med=+52.9%  real=$+39.11             |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  1 100% +906.2 +906.2 +906.2 $   +145         |
|  b197 lab0197_s218_w3_10  1 100% +737.5 +737.5 +737.5 $   +118         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  2 100% +273.1 +273.1 +273.1 $   +142         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b791 lab0791_s398_w4_11  2 100% +246.8 +246.8 +338.1 $   +254         |
|  b844 lab0844_s407_w2_10  2 100% +245.5 +245.5 +446.1 $    +80         |
|  ... 194 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  2   0% -95.9 -95.9 -95.9 $    -94       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (42)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S366:NKE(4), S398:AMZN(4), S405:AMZN(4) |
+------------------------------------------------------------------------+
|  b24  S203 SMCI     limit=0.44                                         |
|  b25  S203 SMCI     limit=0.44                                         |
|  b432 S366 NKE      limit=0.66                                         |
|  b433 S366 NKE      limit=0.66                                         |
|  b776 S397 AMZN     limit=0.48                                         |
|  ... 37 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b59  S207 OXY260807C00058000 x1 stop_loss (-65.0%)                    |
|  b832 S406 NVDA260805C00217500 x1 take_profit (+51.5%)                 |
|  b844 S407 AMZN260807C00302500 x1 take_profit (+76.9%)                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (27)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  OXY260807C00058000           22    -65.0%   $   -978.52               |
|  AMZN260805C00287500           5   +136.4%   $   +225.00               |
|  T260807C00023000              6    -42.9%   $   -162.00               |
|  AMZN260807C00295000           8    +45.8%   $   +145.78               |
|  NVDA260805C00217500          14    +33.9%   $   +134.56               |
|  PATH260807C00013500           7    +51.9%   $    +98.00               |
|  AMZN260807C00292500           4    +38.0%   $    +97.00               |
|  NKE260807C00042000            6    -23.9%   $    -96.00               |
|  ... 19 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-04.log
elapsed=91.9s reconcile=5.62s cancel=0.03s manage=5.46s scan=59.58s entries=17.59s
STATUS: options_morning_bot run complete (PAPER) elapsed=91.9s. run=#5976 https://github.com/28twagg-ops/TradingBot/actions/runs/30917599618
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.csv
Summary: 22 buckets closed trades, $+39.11 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.8% (31/1105)
# Options signal frequency

_Generated 2026-08-04T10:15:21.007933_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-04
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN | <<<
| Missing exit records (post) |   398 | WARN | <<<
| State/ledger mismatches     |    14 | WARN | <<<
| Total open lots             |   106 | INFO |
| Total closed lots           |   607 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=469.39 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260804T141611Z

- UTC timestamp: `20260804T141611Z`
- GitHub run: [#5977](https://github.com/28twagg-ops/TradingBot/actions/runs/30917958384)
- Run id: `30917958384`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`154s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-04T10:16:17.100671-04:00","date":"2026-08-04","mode":"entry+manage","header":"entry+manage (22 new)","elapsed_s":144.8,"phases_s":{"reconcile":6.83,"cancel":0.16,"manage":14.12,"scan":62.35,"entries":56.03,"reconcile2":4.59},"signals":384,"placed":22,"equity":143000.16,"open_positions":29,"pending_orders":22,"open_lots":118,"submitted_today":70,"filled_today":76,"unattributed_contracts":11,"top_signals":["S165:AMZN","S165:DOCN","S165:GTLB","S165:NKE","S165:XOM","S165:OXY","S164:AMZN","S164:DOCN"],"github_run":"5977","github_run_id":"30917958384","status":"ok"}
```

### Live bot full output

```text
14:16:12  INFO      Mode: exits
14:16:13  INFO        Daily log -> logs/daily/2026-08-04.md
14:16:13  INFO        Daily log reconciled -> logs/daily/2026-08-04.md (0 ledger rows)
14:16:13  INFO        place_all_stops: checking 5 positions...
14:16:13  INFO        STOP already live AES @ $14.62
14:16:13  INFO        STOP skipped ALGN: fractional (0.5404 shares) — software exit will handle it
14:16:13  INFO        STOP skipped AMD: fractional (0.1831 shares) — software exit will handle it
14:16:13  INFO        STOP skipped AVB: fractional (0.5001 shares) — software exit will handle it
14:16:13  INFO        STOP skipped ECHO: fractional (0.8091 shares) — software exit will handle it
14:16:14  INFO        [positions] 5/5 (5 valid)
14:16:14  INFO        Daily log -> logs/daily/2026-08-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $469.52|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALGN  P&L -0.4%  $-0.35                                           HOLD|
|  AES  P&L -0.1%  $-0.07                                            HOLD|
|  AVB  P&L +0.5%  $+0.45                                            HOLD|
|  AMD  P&L +1.0%  $+0.97                                            HOLD|
|  ECHO  P&L +2.8%  $+1.95                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
|  Logged exits                                                         0|
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

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=85 paper_keys=yes dry_run=False
  alpaca positions=29
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-04T10:16:17.100671-04:00 ===

[Run context]
Paper auth OK — equity $142971.16, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-04 10:16:26,827 INFO   EXIT [b81|lab0081_s210_w1_0928_1005_r2|S210] take_profit (+51.9%) SELL 1 PATH260807C00013500 @<= 0.42
2026-08-04 10:16:27,455 INFO   EXIT [b365|lab0365_s361_w2_1005_1045_r2|S361] take_profit (+54.5%) SELL 1 AMZN260805C00290000 @<= 0.39
2026-08-04 10:16:29,402 INFO   EXIT [b276|lab0276_s350_w1_0928_1005_r1|S350] take_profit (+118.2%) SELL 1 AMZN260805C00287500 @<= 0.71

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 384 signal(s); top: ['S165:AMZN', 'S165:DOCN', 'S165:GTLB', 'S165:NKE', 'S165:XOM', 'S165:OXY', 'S164:AMZN', 'S164:DOCN']
Paper lab: $142657 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 116 no tradeable call, 168 open order exists, 130 pending order
Placed 22 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $143,000.16                             |
|  Signals this run              384                                     |
|  Orders submitted (session)    70                                      |
|  Orders filled today (ledger)  76                                      |
|  Entries placed this run       22                                      |
|  Open virtual lots             118                                     |
|  Broker option positions       29                                      |
|  Unattributed contracts        11 (orphan reconcile)                   |
|  Pending orders                22                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=578  buckets=204  win=51%                            |
|  Returns   avg=+31.9%  med=+5.6%  p10=-66.1%  p90=+146.3%              |
|  Realized  $+11,765.99                                                 |
|  Raw incl dropped  trades=1112  real=$+10,170.44                       |
|  Today     trades=28  avg=+24.5%  med=+51.5%  real=$+42.11             |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  1 100% +906.2 +906.2 +906.2 $   +145         |
|  b197 lab0197_s218_w3_10  1 100% +737.5 +737.5 +737.5 $   +118         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  2 100% +273.1 +273.1 +273.1 $   +142         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b791 lab0791_s398_w4_11  2 100% +246.8 +246.8 +338.1 $   +254         |
|  b844 lab0844_s407_w2_10  2 100% +245.5 +245.5 +446.1 $    +80         |
|  ... 196 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  2   0% -95.9 -95.9 -95.9 $    -94       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (22)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S203:SMCI(2), S366:NKE(2), S397:AMZN(2) |
+------------------------------------------------------------------------+
|  b24  S203 SMCI     limit=0.44                                         |
|  b25  S203 SMCI     limit=0.44                                         |
|  b432 S366 NKE      limit=0.66                                         |
|  b433 S366 NKE      limit=0.66                                         |
|  b776 S397 AMZN     limit=0.48                                         |
|  ... 17 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (29)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  OXY260807C00058000           21    -56.2%   $   -808.04               |
|  T260807C00023000              6    -42.9%   $   -162.00               |
|  AMZN260805C00287500           4   +112.1%   $   +148.00               |
|  AMZN260807C00295000          12    +20.4%   $   +109.78               |
|  PATH260807C00013500           6    +51.9%   $    +84.00               |
|  AMZN260807C00292500           4    +22.4%   $    +57.00               |
|  AMZN260805C00290000           5    +36.4%   $    +54.67               |
|  AAPL260814C00330000           6    -14.6%   $    -52.50               |
|  ... 21 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-04.log
elapsed=144.8s reconcile=6.83s cancel=0.16s manage=14.12s scan=62.35s entries=56.03s
STATUS: options_morning_bot run complete (PAPER) elapsed=144.8s. run=#5977 https://github.com/28twagg-ops/TradingBot/actions/runs/30917958384
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.csv
Summary: 25 buckets closed trades, $+42.11 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.8% (31/1112)
# Options signal frequency

_Generated 2026-08-04T10:18:47.632998_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-04
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN | <<<
| Missing exit records (post) |   398 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   118 | INFO |
| Total closed lots           |   614 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=469.55 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260804T142047Z

- UTC timestamp: `20260804T142047Z`
- GitHub run: [#5978](https://github.com/28twagg-ops/TradingBot/actions/runs/30918391386)
- Run id: `30918391386`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`123s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-04T10:20:53.920724-04:00","date":"2026-08-04","mode":"entry+manage","header":"entry+manage (9 new)","elapsed_s":114.4,"phases_s":{"reconcile":0.93,"cancel":0.03,"manage":6.98,"scan":54.67,"entries":50.41,"reconcile2":0.97},"signals":391,"placed":9,"equity":142740.54,"open_positions":32,"pending_orders":20,"open_lots":129,"submitted_today":79,"filled_today":91,"unattributed_contracts":13,"top_signals":["S165:AMZN","S165:DOCN","S165:GTLB","S165:NKE","S165:XOM","S165:OXY","S164:AMZN","S164:DOCN"],"github_run":"5978","github_run_id":"30918391386","status":"ok"}
```

### Live bot full output

```text
14:20:48  INFO      Mode: exits
14:20:49  INFO        Daily log -> logs/daily/2026-08-04.md
14:20:49  INFO        Daily log reconciled -> logs/daily/2026-08-04.md (0 ledger rows)
14:20:49  INFO        place_all_stops: checking 5 positions...
14:20:49  INFO        STOP already live AES @ $14.62
14:20:49  INFO        STOP skipped ALGN: fractional (0.5404 shares) — software exit will handle it
14:20:49  INFO        STOP skipped AMD: fractional (0.1831 shares) — software exit will handle it
14:20:49  INFO        STOP skipped AVB: fractional (0.5001 shares) — software exit will handle it
14:20:49  INFO        STOP skipped ECHO: fractional (0.8091 shares) — software exit will handle it
14:20:49  INFO        [positions] 5/5 (5 valid)
14:20:49  INFO        SELL MARKET [urgent] ALGN closed
14:20:51  INFO        TX logged: SELL ALGN  P&L -0.66%
14:20:51  INFO        Daily log -> logs/daily/2026-08-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $468.63|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALGN  P&L -0.7%  $-0.62                        EXIT: stop_loss (-0.7%)|
|  AES  P&L -0.1%  $-0.10                                            HOLD|
|  AVB  P&L +0.5%  $+0.47                                            HOLD|
|  AMD  P&L +0.5%  $+0.49                                            HOLD|
|  ECHO  P&L +2.6%  $+1.78                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  1 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                4|
|  Logged exits                                                         1|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  ALGN                                        -0.66%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=118 paper_keys=yes dry_run=False
  alpaca positions=31
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-04T10:20:53.920724-04:00 ===

[Run context]
Paper auth OK — equity $142740.54, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-04 10:20:56,311 INFO   EXIT [b351|lab0351_s360_w2_1005_1045_r2|S360] take_profit (+53.0%) SELL 1 AMZN260805C00290000 @<= 0.47
2026-08-04 10:20:58,735 INFO   EXIT [b80|lab0080_s210_w1_0928_1005_r1|S210] take_profit (+59.3%) SELL 1 PATH260807C00013500 @<= 0.40
2026-08-04 10:21:00,669 INFO   EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+136.4%) SELL 1 AMZN260805C00287500 @<= 0.76
2026-08-04 10:21:00,940 INFO   EXIT [b58|lab0058_s207_w2_1005_1045_r1|S207] stop_loss (-51.8%) SELL 1 OXY260807C00058000 @<= 0.34

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 391 signal(s); top: ['S165:AMZN', 'S165:DOCN', 'S165:GTLB', 'S165:NKE', 'S165:XOM', 'S165:OXY', 'S164:AMZN', 'S164:DOCN']
Paper lab: $142796 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 117 no tradeable call, 36 already attempted today, 168 open order exists, 136 pending order
Placed 9 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $142,740.54                             |
|  Signals this run              391                                     |
|  Orders submitted (session)    79                                      |
|  Orders filled today (ledger)  91                                      |
|  Entries placed this run       9                                       |
|  Open virtual lots             129                                     |
|  Broker option positions       32                                      |
|  Unattributed contracts        13 (orphan reconcile)                   |
|  Pending orders                20                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=595  buckets=205  win=51%                            |
|  Returns   avg=+32.4%  med=+6.9%  p10=-66.2%  p90=+149.5%              |
|  Realized  $+11,924.24                                                 |
|  Raw incl dropped  trades=1129  real=$+10,328.69                       |
|  Today     trades=40  avg=+31.1%  med=+53.3%  real=$+113.36            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  1 100% +906.2 +906.2 +906.2 $   +145         |
|  b197 lab0197_s218_w3_10  1 100% +737.5 +737.5 +737.5 $   +118         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  2 100% +273.1 +273.1 +273.1 $   +142         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b791 lab0791_s398_w4_11  2 100% +246.8 +246.8 +338.1 $   +254         |
|  b844 lab0844_s407_w2_10  2 100% +245.5 +245.5 +446.1 $    +80         |
|  ... 197 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  2   0% -95.9 -95.9 -95.9 $    -94       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (20)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S203:SMCI(2), S397:AMZN(2), S398:AMZN(2)|
+------------------------------------------------------------------------+
|  b24  S203 SMCI     limit=0.44                                         |
|  b25  S203 SMCI     limit=0.44                                         |
|  b776 S397 AMZN     limit=0.48                                         |
|  b777 S397 AMZN     limit=0.48                                         |
|  b784 S398 AMZN     limit=0.32                                         |
|  ... 15 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b351 S360 AMZN260805C00290000 x1 take_profit (+53.0%)                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (32)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  OXY260807C00058000           20    -51.8%   $   -709.57               |
|  T260807C00023000              6    -38.1%   $   -144.00               |
|  AMZN260805C00287500           3    +93.9%   $    +93.00               |
|  NKE260828C00045000            8    -16.7%   $    -88.00               |
|  AMZN260807C00295000          12    +15.9%   $    +85.78               |
|  PATH260807C00013500           5    +55.6%   $    +75.00               |
|  AMZN260807C00292500           4    +20.8%   $    +53.00               |
|  AMZN260805C00290000           5    +23.1%   $    +34.67               |
|  ... 24 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-04.log
elapsed=114.4s reconcile=0.93s cancel=0.03s manage=6.98s scan=54.67s entries=50.41s
STATUS: options_morning_bot run complete (PAPER) elapsed=114.4s. run=#5978 https://github.com/28twagg-ops/TradingBot/actions/runs/30918391386
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.csv
Summary: 27 buckets closed trades, $+113.36 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 3.2% (36/1129)
# Options signal frequency

_Generated 2026-08-04T10:22:53.763155_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-04
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN | <<<
| Missing exit records (post) |   398 | WARN | <<<
| State/ledger mismatches     |    19 | WARN | <<<
| Total open lots             |   129 | INFO |
| Total closed lots           |   626 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=468.77 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
