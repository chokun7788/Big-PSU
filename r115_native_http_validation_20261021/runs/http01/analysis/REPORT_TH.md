# ผลตรวจผ่านแชทจริง — http01

ใช้คำถามเดิมครบ 1,400 ข้อ ข้อความ/locale ตรงกับ manifest ทุกข้อ ไม่ส่ง category hint ไม่เพิ่มคำถาม เปิด LLM และยิงจริงผ่าน /api/chat บน candidate DB ข้อมูลที่ย้ายมาแล้ว

## เกณฑ์และข้อจำกัด

- Strict = concept identity/value/status ตรงกับ expected ที่จับคู่ native ก่อนดูคำตอบ พร้อมการตรวจ source refs ที่ snapshot มีจริง ใช้ projection ร่วมเพื่อจัด identity จึงไม่ใช่ independent human semantic accuracy
- Expected เดิมไม่ถูกแก้ ส่วนราคา 24 fields มี presentation ต่างกันแต่ค่าเงิน/หลักฐานยังตรวจแยก การหาหลักฐานผ่านไม่ยืนยันว่ากฎธุรกิจต้นทางถูกต้องครบ
- 160 ข้อ positive ที่ใช้ fake live/news เดิมไม่มี source เหล่านั้นใน native DB รอบนี้ ไม่ใส่ fake data เข้าไปและไม่เอาการตอบ unavailable มาบวกเป็น answered accuracy
- 39 คำถามราคาเดิมใช้ internal record IDs เป็นข้อจำกัด corpus ต้องแยกจากภาษาใช้งานทั่วไป แต่ยังเก็บและยิงทุกข้อเหมือนเดิม
- ค่าต่อไปนี้ต่างจาก 99.14% รอบ shared-engine เดิม เพราะใช้ native DB/API และการอ้างอิง source จริง การเทียบข้ามรอบต้องอ่านข้อจำกัดเหล่านี้

## รายหมวด

| หมวด | Strict ทั้ง 100 ข้อ | Positive ที่มี source จริงผ่าน | Unknown ตอบอย่างปลอดภัย | Fixture goals |
|---|---:|---:|---:|---:|
| C01 | 100/100 | 80/80 | 20/20 | 0 |
| C02 | 95/100 | 75/80 | 20/20 | 0 |
| C03 | 99/100 | 80/80 | 20/20 | 0 |
| C04 | 100/100 | 80/80 | 20/20 | 0 |
| C05 | 100/100 | 80/80 | 20/20 | 0 |
| C06 | 61/100 | 41/80 | 20/20 | 0 |
| C07 | 100/100 | 80/80 | 20/20 | 0 |
| C08 | 93/100 | 80/80 | 13/20 | 0 |
| C09 | 93/100 | 80/80 | 13/20 | 0 |
| C10 | 94/100 | 80/80 | 14/20 | 0 |
| C11 | 89/100 | 69/80 | 20/20 | 0 |
| C12 | 14/100 | 0/0 | 20/20 | 80 |
| C13 | 97/100 | 77/80 | 20/20 | 0 |
| C14 | 6/100 | 0/0 | 6/20 | 80 |

## รวม

- HTTP ตอบกลับ 1400/1400; delivery validation ผ่าน 1400/1400
- Strict รวม 1141/1400 (รวมข้อ source ไม่ตรงกับ fixture เดิมไว้ใน denominator เพื่อไม่ซ่อน coverage)
- Positive ที่มี source จริง: strict 902/960; source claims ครบ 905/960
- Negative safe abstention 246/280 (แยกจากการตอบคำถามได้)
- Median latency 0.453s; P95 6.406s; elapsed 1632.8s

## Model transport/protocol

```json
{
  "calls": 53,
  "transport_ok": 51,
  "schema_ok": 51,
  "http_attempted": 53,
  "identity_verified": 51
}
```

HTTP transport, model transport, schema และความถูกต้องคำตอบเป็นคนละเกณฑ์ ไม่เอาโมเดลตอบกลับสำเร็จมาแทนการตอบถูก

## กลุ่มที่ไม่ผ่าน

```json
{
  "required_claims_missing": 35,
  "expected_state_mismatch": 41,
  "additional_or_wrong_scope_claims": 23,
  "fixture_not_in_native_source": 160
}
```

รายละเอียดทุกข้ออยู่ใน ALL_FAILURES.jsonl และ FAILURES_DETAIL_TH.md ต้องตรวจ actual body คู่กับ artifact เพื่อแยกผิดเนื้อหา/ขอบเขตออกจากรูปแบบและ source gap
