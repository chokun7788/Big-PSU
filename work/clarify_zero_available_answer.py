from pathlib import Path


project = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")


def replace_once(relative: str, old: str, new: str) -> None:
    path = project / relative
    content = path.read_text(encoding="utf-8")
    if content.count(old) != 1:
        raise RuntimeError(f"Expected one match in {path}; got {content.count(old)}")
    path.write_text(content.replace(old, new), encoding="utf-8")


replace_once(
    "app/booking/live_status.py",
    '''        if english:
            return f"{label}: {available}/{len(resources)} resources are available for the full period {window.label}."
        return f"{label}: ว่างตลอดช่วง {window.label} น. {available}/{len(resources)} รายการ"
''',
    '''        if english:
            return f"{label}: {available}/{len(resources)} resources are available for the full period {window.label}."
        if available == 0:
            return f"{label}: ไม่ว่างตลอดช่วง {window.label} น. (ว่าง 0/{len(resources)} รายการ)"
        return f"{label}: ว่างตลอดช่วง {window.label} น. {available}/{len(resources)} รายการ"
''',
)
replace_once(
    "app/booking/live_status.py",
    '''    if english:
        return f"{label}: {available}/{len(rows)} resources are available right now ({window.start}, Asia/Bangkok)."
    return f"{label}: ว่าง {available}/{len(rows)} รายการ ณ {window.start} น. (เวลาไทย)"
''',
    '''    if english:
        return f"{label}: {available}/{len(rows)} resources are available right now ({window.start}, Asia/Bangkok)."
    if available == 0:
        return f"{label}: ไม่ว่าง ณ {window.start} น. (ว่าง 0/{len(rows)} รายการ, เวลาไทย)"
    return f"{label}: ว่าง {available}/{len(rows)} รายการ ณ {window.start} น. (เวลาไทย)"
''',
)
replace_once(
    "tests/smoke_test_live_booking_status.py",
    '''        self.assert_targeted_answer(vr_afternoon, "โซน VR: ว่าง 0/1 รายการ ณ 14:30 น. (เวลาไทย)")''',
    '''        self.assert_targeted_answer(vr_afternoon, "โซน VR: ไม่ว่าง ณ 14:30 น. (ว่าง 0/1 รายการ, เวลาไทย)")''',
)
replace_once(
    "tests/test_p0_calendar_booking_reconciliation_20260925.py",
    '''        self.assertIn("0/1", render_live_booking_answer("Is VR free from 09:30 to 10:00?", live, "en"))
''',
    '''        self.assertIn("0/1", render_live_booking_answer("Is VR free from 09:30 to 10:00?", live, "en"))
        thai = render_live_booking_answer("VR 9โมงครึ่งว่างไหม", live, "th")
        self.assertIn("ไม่ว่างตลอดช่วง 09:00-10:00", thai)
        self.assertIn("0/1", thai)
''',
)
print("Clarified Thai zero-available zone answers and regression expectations.")
