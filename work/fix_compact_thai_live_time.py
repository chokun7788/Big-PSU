from pathlib import Path


project = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
source = project / "app" / "booking" / "live_status.py"
tests = project / "tests" / "test_p0_calendar_booking_reconciliation_20260925.py"


def replace_once(path: Path, old: str, new: str) -> None:
    content = path.read_text(encoding="utf-8")
    if content.count(old) != 1:
        raise RuntimeError(f"Expected exactly one matching block in {path}: found {content.count(old)}")
    path.write_text(content.replace(old, new), encoding="utf-8")


replace_once(
    source,
    '''    point = re.search(r"\\b([01]?\\d|2[0-3]):([0-5]\\d)\\b", q)
    if point:
        value = _clock(point.group(1), point.group(2))
        return TimeWindow(value, explicit=True) if value else None
    hour = re.search(r"\\b([01]?\\d|2[0-3])\\s*(?:โมง|am|pm)\\b", q)
    if hour:
        value = _clock(hour.group(1), suffix=hour.group(0)[-2:] if hour.group(0).endswith(("am", "pm")) else "")
        return TimeWindow(value, explicit=True) if value else None
    if snapshot.now:
        time_match = re.search(r"\\b(\\d{2}:\\d{2})", snapshot.now)
        if time_match:
            return TimeWindow(time_match.group(1), explicit=False)
''',
    '''    # Thai often joins the time to the preceding word ("ตอน10โมง").
    point = re.search(r"(?<!\\d)([01]?\\d|2[0-3]):([0-5]\\d)(?!\\d)", q)
    if point:
        value = _clock(point.group(1), point.group(2))
        return TimeWindow(value, explicit=True) if value else None
    hour = re.search(r"(?<![a-z0-9])([01]?\\d|2[0-3])\\s*(โมง|am|pm)(ครึ่ง)?", q)
    if hour:
        value = _clock(hour.group(1), "30" if hour.group(3) else "00", hour.group(2))
        return TimeWindow(value, explicit=True) if value else None
    if snapshot.now:
        # Anchor the fallback to the time portion of the timestamp. A word
        # boundary can otherwise select its minutes/seconds as the hour.
        time_match = re.search(r"(?:T|\\s)(\\d{2}:\\d{2})(?::\\d{2})?", snapshot.now)
        if time_match:
            return TimeWindow(time_match.group(1), explicit=False)
''',
)

replace_once(
    tests,
    '''    render_live_booking_answer,
)
''',
    '''    render_live_booking_answer,
    requested_time_window,
)
''',
)
replace_once(
    tests,
    '''    def test_regular_open_window_can_report_booking_fact(self) -> None:
''',
    '''    def test_compact_thai_station_time_reads_requested_hour(self) -> None:
        status = snapshot("2026-09-29", "08:00")
        for query, expected in (
            ("วันนี้ตอน10โมง PC1 ว่างไหม", "10:00"),
            ("วันนี้ตอน10:00 PC1 ว่างไหม", "10:00"),
            ("วันนี้ตอน10โมงครึ่ง PC1 ว่างไหม", "10:30"),
            ("Is PC1 free today at 10am?", "10:00"),
        ):
            with self.subTest(query=query):
                window = requested_time_window(query, status)
                self.assertIsNotNone(window)
                self.assertEqual(window.start, expected)
                self.assertTrue(window.explicit)
        self.assertEqual(requested_time_window("PC1 ว่างไหม", status).start, "08:00")

    def test_regular_open_window_can_report_booking_fact(self) -> None:
''',
)
print("Patched compact Thai time parsing and added a regression test.")
