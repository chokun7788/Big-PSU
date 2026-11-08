from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import os
from pathlib import Path


REPO = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
WORK = Path(__file__).resolve().parent
MANIFEST = WORK / "p0_patch_manifest.json"
DIFF = WORK / "p0_patch_preview.diff"


def replace_once(text: str, old: str, new: str, path: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected one match, found {count}: {old[:80]!r}")
    return text.replace(old, new, 1)


def transform(path: str, source: str) -> str:
    if path == "app/calendar/service_calendar.py":
        source = replace_once(
            source,
            '    numeric_match = re.search(r"\\b(\\d{1,2})[/-](\\d{1,2})(?:[/-](\\d{2,4}))?\\b", q)\n',
            '    iso_match = re.search(r"(?<!\\d)(\\d{4})-(\\d{1,2})-(\\d{1,2})(?!\\d)", q)\n'
            '    if iso_match:\n'
            '        year = _parse_year(iso_match.group(1), base.year)\n'
            '        try:\n'
            '            target = date(year, int(iso_match.group(2)), int(iso_match.group(3)))\n'
            '        except ValueError:\n'
            '            return None\n'
            '        return DateResolution(target, f"วันที่ {format_thai_date(target)}", "explicit_date")\n\n'
            '    numeric_match = re.search(r"\\b(\\d{1,2})[/-](\\d{1,2})(?:[/-](\\d{2,4}))?\\b", q)\n',
            path,
        )
    elif path == "app/booking/live_status.py":
        source = replace_once(
            source,
            'from app.calendar.service_calendar import resolve_date_from_text, today_bangkok\n',
            'from app.calendar.service_calendar import closure_for, regular_service_slots, resolve_date_from_text, today_bangkok\n',
            path,
        )
        source = replace_once(
            source,
            '    center = payload.get("center") if isinstance(payload.get("center"), dict) else {}\n',
            '    center = payload.get("center")\n'
            '    if not isinstance(center, dict) or not isinstance(center.get("open"), bool):\n'
            '        raise ValueError("booking dashboard returned no valid center state")\n',
            path,
        )
        source = replace_once(
            source,
            '    return LiveBookingSnapshot(\n        ok=True,\n',
            '    if not resources:\n'
            '        raise ValueError("booking dashboard returned no valid resources")\n\n'
            '    return LiveBookingSnapshot(\n        ok=True,\n',
            path,
        )
        source = replace_once(
            source,
            '    asks_use_now = asks_live and bool(_resource_scopes(q)) and (\n',
            '    asks_center_use_now = asks_live and any(\n'
            '        phrase in q for phrase in ("ตอนนี้เล่นได้ไหม", "ตอนนี้เล่นได้มั้ย", "ตอนนี้ใช้ได้ไหม", "ตอนนี้ใช้ได้มั้ย")\n'
            '    )\n'
            '    asks_use_now = asks_live and bool(_resource_scopes(q)) and (\n',
            path,
        )
        source = replace_once(
            source,
            '    return asks_resource_availability or asks_use_now or (asks_live and asks_availability) or asks_time_availability or (\n',
            '    return asks_resource_availability or asks_use_now or asks_center_use_now or (asks_live and asks_availability) or asks_time_availability or (\n',
            path,
        )
        source = replace_once(
            source,
            '\n\ndef _time_context(snapshot: LiveBookingSnapshot, window: TimeWindow | None, locale: str) -> str:\n',
            '\n\ndef live_booking_calendar_conflict(query: str, snapshot: LiveBookingSnapshot) -> str | None:\n'
            '    """Flag a claimed open Dashboard window that the recorded calendar does not support.\n\n'
            '    This does not choose which source controls bookings; it prevents a false\n'
            '    availability claim until the owner reconciles the two schedules.\n'
            '    """\n'
            '    if not snapshot.ok or not snapshot.center_open:\n'
            '        return None\n'
            '    window = requested_time_window(query, snapshot)\n'
            '    if window is None or not is_open_for_window(snapshot, window):\n'
            '        return None\n'
            '    try:\n'
            '        target = date.fromisoformat(snapshot.date)\n'
            '    except ValueError:\n'
            '        return None\n'
            '    closure = closure_for(target)\n'
            '    if closure is not None and closure.status == "closed":\n'
            '        return "recorded_special_closure"\n'
            '    for period in regular_service_slots(target):\n'
            '        if period["state"] != "open":\n'
            '            continue\n'
            '        start, end = period["start"], period["end"]\n'
            '        if start <= window.start and (window.end <= end if window.end else window.start < end):\n'
            '            return None\n'
            '    return "published_service_hours"\n'
            '\n\ndef _time_context(snapshot: LiveBookingSnapshot, window: TimeWindow | None, locale: str) -> str:\n',
            path,
        )
        source = replace_once(
            source,
            '    window = requested_time_window(query, snapshot)\n    resource_groups = _resource_groups_for_query(snapshot, query)\n',
            '    conflict = live_booking_calendar_conflict(query, snapshot)\n'
            '    if conflict is not None:\n'
            '        window = requested_time_window(query, snapshot)\n'
            '        when = window.label if window is not None else "the requested time"\n'
            '        if english:\n'
            '            return (\n'
            '                f"For {snapshot.date} at {when} (Asia/Bangkok), the Booking Dashboard and the recorded service calendar disagree. "\n'
            '                "I cannot confirm whether this period is bookable or available. Please check with the studio.\\n"\n'
            '                f"Source: {BOOKING_SOURCE_URL}"\n'
            '            )\n'
            '        return (\n'
            '            f"วันที่ {snapshot.date} ช่วง {when} น. (เวลาไทย) ข้อมูลจาก Booking Dashboard ขัดกับปฏิทินบริการที่บันทึกไว้ "\n'
            '            "จึงยังยืนยันไม่ได้ว่าช่วงนี้จองได้หรือมีเครื่องว่าง กรุณาตรวจสอบกับศูนย์ครับ\\n"\n'
            '            f"แหล่งข้อมูล: {BOOKING_SOURCE_URL}"\n'
            '        )\n\n'
            '    window = requested_time_window(query, snapshot)\n    resource_groups = _resource_groups_for_query(snapshot, query)\n',
            path,
        )
    elif path == "app/runtime/fast_answer.py":
        source = replace_once(
            source,
            '    is_live_booking_question,\n    render_live_booking_answer,\n',
            '    is_live_booking_question,\n    live_booking_calendar_conflict,\n    render_live_booking_answer,\n',
            path,
        )
        source = replace_once(
            source,
            '    mode = "live_booking_status_fast_path" if snapshot.ok else "live_booking_status_unavailable"\n    confidence = 0.99 if snapshot.ok else 0.94\n',
            '    conflict = live_booking_calendar_conflict(query, snapshot)\n'
            '    mode = (\n'
            '        "live_booking_calendar_conflict" if conflict\n'
            '        else "live_booking_status_fast_path" if snapshot.ok\n'
            '        else "live_booking_status_unavailable"\n'
            '    )\n'
            '    confidence = 0.99 if snapshot.ok and not conflict else 0.94\n',
            path,
        )
        source = replace_once(
            source,
            '"หมายเหตุ: วันปิดพิเศษ/วันหยุดราชการจะ override ตารางเปิดปิดปกติ",',
            '"หมายเหตุ: วันที่บันทึกว่าศูนย์ปิดในไฟล์ปฏิทินบริการจะมีผลก่อนตารางปกติ",',
            path,
        )
        source = replace_once(
            source,
            '"- วันหยุดราชการ/วันปิดพิเศษในไฟล์ปฏิทินจะมีผลก่อนตารางปกติ",',
            '"- เฉพาะวันที่บันทึกว่าศูนย์ปิดในไฟล์ปฏิทินบริการจะมีผลก่อนตารางปกติ; วันหยุดไทยอย่างเดียวไม่ได้ทำให้ปิดอัตโนมัติ",',
            path,
        )
    elif path == "app/pipeline/bilingual_english.py":
        source = replace_once(
            source,
            '    is_live_booking_question,\n    render_live_booking_answer,\n',
            '    is_live_booking_question,\n    live_booking_calendar_conflict,\n    render_live_booking_answer,\n',
            path,
        )
        source = replace_once(
            source,
            'from app.calendar.service_calendar import closure_for, holidays_for_date, regular_service_slots, today_bangkok\n',
            'from app.calendar.service_calendar import closure_for, holidays_for_date, regular_service_slots, resolve_date_from_text, today_bangkok\n',
            path,
        )
        source = replace_once(
            source,
            '    reference_date = _english_date_label(today_bangkok())\n    closure = closure_for(target)\n',
            '    reference_date = _english_date_label(today_bangkok())\n'
            '    date_heading = f"{relative_label}, {display_date}" if relative_label else display_date\n'
            '    closure = closure_for(target)\n',
            path,
        )
        source = replace_once(source, 'f"{relative_label}, {display_date}: the studio is closed', 'f"{date_heading}: the studio is closed', path)
        source = replace_once(source, 'f"{relative_label}, {display_date}: no regular service', 'f"{date_heading}: no regular service', path)
        source = replace_once(source, 'f"{relative_label}, {display_date}: " + "; ".join(slot_lines)', 'f"{date_heading}: " + "; ".join(slot_lines)', path)
        source = replace_once(
            source,
            '"•    A registered public-holiday or special-closure record takes precedence over the regular schedule.",',
            '"•    Only a recorded studio closure overrides the regular schedule; a Thai public holiday alone does not automatically close the studio.",',
            path,
        )
        source = replace_once(
            source,
            '    elif "tomorrow" in tokens:\n        target_date = today_bangkok() + timedelta(days=1)\n        relative_label = "Tomorrow"\n\n    if target_date is not None:\n',
            '    elif "tomorrow" in tokens:\n        target_date = today_bangkok() + timedelta(days=1)\n        relative_label = "Tomorrow"\n    else:\n        resolved = resolve_date_from_text(query, today=today_bangkok())\n        if resolved is not None:\n            target_date = resolved.target_date\n\n    if target_date is not None:\n',
            path,
        )
        source = replace_once(
            source,
            '    snapshot = get_live_booking_status(resolve_live_target_date(query))\n    route = PipelineRoute(\n        "schedule",\n        "live_booking_status",\n        0.99 if snapshot.ok else 0.94,\n        "fact" if snapshot.ok else "no_answer",\n',
            '    snapshot = get_live_booking_status(resolve_live_target_date(query))\n'
            '    conflict = live_booking_calendar_conflict(query, snapshot)\n'
            '    confirmed = snapshot.ok and not conflict\n'
            '    route = PipelineRoute(\n'
            '        "schedule",\n'
            '        "live_booking_status",\n'
            '        0.99 if confirmed else 0.94,\n'
            '        "fact" if confirmed else "no_answer",\n',
            path,
        )
        source = replace_once(
            source,
            '        mode="pipeline:live_booking_status_en" if snapshot.ok else "pipeline:live_booking_status_unavailable_en",\n',
            '        mode=(\n'
            '            "pipeline:live_booking_calendar_conflict_en" if conflict\n'
            '            else "pipeline:live_booking_status_en" if snapshot.ok\n'
            '            else "pipeline:live_booking_status_unavailable_en"\n'
            '        ),\n',
            path,
        )
        source = replace_once(
            source,
            '        answer_type="fact" if snapshot.ok else "no_answer",\n',
            '        answer_type="fact" if confirmed else "no_answer",\n',
            path,
        )
    else:
        raise RuntimeError(f"unexpected path: {path}")
    return source


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    paths = [
        "app/calendar/service_calendar.py",
        "app/booking/live_status.py",
        "app/runtime/fast_answer.py",
        "app/pipeline/bilingual_english.py",
    ]
    changed: dict[str, tuple[bytes, bytes]] = {}
    for path in paths:
        original = (REPO / path).read_bytes()
        text = original.decode("utf-8")
        updated = transform(path, text).encode("utf-8")
        compile(updated.decode("utf-8"), path, "exec")
        changed[path] = (original, updated)
    test_path = "tests/test_p0_calendar_booking_reconciliation_20260925.py"
    test_bytes = (WORK / "test_p0_calendar_booking_reconciliation_20260925.py").read_bytes()
    compile(test_bytes.decode("utf-8"), test_path, "exec")
    if (REPO / test_path).exists():
        raise RuntimeError(f"new test path already exists: {test_path}")
    changed[test_path] = (b"", test_bytes)
    diff_parts: list[str] = []
    for path, (before, after) in changed.items():
        old_lines = before.decode("utf-8").splitlines(keepends=True)
        new_lines = after.decode("utf-8").splitlines(keepends=True)
        diff_parts.extend(difflib.unified_diff(old_lines, new_lines, fromfile=f"a/{path}", tofile=f"b/{path}"))
    DIFF.write_text("".join(diff_parts), encoding="utf-8")
    if not args.apply:
        MANIFEST.write_text(json.dumps({path: {"sha256_before": sha(before), "sha256_after": sha(after)} for path, (before, after) in changed.items()}, indent=2), encoding="utf-8")
        print(f"Prepared {len(changed)} files; diff: {DIFF}")
        return
    expected = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for path, (before, after) in changed.items():
        if sha(before) != expected[path]["sha256_before"] or sha(after) != expected[path]["sha256_after"]:
            raise RuntimeError(f"source changed since preview: {path}")
    for path, (_, after) in changed.items():
        target = REPO / path
        temporary = target.with_name(target.name + ".p0tmp")
        if temporary.exists():
            raise RuntimeError(f"temporary path already exists: {temporary}")
        temporary.write_bytes(after)
        os.replace(temporary, target)
        print(f"Updated {target}")


if __name__ == "__main__":
    main()
