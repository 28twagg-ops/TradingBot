# Daily Comprehensive Action Review — 2026-08-11

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260811T004302Z

- UTC timestamp: `20260811T004302Z`
- GitHub run: [#6669](https://github.com/28twagg-ops/TradingBot/actions/runs/31446947999)
- Run id: `31446947999`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-10T20:43:05.632636-04:00","date":"2026-08-10","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.13},"signals":0,"placed":0,"equity":139697.47,"open_positions":23,"pending_orders":0,"open_lots":142,"submitted_today":192,"filled_today":296,"unattributed_contracts":1,"top_signals":[],"github_run":"6669","github_run_id":"31446947999","status":"ok"}
```

### Live bot full output

```text
00:43:03  INFO      Mode: summary
00:43:03  INFO        Daily log -> logs/daily/2026-08-11.md
00:43:03  INFO        Daily log reconciled -> logs/daily/2026-08-11.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         00:43 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.69|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $470.69|
|  Cash                                                           $211.88|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $258.81|
|  Open P&L                                                        $-0.10|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $94.17     $307.55  $307.61  +0.0%   $+0.02  |
|  ADM      Pullback50      $94.17     $80.48   $80.49   +0.0%   $+0.02  |
|  CDW      Pullback50      $70.47     $136.69  $136.43  -0.2%   $-0.14  |
|                                                                        |
|  Total invested                                                 $258.81|
|  Total open P&L                                                  $-0.10|
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
|  2026-08-10  SELL  ALGN  Pullback50  $94.20  P&L $+0.11                |
|  2026-08-10  SELL  GOOGL  Pullback50  $94.10  P&L $-0.05               |
|  2026-08-10  SELL  BBY  Pullback50  $96.71  P&L $+2.25                 |
|  2026-08-10  SELL  AES  Pullback50  $94.56  P&L $+0.13                 |
|  2026-08-10  SELL  ESS  Pullback50  $69.46  P&L $-0.50                 |
|  2026-08-10  SELL  AAPL  Pullback50  $92.77  P&L $-1.69                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=142 paper_keys=yes dry_run=False
  alpaca positions=25
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-10T20:43:05.632636-04:00 ===

[Run context]
After hours (20:43 ET) — exit summary only.
Paper auth OK — equity $139697.47, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $139,697.47                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    192                                     |
|  Orders filled today (ledger)  296                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             142                                     |
|  Broker option positions       23                                      |
|  Unattributed contracts        1 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1717  buckets=311  win=37%                           |
|  Returns   avg=+14.1%  med=-41.4%  p10=-82.2%  p90=+125.8%             |
|  Realized  $+4,545.45                                                  |
|  Raw incl dropped  trades=2251  real=$+2,949.90                        |
|  Today     trades=81  avg=-33.7%  med=-53.5%  real=$-1,895.00          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  lab0091_s210_w6_14  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b281 lab0281_s351_w1_09  5  60% +156.4 +197.9 +346.9 $   +296         |
|  b316 lab0316_s355_w3_10  1 100% +193.8 +193.8 +193.8 $    +93         |
|  ... 303 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b802 lab0802_s404_w2_10  5  40% -37.8 -98.2 -98.4 $   -100       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN MARA260814C00012000 x3 stop_loss (-97.4%)                 |
|  b184 S217 RBLX260814C00041000 x1 stop_loss (-79.8%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (23)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260810C00317500           5   -100.0%   $   -268.75               |
|  AAPL260810C00310000           9   -100.0%   $   -220.50               |
|  TTD260814C00012500           12    +24.1%   $   +196.00               |
|  AAPL260812C00312500          12    +18.5%   $   +146.00               |
|  RBLX260814C00041000           4    -79.8%   $   -142.00               |
|  AAPL260812C00315000          38     -7.7%   $   -124.00               |
|  MARA260814C00012000           3    -97.4%   $   -112.00               |
|  AAPL260817C00320000          13    -12.3%   $   -100.00               |
|  ... 15 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-10.log
elapsed=0.6s reconcile=0.13s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.6s. run=#6669 https://github.com/28twagg-ops/TradingBot/actions/runs/31446947999
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-10_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-10_buckets.csv
Summary: 58 buckets closed trades, $-1,895.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-10_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-10_strategy_selection.csv
Summary: keep=0 watch=85 drop=20
Orphan rate: 11.5% (259/2251) ALERT
# Options signal frequency

_Generated 2026-08-10T20:43:11.969105_

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
## Ledger health — 2026-08-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   560 | WARN | <<<
| Missing exit records (post) |   560 | WARN | <<<
| State/ledger mismatches     |    16 | WARN | <<<
| Total open lots             |   142 | INFO |
| Total closed lots           |  1525 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=470.69 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260811T010221Z

- UTC timestamp: `20260811T010221Z`
- GitHub run: [#6670](https://github.com/28twagg-ops/TradingBot/actions/runs/31447994714)
- Run id: `31447994714`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-10T21:02:25.833347-04:00","date":"2026-08-10","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.1},"signals":0,"placed":0,"equity":139901.47,"open_positions":20,"pending_orders":0,"open_lots":127,"submitted_today":192,"filled_today":296,"unattributed_contracts":1,"top_signals":[],"github_run":"6670","github_run_id":"31447994714","status":"ok"}
```

### Live bot full output

```text
01:02:23  INFO      Mode: summary
01:02:23  INFO        Daily log -> logs/daily/2026-08-11.md
01:02:23  INFO        Daily log reconciled -> logs/daily/2026-08-11.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         01:02 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.74|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $470.74|
|  Cash                                                           $211.88|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $258.86|
|  Open P&L                                                        $-0.05|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $94.22     $307.55  $307.78  +0.1%   $+0.07  |
|  ADM      Pullback50      $94.17     $80.48   $80.49   +0.0%   $+0.02  |
|  CDW      Pullback50      $70.47     $136.69  $136.43  -0.2%   $-0.14  |
|                                                                        |
|  Total invested                                                 $258.86|
|  Total open P&L                                                  $-0.05|
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
|  2026-08-10  SELL  ALGN  Pullback50  $94.20  P&L $+0.11                |
|  2026-08-10  SELL  GOOGL  Pullback50  $94.10  P&L $-0.05               |
|  2026-08-10  SELL  BBY  Pullback50  $96.71  P&L $+2.25                 |
|  2026-08-10  SELL  AES  Pullback50  $94.56  P&L $+0.13                 |
|  2026-08-10  SELL  ESS  Pullback50  $69.46  P&L $-0.50                 |
|  2026-08-10  SELL  AAPL  Pullback50  $92.77  P&L $-1.69                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=142 paper_keys=yes dry_run=False
  alpaca positions=22
  FLAG b109|S212|7dc121b4 missing from Alpaca
  FLAG b347|S359|f2c03e8f missing from Alpaca
  FLAG b346|S359|67a49bb1 missing from Alpaca
  FLAG b345|S359|8073a03c missing from Alpaca
  FLAG b344|S359|45d38b6b missing from Alpaca
  FLAG b108|S212|a3917d88 missing from Alpaca
  FLAG b269|S403|c816951c missing from Alpaca
  FLAG b268|S403|77c410ad missing from Alpaca
  FLAG b170|S216|edae55e4 missing from Alpaca
  FLAG b281|S351|28a6c62f missing from Alpaca
  FLAG b349|S360|724b3674 missing from Alpaca
  FLAG b348|S360|84afc8c8 missing from Alpaca
  FLAG b283|S351|8729f45a missing from Alpaca
  FLAG b282|S351|093e90b6 missing from Alpaca
  FLAG b0|ORPHAN|2ae58f33 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-10T21:02:25.833347-04:00 ===

[Run context]
After hours (21:02 ET) — exit summary only.
Paper auth OK — equity $139901.47, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $139,901.47                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    192                                     |
|  Orders filled today (ledger)  296                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             127                                     |
|  Broker option positions       20                                      |
|  Unattributed contracts        1 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1717  buckets=311  win=37%                           |
|  Returns   avg=+14.1%  med=-41.4%  p10=-82.2%  p90=+125.8%             |
|  Realized  $+4,545.45                                                  |
|  Raw incl dropped  trades=2251  real=$+2,949.90                        |
|  Today     trades=81  avg=-33.7%  med=-53.5%  real=$-1,895.00          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  lab0091_s210_w6_14  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b281 lab0281_s351_w1_09  5  60% +156.4 +197.9 +346.9 $   +296         |
|  b316 lab0316_s355_w3_10  1 100% +193.8 +193.8 +193.8 $    +93         |
|  ... 303 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b802 lab0802_s404_w2_10  5  40% -37.8 -98.2 -98.4 $   -100       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN MARA260814C00012000 x3 stop_loss (-97.4%)                 |
|  b184 S217 RBLX260814C00041000 x1 stop_loss (-79.8%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (20)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  TTD260814C00012500           12    +24.1%   $   +196.00               |
|  AAPL260812C00312500          12    +18.5%   $   +146.00               |
|  RBLX260814C00041000           4    -79.8%   $   -142.00               |
|  AAPL260812C00315000          38     -7.7%   $   -124.00               |
|  MARA260814C00012000           3    -97.4%   $   -112.00               |
|  AAPL260817C00320000          13    -12.3%   $   -100.00               |
|  C260814C00139000              3    -37.7%   $    -78.00               |
|  CELH260814C00028500           8    -44.1%   $    -69.33               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-10.log
elapsed=0.6s reconcile=0.1s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.6s. run=#6670 https://github.com/28twagg-ops/TradingBot/actions/runs/31447994714
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-10_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-10_buckets.csv
Summary: 58 buckets closed trades, $-1,895.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-10_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-10_strategy_selection.csv
Summary: keep=0 watch=85 drop=20
Orphan rate: 11.5% (259/2251) ALERT
# Options signal frequency

_Generated 2026-08-10T21:02:32.093185_

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
## Ledger health — 2026-08-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   560 | WARN | <<<
| Missing exit records (post) |   560 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   127 | INFO |
| Total closed lots           |  1525 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=470.74 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260811T030752Z

- UTC timestamp: `20260811T030752Z`
- GitHub run: [#6671](https://github.com/28twagg-ops/TradingBot/actions/runs/31454439539)
- Run id: `31454439539`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-10T23:07:56.501024-04:00","date":"2026-08-10","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.22},"signals":0,"placed":0,"equity":140097.47,"open_positions":20,"pending_orders":0,"open_lots":127,"submitted_today":192,"filled_today":296,"unattributed_contracts":1,"top_signals":[],"github_run":"6671","github_run_id":"31454439539","status":"ok"}
```

### Live bot full output

```text
03:07:53  INFO      Mode: summary
03:07:54  INFO        Daily log -> logs/daily/2026-08-11.md
03:07:54  INFO        Daily log reconciled -> logs/daily/2026-08-11.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         03:07 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.10|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $471.10|
|  Cash                                                           $211.88|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $259.22|
|  Open P&L                                                        $+0.31|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $94.58     $307.55  $308.95  +0.5%   $+0.43  |
|  ADM      Pullback50      $94.17     $80.48   $80.49   +0.0%   $+0.02  |
|  CDW      Pullback50      $70.47     $136.69  $136.43  -0.2%   $-0.14  |
|                                                                        |
|  Total invested                                                 $259.22|
|  Total open P&L                                                  $+0.31|
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
|  2026-08-10  SELL  ALGN  Pullback50  $94.20  P&L $+0.11                |
|  2026-08-10  SELL  GOOGL  Pullback50  $94.10  P&L $-0.05               |
|  2026-08-10  SELL  BBY  Pullback50  $96.71  P&L $+2.25                 |
|  2026-08-10  SELL  AES  Pullback50  $94.56  P&L $+0.13                 |
|  2026-08-10  SELL  ESS  Pullback50  $69.46  P&L $-0.50                 |
|  2026-08-10  SELL  AAPL  Pullback50  $92.77  P&L $-1.69                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=127 paper_keys=yes dry_run=False
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-10T23:07:56.501024-04:00 ===

[Run context]
After hours (23:07 ET) — exit summary only.
Paper auth OK — equity $140097.47, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $140,097.47                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    192                                     |
|  Orders filled today (ledger)  296                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             127                                     |
|  Broker option positions       20                                      |
|  Unattributed contracts        1 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1717  buckets=311  win=37%                           |
|  Returns   avg=+14.1%  med=-41.4%  p10=-82.2%  p90=+125.8%             |
|  Realized  $+4,545.45                                                  |
|  Raw incl dropped  trades=2251  real=$+2,949.90                        |
|  Today     trades=81  avg=-33.7%  med=-53.5%  real=$-1,895.00          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  lab0091_s210_w6_14  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b281 lab0281_s351_w1_09  5  60% +156.4 +197.9 +346.9 $   +296         |
|  b316 lab0316_s355_w3_10  1 100% +193.8 +193.8 +193.8 $    +93         |
|  ... 303 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b802 lab0802_s404_w2_10  5  40% -37.8 -98.2 -98.4 $   -100       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN MARA260814C00012000 x3 stop_loss (-97.4%)                 |
|  b184 S217 RBLX260814C00041000 x1 stop_loss (-79.8%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (20)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  TTD260814C00012500           12    +24.1%   $   +196.00               |
|  AAPL260812C00312500          12    +18.5%   $   +146.00               |
|  RBLX260814C00041000           4    -79.8%   $   -142.00               |
|  AAPL260812C00315000          38     -7.7%   $   -124.00               |
|  MARA260814C00012000           3    -97.4%   $   -112.00               |
|  AAPL260817C00320000          13    -12.3%   $   -100.00               |
|  C260814C00139000              3    -37.7%   $    -78.00               |
|  CELH260814C00028500           8    -44.1%   $    -69.33               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-10.log
elapsed=0.8s reconcile=0.22s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.8s. run=#6671 https://github.com/28twagg-ops/TradingBot/actions/runs/31454439539
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-10_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-10_buckets.csv
Summary: 58 buckets closed trades, $-1,895.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-10_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-10_strategy_selection.csv
Summary: keep=0 watch=85 drop=20
Orphan rate: 11.5% (259/2251) ALERT
# Options signal frequency

_Generated 2026-08-10T23:08:03.037950_

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
## Ledger health — 2026-08-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   560 | WARN | <<<
| Missing exit records (post) |   560 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   127 | INFO |
| Total closed lots           |  1525 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.1 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260811T130059Z

- UTC timestamp: `20260811T130059Z`
- GitHub run: [#6672](https://github.com/28twagg-ops/TradingBot/actions/runs/31493947990)
- Run id: `31493947990`
- Live bot: exit=`0`, duration=`5s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-11T09:01:06.231395-04:00","date":"2026-08-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.19},"signals":0,"placed":0,"equity":140300.84,"open_positions":20,"pending_orders":0,"open_lots":127,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"6672","github_run_id":"31493947990","status":"ok"}
```

### Live bot full output

```text
13:01:00  INFO      Mode: summary
13:01:04  INFO        Daily log -> logs/daily/2026-08-11.md
13:01:04  INFO        Daily log reconciled -> logs/daily/2026-08-11.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.02|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $471.02|
|  Cash                                                           $211.88|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $259.14|
|  Open P&L                                                        $+0.23|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $94.38     $307.55  $308.30  +0.2%   $+0.23  |
|  ADM      Pullback50      $94.28     $80.48   $80.59   +0.1%   $+0.13  |
|  CDW      Pullback50      $70.47     $136.69  $136.43  -0.2%   $-0.14  |
|                                                                        |
|  Total invested                                                 $259.14|
|  Total open P&L                                                  $+0.23|
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
|  2026-08-10  SELL  ALGN  Pullback50  $94.20  P&L $+0.11                |
|  2026-08-10  SELL  GOOGL  Pullback50  $94.10  P&L $-0.05               |
|  2026-08-10  SELL  BBY  Pullback50  $96.71  P&L $+2.25                 |
|  2026-08-10  SELL  AES  Pullback50  $94.56  P&L $+0.13                 |
|  2026-08-10  SELL  ESS  Pullback50  $69.46  P&L $-0.50                 |
|  2026-08-10  SELL  AAPL  Pullback50  $92.77  P&L $-1.69                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=127 paper_keys=yes dry_run=False
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-11T09:01:06.231395-04:00 ===

[Run context]
After hours (09:01 ET) — exit summary only.
Paper auth OK — equity $140300.84, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $140,300.84                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             127                                     |
|  Broker option positions       20                                      |
|  Unattributed contracts        1 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1717  buckets=311  win=37%                           |
|  Returns   avg=+14.1%  med=-41.4%  p10=-82.2%  p90=+125.8%             |
|  Realized  $+4,545.45                                                  |
|  Raw incl dropped  trades=2251  real=$+2,949.90                        |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  lab0091_s210_w6_14  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b281 lab0281_s351_w1_09  5  60% +156.4 +197.9 +346.9 $   +296         |
|  b316 lab0316_s355_w3_10  1 100% +193.8 +193.8 +193.8 $    +93         |
|  ... 303 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b802 lab0802_s404_w2_10  5  40% -37.8 -98.2 -98.4 $   -100       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN MARA260814C00012000 x3 stop_loss (-97.4%)                 |
|  b184 S217 RBLX260814C00041000 x1 stop_loss (-79.8%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (20)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  TTD260814C00012500           12    +24.1%   $   +196.00               |
|  AAPL260812C00312500          12    +18.5%   $   +146.00               |
|  RBLX260814C00041000           4    -79.8%   $   -142.00               |
|  AAPL260812C00315000          38     -7.7%   $   -124.00               |
|  MARA260814C00012000           3    -97.4%   $   -112.00               |
|  AAPL260817C00320000          13    -12.3%   $   -100.00               |
|  C260814C00139000              3    -37.7%   $    -78.00               |
|  CELH260814C00028500           8    -44.1%   $    -69.33               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-11.log
elapsed=0.7s reconcile=0.19s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.7s. run=#6672 https://github.com/28twagg-ops/TradingBot/actions/runs/31493947990
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.csv
Summary: keep=0 watch=85 drop=20
Orphan rate: 11.5% (259/2251) ALERT
# Options signal frequency

_Generated 2026-08-11T09:01:12.661361_

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
## Ledger health — 2026-08-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   591 | WARN | <<<
| Missing exit records (post) |   591 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   127 | INFO |
| Total closed lots           |  1525 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.02 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260811T130559Z

- UTC timestamp: `20260811T130559Z`
- GitHub run: [#6674](https://github.com/28twagg-ops/TradingBot/actions/runs/31494362207)
- Run id: `31494362207`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-11T09:06:03.585234-04:00","date":"2026-08-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.5},"signals":0,"placed":0,"equity":140120.08,"open_positions":20,"pending_orders":0,"open_lots":127,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"6674","github_run_id":"31494362207","status":"ok"}
```

### Live bot full output

```text
13:06:00  INFO      Mode: summary
13:06:01  INFO        Daily log -> logs/daily/2026-08-11.md
13:06:01  INFO        Daily log reconciled -> logs/daily/2026-08-11.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.00|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $471.00|
|  Cash                                                           $211.88|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $259.12|
|  Open P&L                                                        $+0.21|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $94.37     $307.55  $308.25  +0.2%   $+0.22  |
|  ADM      Pullback50      $94.28     $80.48   $80.59   +0.1%   $+0.13  |
|  CDW      Pullback50      $70.47     $136.69  $136.43  -0.2%   $-0.14  |
|                                                                        |
|  Total invested                                                 $259.12|
|  Total open P&L                                                  $+0.21|
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
|  2026-08-10  SELL  ALGN  Pullback50  $94.20  P&L $+0.11                |
|  2026-08-10  SELL  GOOGL  Pullback50  $94.10  P&L $-0.05               |
|  2026-08-10  SELL  BBY  Pullback50  $96.71  P&L $+2.25                 |
|  2026-08-10  SELL  AES  Pullback50  $94.56  P&L $+0.13                 |
|  2026-08-10  SELL  ESS  Pullback50  $69.46  P&L $-0.50                 |
|  2026-08-10  SELL  AAPL  Pullback50  $92.77  P&L $-1.69                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=127 paper_keys=yes dry_run=False
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-11T09:06:03.585234-04:00 ===

[Run context]
After hours (09:06 ET) — exit summary only.
Paper auth OK — equity $140120.08, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $140,120.08                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             127                                     |
|  Broker option positions       20                                      |
|  Unattributed contracts        1 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1717  buckets=311  win=37%                           |
|  Returns   avg=+14.1%  med=-41.4%  p10=-82.2%  p90=+125.8%             |
|  Realized  $+4,545.45                                                  |
|  Raw incl dropped  trades=2251  real=$+2,949.90                        |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  lab0091_s210_w6_14  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b281 lab0281_s351_w1_09  5  60% +156.4 +197.9 +346.9 $   +296         |
|  b316 lab0316_s355_w3_10  1 100% +193.8 +193.8 +193.8 $    +93         |
|  ... 303 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b802 lab0802_s404_w2_10  5  40% -37.8 -98.2 -98.4 $   -100       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN MARA260814C00012000 x3 stop_loss (-97.4%)                 |
|  b184 S217 RBLX260814C00041000 x1 stop_loss (-79.8%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (20)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  TTD260814C00012500           12    +24.1%   $   +196.00               |
|  AAPL260812C00312500          12    +18.5%   $   +146.00               |
|  RBLX260814C00041000           4    -79.8%   $   -142.00               |
|  AAPL260812C00315000          38     -7.7%   $   -124.00               |
|  MARA260814C00012000           3    -97.4%   $   -112.00               |
|  AAPL260817C00320000          13    -12.3%   $   -100.00               |
|  C260814C00139000              3    -37.7%   $    -78.00               |
|  CELH260814C00028500           8    -44.1%   $    -69.33               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-11.log
elapsed=1.2s reconcile=0.5s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.2s. run=#6674 https://github.com/28twagg-ops/TradingBot/actions/runs/31494362207
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.csv
Summary: keep=0 watch=85 drop=20
Orphan rate: 11.5% (259/2251) ALERT
# Options signal frequency

_Generated 2026-08-11T09:06:10.505402_

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
## Ledger health — 2026-08-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   591 | WARN | <<<
| Missing exit records (post) |   591 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   127 | INFO |
| Total closed lots           |  1525 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.0 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260811T131055Z

- UTC timestamp: `20260811T131055Z`
- GitHub run: [#6675](https://github.com/28twagg-ops/TradingBot/actions/runs/31494783350)
- Run id: `31494783350`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`11s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-11T09:11:01.029439-04:00","date":"2026-08-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.61},"signals":0,"placed":0,"equity":140188.08,"open_positions":20,"pending_orders":0,"open_lots":127,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"6675","github_run_id":"31494783350","status":"ok"}
```

### Live bot full output

```text
13:10:57  INFO      Mode: summary
13:10:58  INFO        Daily log -> logs/daily/2026-08-11.md
13:10:58  INFO        Daily log reconciled -> logs/daily/2026-08-11.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.90|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $470.90|
|  Cash                                                           $211.88|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $259.02|
|  Open P&L                                                        $+0.11|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $94.26     $307.55  $307.90  +0.1%   $+0.11  |
|  ADM      Pullback50      $94.28     $80.48   $80.59   +0.1%   $+0.13  |
|  CDW      Pullback50      $70.47     $136.69  $136.43  -0.2%   $-0.14  |
|                                                                        |
|  Total invested                                                 $259.02|
|  Total open P&L                                                  $+0.11|
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
|  2026-08-10  SELL  ALGN  Pullback50  $94.20  P&L $+0.11                |
|  2026-08-10  SELL  GOOGL  Pullback50  $94.10  P&L $-0.05               |
|  2026-08-10  SELL  BBY  Pullback50  $96.71  P&L $+2.25                 |
|  2026-08-10  SELL  AES  Pullback50  $94.56  P&L $+0.13                 |
|  2026-08-10  SELL  ESS  Pullback50  $69.46  P&L $-0.50                 |
|  2026-08-10  SELL  AAPL  Pullback50  $92.77  P&L $-1.69                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=127 paper_keys=yes dry_run=False
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-11T09:11:01.029439-04:00 ===

[Run context]
After hours (09:11 ET) — exit summary only.
Paper auth OK — equity $140188.08, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $140,188.08                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             127                                     |
|  Broker option positions       20                                      |
|  Unattributed contracts        1 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1717  buckets=311  win=37%                           |
|  Returns   avg=+14.1%  med=-41.4%  p10=-82.2%  p90=+125.8%             |
|  Realized  $+4,545.45                                                  |
|  Raw incl dropped  trades=2251  real=$+2,949.90                        |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  lab0091_s210_w6_14  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b281 lab0281_s351_w1_09  5  60% +156.4 +197.9 +346.9 $   +296         |
|  b316 lab0316_s355_w3_10  1 100% +193.8 +193.8 +193.8 $    +93         |
|  ... 303 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b802 lab0802_s404_w2_10  5  40% -37.8 -98.2 -98.4 $   -100       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN MARA260814C00012000 x3 stop_loss (-97.4%)                 |
|  b184 S217 RBLX260814C00041000 x1 stop_loss (-79.8%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (20)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  TTD260814C00012500           12    +24.1%   $   +196.00               |
|  AAPL260812C00312500          12    +18.5%   $   +146.00               |
|  RBLX260814C00041000           4    -79.8%   $   -142.00               |
|  AAPL260812C00315000          38     -7.7%   $   -124.00               |
|  MARA260814C00012000           3    -97.4%   $   -112.00               |
|  AAPL260817C00320000          13    -12.3%   $   -100.00               |
|  C260814C00139000              3    -37.7%   $    -78.00               |
|  CELH260814C00028500           8    -44.1%   $    -69.33               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-11.log
elapsed=1.3s reconcile=0.61s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.3s. run=#6675 https://github.com/28twagg-ops/TradingBot/actions/runs/31494783350
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.csv
Summary: keep=0 watch=85 drop=20
Orphan rate: 11.5% (259/2251) ALERT
# Options signal frequency

_Generated 2026-08-11T09:11:08.227457_

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
## Ledger health — 2026-08-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   591 | WARN | <<<
| Missing exit records (post) |   591 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   127 | INFO |
| Total closed lots           |  1525 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=470.9 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260811T131551Z

- UTC timestamp: `20260811T131551Z`
- GitHub run: [#6676](https://github.com/28twagg-ops/TradingBot/actions/runs/31495210237)
- Run id: `31495210237`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-11T09:15:55.013469-04:00","date":"2026-08-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.51},"signals":0,"placed":0,"equity":139460.2,"open_positions":20,"pending_orders":0,"open_lots":127,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"6676","github_run_id":"31495210237","status":"ok"}
```

### Live bot full output

```text
13:15:52  INFO      Mode: summary
13:15:52  INFO        Daily log -> logs/daily/2026-08-11.md
13:15:52  INFO        Daily log reconciled -> logs/daily/2026-08-11.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.83|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $470.83|
|  Cash                                                           $211.88|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $258.95|
|  Open P&L                                                        $+0.04|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $94.19     $307.55  $307.69  +0.0%   $+0.04  |
|  ADM      Pullback50      $94.28     $80.48   $80.59   +0.1%   $+0.13  |
|  CDW      Pullback50      $70.47     $136.69  $136.43  -0.2%   $-0.14  |
|                                                                        |
|  Total invested                                                 $258.95|
|  Total open P&L                                                  $+0.04|
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
|  2026-08-10  SELL  ALGN  Pullback50  $94.20  P&L $+0.11                |
|  2026-08-10  SELL  GOOGL  Pullback50  $94.10  P&L $-0.05               |
|  2026-08-10  SELL  BBY  Pullback50  $96.71  P&L $+2.25                 |
|  2026-08-10  SELL  AES  Pullback50  $94.56  P&L $+0.13                 |
|  2026-08-10  SELL  ESS  Pullback50  $69.46  P&L $-0.50                 |
|  2026-08-10  SELL  AAPL  Pullback50  $92.77  P&L $-1.69                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=127 paper_keys=yes dry_run=False
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-11T09:15:55.013469-04:00 ===

[Run context]
After hours (09:15 ET) — exit summary only.
Paper auth OK — equity $139460.20, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $139,460.20                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             127                                     |
|  Broker option positions       20                                      |
|  Unattributed contracts        1 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1717  buckets=311  win=37%                           |
|  Returns   avg=+14.1%  med=-41.4%  p10=-82.2%  p90=+125.8%             |
|  Realized  $+4,545.45                                                  |
|  Raw incl dropped  trades=2251  real=$+2,949.90                        |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  lab0091_s210_w6_14  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b281 lab0281_s351_w1_09  5  60% +156.4 +197.9 +346.9 $   +296         |
|  b316 lab0316_s355_w3_10  1 100% +193.8 +193.8 +193.8 $    +93         |
|  ... 303 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b802 lab0802_s404_w2_10  5  40% -37.8 -98.2 -98.4 $   -100       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN MARA260814C00012000 x3 stop_loss (-97.4%)                 |
|  b184 S217 RBLX260814C00041000 x1 stop_loss (-79.8%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (20)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  TTD260814C00012500           12    +24.1%   $   +196.00               |
|  AAPL260812C00312500          12    +18.5%   $   +146.00               |
|  RBLX260814C00041000           4    -79.8%   $   -142.00               |
|  AAPL260812C00315000          38     -7.7%   $   -124.00               |
|  MARA260814C00012000           3    -97.4%   $   -112.00               |
|  AAPL260817C00320000          13    -12.3%   $   -100.00               |
|  C260814C00139000              3    -37.7%   $    -78.00               |
|  CELH260814C00028500           8    -44.1%   $    -69.33               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-11.log
elapsed=1.2s reconcile=0.51s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.2s. run=#6676 https://github.com/28twagg-ops/TradingBot/actions/runs/31495210237
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.csv
Summary: keep=0 watch=85 drop=20
Orphan rate: 11.5% (259/2251) ALERT
# Options signal frequency

_Generated 2026-08-11T09:16:01.980750_

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
## Ledger health — 2026-08-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   591 | WARN | <<<
| Missing exit records (post) |   591 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   127 | INFO |
| Total closed lots           |  1525 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=470.83 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260811T132050Z

- UTC timestamp: `20260811T132050Z`
- GitHub run: [#6677](https://github.com/28twagg-ops/TradingBot/actions/runs/31495627154)
- Run id: `31495627154`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-11T09:20:53.601102-04:00","date":"2026-08-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.28},"signals":0,"placed":0,"equity":140399.28,"open_positions":20,"pending_orders":0,"open_lots":127,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"6677","github_run_id":"31495627154","status":"ok"}
```

### Live bot full output

```text
13:20:50  INFO      Mode: summary
13:20:51  INFO        Daily log -> logs/daily/2026-08-11.md
13:20:51  INFO        Daily log reconciled -> logs/daily/2026-08-11.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.71|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $470.71|
|  Cash                                                           $211.88|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $258.83|
|  Open P&L                                                        $-0.08|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $94.24     $307.55  $307.85  +0.1%   $+0.09  |
|  ADM      Pullback50      $94.28     $80.48   $80.59   +0.1%   $+0.13  |
|  CDW      Pullback50      $70.30     $136.69  $136.10  -0.4%   $-0.31  |
|                                                                        |
|  Total invested                                                 $258.83|
|  Total open P&L                                                  $-0.08|
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
|  2026-08-10  SELL  ALGN  Pullback50  $94.20  P&L $+0.11                |
|  2026-08-10  SELL  GOOGL  Pullback50  $94.10  P&L $-0.05               |
|  2026-08-10  SELL  BBY  Pullback50  $96.71  P&L $+2.25                 |
|  2026-08-10  SELL  AES  Pullback50  $94.56  P&L $+0.13                 |
|  2026-08-10  SELL  ESS  Pullback50  $69.46  P&L $-0.50                 |
|  2026-08-10  SELL  AAPL  Pullback50  $92.77  P&L $-1.69                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=127 paper_keys=yes dry_run=False
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-11T09:20:53.601102-04:00 ===

[Run context]
After hours (09:20 ET) — exit summary only.
Paper auth OK — equity $140399.28, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $140,399.28                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             127                                     |
|  Broker option positions       20                                      |
|  Unattributed contracts        1 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1717  buckets=311  win=37%                           |
|  Returns   avg=+14.1%  med=-41.4%  p10=-82.2%  p90=+125.8%             |
|  Realized  $+4,545.45                                                  |
|  Raw incl dropped  trades=2251  real=$+2,949.90                        |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  lab0091_s210_w6_14  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b281 lab0281_s351_w1_09  5  60% +156.4 +197.9 +346.9 $   +296         |
|  b316 lab0316_s355_w3_10  1 100% +193.8 +193.8 +193.8 $    +93         |
|  ... 303 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b802 lab0802_s404_w2_10  5  40% -37.8 -98.2 -98.4 $   -100       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN MARA260814C00012000 x3 stop_loss (-97.4%)                 |
|  b184 S217 RBLX260814C00041000 x1 stop_loss (-79.8%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (20)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  TTD260814C00012500           12    +24.1%   $   +196.00               |
|  AAPL260812C00312500          12    +18.5%   $   +146.00               |
|  RBLX260814C00041000           4    -79.8%   $   -142.00               |
|  AAPL260812C00315000          38     -7.7%   $   -124.00               |
|  MARA260814C00012000           3    -97.4%   $   -112.00               |
|  AAPL260817C00320000          13    -12.3%   $   -100.00               |
|  C260814C00139000              3    -37.7%   $    -78.00               |
|  CELH260814C00028500           8    -44.1%   $    -69.33               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-11.log
elapsed=0.9s reconcile=0.28s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.9s. run=#6677 https://github.com/28twagg-ops/TradingBot/actions/runs/31495627154
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.csv
Summary: keep=0 watch=85 drop=20
Orphan rate: 11.5% (259/2251) ALERT
# Options signal frequency

_Generated 2026-08-11T09:21:00.079868_

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
## Ledger health — 2026-08-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   591 | WARN | <<<
| Missing exit records (post) |   591 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   127 | INFO |
| Total closed lots           |  1525 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=470.71 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260811T132545Z

- UTC timestamp: `20260811T132545Z`
- GitHub run: [#6678](https://github.com/28twagg-ops/TradingBot/actions/runs/31496048357)
- Run id: `31496048357`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-11T09:25:49.736216-04:00","date":"2026-08-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.67},"signals":0,"placed":0,"equity":140246.92,"open_positions":20,"pending_orders":0,"open_lots":127,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"6678","github_run_id":"31496048357","status":"ok"}
```

### Live bot full output

```text
13:25:46  INFO      Mode: summary
13:25:47  INFO        Daily log -> logs/daily/2026-08-11.md
13:25:47  INFO        Daily log reconciled -> logs/daily/2026-08-11.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.91|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $470.91|
|  Cash                                                           $211.88|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $259.03|
|  Open P&L                                                        $+0.12|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $94.29     $307.55  $308.00  +0.1%   $+0.14  |
|  ADM      Pullback50      $94.28     $80.48   $80.59   +0.1%   $+0.13  |
|  CDW      Pullback50      $70.46     $136.69  $136.40  -0.2%   $-0.15  |
|                                                                        |
|  Total invested                                                 $259.03|
|  Total open P&L                                                  $+0.12|
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
|  2026-08-10  SELL  ALGN  Pullback50  $94.20  P&L $+0.11                |
|  2026-08-10  SELL  GOOGL  Pullback50  $94.10  P&L $-0.05               |
|  2026-08-10  SELL  BBY  Pullback50  $96.71  P&L $+2.25                 |
|  2026-08-10  SELL  AES  Pullback50  $94.56  P&L $+0.13                 |
|  2026-08-10  SELL  ESS  Pullback50  $69.46  P&L $-0.50                 |
|  2026-08-10  SELL  AAPL  Pullback50  $92.77  P&L $-1.69                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=127 paper_keys=yes dry_run=False
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-11T09:25:49.736216-04:00 ===

[Run context]
After hours (09:25 ET) — exit summary only.
Paper auth OK — equity $140246.92, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $140,246.92                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             127                                     |
|  Broker option positions       20                                      |
|  Unattributed contracts        1 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1717  buckets=311  win=37%                           |
|  Returns   avg=+14.1%  med=-41.4%  p10=-82.2%  p90=+125.8%             |
|  Realized  $+4,545.45                                                  |
|  Raw incl dropped  trades=2251  real=$+2,949.90                        |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  lab0091_s210_w6_14  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b281 lab0281_s351_w1_09  5  60% +156.4 +197.9 +346.9 $   +296         |
|  b316 lab0316_s355_w3_10  1 100% +193.8 +193.8 +193.8 $    +93         |
|  ... 303 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b802 lab0802_s404_w2_10  5  40% -37.8 -98.2 -98.4 $   -100       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN MARA260814C00012000 x3 stop_loss (-97.4%)                 |
|  b184 S217 RBLX260814C00041000 x1 stop_loss (-79.8%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (20)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  TTD260814C00012500           12    +24.1%   $   +196.00               |
|  AAPL260812C00312500          12    +18.5%   $   +146.00               |
|  RBLX260814C00041000           4    -79.8%   $   -142.00               |
|  AAPL260812C00315000          38     -7.7%   $   -124.00               |
|  MARA260814C00012000           3    -97.4%   $   -112.00               |
|  AAPL260817C00320000          13    -12.3%   $   -100.00               |
|  C260814C00139000              3    -37.7%   $    -78.00               |
|  CELH260814C00028500           8    -44.1%   $    -69.33               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-11.log
elapsed=1.3s reconcile=0.67s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.3s. run=#6678 https://github.com/28twagg-ops/TradingBot/actions/runs/31496048357
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.csv
Summary: keep=0 watch=85 drop=20
Orphan rate: 11.5% (259/2251) ALERT
# Options signal frequency

_Generated 2026-08-11T09:25:56.718009_

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
## Ledger health — 2026-08-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   591 | WARN | <<<
| Missing exit records (post) |   591 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   127 | INFO |
| Total closed lots           |  1525 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=470.91 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260811T133101Z

- UTC timestamp: `20260811T133101Z`
- GitHub run: [#6679](https://github.com/28twagg-ops/TradingBot/actions/runs/31496481684)
- Run id: `31496481684`
- Live bot: exit=`0`, duration=`219s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-11T09:25:49.736216-04:00","date":"2026-08-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.67},"signals":0,"placed":0,"equity":140246.92,"open_positions":20,"pending_orders":0,"open_lots":127,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"6678","github_run_id":"31496048357","status":"ok"}
```

### Live bot full output

```text
13:31:03  INFO      Mode: morning_prep
13:31:05  INFO        [prep_positions] 5/5 (5 valid)
13:31:05  INFO      Fetching tickers (universe=both)...
13:31:05  INFO        S&P 500: 503
13:31:06  INFO        MidCap 400: 400
13:31:06  INFO        Total: 903 tickers
13:31:07  INFO        [prep_universe] 40/898 (40 valid)
13:31:09  INFO        [prep_universe] 80/898 (80 valid)
13:31:10  INFO        [prep_universe] 120/898 (120 valid)
13:31:13  INFO        [prep_universe] 160/898 (160 valid)
13:31:14  INFO        [prep_universe] 200/898 (199 valid)
13:31:19  INFO        [prep_universe] 240/898 (238 valid)
13:31:33  INFO        [prep_universe] 280/898 (278 valid)
13:31:43  INFO        [prep_universe] 320/898 (318 valid)
13:31:55  INFO        [prep_universe] 360/898 (358 valid)
13:32:08  INFO        [prep_universe] 400/898 (397 valid)
13:32:19  INFO        [prep_universe] 440/898 (437 valid)
13:32:32  INFO        [prep_universe] 480/898 (477 valid)
13:32:42  INFO        [prep_universe] 520/898 (517 valid)
13:32:55  INFO        [prep_universe] 560/898 (557 valid)
13:33:06  INFO        [prep_universe] 600/898 (597 valid)
13:33:19  INFO        [prep_universe] 640/898 (637 valid)
13:33:30  INFO        [prep_universe] 680/898 (677 valid)
13:33:44  INFO        [prep_universe] 720/898 (717 valid)
13:33:57  INFO        [prep_universe] 760/898 (757 valid)
13:34:08  INFO        [prep_universe] 800/898 (797 valid)
13:34:21  INFO        [prep_universe] 840/898 (836 valid)
13:34:31  INFO        [prep_universe] 880/898 (876 valid)
13:34:38  INFO        [prep_universe] 898/898 (894 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.35|
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
|  Open positions                                                       5|
|  Invested                                                       $446.66|
|  Open P&L                                                        $-0.43|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $94.80     $307.55  $309.68  +0.7%   $+0.65  |
|  ADM      Pullback50      $94.20     $80.48   $80.52   +0.1%   $+0.05  |
|  AES      Pullback50      $94.12     $14.72   $14.72   +0.0%   $+0.03  |
|  CDW      Pullback50      $69.77     $136.69  $135.06  -1.2%   $-0.84  |
|  GOOG     Pullback50      $93.77     $354.24  $353.04  -0.3%   $-0.32  |
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
|  Signal candidates                                                   41|
|  Universe scanned                                                   898|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=127 paper_keys=yes dry_run=False
  alpaca positions=21
  FLAG b0|ORPHAN|3e0808db missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-11T09:34:42.503708-04:00 ===

[Run context]
Paper auth OK — equity $138309.99, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-11 09:34:46,249 INFO   EXIT [b814|lab0814_s405_w1_0928_1005_r1|S405] stop_loss (-100.0%) SELL 1 CELH260814C00028500 @<= 0.01
  EXIT [b111|lab0111_s212_w2_1005_1045_r2|S212] stop_loss (-62.1%) SELL failed QQQ260813C00740000: {"code":40010001,"message":"client_order_id must be unique"}
  EXIT [b185|lab0185_s217_w4_1120_1135_r2|S217] stop_loss (-77.5%) SELL failed RBLX260814C00041000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-11 09:34:51,648 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-77.5%) SELL 2 RBLX260814C00041000 @<= 0.11

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260811T133616Z

- UTC timestamp: `20260811T133616Z`
- GitHub run: [#6680](https://github.com/28twagg-ops/TradingBot/actions/runs/31496927582)
- Run id: `31496927582`
- Live bot: exit=`0`, duration=`216s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-11T09:25:49.736216-04:00","date":"2026-08-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.67},"signals":0,"placed":0,"equity":140246.92,"open_positions":20,"pending_orders":0,"open_lots":127,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"6678","github_run_id":"31496048357","status":"ok"}
```

### Live bot full output

```text
13:36:17  INFO      Mode: morning_prep
13:36:19  INFO        [prep_positions] 5/5 (5 valid)
13:36:19  INFO      Fetching tickers (universe=both)...
13:36:20  INFO        S&P 500: 503
13:36:20  INFO        MidCap 400: 400
13:36:20  INFO        Total: 903 tickers
13:36:21  INFO        [prep_universe] 40/898 (40 valid)
13:36:22  INFO        [prep_universe] 80/898 (80 valid)
13:36:24  INFO        [prep_universe] 120/898 (120 valid)
13:36:25  INFO        [prep_universe] 160/898 (160 valid)
13:36:27  INFO        [prep_universe] 200/898 (199 valid)
13:36:34  INFO        [prep_universe] 240/898 (238 valid)
13:36:45  INFO        [prep_universe] 280/898 (278 valid)
13:36:59  INFO        [prep_universe] 320/898 (318 valid)
13:37:09  INFO        [prep_universe] 360/898 (358 valid)
13:37:23  INFO        [prep_universe] 400/898 (397 valid)
13:37:33  INFO        [prep_universe] 440/898 (437 valid)
13:37:47  INFO        [prep_universe] 480/898 (477 valid)
13:37:57  INFO        [prep_universe] 520/898 (517 valid)
13:38:08  INFO        [prep_universe] 560/898 (557 valid)
13:38:22  INFO        [prep_universe] 600/898 (597 valid)
13:38:32  INFO        [prep_universe] 640/898 (637 valid)
13:38:46  INFO        [prep_universe] 680/898 (677 valid)
13:38:59  INFO        [prep_universe] 720/898 (717 valid)
13:39:09  INFO        [prep_universe] 760/898 (757 valid)
13:39:23  INFO        [prep_universe] 800/898 (797 valid)
13:39:33  INFO        [prep_universe] 840/898 (836 valid)
13:39:47  INFO        [prep_universe] 880/898 (876 valid)
13:39:50  INFO        [prep_universe] 898/898 (894 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $469.48|
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
|  Open positions                                                       5|
|  Invested                                                       $445.65|
|  Open P&L                                                        $-1.44|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $94.10     $307.55  $307.39  -0.1%   $-0.05  |
|  ADM      Pullback50      $94.00     $80.48   $80.35   -0.2%   $-0.15  |
|  AES      Pullback50      $94.15     $14.72   $14.73   +0.1%   $+0.06  |
|  CDW      Pullback50      $70.01     $136.69  $135.54  -0.8%   $-0.60  |
|  GOOG     Pullback50      $93.38     $354.24  $351.56  -0.8%   $-0.71  |
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
|  Signal candidates                                                   48|
|  Universe scanned                                                   898|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=127 paper_keys=yes dry_run=False
  alpaca positions=21
  FLAG b0|ORPHAN|3e0808db missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-11T09:39:54.725415-04:00 ===

[Run context]
Paper auth OK — equity $135932.99, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-11 09:40:00,015 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-63.6%) SELL 1 AAPL260812C00320000 @<= 0.01
2026-08-11 09:40:02,614 INFO   EXIT [b829|lab0829_s406_w1_0928_1005_r2|S406] stop_loss (-64.0%) SELL 1 AAPL260812C00317500 @<= 0.09
  EXIT [b111|lab0111_s212_w2_1005_1045_r2|S212] stop_loss (-63.8%) SELL failed QQQ260813C00740000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-11 09:40:14,126 INFO   EXIT [b817|lab0817_s405_w2_1005_1045_r2|S405] stop_loss (-55.0%) SELL 1 AAPL260812C00315000 @<= 0.19

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
```

---

## Run 20260811T134127Z

- UTC timestamp: `20260811T134127Z`
- GitHub run: [#6681](https://github.com/28twagg-ops/TradingBot/actions/runs/31497364886)
- Run id: `31497364886`
- Live bot: exit=`0`, duration=`216s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-11T09:25:49.736216-04:00","date":"2026-08-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.67},"signals":0,"placed":0,"equity":140246.92,"open_positions":20,"pending_orders":0,"open_lots":127,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"6678","github_run_id":"31496048357","status":"ok"}
```

### Live bot full output

```text
13:41:28  INFO      Mode: morning_prep
13:41:30  INFO        [prep_positions] 5/5 (5 valid)
13:41:30  INFO        Universe cache hit: 903 tickers (tickers_2026-08-11.json)
13:41:31  INFO        [prep_universe] 40/898 (40 valid)
13:41:32  INFO        [prep_universe] 80/898 (80 valid)
13:41:34  INFO        [prep_universe] 120/898 (120 valid)
13:41:35  INFO        [prep_universe] 160/898 (160 valid)
13:41:36  INFO        [prep_universe] 200/898 (199 valid)
13:41:43  INFO        [prep_universe] 240/898 (238 valid)
13:41:57  INFO        [prep_universe] 280/898 (278 valid)
13:42:07  INFO        [prep_universe] 320/898 (318 valid)
13:42:21  INFO        [prep_universe] 360/898 (358 valid)
13:42:31  INFO        [prep_universe] 400/898 (397 valid)
13:42:44  INFO        [prep_universe] 440/898 (437 valid)
13:42:55  INFO        [prep_universe] 480/898 (477 valid)
13:43:09  INFO        [prep_universe] 520/898 (517 valid)
13:43:19  INFO        [prep_universe] 560/898 (557 valid)
13:43:33  INFO        [prep_universe] 600/898 (597 valid)
13:43:43  INFO        [prep_universe] 640/898 (637 valid)
13:43:57  INFO        [prep_universe] 680/898 (677 valid)
13:44:10  INFO        [prep_universe] 720/898 (717 valid)
13:44:20  INFO        [prep_universe] 760/898 (757 valid)
13:44:34  INFO        [prep_universe] 800/898 (797 valid)
13:44:44  INFO        [prep_universe] 840/898 (836 valid)
13:44:58  INFO        [prep_universe] 880/898 (876 valid)
13:45:01  INFO        [prep_universe] 898/898 (894 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $468.33|
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
|  Open positions                                                       5|
|  Invested                                                       $444.57|
|  Open P&L                                                        $-2.52|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $93.79     $307.55  $306.38  -0.4%   $-0.36  |
|  ADM      Pullback50      $94.18     $80.48   $80.50   +0.0%   $+0.03  |
|  AES      Pullback50      $94.12     $14.72   $14.72   +0.0%   $+0.03  |
|  CDW      Pullback50      $69.46     $136.69  $134.47  -1.6%   $-1.15  |
|  GOOG     Pullback50      $93.02     $354.24  $350.20  -1.1%   $-1.07  |
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
|  Signal candidates                                                   48|
|  Universe scanned                                                   898|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=134 paper_keys=yes dry_run=False
  alpaca positions=21
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-11T09:45:05.711466-04:00 ===

[Run context]
Paper auth OK — equity $135848.95, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
```

---

## Run 20260811T134617Z

- UTC timestamp: `20260811T134617Z`
- GitHub run: [#6682](https://github.com/28twagg-ops/TradingBot/actions/runs/31497811084)
- Run id: `31497811084`
- Live bot: exit=`0`, duration=`223s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-11T09:25:49.736216-04:00","date":"2026-08-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.67},"signals":0,"placed":0,"equity":140246.92,"open_positions":20,"pending_orders":0,"open_lots":127,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"6678","github_run_id":"31496048357","status":"ok"}
```

### Live bot full output

```text
13:46:18  INFO      Mode: morning_scan
13:46:19  INFO        [positions] 5/5 (5 valid)
13:46:20  INFO        SELL MARKET [urgent] GOOG closed
13:46:22  INFO        TX logged: SELL GOOG  P&L -1.4%
13:46:23  INFO        SELL MARKET [urgent] CDW closed
13:46:25  INFO        TX logged: SELL CDW  P&L -1.31%
13:46:25  INFO        Universe cache hit: 903 tickers (tickers_2026-08-11.json)
13:46:26  INFO        [universe] 40/900 (40 valid)
13:46:28  INFO        [universe] 80/900 (80 valid)
13:46:29  INFO        [universe] 120/900 (120 valid)
13:46:31  INFO        [universe] 160/900 (160 valid)
13:46:33  INFO        [universe] 200/900 (199 valid)
13:46:39  INFO        [universe] 240/900 (238 valid)
13:46:50  INFO        [universe] 280/900 (278 valid)
13:47:04  INFO        [universe] 320/900 (318 valid)
13:47:14  INFO        [universe] 360/900 (358 valid)
13:47:28  INFO        [universe] 400/900 (397 valid)
13:47:38  INFO        [universe] 440/900 (437 valid)
13:47:52  INFO        [universe] 480/900 (477 valid)
13:48:03  INFO        [universe] 520/900 (517 valid)
13:48:13  INFO        [universe] 560/900 (557 valid)
13:48:27  INFO        [universe] 600/900 (597 valid)
13:48:40  INFO        [universe] 640/900 (637 valid)
13:48:51  INFO        [universe] 680/900 (677 valid)
13:49:02  INFO        [universe] 720/900 (717 valid)
13:49:16  INFO        [universe] 760/900 (757 valid)
13:49:26  INFO        [universe] 800/900 (797 valid)
13:49:39  INFO        [universe] 840/900 (836 valid)
13:49:50  INFO        [universe] 880/900 (876 valid)
13:49:57  INFO        [universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $468.04|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-08-11|
|  Universe                                                          both|
|  Mo~  Aug: VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Disabled                GapDown, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $468.04|
|  Cash                                                            $23.69|
|  Reserve                                          $23.40  (always kept)|
|  Available                                      $0.29  (for new trades)|
|  Trade size             $93.61  (20% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (5 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $93.79     $307.55  $306.37  -0.4%   $-0.36  |
|  ADM      Pullback50      $94.00     $80.48   $80.35   -0.2%   $-0.15  |
|  AES      Pullback50      $94.09     $14.72   $14.72   +0.0%   $+0.00  |
|  CDW      Pullback50      $69.68     $136.69  $134.90  -1.3%   $-0.93  |
|  GOOG     Pullback50      $92.77     $354.24  $349.28  -1.4%   $-1.32  |
|                                                                        |
|  Total invested                                                 $444.34|
|  Total open P&L                                                  $-2.75|
|  Buys today: 0  |  entry cap: 0  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (47520.8m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  GOOG  P&L -1.4%  $-1.32                        EXIT: stop_loss (-1.4%)|
|  CDW  P&L -1.3%  $-0.93                         EXIT: stop_loss (-1.3%)|
|  AAPL  P&L -0.4%  $-0.36                                           HOLD|
|  ADM  P&L -0.2%  $-0.15                                            HOLD|
|  AES  P&L +0.0%  $+0.00                                            HOLD|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 2 | filled 2 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 3|
|  Stop-loss breaches                                                   2|
|  GOOG                                        -1.40%  (threshold -0.50%)|
|  CDW                                         -1.31%  (threshold -0.50%)|
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
|                         SIGNALS FOUND  --  44                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AFL      Pullback50      eq     $121.34  43.6   -2.56   50MA bounce (+|
|  ALGN     Pullback50      eq     $175.83  53.5   -2.32   50MA bounce (+|
|  AIG      Pullback50      eq     $77.60   46.4   -2.35   50MA bounce (+|
|  ADI      Pullback50      eq     $392.90  53.0   -2.77   50MA bounce (-|
|  C        Pullback50      eq     $136.85  59.2   -2.97   50MA bounce (+|
|  DOV      Pullback50      eq     $212.37  47.8   -1.48   50MA bounce (-|
|  EQIX     Pullback50      eq     $1049.~  54.0   -2.74   50MA bounce (-|
|  ES       Pullback50      eq     $71.44   32.4   -2.10   50MA bounce (-|
|  EXR      Pullback50      eq     $147.04  55.4   -2.15   50MA bounce (+|
|  GEV      Pullback50      eq     $1017.~  54.7   -2.47   50MA bounce (-|
|  INVH     Pullback50      eq     $29.93   57.2   -2.41   50MA bounce (+|
|  KEY      Pullback50      eq     $22.82   44.8   -2.64   50MA bounce (+|
|  MAS      Pullback50      eq     $75.81   46.2   -1.43   50MA bounce (-|
|  MDLZ     Pullback50      eq     $61.35   52.1   -2.20   50MA bounce (+|
|  PCG      Pullback50      eq     $17.16   36.0   -2.11   50MA bounce (+|
|  PGR      Pullback50      eq     $213.42  64.0   -1.81   50MA bounce (+|
|  PPG      Pullback50      eq     $116.96  49.4   -1.85   50MA bounce (-|
|  TER      Pullback50      eq     $382.10  53.1   -1.74   50MA bounce (-|
|  TRGP     Pullback50      eq     $267.57  38.6   -2.66   50MA bounce (-|
|  TJX      Pullback50      eq     $158.42  56.6   -2.98   50MA bounce (+|
|  VTRS     Pullback50      eq     $16.52   42.6   -2.32   50MA bounce (-|
|  WRB      Pullback50      eq     $70.71   42.3   -2.38   50MA bounce (+|13:50:00  INFO        place_all_stops: checking 3 positions...
13:50:00  INFO        STOP skipped AAPL: fractional (0.3061 shares) — software exit will handle it
13:50:00  INFO        STOP-MARKET placed ADM  qty=1 (pos=1.1699)  stop=$80.07  id=b841c5cd-5e07-44c2-913d-70d13e04ea23
13:50:00  INFO        STOP-MARKET placed AES  qty=6 (pos=6.3920)  stop=$14.65  id=1f98fd70-6982-4e2b-a1db-5f700e7f2ebf
13:50:00  INFO        Daily log -> logs/daily/2026-08-11.md
13:50:00  INFO        Dashboard written → logs/dashboard.md

|  WM       Pullback50      eq     $228.50  36.5   -2.62   50MA bounce (+|
|  WMB      Pullback50      eq     $72.53   42.6   -2.55   50MA bounce (-|
|  AEIS     Pullback50      eq     $321.59  51.1   -1.92   50MA bounce (+|
|  ALLY     Pullback50      eq     $44.25   47.5   -2.19   50MA bounce (-|
|  ALV      Pullback50      eq     $122.33  56.8   -1.76   50MA bounce (+|
|  AM       Pullback50      eq     $22.11   41.4   -2.72   50MA bounce (+|
|  BC       Pullback50      eq     $81.44   48.2   -2.43   50MA bounce (+|
|  BKH      Pullback50      eq     $74.02   45.4   -2.27   50MA bounce (+|
|  CBT      Pullback50      eq     $88.65   48.2   -1.51   50MA bounce (+|
|  CUBE     Pullback50      eq     $41.27   51.6   -2.58   50MA bounce (+|
|  COLB     Pullback50      eq     $31.51   38.4   -2.45   50MA bounce (+|
|  ELS      Pullback50      eq     $64.57   45.3   -2.24   50MA bounce (+|
|  EXP      Pullback50      eq     $213.27  57.7   -1.97   50MA bounce (-|
|  FHN      Pullback50      eq     $25.34   43.9   -1.85   50MA bounce (+|
|  GATX     Pullback50      eq     $177.97  45.2   -2.46   50MA bounce (+|
|  IRT      Pullback50      eq     $16.73   57.4   -1.56   50MA bounce (+|
|  JEF      Pullback50      eq     $56.09   50.7   -2.66   50MA bounce (+|
|  PK       Pullback50      eq     $14.52   40.9   -2.42   50MA bounce (+|
|  SLAB     Pullback50      eq     $218.78  63.4   -2.47   50MA bounce (+|
|  TNL      Pullback50      eq     $74.19   46.2   -2.42   50MA bounce (-|
|  TOL      Pullback50      eq     $151.56  53.0   -2.80   50MA bounce (+|
|  WTFC     Pullback50      eq     $160.16  55.2   -2.02   50MA bounce (+|
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
|  Scanned                                                            896|
|  Signals                                                             44|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                2|
|  Open pos                                                             3|
|  Equity                                                         $467.69|
|  Cash                                                           $186.00|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=134 paper_keys=yes dry_run=False
  alpaca positions=21
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-11T09:50:02.904616-04:00 ===

[Run context]
Paper auth OK — equity $134909.95, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-11 09:50:06,699 INFO   EXIT [b383|lab0383_s362_w4_1120_1135_r2|S362] stop_loss (-57.5%) SELL 1 AAPL260812C00312500 @<= 0.25
2026-08-11 09:50:11,739 INFO   EXIT [b857|lab0857_s408_w1_0928_1005_r2|S408] stop_loss (-51.7%) SELL 1 AAPL260814C00320000 @<= 0.16
2026-08-11 09:50:16,383 INFO   EXIT [b785|lab0785_s398_w1_0928_1005_r2|S398] stop_loss (-84.7%) SELL 1 CELH260814C00028500 @<= 0.04
```

---

## Run 20260811T135119Z

- UTC timestamp: `20260811T135119Z`
- GitHub run: [#6683](https://github.com/28twagg-ops/TradingBot/actions/runs/31498255761)
- Run id: `31498255761`
- Live bot: exit=`0`, duration=`250s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-11T09:25:49.736216-04:00","date":"2026-08-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.67},"signals":0,"placed":0,"equity":140246.92,"open_positions":20,"pending_orders":0,"open_lots":127,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"6678","github_run_id":"31496048357","status":"ok"}
```

### Live bot full output

```text
13:51:20  INFO      Mode: morning_scan
13:51:21  INFO        [positions] 3/3 (3 valid)
13:51:21  INFO        SELL MARKET [urgent] AAPL closed
13:51:24  INFO        TX logged: SELL AAPL  P&L -0.57%
13:51:24  INFO        Universe cache hit: 903 tickers (tickers_2026-08-11.json)
13:51:25  INFO        [universe] 40/901 (40 valid)
13:51:26  INFO        [universe] 80/901 (80 valid)
13:51:27  INFO        [universe] 120/901 (120 valid)
13:51:29  INFO        [universe] 160/901 (160 valid)
13:51:30  INFO        [universe] 200/901 (199 valid)
13:51:37  INFO        [universe] 240/901 (238 valid)
13:51:50  INFO        [universe] 280/901 (278 valid)
13:52:00  INFO        [universe] 320/901 (318 valid)
13:52:13  INFO        [universe] 360/901 (358 valid)
13:52:26  INFO        [universe] 400/901 (397 valid)
13:52:36  INFO        [universe] 440/901 (437 valid)
13:52:50  INFO        [universe] 480/901 (477 valid)
13:53:03  INFO        [universe] 520/901 (517 valid)
13:53:13  INFO        [universe] 560/901 (557 valid)
13:53:26  INFO        [universe] 600/901 (597 valid)
13:53:36  INFO        [universe] 640/901 (637 valid)
13:53:49  INFO        [universe] 680/901 (677 valid)
13:54:02  INFO        [universe] 720/901 (717 valid)
13:54:13  INFO        [universe] 760/901 (757 valid)
13:54:25  INFO        [universe] 800/901 (797 valid)
13:54:39  INFO        [universe] 840/901 (836 valid)
13:54:49  INFO        [universe] 880/901 (876 valid)
13:54:56  INFO        [universe] 901/901 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.73|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-08-11|
|  Universe                                                          both|
|  Mo~  Aug: VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Disabled                GapDown, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $467.73|
|  Cash                                                           $186.00|
|  Reserve                                          $23.39  (always kept)|
|  Available                                    $162.61  (for new trades)|
|  Trade size             $93.55  (20% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (3 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $93.61     $307.55  $305.79  -0.6%   $-0.54  |
|  ADM      Pullback50      $93.97     $80.48   $80.32   -0.2%   $-0.18  |
|  AES      Pullback50      $94.15     $14.72   $14.73   +0.1%   $+0.06  |
|                                                                        |
|  Total invested                                                 $281.73|
|  Total open P&L                                                  $-0.66|
|  Buys today: 0  |  entry cap: 2  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (47525.9m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  AAPL  P&L -0.6%  $-0.54                        EXIT: stop_loss (-0.6%)|
|  ADM  P&L -0.2%  $-0.18                                            HOLD|
|  AES  P&L +0.1%  $+0.06                                            HOLD|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 1 | filled 1 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 2|
|  Stop-loss breaches                                                   1|
|  AAPL                                        -0.57%  (threshold -0.50%)|
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
|                         SIGNALS FOUND  --  44                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AFL      Pullback50      eq     $121.44  43.8   -2.55   50MA bounce (+|
|  ALGN     Pullback50      eq     $175.79  53.5   -2.30   50MA bounce (+|
|  AIG      Pullback50      eq     $77.57   46.3   -2.34   50MA bounce (+|
|  ADI      Pullback50      eq     $392.90  53.0   -2.76   50MA bounce (-|
|  C        Pullback50      eq     $136.96  59.4   -2.96   50MA bounce (+|
|  DOV      Pullback50      eq     $212.65  48.1   -1.48   50MA bounce (-|
|  EQIX     Pullback50      eq     $1045.~  53.4   -2.73   50MA bounce (-|
|  EXR      Pullback50      eq     $147.66  56.9   -2.15   50MA bounce (+|
|  ES       Pullback50      eq     $71.47   32.8   -2.09   50MA bounce (-|
|  GEV      Pullback50      eq     $1021.~  55.1   -2.43   50MA bounce (-|
|  INVH     Pullback50      eq     $29.96   57.6   -2.40   50MA bounce (+|
|  KEY      Pullback50      eq     $22.82   44.9   -2.62   50MA bounce (+|
|  MAS      Pullback50      eq     $75.96   46.4   -1.42   50MA bounce (+|
|  MDLZ     Pullback50      eq     $61.40   52.4   -2.19   50MA bounce (+|
|  MS       Pullback50      eq     $216.45  47.4   -2.37   50MA bounce (+|
|  PCG      Pullback50      eq     $17.11   35.0   -2.11   50MA bounce (-|
|  PPG      Pullback50      eq     $117.30  49.9   -1.84   50MA bounce (+|
|  PGR      Pullback50      eq     $213.37  63.9   -1.81   50MA bounce (+|
|  PWR      Pullback50      eq     $670.70  54.8   -1.59   50MA bounce (-|
|  SPG      Pullback50      eq     $222.40  44.2   -2.90   50MA bounce (+|
|  TRGP     Pullback50      eq     $267.55  38.6   -2.66   50MA bounce (-|
|  TER      Pullback50      eq     $378.52  52.3   -1.73   50MA bounce (-|
|  TJX      Pullback50      eq     $158.05  55.7   -2.97   50MA bounce (+|
|  VTRS     Pullback50      eq     $16.52   42.7   -2.31   50MA bounce (-|
|  WRB      Pullback50      eq     $70.63   42.0   -2.38   50MA bounce (+|
|  WM       Pullback50      eq     $228.29  36.1   -2.61   50MA bounce (+|
|  WMB      Pullback50      eq     $72.52   42.6   -2.54   50MA bounce (-|13:54:59  INFO        BUY  AFL  $93.55  [Pullback50]  id=da543734-6b57-4fb8-88af-7ecae6db4fa7
13:54:59  INFO        BUY  ALGN  $93.55  [Pullback50]  id=d6886527-6ea8-40ce-a94f-f02cc6576ad1
13:54:59  INFO        BUY  AIG  $69.13  [Pullback50]  id=7fffae41-a532-4d95-9ca2-8953c48e1857
13:55:28  INFO        place_all_stops: checking 5 positions...
13:55:28  INFO        STOP skipped ADM: fractional (0.1699 shares) — software exit will handle it
13:55:28  INFO        STOP already live AES @ $14.65
13:55:28  INFO        STOP skipped AFL: fractional (0.7678 shares) — software exit will handle it
13:55:28  INFO        STOP skipped AIG: fractional (0.8895 shares) — software exit will handle it
13:55:28  INFO        STOP skipped ALGN: fractional (0.5257 shares) — software exit will handle it
13:55:28  INFO        Daily log -> logs/daily/2026-08-11.md
13:55:28  INFO        Dashboard written → logs/dashboard.md

|  ALLY     Pullback50      eq     $44.37   48.2   -2.18   50MA bounce (-|
|  AM       Pullback50      eq     $22.11   41.4   -2.71   50MA bounce (+|
|  ALV      Pullback50      eq     $122.61  57.3   -1.76   50MA bounce (+|
|  BC       Pullback50      eq     $81.30   47.7   -2.43   50MA bounce (+|
|  COLB     Pullback50      eq     $31.53   38.6   -2.44   50MA bounce (+|
|  CUBE     Pullback50      eq     $41.25   51.4   -2.57   50MA bounce (+|
|  CYTK     Pullback50      eq     $78.91   42.4   -2.42   50MA bounce (+|
|  ELS      Pullback50      eq     $64.52   45.1   -2.24   50MA bounce (+|
|  EXP      Pullback50      eq     $213.52  57.8   -1.96   50MA bounce (-|
|  FHN      Pullback50      eq     $25.35   44.1   -1.85   50MA bounce (+|
|  GATX     Pullback50      eq     $177.82  44.9   -2.45   50MA bounce (+|
|  IRT      Pullback50      eq     $16.72   57.2   -1.56   50MA bounce (+|
|  JEF      Pullback50      eq     $56.08   50.7   -2.62   50MA bounce (+|
|  LAMR     Pullback50      eq     $155.12  42.7   -1.97   50MA bounce (-|
|  SLAB     Pullback50      eq     $218.80  63.5   -2.47   50MA bounce (+|
|  TNL      Pullback50      eq     $74.02   45.7   -2.41   50MA bounce (-|
|  VNO      Pullback50      eq     $38.94   52.5   -1.70   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] AFL  Pullback50                                    $93.55|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] ALGN  Pullback50                                   $93.55|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] AIG  Pullback50                                    $69.13|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] ADI  Pullback50                                      cap 5|
|    SKIP [eq] C  Pullback50                                        cap 5|
|    SKIP [eq] DOV  Pullback50                                      cap 5|
|    SKIP [eq] EQIX  Pullback50                                     cap 5|
|    SKIP [eq] EXR  Pullback50                                      cap 5|
|    SKIP [eq] ES  Pullback50                                       cap 5|
|    SKIP [eq] GEV  Pullback50                                      cap 5|
|    SKIP [eq] INVH  Pullback50                                     cap 5|
|    SKIP [eq] KEY  Pullback50                                      cap 5|
|    SKIP [eq] MAS  Pullback50                                      cap 5|
|    SKIP [eq] MDLZ  Pullback50                                     cap 5|
|    SKIP [eq] MS  Pullback50                                       cap 5|
|    SKIP [eq] PCG  Pullback50                                      cap 5|
|    SKIP [eq] PPG  Pullback50                                      cap 5|
|    SKIP [eq] PGR  Pullback50                                      cap 5|
|    SKIP [eq] PWR  Pullback50                                      cap 5|
|    SKIP [eq] SPG  Pullback50                                      cap 5|
|    SKIP [eq] TRGP  Pullback50                                     cap 5|
|    SKIP [eq] TER  Pullback50                                      cap 5|
|    SKIP [eq] TJX  Pullback50                                      cap 5|
|    SKIP [eq] VTRS  Pullback50                                     cap 5|
|    SKIP [eq] WRB  Pullback50                                      cap 5|
|    SKIP [eq] WM  Pullback50                                       cap 5|
|    SKIP [eq] WMB  Pullback50                                      cap 5|
|    SKIP [eq] ALLY  Pullback50                                     cap 5|
|    SKIP [eq] AM  Pullback50                                       cap 5|
|    SKIP [eq] ALV  Pullback50                                      cap 5|
|    SKIP [eq] BC  Pullback50                                       cap 5|
|    SKIP [eq] COLB  Pullback50                                     cap 5|
|    SKIP [eq] CUBE  Pullback50                                     cap 5|
|    SKIP [eq] CYTK  Pullback50                                     cap 5|
|    SKIP [eq] ELS  Pullback50                                      cap 5|
|    SKIP [eq] EXP  Pullback50                                      cap 5|
|    SKIP [eq] FHN  Pullback50                                      cap 5|
|    SKIP [eq] GATX  Pullback50                                     cap 5|
|    SKIP [eq] IRT  Pullback50                                      cap 5|
|    SKIP [eq] JEF  Pullback50                                      cap 5|
|    SKIP [eq] LAMR  Pullback50                                     cap 5|
|    SKIP [eq] SLAB  Pullback50                                     cap 5|
|    SKIP [eq] TNL  Pullback50                                      cap 5|
|    SKIP [eq] VNO  Pullback50                                      cap 5|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      3|
+------------------------------------------------------------------------+
|  AFL                                                  still unconfirmed|
|  ALGN                                                 still unconfirmed|
|  AIG                                                  still unconfirmed|
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
|  Strategy  VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Scanned                                                            897|
|  Signals                                                             44|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  3 unconfirmed|
|  Exits                                                                1|
|  Open pos                                                             5|
|  Equity                                                         $466.91|
|  Cash                                                           $103.41|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=133 paper_keys=yes dry_run=False
  alpaca positions=21
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-11T09:55:31.096884-04:00 ===

[Run context]
Paper auth OK — equity $134939.41, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-11 09:55:32,286 INFO   EXIT [b382|lab0382_s362_w4_1120_1135_r1|S362] stop_loss (-57.5%) SELL 1 AAPL260812C00312500 @<= 0.29
2026-08-11 09:55:34,074 INFO   EXIT [b856|lab0856_s408_w1_0928_1005_r1|S408] stop_loss (-51.7%) SELL 1 AAPL260814C00320000 @<= 0.16
  EXIT [b111|lab0111_s212_w2_1005_1045_r2|S212] stop_loss (-58.6%) SELL failed QQQ260813C00740000: {"code":40010001,"message":"client_order_id must be unique"}

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260811T135655Z

- UTC timestamp: `20260811T135655Z`
- GitHub run: [#6684](https://github.com/28twagg-ops/TradingBot/actions/runs/31498705337)
- Run id: `31498705337`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-11T09:25:49.736216-04:00","date":"2026-08-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.67},"signals":0,"placed":0,"equity":140246.92,"open_positions":20,"pending_orders":0,"open_lots":127,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"6678","github_run_id":"31496048357","status":"ok"}
```

### Live bot full output

```text
13:56:56  INFO      Mode: morning_scan
13:56:57  INFO        [positions] 5/5 (5 valid)
13:56:57  INFO        SELL MARKET [urgent] ADM closed
13:57:00  INFO        TX logged: SELL ADM  P&L -0.59%
13:57:00  INFO        SELL LIMIT ALGN  qty=0.525665089  limit=$177.60  id=4c4db0a2-e8c3-44ea-b60a-342bd968e85e
13:57:30  INFO        SELL LIMIT filled ALGN (confirmed by position check)
13:57:31  INFO        TX logged: SELL ALGN  P&L 0.01%
13:57:31  INFO        Universe cache hit: 903 tickers (tickers_2026-08-11.json)
13:57:32  INFO        [universe] 40/900 (40 valid)
13:57:33  INFO        [universe] 80/900 (80 valid)
13:57:34  INFO        [universe] 120/900 (120 valid)
13:57:35  INFO        [universe] 160/900 (160 valid)
13:57:37  INFO        [universe] 200/900 (199 valid)
13:57:44  INFO        [universe] 240/900 (238 valid)
13:57:57  INFO        [universe] 280/900 (278 valid)
13:58:08  INFO        [universe] 320/900 (318 valid)
13:58:21  INFO        [universe] 360/900 (358 valid)
13:58:32  INFO        [universe] 400/900 (397 valid)
13:58:45  INFO        [universe] 440/900 (437 valid)
13:58:56  INFO        [universe] 480/900 (477 valid)
13:59:09  INFO        [universe] 520/900 (517 valid)
13:59:19  INFO        [universe] 560/900 (557 valid)
13:59:33  INFO        [universe] 600/900 (597 valid)
13:59:43  INFO        [universe] 640/900 (637 valid)
13:59:57  INFO        [universe] 680/900 (677 valid)
14:00:07  INFO        [universe] 720/900 (717 valid)
14:00:21  INFO        [universe] 760/900 (757 valid)
14:00:31  INFO        [universe] 800/900 (797 valid)
```

### Options bot full output

```text

## Run 20260811T140138Z

- UTC timestamp: `20260811T140138Z`
- GitHub run: [#6685](https://github.com/28twagg-ops/TradingBot/actions/runs/31499161640)
- Run id: `31499161640`
- Live bot: exit=`0`, duration=`5s`
- Options bot: exit=`0`, duration=`101s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-11T10:01:45.693938-04:00","date":"2026-08-11","mode":"entry+manage","header":"entry+manage (13 new)","elapsed_s":91.9,"phases_s":{"reconcile":0.56,"cancel":0.12,"manage":20.23,"scan":61.89,"entries":6.21,"reconcile2":2.12},"signals":61,"placed":13,"equity":136064.83,"open_positions":23,"pending_orders":2,"open_lots":130,"submitted_today":13,"filled_today":11,"unattributed_contracts":6,"top_signals":["S203:MARA","S210:ARM","S210:AFRM","S211:AVGO","S211:BA","S212:META","S212:NFLX","S212:AFRM"],"github_run":"6685","github_run_id":"31499161640","status":"ok"}
```

### Live bot full output

```text
14:01:39  INFO      Mode: exits
14:01:40  INFO        Daily log -> logs/daily/2026-08-11.md
14:01:40  INFO        Daily log reconciled -> logs/daily/2026-08-11.md (3 ledger rows)
14:01:40  INFO        place_all_stops: checking 3 positions...
14:01:40  INFO        STOP already live AES @ $14.65
14:01:40  INFO        STOP skipped AFL: fractional (0.7678 shares) — software exit will handle it
14:01:40  INFO        STOP skipped AIG: fractional (0.8895 shares) — software exit will handle it
14:01:40  INFO        [positions] 3/3 (3 valid)
14:01:41  INFO        SELL MARKET [urgent] AIG closed
14:01:43  INFO        TX logged: SELL AIG  P&L -0.59%
14:01:43  INFO        Daily log -> logs/daily/2026-08-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.55|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AIG  P&L -0.6%  $-0.41                         EXIT: stop_loss (-0.6%)|
|  AFL  P&L -0.2%  $-0.20                                            HOLD|
|  AES  P&L +0.0%  $+0.03                                            HOLD|
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
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  AIG                                         -0.59%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=130 paper_keys=yes dry_run=False
  alpaca positions=21
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-11T10:01:45.693938-04:00 ===

[Run context]
Paper auth OK — equity $136066.83, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-11 10:01:51,735 INFO   EXIT [b305|lab0305_s354_w1_0928_1005_r2|S354] stop_loss (-50.9%) SELL 1 AAPL260814C00317500 @<= 0.27
2026-08-11 10:01:52,758 INFO   EXIT [b784|lab0784_s398_w1_0928_1005_r1|S398] stop_loss (-74.6%) SELL 1 CELH260814C00028500 @<= 0.06
2026-08-11 10:01:55,733 INFO   EXIT [b858|lab0858_s408_w2_1005_1045_r1|S408] stop_loss (-54.2%) SELL 1 AAPL260814C00320000 @<= 0.15
  EXIT [b111|lab0111_s212_w2_1005_1045_r2|S212] stop_loss (-58.6%) SELL failed QQQ260813C00740000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-11 10:02:05,325 INFO   EXIT [b919|lab0919_s412_w4_1120_1135_r2|S412] stop_loss (-59.0%) SELL 1 AAPL260812C00312500 @<= 0.28
2026-08-11 10:02:06,922 INFO   EXIT [b404|lab0404_s364_w1_0928_1005_r1|S364] stop_loss (-50.6%) SELL 1 AAPL260817C00320000 @<= 0.32

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 61 signal(s); top: ['S203:MARA', 'S210:ARM', 'S210:AFRM', 'S211:AVGO', 'S211:BA', 'S212:META', 'S212:NFLX', 'S212:AFRM']
Paper lab: $135913 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 13 no tradeable call, 83 pending order
Placed 13 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $136,064.83                             |
|  Signals this run              61                                      |
|  Orders submitted (session)    13                                      |
|  Orders filled today (ledger)  11                                      |
|  Entries placed this run       13                                      |
|  Open virtual lots             130                                     |
|  Broker option positions       23                                      |
|  Unattributed contracts        6 (orphan reconcile)                    |
|  Pending orders                2                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1757  buckets=313  win=37%                           |
|  Returns   avg=+13.1%  med=-42.2%  p10=-82.5%  p90=+125.0%             |
|  Realized  $+3,699.47                                                  |
|  Raw incl dropped  trades=2291  real=$+2,103.92                        |
|  Today     trades=14  avg=-66.9%  med=-59.4%  real=$-532.67            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b383 lab0383_s362_w4_11  2  50% +581.3 +581.3 +1222.6 $   +337        |
|  b382 lab0382_s362_w4_11  2  50% +533.6 +533.6 +1125.8 $   +308        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  lab0091_s210_w6_14  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b281 lab0281_s351_w1_09  5  60% +156.4 +197.9 +346.9 $   +296         |
|  b316 lab0316_s355_w3_10  1 100% +193.8 +193.8 +193.8 $    +93         |
|  ... 305 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b802 lab0802_s404_w2_10  5  40% -37.8 -98.2 -98.4 $   -100       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (2)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S211:BA(2)                              |
+------------------------------------------------------------------------+
|  b94  S211 BA       limit=0.42                                         |
|  b95  S211 BA       limit=0.42                                         |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b784 S398 CELH260814C00028500 x1 stop_loss (-74.6%)                   |
|  b404 S364 AAPL260817C00320000 x1 stop_loss (-50.6%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (23)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260812C00315000          38    -71.6%   $ -1,150.00               |
|  AAPL260814C00317500          22    -50.9%   $   -684.87               |
|  TTD260814C00012500           12    +47.8%   $   +388.00               |
|  AAPL260817C00320000          12    -50.6%   $   -380.31               |
|  AAPL260812C00312500           9    -54.4%   $   -322.50               |
|  AAPL260812C00317500          10    -77.5%   $   -172.00               |
|  UBER260814C00080000           6    +53.3%   $   +146.00               |
|  CELH260814C00028500           6    -74.6%   $    -88.00               |
|  ... 15 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-11.log
elapsed=91.9s reconcile=0.56s cancel=0.12s manage=20.23s scan=61.89s entries=6.21s
STATUS: options_morning_bot run complete (PAPER) elapsed=91.9s. run=#6685 https://github.com/28twagg-ops/TradingBot/actions/runs/31499161640
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.csv
Summary: 12 buckets closed trades, $-532.67 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.csv
Summary: keep=0 watch=83 drop=22
Orphan rate: 11.6% (265/2291) ALERT
# Options signal frequency

_Generated 2026-08-11T10:03:23.464006_

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
## Ledger health — 2026-08-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   591 | WARN | <<<
| Missing exit records (post) |   591 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   130 | INFO |
| Total closed lots           |  1559 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=466.49 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260811T140739Z

- UTC timestamp: `20260811T140739Z`
- GitHub run: [#6686](https://github.com/28twagg-ops/TradingBot/actions/runs/31499619166)
- Run id: `31499619166`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`80s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-11T10:07:45.106053-04:00","date":"2026-08-11","mode":"entry+manage","header":"entry+manage (13 new)","elapsed_s":71.9,"phases_s":{"reconcile":1.66,"cancel":0.02,"manage":6.0,"scan":60.62,"entries":1.95,"reconcile2":1.15},"signals":85,"placed":13,"equity":136371.37,"open_positions":27,"pending_orders":0,"open_lots":132,"submitted_today":26,"filled_today":26,"unattributed_contracts":2,"top_signals":["S203:MARA","S210:ARM","S210:AFRM","S211:AVGO","S211:BA","S212:META","S212:NFLX","S212:AFRM"],"github_run":"6686","github_run_id":"31499619166","status":"ok"}
```

### Live bot full output

```text
14:07:40  INFO      Mode: exits
14:07:41  INFO        Daily log -> logs/daily/2026-08-11.md
14:07:41  INFO        Daily log reconciled -> logs/daily/2026-08-11.md (6 ledger rows)
14:07:41  INFO        place_all_stops: checking 2 positions...
14:07:41  INFO        STOP already live AES @ $14.65
14:07:41  INFO        STOP skipped AFL: fractional (0.7678 shares) — software exit will handle it
14:07:41  INFO        [positions] 2/2 (2 valid)
14:07:41  INFO        SELL MARKET [urgent] AFL closed
14:07:43  INFO        TX logged: SELL AFL  P&L -0.54%
14:07:43  INFO        Daily log -> logs/daily/2026-08-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:07 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.16|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AFL  P&L -0.5%  $-0.50                         EXIT: stop_loss (-0.5%)|
|  AES  P&L +0.0%  $+0.00                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  1 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
|  Logged exits                                                         1|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  AFL                                         -0.54%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=130 paper_keys=yes dry_run=False
  alpaca positions=26
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-11T10:07:45.106053-04:00 ===

[Run context]
Paper auth OK — equity $136365.37, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-11 10:07:47,435 INFO   EXIT [b304|lab0304_s354_w1_0928_1005_r1|S354] stop_loss (-50.9%) SELL 1 AAPL260814C00317500 @<= 0.31
  EXIT [b111|lab0111_s212_w2_1005_1045_r2|S212] stop_loss (-58.6%) SELL failed QQQ260813C00740000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-11 10:07:50,370 INFO   EXIT [b918|lab0918_s412_w4_1120_1135_r1|S412] stop_loss (-57.5%) SELL 1 AAPL260812C00312500 @<= 0.29
2026-08-11 10:07:50,827 INFO   EXIT [b861|lab0861_s408_w3_1045_1120_r2|S408] stop_loss (-54.2%) SELL 1 AAPL260814C00320000 @<= 0.15
2026-08-11 10:07:51,262 INFO   EXIT [b313|lab0313_s355_w1_0928_1005_r2|S355] stop_loss (-50.6%) SELL 1 AAPL260817C00320000 @<= 0.28
2026-08-11 10:07:51,606 INFO   EXIT [b182|lab0182_s217_w3_1045_1120_r1|S217] stop_loss (-75.3%) SELL 1 RBLX260814C00041000 @<= 0.12

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 85 signal(s); top: ['S203:MARA', 'S210:ARM', 'S210:AFRM', 'S211:AVGO', 'S211:BA', 'S212:META', 'S212:NFLX', 'S212:AFRM']
Paper lab: $136309 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 41 no tradeable call, 75 pending order
Placed 13 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $136,371.37                             |
|  Signals this run              85                                      |
|  Orders submitted (session)    26                                      |
|  Orders filled today (ledger)  26                                      |
|  Entries placed this run       13                                      |
|  Open virtual lots             132                                     |
|  Broker option positions       27                                      |
|  Unattributed contracts        2 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1786  buckets=314  win=37%                           |
|  Returns   avg=+13.9%  med=-42.2%  p10=-82.6%  p90=+127.9%             |
|  Realized  $+3,632.21                                                  |
|  Raw incl dropped  trades=2320  real=$+2,036.66                        |
|  Today     trades=18  avg=-64.1%  med=-58.7%  real=$-632.67            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b383 lab0383_s362_w4_11  2  50% +581.3 +581.3 +1222.6 $   +337        |
|  b382 lab0382_s362_w4_11  2  50% +533.6 +533.6 +1125.8 $   +308        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  lab0091_s210_w6_14  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b281 lab0281_s351_w1_09  5  60% +156.4 +197.9 +346.9 $   +296         |
|  b316 lab0316_s355_w3_10  1 100% +193.8 +193.8 +193.8 $    +93         |
|  ... 306 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b802 lab0802_s404_w2_10  5  40% -37.8 -98.2 -98.4 $   -100       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b304 S354 AAPL260814C00317500 x1 stop_loss (-50.9%)                   |
|  b918 S412 AAPL260812C00312500 x1 stop_loss (-57.5%)                   |
|  b182 S217 RBLX260814C00041000 x1 stop_loss (-75.3%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (27)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260812C00315000          38    -71.6%   $ -1,150.00               |
|  AAPL260814C00317500          22    -50.9%   $   -684.87               |
|  TTD260814C00012500           12    +61.1%   $   +496.00               |
|  AAPL260812C00312500           9    -59.0%   $   -349.50               |
|  AAPL260817C00320000          10    -50.6%   $   -316.92               |
|  AAPL260812C00317500          10    -77.5%   $   -172.00               |
|  UBER260814C00080000           6    +42.3%   $   +116.00               |
|  C260814C00139000              3    -26.1%   $    -54.00               |
|  ... 19 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-11.log
elapsed=71.9s reconcile=1.66s cancel=0.02s manage=6.0s scan=60.62s entries=1.95s
STATUS: options_morning_bot run complete (PAPER) elapsed=71.9s. run=#6686 https://github.com/28twagg-ops/TradingBot/actions/runs/31499619166
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.csv
Summary: 16 buckets closed trades, $-632.67 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.csv
Summary: keep=0 watch=81 drop=24
Orphan rate: 11.6% (268/2320) ALERT
# Options signal frequency

_Generated 2026-08-11T10:09:02.665160_

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
## Ledger health — 2026-08-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   591 | WARN | <<<
| Missing exit records (post) |   591 | WARN | <<<
| State/ledger mismatches     |    21 | WARN | <<<
| Total open lots             |   132 | INFO |
| Total closed lots           |  1585 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=466.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260811T141059Z

- UTC timestamp: `20260811T141059Z`
- GitHub run: [#6687](https://github.com/28twagg-ops/TradingBot/actions/runs/31500067413)
- Run id: `31500067413`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`75s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-11T10:11:03.963765-04:00","date":"2026-08-11","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":67.3,"phases_s":{"reconcile":0.45,"cancel":0.13,"manage":9.86,"scan":52.0,"entries":4.14},"signals":72,"placed":0,"equity":136432.24,"open_positions":27,"pending_orders":0,"open_lots":131,"submitted_today":26,"filled_today":26,"unattributed_contracts":0,"top_signals":["S203:MARA","S210:ARM","S210:AFRM","S211:AVGO","S211:BA","S212:META","S212:NFLX","S212:AFRM"],"github_run":"6687","github_run_id":"31500067413","status":"ok"}
```

### Live bot full output

```text
14:11:00  INFO      Mode: exits
14:11:01  INFO        Daily log -> logs/daily/2026-08-11.md
14:11:01  INFO        Daily log reconciled -> logs/daily/2026-08-11.md (7 ledger rows)
14:11:01  INFO        place_all_stops: checking 1 positions...
14:11:01  INFO        STOP already live AES @ $14.65
14:11:01  INFO        [positions] 1/1 (1 valid)
14:11:02  INFO        Daily log -> logs/daily/2026-08-11.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.19|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L +0.0%  $+0.03                                            HOLD|
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
  open_lots=132 paper_keys=yes dry_run=False
  alpaca positions=29
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-11T10:11:03.963765-04:00 ===

[Run context]
Paper auth OK — equity $136418.24, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-11 10:11:07,805 INFO   EXIT [b821|lab0821_s405_w4_1120_1135_r2|S405] stop_loss (-59.0%) SELL 1 AAPL260812C00312500 @<= 0.24
2026-08-11 10:11:08,209 INFO   EXIT [b803|lab0803_s404_w2_1005_1045_r2|S404] take_profit (+61.1%) SELL 1 TTD260814C00012500 @<= 1.06
2026-08-11 10:11:09,963 INFO   EXIT [b312|lab0312_s355_w1_0928_1005_r1|S355] stop_loss (-50.6%) SELL 1 AAPL260817C00320000 @<= 0.28
  EXIT [b111|lab0111_s212_w2_1005_1045_r2|S212] stop_loss (-58.6%) SELL failed QQQ260813C00740000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-11 10:11:14,704 INFO   EXIT [b860|lab0860_s408_w3_1045_1120_r1|S408] stop_loss (-54.2%) SELL 1 AAPL260814C00320000 @<= 0.19

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 72 signal(s); top: ['S203:MARA', 'S210:ARM', 'S210:AFRM', 'S211:AVGO', 'S211:BA', 'S212:META', 'S212:NFLX', 'S212:AFRM']
Paper lab: $136567 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 20 no tradeable call, 84 already attempted today
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $136,432.24                             |
|  Signals this run              72                                      |
|  Orders submitted (session)    26                                      |
|  Orders filled today (ledger)  26                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             131                                     |
|  Broker option positions       27                                      |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1787  buckets=315  win=36%                           |
|  Returns   avg=+13.8%  med=-42.2%  p10=-82.6%  p90=+127.9%             |
|  Realized  $+3,596.21                                                  |
|  Raw incl dropped  trades=2321  real=$+2,000.66                        |
|  Today     trades=19  avg=-63.7%  med=-58.7%  real=$-668.67            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b383 lab0383_s362_w4_11  2  50% +581.3 +581.3 +1222.6 $   +337        |
|  b382 lab0382_s362_w4_11  2  50% +533.6 +533.6 +1125.8 $   +308        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  lab0091_s210_w6_14  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b281 lab0281_s351_w1_09  5  60% +156.4 +197.9 +346.9 $   +296         |
|  b316 lab0316_s355_w3_10  1 100% +193.8 +193.8 +193.8 $    +93         |
|  ... 307 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b802 lab0802_s404_w2_10  5  40% -37.8 -98.2 -98.4 $   -100       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (6)                                                     |
+------------------------------------------------------------------------+
|  b304 S354 AAPL260814C00317500 x1 stop_loss (-50.9%)                   |
|  b182 S217 RBLX260814C00041000 x1 stop_loss (-75.3%)                   |
|  b821 S405 AAPL260812C00312500 x1 stop_loss (-59.0%)                   |
|  b803 S404 TTD260814C00012500 x1 take_profit (+61.1%)                  |
|  b312 S355 AAPL260817C00320000 x1 stop_loss (-50.6%)                   |
|  ... 1 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (27)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260812C00315000          38    -71.6%   $ -1,150.00               |
|  AAPL260814C00317500          22    -50.9%   $   -684.87               |
|  TTD260814C00012500           11    +70.0%   $   +520.67               |
|  AAPL260817C00320000           9    -50.6%   $   -285.23               |
|  AAPL260812C00312500           7    -55.9%   $   -257.83               |
|  AAPL260812C00317500          10    -77.5%   $   -172.00               |
|  UBER260814C00080000           6    +31.4%   $    +86.00               |
|  C260814C00139000              3    -34.8%   $    -72.00               |
|  ... 19 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-11.log
elapsed=67.3s reconcile=0.45s cancel=0.13s manage=9.86s scan=52.0s entries=4.14s
STATUS: options_morning_bot run complete (PAPER) elapsed=67.3s. run=#6687 https://github.com/28twagg-ops/TradingBot/actions/runs/31500067413
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.csv
Summary: 17 buckets closed trades, $-668.67 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.csv
Summary: keep=0 watch=81 drop=24
Orphan rate: 11.6% (268/2321) ALERT
# Options signal frequency

_Generated 2026-08-11T10:12:16.388643_

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
## Ledger health — 2026-08-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   591 | WARN | <<<
| Missing exit records (post) |   591 | WARN | <<<
| State/ledger mismatches     |    21 | WARN | <<<
| Total open lots             |   131 | INFO |
| Total closed lots           |  1586 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=466.19 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
