"""Locate the TradingBot repository root regardless of package nesting."""
from __future__ import annotations

from pathlib import Path


def find_repo_root(start: Path | None = None) -> Path:
    here = (start or Path(__file__)).resolve()
    if here.is_file():
        here = here.parent
    for cand in [here, *here.parents]:
        if (cand / "logs").is_dir() and (
            (cand / ".git").exists()
            or (cand / ".github").is_dir()
            or (cand / "requirements.txt").is_file()
        ):
            return cand
    raise RuntimeError(f"TradingBot repo root not found from {start}")
