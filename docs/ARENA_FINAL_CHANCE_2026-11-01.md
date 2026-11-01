# Trading Arena final-chance evaluation — November 1, 2026

**Decision deadline:** November 1, 2026, end of day, America/Chicago.
**Research priority window (UTC):** 2026-11-01 18:00 to 2026-11-02 05:30
(12:00 PM to 11:30 PM Central Standard Time on November 1).
**Environment:** GitHub-hosted Groq AI and existing isolated paper ledger only.
The local Ollama laptop is not available and must not be assumed to run.

## Fixed challenged cohort (do not reselect to flatter results)

| Worker | Baseline paper equity | Return from original $100 |
|---|---:|---:|
| S09 | $97.3889 | -2.6111% |
| S02 | $97.7742 | -2.2258% |
| S07 | $98.2183 | -1.7817% |
| S10 | $98.3184 | -1.6816% |
| S06 | $98.5356 | -1.4644% |

All five may receive priority in the *existing* free quota scheduler; minimum
request spacing, rate-limit cooldown, maximum batch size, and daily request
ceiling still apply. There is no extra paid quota, no live order, and no
automatic promotion to live trading. Existing rules for independent backtests
and virtual orders remain unchanged. After 05:30 UTC November 2, all ten bots
resume ordinary request priority without intervention.

## Evidence-based pass/fail review

A **KEEP (provisional paper-only)** requires all:
1. Positive cumulative paper equity above $100 net of all recorded fees at the
   cutoff, with independently replayable ledger events and no missing quotes
   masquerading as executable fills.
2. Credible positive *independent forward / genuinely out-of-sample* results
   after costs for a clearly specified strategy. Retrospective_validation of a
   reused research sample is not an untouched forward holdout. A model's
   assertion, a hypothetical experiment, a single lucky trade, or a profitable
   one-day price move alone cannot prove a reliable edge.
3. No hard veto, orphan/inconsistent ledger events, fabricated source
   verification, or unsupported options/volume/order-book inputs.

**TRIM RECOMMENDED:** cumulative loss persists or credible profit evidence is
missing. **INSUFFICIENT EVIDENCE:** the data quality or sample cannot support
a confident verdict; do not mislabel it as profitable. Under the challenge
terms, insufficient evidence is not a pass.

Trimming means disabling *new active paper-strategy participation only* after
review; preserve full trade records, research hypotheses, and audit trail.
Never delete histories or change the existing main brokerage bot or its
live-order permissions. One day cannot statistically prove a robust trading
edge; even a provisional KEEP is not a live-trading promotion.

## Review source

At cutoff, read `records/arena/last_run.json`,
`records/arena/ai_state.json`, `records/arena/groq_research.json`,
`records/arena/GROQ_RESEARCH.md` on the **arena-ledger** branch, and record
the before/after equity for all five. Distinguish cumulative P&L from
November 1 only. Report distinct trades, actual forward evidence, validation
warnings, and recommended KEEP/TRIM decisions. Do not claim a GitHub Actions
success means a model strategy succeeded.
