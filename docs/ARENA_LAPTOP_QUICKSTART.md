# Trading Arena — Laptop Llama Quick Start

**Prepared October 31, 2026.** The code is ready to install and test; it has **not** been installed on your computer. Runs local Ollama/Llama models, **not** a cloud Llama API. Each Llama model's license and any electricity/storage costs still apply.

## Your tasks tonight (Windows or Mac)

### Windows 10/11 — preferred one-command route

1. Open **PowerShell** (normal user account). Review the [source of the setup script](../scripts/overnight/Start-Windows.ps1) if desired.
2. Paste this single command, then approve installation of missing applications:

   ```powershell
   irm https://raw.githubusercontent.com/28twagg-ops/TradingBot/main/scripts/overnight/Start-Windows.ps1 | iex
   ```

3. Follow the GitHub browser sign-in when prompted. Leave the computer **plugged in, awake and connected to Wi-Fi** with Ollama open. If Windows says a program was just installed but cannot be found, close PowerShell, reopen and run the *same* command once more.

The script installs any missing **Git, Python 3.11, GitHub CLI and Ollama** through Windows Package Manager, clones only the relevant Arena source folders, downloads a local Llama model and sets up a daily **midnight** Windows task. An 8+ GB machine normally gets `llama3.2:3b` (~2 GB download); lower-RAM systems use `llama3.2:1b` (~1.3 GB download). Actual performance depends on laptop hardware. Under ~5.5 GB RAM, setup stops safely.

### macOS — alternative

Requires [Homebrew](https://brew.sh) (install first if missing). Open **Terminal**, review the [Mac script](../scripts/overnight/Start-Mac.sh), then run:

```bash
curl -fsSL https://raw.githubusercontent.com/28twagg-ops/TradingBot/main/scripts/overnight/Start-Mac.sh | bash
```

The script uses Homebrew to install missing dependencies, opens Ollama, signs in to GitHub via browser and configures a user `launchd` midnight task.

## What the laptop will do

- **Midnight–7:00 AM America/Chicago:** cycle sequentially through researchers **S01–S10**, roughly one pass every 40 minutes while the machine stays running.
- Every bot retains an independent history, with its previously configured [personality](../research/trading-arena/personas.py). Personality inspires brainstorming, but is never a fixed market or strategy assignment.
- Each bot can research any idea it wants using public search metadata and available historical prices, propose falsification tests, and save **research-only** output. Model-generated code is never executed.
- Uses the existing bounded deterministic backtest for supported hourly single-asset ideas. Unsupported or untestable ideas remain research-only.
- Saves all outcomes immediately to `~/.trading-arena/pending/`. Wi-Fi outages do **not** erase pending work.
- Syncs completed immutable JSON experiments to `arena-ledger/records/arena/local_research/YYYY-MM-DD/`, without changing the cloud-managed `ai_state.json`, `state.json`, or Groq's research log. Remote push conflicts are retried safely; records are verified before being considered sent.
- **No real-money orders, no new virtual buys/sells, and no paid API fallback.** Independent reviewers still need credible evidence before any later change to execution.

## How to check the first morning

- Status and each bot's work: `~/.trading-arena/MORNING_REPORT.md` (on Windows, open `%USERPROFILE%\.trading-arena\MORNING_REPORT.md`).
- Detailed local log: `~/.trading-arena/overnight.log`.
- Completed individual work: `~/.trading-arena/sent/`; unsynced evidence: `~/.trading-arena/pending/`.
- Uploaded work: [Arena local research folder](https://github.com/28twagg-ops/TradingBot/tree/arena-ledger/records/arena/local_research) (appears after the first successful upload).

Optional manual test **after setup**, using your installed local Python environment:

**Windows PowerShell:**
```powershell
& "$HOME\.trading-arena\venv\Scripts\python.exe" "$HOME\TradingArenaLocal\research\trading-arena\overnight_local.py" --smoke
```

**macOS Terminal:**
```bash
"$HOME/.trading-arena/venv/bin/python" "$HOME/TradingArenaLocal/research/trading-arena/overnight_local.py" --smoke
```

`--smoke` sends **one** local test prompt, but does not change accounts or push anything. `--once` performs one full **ten-bot research pass** immediately, even outside midnight–7 AM.

## Important operating conditions

- **Wake/sleep:** macOS launchd or Windows Task Scheduler can run at midnight only when the user session and hardware permit it. Keep the laptop open/awake or use an approved awake/power setting, plugged in and on Wi-Fi. Closing the lid commonly sleeps the laptop; this installer does **not** silently change power settings.
- **Login:** The first GitHub CLI browser login is required to upload research. GitHub CLI's authorization may have broader repository permissions than the one Arena branch; the model never sees that token. Do not copy passwords or tokens into a file or chat.
- **Cloud services:** Ollama's local models require no inference API key. This installer refuses model names containing `:cloud`, remote URLs and nonlocal endpoints. Do not select a cloud model.
- **Quota/duplicates:** Ten researchers share one Ollama instance sequentially to limit memory load. Unique research IDs and Git verification prevent duplicate uploads; an app-only lock blocks parallel laptop runs.
- **Missed schedule:** Windows task runs at midnight if possible and checks its Central-time execution window. If the laptop wakes later, only remaining hours are available. If it wakes after 7 AM, it exits without generating new overnight work.
- **Slow laptop:** Local Llama can take substantial time without a GPU; some bots may complete fewer ideas than others. Low disk, missing prices, API errors, and incompatible history fail safely.
- **No guarantee of profitability:** Research records and proxy backtests are not real fills, statistically proven edge or investment recommendations.

## If setup fails

| Symptom | Action |
|---|---|
| `winget` not found | Update Windows App Installer or install [winget](https://learn.microsoft.com/windows/package-manager/winget/) first |
| Program missing right after install | Open a new terminal and rerun bootstrap |
| `OLLAMA_MODEL_NOT_INSTALLED_OR_SERVICE_OFFLINE` | Open the Ollama desktop app; run `ollama pull llama3.2:3b` (or `llama3.2:1b`) and retry |
| `OLLAMA_INVALID_JSON` or slow generation | Try smaller `llama3.2:1b`; no positions are changed |
| GitHub sign-in fails | In terminal run `gh auth login --web`, then rerun setup |
| GitHub uploads fail | Leave pending local JSON files untouched. Rerun overnight or `--once`; the next successful sync resumes |
| `ANOTHER_RUN_ALREADY_ACTIVE` | Do not start a second run. Wait for the first to finish |
| `ANOTHER_RUN_OR_STALE_LOCK` | Confirm no process is running; then remove `~/.trading-arena/overnight.lock` |
| No output next morning | Check `overnight.log`; verify task exists, Ollama is running, laptop was awake and session logged in |

**Manual pause:** Disable the `TradingArenaOvernightOllama` task in Windows Task Scheduler or disable `com.tradingarena.overnight` in macOS launchd; no GitHub or local trade history needs deletion.

## Implementation and safety notes

Files: `local_ollama.py` (local inference adapter), `overnight_local.py` (scheduler / checkpoints / Git sync), `setup_local.py` (installer and OS task), `scripts/overnight/Start-*.ps1/.sh` (bootstraps). GitHub-hosted cloud workflows continue independently.

**Acceptance criteria before relying on nightly results:** CI tests pass, real local smoke test succeeds, model fits RAM, GitHub authentication works, a single research pass produces immutable remote events, and restart/disconnect tests preserve pending work.

Source references: [Ollama official download](https://ollama.com/download), [Llama 3.2 models](https://ollama.com/library/llama3.2), [GitHub CLI sign-in](https://cli.github.com/manual/gh_auth_login).
