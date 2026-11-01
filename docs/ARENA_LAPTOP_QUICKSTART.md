# Trading Arena — Laptop Llama Quick Start

**Updated November 1, 2026.** After observing the real Intel i7-1365U / Iris Xe trial, the Windows 24+ GB default is **Qwen3 4B Instruct with one lane**, not Qwen3 8B with two lanes. The smaller model is a safer CPU inference choice; the larger model remains available by explicit request. Existing research stays intact. Runs local Ollama/Llama models, **not** a cloud Llama API. Each Llama model's license and any electricity/storage costs still apply.

## Your tasks tonight (Windows or Mac)

### Windows 10/11 — preferred one-command route

1. Open **PowerShell** (normal user account). Review the [source of the setup script](../scripts/overnight/Start-Windows.ps1) if desired.
2. Paste this single command, then approve installation of missing applications:

   ```powershell
   irm https://raw.githubusercontent.com/28twagg-ops/TradingBot/main/scripts/overnight/Start-Windows.ps1 | iex
   ```

3. Follow the GitHub browser sign-in when prompted. Leave the computer **plugged in, awake and connected to Wi-Fi** with Ollama open. If Windows says a program was just installed but cannot be found, close PowerShell, reopen and run the *same* command once more.

The script installs any missing **Git, Python 3.11, GitHub CLI and Ollama** through Windows Package Manager, downloads/refreshes only the relevant Arena source folders, downloads a local Llama model and sets up a daily **midnight** Windows task. Re-running it updates an existing checkout and refreshes the task and settings. On **Windows with 24+ GB RAM**, the conservative default is `qwen3:4b-instruct` (~2.5 GB model) with **one lane**, because high RAM does not imply an AI-capable GPU. 9–24 GB RAM selects `llama3.2:3b` (~2 GB) with one lane; 5.5–9 GB uses `llama3.2:1b` (~1.3 GB). On 24+ GB macOS systems, Qwen3 8B and two lanes remain the automatic profile. You can override with explicit model/parallel flags, after measuring throughput. Windows installer sets the user-level `OLLAMA_NUM_PARALLEL` to the chosen lane count; **fully quit Ollama from the tray and reopen** to apply it. Under ~5.5 GB RAM, setup stops safely. It also retries any prior pending GitHub uploads without generating new research.

### macOS — alternative

Requires [Homebrew](https://brew.sh) (install first if missing). Open **Terminal**, review the [Mac script](../scripts/overnight/Start-Mac.sh), then run:

```bash
curl -fsSL https://raw.githubusercontent.com/28twagg-ops/TradingBot/main/scripts/overnight/Start-Mac.sh | bash
```

The script uses Homebrew to install missing dependencies, opens Ollama, signs in to GitHub via browser and configures a user `launchd` midnight task.

## What the laptop will do

- **Weekdays: midnight–7:00 AM; Saturdays and Sundays: midnight–10:00 AM America/Chicago.** Cycle researchers **S01–S10** with one sequential worker on Windows by default, or up to two on explicitly supported systems; roughly one pass per 40 minutes while running. With CPU-only inference, the actual pass may exceed that interval. The weekend window follows Central Time, including daylight-saving changes.
- Every bot retains an independent history, with its previously configured [personality](../research/trading-arena/personas.py). Personality inspires brainstorming, but is never a fixed market or strategy assignment.
- Each bot can research any idea it wants using public search metadata and available historical prices, propose falsification tests, and save **research-only** output. Model-generated code is never executed.
- Uses the existing bounded deterministic backtest for supported hourly single-asset ideas. Unsupported or untestable ideas remain research-only.
- Saves all outcomes immediately to `~/.trading-arena/pending/`. Wi-Fi outages do **not** erase pending work.
- Syncs completed immutable experiments to the dedicated **`arena-local-research`** GitHub branch. Scheduled GitHub Actions import them into the canonical `arena-ledger` after the weekday stop and again after the weekend 10 AM stop, using the cloud ledger-write lock. The laptop never updates `ai_state.json`, `state.json`, or Groq's research log.
- **No real-money orders, no new virtual buys/sells, and no paid API fallback.** Independent reviewers still need credible evidence before any later change to execution.

## How to check the first morning

- Status and each bot's work: `~/.trading-arena/MORNING_REPORT.md` (on Windows, open `%USERPROFILE%\.trading-arena\MORNING_REPORT.md`).
- Detailed local log: `~/.trading-arena/overnight.log`.
- Completed individual work: `~/.trading-arena/sent/`; unsynced evidence: `~/.trading-arena/pending/`.
- Uploaded immediately: [isolated laptop research inbox](https://github.com/28twagg-ops/TradingBot/tree/arena-local-research/records/arena/local_research). Imported each morning: [canonical overnight dashboard](https://github.com/28twagg-ops/TradingBot/blob/arena-ledger/records/arena/LOCAL_NIGHTLY.md). Both populate only after successful runs.

Optional manual test **after setup**, using your installed local Python environment:

**Windows PowerShell:**
```powershell
& "$HOME\.trading-arena\venv\Scripts\python.exe" "$HOME\TradingArenaLocal\research\trading-arena\overnight_local.py" --smoke
```

**Two-bot real trial after installing Qwen3 and restarting Ollama (Command Prompt):**
```cmd
"%USERPROFILE%\.trading-arena\venv\Scripts\python.exe" "%USERPROFILE%\TradingArenaLocal\research\trading-arena\overnight_local.py" --model qwen3:8b --parallel 2 --trial
```

Observe the terminal output and review `%USERPROFILE%\.trading-arena\MORNING_REPORT.md`. Trial records are clearly marked as research-only and uploaded to the isolated GitHub inbox when possible.

**Recover unsent research only (no model inference or market-data requests, Command Prompt):**
```cmd
"%USERPROFILE%\.trading-arena\venv\Scripts\python.exe" "%USERPROFILE%\TradingArenaLocal\research\trading-arena\overnight_local.py" --sync-only
```

On Windows, older JSON files may use CRLF line endings while Git stores LF; the sync process now compares normalized JSON to avoid false `REMOTE_EVENT_NOT_CONFIRMED` errors. The installer also attempts this recovery automatically. **Do not delete your `pending` folder.**

**macOS Terminal:**
```bash
"$HOME/.trading-arena/venv/bin/python" "$HOME/TradingArenaLocal/research/trading-arena/overnight_local.py" --smoke
```

`--smoke` sends **one** local test prompt, but does not change accounts or push anything. `--trial --parallel 2 --model qwen3:8b` runs only **S01 and S02** concurrently (then performs the normal research-only GitHub sync) and may be used immediately, outside the overnight window. `--once` performs a full **ten-bot research pass**.

## Important operating conditions

- **Wake/sleep:** macOS launchd or Windows Task Scheduler can run at midnight only when the user session and hardware permit it. Keep the laptop open/awake or use an approved awake/power setting, plugged in and on Wi-Fi. Closing the lid commonly sleeps the laptop; this installer does **not** silently change power settings.
- **Login:** The first GitHub CLI browser login is required to upload research. GitHub CLI's authorization may have broader repository permissions than the one Arena branch; the model never sees that token. Do not copy passwords or tokens into a file or chat.
- **Cloud services:** Ollama's local models require no inference API key. This installer refuses model names containing `:cloud`, remote URLs and nonlocal endpoints. Do not select a cloud model.
- **Quota/duplicates:** Ten researchers share one Ollama instance with **one lane on Windows by default**, or up to two independent in-process lanes on explicitly supported machines. Unique research IDs and Git verification prevent duplicate uploads; an app-only lock blocks overlapping *overnight program instances*. This limit is separate from the two allowed research lanes.
- **Missed schedule:** Windows task runs at midnight if possible and checks its Central-time execution window. If the laptop wakes later, only remaining hours are available. If it wakes after 7 AM on a weekday or after 10 AM on a weekend, it exits without generating new overnight work. Windows Task Scheduler allows a 12-hour maximum runtime to accommodate the extra hour during the fall daylight-saving transition; the runner itself still enforces the local stop time.
- **Slow laptop:** Qwen3 8B already timed out on an Intel i7-1365U running 100% CPU. The CPU-friendly Qwen3 4B Instruct is now the Windows 24+ GB default, but still requires real testing. Some bots may complete fewer ideas than others. Low disk, missing prices, API errors and incompatible history fail safely.
- **No guarantee of profitability:** Research records and proxy backtests are not real fills, statistically proven edge or investment recommendations.

## If setup fails

| Symptom | Action |
|---|---|
| `winget` not found | Update Windows App Installer or install [winget](https://learn.microsoft.com/windows/package-manager/winget/) first |
| Program missing right after install | Open a new terminal and rerun bootstrap |
| `OLLAMA_MODEL_NOT_INSTALLED_OR_SERVICE_OFFLINE` | Open the Ollama desktop app; run `ollama pull llama3.2:3b` (or `llama3.2:1b`) and retry |
| `OLLAMA_INVALID_JSON` or slow generation | Inspect `ollama ps`: 100% CPU processing on an integrated-graphics laptop can be slow. Prefer `qwen3:4b-instruct` with `--parallel 1` until benchmarked. No positions are changed |
| GitHub sign-in fails | In terminal run `gh auth login --web`, then rerun setup |
| GitHub uploads fail | Leave pending local JSON files untouched. Rerun overnight or `--once`; the next successful sync resumes |
| `ANOTHER_RUN_ALREADY_ACTIVE` | Do not start a second run. Wait for the first to finish |
| `ANOTHER_RUN_OR_STALE_LOCK` | Confirm no process is running; then remove `~/.trading-arena/overnight.lock` |
| No output next morning | Check `overnight.log`; verify task exists, Ollama is running, laptop was awake and session logged in |

**Manual pause:** Disable the `TradingArenaOvernightOllama` task in Windows Task Scheduler or disable `com.tradingarena.overnight` in macOS launchd; no GitHub or local trade history needs deletion.

## Implementation and safety notes

Files: `local_ollama.py` (local inference adapter), `overnight_local.py` (scheduler / checkpoints / Git sync), `setup_local.py` (installer and OS task), `scripts/overnight/Start-*.ps1/.sh` (bootstraps). GitHub-hosted cloud workflows continue independently.

**Acceptance criteria before relying on nightly results:** CI tests pass, real local smoke succeeds, model fits RAM, login works, one research pass produces immutable remote events, and the importer serializes successfully with cloud ledger updates. Disconnect/restart tests must retain pending work.

Source references: [Ollama official download](https://ollama.com/download), [Llama 3.2 models](https://ollama.com/library/llama3.2), [GitHub CLI sign-in](https://cli.github.com/manual/gh_auth_login).
