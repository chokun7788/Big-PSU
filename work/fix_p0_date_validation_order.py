from __future__ import annotations

import argparse
import difflib
import hashlib
import os
from pathlib import Path


SOURCE = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\app\booking\live_status.py")
WORK = Path(__file__).resolve().parent
HASH_FILE = WORK / "p0_date_order_before.sha256"
DIFF_FILE = WORK / "p0_date_order_preview.diff"
OLD = '''            snapshot = _snapshot_from_payload(payload)
            if snapshot.date != selected_date:
                raise ValueError(f"booking dashboard returned date {snapshot.date!r}, expected {selected_date!r}")
'''
NEW = '''            returned_date = str(payload.get("date") or "")
            if returned_date != selected_date:
                raise ValueError(f"booking dashboard returned date {returned_date!r}, expected {selected_date!r}")
            snapshot = _snapshot_from_payload(payload)
'''


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    original = SOURCE.read_bytes()
    text = original.decode("utf-8")
    if text.count(OLD) != 1:
        raise RuntimeError("source changed or expected block is missing")
    updated = text.replace(OLD, NEW, 1)
    compile(updated, str(SOURCE), "exec")
    digest = hashlib.sha256(original).hexdigest()
    if not args.apply:
        HASH_FILE.write_text(digest, encoding="ascii")
        DIFF_FILE.write_text("".join(difflib.unified_diff(
            text.splitlines(keepends=True), updated.splitlines(keepends=True),
            fromfile="a/app/booking/live_status.py", tofile="b/app/booking/live_status.py",
        )), encoding="utf-8")
        print(DIFF_FILE)
        return
    if HASH_FILE.read_text(encoding="ascii") != digest:
        raise RuntimeError("source changed after preview")
    temporary = SOURCE.with_name(SOURCE.name + ".p0tmp")
    if temporary.exists():
        raise RuntimeError(f"temporary path already exists: {temporary}")
    temporary.write_text(updated, encoding="utf-8", newline="")
    os.replace(temporary, SOURCE)
    print(f"Updated {SOURCE}")


if __name__ == "__main__":
    main()
