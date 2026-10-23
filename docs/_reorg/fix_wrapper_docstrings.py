#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
paths = [ROOT / "rubber_band_bot.py"]
paths += list((ROOT / "scripts").glob("*.py"))
paths += list((ROOT / "simulations").glob("*.py"))
rx = re.compile(r'"""Compatibility wrapper.{0,8}canonical module: ([^"]+)"""')
n = 0
for p in paths:
    if not p.is_file():
        continue
    t = p.read_text(encoding="utf-8")
    m = rx.match(t.splitlines()[0] if t else "")
    if not m and "Compatibility wrapper" in t[:80]:
        # rebuild first line
        lines = t.splitlines()
        # extract target from _TARGET or from garbled first line
        tm = re.search(r'canonical module:\s*(.+?)"""', lines[0])
        if not tm:
            continue
        target = tm.group(1).strip()
        lines[0] = f'"""Compatibility wrapper - canonical module: {target}"""'
        p.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
        n += 1
        print("fixed", p.relative_to(ROOT))
print("count", n)
