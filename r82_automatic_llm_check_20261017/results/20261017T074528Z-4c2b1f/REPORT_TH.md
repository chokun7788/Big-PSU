# ผลทดสอบจริงอัตโนมัติหลังเปิด Full access

- ตัวรันเรียกจากเครื่องมือในแชท ไม่ต้องให้ผู้ใช้ส่งคำถามทีละข้อ
- ตรวจว่าเปิด LLM: True
- โมเดลสร้างข้อความจริงสำเร็จ: True
- ข้อความที่ได้ผล: 14/14
- ผ่านเกณฑ์คำตอบ: 14/14
- DB ไม่เปลี่ยน: True
- โค้ด R81 ไม่เปลี่ยนระหว่างรอบ: True

## ผลการเรียกโมเดลแยกจากเนื้อหา

```json
{
  "actual_calls_attempted": 3,
  "calls_with_valid_schema": 1,
  "failures": [
    {
      "case": "th-personal",
      "question": "ผมเอาอุปกรณ์อินพุตส่วนตัวมาใช้ได้ไหม",
      "failure": "timeout"
    },
    {
      "case": "th-reject",
      "question": "ผมเอาอุปกรณ์อินพุตส่วนตัวมาใช้ได้ไหม",
      "failure": "timeout"
    }
  ]
}
```

คำถามบางข้อใช้ข้อมูลตรงหรือถามยืนยัน จึงไม่เรียก LLM ตาม Flow ปกติ การสร้าง READY สำเร็จพิสูจน์ว่าโมเดลสร้างข้อความได้ แต่ไม่พิสูจน์ว่า selector เลือกแหล่งข้อมูลถูก การคืน JSON ถูกเป็นอีกเกณฑ์แยกจากความหมายและคำตอบ

## เวลา HTTP หลัง warm-up

| ภาษา | จำนวนข้อความ | มัธยฐาน (วินาที) | ต่ำสุด | สูงสุด |
|---|---:|---:|---:|---:|
| th | 6 | 1.998 | 0.479 | 9.143 |
| en | 8 | 2.159 | 1.0 | 10.076 |

เป็นตัวอย่างชุดเล็กหลัง warm-up ไม่ใช่เวลาปกติทุกคำถามหรือ benchmark ความจุระบบ ไม่ได้รัน full corpus

## ผลรายข้อความ

### 1. Can I bring my own input peripheral?

- ภาษา: en; HTTP 10.076 วินาที; ผ่าน: True
- วิธีตอบ: profile_topic_clarification; model_call_avoided=True
- selector: attempted=False, transport=None, schema=None, semantic=None
- ข้อผิดพลาด: []; selector_failure=None; reason=declared_profiles_require_topic_selection

Do you mean this topic: Can I use my own keyboard or mouse??
Reply “yes” or “no”.

### 2. Yes, but it is my own keyboard.

- ภาษา: en; HTTP 2.558 วินาที; ผ่าน: True
- วิธีตอบ: qualified_declared_profile; model_call_avoided=None
- selector: attempted=None, transport=None, schema=None, semantic=None
- ข้อผิดพลาด: []; selector_failure=None; reason=None

**Relevant information**
• Confirmed information: Personal keyboards and mice are not allowed for general studio use. [S1]

English translation is machine generated and has not been reviewed by the owner.

### 3. And my mouse?

- ภาษา: en; HTTP 6.903 วินาที; ผ่าน: True
- วิธีตอบ: qualified_declared_profile; model_call_avoided=None
- selector: attempted=None, transport=None, schema=None, semantic=None
- ข้อผิดพลาด: []; selector_failure=None; reason=None

**Relevant information**
• Confirmed information: Personal keyboards and mice are not allowed for general studio use. [S1]

English translation is machine generated and has not been reviewed by the owner.

### 4. ผมเอาอุปกรณ์อินพุตส่วนตัวมาใช้ได้ไหม

- ภาษา: th; HTTP 9.143 วินาที; ผ่าน: True
- วิธีตอบ: profile_topic_clarification; model_call_avoided=None
- selector: attempted=True, transport=False, schema=False, semantic=None
- ข้อผิดพลาด: []; selector_failure=timeout; reason=None

คุณหมายถึงหัวข้อนี้ใช่ไหมครับ: เอาคีย์บอร์ดหรือเมาส์ตัวเองมาใช้ได้ไหม??
ตอบ “ใช่” หรือ “ไม่ใช่” ได้ครับ

### 5. ใช่ แต่เป็นเมาส์ของผม

- ภาษา: th; HTTP 2.519 วินาที; ผ่าน: True
- วิธีตอบ: qualified_declared_profile; model_call_avoided=None
- selector: attempted=None, transport=None, schema=None, semantic=None
- ข้อผิดพลาด: []; selector_failure=None; reason=None

**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ไม่อนุญาตให้นำคีย์บอร์ดหรือเมาส์ส่วนตัวมาใช้ครับ [S1]

### 6. คีย์บอร์ดด้วยได้ไหม

- ภาษา: th; HTTP 1.476 วินาที; ผ่าน: True
- วิธีตอบ: qualified_declared_profile; model_call_avoided=None
- selector: attempted=None, transport=None, schema=None, semantic=None
- ข้อผิดพลาด: []; selector_failure=None; reason=None

**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ไม่อนุญาตให้นำคีย์บอร์ดหรือเมาส์ส่วนตัวมาใช้ครับ [S1]

### 7. I attached incorrect proof of payment. How do I fix it?

- ภาษา: en; HTTP 5.3 วินาที; ผ่าน: True
- วิธีตอบ: profile_topic_clarification; model_call_avoided=None
- selector: attempted=True, transport=True, schema=True, semantic=False
- ข้อผิดพลาด: []; selector_failure=None; reason=unsupported_task_span

Do you mean this topic: Correct an incorrect payment-slip image?
Reply “yes” or “no”.

### 8. yes

- ภาษา: en; HTTP 1.76 วินาที; ผ่าน: True
- วิธีตอบ: user_confirmed_question_profile; model_call_avoided=None
- selector: attempted=None, transport=None, schema=None, semantic=None
- ข้อผิดพลาด: []; selector_failure=None; reason=None

**Correct an incorrect payment-slip image**
• steps: 1. If you uploaded the wrong payment slip image, send the slip to the studio Facebook page: https://www.facebook.com/psuesportsphuket — Studio Facebook page [S1]
• preconditions: Applies to: Correct an incorrect payment-slip image [S2]

English translation is machine generated and has not been reviewed by the owner.

### 9. ผมเอาอุปกรณ์อินพุตส่วนตัวมาใช้ได้ไหม

- ภาษา: th; HTTP 7.729 วินาที; ผ่าน: True
- วิธีตอบ: profile_topic_clarification; model_call_avoided=None
- selector: attempted=True, transport=False, schema=False, semantic=None
- ข้อผิดพลาด: []; selector_failure=timeout; reason=None

คุณหมายถึงหัวข้อนี้ใช่ไหมครับ: เอาคีย์บอร์ดหรือเมาส์ตัวเองมาใช้ได้ไหม??
ตอบ “ใช่” หรือ “ไม่ใช่” ได้ครับ

### 10. ไม่ใช่ครับ หมายถึงหลังจองต้องจ่ายภายในกี่นาที

- ภาษา: th; HTTP 1.418 วินาที; ผ่าน: True
- วิธีตอบ: common_procedure_topic; model_call_avoided=None
- selector: attempted=None, transport=None, schema=None, semantic=None
- ข้อผิดพลาด: []; selector_failure=None; reason=None

บริการที่ถาม: หลังจอง — จ่าย

**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: หลังจองต้องชำระเงินทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิก และหากต้องการใช้บริการต้องทำรายการจองใหม่ [S1]

### 11. Can I bring my own input peripheral?

- ภาษา: en; HTTP 1.183 วินาที; ผ่าน: True
- วิธีตอบ: profile_topic_clarification; model_call_avoided=True
- selector: attempted=False, transport=None, schema=None, semantic=None
- ข้อผิดพลาด: []; selector_failure=None; reason=declared_profiles_require_topic_selection

Do you mean this topic: Can I use my own keyboard or mouse??
Reply “yes” or “no”.

### 12. Yes, but it is my wireless keyboard.

- ภาษา: en; HTTP 1.0 วินาที; ผ่าน: True
- วิธีตอบ: qualified_profile_scope_unconfirmed; model_call_avoided=None
- selector: attempted=None, transport=None, schema=None, semantic=None
- ข้อผิดพลาด: []; selector_failure=None; reason=None

The added condition needs a separate check. The information for the previous topic does not confirm an answer under this condition. Please contact the studio staff to confirm.

### 13. วันนี้เปิดไหม

- ภาษา: th; HTTP 0.479 วินาที; ผ่าน: True
- วิธีตอบ: common_calendar_open_status; model_call_avoided=None
- selector: attempted=None, transport=None, schema=None, semantic=None
- ข้อผิดพลาด: []; selector_failure=None; reason=None

วันนี้วันที่ 17 ตุลาคม 2569 ไม่เปิดให้บริการครับ

### 14. Is the studio open today?

- ภาษา: en; HTTP 1.009 วินาที; ผ่าน: True
- วิธีตอบ: common_calendar_open_status; model_call_avoided=None
- selector: attempted=None, transport=None, schema=None, semantic=None
- ข้อผิดพลาด: []; selector_failure=None; reason=None

Today, 17 October 2026, the studio is closed.

## หลักฐาน

- RESULTS.json: ผลรวม ข้อผิดพลาด และ hash ของ DB
- CHAT_TURNS.jsonl: คำถาม คำตอบ และ audit จริงทั้งหมด
- *_real_model_generation.json: response และ timing จาก Ollama
- *_chat_health_*.json และ launcher logs: source fingerprint, LLM ON และการเปิด/ปิด R78
- REVIEW.json: สรุปแบบอ่านด้วยเครื่อง ไม่มีการแก้ log เดิม
