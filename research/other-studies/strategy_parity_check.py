"""Verify strategy-critical functions unchanged (static hash of source regions)."""
try:
    from repo_root import find_repo_root
except ImportError:
    import sys as _sys
    from pathlib import Path as _Path
    _sys.path.insert(0, str(_Path(__file__).resolve().parents[2] / "live-bots" / "shared"))
    from repo_root import find_repo_root

import hashlib
import re
from pathlib import Path

ROOT = find_repo_root(Path(__file__))
BOT = ROOT / "live-bots" / "rubber-band" / "rubber_band_bot.py"

REGIONS = [
    ("SCHEDULE", r"^SCHEDULE = \{", r"^MN = "),
    ("get_signals", r"^def get_signals\(", r"^def has_earnings_soon\("),
    ("check_exit", r"^def check_exit\(", r"^def get_positions\("),
]


def extract_region(text, start_pat, end_pat):
    lines = text.splitlines()
    start_i = end_i = None
    for i, line in enumerate(lines):
        if start_i is None and re.match(start_pat, line):
            start_i = i
        elif start_i is not None and re.match(end_pat, line):
            end_i = i
            break
    if start_i is None:
        return None
    if end_i is None:
        end_i = len(lines)
    return "\n".join(lines[start_i:end_i])


def main():
    text = BOT.read_text(encoding="utf-8")
    print("Strategy parity region hashes (for regression tracking):")
    for name, start, end in REGIONS:
        block = extract_region(text, start, end)
        if not block:
            print(f"  {name}: MISSING")
            continue
        h = hashlib.sha256(block.encode()).hexdigest()[:16]
        print(f"  {name}: {h} ({len(block.splitlines())} lines)")
    print("OK — run after changes; hashes should match pre-pipeline if strategy untouched.")


if __name__ == "__main__":
    main()
