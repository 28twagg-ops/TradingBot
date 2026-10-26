"""Compatibility wrapper — canonical module: research/other-studies/run_options_research.py

Do not edit trading logic here. GHA and local tools may still invoke this path.
"""
from __future__ import annotations

import runpy
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_SEARCH = [
    _ROOT / "live-bots/options-paper/lab",
    _ROOT / "live-bots/options-paper/strategies",
    _ROOT / "live-bots/options-paper/bot",
    _ROOT / "live-bots/options-paper/reporting",
    _ROOT / "live-bots/options-micro",
    _ROOT / "live-bots/shared",
    _ROOT / "live-bots/rubber-band",
    _ROOT / "research/market-research",
    _ROOT / "research/other-studies",
    _ROOT / "research/options-strategies/backtests",
    _ROOT / "research/options-strategies/experiments"
]
for _p in _SEARCH:
    _s = str(_p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

_TARGET = _ROOT / "research" / "other-studies" / "run_options_research.py"
if not _TARGET.is_file():
    raise SystemExit(f"wrapper target missing: {_TARGET}")

if __name__ == "__main__":
    sys.argv[0] = str(_TARGET)
    runpy.run_path(str(_TARGET), run_name="__main__")
else:
    # Import-time: load real module into this namespace for `import options_lab` style.
    _mod = runpy.run_path(str(_TARGET), run_name=__name__)
    globals().update({k: v for k, v in _mod.items() if not k.startswith("__")})
    globals()["__file__"] = str(_TARGET)
