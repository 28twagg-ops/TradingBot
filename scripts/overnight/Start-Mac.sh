#!/bin/bash
# Trading Arena macOS one-time installer; local research only.
set -euo pipefail
echo "Trading Arena - overnight local Ollama setup"
if ! command -v brew >/dev/null 2>&1; then
  echo "Install Homebrew from https://brew.sh and rerun this command."
  exit 2
fi
if ! command -v git >/dev/null 2>&1; then brew install git; fi
if ! command -v gh >/dev/null 2>&1; then brew install gh; fi
if ! command -v python3.11 >/dev/null 2>&1; then brew install python@3.11; fi
if ! command -v ollama >/dev/null 2>&1; then brew install --cask ollama; fi
open -a Ollama || true
DIRECTORY="$HOME/TradingArenaLocal"
if [ ! -d "$DIRECTORY/.git" ]; then
  git clone --quiet --filter=blob:none --depth 1 --sparse --branch main \
    https://github.com/28twagg-ops/TradingBot.git "$DIRECTORY"
fi
git -C "$DIRECTORY" sparse-checkout set research/trading-arena scripts/overnight docs
python3.11 "$DIRECTORY/research/trading-arena/setup_local.py"
echo "Done. Nightly research is scheduled; keep laptop awake and Ollama running."
