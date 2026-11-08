# ผลทดสอบเพิ่ม 20 ชุดหลากหลาย ก่อนแก้ระบบ

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

วันที่อ้างอิง 2026-10-12 เวลาไทย รอบนี้เพิ่มข้อมูลและทดสอบก่อนแก้ตามคำขอ ไม่เปลี่ยนโค้ด production

## 1. ข้อมูลที่เพิ่ม

20 สถานการณ์ × 24 หมวด = 480 รายการใหม่ สำเนาฐานเดิม 240 รายการมาเก็บในฐาน DEMO ใหม่ รวม active 720 รายการ ฐานเดิมและ log เดิมยังอยู่

ชุดใหม่เป็นเกมและสถานที่สมมุติทั้งหมด เพื่อกำหนด Ground Truth ได้แน่นอน ไม่เพิ่มข้อเท็จจริงจากเกมหรือศูนย์จริงโดยไม่มีหลักฐาน คำแปลเป็น agent_translated

ความต่างที่ตั้งใจทดสอบ: 5 แพลตฟอร์ม, จำนวนขั้นต่ำ/สูงสุด, เล่น 20–240 นาที, เวลาเล่นกับ occupancy ต่างกัน, ราคา 0 และราคาปกติ, 4 หน่วยคิดราคา, 4 คำตัดสินกฎ, ขั้นตอน 2/3 ขั้น, วัน closed/modified_hours/open_override, มี/ไม่มีช่วง maintenance, game offered true/false, เครื่อง in_service/out_of_service/retired, known-empty/known-zero/known-false/unknown/not_applicable

ช่องใหม่ 3,100 ช่อง: known 3048, unknown 32, not_applicable 20 กรอกผ่าน schema/source/reference/save/approve/publish จริงใน DEMO ไม่ใช้เจ้าของจริงอนุมัติ

## 2. ผลรวม แยกการเก็บข้อมูลจากการตอบ

| ชั้นที่ทดสอบ | ผ่าน | ผิด | ขอบเขต |
|---|---:|---:|---|
| นำเข้ารายการใหม่ | 480 | 0 | ตรวจชนิดข้อมูล source และ reference |
| คำถามหลักทั้งหมด | 2653 | 2403 | 5056 เคส รวม control เดิม 96 |
| เฉพาะคำถามข้อมูลใหม่ | 2584 | 2376 | 4960 เคส |
| HTTP API | 116 | 108 | 224 เคส; HTTP 200 224 ไม่ใช่จำนวนตอบถูก |
| ทางเข้าของ AnswerQualityPipeline | 116 | 108 | 224 เคส; skipped legacy 8 |
| บทสนทนา 3 รอบ | 360 | 120 | 160 บทสนทนา / 480 turns ใช้คำตอบก่อนหน้าจริง |
| โมเดลช่วยเลือกหัวข้อ | 5 | 43 | 48 เคสที่เน้นหมวดมีปัญหา ใช้ Ollama จริง |

ตารางมีการทวนคำถามบางส่วนซ้ำกัน ห้ามบวกรวมเป็นจำนวนเคสไม่ซ้ำ หรือใช้อัตรานี้แทนความแม่นยำของลูกค้าจริง ชุดก่อนมีคำถามตามชื่อช่องจำนวนมาก ส่วนชุดนี้เน้นสำนวนและหลายหัวข้อ จึงไม่ใช่คะแนนก่อน/หลังแก้ที่เทียบกันตรง ๆ

**ข้อจำกัดของคะแนนผ่าน:** 2,653 หมายถึงผ่านเกณฑ์เนื้อหาที่ต้องมี/status/evidence ไม่ใช่ยืนยันว่าเข้าใจเจตนาทั้งหมด ตรวจเพิ่มพบ 26 เคสพิมพ์ซ้ำที่ requested_fields ว่างและ all_fields=false แต่มีคำตอบที่ต้องการจากการตอบหลายช่องตามค่าเริ่มต้น จึงผ่าน content test ทั้งที่หัวข้อยังไม่ได้ถูกเลือก ดู SCORING_REVIEW.json เก็บคะแนนเดิมไว้และแยกผล audit นี้ ไม่เปลี่ยนเกณฑ์ย้อนหลังโดยไม่แจ้ง

## 3. ผลตามรูปแบบคำถาม

| รูปแบบ | ผ่าน | ผิด | รวม |
|---|---:|---:|---:|
| all_fields | 960 | 0 | 960 |
| natural | 420 | 540 | 960 |
| paraphrase | 380 | 580 | 960 |
| followup | 440 | 520 | 960 |
| multi_field | 320 | 640 | 960 |
| name_repeat | 64 | 96 | 160 |
| old_control_all_fields | 48 | 0 | 48 |
| old_control_natural | 21 | 27 | 48 |

## 4. ทุกหมวด

ผลด้านล่างรวม control เดิมในหมวดละ 4 เคส

| หมวด | ใหม่ | ผ่าน | ผิด |
|---|---:|---:|---:|
| ข้อมูลศูนย์ (`center`) | 20 | 143 | 61 |
| โซนบริการ (`zone`) | 20 | 62 | 142 |
| รุ่นและสเปกอุปกรณ์ (`equipment_model`) | 20 | 123 | 81 |
| เครื่องหรือทรัพยากรจริง (`resource`) | 20 | 42 | 202 |
| รายการที่เลือกในระบบจอง (`service`) | 20 | 68 | 176 |
| ข้อมูลเกม (`game`) | 20 | 202 | 42 |
| กลุ่มผู้ใช้ (`audience`) | 20 | 42 | 202 |
| ติดต่อ (`contact`) | 20 | 164 | 40 |
| ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`) | 20 | 184 | 20 |
| นโยบายและกฎศูนย์ (`policy`) | 20 | 204 | 0 |
| สิ่งอำนวยความสะดวก (`facility`) | 20 | 42 | 162 |
| เกมที่ศูนย์มีให้เล่นจริง (`game_service`) | 20 | 83 | 121 |
| รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`) | 20 | 42 | 162 |
| วิธีเล่นและปุ่ม (`control_set`) | 20 | 184 | 20 |
| ราคาต่อบริการ (`rate`) | 20 | 204 | 0 |
| ราคาเหมาโซน/ห้อง (`rental_package`) | 20 | 204 | 0 |
| ตารางบริการ (`schedule`) | 20 | 83 | 121 |
| วันปิด/ข้อยกเว้น (`closure`) | 20 | 42 | 162 |
| รายการแข่งขันและฉบับกติกา (`competition`) | 20 | 103 | 101 |
| ข้อกติกาการแข่งขัน (`competition_rule`) | 20 | 102 | 102 |
| ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`) | 20 | 82 | 122 |
| บุคลากร/ทีมที่เปิดเผยได้ (`person`) | 20 | 83 | 121 |
| คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`) | 20 | 103 | 101 |
| การเชื่อมสถานะสด (`live_binding`) | 20 | 62 | 142 |

## 5. พลาดตรงขั้นตอนไหน

จัดเป็นกลุ่มไม่ซ้ำตาม plan ก่อน แล้วค่อยอ่าน reasons ที่หนึ่งเคสมีได้หลายป้าย

```json
{
  "record_found_but_no_fields": 1509,
  "record_found_but_requested_fields_incomplete_or_wrong": 763,
  "no_common_answer_or_exception": 131
}
```

สาเหตุที่ตรวจได้จากโค้ดเดิม:

1. field_requests ใช้ keyword กลาง: กี่คน→players_min โดยไม่ remap ตาม kind ทำให้ resource/service/zone หรือคำถาม max เลือกผิด
2. สำนวนใหม่หลายแบบไม่ได้เชื่อมกับชื่อช่อง เช่นหลักฐาน ที่นั่ง เวลาเล่น จึงเลือก record ได้แต่ requested_fields ว่าง
3. คำในชื่อหมวด/รายการเข้าไปรบกวน intent เช่นปุ่ม กฎ ราคา มีผลแม้ผู้ใช้ถามอีกหัวข้อ
4. multi-field เลือกบางหัวข้อได้แต่ไม่ครอบคลุมทุกสิ่งที่ถาม; ต่อให้คำตอบมี source ก็ยังขาดหัวข้อที่ขอ
5. ประวัติช่วยเลือก record ได้ แต่ไม่ได้รับประกันว่ารู้ field ของคำถามต่อ; บทสนทนาจริงที่เก็บ assistant history แยกตรวจไว้
6. fuzzy มีข้อจำกัด แต่ต้องเทียบ clean/typo เป็นคู่ ไม่ถือว่าทุกเคส typo ที่ตกเกิดจากสะกดผิด
7. planner เรียกเมื่อไม่มีหัวข้อหรือบางเงื่อนไข steps เท่านั้น จึงไม่ช่วยกรณี keyword เลือก field ผิดที่มีอยู่แล้ว
8. confidence/validation ใน CommonAnswerer.finish ปัจจุบันกำหนดค่า 1.0/True คงที่ จึงไม่ใช่โอกาสที่คำตอบถูกตามคำถาม สามารถเลือกหัวข้อผิดแล้วมีค่าพวกนี้ได้

## 6. พิมพ์ซ้ำกับคำปกติ เปรียบเทียบเป็นคู่

```json
{
  "clean_fail/repeat_fail": 94,
  "clean_fail/repeat_pass": 26,
  "clean_pass/repeat_pass": 38,
  "clean_pass/repeat_fail": 2
}
```

`clean_fail/repeat_fail` ยังไม่พิสูจน์ว่าการพิมพ์ผิดเป็นต้นเหตุ ต้องอ่านสอง plan; `clean_pass/repeat_fail` จึงเป็นการเสื่อมหลังพิมพ์ซ้ำที่ชัดกว่า

### เคสพิมพ์ซ้ำที่ดูเหมือนดีขึ้นแต่ยังมีปัญหา

26 เคส clean_fail/repeat_pass ล้วนยังมี requested_fields=[] และ all_fields=false เช่น `Demo sessionn Northstar How many minutes does one session last?` ได้คำตอบรวม name/resource/platform/session_minutes/occupancy_minutes ค่า 60 นาทีมีอยู่จึงผ่านเกณฑ์เนื้อหา แต่ไม่ได้พิสูจน์ว่าระบบเลือก session_minutes จากความหมายคำถาม

โค้ดเดิมยกเว้นการถามกลับเมื่อ method=bounded_fuzzy จึงปล่อยให้ตอบตามชุดช่องเริ่มต้นเมื่อยังไม่รู้หัวข้อ ต้องแก้ให้ทั้งคำปกติและ typo เลือกหัวข้อด้วยเกณฑ์เดียวกัน โดยไม่ใช้การตอบหลายช่องกลบความไม่เข้าใจ

## 7. บทสนทนา 3 รอบ

160 บทสนทนา: ขอทั้งหมด → ถามสั้นโดยไม่บอกชื่อ → เปลี่ยนชื่อรายการและขอทั้งหมด ใส่ข้อความคำตอบของ assistant จริงลง history ทุกครั้ง ตรวจว่า record เดิมไม่รั่วเข้าสู่ turn เปลี่ยนรายการ

```json
{
  "first": {
    "pass": 160,
    "fail": 0
  },
  "switch_record": {
    "pass": 160,
    "fail": 0
  },
  "followup": {
    "pass": 40,
    "fail": 120
  }
}
```

## 8. LLM: แยกเรียกได้ / plan ผ่าน / ตอบผ่าน

48 คำถามเดียวกันปิด LLM ผ่าน 3/48 เปิด LLM ผ่าน 5/48; planner attempts 27, accepted plans 2. เป็น CommonAnswerer+planner จริง ไม่ได้เปิด legacy/RAG มาสร้างคำตอบให้เรื่องสมมุติ

ตรวจ raw จากการเรียกครั้งเดียวกันนี้ ไม่ใช้การเรียกใหม่มาอ้างแทนผลเก่า:

```json
{
  "valid_shape_and_scope": 2,
  "unsupported_platform": 25
}
```

accepted plan ไม่เท่ากับตอบถูกเสมอ; accepted count กับ pass count แยกอยู่ใน LLM_SUMMARY โดยเคสที่ keyword ตอบอยู่แล้วอาจไม่เรียก LLM

## 9. ผลเดิมหลังเพิ่มข้อมูล

Control 96 เคส: 24 หมวด × 2 ภาษา × (all-fields/natural) ของรายการเดิม 01 เทียบสถานะผ่านและ query_plan กับ log ชุดเดิม ผลเปลี่ยน 0 เคส รายละเอียดใน OLD_CONTROL_CHANGES.json

## 10. ตัวอย่างที่ยังผิดและควรตอบอะไร

เป็นค่าของ fixture เท่านั้น ทุกตัวอย่างเลือกจาก log ที่รันจริง ไม่แต่งคำตอบของระบบเพิ่ม

### center / เคส 00002

ถาม: ศูนย์ทดลอง ดาวเหนือ อยู่ตรงไหน

ตอบจริง: ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

เหตุที่ตก: response_clarification, missing_field:address

Plan:
```json
{
  "record_ids": [
    "demo20_center_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

สิ่งที่ควรนำมาตอบ:
```json
{
  "address": {
    "evidence_refs": [
      {
        "locator": "/values/address",
        "source_id": "fixture20_demo20_center_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional address 7, Example Road, Test District",
      "th": "เลขที่สมมุติ 7 ถนนตัวอย่าง แขวงทดลอง"
    }
  }
}
```

### zone / เคส 00202

ถาม: โซนทดลอง ดาวเหนือ มีที่นั่งกี่ที่

ตอบจริง: ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

เหตุที่ตก: response_clarification, missing_field:room_seats

Plan:
```json
{
  "record_ids": [
    "demo20_zone_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

สิ่งที่ควรนำมาตอบ:
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture20_demo20_zone_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 7
  }
}
```

### equipment_model / เคส 00402

ถาม: รุ่นอุปกรณ์ ดาวเหนือ สเปกมีอะไรบ้าง

ตอบจริง: ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

เหตุที่ตก: response_clarification, missing_field:specifications

Plan:
```json
{
  "record_ids": [
    "demo20_equipment_model_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

สิ่งที่ควรนำมาตอบ:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "27"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

### resource / เคส 00602

ถาม: เครื่องทดลอง ดาวเหนือ เล่นพร้อมกันได้กี่คน

ตอบจริง: players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้

เหตุที่ตก: missing_field:capacity_persons

Plan:
```json
{
  "record_ids": [
    "demo20_resource_01"
  ],
  "requested_fields": [
    "players_min"
  ],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

สิ่งที่ควรนำมาตอบ:
```json
{
  "capacity_persons": {
    "evidence_refs": [
      {
        "locator": "/values/capacity_persons",
        "source_id": "fixture20_demo20_resource_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 4
  }
}
```

### service / เคส 00842

ถาม: รอบทดลอง ดาวเหนือ หนึ่งรอบเล่นได้กี่นาที

ตอบจริง: ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

เหตุที่ตก: response_clarification, missing_field:session_minutes

Plan:
```json
{
  "record_ids": [
    "demo20_service_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

สิ่งที่ควรนำมาตอบ:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 60
  }
}
```

### game / เคส 01083

ถาม: เกมสมมุติ ดาวเหนือ เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ

ตอบจริง: ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

เหตุที่ตก: response_clarification, missing_field:how_to_play

Plan:
```json
{
  "record_ids": [
    "demo20_game_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

สิ่งที่ควรนำมาตอบ:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Plant together and split seed collecting tasks; follow the demonstration controls",
      "th": "ปลูกต้นไม้ร่วมกันและแบ่งหน้าที่เก็บเมล็ด; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

### audience / เคส 01322

ถาม: กลุ่มผู้ใช้ ดาวเหนือ ต้องใช้หลักฐานอะไร

ตอบจริง: ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

เหตุที่ตก: response_clarification, missing_field:required_proofs

Plan:
```json
{
  "record_ids": [
    "demo20_audience_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

สิ่งที่ควรนำมาตอบ:
```json
{
  "required_proofs": {
    "evidence_refs": [
      {
        "locator": "/values/required_proofs",
        "source_id": "fixture20_demo20_audience_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "DEMO pass Northstar"
    ]
  }
}
```

### contact / เคส 01565

ถาม: ช่องทางช่วยเหลือ ดาวเหนือ ติดต่อที่ไหนและติดต่อได้ช่วงไหน

ตอบจริง: **demo20_contact_01**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: fiction01@example.invalid [S1]

address: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้

เหตุที่ตก: missing_field:office_hours

Plan:
```json
{
  "record_ids": [
    "demo20_contact_01"
  ],
  "requested_fields": [
    "address",
    "value"
  ],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

สิ่งที่ควรนำมาตอบ:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "fiction01@example.invalid"
  },
  "office_hours": {
    "evidence_refs": [
      {
        "locator": "/values/office_hours",
        "source_id": "fixture20_demo20_contact_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Demo hours 09:00–18:00",
      "th": "ช่วงทดลอง 09:00–18:00"
    }
  }
}
```

### procedure / เคส 01765

ถาม: ขั้นตอนทดลอง ดาวเหนือ มีขั้นตอนอะไรและต้องใช้เอกสารอะไร

ตอบจริง: **demo20_procedure_01**
• ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production: 1. เลือกบริการสมมุติ ดาวเหนือ
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — demo20_contact_01 [S1]

เหตุที่ตก: missing_field:required_documents

Plan:
```json
{
  "record_ids": [
    "demo20_procedure_01"
  ],
  "requested_fields": [
    "steps"
  ],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

สิ่งที่ควรนำมาตอบ:
```json
{
  "steps": {
    "evidence_refs": [
      {
        "locator": "/values/steps",
        "source_id": "fixture20_demo20_procedure_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "contact_id": null,
        "instruction": {
          "en": "Select the fictional Northstar service",
          "th": "เลือกบริการสมมุติ ดาวเหนือ"
        },
        "order": 1
      },
      {
        "contact_id": "demo20_contact_01",
        "instruction": {
          "en": "Check names and conditions before confirming",
          "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
        },
        "order": 2
      }
    ]
  },
  "required_documents": {
    "evidence_refs": [
      {
        "locator": "/values/required_documents",
        "source_id": "fixture20_demo20_procedure_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "DEMO pass Northstar"
    ]
  }
}
```

### facility / เคส 02162

ถาม: พื้นที่พัก ดาวเหนือ อยู่ตรงไหนในร้าน

ตอบจริง: ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

เหตุที่ตก: response_clarification, missing_field:location

Plan:
```json
{
  "record_ids": [
    "demo20_facility_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

สิ่งที่ควรนำมาตอบ:
```json
{
  "location": {
    "evidence_refs": [
      {
        "locator": "/values/location",
        "source_id": "fixture20_demo20_facility_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Spectator corner in demo room 101",
      "th": "มุมดูเพื่อน อยู่ห้องทดสอบ 101"
    }
  }
}
```

### game_service / เคส 02362

ถาม: การติดตั้งทดลอง ดาวเหนือ มีให้เล่นหรือยัง

ตอบจริง: ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

เหตุที่ตก: response_clarification, missing_field:offered

Plan:
```json
{
  "record_ids": [
    "demo20_game_service_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

สิ่งที่ควรนำมาตอบ:
```json
{
  "offered": {
    "evidence_refs": [
      {
        "locator": "/values/offered",
        "source_id": "fixture20_demo20_game_service_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": true
  }
}
```

### game_mode / เคส 02562

ถาม: โหมดทดลอง ดาวเหนือ เล่นพร้อมกันได้สูงสุดกี่คน

ตอบจริง: **โหมดทดลอง ดาวเหนือ**
• จำนวนผู้เล่นขั้นต่ำของโหมด: 1 [S1]

เหตุที่ตก: missing_field:players_max

Plan:
```json
{
  "record_ids": [
    "demo20_game_mode_01"
  ],
  "requested_fields": [
    "players_min"
  ],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

สิ่งที่ควรนำมาตอบ:
```json
{
  "players_max": {
    "evidence_refs": [
      {
        "locator": "/values/players_max",
        "source_id": "fixture20_demo20_game_mode_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 4
  }
}
```

### control_set / เคส 02765

ถาม: ชุดควบคุมทดลอง ดาวเหนือ ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร

ตอบจริง: **demo20_control_set_01**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • ยืนยัน → DEMO_gamepad_1 (press; คำสั่งสมมุติของ สวนเมฆ)
• เคลื่อนที่ → DEMO_gamepad_2 (press; คำสั่งสมมุติของ สวนเมฆ) [S1]

เหตุที่ตก: missing_field:platform

Plan:
```json
{
  "record_ids": [
    "demo20_control_set_01"
  ],
  "requested_fields": [
    "bindings"
  ],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

สิ่งที่ควรนำมาตอบ:
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture20_demo20_control_set_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "Nintendo Switch"
  },
  "bindings": {
    "evidence_refs": [
      {
        "locator": "/values/bindings",
        "source_id": "fixture20_demo20_control_set_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "action": {
          "en": "Confirm",
          "th": "ยืนยัน"
        },
        "buttons": [
          "DEMO_gamepad_1"
        ],
        "context": {
          "en": "Fictional input for Cloud Garden",
          "th": "คำสั่งสมมุติของ สวนเมฆ"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Move",
          "th": "เคลื่อนที่"
        },
        "buttons": [
          "DEMO_gamepad_2"
        ],
        "context": {
          "en": "Fictional input for Cloud Garden",
          "th": "คำสั่งสมมุติของ สวนเมฆ"
        },
        "gesture": "press"
      }
    ]
  }
}
```

### schedule / เคส 03362

ถาม: ตารางทดลอง ดาวเหนือ จองช่วงไหนได้บ้าง

ตอบจริง: ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

เหตุที่ตก: response_clarification, missing_field:bookable_periods

Plan:
```json
{
  "record_ids": [
    "demo20_schedule_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

สิ่งที่ควรนำมาตอบ:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

### closure / เคส 03562

ถาม: ประกาศวันทดลอง ดาวเหนือ วันนั้นปิดไหม

ตอบจริง: ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

เหตุที่ตก: response_clarification, missing_field:state

Plan:
```json
{
  "record_ids": [
    "demo20_closure_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

สิ่งที่ควรนำมาตอบ:
```json
{
  "state": {
    "evidence_refs": [
      {
        "locator": "/values/state",
        "source_id": "fixture20_demo20_closure_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "modified_hours"
  }
}
```

### competition / เคส 03762

ถาม: รายการฝึก ดาวเหนือ ใช้กติกาฉบับไหน

ตอบจริง: ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

เหตุที่ตก: response_clarification, missing_field:rulebook_release

Plan:
```json
{
  "record_ids": [
    "demo20_competition_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

สิ่งที่ควรนำมาตอบ:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_1"
  }
}
```

### competition_rule / เคส 03962

ถาม: ข้อการแข่งขันทดลอง ดาวเหนือ ข้อนี้กำหนดอะไร

ตอบจริง: ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

เหตุที่ตก: response_clarification, missing_field:text

Plan:
```json
{
  "record_ids": [
    "demo20_competition_rule_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

สิ่งที่ควรนำมาตอบ:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 1: for Watching friends, follow decision allowed; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 1: ดูเพื่อนเล่น ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  }
}
```

### news / เคส 04162

ถาม: ข่าวทดลอง ดาวเหนือ ประกาศว่าอะไร

ตอบจริง: ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

เหตุที่ตก: response_clarification, missing_field:body

Plan:
```json
{
  "record_ids": [
    "demo20_news_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

สิ่งที่ควรนำมาตอบ:
```json
{
  "body": {
    "evidence_refs": [
      {
        "locator": "/values/body",
        "source_id": "fixture20_demo20_news_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Synthetic bulletin: Cloud Garden activity for 1–4 people; no actual payment",
      "th": "ข่าวสมมุติ: กิจกรรมสวนเมฆ สำหรับกลุ่ม 1–4 คน; ไม่มีรับเงินจริง"
    }
  }
}
```

### person / เคส 04362

ถาม: ผู้ดูแลสมมุติ ดาวเหนือ รับผิดชอบอะไร

ตอบจริง: ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

เหตุที่ตก: response_clarification, missing_field:role

Plan:
```json
{
  "record_ids": [
    "demo20_person_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

สิ่งที่ควรนำมาตอบ:
```json
{
  "role": {
    "evidence_refs": [
      {
        "locator": "/values/role",
        "source_id": "fixture20_demo20_person_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional host for Watching friends",
      "th": "ผู้ดูแลสมมุติเรื่อง ดูเพื่อนเล่น"
    }
  }
}
```

### faq / เคส 04562

ถาม: คำถามตัวอย่าง ดาวเหนือ คำตอบคืออะไร

ตอบจริง: summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้

เหตุที่ตก: missing_field:answer

Plan:
```json
{
  "record_ids": [
    "demo20_faq_01"
  ],
  "requested_fields": [
    "summary"
  ],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

สิ่งที่ควรนำมาตอบ:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Watching friends: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องดูเพื่อนเล่น: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

### live_binding / เคส 04762

ถาม: ตัวเชื่อมทดลอง ดาวเหนือ จับคู่สถานะยังไง

ตอบจริง: ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

เหตุที่ตก: response_clarification, missing_field:status_mapping

Plan:
```json
{
  "record_ids": [
    "demo20_live_binding_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

สิ่งที่ควรนำมาตอบ:
```json
{
  "status_mapping": {
    "evidence_refs": [
      {
        "locator": "/values/status_mapping",
        "source_id": "fixture20_demo20_live_binding_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "normalized": "free",
        "raw": "DEMO_EMPTY_1"
      },
      {
        "normalized": "occupied",
        "raw": "DEMO_BUSY_1"
      },
      {
        "normalized": "unknown",
        "raw": "DEMO_UNKNOWN_1"
      }
    ]
  }
}
```

## 11. ข้อจำกัดและผลรอบที่เก็บแยก

- รูปแบบราคา/จำนวนคน/กฎนี้เป็น synthetic ไม่ใช่นโยบายจริง และไม่ใช่การตรวจสถานะ WordPress
- scoring ตรวจ obligation/status/เนื้อหาที่ต้องมี/evidence ไม่ได้ให้มนุษย์ตัดสินความลื่นไหล ความยาว และการแปลทุกคำ
- HTTP ไม่เปิดเผย hits จึงตรวจ obligation/content/unknown wording; pipeline และ CommonAnswerer ตรวจ evidence เพิ่ม
- HTTP รอบแรกตั้ง handler ให้ตรวจ Host ด้วยพอร์ต 0 ขณะที่ server ได้พอร์ตสุ่ม จึงได้ 403 ทั้ง 224 เป็นบั๊กตัวรันทดสอบ แก้เฉพาะ harness แล้วเก็บรอบ 2 ใหม่ ไม่ใช้รอบแรกเป็นข้อสรุปว่า chatbot เชื่อมต่อไม่ได้
- รันหลักรอบแรกเก็บบางเคสแล้วหยุดเฉพาะ parent/worker ของตัวทดสอบ รันต่อจาก log เดิมใน content_final เก็บทั้งสองรอบ
- snapshot reuse และ cache การค้นชื่อใช้เฉพาะ test process กับคำถามเดิม/ชื่อใน release เดิม ผลยังมาจาก named() จริง ตรวจ epoch ทุกคำตอบ ไม่ใช่ cache คำตอบที่รู้จาก oracle และไม่ใช่ benchmark latency ของเว็บ
- ไม่รัน full GT 20,000 เคส ไม่แก้ routing/threshold/alias/นโยบายจริงในรอบนี้

## 12. ลำดับแก้หลังตรวจเพิ่ม

1. เลือก semantic field ตาม kind และความหมาย min/max/seat/session/occupancy/proof ให้ตรง
2. แยกชื่อรายการออกจากคำถามก่อนจับหัวข้อ และรักษาทุกหัวข้อเมื่อถามหลายเรื่อง
3. ใช้ประวัติที่ระบุ record ชัดแล้วช่วยเลือก field; ถ้าไม่แน่ใจถามเฉพาะหัวข้อที่ยังขาด
4. LLM schema ต้องจำกัด enum ของ field/platform; เปิดทางช่วยเมื่อ field ที่จับได้ไม่มีใน kind พร้อม log เหตุผล rejection
5. ตรวจ typo ด้วย clean/typo pairs และการเปลี่ยนเรื่อง ห้ามลด threshold จนเลือกอีกเครื่อง/อีกชุด
6. แยก store validity/source confidence ออกจากความถูกต้องของ intent/answer; ไม่ใช้ static 1.0 เป็นคำรับรองตอบตรง

## 13. หลักฐาน

- [MANIFEST.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/MANIFEST.json)
- [SCENARIOS.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SCENARIOS.json)
- [FIELD_DIVERSITY.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/FIELD_DIVERSITY.json)
- [QUESTIONS_EXPECTED.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/QUESTIONS_EXPECTED.json)
- [content_final/SUMMARY.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/content_final/SUMMARY.json)
- [content_final/ANSWERS_AND_DECISIONS.jsonl](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/content_final/ANSWERS_AND_DECISIONS.jsonl)
- [content_final/FAILURES.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/content_final/FAILURES.json)
- [content_final/EVALUATION_SCOPE.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/content_final/EVALUATION_SCOPE.json)
- [ANALYSIS.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/ANALYSIS.json)
- [SCORING_REVIEW.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SCORING_REVIEW.json)
- [OLD_CONTROL_CHANGES.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/OLD_CONTROL_CHANGES.json)
- [TYPO_CLEAN_PAIRS.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/TYPO_CLEAN_PAIRS.json)
- [HTTP_ROUND2_SUMMARY.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/HTTP_ROUND2_SUMMARY.json)
- [HTTP_ROUND2_RESULTS.jsonl](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/HTTP_ROUND2_RESULTS.jsonl)
- [PIPELINE_SUMMARY.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/PIPELINE_SUMMARY.json)
- [PIPELINE_RESULTS.jsonl](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/PIPELINE_RESULTS.jsonl)
- [CONVERSATION_SUMMARY.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/CONVERSATION_SUMMARY.json)
- [CONVERSATION_RESULTS.jsonl](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/CONVERSATION_RESULTS.jsonl)
- [LLM_SUMMARY.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/LLM_SUMMARY.json)
- [LLM_RESULTS.jsonl](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/LLM_RESULTS.jsonl)
- [PRESERVATION_RECEIPT.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/PRESERVATION_RECEIPT.json)

