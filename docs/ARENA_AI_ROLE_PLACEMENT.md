# Trading Arena — Three-Provider AI Task Placement

**Architecture:** one shared research pipeline, three very different assignments.
These AI services are *not* three mutually independent sources of empirical truth.
None can authorize live trading, bypass deterministic account validation or
turn a historical close-price proxy into verified executable results.

| Priority | Provider / model | Primary job | Schedule & constraint | Authority |
|---|---|---|---|---|
| 1 (bulk discovery) | **Local Ollama / `llama3.2:3b`** | Ten distinct personas find falsifiable hypotheses, identify data requirements and propose next research searches | Sequential; midnight–7 AM Mon–Fri, midnight–10 AM weekends, Central; laptop must stay awake | Research only; HOLD; no orders |
| 2 (technical testing) | **Groq / `openai/gpt-oss-20b`** | Explore independently, challenge Llama leads, try bounded hourly-close test specifications, and document failures/limitations | Existing time-paced cloud quota, max 5 per job; no retry or paid fallback | Only existing paper simulator after deterministic checks; no live orders |
| 3 (independent review) | **Gemini / `gemini-3.8-flash`** | Weekly independent review: financial reconciliation, lookahead/survivorship methodology, liquidity/risk/overfitting, including disagreements between Llama and Groq | Max 3 existing Sunday specialist calls; requires GitHub Gemini secret and model access | Advice only; no strategy promotion or live orders |

**Other Gemini use:** `gemini-3.5-flash-lite` remains the lighter default
for optional high-volume structured Gemini research. It is not chosen for the
weekly critical risk review, which benefits from the stronger Flash model.

## Handoff and source quality

1. Laptop saves each Llama result as an immutable *local_research_only* JSON
   record on the separate `arena-local-research` branch.
2. GitHub importer validates safe HOLD actions and copies research-only evidence
   to `arena-ledger/records/arena/local_research/`. It never changes accounts.
3. Groq reads only bounded, whitelisted, **untrusted** hypotheses **for the
   same worker** after import, and can challenge them or pursue other leads.
   It does not trust Llama's recommendations as market evidence.
4. Weekly Gemini uses up to 12 recent Groq summaries and 10 imported local
   hypotheses. Its three independent reviewers can request further evidence;
   majority agreement is not verification.
5. Historical close-only backtests remain *proxy tests*, and paper P&L is not
   a broker-verified return. No automatic model promotion or live entries.

## Quality first; avoid false confidence

- Small local models excel at cheap, varied brainstorming, but often omit
  research JSON fields. The local Ollama API now uses a compact JSON schema.
- The installer smoke test proves Ollama works and returns safe JSON; it is
  **not** a guarantee that every hypothesis is good or fully validated.
- Data requirements beyond hourly closes (e.g., 5-minute order flow, options
  chains, spreads or fundamentals) must remain untested until proper data exists.
- Review rate of supported hypotheses, *out-of-sample* validation, duplicate
  topics, useful data requirements, model failures, and new independent evidence.
  Raw idea counts are not a profitability metric.
- If Gemini 3.8 Flash is unavailable or rate-limited, record an incomplete
  review; do not silently downgrade models or exceed the existing 3-call budget.
- The API pricing tables list free tiers but keys linked to paid projects may
  incur charges; actual billing eligibility cannot be inferred from repository
  configuration. No additional APIs, accounts or keys are needed for laptop Llama.

## Laptop refresh

If the installer previously stopped at `OLLAMA_SMOKE_JSON_FIELDS_MISSING`,
rerun the original Windows setup. The bootstrap fast-forwards its sparse local
checkout, retries a safer Ollama connectivity check and re-registers the
midnight scheduled task. The downloaded model is reused.

This release requires a local manual smoke + first full overnight pass and
successful cloud import before declaring three-provider collaboration operational.
