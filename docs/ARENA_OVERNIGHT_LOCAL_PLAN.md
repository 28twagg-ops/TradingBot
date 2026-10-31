# Trading Arena — overnight local Llama deployment plan (draft)

Updated: 2026-10-31. **Plan only: no desktop runner installed or scheduled in this PR.**

## Goal: minimum user setup
One assisted setup on the owner's laptop, then automatically run independent S01–S10 research **00:00–07:00 America/Chicago local time** whenever powered, awake and connected. No hosted inference billing; electricity and hardware resources still cost money. Paper-only research; NEVER call existing brokerage trading code or production credentials.

1. Installer detects Windows/macOS, RAM/CPU/GPU, available disk, Python and Ollama; checks the right localhost endpoint (`http://127.0.0.1:11434`). Present one suggested lightweight model appropriate to hardware, confirm license/storage, install it once.
2. Interactive initial GitHub authorization using the OS credential manager or GitHub CLI; narrowly scoped to the Arena repository's **arena-ledger** branch for records and the read-only source branch. Never ask for or write a credential into a repository file, model prompt, or log. **Do not** register a public GitHub self-hosted runner.
3. Installer sets an OS-native daily task (Windows Task Scheduler / macOS launchd), runs a five-minute paper-only smoke test, then displays one screen: enabled, local model, next run, last successful sync. User should not need to edit YAML or hand-create multiple secrets.
4. A single local supervisor invokes ten **serial** worker turns (not ten simultaneous models), reusing `personas.py` and each worker's own existing experiment history, bounded by model context and configurable safe resource caps. Each bot is free to follow original ideas, public research, or any asset; personalities are brainstorming aids, not mandates.
5. Use the existing deterministic backtest and safety validators rather than executing model-generated code. Data-dependent hypotheses are saved as research-only until real, correctly timestamped data can test them. Never promote to real orders.
6. Write each turn to a durable local queue with a unique run/worker ID, atomically fsync on completion, then sync to GitHub. Sync uses fetch/rebase/replay or a conflict-aware merge of **unique events**, never a force push. Verify remote record IDs and hash-linked ledgers after upload. GitHub Action writers are concurrent with laptop sync, so the current workflow-only `concurrency` lock is insufficient.
7. Stop launching new calls at 07:00 local time, finish or abort safely at a bounded timeout, save a short morning report and the queue. Shutdown and resume must not duplicate entries. Respect daylight saving time and clock changes.

## Likely failure modes and automatic handling

| Failure | Handling |
| --- | --- |
| Lid closed, OS sleep, power loss, hot CPU/GPU, insufficient RAM, disk full | Preflight; do not start if below minimum; partial results stay in durable queue; health/failure summary next time; advise power/awake settings without silently changing unrelated settings |
| Wi-Fi drops, GitHub unavailable, Yahoo data stale | Continue **offline research only** if possible, do not pretend historical data is fresh; queue changes locally, reconcile before subsequent upload; no stale quote-based buys |
| Ollama not started, missing model, localhost port conflict, model crash, context overflow, slow responses | Probe API/model; timeouts, bounded retries and small local-model fallback only if approved; checkpoint after each turn; never spin forever |
| Invalid JSON, reasoning bleed, hallucinated code/citations, repeated S07-style invalid specs | Local schema and numeric validation; preserve research-only ideas with safe issue code, no trade; consecutive-failure backoff; no raw model-generated code executed |
| Rate limits on research/search providers or surprise paid-cloud use | Prefer local LLM; no paid fallback, never use Groq key from desktop unless explicitly configured; obey source API quotas |
| Two computers/jobs writing same branch, duplicate idea/trade, corrupt partial JSON | Unique worker-event IDs, hashes, atomic files, merge with remote verification; quarantine irreconcilable conflicts; never force push |
| Untrusted websites inject instructions, malicious GitHub code, prompt leakage | Treat third-party text as quoted data; URL/network allowlist, no running downloaded scripts, no giving LLM credentials, no local API exposure beyond loopback |
| 10 personas collapse into similar BTC ideas, one monopolizes model | Independent per-worker memory, nonbinding brainstorm prompts, fairness scheduling, track topic diversity and meaningful *tested* progress—not manufactured novelty |
| No actual trading edge, lookahead, proxy quote mistaken for fill | Distinct research/validated backtest/virtual trading fields and judges; no unsupported profit claims; production trading remains disconnected |
| Laptop available outside 00:00–07:00 or daylight-saving boundary | Use `America/Chicago` scheduler window, clock-aware checks for every turn, and strict stop boundary |

## Release gates
- API-free unit tests pass; synthetic Ollama JSON and failure-path tests pass.
- Test with Ollama stopped, disconnected Wi-Fi, unexpected sleep, invalid model JSON, concurrent GitHub writes and duplicate job restarts.
- Simulated overnight dry run under realistic laptop RAM/CPU limits without real trades or GitHub token exposure.
- Review morning report: number of valid ideas, rejected invalids, model failures, data coverage, valid historical tests, virtual positions and source evidence.
- Enable the overnight task **only after** a hardware check and an owner-approved local install.

## Suggested staged implementation
**Now:** repair Groq/S07 in a PR and add 10 distinct research personalities. **Next:** design a small provider adapter (Groq/Ollama) with the same safe structured-output validator, then a local supervisor and installer. **Finally:** test the 7-hour schedule and GitHub reconciliation before turning on unattended overnight operation.

The existing cloud Groq/Gemini workflows are separate. This plan neither installs software on the owner's laptop nor changes the live stock/options trading workflows.
