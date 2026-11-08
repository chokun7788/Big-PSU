# ผลทดสอบจริงอัตโนมัติหลังเปิด Full access

- ตัวรันเรียกจากเครื่องมือในแชท ไม่ต้องให้ผู้ใช้ส่งคำถามทีละข้อ
- ตรวจว่าเปิด LLM: False
- โมเดลสร้างข้อความจริงสำเร็จ: False
- ข้อความที่ได้ผล: 0/14
- ผ่านเกณฑ์คำตอบ: 0/0
- DB ไม่เปลี่ยน: True
- โค้ด R81 ไม่เปลี่ยนระหว่างรอบ: True

## ผลการเรียกโมเดลแยกจากเนื้อหา

```json
{
  "actual_calls_attempted": 0,
  "calls_with_valid_schema": 0,
  "failures": []
}
```

คำถามบางข้อใช้ข้อมูลตรงหรือถามยืนยัน จึงไม่เรียก LLM ตาม Flow ปกติ การสร้าง READY สำเร็จพิสูจน์ว่าโมเดลสร้างข้อความได้ แต่ไม่พิสูจน์ว่า selector เลือกแหล่งข้อมูลถูก การคืน JSON ถูกเป็นอีกเกณฑ์แยกจากความหมายและคำตอบ

## เวลา HTTP หลัง warm-up

| ภาษา | จำนวนข้อความ | มัธยฐาน (วินาที) | ต่ำสุด | สูงสุด |
|---|---:|---:|---:|---:|
| th | 0 | None | None | None |
| en | 0 | None | None | None |

เป็นตัวอย่างชุดเล็กหลัง warm-up ไม่ใช่เวลาปกติทุกคำถามหรือ benchmark ความจุระบบ ไม่ได้รัน full corpus

## ผลรายข้อความ

## อุปสรรคที่พบ

{
  "type": "StopCheck",
  "message": "start_r78 exceeded its wait limit; inspect saved launcher logs before restarting again."
}

## หลักฐาน

- RESULTS.json: ผลรวม ข้อผิดพลาด และ hash ของ DB
- CHAT_TURNS.jsonl: คำถาม คำตอบ และ audit จริงทั้งหมด
- *_real_model_generation.json: response และ timing จาก Ollama
- *_chat_health_*.json และ launcher logs: source fingerprint, LLM ON และการเปิด/ปิด R78
- REVIEW.json: สรุปแบบอ่านด้วยเครื่อง ไม่มีการแก้ log เดิม
