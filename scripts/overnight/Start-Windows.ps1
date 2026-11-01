# Trading Arena Windows one-time installer. Read before running.
# Installs missing dependencies with official Windows Package Manager (winget).
$ErrorActionPreference = "Stop"
Write-Host "Trading Arena - local-only overnight Ollama research setup"
Write-Host "This installs missing Git, GitHub CLI, Python and Ollama programs."
Write-Host "No broker credentials, cloud inference services, or paid API fallback."
$tools = @(
    @{ Command="git"; Id="Git.Git" },
    @{ Command="gh"; Id="GitHub.cli" },
    @{ Command="py"; Id="Python.Python.3.11" },
    @{ Command="ollama"; Id="Ollama.Ollama" }
)
function Test-ArenaPython {
    if (-not (Get-Command py -ErrorAction SilentlyContinue)) { return $false }
    & py -3 -c 'import sys; assert sys.version_info >= (3,11)' 2>$null
    return ($LASTEXITCODE -eq 0)
}
$missing = @($tools | Where-Object {
    if ($_.Command -eq "py") { -not (Test-ArenaPython) }
    else { -not (Get-Command $_.Command -ErrorAction SilentlyContinue) }
})
if ($missing.Count -gt 0) {
    if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
        throw "Windows Package Manager (winget) is required. See docs/ARENA_LAPTOP_QUICKSTART.md."
    }
    $answer = Read-Host "Install missing programs with winget? (Y/n)"
    if ($answer -match '^[Nn]') { throw "Setup cancelled." }
    foreach ($tool in $missing) {
        Write-Host "Installing $($tool.Id)..."
        & winget install --id $tool.Id --exact --accept-source-agreements --accept-package-agreements
        if ($LASTEXITCODE -ne 0) { throw "Install failed for $($tool.Id). Please install manually." }
    }
    $env:Path = [Environment]::GetEnvironmentVariable("Path", "Machine") + ";" +
        [Environment]::GetEnvironmentVariable("Path", "User")
}
foreach ($tool in $tools) {
    if (($tool.Command -eq "py" -and -not (Test-ArenaPython)) -or
        ($tool.Command -ne "py" -and -not (Get-Command $tool.Command -ErrorAction SilentlyContinue))) {
        throw "$($tool.Command) not found yet. Open a NEW PowerShell window and rerun this same setup."
    }
}
$dir = Join-Path $HOME "TradingArenaLocal"
if (-not (Test-Path (Join-Path $dir ".git"))) {
    & git clone --quiet --depth 1 --filter=blob:none --sparse --branch main https://github.com/28twagg-ops/TradingBot.git $dir
    if ($LASTEXITCODE -ne 0) { throw "Failed to fetch Arena source from GitHub." }
}
& git -C $dir sparse-checkout set research/trading-arena scripts/overnight docs
if ($LASTEXITCODE -ne 0) { throw "Sparse source checkout failed." }
# Re-running this bootstrap also updates an existing installation safely.
& git -C $dir pull --ff-only origin main
if ($LASTEXITCODE -ne 0) { throw "Could not fast-forward local Arena source. No files were overwritten." }
Write-Host "GitHub sign-in and model installation will be handled by the guided setup."
& py -3 (Join-Path $dir "research/trading-arena/setup_local.py")
if ($LASTEXITCODE -ne 0) { throw "Local Arena setup did not complete. See troubleshooting document." }
Write-Host "Done. Midnight-7 AM weekdays / midnight-10 AM weekends Central; keep laptop on and awake."
