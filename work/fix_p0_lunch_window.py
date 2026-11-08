from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import os
from pathlib import Path


REPO = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
WORK = Path(__file__).resolve().parent
FILES = ["booking_dashboard/server.py", "tests/test_p0_calendar_booking_reconciliation_20260925.py"]
MANIFEST = WORK / "p0_lunch_manifest.json"
DIFF = WORK / "p0_lunch_preview.diff"


def once(text: str, old: str, new: str, path: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected one match, got {count}: {old[:90]!r}")
    return text.replace(old, new, 1)


def transform(path: str, source: str) -> str:
    if path == "booking_dashboard/server.py":
        source = once(
            source,
            '\n\ndef weekday_key_from_date(selected_date: str) -> str:\n',
            '\n\ndef exclude_lunch_break(periods: List[List[str]]) -> List[List[str]]:\n'
            '    """Keep owner opening bounds while excluding the confirmed 12:00-13:00 booking break."""\n'
            '    bookable: List[List[str]] = []\n'
            '    for start, end in periods:\n'
            '        if start < "12:00":\n'
            '            morning_end = min(end, "12:00")\n'
            '            if start < morning_end:\n'
            '                bookable.append([start, morning_end])\n'
            '        if end > "13:00":\n'
            '            afternoon_start = max(start, "13:00")\n'
            '            if afternoon_start < end:\n'
            '                bookable.append([afternoon_start, end])\n'
            '    return bookable\n'
            '\n\ndef weekday_key_from_date(selected_date: str) -> str:\n',
            path,
        )
        source = once(
            source,
            '        if is_open and not periods:\n'
            '            hours = cfg.get("hours") if isinstance(cfg.get("hours"), dict) else schedule.get("default_hours", {})\n'
            '            periods = normalize_periods([[hours.get("start", "09:00"), hours.get("end", "16:00")]])\n'
            '        return {\n',
            '        if is_open and not periods:\n'
            '            hours = cfg.get("hours") if isinstance(cfg.get("hours"), dict) else schedule.get("default_hours", {})\n'
            '            periods = normalize_periods([[hours.get("start", "09:00"), hours.get("end", "16:00")]])\n'
            '        periods = exclude_lunch_break(periods)\n'
            '        return {\n',
            path,
        )
        source = once(
            source,
            '    periods = normalize_periods(cfg.get("open_periods"))\n    return {\n',
            '    periods = exclude_lunch_break(normalize_periods(cfg.get("open_periods")))\n    return {\n',
            path,
        )
    elif path == "tests/test_p0_calendar_booking_reconciliation_20260925.py":
        source = once(source, 'from datetime import date\n', 'from datetime import date, datetime\n', path)
        source = once(
            source,
            'from app.runtime.fast_answer import answer_schedule\n',
            'from app.runtime.fast_answer import answer_schedule\n'
            'from booking_dashboard import server as dashboard\n',
            path,
        )
        source = once(
            source,
            '\n\nif __name__ == "__main__":\n',
            '\n\n    def test_dashboard_weekly_lunch_is_not_bookable(self) -> None:\n'
            '        for day, open_at_13 in (("2026-09-28", True), ("2026-09-29", True), ("2026-10-02", False)):\n'
            '            with self.subTest(day=day), patch.object(dashboard, "now_bangkok", return_value=datetime(2026, 9, 25, 8, 0)):\n'
            '                status = dashboard.build_status(\n'
            '                    [], [{"id": "1", "name": "PC #01", "duration": "60"}], day,\n'
            '                    {"mode": "remote_csv_live", "appointments_meta": {"hash": "fixture"}, "services_meta": {"hash": "fixture"}},\n'
            '                )\n'
            '                lunch = next(s for s in status["services"][0]["slots"] if s["start"] == "12:00")\n'
            '                self.assertEqual((lunch["status"], lunch["available_count"]), ("closed", 0))\n'
            '                self.assertFalse(any(start <= "12:30" < end for start, end in status["center"]["open_periods"]))\n'
            '                at_13 = next(s for s in status["services"][0]["slots"] if s["start"] == "13:00")\n'
            '                self.assertEqual(at_13["status"] == "available", open_at_13)\n'
            '\n'
            '    def test_dashboard_date_override_cannot_open_lunch(self) -> None:\n'
            '        schedule = dashboard.default_center_schedule()\n'
            '        schedule["dates"]["2026-09-29"] = {"open": True, "open_periods": [["11:00", "14:00"]]}\n'
            '        with patch.object(dashboard, "load_center_schedule", return_value=schedule):\n'
            '            center = dashboard.center_status_for_date("2026-09-29")\n'
            '        self.assertEqual(center["source"], "date_override")\n'
            '        self.assertEqual(center["open_periods"], [["11:00", "12:00"], ["13:00", "14:00"]])\n'
            '\n\nif __name__ == "__main__":\n',
            path,
        )
    else:
        raise RuntimeError(path)
    return source


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    changed: dict[str, tuple[bytes, bytes]] = {}
    for path in FILES:
        original = (REPO / path).read_bytes()
        updated = transform(path, original.decode("utf-8")).encode("utf-8")
        compile(updated.decode("utf-8"), path, "exec")
        changed[path] = original, updated
    DIFF.write_text("".join(
        line for path, (before, after) in changed.items()
        for line in difflib.unified_diff(
            before.decode("utf-8").splitlines(keepends=True),
            after.decode("utf-8").splitlines(keepends=True),
            fromfile=f"a/{path}", tofile=f"b/{path}",
        )
    ), encoding="utf-8")
    if not args.apply:
        MANIFEST.write_text(json.dumps({path: {"before": digest(before), "after": digest(after)} for path, (before, after) in changed.items()}, indent=2), encoding="utf-8")
        print(DIFF)
        return
    expected = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for path, (before, after) in changed.items():
        if digest(before) != expected[path]["before"] or digest(after) != expected[path]["after"]:
            raise RuntimeError(f"file changed after preview: {path}")
    for path, (_, after) in changed.items():
        target = REPO / path
        temporary = target.with_name(target.name + ".lunchtmp")
        if temporary.exists():
            raise RuntimeError(f"temporary exists: {temporary}")
        temporary.write_bytes(after)
        os.replace(temporary, target)
        print(f"Updated {target}")


if __name__ == "__main__":
    main()
