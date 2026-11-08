# ข้อไม่ผ่าน strict ทุกข้อ

ผลอัตโนมัติยังไม่ใช่ semantic adjudication

## C11-Q003 — expected_state_mismatch

ช่วยตอบสั้น ๆ ว่า ถ้าไปวันอังคารเลือกช่วงเล่นอะไรได้บ้าง

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
อังคาร — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S1]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 1,
  "mapped_expected_claims": 1,
  "returned_claims": 1,
  "matched_claims": 1,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_1:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q005 — expected_state_mismatch

กำลังวางแผนไปใช้บริการ เลยขอถามว่า วันเสาร์มีรอบไหนให้จอง

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
เสาร์ — ช่วงจองเล่น: ไม่มี / None [S1]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 1,
  "mapped_expected_claims": 1,
  "returned_claims": 1,
  "matched_claims": 1,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_5:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q010 — expected_state_mismatch

ช่วยตอบสั้น ๆ ว่า วันพฤหัสบดีจองเล่นได้กี่โมงถึงกี่โมง

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
พฤหัสบดี — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S1]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 1,
  "mapped_expected_claims": 1,
  "returned_claims": 1,
  "matched_claims": 1,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_3:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q013 — expected_state_mismatch

รบกวนเช็กให้หน่อย วันจันทร์จองเล่นได้กี่โมงถึงกี่โมง

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
จันทร์ — ช่วงจองเล่น: 13:00–16:00 [S1]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 1,
  "mapped_expected_claims": 1,
  "returned_claims": 1,
  "matched_claims": 1,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_0:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q014 — expected_state_mismatch

ถามจากข้อมูลที่ศูนย์ให้ไว้ วันอาทิตย์มีรอบไหนให้จอง

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
อาทิตย์ — ช่วงจองเล่น: ไม่มี / None [S1]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 1,
  "mapped_expected_claims": 1,
  "returned_claims": 1,
  "matched_claims": 1,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_6:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q017 — expected_state_mismatch

ช่วยตอบสั้น ๆ ว่า วันศุกร์มีรอบไหนให้จอง

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
ศุกร์ — ช่วงจองเล่น: 09:00–12:00 [S1]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 1,
  "mapped_expected_claims": 1,
  "returned_claims": 1,
  "matched_claims": 1,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_4:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q021 — expected_state_mismatch

ถามจากข้อมูลที่ศูนย์ให้ไว้ ถ้าไปวันพุธเลือกช่วงเล่นอะไรได้บ้าง

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
พุธ — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S1]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 1,
  "mapped_expected_claims": 1,
  "returned_claims": 1,
  "matched_claims": 1,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_2:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q025 — expected_state_mismatch

อยากรู้ว่า วันอังคารจองเล่นได้กี่โมงถึงกี่โมง

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
อังคาร — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S1]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 1,
  "mapped_expected_claims": 1,
  "returned_claims": 1,
  "matched_claims": 1,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_1:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q027 — expected_state_mismatch

รบกวนเช็กให้หน่อย ถ้าไปวันเสาร์เลือกช่วงเล่นอะไรได้บ้าง

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
เสาร์ — ช่วงจองเล่น: ไม่มี / None [S1]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 1,
  "mapped_expected_claims": 1,
  "returned_claims": 1,
  "matched_claims": 1,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_5:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q032 — expected_state_mismatch

อยากรู้ว่า วันพฤหัสบดีมีรอบไหนให้จอง

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
พฤหัสบดี — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S1]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 1,
  "mapped_expected_claims": 1,
  "returned_claims": 1,
  "matched_claims": 1,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_3:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q035 — expected_state_mismatch

ถามจากข้อมูลที่ศูนย์ให้ไว้ วันจันทร์มีรอบไหนให้จอง

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
จันทร์ — ช่วงจองเล่น: 13:00–16:00 [S1]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 1,
  "mapped_expected_claims": 1,
  "returned_claims": 1,
  "matched_claims": 1,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_0:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q036 — expected_state_mismatch

ถ้าไปวันอาทิตย์เลือกช่วงเล่นอะไรได้บ้าง

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
อาทิตย์ — ช่วงจองเล่น: ไม่มี / None [S1]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 1,
  "mapped_expected_claims": 1,
  "returned_claims": 1,
  "matched_claims": 1,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_6:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q039 — expected_state_mismatch

อยากรู้ว่า ถ้าไปวันศุกร์เลือกช่วงเล่นอะไรได้บ้าง

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
ศุกร์ — ช่วงจองเล่น: 09:00–12:00 [S1]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 1,
  "mapped_expected_claims": 1,
  "returned_claims": 1,
  "matched_claims": 1,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_4:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q043 — expected_state_mismatch

วันพุธจองเล่นได้กี่โมงถึงกี่โมง

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
พุธ — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S1]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 1,
  "mapped_expected_claims": 1,
  "returned_claims": 1,
  "matched_claims": 1,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_2:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q047 — expected_state_mismatch

กำลังวางแผนไปใช้บริการ เลยขอถามว่า วันอังคารมีรอบไหนให้จอง

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
อังคาร — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S1]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 1,
  "mapped_expected_claims": 1,
  "returned_claims": 1,
  "matched_claims": 1,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_1:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q049 — expected_state_mismatch

ถามจากข้อมูลที่ศูนย์ให้ไว้ วันเสาร์จองเล่นได้กี่โมงถึงกี่โมง

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
เสาร์ — ช่วงจองเล่น: ไม่มี / None [S1]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 1,
  "mapped_expected_claims": 1,
  "returned_claims": 1,
  "matched_claims": 1,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_5:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q054 — expected_state_mismatch

I would like to know: What are the bookable hours on Thursday?

```text
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Thursday — bookable periods: 09:00–12:00; 13:00–16:00 [S1]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 1,
  "mapped_expected_claims": 1,
  "returned_claims": 1,
  "matched_claims": 1,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_3:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q057 — expected_state_mismatch

Could you help me with this: When can I reserve a play session on Monday?

```text
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Monday — bookable periods: 13:00–16:00 [S1]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 1,
  "mapped_expected_claims": 1,
  "returned_claims": 1,
  "matched_claims": 1,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_0:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q058 — expected_state_mismatch

Please answer briefly: What are the bookable hours on Sunday?

```text
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Sunday — bookable periods: ไม่มี / None [S1]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 1,
  "mapped_expected_claims": 1,
  "returned_claims": 1,
  "matched_claims": 1,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_6:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q061 — expected_state_mismatch

When can I reserve a play session on Friday? and also Which hours are reserved for maintenance on Friday?

```text
1. when can i reserve a play session on friday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Friday — bookable periods: 09:00–12:00 [S1]

2. which hours are reserved for maintenance on friday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Friday — maintenance periods: 13:00–16:00 [S2]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 2,
  "returned_claims": 2,
  "matched_claims": 2,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_4:bookable_periods",
    "C11:migrated_schedule_4:maintenance_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q065 — expected_state_mismatch

Based on the studio sources, When can I reserve a play session on Wednesday? and also Which hours are reserved for maintenance on Wednesday?

```text
1. based on the studio sources, when can i reserve a play session on wednesday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Wednesday — bookable periods: 09:00–12:00; 13:00–16:00 [S1]

2. which hours are reserved for maintenance on wednesday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Wednesday — maintenance periods: ไม่มี / None [S2]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 2,
  "returned_claims": 2,
  "matched_claims": 2,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_2:bookable_periods",
    "C11:migrated_schedule_2:maintenance_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q066 — expected_state_mismatch

Which hours are reserved for maintenance on Sunday? and also When can I reserve a play session on Sunday?

```text
1. which hours are reserved for maintenance on sunday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Sunday — maintenance periods: ไม่มี / None [S1]

2. when can i reserve a play session on sunday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Sunday — bookable periods: ไม่มี / None [S2]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 2,
  "returned_claims": 2,
  "matched_claims": 2,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_6:maintenance_periods",
    "C11:migrated_schedule_6:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q067 — expected_state_mismatch

Could you help me with this: When is maintenance on Tuesday? and also What are the bookable hours on Tuesday?

```text
1. when is maintenance on tuesday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Tuesday — maintenance periods: ไม่มี / None [S1]

2. what are the bookable hours on tuesday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Tuesday — bookable periods: 09:00–12:00; 13:00–16:00 [S2]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 2,
  "returned_claims": 2,
  "matched_claims": 2,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_1:maintenance_periods",
    "C11:migrated_schedule_1:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q069 — expected_state_mismatch

I would like to know: When can I reserve a play session on Tuesday? and also Which hours are reserved for maintenance on Tuesday?

```text
1. when can i reserve a play session on tuesday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Tuesday — bookable periods: 09:00–12:00; 13:00–16:00 [S1]

2. which hours are reserved for maintenance on tuesday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Tuesday — maintenance periods: ไม่มี / None [S2]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 2,
  "returned_claims": 2,
  "matched_claims": 2,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_1:bookable_periods",
    "C11:migrated_schedule_1:maintenance_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q070 — expected_state_mismatch

Based on the studio sources, Which hours are reserved for maintenance on Thursday? and also When can I reserve a play session on Thursday?

```text
1. based on the studio sources, which hours are reserved for maintenance on thursday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Thursday — maintenance periods: ไม่มี / None [S1]

2. when can i reserve a play session on thursday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Thursday — bookable periods: 09:00–12:00; 13:00–16:00 [S2]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 2,
  "returned_claims": 2,
  "matched_claims": 2,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_3:maintenance_periods",
    "C11:migrated_schedule_3:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q071 — expected_state_mismatch

วันเสาร์มีรอบไหนให้จอง แล้วขอช่วงบำรุงรักษาของวันเสาร์คือเวลาใด

```text
1. วันเสาร์มีรอบไหนให้จอง
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
เสาร์ — ช่วงจองเล่น: ไม่มี / None [S1]

2. ช่วงบำรุงรักษาของวันเสาร์คือเวลาใด
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
เสาร์ — ช่วงบำรุงรักษา: ไม่มี / None [S2]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 2,
  "returned_claims": 2,
  "matched_claims": 2,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_5:bookable_periods",
    "C11:migrated_schedule_5:maintenance_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q072 — expected_state_mismatch

ขอสอบถามหน่อยครับ ช่วงบำรุงรักษาของวันพุธคือเวลาใด แล้วขอวันพุธจองเล่นได้กี่โมงถึงกี่โมง

```text
1. ช่วงบำรุงรักษาของวันพุธคือเวลาใด
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
พุธ — ช่วงบำรุงรักษา: ไม่มี / None [S1]

2. วันพุธจองเล่นได้กี่โมงถึงกี่โมง
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
พุธ — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S2]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 2,
  "returned_claims": 2,
  "matched_claims": 2,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_2:maintenance_periods",
    "C11:migrated_schedule_2:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q076 — expected_state_mismatch

รบกวนเช็กให้หน่อย วันพฤหัสบดีจองเล่นได้กี่โมงถึงกี่โมง แล้วขอวันพฤหัสบดีงดเล่นเพื่อ maintenance กี่โมง

```text
1. รบกวนเช็กให้หน่อย วันพฤหัสบดีจองเล่นได้กี่โมงถึงกี่โมง
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
พฤหัสบดี — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S1]

2. วันพฤหัสบดีงดเล่นเพื่อ maintenance กี่โมง
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
พฤหัสบดี — ช่วงบำรุงรักษา: ไม่มี / None [S2]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 2,
  "returned_claims": 2,
  "matched_claims": 2,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_3:bookable_periods",
    "C11:migrated_schedule_3:maintenance_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q077 — expected_state_mismatch

ถามจากข้อมูลที่ศูนย์ให้ไว้ วันศุกร์งดเล่นเพื่อ maintenance กี่โมง แล้วขอถ้าไปวันศุกร์เลือกช่วงเล่นอะไรได้บ้าง

```text
1. ถามจากข้อมูลที่ศูนย์ให้ไว้ วันศุกร์งดเล่นเพื่อ maintenance กี่โมง
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
ศุกร์ — ช่วงบำรุงรักษา: 13:00–16:00 [S1]

2. ถ้าไปวันศุกร์เลือกช่วงเล่นอะไรได้บ้าง
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
ศุกร์ — ช่วงจองเล่น: 09:00–12:00 [S2]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 2,
  "returned_claims": 2,
  "matched_claims": 2,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_4:maintenance_periods",
    "C11:migrated_schedule_4:bookable_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q079 — expected_state_mismatch

ขอสอบถามหน่อยครับ วันจันทร์จองเล่นได้กี่โมงถึงกี่โมง แล้วขอวันจันทร์งดเล่นเพื่อ maintenance กี่โมง

```text
1. วันจันทร์จองเล่นได้กี่โมงถึงกี่โมง
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
จันทร์ — ช่วงจองเล่น: 13:00–16:00 [S1]

2. วันจันทร์งดเล่นเพื่อ maintenance กี่โมง
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
จันทร์ — ช่วงบำรุงรักษา: 09:00–12:00 [S2]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 2,
  "returned_claims": 2,
  "matched_claims": 2,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_0:bookable_periods",
    "C11:migrated_schedule_0:maintenance_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C11-Q080 — expected_state_mismatch

ช่วยตอบสั้น ๆ ว่า วันอาทิตย์มีรอบไหนให้จอง แล้วขอช่วงบำรุงรักษาของวันอาทิตย์คือเวลาใด

```text
1. ช่วยตอบสั้น ๆ ว่า วันอาทิตย์มีรอบไหนให้จอง
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
อาทิตย์ — ช่วงจองเล่น: ไม่มี / None [S1]

2. ช่วงบำรุงรักษาของวันอาทิตย์คือเวลาใด
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
อาทิตย์ — ช่วงบำรุงรักษา: ไม่มี / None [S2]
```

```json
{
  "passed": false,
  "content_exact": true,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 2,
  "returned_claims": 2,
  "matched_claims": 2,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C11:migrated_schedule_6:bookable_periods",
    "C11:migrated_schedule_6:maintenance_periods"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "expected_state_mismatch",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q001 — fixture_not_in_native_source

Cockpit #01 / 2026-10-21 10:00 ว่างอยู่ไหม

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_01_1:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q002 — fixture_not_in_native_source

ขอสอบถามหน่อยครับ ช่วยเช็กว่าจอง PC #05 / 2026-10-21 12:00 ได้หรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_05_3:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q003 — fixture_not_in_native_source

ช่วยตอบสั้น ๆ ว่า อยากรู้ว่า PC #01 / 2026-10-21 10:00 ถูกจองหรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_01_1:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q004 — fixture_not_in_native_source

อยากรู้ว่า PC #03 / 2026-10-21 09:00 ว่างอยู่ไหม

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_03_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_pc_03_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q005 — fixture_not_in_native_source

กำลังวางแผนไปใช้บริการ เลยขอถามว่า ช่วยเช็กว่าจอง PC #09 / 2026-10-21 09:00 ได้หรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_09_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_pc_09_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q006 — fixture_not_in_native_source

รบกวนเช็กให้หน่อย อยากรู้ว่า PlayStation 5 #02 / 2026-10-21 11:00 ถูกจองหรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_02_2:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q007 — fixture_not_in_native_source

ถามจากข้อมูลที่ศูนย์ให้ไว้ PC #07 / 2026-10-21 12:00 ว่างอยู่ไหม

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_07_3:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q008 — fixture_not_in_native_source

ช่วยเช็กว่าจอง PC #10 / 2026-10-21 12:00 ได้หรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_10_3:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q009 — fixture_not_in_native_source

ขอสอบถามหน่อยครับ อยากรู้ว่า PlayStation 5 #01 / 2026-10-21 09:00 ถูกจองหรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_01_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_ps5_01_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q010 — fixture_not_in_native_source

ช่วยตอบสั้น ๆ ว่า PC #01 / 2026-10-21 11:00 ว่างอยู่ไหม

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_01_2:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q011 — fixture_not_in_native_source

อยากรู้ว่า ช่วยเช็กว่าจอง PC #06 / 2026-10-21 09:00 ได้หรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_06_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_pc_06_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q012 — fixture_not_in_native_source

กำลังวางแผนไปใช้บริการ เลยขอถามว่า อยากรู้ว่า PlayStation 5 #02 / 2026-10-21 12:00 ถูกจองหรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_02_3:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q013 — fixture_not_in_native_source

รบกวนเช็กให้หน่อย Cockpit #02 / 2026-10-21 10:00 ว่างอยู่ไหม

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_02_1:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q014 — fixture_not_in_native_source

ถามจากข้อมูลที่ศูนย์ให้ไว้ ช่วยเช็กว่าจอง PlayStation 5 #01 / 2026-10-21 12:00 ได้หรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_01_3:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q015 — fixture_not_in_native_source

อยากรู้ว่า PC #08 / 2026-10-21 09:00 ถูกจองหรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_08_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_pc_08_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q016 — fixture_not_in_native_source

ขอสอบถามหน่อยครับ PlayStation 5 #02 / 2026-10-21 09:00 ว่างอยู่ไหม

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_02_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_ps5_02_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q017 — fixture_not_in_native_source

ช่วยตอบสั้น ๆ ว่า ช่วยเช็กว่าจอง PC #08 / 2026-10-21 11:00 ได้หรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_08_2:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q018 — fixture_not_in_native_source

อยากรู้ว่า อยากรู้ว่า PC #09 / 2026-10-21 10:00 ถูกจองหรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_09_1:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q019 — fixture_not_in_native_source

กำลังวางแผนไปใช้บริการ เลยขอถามว่า Cockpit #02 / 2026-10-21 09:00 ว่างอยู่ไหม

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_02_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_cockpit_02_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q020 — fixture_not_in_native_source

รบกวนเช็กให้หน่อย ช่วยเช็กว่าจอง Cockpit #01 / 2026-10-21 09:00 ได้หรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_01_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_cockpit_01_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q021 — fixture_not_in_native_source

ถามจากข้อมูลที่ศูนย์ให้ไว้ อยากรู้ว่า PC #04 / 2026-10-21 11:00 ถูกจองหรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_04_2:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q022 — fixture_not_in_native_source

PlayStation 5 #01 / 2026-10-21 11:00 ว่างอยู่ไหม

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_01_2:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q023 — fixture_not_in_native_source

ขอสอบถามหน่อยครับ ช่วยเช็กว่าจอง PC #04 / 2026-10-21 12:00 ได้หรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_04_3:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q024 — fixture_not_in_native_source

ช่วยตอบสั้น ๆ ว่า อยากรู้ว่า PC #01 / 2026-10-21 12:00 ถูกจองหรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_01_3:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q025 — fixture_not_in_native_source

อยากรู้ว่า PC #01 / 2026-10-21 09:00 ว่างอยู่ไหม

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_01_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_pc_01_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q026 — fixture_not_in_native_source

กำลังวางแผนไปใช้บริการ เลยขอถามว่า ช่วยเช็กว่าจอง PC #03 / 2026-10-21 12:00 ได้หรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_03_3:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q027 — fixture_not_in_native_source

รบกวนเช็กให้หน่อย อยากรู้ว่า PC #02 / 2026-10-21 12:00 ถูกจองหรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_02_3:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q028 — fixture_not_in_native_source

ถามจากข้อมูลที่ศูนย์ให้ไว้ PC #10 / 2026-10-21 09:00 ว่างอยู่ไหม

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_10_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_pc_10_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q029 — fixture_not_in_native_source

ช่วยเช็กว่าจอง PC #05 / 2026-10-21 10:00 ได้หรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_05_1:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q030 — fixture_not_in_native_source

ขอสอบถามหน่อยครับ อยากรู้ว่า PC #02 / 2026-10-21 10:00 ถูกจองหรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_02_1:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q031 — fixture_not_in_native_source

ช่วยตอบสั้น ๆ ว่า PC #09 / 2026-10-21 11:00 ว่างอยู่ไหม

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_09_2:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q032 — fixture_not_in_native_source

อยากรู้ว่า ช่วยเช็กว่าจอง PC #07 / 2026-10-21 09:00 ได้หรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_07_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_pc_07_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q033 — fixture_not_in_native_source

กำลังวางแผนไปใช้บริการ เลยขอถามว่า อยากรู้ว่า PlayStation 5 #02 / 2026-10-21 10:00 ถูกจองหรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_02_1:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q034 — fixture_not_in_native_source

รบกวนเช็กให้หน่อย PC #10 / 2026-10-21 11:00 ว่างอยู่ไหม

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_10_2:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q035 — fixture_not_in_native_source

ถามจากข้อมูลที่ศูนย์ให้ไว้ ช่วยเช็กว่าจอง Cockpit #02 / 2026-10-21 12:00 ได้หรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_02_3:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q036 — fixture_not_in_native_source

อยากรู้ว่า PC #09 / 2026-10-21 12:00 ถูกจองหรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_09_3:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q037 — fixture_not_in_native_source

ขอสอบถามหน่อยครับ PC #10 / 2026-10-21 10:00 ว่างอยู่ไหม

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_10_1:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q038 — fixture_not_in_native_source

ช่วยตอบสั้น ๆ ว่า ช่วยเช็กว่าจอง Cockpit #01 / 2026-10-21 11:00 ได้หรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_01_2:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q039 — fixture_not_in_native_source

อยากรู้ว่า อยากรู้ว่า PC #08 / 2026-10-21 10:00 ถูกจองหรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_08_1:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q040 — fixture_not_in_native_source

กำลังวางแผนไปใช้บริการ เลยขอถามว่า PC #02 / 2026-10-21 11:00 ว่างอยู่ไหม

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_02_2:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q041 — fixture_not_in_native_source

รบกวนเช็กให้หน่อย ช่วยเช็กว่าจอง PC #02 / 2026-10-21 09:00 ได้หรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_02_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_pc_02_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q042 — fixture_not_in_native_source

ถามจากข้อมูลที่ศูนย์ให้ไว้ อยากรู้ว่า Cockpit #01 / 2026-10-21 12:00 ถูกจองหรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_01_3:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q043 — fixture_not_in_native_source

PC #08 / 2026-10-21 12:00 ว่างอยู่ไหม

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_08_3:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q044 — fixture_not_in_native_source

ขอสอบถามหน่อยครับ ช่วยเช็กว่าจอง PC #06 / 2026-10-21 11:00 ได้หรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_06_2:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q045 — fixture_not_in_native_source

ช่วยตอบสั้น ๆ ว่า อยากรู้ว่า PC #04 / 2026-10-21 10:00 ถูกจองหรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_04_1:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q046 — fixture_not_in_native_source

อยากรู้ว่า PC #04 / 2026-10-21 09:00 ว่างอยู่ไหม

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_04_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_pc_04_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q047 — fixture_not_in_native_source

กำลังวางแผนไปใช้บริการ เลยขอถามว่า ช่วยเช็กว่าจอง PC #07 / 2026-10-21 10:00 ได้หรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_07_1:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q048 — fixture_not_in_native_source

รบกวนเช็กให้หน่อย อยากรู้ว่า PC #03 / 2026-10-21 11:00 ถูกจองหรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_03_2:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q049 — fixture_not_in_native_source

ถามจากข้อมูลที่ศูนย์ให้ไว้ PC #05 / 2026-10-21 11:00 ว่างอยู่ไหม

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_05_2:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q050 — fixture_not_in_native_source

ช่วยเช็กว่าจอง PC #05 / 2026-10-21 09:00 ได้หรือยัง

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_05_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_pc_05_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q051 — fixture_not_in_native_source

Is PC #06 / 2026-10-21 12:00 available?

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_06_3:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q052 — fixture_not_in_native_source

Could you help me with this: Can you check whether PC #03 / 2026-10-21 10:00 is already booked?

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_03_1:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q053 — fixture_not_in_native_source

Please answer briefly: Is Cockpit #02 / 2026-10-21 11:00 available?

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_02_2:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q054 — fixture_not_in_native_source

I would like to know: Can you check whether PlayStation 5 #01 / 2026-10-21 10:00 is already booked?

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_01_1:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q055 — fixture_not_in_native_source

Based on the studio sources, Is PC #07 / 2026-10-21 11:00 available?

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_07_2:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q056 — fixture_not_in_native_source

Can you check whether PC #06 / 2026-10-21 10:00 is already booked?

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_06_1:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q057 — fixture_not_in_native_source

Could you help me with this: Is Cockpit #01 / 2026-10-21 10:00 available?

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_01_1:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q058 — fixture_not_in_native_source

Please answer briefly: Can you check whether PC #05 / 2026-10-21 12:00 is already booked?

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "unavailable",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_05_3:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q059 — fixture_not_in_native_source

I would like to know: Is PC #01 / 2026-10-21 10:00 available?

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_01_1:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q060 — fixture_not_in_native_source

Based on the studio sources, Can you check whether PC #03 / 2026-10-21 09:00 is already booked?

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "unavailable",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_03_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_pc_03_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q061 — fixture_not_in_native_source

Is PC #09 / 2026-10-21 09:00 available? and also Can you check whether PC #10 / 2026-10-21 12:00 is already booked?

```text
1. is pc #09 / 2026-10-21 09:00 available
No confirmed live binding is available, so occupancy cannot be checked.

2. can you check whether pc #10 / 2026-10-21 12:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_09_0:live_status",
    "C12:resource_pc_10_3:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_pc_09_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q062 — fixture_not_in_native_source

Could you help me with this: Can you check whether PlayStation 5 #02 / 2026-10-21 11:00 is already booked? and also Is PlayStation 5 #01 / 2026-10-21 09:00 available?

```text
1. can you check whether ps5 #02 / 2026-10-21 11:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.

2. is ps5 #01 / 2026-10-21 09:00 available
No confirmed live binding is available, so occupancy cannot be checked.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_02_2:live_status",
    "C12:resource_ps5_01_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_ps5_01_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q063 — fixture_not_in_native_source

Please answer briefly: Is PC #07 / 2026-10-21 12:00 available? and also Can you check whether PC #01 / 2026-10-21 11:00 is already booked?

```text
1. please answer briefly: is pc #07 / 2026-10-21 12:00 available
No confirmed live binding is available, so occupancy cannot be checked.

2. can you check whether pc #01 / 2026-10-21 11:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "unavailable",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_07_3:live_status",
    "C12:resource_pc_01_2:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q064 — fixture_not_in_native_source

I would like to know: Can you check whether PC #10 / 2026-10-21 12:00 is already booked? and also Is PC #06 / 2026-10-21 09:00 available?

```text
1. can you check whether pc #10 / 2026-10-21 12:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.

2. is pc #06 / 2026-10-21 09:00 available
No confirmed live binding is available, so occupancy cannot be checked.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_10_3:live_status",
    "C12:resource_pc_06_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_pc_06_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q065 — fixture_not_in_native_source

Based on the studio sources, Is PlayStation 5 #01 / 2026-10-21 09:00 available? and also Can you check whether PlayStation 5 #02 / 2026-10-21 12:00 is already booked?

```text
1. based on the studio sources, is ps5 #01 / 2026-10-21 09:00 available
No confirmed live binding is available, so occupancy cannot be checked.

2. can you check whether ps5 #02 / 2026-10-21 12:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_01_0:live_status",
    "C12:resource_ps5_02_3:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_ps5_01_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q066 — fixture_not_in_native_source

Can you check whether PC #01 / 2026-10-21 11:00 is already booked? and also Is Cockpit #02 / 2026-10-21 10:00 available?

```text
1. can you check whether pc #01 / 2026-10-21 11:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.

2. is cockpit #02 / 2026-10-21 10:00 available
No confirmed live binding is available, so occupancy cannot be checked.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_01_2:live_status",
    "C12:resource_cockpit_02_1:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_cockpit_02_1:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q067 — fixture_not_in_native_source

Could you help me with this: Is PC #06 / 2026-10-21 09:00 available? and also Can you check whether PlayStation 5 #01 / 2026-10-21 12:00 is already booked?

```text
1. is pc #06 / 2026-10-21 09:00 available
No confirmed live binding is available, so occupancy cannot be checked.

2. can you check whether ps5 #01 / 2026-10-21 12:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_06_0:live_status",
    "C12:resource_ps5_01_3:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_pc_06_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q068 — fixture_not_in_native_source

Please answer briefly: Can you check whether PlayStation 5 #02 / 2026-10-21 12:00 is already booked? and also Is PC #08 / 2026-10-21 09:00 available?

```text
1. please answer briefly: can you check whether ps5 #02 / 2026-10-21 12:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.

2. is pc #08 / 2026-10-21 09:00 available
No confirmed live binding is available, so occupancy cannot be checked.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_02_3:live_status",
    "C12:resource_pc_08_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_pc_08_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q069 — fixture_not_in_native_source

I would like to know: Is Cockpit #02 / 2026-10-21 10:00 available? and also Can you check whether PlayStation 5 #02 / 2026-10-21 09:00 is already booked?

```text
1. is cockpit #02 / 2026-10-21 10:00 available
No confirmed live binding is available, so occupancy cannot be checked.

2. can you check whether ps5 #02 / 2026-10-21 09:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_02_1:live_status",
    "C12:resource_ps5_02_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_cockpit_02_1:live_status",
    "C12:resource_ps5_02_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q070 — fixture_not_in_native_source

Based on the studio sources, Can you check whether PlayStation 5 #01 / 2026-10-21 12:00 is already booked? and also Is PC #08 / 2026-10-21 11:00 available?

```text
1. based on the studio sources, can you check whether ps5 #01 / 2026-10-21 12:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.

2. is pc #08 / 2026-10-21 11:00 available
No confirmed live binding is available, so occupancy cannot be checked.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "unavailable",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_01_3:live_status",
    "C12:resource_pc_08_2:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q071 — fixture_not_in_native_source

ช่วยเช็กว่าจอง PC #08 / 2026-10-21 09:00 ได้หรือยัง แล้วขออยากรู้ว่า PC #09 / 2026-10-21 10:00 ถูกจองหรือยัง

```text
1. ช่วยเช็กว่าจอง pc #08 / 2026-10-21 09:00 ได้หรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. อยากรู้ว่า pc #09 / 2026-10-21 10:00 ถูกจองหรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_08_0:live_status",
    "C12:resource_pc_09_1:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_pc_08_0:live_status",
    "C12:resource_pc_09_1:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q072 — fixture_not_in_native_source

ขอสอบถามหน่อยครับ อยากรู้ว่า PlayStation 5 #02 / 2026-10-21 09:00 ถูกจองหรือยัง แล้วขอCockpit #02 / 2026-10-21 09:00 ว่างอยู่ไหม

```text
1. อยากรู้ว่า ps5 #02 / 2026-10-21 09:00 ถูกจองหรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. cockpit #02 / 2026-10-21 09:00 ว่างอยู่ไหม
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_02_0:live_status",
    "C12:resource_cockpit_02_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_ps5_02_0:live_status",
    "C12:resource_cockpit_02_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q073 — fixture_not_in_native_source

ช่วยตอบสั้น ๆ ว่า PC #08 / 2026-10-21 11:00 ว่างอยู่ไหม แล้วขอช่วยเช็กว่าจอง Cockpit #01 / 2026-10-21 09:00 ได้หรือยัง

```text
1. ช่วยตอบสั้น ๆ ว่า pc #08 / 2026-10-21 11:00 ว่างอยู่ไหม
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. ช่วยเช็กว่าจอง cockpit #01 / 2026-10-21 09:00 ได้หรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_08_2:live_status",
    "C12:resource_cockpit_01_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_cockpit_01_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q074 — fixture_not_in_native_source

อยากรู้ว่า ช่วยเช็กว่าจอง PC #09 / 2026-10-21 10:00 ได้หรือยัง แล้วขออยากรู้ว่า PC #04 / 2026-10-21 11:00 ถูกจองหรือยัง

```text
1. อยากรู้ว่า ช่วยเช็กว่าจอง pc #09 / 2026-10-21 10:00 ได้หรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. อยากรู้ว่า pc #04 / 2026-10-21 11:00 ถูกจองหรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_09_1:live_status",
    "C12:resource_pc_04_2:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_pc_09_1:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q075 — fixture_not_in_native_source

กำลังวางแผนไปใช้บริการ เลยขอถามว่า อยากรู้ว่า Cockpit #02 / 2026-10-21 09:00 ถูกจองหรือยัง แล้วขอPlayStation 5 #01 / 2026-10-21 11:00 ว่างอยู่ไหม

```text
1. กำลังวางแผนไปใช้บริการ เลยขอถามว่า อยากรู้ว่า cockpit #02 / 2026-10-21 09:00 ถูกจองหรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. playstation 5 #01 / 2026-10-21 11:00 ว่างอยู่ไหม
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_02_0:live_status",
    "C12:resource_ps5_01_2:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_cockpit_02_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q076 — fixture_not_in_native_source

รบกวนเช็กให้หน่อย Cockpit #01 / 2026-10-21 09:00 ว่างอยู่ไหม แล้วขอช่วยเช็กว่าจอง PC #04 / 2026-10-21 12:00 ได้หรือยัง

```text
1. รบกวนเช็กให้หน่อย cockpit #01 / 2026-10-21 09:00 ว่างอยู่ไหม
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. ช่วยเช็กว่าจอง pc #04 / 2026-10-21 12:00 ได้หรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_01_0:live_status",
    "C12:resource_pc_04_3:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_cockpit_01_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q077 — fixture_not_in_native_source

ถามจากข้อมูลที่ศูนย์ให้ไว้ ช่วยเช็กว่าจอง PC #04 / 2026-10-21 11:00 ได้หรือยัง แล้วขออยากรู้ว่า PC #01 / 2026-10-21 12:00 ถูกจองหรือยัง

```text
1. ถามจากข้อมูลที่ศูนย์ให้ไว้ ช่วยเช็กว่าจอง pc #04 / 2026-10-21 11:00 ได้หรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. อยากรู้ว่า pc #01 / 2026-10-21 12:00 ถูกจองหรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "unavailable",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_04_2:live_status",
    "C12:resource_pc_01_3:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q078 — fixture_not_in_native_source

อยากรู้ว่า PlayStation 5 #01 / 2026-10-21 11:00 ถูกจองหรือยัง แล้วขอPC #01 / 2026-10-21 09:00 ว่างอยู่ไหม

```text
1. อยากรู้ว่า ps5 #01 / 2026-10-21 11:00 ถูกจองหรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. pc #01 / 2026-10-21 09:00 ว่างอยู่ไหม
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_01_2:live_status",
    "C12:resource_pc_01_0:live_status"
  ],
  "literal_goal_spans_present": [
    "C12:resource_pc_01_0:live_status"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q079 — fixture_not_in_native_source

ขอสอบถามหน่อยครับ PC #04 / 2026-10-21 12:00 ว่างอยู่ไหม แล้วขอช่วยเช็กว่าจอง PC #03 / 2026-10-21 12:00 ได้หรือยัง

```text
1. pc #04 / 2026-10-21 12:00 ว่างอยู่ไหม
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. ช่วยเช็กว่าจอง pc #03 / 2026-10-21 12:00 ได้หรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "unavailable",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_04_3:live_status",
    "C12:resource_pc_03_3:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C12-Q080 — fixture_not_in_native_source

ช่วยตอบสั้น ๆ ว่า ช่วยเช็กว่าจอง PC #01 / 2026-10-21 12:00 ได้หรือยัง แล้วขออยากรู้ว่า PC #02 / 2026-10-21 12:00 ถูกจองหรือยัง

```text
1. ช่วยตอบสั้น ๆ ว่า ช่วยเช็กว่าจอง pc #01 / 2026-10-21 12:00 ได้หรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. อยากรู้ว่า pc #02 / 2026-10-21 12:00 ถูกจองหรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "unavailable",
  "actual_status": "partial",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_01_3:live_status",
    "C12:resource_pc_02_3:live_status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C13-Q052 — additional_or_wrong_scope_claims

Could you help me with this: Under PSU Phuket VALORANT 2026 Tournament, what does the section ประเภทบทลงโทษในเกม specify?

```text
A confirmed English translation is unavailable for some clauses; their Thai source text is retained below.
PSU Phuket VALORANT 2026 Tournament — Types of penalties in the game: Penalty types in the game [S1]
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม: การตักเตือน (Warning) สำหรับความผิดครั้งแรกที่มีผลกระทบต่ำ [S2]
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม: การย้อนรอบ (Round Rollback) เมื่อการใช้ช่องโหว่ส่งผลต่อรอบนั้นอย่างชัดเจนแต่ระบุเจตนาไม่ได้ [S3]
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม: การปรับแพ้ในรอบ (Round Loss) เมื่อพบว่าผู้เล่นหรือทีมมีเจตนาใช้ช่องโหว่เพื่อสร้างความได้เปรียบ [S4]
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม: การปรับแพ้ในแผนที่ (Map Forfeit) สำหรับความผิดร้ายแรงหรือความผิดซ้ำที่ส่งผลกระทบต่อผลการแข่งในแผนที่นั้น [S5]
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม: การปรับแพ้ในแมตช์ (Match Forfeit) กรณีทุจริต (Cheating) หรือล็อกผล (Match fixing)   [S6]
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม: ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า [S7]
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม: -------------------------------------------------------------------------------------- [S8]
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "answer",
  "actual_status": "answer",
  "expected_claims": 7,
  "mapped_expected_claims": 7,
  "returned_claims": 8,
  "matched_claims": 7,
  "missing": [],
  "extra": [
    "C13:competition_competition_rules_valorant_psu_phuket_2026_section_010:rule_clause"
  ],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C13:valorant_76:rule_clause",
    "C13:valorant_73:rule_clause",
    "C13:valorant_78:rule_clause",
    "C13:valorant_75:rule_clause",
    "C13:valorant_77:rule_clause",
    "C13:valorant_79:rule_clause",
    "C13:valorant_74:rule_clause"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "additional_or_wrong_scope_claims",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C13-Q055 — additional_or_wrong_scope_claims

Based on the studio sources, Under PSU Phuket VALORANT 2026 Tournament, what does the section พื้นที่การแข่งขันและกฎระเบียบ specify?

```text
A confirmed English translation is unavailable for some clauses; their Thai source text is retained below.
PSU Phuket VALORANT 2026 Tournament — Competition Venue and Regulations: Competition area and regulations
* During Match Prep, no more than 6 players are allowed.
* Mobile phones, tablets and smartwatches are prohibited in the competition area until the match ends.
* Players may not bring notes or documents into the area. The team captain may bring them, but must give the documents to the referee before every competition.
* Only drinking water in a sealed container and chewing gum are allowed.
Competition process [S1]
PSU Phuket VALORANT 2026 Tournament — พื้นที่การแข่งขันและกฎระเบียบ: จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน [S2]
PSU Phuket VALORANT 2026 Tournament — พื้นที่การแข่งขันและกฎระเบียบ: อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์ [S3]
PSU Phuket VALORANT 2026 Tournament — พื้นที่การแข่งขันและกฎระเบียบ: เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง [S4]
PSU Phuket VALORANT 2026 Tournament — พื้นที่การแข่งขันและกฎระเบียบ: อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น [S5]
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "answer",
  "actual_status": "answer",
  "expected_claims": 4,
  "mapped_expected_claims": 4,
  "returned_claims": 5,
  "matched_claims": 4,
  "missing": [],
  "extra": [
    "C13:competition_competition_rules_valorant_psu_phuket_2026_section_002:rule_clause"
  ],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C13:valorant_16:rule_clause",
    "C13:valorant_15:rule_clause",
    "C13:valorant_17:rule_clause",
    "C13:valorant_18:rule_clause"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "additional_or_wrong_scope_claims",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C13-Q056 — additional_or_wrong_scope_claims

Under PSU Phuket VALORANT 2026 Tournament, what does the section 1. เวลานอกทางยุทธวิธี (Tactical Timeout) specify?

```text
A confirmed English translation is unavailable for some clauses; their Thai source text is retained below.
PSU Phuket VALORANT 2026 Tournament — 1. Tactical Timeout: 1. Tactical Timeout
* 2 requests per map during regulation (the first 24 rounds), 60 seconds each.
* In Overtime, each team receives 1 additional request. Unused regulation requests do not carry over. [S1]
PSU Phuket VALORANT 2026 Tournament — 1. เวลานอกทางยุทธวิธี (Tactical Timeout): ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที [S2]
PSU Phuket VALORANT 2026 Tournament — 1. เวลานอกทางยุทธวิธี (Tactical Timeout): เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ [S3]
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": true,
  "expected_status": "answer",
  "actual_status": "answer",
  "expected_claims": 2,
  "mapped_expected_claims": 2,
  "returned_claims": 3,
  "matched_claims": 2,
  "missing": [],
  "extra": [
    "C13:competition_competition_rules_valorant_psu_phuket_2026_section_006:rule_clause"
  ],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "literal_goal_spans_present": [
    "C13:valorant_47:rule_clause",
    "C13:valorant_46:rule_clause"
  ],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": false,
  "classification": "additional_or_wrong_scope_claims",
  "fixture_only_goal": false,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q001 — fixture_not_in_native_source

งาน กิจกรรมจำลองทดสอบ 06 ยังสมัครได้ไหม

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_6:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q002 — fixture_not_in_native_source

ขอสอบถามหน่อยครับ กิจกรรมจำลองทดสอบ 12 ปิดรับสมัครหรือยัง

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_12:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q003 — fixture_not_in_native_source

ช่วยตอบสั้น ๆ ว่า อยากไป กิจกรรมจำลองทดสอบ 04 ต้องไปวันไหน

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_4:date"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q004 — fixture_not_in_native_source

อยากรู้ว่า งาน กิจกรรมจำลองทดสอบ 08 ยังสมัครได้ไหม

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_8:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q005 — fixture_not_in_native_source

กำลังวางแผนไปใช้บริการ เลยขอถามว่า วันจัดงาน กิจกรรมจำลองทดสอบ 02 คือวันที่เท่าไร

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_2:date"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q006 — fixture_not_in_native_source

รบกวนเช็กให้หน่อย สถานะการรับสมัคร กิจกรรมจำลองทดสอบ 10 เป็นอย่างไร

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_10:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q007 — fixture_not_in_native_source

ถามจากข้อมูลที่ศูนย์ให้ไว้ งาน กิจกรรมจำลองทดสอบ 01 ยังสมัครได้ไหม

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_1:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q008 — fixture_not_in_native_source

ขอลิงก์สมัครงาน กิจกรรมจำลองทดสอบ 09

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_9:registration"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q009 — fixture_not_in_native_source

ขอสอบถามหน่อยครับ สถานะการรับสมัคร กิจกรรมจำลองทดสอบ 03 เป็นอย่างไร

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_3:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q010 — fixture_not_in_native_source

ช่วยตอบสั้น ๆ ว่า กิจกรรมจำลองทดสอบ 01 จัดวันไหน

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_1:date"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q011 — fixture_not_in_native_source

อยากรู้ว่า วันจัดงาน กิจกรรมจำลองทดสอบ 10 คือวันที่เท่าไร

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_10:date"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q012 — fixture_not_in_native_source

กำลังวางแผนไปใช้บริการ เลยขอถามว่า สถานะการรับสมัคร กิจกรรมจำลองทดสอบ 07 เป็นอย่างไร

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_7:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q013 — fixture_not_in_native_source

รบกวนเช็กให้หน่อย งาน กิจกรรมจำลองทดสอบ 02 ยังสมัครได้ไหม

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_2:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q014 — fixture_not_in_native_source

ถามจากข้อมูลที่ศูนย์ให้ไว้ กิจกรรมจำลองทดสอบ 05 ปิดรับสมัครหรือยัง

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_5:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q015 — fixture_not_in_native_source

อยากไป กิจกรรมจำลองทดสอบ 06 ต้องไปวันไหน

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_6:date"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q016 — fixture_not_in_native_source

ขอสอบถามหน่อยครับ จะสมัคร กิจกรรมจำลองทดสอบ 03 ได้จากลิงก์ไหน

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_3:registration"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q017 — fixture_not_in_native_source

ช่วยตอบสั้น ๆ ว่า ขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 03

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_3:description"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q018 — fixture_not_in_native_source

อยากรู้ว่า มีช่องทางลงทะเบียน กิจกรรมจำลองทดสอบ 01 ไหม

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_1:registration"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q019 — fixture_not_in_native_source

กำลังวางแผนไปใช้บริการ เลยขอถามว่า กิจกรรมจำลองทดสอบ 08 จัดวันไหน

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_8:date"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q020 — fixture_not_in_native_source

รบกวนเช็กให้หน่อย ขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 11

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_11:description"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q021 — fixture_not_in_native_source

ถามจากข้อมูลที่ศูนย์ให้ไว้ สถานะการรับสมัคร กิจกรรมจำลองทดสอบ 09 เป็นอย่างไร

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_9:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q022 — fixture_not_in_native_source

จะสมัคร กิจกรรมจำลองทดสอบ 10 ได้จากลิงก์ไหน

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_10:registration"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q023 — fixture_not_in_native_source

ขอสอบถามหน่อยครับ ขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 08

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_8:description"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q024 — fixture_not_in_native_source

ช่วยตอบสั้น ๆ ว่า อยากไป กิจกรรมจำลองทดสอบ 05 ต้องไปวันไหน

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_5:date"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q025 — fixture_not_in_native_source

อยากรู้ว่า กิจกรรมจำลองทดสอบ 11 จัดวันไหน

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_11:date"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q026 — fixture_not_in_native_source

กำลังวางแผนไปใช้บริการ เลยขอถามว่า ขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 12

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_12:description"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q027 — fixture_not_in_native_source

รบกวนเช็กให้หน่อย มีช่องทางลงทะเบียน กิจกรรมจำลองทดสอบ 12 ไหม

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_12:registration"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q028 — fixture_not_in_native_source

ถามจากข้อมูลที่ศูนย์ให้ไว้ จะสมัคร กิจกรรมจำลองทดสอบ 07 ได้จากลิงก์ไหน

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_7:registration"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q029 — fixture_not_in_native_source

ขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 02

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_2:description"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q030 — fixture_not_in_native_source

ขอสอบถามหน่อยครับ กิจกรรมจำลองทดสอบ 09 จัดเกี่ยวกับอะไร

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_9:description"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q031 — fixture_not_in_native_source

ช่วยตอบสั้น ๆ ว่า จะสมัคร กิจกรรมจำลองทดสอบ 11 ได้จากลิงก์ไหน

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_11:registration"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q032 — fixture_not_in_native_source

อยากรู้ว่า วันจัดงาน กิจกรรมจำลองทดสอบ 07 คือวันที่เท่าไร

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_7:date"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q033 — fixture_not_in_native_source

กำลังวางแผนไปใช้บริการ เลยขอถามว่า อยากไป กิจกรรมจำลองทดสอบ 09 ต้องไปวันไหน

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_9:date"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q034 — fixture_not_in_native_source

รบกวนเช็กให้หน่อย กิจกรรมจำลองทดสอบ 12 จัดวันไหน

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_12:date"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q035 — fixture_not_in_native_source

ถามจากข้อมูลที่ศูนย์ให้ไว้ ขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 05

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_5:description"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q036 — fixture_not_in_native_source

สถานะการรับสมัคร กิจกรรมจำลองทดสอบ 04 เป็นอย่างไรร

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_4:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q037 — fixture_not_in_native_source

ขอสอบถามหน่อยครับ งาน กิจกรรมจำลองทดสอบ 06 คือกิจกรรมอะไร

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_6:description"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q038 — fixture_not_in_native_source

ช่วยตอบสั้น ๆ ว่า ขอลิงก์สมัครงาน กิจกรรมจำลองทดสอบ 08

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_8:registration"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q039 — fixture_not_in_native_source

อยากรู้ว่า กิจกรรมจำลองทดสอบ 04 จัดเกี่ยวกับอะไร

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_4:description"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q040 — fixture_not_in_native_source

กำลังวางแผนไปใช้บริการ เลยขอถามว่า จะสมัคร กิจกรรมจำลองทดสอบ 02 ได้จากลิงก์ไหน

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_2:registration"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q041 — fixture_not_in_native_source

รบกวนเช็กให้หน่อย ขอลิงก์สมัครงาน กิจกรรมจำลองทดสอบ 04

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_4:registration"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q042 — fixture_not_in_native_source

ถามจากข้อมูลที่ศูนย์ให้ไว้ สถานะการรับสมัคร กิจกรรมจำลองทดสอบ 11 เป็นอย่างไร

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_11:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q043 — fixture_not_in_native_source

จะสมัคร กิจกรรมจำลองทดสอบ 06 ได้จากลิงก์ไหน

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_6:registration"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q044 — fixture_not_in_native_source

ขอสอบถามหน่อยครับ ขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 07

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_7:description"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q045 — fixture_not_in_native_source

ช่วยตอบสั้น ๆ ว่า กิจกรรมจำลองทดสอบ 01 จัดเกี่ยวกับอะไร

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_1:description"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q046 — fixture_not_in_native_source

อยากรู้ว่า กิจกรรมจำลองทดสอบ 03 จัดวันไหน

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_3:date"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q047 — fixture_not_in_native_source

กำลังวางแผนไปใช้บริการ เลยขอถามว่า ขอลิงก์สมัครงาน กิจกรรมจำลองทดสอบ 05

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_5:registration"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q048 — fixture_not_in_native_source

รบกวนเช็กให้หน่อย กิจกรรมจำลองทดสอบ 10 จัดเกี่ยวกับอะไร

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_10:description"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q049 — fixture_not_in_native_source

ถามจากข้อมูลที่ศูนย์ให้ไว้ งาน กิจกรรมจำลองทดสอบ 06 ยังสมัครได้ไหม

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_6:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q050 — fixture_not_in_native_source

กิจกรรมจำลองทดสอบ 12 ปิดรับสมัครหรือยัง

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_12:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q051 — fixture_not_in_native_source

When does Synthetic test event 04 take place?

```text
No confirmed source is available for the requested detail.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_4:date"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q052 — fixture_not_in_native_source

Could you help me with this: Has registration closed for Synthetic test event 08?

```text
No confirmed source is available for the requested detail.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_8:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q053 — fixture_not_in_native_source

Please answer briefly: When does Synthetic test event 02 take place?

```text
No confirmed source is available for the requested detail.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_2:date"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q054 — fixture_not_in_native_source

I would like to know: Has registration closed for Synthetic test event 10?

```text
No confirmed source is available for the requested detail.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_10:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q055 — fixture_not_in_native_source

Based on the studio sources, Is registration for Synthetic test event 01 still open?

```text
No confirmed source is available for the requested detail.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_1:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q056 — fixture_not_in_native_source

Give me the registration URL for Synthetic test event 09.

```text
No confirmed source is available for the requested detail.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_9:registration"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q057 — fixture_not_in_native_source

Could you help me with this: Is registration for Synthetic test event 03 still open?

```text
No confirmed source is available for the requested detail.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_3:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q058 — fixture_not_in_native_source

Please answer briefly: What is the date of Synthetic test event 01?

```text
No confirmed source is available for the requested detail.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_1:date"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q059 — fixture_not_in_native_source

I would like to know: When does Synthetic test event 10 take place?

```text
No confirmed source is available for the requested detail.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_10:date"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q060 — fixture_not_in_native_source

Based on the studio sources, Has registration closed for Synthetic test event 07?

```text
No confirmed source is available for the requested detail.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 1,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_7:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q061 — fixture_not_in_native_source

Is registration for Synthetic test event 02 still open? and also What is the date of Synthetic test event 02?

```text
No confirmed source is available for the requested detail.

No confirmed source is available for the requested detail.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_2:status",
    "C14:fixture_event_2:date"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q062 — fixture_not_in_native_source

Could you help me with this: Has registration closed for Synthetic test event 05? and also When does Synthetic test event 05 take place?

```text
No confirmed source is available for the requested detail.

No confirmed source is available for the requested detail.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_5:status",
    "C14:fixture_event_5:date"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q063 — fixture_not_in_native_source

Please answer briefly: When does Synthetic test event 06 take place? and also Has registration closed for Synthetic test event 06?

```text
No confirmed source is available for the requested detail.

No confirmed source is available for the requested detail.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_6:date",
    "C14:fixture_event_6:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q064 — fixture_not_in_native_source

I would like to know: Give me the registration URL for Synthetic test event 03. and also Is registration for Synthetic test event 03 still open?

```text
No confirmed source is available for the requested detail.

No confirmed source is available for the requested detail.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_3:registration",
    "C14:fixture_event_3:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q065 — fixture_not_in_native_source

Based on the studio sources, What is Synthetic test event 03 about? and also Has registration closed for Synthetic test event 03?

```text
No confirmed source is available for the requested detail.

No confirmed source is available for the requested detail.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_3:description",
    "C14:fixture_event_3:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q066 — fixture_not_in_native_source

Give me the registration URL for Synthetic test event 01. and also Is registration for Synthetic test event 01 still open?

```text
No confirmed source is available for the requested detail.

No confirmed source is available for the requested detail.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_1:registration",
    "C14:fixture_event_1:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q067 — fixture_not_in_native_source

Could you help me with this: When does Synthetic test event 08 take place? and also Has registration closed for Synthetic test event 08?

```text
No confirmed source is available for the requested detail.

No confirmed source is available for the requested detail.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_8:date",
    "C14:fixture_event_8:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q068 — fixture_not_in_native_source

Please answer briefly: Describe the event Synthetic test event 11. and also When does Synthetic test event 11 take place?

```text
No confirmed source is available for the requested detail.

No confirmed source is available for the requested detail.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_11:description",
    "C14:fixture_event_11:date"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q069 — fixture_not_in_native_source

I would like to know: Is registration for Synthetic test event 09 still open? and also Give me the registration URL for Synthetic test event 09.

```text
No confirmed source is available for the requested detail.

No confirmed source is available for the requested detail.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_9:status",
    "C14:fixture_event_9:registration"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q070 — fixture_not_in_native_source

Based on the studio sources, Give me the registration URL for Synthetic test event 10. and also Is registration for Synthetic test event 10 still open?

```text
No confirmed source is available for the requested detail.

No confirmed source is available for the requested detail.
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_10:registration",
    "C14:fixture_event_10:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q071 — fixture_not_in_native_source

ขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 08 แล้วขอสถานะการรับสมัคร กิจกรรมจำลองทดสอบ 08 เป็นอย่างไรร

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_8:description",
    "C14:fixture_event_8:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q072 — fixture_not_in_native_source

ขอสอบถามหน่อยครับ อยากไป กิจกรรมจำลองทดสอบ 05 ต้องไปวันไหน แล้วของาน กิจกรรมจำลองทดสอบ 05 ยังสมัครได้ไหม

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_5:date",
    "C14:fixture_event_5:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q073 — fixture_not_in_native_source

ช่วยตอบสั้น ๆ ว่า กิจกรรมจำลองทดสอบ 11 จัดวันไหน แล้วขอขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 11

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_11:date",
    "C14:fixture_event_11:description"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q074 — fixture_not_in_native_source

อยากรู้ว่า ขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 12 แล้วขอสถานะการรับสมัคร กิจกรรมจำลองทดสอบ 12 เป็นอย่างไร

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_12:description",
    "C14:fixture_event_12:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q075 — fixture_not_in_native_source

กำลังวางแผนไปใช้บริการ เลยขอถามว่า มีช่องทางลงทะเบียน กิจกรรมจำลองทดสอบ 12 ไหม แล้วของาน กิจกรรมจำลองทดสอบ 12 ยังสมัครได้ไหม

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_12:registration",
    "C14:fixture_event_12:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q076 — fixture_not_in_native_source

รบกวนเช็กให้หน่อย จะสมัคร กิจกรรมจำลองทดสอบ 07 ได้จากลิงก์ไหน แล้วขอกิจกรรมจำลองทดสอบ 07 ปิดรับสมัครหรือยัง

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_7:registration",
    "C14:fixture_event_7:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q077 — fixture_not_in_native_source

ถามจากข้อมูลที่ศูนย์ให้ไว้ ขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 02 แล้วขออยากไป กิจกรรมจำลองทดสอบ 02 ต้องไปวันไหน

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_2:description",
    "C14:fixture_event_2:date"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q078 — fixture_not_in_native_source

กิจกรรมจำลองทดสอบ 09 จัดเกี่ยวกับอะไร แล้วขอจะสมัคร กิจกรรมจำลองทดสอบ 09 ได้จากลิงก์ไหน

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_9:description",
    "C14:fixture_event_9:registration"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q079 — fixture_not_in_native_source

ขอสอบถามหน่อยครับ จะสมัคร กิจกรรมจำลองทดสอบ 11 ได้จากลิงก์ไหน แล้วขอขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 11

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_11:registration",
    "C14:fixture_event_11:description"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```

## C14-Q080 — fixture_not_in_native_source

ช่วยตอบสั้น ๆ ว่า วันจัดงาน กิจกรรมจำลองทดสอบ 07 คือวันที่เท่าไร แล้วขอสถานะการรับสมัคร กิจกรรมจำลองทดสอบ 07 เป็นอย่างไร

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

```json
{
  "passed": false,
  "content_exact": false,
  "state_ok": false,
  "expected_status": "answer",
  "actual_status": "missing_source",
  "expected_claims": 2,
  "mapped_expected_claims": 0,
  "returned_claims": 0,
  "matched_claims": 0,
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_7:date",
    "C14:fixture_event_7:status"
  ],
  "literal_goal_spans_present": [],
  "validation_ok": true,
  "http_ok": true,
  "safe_abstention": true,
  "classification": "fixture_not_in_native_source",
  "fixture_only_goal": true,
  "metric": "saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy"
}
```
