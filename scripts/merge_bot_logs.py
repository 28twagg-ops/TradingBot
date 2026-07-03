"""
Merge log output from a bot run into the repo's logs/ directory.
Used by CI to avoid git rebase conflicts on append-only CSV files.
"""
import csv
import re
import shutil
import sys
from pathlib import Path


def _read_csv(path):
    if not path.exists():
        return [], []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        return fields, list(reader)


def _write_csv(path, fields, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)


def merge_csv(name, src_dir, dst_dir):
    src = src_dir / name
    dst = dst_dir / name
    if not src.exists():
        return
    src_fields, src_rows = _read_csv(src)
    dst_fields, dst_rows = _read_csv(dst)
    all_fields = list(dict.fromkeys(dst_fields + src_fields))
    seen = set()
    merged = []
    for r in dst_rows + src_rows:
        key = "|".join(str(r.get(c, "")) for c in all_fields[:3])  # timestamp-heavy key
        if key in seen:
            continue
        seen.add(key)
        merged.append(r)
    _write_csv(dst, all_fields, merged)


def merge_options_md(src: Path, dst: Path):
    """Append-only merge for logs/options/YYYY-MM-DD.md run sections."""
    if not src.exists():
        return
    if not dst.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        return
    src_text = src.read_text(encoding="utf-8")
    dst_text = dst.read_text(encoding="utf-8")
    for block in re.split(r"(?=^## \d)", src_text, flags=re.MULTILINE):
        block = block.strip()
        if not block.startswith("## "):
            continue
        header = block.split("\n", 1)[0].strip()
        if header not in dst_text:
            dst_text = dst_text.rstrip() + "\n\n" + block + "\n"
    dst.write_text(dst_text, encoding="utf-8")


def merge_tree(src: Path, dst: Path):
    if not src.exists():
        return
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.rglob("*"):
        if item.is_dir():
            continue
        rel = item.relative_to(src)
        # Options paper trial logs are committed by options_morning_bot.yml only.
        if rel.parts and rel.parts[0] == "options_trial":
            continue
        target = dst / rel
        if item.suffix == ".csv" and item.name in ("runs.csv", "transactions.csv", "execution_audit.csv"):
            merge_csv(item.name, item.parent, target.parent)
        elif len(rel.parts) >= 2 and rel.parts[0] == "options" and item.suffix == ".md":
            merge_options_md(item, target)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists() or item.stat().st_mtime >= target.stat().st_mtime:
                shutil.copy2(item, target)


def main():
    if len(sys.argv) != 3:
        print("Usage: merge_bot_logs.py <src_logs_dir> <dst_logs_dir>")
        sys.exit(1)
    merge_tree(Path(sys.argv[1]), Path(sys.argv[2]))
    print(f"Merged {sys.argv[1]} -> {sys.argv[2]}")


if __name__ == "__main__":
    main()
