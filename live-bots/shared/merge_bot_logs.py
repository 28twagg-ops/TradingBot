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


def merge_daily_md(src: Path, dst: Path):
    """Keep the newest daily log (evening scan beats morning via footer timestamp)."""
    if not src.exists():
        return
    if not dst.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        return

    def _stamp(text: str) -> str:
        m = re.search(r"_RBv8\s*(\d{4}-\d{2}-\d{2}T[\d:Z]+)_", text)
        if m:
            return m.group(1)
        m = re.search(r"_RBv8(\d{2}:\d{2} UTC)_", text)
        return m.group(1) if m else ""

    src_text = src.read_text(encoding="utf-8")
    dst_text = dst.read_text(encoding="utf-8")
    src_s, dst_s = _stamp(src_text), _stamp(dst_text)
    if src_s > dst_s or (src_s == dst_s and len(src_text) >= len(dst_text)):
        shutil.copy2(src, dst)


CANONICAL_RUN_INDEX_FIELDS = [
    "run_stamp", "run_number", "run_id",
    "live_exit", "live_options_exit", "options_exit",
    "live_duration_s", "live_options_duration_s", "options_duration_s",
    "event_type",
]


def _normalize_run_index_row(row: dict) -> dict:
    out = {k: str(row.get(k) or "").strip() for k in CANONICAL_RUN_INDEX_FIELDS}
    ev = out.get("event_type", "")
    # Rows appended after live_options split but before header migration:
    # event_type holds live_options_duration_s (numeric).
    if ev.isdigit():
        out["live_options_duration_s"] = ev
        out["options_duration_s"] = "0"
        out["event_type"] = "workflow_dispatch"
        out["live_duration_s"] = str(row.get("options_duration_s") or out.get("live_duration_s") or "0")
        out["options_exit"] = str(row.get("options_exit") or "0")
        out["live_options_exit"] = "0"
    elif not out.get("live_options_exit") and "live_options_exit" not in (row.keys() or []):
        out["live_options_exit"] = "0"
        out["live_options_duration_s"] = str(row.get("options_duration_s") or "0")
        out["options_duration_s"] = "0"
    if not out.get("event_type"):
        out["event_type"] = "workflow_dispatch"
    return out


def merge_run_index_csv(src: Path, dst: Path):
    """Append-only merge for daily action run index CSVs."""
    if not src.exists():
        return
    if not dst.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        return
    _, src_rows = _read_csv(src)
    _, dst_rows = _read_csv(dst)
    seen = set()
    merged = []
    for r in dst_rows + src_rows:
        norm = _normalize_run_index_row(r)
        key = norm.get("run_stamp") or norm.get("run_id") or ""
        if not key or key in seen:
            continue
        seen.add(key)
        merged.append(norm)
    merged.sort(key=lambda r: str(r.get("run_stamp") or ""))
    _write_csv(dst, CANONICAL_RUN_INDEX_FIELDS, merged)


def merge_comprehensive_review(src: Path, dst: Path):
    """Append run sections; keep header once."""
    if not src.exists():
        return
    if not dst.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        return
    src_text = src.read_text(encoding="utf-8")
    dst_text = dst.read_text(encoding="utf-8")
    for block in re.split(r"(?=^## Run )", src_text, flags=re.MULTILINE):
        block = block.strip()
        if not block.startswith("## Run "):
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
        elif (len(rel.parts) >= 3 and rel.parts[0] == "action_runs"
              and rel.parts[1] == "reports"
              and item.name.endswith("_run_index.csv")):
            merge_run_index_csv(item, target)
        elif (len(rel.parts) >= 3 and rel.parts[0] == "action_runs"
              and rel.parts[1] == "reports"
              and item.name.endswith("_comprehensive_review.md")):
            merge_comprehensive_review(item, target)
        elif len(rel.parts) >= 2 and rel.parts[0] == "options" and item.suffix == ".md":
            merge_options_md(item, target)
        elif len(rel.parts) == 2 and rel.parts[0] == "daily" and item.suffix == ".md":
            merge_daily_md(item, target)
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
