"""Post-PDT-removal verification (Phase C4 checklist)."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOT = ROOT / "rubber_band_bot.py"


def main():
    text = BOT.read_text(encoding="utf-8")
    checks = [
        ("STRICT_SAME_DAY_EXIT absent", "STRICT_SAME_DAY_EXIT" not in text),
        ("_pdt_blocks_exit absent", "_pdt_blocks_exit" not in text),
        ("pdt_ok absent", "def pdt_ok" not in text),
        ("save_pdt absent", "def save_pdt" not in text),
        ("load_pdt absent", "def load_pdt" not in text),
        ("entry_slot_ok present", "def entry_slot_ok" in text),
        ("EVENING_ONLY_ENTRIES present", "EVENING_ONLY_ENTRIES" in text),
        ("MAX_OPEN_POSITIONS present", "MAX_OPEN_POSITIONS" in text),
        ("no deprecated field reads", ".daytrade_count" not in text and ".pattern_day_trader" not in text),
    ]
    print("PDT removal verification:")
    ok = True
    for name, passed in checks:
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {name}")
        ok = ok and passed
    try:
        import py_compile
        py_compile.compile(str(BOT), doraise=True)
        print("  [PASS] py_compile rubber_band_bot.py")
    except Exception as e:
        print(f"  [FAIL] py_compile: {e}")
        ok = False
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
