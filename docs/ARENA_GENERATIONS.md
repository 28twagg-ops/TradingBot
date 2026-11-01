# Trading Arena — versioned strategy generations

## Concept

Keep the internal ledger and safety identity `S01`–`S10` stable while
showing separate **paper-trial generations**, such as `S07a`, `S07b`,
`S07c` ... `S07z`, `S07aa` and later. Never reuse a retired name.

Each successor begins a **fresh simulated $100 account**, a different
predefined bounded rule variant, and a separate AI research history. Every
predecessor remains archived, including **negative P&L**, all events,
open virtual positions, test results, fee information, prior model research,
original account state, replay-vetted deterministic council findings,
and the optional Gemini specialist advisory. The original account is *not*
represented as closed using an invented price. No successor inherits prior
returns as profitable performance.

Archive path: `records/arena/generations/S07a.json` (similarly other
generations). Each archive has a SHA-256 content fingerprint to help detect
accidental changes. This is not a cryptographic third-party signature.
The immutable local Ollama event evidence stays in the independent
`arena-local-research` branch; local record generational identity is
included for future events and remains separate from prior generations.

## Cadence (paper only)

- **Every two hours:** record a new indicative hourly paper mark, if the
  scheduled data feed and rule worker run successfully.
- **Weekly (Sunday):** deterministic 3-role council audits every rule-based
  and AI paper book, asks whether each active version should continue, and
  generates a ranked historical dashboard. The existing free Gemini specialist
  may advise, but an AI vote does not constitute evidence of profitability or
  authorize trading.
- **Routine retirement eligibility no sooner than 28 days:** require at
  least 60 valid, timestamped marks spanning at least 14 distinct UTC dates.
  Automatically replace a version with an indicated loss exceeding 1% only
  if it has at least 6 recorded sales, or it remains negative after 56 days.
  A completely inactive version may be replaced after 56 days with adequate
  observations. **These are operating thresholds chosen conservatively for
  this trial, not a statistical proof that 28 days or six sales suffice to
  estimate an edge.** Twenty-plus complete round trips or much longer forward
  histories would give stronger evidence.
- **One-time exception:** the five previously selected loss leaders
  S09/S02/S07/S10/S06 receive the Nov 1 final chance. The schedule at
  2026-11-02 05:41 UTC (Nov 1 at 11:41 PM Central) checks them after the
  cutoff. If their initial generation has not earned sufficient evidence,
  and ledger/mark checks pass, archive version a and begin version b.
  A missing/stale quote or ledger mismatch blocks automatic resets and
  triggers review instead. Date-gated code prevents this special case
  repeating in 2027.

## Generation evidence requirements

The following are *not* proven profit: a Yahoo completed-hour close,
a virtual entry priced at the same delayed close, an LLM-authored claim,
an in-sample or reused retrospective backtest, or a small number of trades.
The ranking is descriptive only and is not comparable across market regimes.
A marked negative paper return can be used to stop wasting trial resources;
a positive return is not sufficient to enable live trading.

No live broker code is executed, altered or enabled by generation rotation.
All account state changes occur on the isolated `arena-ledger` branch with
the existing `paper-arena-ledger-writes` GitHub Actions concurrency lock.
The old ledger remains preserved in the historical generation archives.

## Files

- `generation_registry.json`: active index and complete archived lineage.
- `generation_observations.json`: dated equity observations by generation.
- `generation_review.json`: per-worker council rotation verdict.
- `generation_rankings.json` / `GENERATIONS.md`: best-to-worst indicative
  performance and current/archived status.
- `generations/S07a.json`: full immutable predecessor snapshot, including
  rule-based and AI paper accounts.

## Laptop / Llama

GitHub-hosted Groq and paper rotations operate without the laptop. Local
Ollama only becomes generation-aware when the user updates their desktop
repository. It cannot be remotely installed or updated while the laptop
is unavailable. The desktop still produces research-only, forced-HOLD
ideas: it does not execute trades or select new live strategies.
