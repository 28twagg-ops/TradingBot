#!/usr/bin/env python3
"""Move find_repo_root bootstrap to immediately after from __future__."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

BLOCK_RE = re.compile(
    r"try:\n"
    r"    from repo_root import find_repo_root\n"
    r"except ImportError:\n"
    r"    import sys as _sys\n"
    r"    from pathlib import Path as _Path\n"
    r"    _sys\.path\.insert\(0, str\(_Path\(__file__\)\.resolve\(\)\.parents\[\d+\] / \"live-bots\" / \"shared\"\)\)\n"
    r"    from repo_root import find_repo_root\n\n?",
    re.M,
)

BOOTSTRAP_TMPL = """\
try:
    from repo_root import find_repo_root
except ImportError:
    import sys as _sys
    from pathlib import Path as _Path
    _sys.path.insert(0, str(_Path(__file__).resolve().parents[{depth}] / "live-bots" / "shared"))
    from repo_root import find_repo_root
"""


def process(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "from repo_root import find_repo_root" not in text:
        return False
    m = BLOCK_RE.search(text)
    if not m:
        print("BLOCK NOT MATCHED", path)
        return False
    text2 = BLOCK_RE.sub("", text, count=1)
    depth = len(path.relative_to(ROOT).parts) - 1
    block = BOOTSTRAP_TMPL.format(depth=depth)
    fut = "from __future__ import annotations"
    idx = text2.find(fut)
    if idx == -1:
        # insert after module docstring if any
        if text2.lstrip().startswith(('"""', "'''")):
            print("NO FUTURE", path)
            return False
        text2 = block + "\n" + text2
    else:
        end = idx + len(fut)
        # consume trailing newline
        if end < len(text2) and text2[end] == "\r":
            end += 1
        if end < len(text2) and text2[end] == "\n":
            end += 1
        text2 = text2[:end] + "\n" + block + "\n" + text2[end:]
    if text2 != text:
        path.write_text(text2, encoding="utf-8", newline="\n")
        print("fixed", path.relative_to(ROOT))
        return True
    return False


def main() -> None:
    n = 0
    for p in ROOT.rglob("*.py"):
        if "_reorg" in p.parts:
            continue
        if "find_repo_root" in p.read_text(encoding="utf-8", errors="ignore"):
            if p.name == "repo_root.py":
                continue
            if process(p):
                n += 1
    print("fixed count", n)


if __name__ == "__main__":
    main()
