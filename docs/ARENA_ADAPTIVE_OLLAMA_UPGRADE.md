# Trading Arena — adaptive local research and mentor-led process

**Status:** zero-cost, paper-only system. No real broker order, account permission, margin or options capability is changed here. The local computer is not remotely managed; a one-time desktop update is required.

## Why use two local models?

The current local engine is **Ollama**, and the installed model `qwen3:4b-instruct` is Qwen, not Meta Llama. The 4B model is a lower-resource structured research assistant. The optional `qwen3:8b` checkpoint (approximately 5.2 GB download, plus runtime memory overhead) is the more demanding candidate; *parameter count does not prove better research output or profits*. The hosted Groq and weekly Gemini reviewers provide independent challenges, but their model responses are never proof of trading returns.

The router only uses locally installed models. It never downloads weights, invokes an API key, falls back to a paid cloud model, or enables trading at night.

### Automatic selection and fallback

- Observe actual local inference fields: prompt tokens, generated tokens, token/s, loading seconds, latency, bounded JSON retries, and research-validator status. Ollama reports durations in nanoseconds.
- The first four baseline calls collect stability evidence. If at least 70% of recent baseline replies are acceptable research output, try **one optional 8B canary in each group of four worker calls**.
- 8B requires **at least 8 GB *available* RAM at selection time**, and measured sampled CPU below 88% if CPU telemetry is available. Unknown free memory means *do not risk* the larger model.
- Automatically revert to the compact baseline if two recent 8B outputs show less than 60% valid research or median generation throughput below 4 tokens/s or median latency above 180 seconds. Recheck in later model sessions; no hard-coded overnight 'best model' promise.
- `psutil` is installed into the isolated Python virtual environment for an indicative CPU sample and available RAM. This is not a full CPU usage time series and cannot reconstruct an earlier overnight run.
- Only **one inference lane** in adaptive mode to avoid simultaneous 4B/8B memory loading. Research rounds remain rate-limited as before. Large models are attempted as bounded canaries, never all ten workers immediately.
- A model result counts as *format-valid research* if it passes existing validators and reports a supported research status. **It is NOT a profitable trading win or statistically validated alpha.**

### Research roles

1. **Smaller local Qwen:** one constrained scientific task at a time—hypothesis, data audit, negative test, replication plan. The deterministic mentor reads only bounded recent Groq experiments and untrusted Gemini council suggestions. The local reply remains strictly forced to HOLD.
2. **Groq:** tests or rejects the proposed idea against the actual available data, checks citations and tests where possible. Unsupported volume, order-book and options research stays untested.
3. **Three-role council plus optional Gemini specialist:** weekly ledger, evidence and risk review; every retired paper generation remains archived `S07a` → `S07b`, with its separate $100 trial and past losses.

Every night `~/.trading-arena/MORNING_REPORT.md` includes counts and a **per-model table** of success percentage, median completion speed and median latency, plus the last hardware sample. Detailed numerical chronological results are saved in `~/.trading-arena/model_runtime.json`. Numeric per-request telemetry is also attached to immutable research records pushed to the isolated `arena-local-research` branch. A night with no network or no completed research is reported honestly, never fabricated.

### Council approval-readiness

Automated weekly council reviews create `records/arena/approval_readiness.json` and `APPROVAL_READINESS.md`. For every generation they explain blockers including:
- minimum 60 genuinely forward paper marks over at least 30 days;
- at least 20 completed paper exits and positive cumulative indicated balance after recorded fees;
- audit/replay integrity;
- **independent executable bid/ask quote observations and realistic slippage and transaction costs**;
- untouched out-of-sample validation and correction for repeatedly trying many strategies (selection bias / probability of backtest overfitting).

Crucially, the currently available Yahoo hourly close observations **cannot clear the executable-quote and independent out-of-sample gates**. The council is therefore **not authorized to mark a strategy live-ready or request money**. This cannot be solved by a bigger LLM. A future independently verified quote/forward-trade evidence integration will be needed before an approval candidate can be considered. Even then, explicit human approval, separate brokerage connection and live risk limits are required; **no strategy is guaranteed 100% profitable**. There is no auto-live promotion.

Research background: D. Bailey & M. López de Prado, *The Deflated Sharpe Ratio* (Journal of Portfolio Management, 2014); D. Bailey et al., *The Probability of Backtest Overfitting* (Journal of Computational Finance, 2017). The 28-day rotation and measured model-selection thresholds are experimental operating choices **not statistically established optimums**.

## One-time update on Windows (Command Prompt, before the next overnight run)

Close any existing Arena overnight Python task if it is running; do not kill a model mid-write. Run this exact command in regular Command Prompt:

```bat
git -C "%USERPROFILE%\TradingArenaLocal" switch main && git -C "%USERPROFILE%\TradingArenaLocal" pull --ff-only origin main && "%USERPROFILE%\.trading-arena\venv\Scripts\python.exe" "%USERPROFILE%\TradingArenaLocal\research\trading-arena\setup_local.py" --model auto --parallel 1
```

The command fails safely if local source changes block switching branches or a fast-forward pull. It keeps old research records and separate GitHub ledger history, installs the extra telemetry dependency and potentially the optional larger model if hardware and free disk qualify, checks Ollama and GitHub access, then updates the existing Windows Task Scheduler job. No extra GitHub repository or separate deployment is needed. It will not install software without your running it.

Verify the setup prints **SETUP COMPLETE** and Windows Task Scheduler action contains `--model auto --parallel 1 --scheduled --log`. Keep the laptop powered, awake, signed in, with Ollama running during overnight windows. The task runs under the interactive user account, not a power-on cloud service.

The existing `qwen3:4b-instruct` model and tonight's cloud Groq research remain unaffected until you run this command locally.

## Inspect the next morning

- `%USERPROFILE%\.trading-arena\MORNING_REPORT.md`
- `%USERPROFILE%\.trading-arena\model_runtime.json`
- `%USERPROFILE%\.trading-arena\overnight.log`
- `arena-local-research` on GitHub for immutable numeric model telemetry and experiment outputs.

Do not interpret a good JSON response rate or benchmark throughput as successful trading performance.
