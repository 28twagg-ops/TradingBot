"""Local documentation root (TradingBot workspace — not pushed to GitHub).

On GitHub Actions there is no sibling local workspace, so callers should treat
a missing/unavailable docs root as optional.
"""
from __future__ import annotations

import os
from pathlib import Path

GIT_REPO = Path(__file__).resolve().parent.parent
# Local desktop layout: TradingBot-git/../TradingBot/docs
LOCAL_DOCS = GIT_REPO.parent / "TradingBot" / "docs"


def local_docs_available() -> bool:
    """True when we should write human docs (local machine, not GHA)."""
    if os.environ.get("GITHUB_ACTIONS", "").strip().lower() in ("1", "true", "yes"):
        return False
    return True


def local_docs(*parts: str) -> Path:
    """Return (and create) a path under the local docs folder."""
    if not local_docs_available():
        # Scratch path inside the runner workspace; never relied on for commits.
        base = GIT_REPO / "logs" / "_docs_scratch"
    else:
        base = LOCAL_DOCS
    p = base.joinpath(*parts) if parts else base
    p.mkdir(parents=True, exist_ok=True)
    return p
