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

## Run 20260803T132720Z

- UTC timestamp: `20260803T132720Z`
- GitHub run: [#5824](https://github.com/28twagg-ops/TradingBot/actions/runs/30817850323)
- Run id: `30817850323`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T09:27:23.675337-04:00","date":"2026-08-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.4,"phases_s":{"reconcile":0.09},"signals":0,"placed":0,"equity":134537.4,"open_positions":12,"pending_orders":0,"open_lots":60,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5824","github_run_id":"30817850323","status":"ok"}
```

### Live bot full output

```text
13:27:21  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:27 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $468.27|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $468.27|
|  Cash                                                           $153.29|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $314.98|
|  Open P&L                                                        $+1.66|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (4 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  APG      MomReversal     $32.16     $38.85   $39.52   +1.7%   $+0.55  |
|  CINF     Pullback50      $95.53     $175.04  $178.00  +1.7%   $+1.59  |
|  MP       MomReversal     $93.94     $41.37   $41.40   +0.1%   $+0.06  |
|  PWR      EarningsDrift   $93.34     $667.29  $663.49  -0.6%   $-0.54  |
|                                                                        |
|  Total invested                                                 $314.98|
|  Total open P&L                                                  $+1.66|
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
=== options_morning_bot (PAPER) 2026-08-03T09:27:23.675337-04:00 ===

[Run context]
After hours (09:27 ET) — exit summary only.
Paper auth OK — equity $134537.40, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $134,537.40                             |
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
elapsed=0.4s reconcile=0.09s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.4s. run=#5824 https://github.com/28twagg-ops/TradingBot/actions/runs/30817850323
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.5% (22/891)
# Options signal frequency

_Generated 2026-08-03T09:27:29.446466_

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
equity=468.27 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260803T133052Z

- UTC timestamp: `20260803T133052Z`
- GitHub run: [#5825](https://github.com/28twagg-ops/TradingBot/actions/runs/30818231044)
- Run id: `30818231044`
- Live bot: exit=`0`, duration=`217s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T09:27:23.675337-04:00","date":"2026-08-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.4,"phases_s":{"reconcile":0.09},"signals":0,"placed":0,"equity":134537.4,"open_positions":12,"pending_orders":0,"open_lots":60,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5824","github_run_id":"30817850323","status":"ok"}
```

### Live bot full output

```text
13:30:53  INFO      Mode: morning_prep
13:30:56  INFO        [prep_positions] 4/4 (4 valid)
13:30:56  INFO      Fetching tickers (universe=both)...
13:30:56  INFO        S&P 500: 503
13:30:56  INFO        MidCap 400: 400
13:30:56  INFO        Total: 903 tickers
13:30:58  INFO        [prep_universe] 40/899 (40 valid)
13:30:59  INFO        [prep_universe] 80/899 (80 valid)
13:31:00  INFO        [prep_universe] 120/899 (120 valid)
13:31:02  INFO        [prep_universe] 160/899 (160 valid)
13:31:03  INFO        [prep_universe] 200/899 (199 valid)
13:31:10  INFO        [prep_universe] 240/899 (238 valid)
13:31:21  INFO        [prep_universe] 280/899 (278 valid)
13:31:35  INFO        [prep_universe] 320/899 (318 valid)
13:31:48  INFO        [prep_universe] 360/899 (358 valid)
13:31:58  INFO        [prep_universe] 400/899 (397 valid)
13:32:12  INFO        [prep_universe] 440/899 (437 valid)
13:32:22  INFO        [prep_universe] 480/899 (477 valid)
13:32:35  INFO        [prep_universe] 520/899 (517 valid)
13:32:46  INFO        [prep_universe] 560/899 (557 valid)
13:32:59  INFO        [prep_universe] 600/899 (597 valid)
13:33:09  INFO        [prep_universe] 640/899 (637 valid)
13:33:23  INFO        [prep_universe] 680/899 (677 valid)
13:33:33  INFO        [prep_universe] 720/899 (717 valid)
13:33:46  INFO        [prep_universe] 760/899 (757 valid)
13:34:00  INFO        [prep_universe] 800/899 (797 valid)
13:34:10  INFO        [prep_universe] 840/899 (836 valid)
13:34:23  INFO        [prep_universe] 880/899 (876 valid)
13:34:27  INFO        [prep_universe] 899/899 (895 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $465.85|
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
|  Open positions                                                       4|
|  Invested                                                       $312.66|
|  Open P&L                                                        $-0.66|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  APG      MomReversal     $32.10     $38.85   $39.44   +1.5%   $+0.48  |
|  CINF     Pullback50      $95.42     $175.04  $177.79  +1.6%   $+1.48  |
|  MP       MomReversal     $92.58     $41.37   $40.80   -1.4%   $-1.30  |
|  PWR      EarningsDrift   $92.57     $667.29  $657.95  -1.4%   $-1.31  |
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
|  Exit candidates                                                      4|
|  Signal candidates                                                   34|
|  Universe scanned                                                   899|
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
=== options_morning_bot (PAPER) 2026-08-03T09:34:30.929675-04:00 ===

[Run context]
Paper auth OK — equity $130455.34, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-03 09:34:33,101 INFO   EXIT [b113|lab0113_s212_w3_1045_1120_r2|S212] stop_loss (-82.3%) SELL 1 OXY260807C00059000 @<= 0.12
2026-08-03 09:34:37,378 INFO   EXIT [b238|lab0238_s401_w3_1045_1120_r1|S401] take_profit (+62.7%) SELL 1 V260807C00380000 @<= 0.97

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260803T133602Z

- UTC timestamp: `20260803T133602Z`
- GitHub run: [#5826](https://github.com/28twagg-ops/TradingBot/actions/runs/30818617455)
- Run id: `30818617455`
- Live bot: exit=`0`, duration=`219s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T09:27:23.675337-04:00","date":"2026-08-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.4,"phases_s":{"reconcile":0.09},"signals":0,"placed":0,"equity":134537.4,"open_positions":12,"pending_orders":0,"open_lots":60,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5824","github_run_id":"30817850323","status":"ok"}
```

### Live bot full output

```text
13:36:03  INFO      Mode: morning_prep
13:36:05  INFO        [prep_positions] 4/4 (4 valid)
13:36:05  INFO      Fetching tickers (universe=both)...
13:36:05  INFO        S&P 500: 503
13:36:05  INFO        MidCap 400: 400
13:36:05  INFO        Total: 903 tickers
13:36:06  INFO        [prep_universe] 40/899 (40 valid)
13:36:08  INFO        [prep_universe] 80/899 (80 valid)
13:36:09  INFO        [prep_universe] 120/899 (120 valid)
13:36:11  INFO        [prep_universe] 160/899 (160 valid)
13:36:12  INFO        [prep_universe] 200/899 (199 valid)
13:36:19  INFO        [prep_universe] 240/899 (238 valid)
13:36:32  INFO        [prep_universe] 280/899 (278 valid)
13:36:43  INFO        [prep_universe] 320/899 (318 valid)
13:36:56  INFO        [prep_universe] 360/899 (358 valid)
13:37:06  INFO        [prep_universe] 400/899 (397 valid)
13:37:19  INFO        [prep_universe] 440/899 (437 valid)
13:37:32  INFO        [prep_universe] 480/899 (477 valid)
13:37:42  INFO        [prep_universe] 520/899 (517 valid)
13:37:56  INFO        [prep_universe] 560/899 (557 valid)
13:38:09  INFO        [prep_universe] 600/899 (597 valid)
13:38:19  INFO        [prep_universe] 640/899 (637 valid)
13:38:32  INFO        [prep_universe] 680/899 (677 valid)
13:38:42  INFO        [prep_universe] 720/899 (717 valid)
13:38:55  INFO        [prep_universe] 760/899 (757 valid)
13:39:08  INFO        [prep_universe] 800/899 (797 valid)
13:39:18  INFO        [prep_universe] 840/899 (836 valid)
13:39:32  INFO        [prep_universe] 880/899 (876 valid)
13:39:38  INFO        [prep_universe] 899/899 (895 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.28|
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
|  Open positions                                                       4|
|  Invested                                                       $314.35|
|  Open P&L                                                        $+1.03|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  APG      MomReversal     $31.95     $38.85   $39.26   +1.1%   $+0.34  |
|  CINF     Pullback50      $95.41     $175.04  $177.78  +1.6%   $+1.47  |
|  MP       MomReversal     $94.40     $41.37   $41.60   +0.5%   $+0.51  |
|  PWR      EarningsDrift   $92.59     $667.29  $658.12  -1.4%   $-1.29  |
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
|  Exit candidates                                                      4|
|  Signal candidates                                                   32|
|  Universe scanned                                                   899|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=60 paper_keys=yes dry_run=False
  alpaca positions=13
  FLAG b238|S401|61bed18f missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-03T09:39:43.121067-04:00 ===

[Run context]
Paper auth OK — equity $130081.30, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-03 09:39:45,933 INFO   EXIT [b195|lab0195_s218_w2_1005_1045_r2|S218] take_profit (+111.4%) SELL 1 META260803C00600000 @<= 0.28
2026-08-03 09:39:46,849 INFO   EXIT [b235|lab0235_s401_w1_0928_1005_r2|S401] take_profit (+56.0%) SELL 1 NFLX260807C00075000 @<= 0.74
2026-08-03 09:39:47,030 INFO   EXIT [b112|lab0112_s212_w3_1045_1120_r1|S212] stop_loss (-58.1%) SELL 1 OXY260807C00059000 @<= 0.23

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260803T134104Z

- UTC timestamp: `20260803T134104Z`
- GitHub run: [#5827](https://github.com/28twagg-ops/TradingBot/actions/runs/30819005975)
- Run id: `30819005975`
- Live bot: exit=`0`, duration=`217s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T09:27:23.675337-04:00","date":"2026-08-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.4,"phases_s":{"reconcile":0.09},"signals":0,"placed":0,"equity":134537.4,"open_positions":12,"pending_orders":0,"open_lots":60,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5824","github_run_id":"30817850323","status":"ok"}
```

### Live bot full output

```text
13:41:04  INFO      Mode: morning_prep
13:41:05  INFO        [prep_positions] 4/4 (4 valid)
13:41:05  INFO        Universe cache hit: 903 tickers (tickers_2026-08-03.json)
13:41:06  INFO        [prep_universe] 40/899 (40 valid)
13:41:08  INFO        [prep_universe] 80/899 (80 valid)
13:41:09  INFO        [prep_universe] 120/899 (120 valid)
13:41:10  INFO        [prep_universe] 160/899 (160 valid)
13:41:11  INFO        [prep_universe] 200/899 (199 valid)
13:41:21  INFO        [prep_universe] 240/899 (238 valid)
13:41:31  INFO        [prep_universe] 280/899 (278 valid)
13:41:45  INFO        [prep_universe] 320/899 (318 valid)
13:41:58  INFO        [prep_universe] 360/899 (358 valid)
13:42:08  INFO        [prep_universe] 400/899 (397 valid)
13:42:21  INFO        [prep_universe] 440/899 (437 valid)
13:42:31  INFO        [prep_universe] 480/899 (477 valid)
13:42:44  INFO        [prep_universe] 520/899 (517 valid)
13:42:57  INFO        [prep_universe] 560/899 (557 valid)
13:43:07  INFO        [prep_universe] 600/899 (597 valid)
13:43:20  INFO        [prep_universe] 640/899 (637 valid)
13:43:33  INFO        [prep_universe] 680/899 (677 valid)
13:43:43  INFO        [prep_universe] 720/899 (717 valid)
13:43:56  INFO        [prep_universe] 760/899 (757 valid)
13:44:09  INFO        [prep_universe] 800/899 (797 valid)
13:44:19  INFO        [prep_universe] 840/899 (836 valid)
13:44:32  INFO        [prep_universe] 880/899 (876 valid)
13:44:39  INFO        [prep_universe] 899/899 (895 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $468.38|
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
|  Open positions                                                       4|
|  Invested                                                       $315.09|
|  Open P&L                                                        $+1.77|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  APG      MomReversal     $31.87     $38.85   $39.16   +0.8%   $+0.26  |
|  CINF     Pullback50      $95.46     $175.04  $177.87  +1.6%   $+1.52  |
|  MP       MomReversal     $94.33     $41.37   $41.57   +0.5%   $+0.45  |
|  PWR      EarningsDrift   $93.43     $667.29  $664.12  -0.5%   $-0.45  |
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
|  Exit candidates                                                      4|
|  Signal candidates                                                   30|
|  Universe scanned                                                   899|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=57 paper_keys=yes dry_run=False
  alpaca positions=13
  FLAG b238|S401|61bed18f missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-03T09:44:42.981686-04:00 ===

[Run context]
Paper auth OK — equity $129433.24, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-03 09:44:44,654 INFO   EXIT [b19|lab0019_s202_w2_1005_1045_r2|S202] stop_loss (-58.5%) SELL 1 AAPL260803C00315000 @<= 0.14
2026-08-03 09:44:45,042 INFO   EXIT [b115|lab0115_s212_w4_1120_1135_r2|S212] stop_loss (-56.5%) SELL 1 OXY260807C00059000 @<= 0.28
2026-08-03 09:44:45,722 INFO   EXIT [b234|lab0234_s401_w1_0928_1005_r1|S401] take_profit (+56.0%) SELL 1 NFLX260807C00075000 @<= 0.75
2026-08-03 09:44:46,664 INFO   EXIT [b194|lab0194_s218_w2_1005_1045_r1|S218] take_profit (+220.5%) SELL 1 META260803C00600000 @<= 0.44
2026-08-03 09:44:47,236 INFO   EXIT [b241|lab0241_s401_w4_1120_1135_r2|S401] take_profit (+63.3%) SELL 1 PATH260807C00013000 @<= 0.50

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260803T134602Z

- UTC timestamp: `20260803T134602Z`
- GitHub run: [#5828](https://github.com/28twagg-ops/TradingBot/actions/runs/30819398049)
- Run id: `30819398049`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T09:27:23.675337-04:00","date":"2026-08-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.4,"phases_s":{"reconcile":0.09},"signals":0,"placed":0,"equity":134537.4,"open_positions":12,"pending_orders":0,"open_lots":60,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5824","github_run_id":"30817850323","status":"ok"}
```

### Live bot full output

```text
13:46:03  INFO      Mode: morning_scan
13:46:04  INFO        [positions] 4/4 (4 valid)
13:46:04  INFO        SELL MARKET [urgent] PWR closed
13:46:06  INFO        TX logged: SELL PWR  P&L -0.71%
13:46:06  INFO        SELL LIMIT MP  qty=2.269176014  limit=$41.47  id=fc08e2f0-37a5-4627-95f0-d62cb5bc5f26
13:46:26  INFO        SELL LIMIT filled MP (confirmed by position check)
13:46:26  INFO        TX logged: SELL MP  P&L 0.49%
13:46:26  INFO        SELL LIMIT APG  qty=0.813828965  limit=$39.14  id=38274bfa-34e6-4e02-97b6-8114c5e910b3
13:46:46  INFO        SELL LIMIT filled APG (confirmed by position check)
13:46:46  INFO        TX logged: SELL APG  P&L 0.86%
13:46:46  INFO        SELL LIMIT CINF  qty=0.536665067  limit=$178.18  id=dee305e6-7801-45e8-9fdb-e2800c2adcfe
13:47:06  INFO        SELL LIMIT filled CINF (confirmed by position check)
13:47:06  INFO        TX logged: SELL CINF  P&L 1.91%
13:47:06  INFO        Universe cache hit: 903 tickers (tickers_2026-08-03.json)
13:47:07  INFO        [universe] 40/903 (40 valid)
13:47:09  INFO        [universe] 80/903 (80 valid)
13:47:10  INFO        [universe] 120/903 (120 valid)
13:47:12  INFO        [universe] 160/903 (160 valid)
13:47:13  INFO        [universe] 200/903 (199 valid)
13:47:20  INFO        [universe] 240/903 (238 valid)
13:47:31  INFO        [universe] 280/903 (278 valid)
13:47:44  INFO        [universe] 320/903 (318 valid)
13:47:57  INFO        [universe] 360/903 (358 valid)
13:48:07  INFO        [universe] 400/903 (397 valid)
13:48:20  INFO        [universe] 440/903 (437 valid)
13:48:33  INFO        [universe] 480/903 (477 valid)
13:48:43  INFO        [universe] 520/903 (517 valid)
13:48:56  INFO        [universe] 560/903 (557 valid)
13:49:09  INFO        [universe] 600/903 (597 valid)
13:49:19  INFO        [universe] 640/903 (637 valid)
13:49:32  INFO        [universe] 680/903 (677 valid)
13:49:44  INFO        [universe] 720/903 (717 valid)
13:49:57  INFO        [universe] 760/903 (757 valid)
13:50:07  INFO        [universe] 800/903 (797 valid)
```

### Options bot full output

```text

## Run 20260803T135416Z

- UTC timestamp: `20260803T135416Z`
- GitHub run: [#5829](https://github.com/28twagg-ops/TradingBot/actions/runs/30819782916)
- Run id: `30819782916`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T09:27:23.675337-04:00","date":"2026-08-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.4,"phases_s":{"reconcile":0.09},"signals":0,"placed":0,"equity":134537.4,"open_positions":12,"pending_orders":0,"open_lots":60,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5824","github_run_id":"30817850323","status":"ok"}
```

### Live bot full output

```text
13:54:17  INFO      Mode: morning_scan
13:54:18  INFO        Universe cache hit: 903 tickers (tickers_2026-08-03.json)
13:54:19  INFO        [universe] 40/903 (40 valid)
13:54:20  INFO        [universe] 80/903 (80 valid)
13:54:21  INFO        [universe] 120/903 (120 valid)
13:54:22  INFO        [universe] 160/903 (160 valid)
13:54:24  INFO        [universe] 200/903 (199 valid)
13:54:31  INFO        [universe] 240/903 (238 valid)
13:54:44  INFO        [universe] 280/903 (278 valid)
13:54:54  INFO        [universe] 320/903 (318 valid)
13:55:07  INFO        [universe] 360/903 (358 valid)
```

### Options bot full output

```text

## Run 20260803T135607Z

- UTC timestamp: `20260803T135607Z`
- GitHub run: [#5830](https://github.com/28twagg-ops/TradingBot/actions/runs/30820179673)
- Run id: `30820179673`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T09:27:23.675337-04:00","date":"2026-08-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.4,"phases_s":{"reconcile":0.09},"signals":0,"placed":0,"equity":134537.4,"open_positions":12,"pending_orders":0,"open_lots":60,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5824","github_run_id":"30817850323","status":"ok"}
```

### Live bot full output

```text
13:56:10  INFO      Mode: morning_scan
13:56:10  INFO        Universe cache hit: 903 tickers (tickers_2026-08-03.json)
13:56:11  INFO        [universe] 40/903 (40 valid)
13:56:13  INFO        [universe] 80/903 (80 valid)
13:56:14  INFO        [universe] 120/903 (120 valid)
13:56:15  INFO        [universe] 160/903 (160 valid)
13:56:22  INFO        [universe] 200/903 (199 valid)
13:56:35  INFO        [universe] 240/903 (238 valid)
13:56:48  INFO        [universe] 280/903 (278 valid)
13:56:57  INFO        [universe] 320/903 (318 valid)
13:57:10  INFO        [universe] 360/903 (358 valid)
13:57:23  INFO        [universe] 400/903 (397 valid)
13:57:33  INFO        [universe] 440/903 (437 valid)
13:57:46  INFO        [universe] 480/903 (477 valid)
13:57:59  INFO        [universe] 520/903 (517 valid)
13:58:09  INFO        [universe] 560/903 (557 valid)
13:58:22  INFO        [universe] 600/903 (597 valid)
13:58:35  INFO        [universe] 640/903 (637 valid)
13:58:45  INFO        [universe] 680/903 (677 valid)
13:58:58  INFO        [universe] 720/903 (717 valid)
13:59:11  INFO        [universe] 760/903 (757 valid)
13:59:24  INFO        [universe] 800/903 (797 valid)
13:59:34  INFO        [universe] 840/903 (836 valid)
13:59:47  INFO        [universe] 880/903 (876 valid)
13:59:53  INFO        [universe] 903/903 (899 valid)
13:59:55  INFO        BUY  ALGN  $93.65  [Pullback50]  id=d3a4687e-632b-4230-a21a-185236ed13b7

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $468.25|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-08-03|
|  Universe                                                          both|
|  Mo~  Aug: VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Disabled                GapDown, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $468.25|
|  Cash                                                           $468.25|
|  Reserve                                          $23.41  (always kept)|
|  Available                                    $444.84  (for new trades)|
|  Trade size             $93.65  (20% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (0 open)                           |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
|  Buys today: 0  |  entry cap: 5  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (36010.7m))|
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
|                         SIGNALS FOUND  --  40                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  ALGN     Pullback50      eq     $174.52  46.2   -1.99   50MA bounce (+|
|  AES      Pullback50      eq     $14.70   38.1   -1.41   50MA bounce (-|
|  AVB      Pullback50      eq     $187.15  42.0   -2.99   50MA bounce (-|
|  CPT      Pullback50      eq     $111.77  46.8   -1.93   50MA bounce (-|
|  ED       Pullback50      eq     $108.51  38.9   -2.78   50MA bounce (-|
|  DUK      Pullback50      eq     $125.42  47.1   -3.00   50MA bounce (-|
|  EW       Pullback50      eq     $87.97   43.2   -2.33   50MA bounce (+|
|  ESS      Pullback50      eq     $287.98  39.2   -2.50   50MA bounce (+|
|  EQR      Pullback50      eq     $67.12   41.7   -2.38   50MA bounce (-|
|  ES       Pullback50      eq     $72.08   38.5   -1.98   50MA bounce (+|
|  HBAN     Pullback50      eq     $17.23   41.3   -1.75   50MA bounce (-|
|  KEY      Pullback50      eq     $22.75   42.6   -2.91   50MA bounce (+|
|  MAA      Pullback50      eq     $133.89  50.5   -2.24   50MA bounce (-|
|  REG      Pullback50      eq     $80.36   50.2   -3.15   50MA bounce (+|
|  SO       Pullback50      eq     $94.45   43.8   -2.67   50MA bounce (-|
|  LUV      Pullback50      eq     $46.62   46.8   -2.30   50MA bounce (+|
|  YUM      Pullback50      eq     $154.40  43.3   -2.43   50MA bounce (+|
|  ALSN     Pullback50      eq     $115.73  51.4   -2.71   50MA bounce (-|
|  ALLY     Pullback50      eq     $44.45   45.5   -2.05   50MA bounce (+|
|  AM       Pullback50      eq     $21.84   37.5   -2.81   50MA bounce (-|
|  ARW      Pullback50      eq     $217.65  61.7   -3.05   50MA bounce (+|
|  ATI      Pullback50      eq     $187.33  48.3   -2.58   50MA bounce (-|
|  BC       Pullback50      eq     $80.90   58.4   -2.28   50MA bounce (-|
|  BRX      Pullback50      eq     $31.71   50.9   -1.97   50MA bounce (+|
|  FLR      Pullback50      eq     $50.44   47.9   -2.42   50MA bounce (+|
|  GBCI     Pullback50      eq     $50.26   42.9   -2.62   50MA bounce (+|
|  HOG      Pullback50      eq     $25.10   50.1   -1.93   50MA bounce (-|
|  JEF      Pullback50      eq     $55.49   55.6   -2.78   50MA bounce (+|
|  MOG-A    Pullback50      eq     $389.52  49.3   -1.78   50MA bounce (-|
|  NBIX     Pullback50      eq     $167.58  45.7   -1.34   50MA bounce (-|
|  SLAB     Pullback50      eq     $218.07  50.7   -2.73   50MA bounce (-|
|  SSD      Pullback50      eq     $191.67  52.8   -2.43   50MA bounce (-|
|  SWX      Pullback50      eq     $90.04   39.3   -3.18   50MA bounce (+|
|  TEX      Pullback50      eq     $64.50   48.3   -1.87   50MA bounce (-|
|  TREX     Pullback50      eq     $44.76   52.3   -2.07   50MA bounce (+|
|  TWLO     Pullback50      eq     $199.84  35.8   -2.88   50MA bounce (-|
|  ULS      Pullback50      eq     $93.26   66.0   -2.19   50MA bounce (-|
|  UNM      Pullback50      eq     $88.39   49.8   -2.13   50MA bounce (+|
|  WAL      Pullback50      eq     $81.70   53.9   -1.74   50MA bounce (+|
|  WPC      Pullback50      eq     $73.95   60.0   -2.81   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] ALGN  Pullback50                                   $93.65|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] AES  Pullback50                                    $93.65|
13:59:55  INFO        BUY  AES  $93.65  [Pullback50]  id=254b4e84-41b7-4308-bc3b-ef1eaf0da180
13:59:56  INFO        BUY  AVB  $93.65  [Pullback50]  id=a9f13aa1-6114-4e54-8064-7a05bf44b119
13:59:56  INFO        BUY  CPT  $93.65  [Pullback50]  id=3199f80a-7ac3-49bc-ad6a-4738ade67364
13:59:56  INFO        BUY  ED  $70.24  [Pullback50]  id=533c0c02-484a-496e-babf-134b583c9207
```

### Options bot full output

```text

## Run 20260803T140114Z

- UTC timestamp: `20260803T140114Z`
- GitHub run: [#5831](https://github.com/28twagg-ops/TradingBot/actions/runs/30820576789)
- Run id: `30820576789`
- Live bot: exit=`0`, duration=`5s`
- Options bot: exit=`0`, duration=`152s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T10:01:21.973192-04:00","date":"2026-08-03","mode":"entry+manage","header":"entry+manage (44 new)","elapsed_s":142.9,"phases_s":{"reconcile":0.62,"cancel":0.15,"manage":13.31,"scan":65.89,"entries":57.84,"reconcile2":4.51},"signals":241,"placed":44,"equity":130299.22,"open_positions":18,"pending_orders":24,"open_lots":62,"submitted_today":44,"filled_today":20,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:ARM","S165:EOG","S165:OXY","S164:AMD","S164:ARM","S164:EOG","S164:OXY"],"github_run":"5831","github_run_id":"30820576789","status":"ok"}
```

### Live bot full output

```text
14:01:14  INFO      Mode: exits
14:01:15  INFO        Daily log -> logs/daily/2026-08-03.md
14:01:15  INFO        Daily log reconciled -> logs/daily/2026-08-03.md (4 ledger rows)
14:01:15  INFO        place_all_stops: checking 5 positions...
14:01:15  INFO        STOP-MARKET placed AES  qty=6 (pos=6.3718)  stop=$14.62  id=23533982-3e67-467b-bdb9-17e4f95b8852
14:01:15  INFO        STOP skipped ALGN: fractional (0.5376 shares) — software exit will handle it
14:01:15  INFO        STOP skipped AVB: fractional (0.5001 shares) — software exit will handle it
14:01:15  INFO        STOP skipped CPT: fractional (0.8366 shares) — software exit will handle it
14:01:15  INFO        STOP skipped ED: fractional (0.6468 shares) — software exit will handle it
14:01:17  INFO        [positions] 5/5 (5 valid)
14:01:17  INFO        SELL MARKET [urgent] ALGN closed
14:01:19  INFO        TX logged: SELL ALGN  P&L -0.54%
14:01:19  INFO        Daily log -> logs/daily/2026-08-03.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.32|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALGN  P&L -0.5%  $-0.51                        EXIT: stop_loss (-0.5%)|
|  CPT  P&L -0.4%  $-0.41                                            HOLD|
|  AVB  P&L -0.1%  $-0.10                                            HOLD|
|  ED  P&L +0.0%  $+0.03                                             HOLD|
|  AES  P&L +0.1%  $+0.06                                            HOLD|
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
|  ALGN                                        -0.54%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=52 paper_keys=yes dry_run=False
  alpaca positions=12
  FLAG b234|S401|dcac5f32 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-03T10:01:21.973192-04:00 ===

[Run context]
Paper auth OK — equity $130301.22, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-03 10:01:24,613 INFO   EXIT [b28|lab0028_s203_w3_1045_1120_r1|S203] stop_loss (-54.5%) SELL 1 SMCI260807P00025500 @<= 0.26
2026-08-03 10:01:31,775 INFO   EXIT [b181|lab0181_s217_w2_1005_1045_r2|S217] take_profit (+1045.5%) SELL 1 META260803C00600000 @<= 1.52
2026-08-03 10:01:35,150 INFO   EXIT [b18|lab0018_s202_w2_1005_1045_r1|S202] stop_loss (-78.0%) SELL 1 AAPL260803C00315000 @<= 0.10
2026-08-03 10:01:35,511 INFO   EXIT [b114|lab0114_s212_w4_1120_1135_r1|S212] stop_loss (-59.7%) SELL 1 OXY260807C00059000 @<= 0.22
2026-08-03 10:01:36,416 INFO   EXIT [b26|lab0026_s203_w2_1005_1045_r1|S203] stop_loss (-53.5%) SELL 1 SMCI260807P00025000 @<= 0.21

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 241 signal(s); top: ['S165:AMD', 'S165:ARM', 'S165:EOG', 'S165:OXY', 'S164:AMD', 'S164:ARM', 'S164:EOG', 'S164:OXY']
Paper lab: $130037 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 226 no tradeable call, 168 pending order
Placed 44 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $130,299.22                             |
|  Signals this run              241                                     |
|  Orders submitted (session)    44                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       44                                      |
|  Open virtual lots             62                                      |
|  Broker option positions       18                                      |
|  Pending orders                24                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=375  buckets=127  win=40%                            |
|  Returns   avg=+14.3%  med=-23.1%  p10=-65.9%  p90=+138.6%             |
|  Realized  $+7,395.13                                                  |
|  Raw incl dropped  trades=909  real=$+5,799.58                         |
|  Today     trades=17  avg=+66.9%  med=+8.3%  real=$+57.00              |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b181 lab0181_s217_w2_10  1 100% +1007.1 +1007.1 +1007.1 $   +141      |
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b311 lab0311_s354_w4_11  1 100% +290.5 +290.5 +290.5 $   +122         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b820 lab0820_s405_w4_11  1 100% +254.8 +254.8 +254.8 $   +107         |
|  ... 119 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b20  lab0020_s202_w3_10  1   0% -88.9 -88.9 -88.9 $     -8       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (24)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S403:SPY(2), S350:AMD(2), S351:AMD(2)   |
+------------------------------------------------------------------------+
|  b262 S403 SPY      limit=0.52                                         |
|  b263 S403 SPY      limit=0.52                                         |
|  b276 S350 AMD      limit=0.48                                         |
|  b277 S350 AMD      limit=0.48                                         |
|  b280 S351 AMD      limit=0.48                                         |
|  ... 19 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (18)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260803C00315000          18    -78.0%   $   -574.71               |
|  META260803C00600000           3   +711.4%   $   +313.00               |
|  AAPL260814C00330000           6    -13.0%   $    -46.50               |
|  SMCI260807P00025000           2    -51.2%   $    -44.00               |
|  T260807C00023000              6    +11.1%   $    +42.00               |
|  MSFT260807C00525000           2    -17.6%   $    -24.00               |
|  UBER260807C00077000           2    +18.2%   $    +20.00               |
|  NVDA260807C00212500           2    +12.5%   $    +18.00               |
|  ... 10 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-03.log
elapsed=142.9s reconcile=0.62s cancel=0.15s manage=13.31s scan=65.89s entries=57.84s
STATUS: options_morning_bot run complete (PAPER) elapsed=142.9s. run=#5831 https://github.com/28twagg-ops/TradingBot/actions/runs/30820576789
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.csv
Summary: 17 buckets closed trades, $+57.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.4% (22/909)
# Options signal frequency

_Generated 2026-08-03T10:03:50.404911_

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    62 | INFO |
| Total closed lots           |   420 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=467.44 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260803T140541Z

- UTC timestamp: `20260803T140541Z`
- GitHub run: [#5832](https://github.com/28twagg-ops/TradingBot/actions/runs/30820984199)
- Run id: `30820984199`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`190s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T10:05:45.683211-04:00","date":"2026-08-03","mode":"entry+manage","header":"entry+manage (41 new)","elapsed_s":182.1,"phases_s":{"reconcile":0.48,"cancel":0.08,"manage":13.46,"scan":59.21,"entries":106.93,"reconcile2":1.49},"signals":261,"placed":41,"equity":129845.26,"open_positions":26,"pending_orders":24,"open_lots":99,"submitted_today":85,"filled_today":61,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:ARM","S165:EOG","S165:OXY","S164:AMD","S164:ARM","S164:EOG","S164:OXY"],"github_run":"5832","github_run_id":"30820984199","status":"ok"}
```

### Live bot full output

```text
14:05:42  INFO      Mode: exits
14:05:42  INFO        Daily log -> logs/daily/2026-08-03.md
14:05:42  INFO        Daily log reconciled -> logs/daily/2026-08-03.md (5 ledger rows)
14:05:42  INFO        place_all_stops: checking 4 positions...
14:05:43  INFO        STOP already live AES @ $14.62
14:05:43  INFO        STOP skipped AVB: fractional (0.5001 shares) — software exit will handle it
14:05:43  INFO        STOP skipped CPT: fractional (0.8366 shares) — software exit will handle it
14:05:43  INFO        STOP skipped ED: fractional (0.6468 shares) — software exit will handle it
14:05:43  INFO        [positions] 4/4 (4 valid)
14:05:43  INFO        Daily log -> logs/daily/2026-08-03.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.91|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CPT  P&L -0.4%  $-0.35                                            HOLD|
|  AES  P&L +0.1%  $+0.09                                            HOLD|
|  AVB  P&L +0.2%  $+0.14                                            HOLD|
|  ED  P&L +0.3%  $+0.18                                             HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           4|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                4|
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
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-03T10:05:45.683211-04:00 ===

[Run context]
Paper auth OK — equity $129845.26, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-03 10:05:55,898 INFO   EXIT [b180|lab0180_s217_w2_1005_1045_r1|S217] take_profit (+786.4%) SELL 1 META260803C00600000 @<= 1.31
2026-08-03 10:05:58,933 INFO   EXIT [b299|lab0299_s353_w2_1005_1045_r2|S353] stop_loss (-80.5%) SELL 1 AAPL260803C00315000 @<= 0.09

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 261 signal(s); top: ['S165:AMD', 'S165:ARM', 'S165:EOG', 'S165:OXY', 'S164:AMD', 'S164:ARM', 'S164:EOG', 'S164:OXY']
Paper lab: $130355 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 396 no tradeable call, 19 already attempted today, 303 pending order
Placed 41 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,845.26                             |
|  Signals this run              261                                     |
|  Orders submitted (session)    85                                      |
|  Orders filled today (ledger)  61                                      |
|  Entries placed this run       41                                      |
|  Open virtual lots             99                                      |
|  Broker option positions       26                                      |
|  Pending orders                24                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=380  buckets=132  win=40%                            |
|  Returns   avg=+16.5%  med=-22.6%  p10=-66.2%  p90=+138.8%             |
|  Realized  $+7,495.13                                                  |
|  Raw incl dropped  trades=914  real=$+5,899.58                         |
|  Today     trades=19  avg=+102.6%  med=+8.3%  real=$+157.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b181 lab0181_s217_w2_10  1 100% +1007.1 +1007.1 +1007.1 $   +141      |
|  b180 lab0180_s217_w2_10  1 100% +885.7 +885.7 +885.7 $   +124         |
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b311 lab0311_s354_w4_11  1 100% +290.5 +290.5 +290.5 $   +122         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  ... 124 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b280 lab0280_s351_w1_09  1   0% -91.7 -91.7 -91.7 $    -44       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (24)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S354:OXY(4), S412:NVDA(4), S353:OXY(2)  |
+------------------------------------------------------------------------+
|  b296 S353 OXY      limit=0.59                                         |
|  b297 S353 OXY      limit=0.59                                         |
|  b304 S354 OXY      limit=0.59                                         |
|  b305 S354 OXY      limit=0.59                                         |
|  b348 S360 NVDA     limit=0.11                                         |
|  ... 19 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (26)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260803C00315000          17    -78.0%   $   -542.79               |
|  META260803C00600000           2  +1100.0%   $   +322.67               |
|  NVDA260807C00212500           2    +62.5%   $    +90.00               |
|  MSFT260807C00525000           4    -29.3%   $    -78.00               |
|  AMD260803C00492500            4    -33.3%   $    -64.00               |
|  OXY260807C00058000            4    -21.0%   $    -52.00               |
|  NVDA260807C00215000           2    +47.1%   $    +48.00               |
|  T260807C00023000              6    +12.7%   $    +48.00               |
|  ... 18 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-03.log
elapsed=182.1s reconcile=0.48s cancel=0.08s manage=13.46s scan=59.21s entries=106.93s
STATUS: options_morning_bot run complete (PAPER) elapsed=182.1s. run=#5832 https://github.com/28twagg-ops/TradingBot/actions/runs/30820984199
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.csv
Summary: 19 buckets closed trades, $+157.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.4% (22/914)
# Options signal frequency

_Generated 2026-08-03T10:08:52.742615_

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
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    99 | INFO |
| Total closed lots           |   425 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=467.91 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260803T141306Z

- UTC timestamp: `20260803T141306Z`
- GitHub run: [#5833](https://github.com/28twagg-ops/TradingBot/actions/runs/30821395164)
- Run id: `30821395164`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`122s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T10:13:11.347473-04:00","date":"2026-08-03","mode":"entry+manage","header":"entry+manage (4 new)","elapsed_s":113.3,"phases_s":{"reconcile":0.6,"cancel":0.15,"manage":17.2,"scan":58.53,"entries":34.93,"reconcile2":0.89},"signals":264,"placed":4,"equity":131016.11,"open_positions":27,"pending_orders":25,"open_lots":95,"submitted_today":89,"filled_today":64,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:ARM","S165:EOG","S165:OXY","S164:AMD","S164:ARM","S164:EOG","S164:OXY"],"github_run":"5833","github_run_id":"30821395164","status":"ok"}
```

### Live bot full output

```text
14:13:07  INFO      Mode: exits
14:13:08  INFO        Daily log -> logs/daily/2026-08-03.md
14:13:08  INFO        Daily log reconciled -> logs/daily/2026-08-03.md (5 ledger rows)
14:13:08  INFO        place_all_stops: checking 4 positions...
14:13:08  INFO        STOP already live AES @ $14.62
14:13:08  INFO        STOP skipped AVB: fractional (0.5001 shares) — software exit will handle it
14:13:08  INFO        STOP skipped CPT: fractional (0.8366 shares) — software exit will handle it
14:13:08  INFO        STOP skipped ED: fractional (0.6468 shares) — software exit will handle it
14:13:09  INFO        [positions] 4/4 (4 valid)
14:13:09  INFO        Daily log -> logs/daily/2026-08-03.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:13 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $468.63|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CPT  P&L -0.1%  $-0.07                                            HOLD|
|  AES  P&L +0.1%  $+0.12                                            HOLD|
|  AVB  P&L +0.4%  $+0.38                                            HOLD|
|  ED  P&L +0.4%  $+0.29                                             HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           4|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                4|
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
  open_lots=99 paper_keys=yes dry_run=False
  alpaca positions=28
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-03T10:13:11.347473-04:00 ===

[Run context]
Paper auth OK — equity $131016.11, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-03 10:13:14,959 INFO   EXIT [b31|lab0031_s203_w4_1120_1135_r2|S203] stop_loss (-51.2%) SELL 1 SMCI260807P00025000 @<= 0.22
2026-08-03 10:13:16,474 INFO   EXIT [b95|lab0095_s211_w1_0928_1005_r2|S211] stop_loss (-60.9%) SELL 1 MSFT260807C00525000 @<= 0.27
2026-08-03 10:13:19,450 INFO   EXIT [b829|lab0829_s406_w1_0928_1005_r2|S406] take_profit (+62.7%) SELL 1 NVDA260807C00215000 @<= 0.86
2026-08-03 10:13:20,120 INFO   EXIT [b298|lab0298_s353_w2_1005_1045_r1|S353] stop_loss (-75.6%) SELL 1 AAPL260803C00315000 @<= 0.07
2026-08-03 10:13:21,505 INFO   EXIT [b197|lab0197_s218_w3_1045_1120_r2|S218] take_profit (+854.5%) SELL 1 META260803C00600000 @<= 1.32
2026-08-03 10:13:22,307 INFO   EXIT [b235|lab0235_s401_w1_0928_1005_r2|S401] take_profit (+79.2%) SELL 1 NVDA260807C00212500 @<= 1.24
2026-08-03 10:13:28,135 INFO   EXIT [b345|lab0345_s359_w1_0928_1005_r2|S359] take_profit (+235.7%) SELL 1 NVDA260803C00207500 @<= 0.46

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 264 signal(s); top: ['S165:AMD', 'S165:ARM', 'S165:EOG', 'S165:OXY', 'S164:AMD', 'S164:ARM', 'S164:EOG', 'S164:OXY']
Paper lab: $130571 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 181 no tradeable call, 8 already attempted today, 23 pending order
Placed 4 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $131,016.11                             |
|  Signals this run              264                                     |
|  Orders submitted (session)    89                                      |
|  Orders filled today (ledger)  64                                      |
|  Entries placed this run       4                                       |
|  Open virtual lots             95                                      |
|  Broker option positions       27                                      |
|  Pending orders                25                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=387  buckets=137  win=41%                            |
|  Returns   avg=+18.6%  med=-22.2%  p10=-66.2%  p90=+140.9%             |
|  Realized  $+7,657.13                                                  |
|  Raw incl dropped  trades=921  real=$+6,061.58                         |
|  Today     trades=26  avg=+111.2%  med=+23.1%  real=$+319.00           |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b181 lab0181_s217_w2_10  1 100% +1007.1 +1007.1 +1007.1 $   +141      |
|  b180 lab0180_s217_w2_10  1 100% +885.7 +885.7 +885.7 $   +124         |
|  b197 lab0197_s218_w3_10  1 100% +737.5 +737.5 +737.5 $   +118         |
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b311 lab0311_s354_w4_11  1 100% +290.5 +290.5 +290.5 $   +122         |
|  ... 129 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b280 lab0280_s351_w1_09  1   0% -91.7 -91.7 -91.7 $    -44       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (25)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S354:OXY(4), S353:OXY(3), S360:NVDA(2)  |
+------------------------------------------------------------------------+
|  b296 S353 OXY      limit=0.59                                         |
|  b297 S353 OXY      limit=0.59                                         |
|  b304 S354 OXY      limit=0.59                                         |
|  b305 S354 OXY      limit=0.59                                         |
|  b348 S360 NVDA     limit=0.11                                         |
|  ... 20 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (27)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260803C00315000          16    -68.2%   $   -446.86               |
|  META260803C00600000           1   +936.4%   $   +137.33               |
|  MSFT260807C00525000           3    -56.4%   $   -112.50               |
|  AMD260803C00492500            4    -35.4%   $    -68.00               |
|  T260807C00023000              6    +12.7%   $    +48.00               |
|  NVDA260807C00212500           1    +65.3%   $    +47.00               |
|  NVDA260805C00212500           4    +20.8%   $    +40.00               |
|  NVDA260807C00217500           4    +22.5%   $    +36.00               |
|  ... 19 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-03.log
elapsed=113.3s reconcile=0.6s cancel=0.15s manage=17.2s scan=58.53s entries=34.93s
STATUS: options_morning_bot run complete (PAPER) elapsed=113.3s. run=#5833 https://github.com/28twagg-ops/TradingBot/actions/runs/30821395164
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.csv
Summary: 25 buckets closed trades, $+319.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.4% (22/921)
# Options signal frequency

_Generated 2026-08-03T10:15:10.112340_

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
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    95 | INFO |
| Total closed lots           |   432 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=468.57 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260803T141555Z

- UTC timestamp: `20260803T141555Z`
- GitHub run: [#5834](https://github.com/28twagg-ops/TradingBot/actions/runs/30821792062)
- Run id: `30821792062`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`99s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T10:15:59.626248-04:00","date":"2026-08-03","mode":"entry+manage","header":"entry+manage (5 new)","elapsed_s":90.3,"phases_s":{"reconcile":0.59,"cancel":0.04,"manage":20.76,"scan":52.15,"entries":13.01,"reconcile2":3.4},"signals":268,"placed":5,"equity":131048.88,"open_positions":25,"pending_orders":25,"open_lots":95,"submitted_today":90,"filled_today":68,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:ARM","S165:EOG","S165:OXY","S164:AMD","S164:ARM","S164:EOG","S164:OXY"],"github_run":"5834","github_run_id":"30821792062","status":"ok"}
```

### Live bot full output

```text
14:15:56  INFO      Mode: exits
14:15:57  INFO        Daily log -> logs/daily/2026-08-03.md
14:15:57  INFO        Daily log reconciled -> logs/daily/2026-08-03.md (5 ledger rows)
14:15:57  INFO        place_all_stops: checking 4 positions...
14:15:57  INFO        STOP already live AES @ $14.62
14:15:57  INFO        STOP skipped AVB: fractional (0.5001 shares) — software exit will handle it
14:15:57  INFO        STOP skipped CPT: fractional (0.8366 shares) — software exit will handle it
14:15:57  INFO        STOP skipped ED: fractional (0.6468 shares) — software exit will handle it
14:15:57  INFO        [positions] 4/4 (4 valid)
14:15:57  INFO        Daily log -> logs/daily/2026-08-03.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $468.48|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CPT  P&L -0.2%  $-0.17                                            HOLD|
|  AES  P&L +0.1%  $+0.09                                            HOLD|
|  AVB  P&L +0.4%  $+0.36                                            HOLD|
|  ED  P&L +0.5%  $+0.34                                             HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           4|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                4|
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
  open_lots=99 paper_keys=yes dry_run=False
  alpaca positions=30
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-03T10:15:59.626248-04:00 ===

[Run context]
Paper auth OK — equity $131048.88, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-03 10:16:06,909 INFO   EXIT [b344|lab0344_s359_w1_0928_1005_r1|S359] take_profit (+128.6%) SELL 1 NVDA260803C00207500 @<= 0.31
2026-08-03 10:16:09,466 INFO   EXIT [b301|lab0301_s353_w3_1045_1120_r2|S353] stop_loss (-60.9%) SELL 1 AAPL260803C00315000 @<= 0.16
2026-08-03 10:16:14,424 INFO   EXIT [b196|lab0196_s218_w3_1045_1120_r1|S218] take_profit (+861.4%) SELL 1 META260803C00600000 @<= 1.57
2026-08-03 10:16:15,969 INFO   EXIT [b94|lab0094_s211_w1_0928_1005_r1|S211] stop_loss (-51.9%) SELL 1 MSFT260807C00525000 @<= 0.33
2026-08-03 10:16:19,549 INFO   EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+62.5%) SELL 1 NVDA260807C00212500 @<= 1.21

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 268 signal(s); top: ['S165:AMD', 'S165:ARM', 'S165:EOG', 'S165:OXY', 'S164:AMD', 'S164:ARM', 'S164:EOG', 'S164:OXY']
Paper lab: $131453 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 173 no tradeable call, 8 already attempted today, 4 open order exists, 22 pending order
Placed 5 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $131,048.88                             |
|  Signals this run              268                                     |
|  Orders submitted (session)    90                                      |
|  Orders filled today (ledger)  68                                      |
|  Entries placed this run       5                                       |
|  Open virtual lots             95                                      |
|  Broker option positions       25                                      |
|  Pending orders                25                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=391  buckets=140  win=41%                            |
|  Returns   avg=+21.2%  med=-20.0%  p10=-66.2%  p90=+142.9%             |
|  Realized  $+7,839.13                                                  |
|  Raw incl dropped  trades=925  real=$+6,243.58                         |
|  Today     trades=30  avg=+132.1%  med=+38.4%  real=$+501.00           |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b181 lab0181_s217_w2_10  1 100% +1007.1 +1007.1 +1007.1 $   +141      |
|  b196 lab0196_s218_w3_10  1 100% +906.2 +906.2 +906.2 $   +145         |
|  b180 lab0180_s217_w2_10  1 100% +885.7 +885.7 +885.7 $   +124         |
|  b197 lab0197_s218_w3_10  1 100% +737.5 +737.5 +737.5 $   +118         |
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 132 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b280 lab0280_s351_w1_09  1   0% -91.7 -91.7 -91.7 $    -44       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (25)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S354:OXY(4), S353:OXY(3), S360:NVDA(2)  |
+------------------------------------------------------------------------+
|  b296 S353 OXY      limit=0.59                                         |
|  b297 S353 OXY      limit=0.59                                         |
|  b304 S354 OXY      limit=0.59                                         |
|  b305 S354 OXY      limit=0.59                                         |
|  b348 S360 NVDA     limit=0.11                                         |
|  ... 20 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b301 S353 AAPL260803C00315000 x1 stop_loss (-60.9%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (25)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260803C00315000          16    -68.2%   $   -446.86               |
|  NVDA260805C00212500           4    +39.6%   $    +76.00               |
|  MSFT260807C00525000           2    -50.4%   $    -67.00               |
|  NVDA260805C00215000           8    +25.1%   $    +61.00               |
|  NVDA260807C00217500           4    +37.5%   $    +60.00               |
|  AMD260803C00492500            4    -29.2%   $    -56.00               |
|  T260807C00023000              6    +12.7%   $    +48.00               |
|  NVDA260807C00215000           1    +70.6%   $    +36.00               |
|  ... 17 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-03.log
elapsed=90.3s reconcile=0.59s cancel=0.04s manage=20.76s scan=52.15s entries=13.01s
STATUS: options_morning_bot run complete (PAPER) elapsed=90.3s. run=#5834 https://github.com/28twagg-ops/TradingBot/actions/runs/30821792062
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.csv
Summary: 29 buckets closed trades, $+501.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.5% (23/925)
# Options signal frequency

_Generated 2026-08-03T10:17:35.402406_

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    95 | INFO |
| Total closed lots           |   435 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=468.48 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260803T142040Z

- UTC timestamp: `20260803T142040Z`
- GitHub run: [#5835](https://github.com/28twagg-ops/TradingBot/actions/runs/30822186162)
- Run id: `30822186162`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`76s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T10:20:43.761494-04:00","date":"2026-08-03","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":68.7,"phases_s":{"reconcile":0.2,"cancel":0.03,"manage":9.7,"scan":50.39,"entries":7.8,"reconcile2":0.23},"signals":269,"placed":2,"equity":131751.68,"open_positions":24,"pending_orders":25,"open_lots":95,"submitted_today":92,"filled_today":70,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:ARM","S165:EOG","S165:OXY","S164:AMD","S164:ARM","S164:EOG","S164:OXY"],"github_run":"5835","github_run_id":"30822186162","status":"ok"}
```

### Live bot full output

```text
14:20:41  INFO      Mode: exits
14:20:41  INFO        Daily log -> logs/daily/2026-08-03.md
14:20:41  INFO        Daily log reconciled -> logs/daily/2026-08-03.md (5 ledger rows)
14:20:41  INFO        place_all_stops: checking 4 positions...
14:20:41  INFO        STOP already live AES @ $14.62
14:20:41  INFO        STOP skipped AVB: fractional (0.5001 shares) — software exit will handle it
14:20:41  INFO        STOP skipped CPT: fractional (0.8366 shares) — software exit will handle it
14:20:41  INFO        STOP skipped ED: fractional (0.6468 shares) — software exit will handle it
14:20:41  INFO        [positions] 4/4 (4 valid)
14:20:41  INFO        Daily log -> logs/daily/2026-08-03.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $468.50|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CPT  P&L -0.1%  $-0.13                                            HOLD|
|  AES  P&L +0.1%  $+0.12                                            HOLD|
|  ED  P&L +0.4%  $+0.27                                             HOLD|
|  AVB  P&L +0.4%  $+0.38                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           4|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                4|
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
  open_lots=95 paper_keys=yes dry_run=False
  alpaca positions=28
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-03T10:20:43.761494-04:00 ===

[Run context]
Paper auth OK — equity $131751.68, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-03 10:20:45,087 INFO   EXIT [b30|lab0030_s203_w4_1120_1135_r1|S203] stop_loss (-53.5%) SELL 1 SMCI260807P00025000 @<= 0.17
2026-08-03 10:20:52,487 INFO   EXIT [b97|lab0097_s211_w2_1005_1045_r2|S211] stop_loss (-50.4%) SELL 1 MSFT260807C00525000 @<= 0.34
2026-08-03 10:20:53,042 INFO   EXIT [b828|lab0828_s406_w1_0928_1005_r1|S406] take_profit (+70.6%) SELL 1 NVDA260807C00215000 @<= 0.84

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 269 signal(s); top: ['S165:AMD', 'S165:ARM', 'S165:EOG', 'S165:OXY', 'S164:AMD', 'S164:ARM', 'S164:EOG', 'S164:OXY']
Paper lab: $132119 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 150 no tradeable call, 8 already attempted today, 4 open order exists, 38 pending order
Placed 2 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $131,751.68                             |
|  Signals this run              269                                     |
|  Orders submitted (session)    92                                      |
|  Orders filled today (ledger)  70                                      |
|  Entries placed this run       2                                       |
|  Open virtual lots             95                                      |
|  Broker option positions       24                                      |
|  Pending orders                25                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=393  buckets=141  win=41%                            |
|  Returns   avg=+21.1%  med=-20.0%  p10=-66.2%  p90=+142.7%             |
|  Realized  $+7,855.13                                                  |
|  Raw incl dropped  trades=927  real=$+6,259.58                         |
|  Today     trades=32  avg=+124.5%  med=+38.4%  real=$+517.00           |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b181 lab0181_s217_w2_10  1 100% +1007.1 +1007.1 +1007.1 $   +141      |
|  b196 lab0196_s218_w3_10  1 100% +906.2 +906.2 +906.2 $   +145         |
|  b180 lab0180_s217_w2_10  1 100% +885.7 +885.7 +885.7 $   +124         |
|  b197 lab0197_s218_w3_10  1 100% +737.5 +737.5 +737.5 $   +118         |
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 133 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b280 lab0280_s351_w1_09  1   0% -91.7 -91.7 -91.7 $    -44       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (25)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S354:OXY(4), S353:OXY(3), S360:NVDA(2)  |
+------------------------------------------------------------------------+
|  b296 S353 OXY      limit=0.59                                         |
|  b297 S353 OXY      limit=0.59                                         |
|  b304 S354 OXY      limit=0.59                                         |
|  b305 S354 OXY      limit=0.59                                         |
|  b348 S360 NVDA     limit=0.11                                         |
|  ... 20 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b301 S353 AAPL260803C00315000 x1 stop_loss (-60.9%)                   |
|  b97  S211 MSFT260807C00525000 x1 stop_loss (-50.4%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (24)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260803C00315000          16    -80.5%   $   -526.86               |
|  NVDA260805C00212500           4    +54.2%   $   +104.00               |
|  NVDA260805C00215000           8    +38.3%   $    +93.00               |
|  NVDA260807C00217500           4    +50.0%   $    +80.00               |
|  MSFT260807C00525000           2    -50.4%   $    -67.00               |
|  AMD260803C00492500            4    +25.0%   $    +48.00               |
|  T260807C00023000              6    +12.7%   $    +48.00               |
|  NVDA260807C00220000           4    +28.8%   $    +34.00               |
|  ... 16 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-03.log
elapsed=68.7s reconcile=0.2s cancel=0.03s manage=9.7s scan=50.39s entries=7.8s
STATUS: options_morning_bot run complete (PAPER) elapsed=68.7s. run=#5835 https://github.com/28twagg-ops/TradingBot/actions/runs/30822186162
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.csv
Summary: 31 buckets closed trades, $+517.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.5% (23/927)
# Options signal frequency

_Generated 2026-08-03T10:21:57.842029_

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    95 | INFO |
| Total closed lots           |   437 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=468.5 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260803T142543Z

- UTC timestamp: `20260803T142543Z`
- GitHub run: [#5836](https://github.com/28twagg-ops/TradingBot/actions/runs/30822586832)
- Run id: `30822586832`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`115s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T10:25:48.346899-04:00","date":"2026-08-03","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":107.0,"phases_s":{"reconcile":0.59,"cancel":0.16,"manage":15.56,"scan":62.22,"entries":27.21,"reconcile2":0.64},"signals":267,"placed":0,"equity":132024.58,"open_positions":25,"pending_orders":23,"open_lots":94,"submitted_today":92,"filled_today":72,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:ARM","S165:EOG","S165:OXY","S164:AMD","S164:ARM","S164:EOG","S164:OXY"],"github_run":"5836","github_run_id":"30822586832","status":"ok"}
```

### Live bot full output

```text
14:25:44  INFO      Mode: exits
14:25:45  INFO        Daily log -> logs/daily/2026-08-03.md
14:25:45  INFO        Daily log reconciled -> logs/daily/2026-08-03.md (5 ledger rows)
14:25:45  INFO        place_all_stops: checking 4 positions...
14:25:45  INFO        STOP already live AES @ $14.62
14:25:45  INFO        STOP skipped AVB: fractional (0.5001 shares) — software exit will handle it
14:25:45  INFO        STOP skipped CPT: fractional (0.8366 shares) — software exit will handle it
14:25:45  INFO        STOP skipped ED: fractional (0.6468 shares) — software exit will handle it
14:25:45  INFO        [positions] 4/4 (4 valid)
14:25:46  INFO        Daily log -> logs/daily/2026-08-03.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.95|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CPT  P&L -0.3%  $-0.30                                            HOLD|
|  ED  P&L +0.1%  $+0.08                                             HOLD|
|  AES  P&L +0.1%  $+0.12                                            HOLD|
|  AVB  P&L +0.2%  $+0.19                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           4|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                4|
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
  open_lots=95 paper_keys=yes dry_run=False
  alpaca positions=27
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-03T10:25:48.346899-04:00 ===

[Run context]
Paper auth OK — equity $132024.58, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-03 10:25:52,337 INFO   EXIT [b377|lab0377_s362_w1_0928_1005_r2|S362] take_profit (+62.5%) SELL 1 NVDA260805C00212500 @<= 0.78
2026-08-03 10:25:56,215 INFO   EXIT [b279|lab0279_s350_w2_1005_1045_r2|S350] take_profit (+88.2%) SELL 1 AMD260803C00500000 @<= 0.33
2026-08-03 10:25:59,300 INFO   EXIT [b391|lab0391_s363_w1_0928_1005_r2|S363] take_profit (+60.0%) SELL 1 NVDA260807C00217500 @<= 0.59
2026-08-03 10:26:01,693 INFO   EXIT [b843|lab0843_s407_w1_0928_1005_r2|S407] take_profit (+51.4%) SELL 1 NVDA260805C00215000 @<= 0.45

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 267 signal(s); top: ['S165:AMD', 'S165:ARM', 'S165:EOG', 'S165:OXY', 'S164:AMD', 'S164:ARM', 'S164:EOG', 'S164:OXY']
Paper lab: $131879 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 148 no tradeable call, 8 already attempted today, 4 open order exists, 20 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $132,024.58                             |
|  Signals this run              267                                     |
|  Orders submitted (session)    92                                      |
|  Orders filled today (ledger)  72                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             94                                      |
|  Broker option positions       25                                      |
|  Pending orders                23                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=396  buckets=144  win=41%                            |
|  Returns   avg=+21.9%  med=-20.0%  p10=-66.2%  p90=+142.5%             |
|  Realized  $+7,955.13                                                  |
|  Raw incl dropped  trades=930  real=$+6,359.58                         |
|  Today     trades=35  avg=+123.8%  med=+47.1%  real=$+617.00           |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b181 lab0181_s217_w2_10  1 100% +1007.1 +1007.1 +1007.1 $   +141      |
|  b196 lab0196_s218_w3_10  1 100% +906.2 +906.2 +906.2 $   +145         |
|  b180 lab0180_s217_w2_10  1 100% +885.7 +885.7 +885.7 $   +124         |
|  b197 lab0197_s218_w3_10  1 100% +737.5 +737.5 +737.5 $   +118         |
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 136 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b280 lab0280_s351_w1_09  1   0% -91.7 -91.7 -91.7 $    -44       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (23)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S354:OXY(4), S353:OXY(3), S360:NVDA(2)  |
+------------------------------------------------------------------------+
|  b296 S353 OXY      limit=0.59                                         |
|  b297 S353 OXY      limit=0.59                                         |
|  b304 S354 OXY      limit=0.59                                         |
|  b305 S354 OXY      limit=0.59                                         |
|  b348 S360 NVDA     limit=0.11                                         |
|  ... 18 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b301 S353 AAPL260803C00315000 x1 stop_loss (-60.9%)                   |
|  b97  S211 MSFT260807C00525000 x1 stop_loss (-50.4%)                   |
|  b279 S350 AMD260803C00500000 x1 take_profit (+88.2%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (25)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260803C00315000          16    -82.9%   $   -542.86               |
|  MSFT260807C00525000           2    -53.4%   $    -71.00               |
|  NVDA260805C00215000           7    +25.1%   $    +53.37               |
|  NVDA260805C00212500           3    +33.3%   $    +48.00               |
|  NVDA260807C00217500           3    +37.5%   $    +45.00               |
|  OXY260807C00058000            6     -9.4%   $    -36.00               |
|  PATH260807C00013500           4    -28.6%   $    -32.00               |
|  AAPL260814C00330000           6     -8.0%   $    -28.50               |
|  ... 17 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-03.log
elapsed=107.0s reconcile=0.59s cancel=0.16s manage=15.56s scan=62.22s entries=27.21s
STATUS: options_morning_bot run complete (PAPER) elapsed=107.0s. run=#5836 https://github.com/28twagg-ops/TradingBot/actions/runs/30822586832
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.csv
Summary: 34 buckets closed trades, $+617.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.5% (23/930)
# Options signal frequency

_Generated 2026-08-03T10:27:40.901687_

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    94 | INFO |
| Total closed lots           |   440 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=467.95 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260803T143045Z

- UTC timestamp: `20260803T143045Z`
- GitHub run: [#5837](https://github.com/28twagg-ops/TradingBot/actions/runs/30822984656)
- Run id: `30822984656`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`92s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T10:30:49.462106-04:00","date":"2026-08-03","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":83.3,"phases_s":{"reconcile":0.18,"cancel":0.02,"manage":16.56,"scan":57.86,"entries":8.19,"reconcile2":0.15},"signals":264,"placed":1,"equity":131488.47,"open_positions":24,"pending_orders":23,"open_lots":93,"submitted_today":93,"filled_today":73,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:ARM","S165:EOG","S165:OXY","S164:AMD","S164:ARM","S164:EOG","S164:OXY"],"github_run":"5837","github_run_id":"30822984656","status":"ok"}
```

### Live bot full output

```text
14:30:46  INFO      Mode: exits
14:30:47  INFO        Daily log -> logs/daily/2026-08-03.md
14:30:47  INFO        Daily log reconciled -> logs/daily/2026-08-03.md (5 ledger rows)
14:30:47  INFO        place_all_stops: checking 4 positions...
14:30:47  INFO        STOP already live AES @ $14.62
14:30:47  INFO        STOP skipped AVB: fractional (0.5001 shares) — software exit will handle it
14:30:47  INFO        STOP skipped CPT: fractional (0.8366 shares) — software exit will handle it
14:30:47  INFO        STOP skipped ED: fractional (0.6468 shares) — software exit will handle it
14:30:47  INFO        [positions] 4/4 (4 valid)
14:30:47  INFO        Daily log -> logs/daily/2026-08-03.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.75|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ED  P&L -0.3%  $-0.19                                             HOLD|
|  CPT  P&L -0.2%  $-0.19                                            HOLD|
|  AES  P&L +0.1%  $+0.12                                            HOLD|
|  AVB  P&L +0.2%  $+0.15                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           4|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                4|
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
  open_lots=94 paper_keys=yes dry_run=False
  alpaca positions=27
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-03T10:30:49.462106-04:00 ===

[Run context]
Paper auth OK — equity $131488.47, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-03 10:31:05,225 INFO   EXIT [b278|lab0278_s350_w2_1005_1045_r1|S350] take_profit (+52.9%) SELL 1 AMD260803C00500000 @<= 0.23

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 264 signal(s); top: ['S165:AMD', 'S165:ARM', 'S165:EOG', 'S165:OXY', 'S164:AMD', 'S164:ARM', 'S164:EOG', 'S164:OXY']
Paper lab: $131932 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 148 no tradeable call, 8 already attempted today, 4 open order exists, 19 pending order
Placed 1 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $131,488.47                             |
|  Signals this run              264                                     |
|  Orders submitted (session)    93                                      |
|  Orders filled today (ledger)  73                                      |
|  Entries placed this run       1                                       |
|  Open virtual lots             93                                      |
|  Broker option positions       24                                      |
|  Pending orders                23                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=398  buckets=144  win=42%                            |
|  Returns   avg=+22.2%  med=-19.5%  p10=-66.2%  p90=+142.4%             |
|  Realized  $+7,984.13                                                  |
|  Raw incl dropped  trades=932  real=$+6,388.58                         |
|  Today     trades=37  avg=+121.8%  med=+54.0%  real=$+646.00           |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b181 lab0181_s217_w2_10  1 100% +1007.1 +1007.1 +1007.1 $   +141      |
|  b196 lab0196_s218_w3_10  1 100% +906.2 +906.2 +906.2 $   +145         |
|  b180 lab0180_s217_w2_10  1 100% +885.7 +885.7 +885.7 $   +124         |
|  b197 lab0197_s218_w3_10  1 100% +737.5 +737.5 +737.5 $   +118         |
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 136 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b280 lab0280_s351_w1_09  1   0% -91.7 -91.7 -91.7 $    -44       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (23)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S354:OXY(4), S353:OXY(2), S360:NVDA(2)  |
+------------------------------------------------------------------------+
|  b296 S353 OXY      limit=0.59                                         |
|  b297 S353 OXY      limit=0.59                                         |
|  b304 S354 OXY      limit=0.59                                         |
|  b305 S354 OXY      limit=0.59                                         |
|  b348 S360 NVDA     limit=0.11                                         |
|  ... 18 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b301 S353 AAPL260803C00315000 x1 stop_loss (-60.9%)                   |
|  b97  S211 MSFT260807C00525000 x1 stop_loss (-50.4%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (24)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260803C00315000          16    -85.3%   $   -558.86               |
|  AMD260803C00492500            4    +66.7%   $   +128.00               |
|  MSFT260807C00525000           2    -60.9%   $    -81.00               |
|  NVDA260805C00212500           3    +43.8%   $    +63.00               |
|  NVDA260805C00215000           7    +28.4%   $    +60.37               |
|  NVDA260807C00217500           3    +47.5%   $    +57.00               |
|  AAPL260814C00330000           6    -14.6%   $    -52.50               |
|  NVDA260807C00220000           4    +25.4%   $    +30.00               |
|  ... 16 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-03.log
elapsed=83.3s reconcile=0.18s cancel=0.02s manage=16.56s scan=57.86s entries=8.19s
STATUS: options_morning_bot run complete (PAPER) elapsed=83.3s. run=#5837 https://github.com/28twagg-ops/TradingBot/actions/runs/30822984656
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.csv
Summary: 36 buckets closed trades, $+646.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.5% (23/932)
# Options signal frequency

_Generated 2026-08-03T10:32:18.241027_

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    93 | INFO |
| Total closed lots           |   442 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=467.82 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260803T143539Z

- UTC timestamp: `20260803T143539Z`
- GitHub run: [#5838](https://github.com/28twagg-ops/TradingBot/actions/runs/30823391100)
- Run id: `30823391100`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`75s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T10:35:42.584657-04:00","date":"2026-08-03","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":66.1,"phases_s":{"reconcile":0.09,"cancel":0.02,"manage":7.27,"scan":51.72,"entries":6.44,"reconcile2":0.21},"signals":269,"placed":1,"equity":132670.45,"open_positions":24,"pending_orders":24,"open_lots":90,"submitted_today":94,"filled_today":73,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:ARM","S165:EOG","S165:OXY","S164:AMD","S164:ARM","S164:EOG","S164:OXY"],"github_run":"5838","github_run_id":"30823391100","status":"ok"}
```

### Live bot full output

```text
14:35:40  INFO      Mode: exits
14:35:40  INFO        Daily log -> logs/daily/2026-08-03.md
14:35:40  INFO        Daily log reconciled -> logs/daily/2026-08-03.md (5 ledger rows)
14:35:40  INFO        place_all_stops: checking 4 positions...
14:35:40  INFO        STOP already live AES @ $14.62
14:35:40  INFO        STOP skipped AVB: fractional (0.5001 shares) — software exit will handle it
14:35:40  INFO        STOP skipped CPT: fractional (0.8366 shares) — software exit will handle it
14:35:40  INFO        STOP skipped ED: fractional (0.6468 shares) — software exit will handle it
14:35:40  INFO        [positions] 4/4 (4 valid)
14:35:40  INFO        Daily log -> logs/daily/2026-08-03.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.39|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CPT  P&L -0.5%  $-0.43                                            HOLD|
|  AVB  P&L -0.1%  $-0.11                                            HOLD|
|  ED  P&L -0.1%  $-0.05                                             HOLD|
|  AES  P&L +0.1%  $+0.12                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           4|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                4|
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
  open_lots=93 paper_keys=yes dry_run=False
  alpaca positions=26
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-03T10:35:42.584657-04:00 ===

[Run context]
Paper auth OK — equity $132670.45, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-03 10:35:46,397 INFO   EXIT [b376|lab0376_s362_w1_0928_1005_r1|S362] take_profit (+54.2%) SELL 1 NVDA260805C00212500 @<= 0.75
2026-08-03 10:35:47,164 INFO   EXIT [b281|lab0281_s351_w1_0928_1005_r2|S351] take_profit (+191.7%) SELL 1 AMD260803C00492500 @<= 1.42
2026-08-03 10:35:49,305 INFO   EXIT [b390|lab0390_s363_w1_0928_1005_r1|S363] take_profit (+60.0%) SELL 1 NVDA260807C00217500 @<= 0.61

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 269 signal(s); top: ['S165:AMD', 'S165:ARM', 'S165:EOG', 'S165:OXY', 'S164:AMD', 'S164:ARM', 'S164:EOG', 'S164:OXY']
Paper lab: $132538 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 150 no tradeable call, 8 already attempted today, 4 open order exists, 23 pending order
Placed 1 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $132,670.45                             |
|  Signals this run              269                                     |
|  Orders submitted (session)    94                                      |
|  Orders filled today (ledger)  73                                      |
|  Entries placed this run       1                                       |
|  Open virtual lots             90                                      |
|  Broker option positions       24                                      |
|  Pending orders                24                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=401  buckets=146  win=42%                            |
|  Returns   avg=+23.1%  med=-18.9%  p10=-66.2%  p90=+142.9%             |
|  Realized  $+8,152.13                                                  |
|  Raw incl dropped  trades=935  real=$+6,556.58                         |
|  Today     trades=40  avg=+123.1%  med=+67.7%  real=$+814.00           |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b181 lab0181_s217_w2_10  1 100% +1007.1 +1007.1 +1007.1 $   +141      |
|  b196 lab0196_s218_w3_10  1 100% +906.2 +906.2 +906.2 $   +145         |
|  b180 lab0180_s217_w2_10  1 100% +885.7 +885.7 +885.7 $   +124         |
|  b197 lab0197_s218_w3_10  1 100% +737.5 +737.5 +737.5 $   +118         |
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 138 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b280 lab0280_s351_w1_09  1   0% -91.7 -91.7 -91.7 $    -44       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (24)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S354:OXY(4), S353:OXY(2), S360:NVDA(2)  |
+------------------------------------------------------------------------+
|  b296 S353 OXY      limit=0.59                                         |
|  b297 S353 OXY      limit=0.59                                         |
|  b304 S354 OXY      limit=0.59                                         |
|  b305 S354 OXY      limit=0.59                                         |
|  b348 S360 NVDA     limit=0.11                                         |
|  ... 19 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b301 S353 AAPL260803C00315000 x1 stop_loss (-60.9%)                   |
|  b97  S211 MSFT260807C00525000 x1 stop_loss (-50.4%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (24)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260803C00315000          16    -82.9%   $   -542.86               |
|  AMD260803C00492500            3   +172.9%   $   +249.00               |
|  NVDA260805C00215000           7    +41.6%   $    +88.37               |
|  MSFT260807C00525000           2    -62.4%   $    -83.00               |
|  AAPL260814C00330000           6    -16.3%   $    -58.50               |
|  NVDA260805C00212500           2    +58.3%   $    +56.00               |
|  NVDA260807C00217500           2    +60.0%   $    +48.00               |
|  NVDA260807C00220000           4    +39.0%   $    +46.00               |
|  ... 16 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-03.log
elapsed=66.1s reconcile=0.09s cancel=0.02s manage=7.27s scan=51.72s entries=6.44s
STATUS: options_morning_bot run complete (PAPER) elapsed=66.1s. run=#5838 https://github.com/28twagg-ops/TradingBot/actions/runs/30823391100
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.csv
Summary: 39 buckets closed trades, $+814.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.5% (23/935)
# Options signal frequency

_Generated 2026-08-03T10:36:54.065231_

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    90 | INFO |
| Total closed lots           |   445 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=467.39 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260803T143917Z

- UTC timestamp: `20260803T143917Z`
- GitHub run: [#5839](https://github.com/28twagg-ops/TradingBot/actions/runs/30823681296)
- Run id: `30823681296`
- Live bot: exit=`0`, duration=`7s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T10:35:42.584657-04:00","date":"2026-08-03","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":66.1,"phases_s":{"reconcile":0.09,"cancel":0.02,"manage":7.27,"scan":51.72,"entries":6.44,"reconcile2":0.21},"signals":269,"placed":1,"equity":132670.45,"open_positions":24,"pending_orders":24,"open_lots":90,"submitted_today":94,"filled_today":73,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:ARM","S165:EOG","S165:OXY","S164:AMD","S164:ARM","S164:EOG","S164:OXY"],"github_run":"5838","github_run_id":"30823391100","status":"ok"}
```

### Live bot full output

```text
14:39:18  INFO      Mode: exits
14:39:21  INFO        Daily log -> logs/daily/2026-08-03.md
14:39:21  INFO        Daily log reconciled -> logs/daily/2026-08-03.md (5 ledger rows)
14:39:21  INFO        place_all_stops: checking 4 positions...
14:39:21  INFO        STOP already live AES @ $14.62
14:39:21  INFO        STOP skipped AVB: fractional (0.5001 shares) — software exit will handle it
14:39:21  INFO        STOP skipped CPT: fractional (0.8366 shares) — software exit will handle it
14:39:21  INFO        STOP skipped ED: fractional (0.6468 shares) — software exit will handle it
14:39:22  INFO        [positions] 4/4 (4 valid)
14:39:22  INFO        SELL MARKET [urgent] CPT closed
14:39:24  INFO        TX logged: SELL CPT  P&L -0.53%
14:39:24  INFO        Daily log -> logs/daily/2026-08-03.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:39 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.14|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CPT  P&L -0.5%  $-0.50                         EXIT: stop_loss (-0.5%)|
|  ED  P&L -0.3%  $-0.20                                             HOLD|
|  AVB  P&L -0.1%  $-0.14                                            HOLD|
|  AES  P&L +0.1%  $+0.12                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           4|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  1 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
|  Logged exits                                                         1|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  CPT                                         -0.53%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=90 paper_keys=yes dry_run=False
  alpaca positions=27
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-03T10:39:26.409354-04:00 ===

[Run context]
Paper auth OK — equity $132842.36, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-03 10:39:29,426 INFO   EXIT [b351|lab0351_s360_w2_1005_1045_r2|S360] take_profit (+63.6%) SELL 1 NVDA260803C00210000 @<= 0.17
2026-08-03 10:39:32,241 INFO   EXIT [b845|lab0845_s407_w2_1005_1045_r2|S407] take_profit (+77.5%) SELL 1 NVDA260807C00217500 @<= 0.67
2026-08-03 10:39:32,860 INFO   EXIT [b277|lab0277_s350_w1_0928_1005_r2|S350] take_profit (+185.4%) SELL 1 AMD260803C00492500 @<= 1.24
2026-08-03 10:39:33,883 INFO   EXIT [b842|lab0842_s407_w1_0928_1005_r1|S407] take_profit (+61.3%) SELL 1 NVDA260805C00215000 @<= 0.48
2026-08-03 10:39:35,123 INFO   EXIT [b859|lab0859_s408_w2_1005_1045_r2|S408] take_profit (+52.5%) SELL 1 NVDA260807C00220000 @<= 0.45
2026-08-03 10:39:35,610 INFO   EXIT [b901|lab0901_s411_w2_1005_1045_r2|S411] take_profit (+79.2%) SELL 1 NVDA260805C00212500 @<= 0.80

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260803T144109Z

- UTC timestamp: `20260803T144109Z`
- GitHub run: [#5840](https://github.com/28twagg-ops/TradingBot/actions/runs/30823787171)
- Run id: `30823787171`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T10:35:42.584657-04:00","date":"2026-08-03","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":66.1,"phases_s":{"reconcile":0.09,"cancel":0.02,"manage":7.27,"scan":51.72,"entries":6.44,"reconcile2":0.21},"signals":269,"placed":1,"equity":132670.45,"open_positions":24,"pending_orders":24,"open_lots":90,"submitted_today":94,"filled_today":73,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:ARM","S165:EOG","S165:OXY","S164:AMD","S164:ARM","S164:EOG","S164:OXY"],"github_run":"5838","github_run_id":"30823391100","status":"ok"}
```

### Live bot full output

```text
14:41:10  INFO      Mode: exits
14:43:24  WARNING   get_account failed attempt 1/3: HTTPSConnectionPool(host='api.alpaca.markets', port=443): Max retries exceeded with url: /v2/account (Caused by ConnectTimeoutError(<HTTPSConnection(host='api.alpaca.markets', port=443) at 0x7f5b7a4b67d0>, 'Connection to api.alpaca.markets timed out. (connect timeout=None)')) retrying in 10s
```

### Options bot full output

```text

## Run 20260803T144613Z

- UTC timestamp: `20260803T144613Z`
- GitHub run: [#5841](https://github.com/28twagg-ops/TradingBot/actions/runs/30824190387)
- Run id: `30824190387`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`132s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T10:46:18.290661-04:00","date":"2026-08-03","mode":"entry+manage","header":"entry+manage (40 new)","elapsed_s":124.1,"phases_s":{"reconcile":0.7,"cancel":0.12,"manage":18.06,"scan":53.8,"entries":49.05,"reconcile2":1.79},"signals":266,"placed":40,"equity":132913.19,"open_positions":29,"pending_orders":34,"open_lots":109,"submitted_today":134,"filled_today":103,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:ARM","S165:EOG","S165:OXY","S164:AMD","S164:ARM","S164:EOG","S164:OXY"],"github_run":"5841","github_run_id":"30824190387","status":"ok"}
```

### Live bot full output

```text
14:46:14  INFO      Mode: exits
14:46:15  INFO        Daily log -> logs/daily/2026-08-03.md
14:46:15  INFO        Daily log reconciled -> logs/daily/2026-08-03.md (6 ledger rows)
14:46:15  INFO        place_all_stops: checking 3 positions...
14:46:15  INFO        STOP already live AES @ $14.62
14:46:15  INFO        STOP skipped AVB: fractional (0.5001 shares) — software exit will handle it
14:46:15  INFO        STOP skipped ED: fractional (0.6468 shares) — software exit will handle it
14:46:15  INFO        [positions] 3/3 (3 valid)
14:46:16  INFO        Daily log -> logs/daily/2026-08-03.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.54|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ED  P&L -0.1%  $-0.05                                             HOLD|
|  AES  P&L +0.1%  $+0.12                                            HOLD|
|  AVB  P&L +0.2%  $+0.16                                            HOLD|
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
  open_lots=91 paper_keys=yes dry_run=False
  alpaca positions=28
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-03T10:46:18.290661-04:00 ===

[Run context]
Paper auth OK — equity $132913.19, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-03 10:46:20,782 INFO   EXIT [b900|lab0900_s411_w2_1005_1045_r1|S411] take_profit (+77.1%) SELL 1 NVDA260805C00212500 @<= 0.86
2026-08-03 10:46:22,331 INFO   EXIT [b379|lab0379_s362_w2_1005_1045_r2|S362] take_profit (+58.0%) SELL 1 NVDA260805C00215000 @<= 0.44
2026-08-03 10:46:28,675 INFO   EXIT [b276|lab0276_s350_w1_0928_1005_r1|S350] take_profit (+97.9%) SELL 1 AMD260803C00492500 @<= 0.99
2026-08-03 10:46:29,493 INFO   EXIT [b858|lab0858_s408_w2_1005_1045_r1|S408] take_profit (+52.5%) SELL 1 NVDA260807C00220000 @<= 0.41
2026-08-03 10:46:30,298 INFO   EXIT [b844|lab0844_s407_w2_1005_1045_r1|S407] take_profit (+77.5%) SELL 1 NVDA260807C00217500 @<= 0.71
2026-08-03 10:46:32,917 INFO   EXIT [b96|lab0096_s211_w2_1005_1045_r1|S211] stop_loss (-62.4%) SELL 1 MSFT260807C00525000 @<= 0.26
2026-08-03 10:46:33,677 INFO   EXIT [b350|lab0350_s360_w2_1005_1045_r1|S360] take_profit (+54.5%) SELL 1 NVDA260803C00210000 @<= 0.18

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 266 signal(s); top: ['S165:AMD', 'S165:ARM', 'S165:EOG', 'S165:OXY', 'S164:AMD', 'S164:ARM', 'S164:EOG', 'S164:OXY']
Paper lab: $132909 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 206 no tradeable call, 186 pending order
Placed 40 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $132,913.19                             |
|  Signals this run              266                                     |
|  Orders submitted (session)    134                                     |
|  Orders filled today (ledger)  103                                     |
|  Entries placed this run       40                                      |
|  Open virtual lots             109                                     |
|  Broker option positions       29                                      |
|  Pending orders                34                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=413  buckets=156  win=44%                            |
|  Returns   avg=+24.7%  med=-17.6%  p10=-65.4%  p90=+143.1%             |
|  Realized  $+8,462.13                                                  |
|  Raw incl dropped  trades=947  real=$+6,866.58                         |
|  Today     trades=52  avg=+112.8%  med=+54.3%  real=$+1,124.00         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b181 lab0181_s217_w2_10  1 100% +1007.1 +1007.1 +1007.1 $   +141      |
|  b196 lab0196_s218_w3_10  1 100% +906.2 +906.2 +906.2 $   +145         |
|  b180 lab0180_s217_w2_10  1 100% +885.7 +885.7 +885.7 $   +124         |
|  b197 lab0197_s218_w3_10  1 100% +737.5 +737.5 +737.5 $   +118         |
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 148 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b280 lab0280_s351_w1_09  1   0% -91.7 -91.7 -91.7 $    -44       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (34)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S354:OXY(6), S360:NVDA(4), S353:OXY(2)  |
+------------------------------------------------------------------------+
|  b296 S353 OXY      limit=0.59                                         |
|  b297 S353 OXY      limit=0.59                                         |
|  b304 S354 OXY      limit=0.59                                         |
|  b305 S354 OXY      limit=0.59                                         |
|  b348 S360 NVDA     limit=0.11                                         |
|  ... 29 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  PENDING EXITS (4)                                                     |
+------------------------------------------------------------------------+
|  b301 S353 AAPL260803C00315000 x1 stop_loss (-60.9%)                   |
|  b900 S411 NVDA260805C00212500 x1 take_profit (+77.1%)                 |
|  b96  S211 MSFT260807C00525000 x1 stop_loss (-62.4%)                   |
|  b350 S360 NVDA260803C00210000 x1 take_profit (+54.5%)                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (29)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260803C00315000          16    -87.8%   $   -574.86               |
|  AMD260803C00492500            1   +206.2%   $    +99.00               |
|  OXY260807C00058000           13    -10.2%   $    -89.00               |
|  NVDA260805C00215000           7    +31.0%   $    +76.12               |
|  AAPL260814C00330000           6    -16.3%   $    -58.50               |
|  NVDA260810C00220000           4    +26.0%   $    +52.00               |
|  SPY260806C00760000            2    +42.3%   $    +44.00               |
|  MSFT260807C00525000           1    -62.4%   $    -41.50               |
|  ... 21 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-03.log
elapsed=124.1s reconcile=0.7s cancel=0.12s manage=18.06s scan=53.8s entries=49.05s
STATUS: options_morning_bot run complete (PAPER) elapsed=124.1s. run=#5841 https://github.com/28twagg-ops/TradingBot/actions/runs/30824190387
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.csv
Summary: 51 buckets closed trades, $+1,124.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.4% (23/947)
# Options signal frequency

_Generated 2026-08-03T10:48:27.972277_

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
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |   109 | INFO |
| Total closed lots           |   457 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=467.54 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260803T145048Z

- UTC timestamp: `20260803T145048Z`
- GitHub run: [#5842](https://github.com/28twagg-ops/TradingBot/actions/runs/30824585160)
- Run id: `30824585160`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`93s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-03T10:50:51.838262-04:00","date":"2026-08-03","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":83.6,"phases_s":{"reconcile":0.16,"cancel":0.03,"manage":11.5,"scan":61.17,"entries":10.13,"reconcile2":0.29},"signals":262,"placed":0,"equity":133308.23,"open_positions":26,"pending_orders":34,"open_lots":103,"submitted_today":134,"filled_today":103,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:ARM","S165:EOG","S165:OXY","S164:AMD","S164:ARM","S164:EOG","S164:OXY"],"github_run":"5842","github_run_id":"30824585160","status":"ok"}
```

### Live bot full output

```text
14:50:48  INFO      Mode: exits
14:50:49  INFO        Daily log -> logs/daily/2026-08-03.md
14:50:49  INFO        Daily log reconciled -> logs/daily/2026-08-03.md (6 ledger rows)
14:50:49  INFO        place_all_stops: checking 3 positions...
14:50:49  INFO        STOP already live AES @ $14.62
14:50:49  INFO        STOP skipped AVB: fractional (0.5001 shares) — software exit will handle it
14:50:49  INFO        STOP skipped ED: fractional (0.6468 shares) — software exit will handle it
14:50:49  INFO        [positions] 3/3 (3 valid)
14:50:49  INFO        Daily log -> logs/daily/2026-08-03.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.28|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ED  P&L -0.2%  $-0.11                                             HOLD|
|  AVB  P&L -0.0%  $-0.01                                            HOLD|
|  AES  P&L +0.1%  $+0.09                                            HOLD|
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
  open_lots=109 paper_keys=yes dry_run=False
  alpaca positions=30
  FLAG b900|S411|15a84578 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-03T10:50:51.838262-04:00 ===

[Run context]
Paper auth OK — equity $133308.23, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-03 10:50:59,622 INFO   EXIT [b393|lab0393_s363_w2_1005_1045_r2|S363] take_profit (+55.9%) SELL 1 NVDA260807C00220000 @<= 0.45
2026-08-03 10:51:00,835 INFO   EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+260.4%) SELL 1 AMD260803C00492500 @<= 1.85
2026-08-03 10:51:01,881 INFO   EXIT [b279|lab0279_s350_w2_1005_1045_r2|S350] take_profit (+93.5%) SELL 1 AMD260803C00497500 @<= 0.92
2026-08-03 10:51:02,429 INFO   EXIT [b347|lab0347_s359_w2_1005_1045_r2|S359] take_profit (+54.5%) SELL 1 NVDA260803C00210000 @<= 0.13

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 262 signal(s); top: ['S165:AMD', 'S165:ARM', 'S165:EOG', 'S165:OXY', 'S164:AMD', 'S164:ARM', 'S164:EOG', 'S164:OXY']
Paper lab: $133674 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 174 no tradeable call, 13 already attempted today, 68 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $133,308.23                             |
|  Signals this run              262                                     |
|  Orders submitted (session)    134                                     |
|  Orders filled today (ledger)  103                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             103                                     |
|  Broker option positions       26                                      |
|  Pending orders                34                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=418  buckets=159  win=44%                            |
|  Returns   avg=+25.7%  med=-16.8%  p10=-65.1%  p90=+143.8%             |
|  Realized  $+8,680.13                                                  |
|  Raw incl dropped  trades=952  real=$+7,084.58                         |
|  Today     trades=57  avg=+113.0%  med=+60.7%  real=$+1,342.00         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b181 lab0181_s217_w2_10  1 100% +1007.1 +1007.1 +1007.1 $   +141      |
|  b196 lab0196_s218_w3_10  1 100% +906.2 +906.2 +906.2 $   +145         |
|  b180 lab0180_s217_w2_10  1 100% +885.7 +885.7 +885.7 $   +124         |
|  b197 lab0197_s218_w3_10  1 100% +737.5 +737.5 +737.5 $   +118         |
|  b791 lab0791_s398_w4_11  1 100% +338.1 +338.1 +338.1 $   +142         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b790 lab0790_s398_w4_11  1 100% +311.9 +311.9 +311.9 $   +131         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 151 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b280 lab0280_s351_w1_09  1   0% -91.7 -91.7 -91.7 $    -44       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (34)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S354:OXY(6), S360:NVDA(4), S353:OXY(2)  |
+------------------------------------------------------------------------+
|  b296 S353 OXY      limit=0.59                                         |
|  b297 S353 OXY      limit=0.59                                         |
|  b304 S354 OXY      limit=0.59                                         |
|  b305 S354 OXY      limit=0.59                                         |
|  b348 S360 NVDA     limit=0.11                                         |
|  ... 29 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b301 S353 AAPL260803C00315000 x1 stop_loss (-60.9%)                   |
|  b96  S211 MSFT260807C00525000 x1 stop_loss (-62.4%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (26)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260803C00315000          16    -90.2%   $   -590.86               |
|  NVDA260805C00215000           7    +42.3%   $   +104.12               |
|  OXY260807C00058000           13    -10.2%   $    -89.00               |
|  NVDA260810C00220000           4    +34.0%   $    +68.00               |
|  T260807C00023000              6    -15.9%   $    -60.00               |
|  AAPL260814C00330000           6    -16.3%   $    -58.50               |
|  SPY260806C00760000            2    +48.1%   $    +50.00               |
|  MSFT260807C00525000           1    -74.4%   $    -49.50               |
|  ... 18 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-03.log
elapsed=83.6s reconcile=0.16s cancel=0.03s manage=11.5s scan=61.17s entries=10.13s
STATUS: options_morning_bot run complete (PAPER) elapsed=83.6s. run=#5842 https://github.com/28twagg-ops/TradingBot/actions/runs/30824585160
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_buckets.csv
Summary: 54 buckets closed trades, $+1,342.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-03_strategy_selection.csv
Summary: keep=0 watch=102 drop=3
Orphan rate: 2.5% (24/952)
# Options signal frequency

_Generated 2026-08-03T10:52:21.054747_

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   103 | INFO |
| Total closed lots           |   461 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=467.28 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
