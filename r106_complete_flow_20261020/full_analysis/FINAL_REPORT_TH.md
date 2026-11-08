# Full Test Flow กลาง R106 — LLM ON

Coverage ครบ: 20,554/20,554 request keys; 55,811/55,811 grades

ทดสอบเฉพาะ common candidate ไม่รัน legacy ระบบจริงไม่ได้ถูกติดตั้งทับ

## ผลแยกภาษา

| ภาษา | Requests | Strict | Positive literal content checks | Model transport |
|---|---:|---:|---:|---:|
| th | 7844 | 2084/25100 (8.3%) | 9344/13126 (71.19%) | 1467/1472 |
| en | 10235 | 2469/27319 (9.04%) | 6377/9465 (67.37%) | 2180/2189 |
| auto | 2475 | 466/3392 (13.74%) | 1517/2300 (65.96%) | 645/646 |

## ความผิดพลาดและข้อจำกัด

```json
{
  "th": {
    "protocol": 22534,
    "outcome": 3914,
    "evidence": 1513,
    "content": 3832,
    "validation": 36,
    "performance": 52,
    "grader": 0
  },
  "en": {
    "protocol": 24475,
    "outcome": 3605,
    "evidence": 1464,
    "content": 3152,
    "validation": 12,
    "performance": 20,
    "grader": 0
  },
  "auto": {
    "protocol": 2680,
    "outcome": 0,
    "evidence": 0,
    "content": 783,
    "validation": 1,
    "performance": 28,
    "grader": 0
  }
}
```

Request exceptions: 18

Full failed grades, question, full answer, validation, need status, query plan และ transport แยกราย request ใน ALL_FAILURES.jsonl.gz; raw results เก็บ artifact ฉบับเต็ม ไม่ตัดคำตอบเพื่อเปลี่ยนผลตรวจ

เทียบ retained R95 keys เดียวกัน 20,554: strict ดีขึ้น 27 grades; ถอยลง 38 grades

R95 กับ R106 ใช้ข้อมูล migration ต่างรุ่นด้วย จึงไม่ใช่การแยก causal effect ของ Flow อย่างเดียว

## วิธีตีความ

- protocol แยก route/intent ของ format เดิมออกจาก content checks
- keyword/phrase mismatch ต้องอ่านคู่คำตอบและแหล่งข้อมูลก่อนสรุป actual content failure
- validity/source missing ต่างจาก hallucination; unknown ต้องคง unknown
- request exception และ HTTP transport แยกจากคำตอบผิด
- provider ถูกควบคุม unavailable ใน workload นี้; ผล live จริงดู integrated real_live
- การครบ 55,811 grades ไม่ใช่ 55,811 independent questions
- ไม่อ้างแก้ทุกความหมายหรือ production-ready จาก literal grader
