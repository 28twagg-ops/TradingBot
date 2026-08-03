# Daily Comprehensive Action Review — 2026-08-03

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260803T015715Z

- UTC timestamp: `20260803T015715Z`
- GitHub run: [#5817](https://github.com/28twagg-ops/TradingBot/actions/runs/30778070406)
- Run id: `30778070406`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-31T21:19:26.840600-04:00","date":"2026-07-31","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.1},"signals":0,"placed":0,"equity":135581.48,"open_positions":12,"pending_orders":0,"open_lots":60,"submitted_today":164,"filled_today":156,"unattributed_contracts":0,"top_signals":[],"github_run":"5816","github_run_id":"30677632858","status":"ok"}
```

### Live bot full output

```text
01:57:16  INFO      Mode: weekly
01:57:16  INFO        Weekly summary -> logs/weekly/2026-W32.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                            WEEKLY|
|  Time                                                         01:57 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.46|
+========================================================================+

+========================================================================+
|              RUBBER BAND BOT  |  Week 32 / 2026  |  LIVE               |
+========================================================================+
+------------------------------------------------------------------------+
|  Date                                                 2026-08-03  (Aug)|
|  Regime                                                            BULL|
|  Strat~  VolumeSpike  +  52wkLow (display only — schedule not enforced)|
|  Execution                      Summary mode only (no orders submitted)|
|  Buys today                                                           0|
|  Cash-based cap            12976 max trades with current available cash|
+------------------------------------------------------------------------+
|  Equity           $470.46       Cash             $153.29               |
|  Invested         $317.17       Available        $129.77               |
|  Open P&L         $+3.86        Realized P&L     $-13.02               |
+------------------------------------------------------------------------+
|  This week         0 buys  |  47 sells  |  Win rate 30%  |  P&L $-12.74|
|  All t~  1064 trades  |  Avg hold 1.8d  |  Return -7.5%  |  P&L $-13.02|
+------------------------------------------------------------------------+
|  TICKER  STRATEGY       INVESTED   ENTRY     NOW       P&L%      P&L$  |
+------------------------------------------------------------------------+
|  APG     MomReversal    $32.29     $38.85    $39.68    +2.1%     $+0.68|
|  CINF    Pullback50     $95.35     $175.04   $177.68   +1.5%     $+1.41|
|  MP      MomReversal    $95.31     $41.37    $42.00    +1.5%     $+1.42|
|  PWR     EarningsDrift  $94.22     $667.29   $669.71   +0.4%     $+0.34|
+------------------------------------------------------------------------+
|  Next month                               Sep:  GapDown  +  VolumeSpike|
+========================================================================+

+========================================================================+
|                        YEAR-BY-YEAR PERFORMANCE                        |
+========================================================================+
|  YEAR   START     END       RETURN    P&L $       TRADES   WIN%        |
+------------------------------------------------------------------------+
|  2026   $509      $469      -7.7%     $-39.34     1064     31.4% ✗     |
+------------------------------------------------------------------------+
|  Profitable years                                             0/1  (0%)|
|  Best  year                                      2026   -7.7%   $-39.34|
|  Worst year                                      2026   -7.7%   $-39.34|
+========================================================================+
```

### Options bot full output

```text
Weekend — skip options paper bot
```

---

## Run 20260803T053833Z

- UTC timestamp: `20260803T053833Z`
- GitHub run: [#5818](https://github.com/28twagg-ops/TradingBot/actions/runs/30787711287)
- Run id: `30787711287`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T01:38:37.302798-04:00","date":"2026-08-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.46},"signals":0,"placed":0,"equity":138189.4,"open_positions":12,"pending_orders":0,"open_lots":60,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5818","github_run_id":"30787711287","status":"ok"}
```

### Live bot full output

```text
05:38:33  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         05:38 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.83|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $471.83|
|  Cash                                                           $153.29|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $318.54|
|  Open P&L                                                        $+5.22|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (4 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  APG      MomReversal     $32.29     $38.85   $39.68   +2.1%   $+0.68  |
|  CINF     Pullback50      $95.35     $175.04  $177.68  +1.5%   $+1.41  |
|  MP       MomReversal     $95.74     $41.37   $42.19   +2.0%   $+1.85  |
|  PWR      EarningsDrift   $95.15     $667.29  $676.33  +1.4%   $+1.27  |
|                                                                        |
|  Total invested                                                 $318.54|
|  Total open P&L                                                  $+5.22|
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
|  2026-07-31  SELL  MPWR  EarningsDrift  $94.50  P&L $+0.30             |
|  2026-07-31  SELL  LECO  EarningsDrift  $93.79  P&L $-0.10             |
|  2026-07-31  SELL  NVT  EarningsDrift  $89.90  P&L $-0.43              |
|  2026-07-31  SELL  AVB  Pullback50  $93.36  P&L $-0.58                 |
|  2026-07-31  SELL  CI  Pullback50  $93.26  P&L $-0.49                  |
|  2026-07-31  SELL  FFIV  Pullback50  $91.92  P&L $-0.54                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=60 paper_keys=yes dry_run=False
  alpaca positions=14
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-03T01:38:37.302798-04:00 ===

[Run context]
After hours (01:38 ET) — exit summary only.
Paper auth OK — equity $138189.40, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $138,189.40                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             60                                      |
|  Broker option positions       12                                      |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=357  buckets=110  win=39%                            |
|  Returns   avg=+11.5%  med=-23.1%  p10=-65.8%  p90=+134.1%             |
|  Realized  $+7,303.13                                                  |
|  Raw incl dropped  trades=891  real=$+5,707.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b311 lab0311_s354_w4_11  1 100% +290.5 +290.5 +290.5 $   +122         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b820 lab0820_s405_w4_11  1 100% +254.8 +254.8 +254.8 $   +107         |
|  b821 lab0821_s405_w4_11  1 100% +242.9 +242.9 +242.9 $   +102         |
|  ... 102 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b20  lab0020_s202_w3_10  1   0% -88.9 -88.9 -88.9 $     -8       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b290 S352 AAPL260803C00315000 x1 take_profit (+188.3%                 |
|  b320 S356 AAPL260814C00330000 x1 take_profit (+54.0%)                 |
|  b328 S357 AAPL260821C00335000 x1 take_profit (+54.7%)                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (12)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260803C00315000          21   +188.3%   $ +1,618.50               |
|  AAPL260814C00330000           7    +54.0%   $   +225.75               |
|  AAPL260821C00335000           5    +54.7%   $   +175.00               |
|  T260807C00023000              6    -22.2%   $    -84.00               |
|  OXY260807C00059000            4    +27.4%   $    +68.00               |
|  SMCI260807P00025000           3    -46.5%   $    -60.00               |
|  SMCI260807P00025500           1    -45.5%   $    -25.00               |
|  NFLX260807C00075000           2    -24.0%   $    -24.00               |
|  ... 4 more position(s)                                                |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-03.log
elapsed=0.9s reconcile=0.46s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.9s. run=#5818 https://github.com/28twagg-ops/TradingBot/actions/runs/30787711287
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.5% (22/891)
# Options signal frequency

_Generated 2026-08-03T01:38:43.259736_

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
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    60 | INFO |
| Total closed lots           |   402 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.83 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260803T130122Z

- UTC timestamp: `20260803T130122Z`
- GitHub run: [#5819](https://github.com/28twagg-ops/TradingBot/actions/runs/30815928929)
- Run id: `30815928929`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T09:01:25.410664-04:00","date":"2026-08-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.27},"signals":0,"placed":0,"equity":134781.04,"open_positions":12,"pending_orders":0,"open_lots":60,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5819","github_run_id":"30815928929","status":"ok"}
```

### Live bot full output

```text
13:01:23  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.60|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $466.60|
|  Cash                                                           $153.29|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $313.31|
|  Open P&L                                                        $-0.01|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (4 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  APG      MomReversal     $30.93     $38.85   $38.00   -2.2%   $-0.69  |
|  CINF     Pullback50      $95.53     $175.04  $178.00  +1.7%   $+1.59  |
|  MP       MomReversal     $93.97     $41.37   $41.41   +0.1%   $+0.08  |
|  PWR      EarningsDrift   $92.89     $667.29  $660.25  -1.1%   $-0.99  |
|                                                                        |
|  Total invested                                                 $313.31|
|  Total open P&L                                                  $-0.01|
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
|  2026-07-31  SELL  MPWR  EarningsDrift  $94.50  P&L $+0.30             |
|  2026-07-31  SELL  LECO  EarningsDrift  $93.79  P&L $-0.10             |
|  2026-07-31  SELL  NVT  EarningsDrift  $89.90  P&L $-0.43              |
|  2026-07-31  SELL  AVB  Pullback50  $93.36  P&L $-0.58                 |
|  2026-07-31  SELL  CI  Pullback50  $93.26  P&L $-0.49                  |
|  2026-07-31  SELL  FFIV  Pullback50  $91.92  P&L $-0.54                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=60 paper_keys=yes dry_run=False
  alpaca positions=14
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-03T09:01:25.410664-04:00 ===

[Run context]
After hours (09:01 ET) — exit summary only.
Paper auth OK — equity $134781.04, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $134,781.04                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             60                                      |
|  Broker option positions       12                                      |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=357  buckets=110  win=39%                            |
|  Returns   avg=+11.5%  med=-23.1%  p10=-65.8%  p90=+134.1%             |
|  Realized  $+7,303.13                                                  |
|  Raw incl dropped  trades=891  real=$+5,707.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b311 lab0311_s354_w4_11  1 100% +290.5 +290.5 +290.5 $   +122         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b820 lab0820_s405_w4_11  1 100% +254.8 +254.8 +254.8 $   +107         |
|  b821 lab0821_s405_w4_11  1 100% +242.9 +242.9 +242.9 $   +102         |
|  ... 102 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b20  lab0020_s202_w3_10  1   0% -88.9 -88.9 -88.9 $     -8       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b290 S352 AAPL260803C00315000 x1 take_profit (+188.3%                 |
|  b320 S356 AAPL260814C00330000 x1 take_profit (+54.0%)                 |
|  b328 S357 AAPL260821C00335000 x1 take_profit (+54.7%)                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (12)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260803C00315000          21   +188.3%   $ +1,618.50               |
|  AAPL260814C00330000           7    +54.0%   $   +225.75               |
|  AAPL260821C00335000           5    +54.7%   $   +175.00               |
|  T260807C00023000              6    -22.2%   $    -84.00               |
|  OXY260807C00059000            4    +27.4%   $    +68.00               |
|  SMCI260807P00025000           3    -46.5%   $    -60.00               |
|  SMCI260807P00025500           1    -45.5%   $    -25.00               |
|  NFLX260807C00075000           2    -24.0%   $    -24.00               |
|  ... 4 more position(s)                                                |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-03.log
elapsed=0.6s reconcile=0.27s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.6s. run=#5819 https://github.com/28twagg-ops/TradingBot/actions/runs/30815928929
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.5% (22/891)
# Options signal frequency

_Generated 2026-08-03T09:01:31.032640_

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
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    60 | INFO |
| Total closed lots           |   402 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=466.6 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260803T130547Z

- UTC timestamp: `20260803T130547Z`
- GitHub run: [#5820](https://github.com/28twagg-ops/TradingBot/actions/runs/30816300088)
- Run id: `30816300088`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T09:05:50.837961-04:00","date":"2026-08-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.55},"signals":0,"placed":0,"equity":135076.6,"open_positions":12,"pending_orders":0,"open_lots":60,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5820","github_run_id":"30816300088","status":"ok"}
```

### Live bot full output

```text
13:05:47  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.60|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $466.60|
|  Cash                                                           $153.29|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $313.31|
|  Open P&L                                                        $-0.01|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (4 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  APG      MomReversal     $30.93     $38.85   $38.00   -2.2%   $-0.69  |
|  CINF     Pullback50      $95.53     $175.04  $178.00  +1.7%   $+1.59  |
|  MP       MomReversal     $93.97     $41.37   $41.41   +0.1%   $+0.08  |
|  PWR      EarningsDrift   $92.89     $667.29  $660.25  -1.1%   $-0.99  |
|                                                                        |
|  Total invested                                                 $313.31|
|  Total open P&L                                                  $-0.01|
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
|  2026-07-31  SELL  MPWR  EarningsDrift  $94.50  P&L $+0.30             |
|  2026-07-31  SELL  LECO  EarningsDrift  $93.79  P&L $-0.10             |
|  2026-07-31  SELL  NVT  EarningsDrift  $89.90  P&L $-0.43              |
|  2026-07-31  SELL  AVB  Pullback50  $93.36  P&L $-0.58                 |
|  2026-07-31  SELL  CI  Pullback50  $93.26  P&L $-0.49                  |
|  2026-07-31  SELL  FFIV  Pullback50  $91.92  P&L $-0.54                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=60 paper_keys=yes dry_run=False
  alpaca positions=14
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-03T09:05:50.837961-04:00 ===

[Run context]
After hours (09:05 ET) — exit summary only.
Paper auth OK — equity $135076.60, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $135,076.60                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             60                                      |
|  Broker option positions       12                                      |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=357  buckets=110  win=39%                            |
|  Returns   avg=+11.5%  med=-23.1%  p10=-65.8%  p90=+134.1%             |
|  Realized  $+7,303.13                                                  |
|  Raw incl dropped  trades=891  real=$+5,707.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b311 lab0311_s354_w4_11  1 100% +290.5 +290.5 +290.5 $   +122         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b820 lab0820_s405_w4_11  1 100% +254.8 +254.8 +254.8 $   +107         |
|  b821 lab0821_s405_w4_11  1 100% +242.9 +242.9 +242.9 $   +102         |
|  ... 102 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b20  lab0020_s202_w3_10  1   0% -88.9 -88.9 -88.9 $     -8       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b290 S352 AAPL260803C00315000 x1 take_profit (+188.3%                 |
|  b320 S356 AAPL260814C00330000 x1 take_profit (+54.0%)                 |
|  b328 S357 AAPL260821C00335000 x1 take_profit (+54.7%)                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (12)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260803C00315000          21   +188.3%   $ +1,618.50               |
|  AAPL260814C00330000           7    +54.0%   $   +225.75               |
|  AAPL260821C00335000           5    +54.7%   $   +175.00               |
|  T260807C00023000              6    -22.2%   $    -84.00               |
|  OXY260807C00059000            4    +27.4%   $    +68.00               |
|  SMCI260807P00025000           3    -46.5%   $    -60.00               |
|  SMCI260807P00025500           1    -45.5%   $    -25.00               |
|  NFLX260807C00075000           2    -24.0%   $    -24.00               |
|  ... 4 more position(s)                                                |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-03.log
elapsed=1.2s reconcile=0.55s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.2s. run=#5820 https://github.com/28twagg-ops/TradingBot/actions/runs/30816300088
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.5% (22/891)
# Options signal frequency

_Generated 2026-08-03T09:05:57.533326_

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
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    60 | INFO |
| Total closed lots           |   402 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=466.6 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260803T131041Z

- UTC timestamp: `20260803T131041Z`
- GitHub run: [#5821](https://github.com/28twagg-ops/TradingBot/actions/runs/30816683863)
- Run id: `30816683863`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T09:10:44.617489-04:00","date":"2026-08-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.4,"phases_s":{"reconcile":0.1},"signals":0,"placed":0,"equity":134694.76,"open_positions":12,"pending_orders":0,"open_lots":60,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5821","github_run_id":"30816683863","status":"ok"}
```

### Live bot full output

```text
13:10:42  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.49|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $466.49|
|  Cash                                                           $153.29|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $313.20|
|  Open P&L                                                        $-0.12|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (4 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  APG      MomReversal     $30.93     $38.85   $38.00   -2.2%   $-0.69  |
|  CINF     Pullback50      $95.53     $175.04  $178.00  +1.7%   $+1.59  |
|  MP       MomReversal     $93.86     $41.37   $41.36   -0.0%   $-0.03  |
|  PWR      EarningsDrift   $92.89     $667.29  $660.25  -1.1%   $-0.99  |
|                                                                        |
|  Total invested                                                 $313.20|
|  Total open P&L                                                  $-0.12|
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
|  2026-07-31  SELL  MPWR  EarningsDrift  $94.50  P&L $+0.30             |
|  2026-07-31  SELL  LECO  EarningsDrift  $93.79  P&L $-0.10             |
|  2026-07-31  SELL  NVT  EarningsDrift  $89.90  P&L $-0.43              |
|  2026-07-31  SELL  AVB  Pullback50  $93.36  P&L $-0.58                 |
|  2026-07-31  SELL  CI  Pullback50  $93.26  P&L $-0.49                  |
|  2026-07-31  SELL  FFIV  Pullback50  $91.92  P&L $-0.54                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=60 paper_keys=yes dry_run=False
  alpaca positions=14
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-03T09:10:44.617489-04:00 ===

[Run context]
After hours (09:10 ET) — exit summary only.
Paper auth OK — equity $134694.76, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $134,694.76                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             60                                      |
|  Broker option positions       12                                      |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=357  buckets=110  win=39%                            |
|  Returns   avg=+11.5%  med=-23.1%  p10=-65.8%  p90=+134.1%             |
|  Realized  $+7,303.13                                                  |
|  Raw incl dropped  trades=891  real=$+5,707.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b311 lab0311_s354_w4_11  1 100% +290.5 +290.5 +290.5 $   +122         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b820 lab0820_s405_w4_11  1 100% +254.8 +254.8 +254.8 $   +107         |
|  b821 lab0821_s405_w4_11  1 100% +242.9 +242.9 +242.9 $   +102         |
|  ... 102 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b20  lab0020_s202_w3_10  1   0% -88.9 -88.9 -88.9 $     -8       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b290 S352 AAPL260803C00315000 x1 take_profit (+188.3%                 |
|  b320 S356 AAPL260814C00330000 x1 take_profit (+54.0%)                 |
|  b328 S357 AAPL260821C00335000 x1 take_profit (+54.7%)                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (12)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260803C00315000          21   +188.3%   $ +1,618.50               |
|  AAPL260814C00330000           7    +54.0%   $   +225.75               |
|  AAPL260821C00335000           5    +54.7%   $   +175.00               |
|  T260807C00023000              6    -22.2%   $    -84.00               |
|  OXY260807C00059000            4    +27.4%   $    +68.00               |
|  SMCI260807P00025000           3    -46.5%   $    -60.00               |
|  SMCI260807P00025500           1    -45.5%   $    -25.00               |
|  NFLX260807C00075000           2    -24.0%   $    -24.00               |
|  ... 4 more position(s)                                                |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-03.log
elapsed=0.4s reconcile=0.1s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.4s. run=#5821 https://github.com/28twagg-ops/TradingBot/actions/runs/30816683863
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.5% (22/891)
# Options signal frequency

_Generated 2026-08-03T09:10:50.547869_

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
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    60 | INFO |
| Total closed lots           |   402 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=466.49 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260803T131546Z

- UTC timestamp: `20260803T131546Z`
- GitHub run: [#5822](https://github.com/28twagg-ops/TradingBot/actions/runs/30817074178)
- Run id: `30817074178`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T09:15:49.445823-04:00","date":"2026-08-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.4,"phases_s":{"reconcile":0.13},"signals":0,"placed":0,"equity":134809.4,"open_positions":12,"pending_orders":0,"open_lots":60,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5822","github_run_id":"30817074178","status":"ok"}
```

### Live bot full output

```text
13:15:47  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.83|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $466.83|
|  Cash                                                           $153.29|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $313.54|
|  Open P&L                                                        $+0.22|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (4 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  APG      MomReversal     $30.93     $38.85   $38.00   -2.2%   $-0.69  |
|  CINF     Pullback50      $95.53     $175.04  $178.00  +1.7%   $+1.59  |
|  MP       MomReversal     $93.74     $41.37   $41.31   -0.2%   $-0.14  |
|  PWR      EarningsDrift   $93.34     $667.29  $663.49  -0.6%   $-0.54  |
|                                                                        |
|  Total invested                                                 $313.54|
|  Total open P&L                                                  $+0.22|
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
|  2026-07-31  SELL  MPWR  EarningsDrift  $94.50  P&L $+0.30             |
|  2026-07-31  SELL  LECO  EarningsDrift  $93.79  P&L $-0.10             |
|  2026-07-31  SELL  NVT  EarningsDrift  $89.90  P&L $-0.43              |
|  2026-07-31  SELL  AVB  Pullback50  $93.36  P&L $-0.58                 |
|  2026-07-31  SELL  CI  Pullback50  $93.26  P&L $-0.49                  |
|  2026-07-31  SELL  FFIV  Pullback50  $91.92  P&L $-0.54                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=60 paper_keys=yes dry_run=False
  alpaca positions=14
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-03T09:15:49.445823-04:00 ===

[Run context]
After hours (09:15 ET) — exit summary only.
Paper auth OK — equity $134809.40, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $134,809.40                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             60                                      |
|  Broker option positions       12                                      |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=357  buckets=110  win=39%                            |
|  Returns   avg=+11.5%  med=-23.1%  p10=-65.8%  p90=+134.1%             |
|  Realized  $+7,303.13                                                  |
|  Raw incl dropped  trades=891  real=$+5,707.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b311 lab0311_s354_w4_11  1 100% +290.5 +290.5 +290.5 $   +122         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b820 lab0820_s405_w4_11  1 100% +254.8 +254.8 +254.8 $   +107         |
|  b821 lab0821_s405_w4_11  1 100% +242.9 +242.9 +242.9 $   +102         |
|  ... 102 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b20  lab0020_s202_w3_10  1   0% -88.9 -88.9 -88.9 $     -8       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b290 S352 AAPL260803C00315000 x1 take_profit (+188.3%                 |
|  b320 S356 AAPL260814C00330000 x1 take_profit (+54.0%)                 |
|  b328 S357 AAPL260821C00335000 x1 take_profit (+54.7%)                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (12)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260803C00315000          21   +188.3%   $ +1,618.50               |
|  AAPL260814C00330000           7    +54.0%   $   +225.75               |
|  AAPL260821C00335000           5    +54.7%   $   +175.00               |
|  T260807C00023000              6    -22.2%   $    -84.00               |
|  OXY260807C00059000            4    +27.4%   $    +68.00               |
|  SMCI260807P00025000           3    -46.5%   $    -60.00               |
|  SMCI260807P00025500           1    -45.5%   $    -25.00               |
|  NFLX260807C00075000           2    -24.0%   $    -24.00               |
|  ... 4 more position(s)                                                |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-03.log
elapsed=0.4s reconcile=0.13s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.4s. run=#5822 https://github.com/28twagg-ops/TradingBot/actions/runs/30817074178
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.5% (22/891)
# Options signal frequency

_Generated 2026-08-03T09:15:55.286689_

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
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    60 | INFO |
| Total closed lots           |   402 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=466.83 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260803T132056Z

- UTC timestamp: `20260803T132056Z`
- GitHub run: [#5823](https://github.com/28twagg-ops/TradingBot/actions/runs/30817463435)
- Run id: `30817463435`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T09:21:00.940649-04:00","date":"2026-08-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.52},"signals":0,"placed":0,"equity":135501.4,"open_positions":12,"pending_orders":0,"open_lots":60,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5823","github_run_id":"30817463435","status":"ok"}
```

### Live bot full output

```text
13:20:58  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.81|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $467.81|
|  Cash                                                           $153.29|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $314.52|
|  Open P&L                                                        $+1.21|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (4 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  APG      MomReversal     $32.16     $38.85   $39.52   +1.7%   $+0.55  |
|  CINF     Pullback50      $95.53     $175.04  $178.00  +1.7%   $+1.59  |
|  MP       MomReversal     $93.49     $41.37   $41.20   -0.4%   $-0.39  |
|  PWR      EarningsDrift   $93.34     $667.29  $663.49  -0.6%   $-0.54  |
|                                                                        |
|  Total invested                                                 $314.52|
|  Total open P&L                                                  $+1.21|
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
|  2026-07-31  SELL  MPWR  EarningsDrift  $94.50  P&L $+0.30             |
|  2026-07-31  SELL  LECO  EarningsDrift  $93.79  P&L $-0.10             |
|  2026-07-31  SELL  NVT  EarningsDrift  $89.90  P&L $-0.43              |
|  2026-07-31  SELL  AVB  Pullback50  $93.36  P&L $-0.58                 |
|  2026-07-31  SELL  CI  Pullback50  $93.26  P&L $-0.49                  |
|  2026-07-31  SELL  FFIV  Pullback50  $91.92  P&L $-0.54                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=60 paper_keys=yes dry_run=False
  alpaca positions=14
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-03T09:21:00.940649-04:00 ===

[Run context]
After hours (09:21 ET) — exit summary only.
Paper auth OK — equity $135501.40, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $135,501.40                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             60                                      |
|  Broker option positions       12                                      |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=357  buckets=110  win=39%                            |
|  Returns   avg=+11.5%  med=-23.1%  p10=-65.8%  p90=+134.1%             |
|  Realized  $+7,303.13                                                  |
|  Raw incl dropped  trades=891  real=$+5,707.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b311 lab0311_s354_w4_11  1 100% +290.5 +290.5 +290.5 $   +122         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b820 lab0820_s405_w4_11  1 100% +254.8 +254.8 +254.8 $   +107         |
|  b821 lab0821_s405_w4_11  1 100% +242.9 +242.9 +242.9 $   +102         |
|  ... 102 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b20  lab0020_s202_w3_10  1   0% -88.9 -88.9 -88.9 $     -8       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b290 S352 AAPL260803C00315000 x1 take_profit (+188.3%                 |
|  b320 S356 AAPL260814C00330000 x1 take_profit (+54.0%)                 |
|  b328 S357 AAPL260821C00335000 x1 take_profit (+54.7%)                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (12)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260803C00315000          21   +188.3%   $ +1,618.50               |
|  AAPL260814C00330000           7    +54.0%   $   +225.75               |
|  AAPL260821C00335000           5    +54.7%   $   +175.00               |
|  T260807C00023000              6    -22.2%   $    -84.00               |
|  OXY260807C00059000            4    +27.4%   $    +68.00               |
|  SMCI260807P00025000           3    -46.5%   $    -60.00               |
|  SMCI260807P00025500           1    -45.5%   $    -25.00               |
|  NFLX260807C00075000           2    -24.0%   $    -24.00               |
|  ... 4 more position(s)                                                |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-03.log
elapsed=0.9s reconcile=0.52s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.9s. run=#5823 https://github.com/28twagg-ops/TradingBot/actions/runs/30817463435
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.5% (22/891)
# Options signal frequency

_Generated 2026-08-03T09:21:06.872574_

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
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    60 | INFO |
| Total closed lots           |   402 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=467.81 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
