# รายงานเพิ่มข้อมูลตัวอย่างทุกหมวดและทดลองถาม

**DEMO ONLY — NOT PSU PRODUCTION DATA**

วันที่อ้างอิง: 2026-10-12 เวลาไทย ข้อมูลที่ใช้ตอบเป็นชุดตัวอย่างแยกทั้งหมด ไม่ได้เอาตัวอย่างไปเผยแพร่ในแชทของศูนย์

## 1. สิ่งที่ทำจริง

- ตรวจ catalog ที่ใช้งานจริง: 24 หมวด สร้างหมวดละ 10 รายการ รวม 240 รายการ มีความสัมพันธ์ศูนย์ → โซน → เครื่อง → บริการ → เกม และราคา/กฎ/ขั้นตอน/การแข่งขัน
- 1,550 ช่องข้อมูล: known 1,530 ช่อง, unknown 10 ช่องเรตอายุเกม, not_applicable 10 ช่องรายการแข่งขันก่อนหน้า
- ค้นคำอธิบายเกม 10 เกมจากแหล่งทางการ ข้อมูลร้านและสถานะที่เหลือสมมุติ ไม่สร้างราคาหรือนโยบายจริงเพิ่มเอง
- ผ่าน CommonStore จริง: ตรวจ source/record/reference → บันทึกร่าง → อนุมัติ → เผยแพร่ atomic release ในฐาน DEMO
- เปิดหน้า editor DEMO แยก ใช้ handler/UI ของ r58 พร้อมคำเตือนและ actor ที่ระบุว่าไม่ใช่เจ้าของจริง
- ทดลองแก้เกม ราคา กฎศูนย์ กติกาแข่งอย่างละ 10 รายการในสำเนา DEMO อีกฐาน เก็บ revision เดิมไว้
- เก็บคำถาม คำตอบ สิ่งที่ต้องตอบ เหตุผลการเลือก evidence และเคสผิด ไม่มีการลบ log เดิม

## 2. ผลแยกตามชั้นที่ตรวจ

| ชั้นที่ตรวจ | ผ่าน | ผิด | สิ่งที่พิสูจน์ / ข้อจำกัด |
|---|---:|---:|---|
| นำเข้าและเผยแพร่ | 240 | 0 | รูปแบบและข้อมูลอ้างอิงผ่านในฐาน DEMO |
| CommonAnswerer รวมไทย/อังกฤษ | 4,250 | 770 | 5,020 คำถาม ไม่เรียก LLM/WordPress |
| ขอทุกข้อมูล (subset ข้างบน) | 480 | 0 | ทั้ง 240 รายการ × 2 ภาษา ตอบค่าและ evidence ครบ |
| ถามตามชื่อช่องข้อมูล | 2,970 | 130 | รวม 3,100 เป็น contract test ไม่ใช่ทุกคำถามที่ลูกค้าจะใช้ |
| ถามภาษาทั่วไป | 210 | 270 | 480 เคส: เจตนาหลักหนึ่งแบบต่อหมวด × 10 × 2 ภาษา |
| ถามต่อจากประวัติ | 220 | 260 | 480 เคส ประวัติระบุรายการก่อนแล้วถามหัวข้อต่อ |
| พิมพ์เบิ้ลชื่อรายการ | 370 | 110 | 480 เคส ดัดชื่อด้วยตัวซ้ำหนึ่งตำแหน่ง ไม่ครอบคลุม typo ทุกชนิด |
| HTTP preview ของ editor จริง | 480 | 0 | ทวนคำถามขอทั้งหมดผ่าน API; อ่าน record กลับตรง JSON ครบ 240 |
| AnswerQualityPipeline จริง | 480 | 0 | เข้า entry ของแชทในสภาพแวดล้อม DEMO; all-fields ไม่มี LLM/RAG/WordPress |
| ตัวอย่างภาษาทั่วไปพร้อม LLM | 23 | 25 | 48 เคส 1 รายการต่อหมวดต่อภาษา ใช้ Typhoon2.5-Qwen3-4B จริง |
| แก้ข้อมูลเดิม | 40 | 0 | 4 หมวด × 10: ร่าง/อนุมัติยังไม่เปลี่ยน live, เผยแพร่แล้วเปลี่ยน, v1 คงเดิม |
| หน้ารายการบน browser | 24 หมวด | 0 หมวด | เห็นหมวดละ 10 และลองคำถาม Minecraft/ศูนย์ ไม่ใช่ส่ง 5,020 ผ่าน browser |

แถวบางส่วนใช้คำถามซ้ำกับชุดหลัก **ห้ามบวกทุกแถวเป็นจำนวนเคสไม่ซ้ำ** ตัวอย่างคล้ายกันตามโครงสร้าง 10 รายการ ผลไม่ได้ประมาณความแม่นยำของลูกค้าจริงทั้งหมด

ไทยผ่าน 1,980/2,510 (78.88%) อังกฤษผ่าน 2,270/2,510 (90.44%) รวม 84.66% คำถามขอทั้งหมดผ่าน 100% ในชุดนี้ แต่คำถามทั่วไปผ่าน 43.75% เท่านั้น จึงยังไม่พอจะรับรองว่าใส่ format แล้วตอบได้ทุกสำนวน

## 3. วิธีตัดสินว่าตอบถูก

ตรวจ target record/field ที่กำหนดไว้ล่วงหน้า, ค่า known ที่ควรปรากฏครบ, unknown/not_applicable, และ source/locator ของ evidence ที่ใช้ตอบ ไม่ใช้แค่ HTTP 200 หรือข้อความที่อ่านดูคล้ายถูก ไม่ส่ง expected_fields ให้ LLM เพื่อช่วยตอบ

ค่าข้อมูลอ้างอิงที่ UI แสดงเป็นชื่อรายการต้องตรงกับชื่อใน fixture; ค่าซ้อน เช่นขั้นตอน/contact ต้องตรวจ leaf value ตาม field ที่อ้างอิง รายงานรอบแรกพบ scorer ที่เทียบรหัส contact กับชื่อแสดงผล จึงแก้ scorer แล้วสร้างผลรอบใหม่ เก็บรอบแรกไว้ไม่ปะปนกับผลสรุป

ชุดหลักใช้ snapshot ของ release ที่ผ่าน validation และไม่เปลี่ยนระหว่างรัน พร้อมตรวจ epoch ต่อคำตอบ ใช้ 4 process เพื่อทำงานให้ครบ จึง **ไม่ใช่ benchmark latency/concurrency ของเว็บ** การทดสอบ HTTP และ pipeline แยกต่างหาก ไม่ได้ยืนยันสถานะจองจริง

## 4. ผลทุกหมวด

จำนวนคำถามต่างกันตามจำนวน field ในหมวด ทุกหมวดมีข้อมูล 10 รายการเท่ากัน

| หมวด | ตัวอย่าง | คำถาม | ผ่าน | ผิด | ผ่าน % |
|---|---:|---:|---:|---:|---:|
| ข้อมูลศูนย์ (`center`) | 10 | 240 | 210 | 30 | 87.50 |
| โซนบริการ (`zone`) | 10 | 160 | 90 | 70 | 56.25 |
| รุ่นและสเปกอุปกรณ์ (`equipment_model`) | 10 | 160 | 130 | 30 | 81.25 |
| เครื่องหรือทรัพยากรจริง (`resource`) | 10 | 200 | 120 | 80 | 60.00 |
| รายการที่เลือกในระบบจอง (`service`) | 10 | 240 | 170 | 70 | 70.83 |
| ข้อมูลเกม (`game`) | 10 | 240 | 230 | 10 | 95.83 |
| กลุ่มผู้ใช้ (`audience`) | 10 | 140 | 80 | 60 | 57.14 |
| ติดต่อ (`contact`) | 10 | 160 | 160 | 0 | 100.00 |
| ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`) | 10 | 200 | 200 | 0 | 100.00 |
| นโยบายและกฎศูนย์ (`policy`) | 10 | 240 | 240 | 0 | 100.00 |
| สิ่งอำนวยความสะดวก (`facility`) | 10 | 160 | 120 | 40 | 75.00 |
| เกมที่ศูนย์มีให้เล่นจริง (`game_service`) | 10 | 200 | 180 | 20 | 90.00 |
| รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`) | 10 | 220 | 160 | 60 | 72.73 |
| วิธีเล่นและปุ่ม (`control_set`) | 10 | 220 | 210 | 10 | 95.45 |
| ราคาต่อบริการ (`rate`) | 10 | 280 | 280 | 0 | 100.00 |
| ราคาเหมาโซน/ห้อง (`rental_package`) | 10 | 280 | 280 | 0 | 100.00 |
| ตารางบริการ (`schedule`) | 10 | 220 | 200 | 20 | 90.91 |
| วันปิด/ข้อยกเว้น (`closure`) | 10 | 220 | 170 | 50 | 77.27 |
| รายการแข่งขันและฉบับกติกา (`competition`) | 10 | 220 | 200 | 20 | 90.91 |
| ข้อกติกาการแข่งขัน (`competition_rule`) | 10 | 220 | 180 | 40 | 81.82 |
| ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`) | 10 | 220 | 190 | 30 | 86.36 |
| บุคลากร/ทีมที่เปิดเผยได้ (`person`) | 10 | 180 | 160 | 20 | 88.89 |
| คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`) | 10 | 180 | 140 | 40 | 77.78 |
| การเชื่อมสถานะสด (`live_binding`) | 10 | 220 | 150 | 70 | 68.18 |

## 5. สาเหตุที่มีข้อมูลครบแต่ยังตอบผิด

### 5.1 ชื่อช่องไทยมีคำอังกฤษ แต่การ normalize ไม่ตรงกัน

`field_requests` ทำ NFC/casefold กับคำถาม แต่เทียบ `meaning_th` ใน catalog โดยไม่ casefold ทั้งสองฝั่ง ชื่อช่องมี ISO/API/PC/VR/WordPress/FAQ/TTL จึงหลุดการจับคู่ตรง ขณะที่ EN canonical key มีตัวเล็กอยู่แล้ว

130 เคส contract ที่ผิดเกิดใน 13 กลุ่ม กลุ่มละ 10: closure.local_date; control_set.platform; faq.scope_note; game.age_rating; live_binding.external_resource_key/freshness_policy/status_mapping; resource.name/physical_pool_key; service.booking_product_key/name/occupancy_minutes; zone.name กลุ่มนี้รวมปัญหา keyword และ routing ข้างล่างด้วย ไม่ใช่ทั้ง 130 เคสเกิดจาก casefold อย่างเดียว

### 5.2 จับจำนวนคนเป็น field ผิดหมวด

คำ “กี่คน / players / together” จับเป็น `players_min` แต่ resource ใช้ `capacity_persons`, service ใช้ `capacity_min/capacity_max`, zone ใช้ `capacity`, rental ใช้ `room_seats` และ game_mode ที่ถามได้สูงสุดต้องตอบ `players_max` ระบบค้นเจอรายการถูกแต่ requested_fields ไม่ตรง จึงไม่พิมพ์ข้อมูลที่ควรตอบ

### 5.3 คำในชื่อรายการถูกนับเป็นหัวข้อคำถาม

alias เช่น “วิธีเล่นและปุ่ม” ของ control_set มี keyword จึงดึง how_to_play/bindings/steps แม้ผู้ถามอยากรู้แพลตฟอร์ม ต้องแยกข้อความชื่อรายการออกก่อนตีความส่วนที่ถาม มิฉะนั้นเพิ่ม alias อาจทำให้หัวข้อแทรกเพิ่ม

### 5.4 keyword ข้ามหมวด และไม่แยกคำปฏิเสธ

ชื่อ field เรตอายุมีข้อความ “ไม่ใช่นโยบายรับเด็กของศูนย์” แต่คำ “นโยบาย” กระตุ้น details และทางแยกกฎแข่งขัน จากนั้นเปลี่ยน target จาก game เป็น competition ทำให้ age_rating ของเกมหาย ปัญหาเป็น routing จากคำประกอบ ไม่มีหลักฐานว่า DB ไม่มีเกม

### 5.5 ถามต่อแล้วยังไม่รู้ว่าจะเอา field ไหน

บาง log มี method `history_exact:pending_fields`: ประวัติช่วยระบุ record ได้แล้ว แต่ “ต้องใช้หลักฐานอะไร” ยังไม่ได้ mapped ไป required_proofs จึงถามซ้ำกว้าง ๆ ไม่ได้แปลว่าประวัติสูญหายทั้งหมด ต้องดู record_ids และ requested_fields แยกกัน

### 5.6 พิมพ์เบิ้ลยังพลาดได้หลายสาเหตุ

110 เคสไม่ใช่ทั้งหมดจับชื่อไม่เจอ บางเคสจับ record ถูกแต่หัวข้อยังผิดเหมือนคำปกติ จึงต้องเทียบคู่ clean/typo ก่อนสรุปว่า fuzzy ไม่ดี Threshold และ margin ป้องกันชื่อคล้ายกัน 01–10; ห้ามลด threshold เพื่อให้ตอบเร็วโดยเสี่ยงเลือกอีกเครื่องหรืออีกราคา

### 5.7 เปิด LLM แล้ว schema ยังปฏิเสธ และบางเคสไม่เรียก LLM

48 เคส sample: planner ถูกเรียก 22 ครั้ง ยอมรับ plan 2 ครั้ง ตอบถูก 23/48 บางเคสที่จับ field ได้แล้วแต่ผิดหมวดไม่เข้าประตูเรียก planner จึงเพิ่ม LLM อย่างเดียวไม่แก้ทั้งหมด

health รายงาน 22 successes / 0 failures คือเรียกโมเดลและ decode ได้ ไม่ได้หมายความว่า accepted plan หรือคำตอบถูก 22 ครั้ง `checked_plan` ตรวจ field กับ platform อีกชั้น แต่ schema ที่ส่งโมเดลยอมให้ platform เป็น string ใดก็ได้

ตรวจ raw ใหม่ 6 เคสที่ครั้งแรก plan ถูกปฏิเสธ พบทั้ง 6 ครั้งใส่ platform ผิด: `unknown` หรือ `demo_audience_01`/`demo_closure_01`/`demo_competition_01`/`demo_competition_rule_01` แทน null/ชื่อแพลตฟอร์ม หลายกรณี requested_fields ถูกแล้วแต่ platform ทำให้ทั้ง plan ถูกปฏิเสธ นี่เป็นเหตุผลที่ยืนยันได้จาก raw สำหรับ 6 probe ไม่ใช่หลักฐานว่าอีก 14 เคสแรกผิดด้วยเหตุเดียวกันทั้งหมด เพราะเป็นการเรียกใหม่

เคส 48 เดียวกันเมื่อปิด LLM ผ่าน 21/48 เทียบเปิด LLM ผ่าน 23/48; ไม่ใช่การวัดประสิทธิภาพโมเดลแบบกว้าง และไม่ได้รัน LLM ทั้ง 5,020

### ป้ายกำกับผิดที่พบ

หนึ่งเคสมีได้หลายป้าย จึงห้ามรวมจำนวนป้ายเป็นจำนวนคำถามผิด

| ป้ายจาก log | จำนวนเคส |
|---|---:|
| `response_clarification` | 480 |
| `no_common_answer` | 60 |
| `missing_field:players_max` | 60 |
| `missing_field:required_proofs` | 50 |
| `missing_field:capacity_persons` | 50 |
| `missing_field:room_seats` | 50 |
| `missing_field:state` | 40 |
| `missing_field:text` | 40 |
| `missing_field:location` | 40 |
| `missing_field:status_mapping` | 40 |
| `missing_field:address` | 30 |
| `missing_field:specifications` | 30 |
| `missing_field:answer` | 30 |
| `missing_field:name` | 30 |
| `missing_field:session_minutes` | 30 |
| `missing_field:rulebook_release` | 20 |
| `missing_field:offered` | 20 |
| `missing_field:body` | 20 |
| `missing_field:role` | 20 |
| `missing_field:bookable_periods` | 20 |
| `missing_field:local_date` | 10 |
| `missing_field:platform` | 10 |
| `missing_field:scope_note` | 10 |
| `missing_field:age_rating` | 10 |
| `missing_field:external_resource_key` | 10 |
| `missing_field:freshness_policy` | 10 |
| `missing_field:physical_pool_key` | 10 |
| `missing_field:occupancy_minutes` | 10 |
| `missing_field:booking_product_key` | 10 |

## 6. ตัวอย่างคำตอบผิดพร้อมค่าที่ควรตอบ ทุกหมวดที่ยังผิด

ค่าด้านล่างเป็น fixture ไม่ใช่คำตอบจริงของ PSU ชื่อไทย/อังกฤษใน JSON ให้เลือกตามภาษา; การแสดงผลตามปกติควรแนบ evidence

### center — เคส 00150

**ถาม (th/natural):** ตัวอย่าง ข้อมูลศูนย์ 01 อยู่ตรงไหน

**ตอบจริง:** ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

**ผิดตรง:** response_clarification, missing_field:address

**plan ที่เลือก:**
```json
{
  "record_ids": [
    "demo_center_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

**ข้อมูลที่ควรนำมาตอบ:**
```json
{
  "address": {
    "evidence_refs": [
      {
        "locator": "/values/address",
        "source_id": "fixture_source_demo_center_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": {
      "en": "Example building 01, fictional road, fictional province",
      "th": "อาคารตัวอย่าง 01 ถนนสมมุติ จังหวัดสมมุติ"
    }
  }
}
```

### zone — เคส 04866

**ถาม (th/natural):** ตัวอย่าง โซนบริการ 01 มีที่นั่งกี่ที่

**ตอบจริง:** ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

**ผิดตรง:** response_clarification, missing_field:room_seats

**plan ที่เลือก:**
```json
{
  "record_ids": [
    "demo_zone_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

**ข้อมูลที่ควรนำมาตอบ:**
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture_source_demo_zone_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": 9
  }
}
```

### equipment_model — เคส 01426

**ถาม (th/natural):** ตัวอย่าง รุ่นและสเปกอุปกรณ์ 01 สเปกมีอะไรบ้าง

**ตอบจริง:** ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

**ผิดตรง:** response_clarification, missing_field:specifications

**plan ที่เลือก:**
```json
{
  "record_ids": [
    "demo_equipment_model_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

**ข้อมูลที่ควรนำมาตอบ:**
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture_source_demo_equipment_model_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": [
      {
        "key": "demo_memory",
        "unit": "GB",
        "value": "12"
      },
      {
        "key": "demo_storage",
        "unit": "GB",
        "value": "384"
      }
    ]
  }
}
```

### resource — เคส 04208

**ถาม (th/natural):** ตัวอย่าง เครื่องหรือทรัพยากรจริง 01 เล่นพร้อมกันได้กี่คน

**ตอบจริง:** players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้

**ผิดตรง:** missing_field:capacity_persons

**plan ที่เลือก:**
```json
{
  "record_ids": [
    "demo_resource_01"
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

**ข้อมูลที่ควรนำมาตอบ:**
```json
{
  "capacity_persons": {
    "evidence_refs": [
      {
        "locator": "/values/capacity_persons",
        "source_id": "fixture_source_demo_resource_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": 4
  }
}
```

### service — เคส 04630

**ถาม (th/natural):** ตัวอย่าง รายการที่เลือกในระบบจอง 01 หนึ่งรอบเล่นได้กี่นาที

**ตอบจริง:** ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

**ผิดตรง:** response_clarification, missing_field:session_minutes

**plan ที่เลือก:**
```json
{
  "record_ids": [
    "demo_service_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

**ข้อมูลที่ควรนำมาตอบ:**
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture_source_demo_service_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": 60
  }
}
```

### game — เคส 01929

**ถาม (th/field_contract):** ตัวอย่าง ข้อมูลเกม 01 เรตเกมจากต้นทาง ไม่ใช่นโยบายรับเด็กของศูนย์

**ตอบจริง:** **ตัวอย่าง ข้อกติกาทดสอบ เช็กอิน 01**
• ฉบับรายการที่กฎเป็นของมัน: ตัวอย่าง การแข่งขัน Coral Mario Kart 8 Deluxe 01 [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: identity [S4]
• หัวข้อข้อกติกา: ตัวอย่าง ข้อกติกาทดสอบ เช็กอิน 01 [S5]
• เลขข้อเดิม เช่น 6.1.5: 1 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: กติกาสมมุติหัวข้อ เช็กอิน: แจ้งผู้ดูแลตัวอย่างก่อนเริ่มรอบ 01; ไม่ใช่กฎทางการของเกมหรือ PSU [S7]

details: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้

age_rating: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้

**ผิดตรง:** missing_field:age_rating

**plan ที่เลือก:**
```json
{
  "record_ids": [
    "demo_competition_01"
  ],
  "requested_fields": [
    "details",
    "age_rating"
  ],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

**ข้อมูลที่ควรนำมาตอบ:**
```json
{
  "age_rating": {
    "evidence_refs": [],
    "note": "ยังไม่ได้ค้นเรตอายุ แยกจากกฎผู้ใช้ของร้าน / Age rating not researched",
    "status": "unknown",
    "value": null
  }
}
```

### audience — เคส 00005

**ถาม (th/natural):** ตัวอย่าง กลุ่มผู้ใช้ 01 ต้องใช้หลักฐานอะไร

**ตอบจริง:** ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

**ผิดตรง:** response_clarification, missing_field:required_proofs

**plan ที่เลือก:**
```json
{
  "record_ids": [
    "demo_audience_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

**ข้อมูลที่ควรนำมาตอบ:**
```json
{
  "required_proofs": {
    "evidence_refs": [
      {
        "locator": "/values/required_proofs",
        "source_id": "fixture_source_demo_audience_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": [
      "DEMO group voucher 01"
    ]
  }
}
```

### contact

ชุดนี้ผ่านทั้งหมด ไม่มีเคสผิดให้ยกจากผลรอบนี้ ยังไม่ใช่รับรองทุกคำถามใหม่

### procedure

ชุดนี้ผ่านทั้งหมด ไม่มีเคสผิดให้ยกจากผลรอบนี้ ยังไม่ใช่รับรองทุกคำถามใหม่

### policy

ชุดนี้ผ่านทั้งหมด ไม่มีเคสผิดให้ยกจากผลรอบนี้ ยังไม่ใช่รับรองทุกคำถามใหม่

### facility — เคส 01586

**ถาม (th/natural):** ตัวอย่าง สิ่งอำนวยความสะดวก 01 อยู่ตรงไหนในร้าน

**ตอบจริง:** ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

**ผิดตรง:** response_clarification, missing_field:location

**plan ที่เลือก:**
```json
{
  "record_ids": [
    "demo_facility_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

**ข้อมูลที่ควรนำมาตอบ:**
```json
{
  "location": {
    "evidence_refs": [
      {
        "locator": "/values/location",
        "source_id": "fixture_source_demo_facility_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": {
      "en": "Fictional area F01",
      "th": "พื้นที่จำลอง F01"
    }
  }
}
```

### game_service — เคส 02388

**ถาม (th/natural):** ตัวอย่าง เกมที่ศูนย์มีให้เล่นจริง 01 มีให้เล่นหรือยัง

**ตอบจริง:** ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

**ผิดตรง:** response_clarification, missing_field:offered

**plan ที่เลือก:**
```json
{
  "record_ids": [
    "demo_game_service_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

**ข้อมูลที่ควรนำมาตอบ:**
```json
{
  "offered": {
    "evidence_refs": [
      {
        "locator": "/values/offered",
        "source_id": "fixture_source_demo_game_service_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": true
  }
}
```

### game_mode — เคส 02169

**ถาม (th/natural):** ตัวอย่าง รูปแบบเล่นและเล่นกับเพื่อน 01 เล่นพร้อมกันได้กี่คน

**ตอบจริง:** **ตัวอย่าง รอบฝึกสมมุติ Mario Kart 8 Deluxe 01**
• จำนวนผู้เล่นขั้นต่ำของโหมด: 1 [S1]

**ผิดตรง:** missing_field:players_max

**plan ที่เลือก:**
```json
{
  "record_ids": [
    "demo_game_mode_01"
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

**ข้อมูลที่ควรนำมาตอบ:**
```json
{
  "players_max": {
    "evidence_refs": [
      {
        "locator": "/values/players_max",
        "source_id": "fixture_source_demo_game_mode_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": 4
  }
}
```

### control_set — เคส 01203

**ถาม (th/field_contract):** ตัวอย่าง วิธีเล่นและปุ่ม 01 PC/PS5/Nintendo Switch/VR

**ตอบจริง:** **demo_control_set_01**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • คำสั่งทดสอบ 01 → DEMO_KEY_01 (press; ปุ่มสมมุติสำหรับทดสอบ ไม่ใช่ปุ่มมาตรฐานของเกม) [S1]

how_to_play: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้

steps: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้

**ผิดตรง:** missing_field:platform

**plan ที่เลือก:**
```json
{
  "record_ids": [
    "demo_control_set_01"
  ],
  "requested_fields": [
    "how_to_play",
    "bindings",
    "steps"
  ],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": "PS5"
}
```

**ข้อมูลที่ควรนำมาตอบ:**
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture_source_demo_control_set_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": "Nintendo Switch"
  }
}
```

### rate

ชุดนี้ผ่านทั้งหมด ไม่มีเคสผิดให้ยกจากผลรอบนี้ ยังไม่ใช่รับรองทุกคำถามใหม่

### rental_package

ชุดนี้ผ่านทั้งหมด ไม่มีเคสผิดให้ยกจากผลรอบนี้ ยังไม่ใช่รับรองทุกคำถามใหม่

### schedule — เคส 04409

**ถาม (th/natural):** ตัวอย่าง ตารางบริการ 01 จองช่วงไหนได้บ้าง

**ตอบจริง:** ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

**ผิดตรง:** response_clarification, missing_field:bookable_periods

**plan ที่เลือก:**
```json
{
  "record_ids": [
    "demo_schedule_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

**ข้อมูลที่ควรนำมาตอบ:**
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture_source_demo_schedule_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
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

### closure — เคส 00389

**ถาม (th/natural):** ตัวอย่าง วันปิด/ข้อยกเว้น 01 วันนั้นปิดไหม

**ตอบจริง:** ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

**ผิดตรง:** response_clarification, missing_field:state

**plan ที่เลือก:**
```json
{
  "record_ids": [
    "demo_closure_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

**ข้อมูลที่ควรนำมาตอบ:**
```json
{
  "state": {
    "evidence_refs": [
      {
        "locator": "/values/state",
        "source_id": "fixture_source_demo_closure_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": "closed"
  }
}
```

### competition — เคส 00609

**ถาม (th/natural):** ตัวอย่าง รายการแข่งขันและฉบับกติกา 01 ใช้กติกาฉบับไหน

**ตอบจริง:** ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

**ผิดตรง:** response_clarification, missing_field:rulebook_release

**plan ที่เลือก:**
```json
{
  "record_ids": [
    "demo_competition_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

**ข้อมูลที่ควรนำมาตอบ:**
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture_source_demo_competition_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": "DEMO_RULEBOOK_01"
  }
}
```

### competition_rule — เคส 00829

**ถาม (th/natural):** ตัวอย่าง ข้อกติกาการแข่งขัน 01 ข้อนี้กำหนดอะไร

**ตอบจริง:** ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

**ผิดตรง:** response_clarification, missing_field:text

**plan ที่เลือก:**
```json
{
  "record_ids": [
    "demo_competition_rule_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

**ข้อมูลที่ควรนำมาตอบ:**
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture_source_demo_competition_rule_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": {
      "en": "Fictional rule for Check-in: notify the demo operator before round 01; not an official game or PSU rule",
      "th": "กติกาสมมุติหัวข้อ เช็กอิน: แจ้งผู้ดูแลตัวอย่างก่อนเริ่มรอบ 01; ไม่ใช่กฎทางการของเกมหรือ PSU"
    }
  }
}
```

### news — เคส 02809

**ถาม (th/natural):** ตัวอย่าง ข่าว/กิจกรรม/ประกาศ/โปรโมชัน 01 ประกาศว่าอะไร

**ตอบจริง:** ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

**ผิดตรง:** response_clarification, missing_field:body

**plan ที่เลือก:**
```json
{
  "record_ids": [
    "demo_news_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

**ข้อมูลที่ควรนำมาตอบ:**
```json
{
  "body": {
    "evidence_refs": [
      {
        "locator": "/values/body",
        "source_id": "fixture_source_demo_news_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": {
      "en": "Fictional announcement: practice C01, no actual registration or payment",
      "th": "ประกาศสมมุติ: เปิดรอบฝึก C01 ไม่มีการรับสมัครหรือชำระเงินจริง"
    }
  }
}
```

### person — เคส 03027

**ถาม (th/natural):** ตัวอย่าง บุคลากร/ทีมที่เปิดเผยได้ 01 รับผิดชอบอะไร

**ตอบจริง:** ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

**ผิดตรง:** response_clarification, missing_field:role

**plan ที่เลือก:**
```json
{
  "record_ids": [
    "demo_person_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

**ข้อมูลที่ควรนำมาตอบ:**
```json
{
  "role": {
    "evidence_refs": [
      {
        "locator": "/values/role",
        "source_id": "fixture_source_demo_person_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": {
      "en": "Fictional operator for Check-in",
      "th": "ผู้ดูแลสมมุติเรื่อง เช็กอิน"
    }
  }
}
```

### faq — เคส 01747

**ถาม (th/natural):** ตัวอย่าง คำถามเสริมและเอกสารทั่วไปของศูนย์ 01 คำตอบคืออะไร

**ตอบจริง:** summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้

**ผิดตรง:** missing_field:answer

**plan ที่เลือก:**
```json
{
  "record_ids": [
    "demo_faq_01"
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

**ข้อมูลที่ควรนำมาตอบ:**
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture_source_demo_faq_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": {
      "en": "Fictional answer: for Check-in, use procedure C01 and the demo contact",
      "th": "คำตอบสมมุติ: เรื่อง เช็กอิน ให้ใช้ขั้นตอน C01 และติดต่อช่องทางตัวอย่าง"
    }
  }
}
```

### live_binding — เคส 02589

**ถาม (th/natural):** ตัวอย่าง การเชื่อมสถานะสด 01 จับคู่สถานะยังไง

**ตอบจริง:** ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

**ผิดตรง:** response_clarification, missing_field:status_mapping

**plan ที่เลือก:**
```json
{
  "record_ids": [
    "demo_live_binding_01"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "scope": "common_published",
  "platform": null
}
```

**ข้อมูลที่ควรนำมาตอบ:**
```json
{
  "status_mapping": {
    "evidence_refs": [
      {
        "locator": "/values/status_mapping",
        "source_id": "fixture_source_demo_live_binding_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": [
      {
        "normalized": "free",
        "raw": "DEMO_FREE_01"
      },
      {
        "normalized": "occupied",
        "raw": "DEMO_BOOKED_01"
      }
    ]
  }
}
```

## 7. ลำดับการแก้ที่หลักฐานรองรับ

| ลำดับ | สิ่งที่แก้ | วิธีตรวจว่าแก้จริง |
|---|---|---|
| P0 | normalize ทั้งคำถามและ label catalog ให้เหมือนกัน; แยก entity span ออกจากข้อความถาม | 13 กลุ่ม contract และคำถาม clean/typo เดิม ต้องไม่เสีย exact record/evidence |
| P0 | เลือกจำนวนคน/ความจุ/หลักฐานตาม kind; ให้ schema descriptions ช่วยจับ semantic field | natural/followup ของ audience, resource, service, zone, game_mode; ตรวจ min/max ตามสิ่งที่ถาม |
| P0 | กัน keyword details/นโยบายเปลี่ยน game เป็น competition โดยไม่มีเจตนาการแข่ง; คำปฏิเสธต้องไม่สลับหมวด | age_rating ต้องตอบ unknown ของเกม และคำถามกฎแข่งจริงยังไป competition |
| P1 | schema ของ planner ต้อง enum field ที่รองรับและ platform ที่มีจริง หรือ null; เก็บ rejection_reason/raw แบบเหมาะสม | API success, parsed, checked accepted, answer correct เป็นสี่ตัวชี้วัดแยก |
| P1 | ให้ planner ช่วยเมื่อ detected_fields ไม่มีใน kind ด้วย ไม่ใช่เฉพาะไม่มี field | natural ที่เคยจับ players_min ผิดหมวด ต้องตอบ capacity โดยไม่แต่งค่า |
| P1 | ผูกประวัติ record/field/context ให้ชัด แล้วถามเจาะจงเมื่อยังคลุมเครือ | สองรอบและเปลี่ยนเรื่องใหม่ ไม่ดึง record/ราคาจากเรื่องเก่า |
| P2 | วิเคราะห์ typo เทียบ clean เป็นคู่ รักษาตัวเลขเครื่องและราคา | ไม่เพิ่มการเลือกผิดเครื่อง 01→10 และไม่เพิ่ม alias เฉพาะเคสทุกประโยค |

รอบนี้เพิ่มชุดข้อมูลและทดสอบตามคำขอ ไม่ได้เอา patch routing หรือข้อมูลสมมุติเหล่านี้ไปเปลี่ยนระบบ production เก็บหลักฐานเพียงพอสำหรับแก้ชั้นตีความต่อโดยไม่แก้นโยบายของเจ้าของ

## 8. การแก้ข้อมูลเดิมและการแยกฐาน

40 เคสแก้: game.how_to_play 10, rate.amount_minor 10, policy.details 10, competition_rule.text 10 ใช้สำเนา `edit_demo/DEMO_EDITS_ONLY.sqlite` เท่านั้น ตรวจค่า live ไม่เปลี่ยนตอน save/approve, เปลี่ยนหลัง publish และ v1 ไม่ถูกเขียนทับ ฐาน DEMO หลักคง 240 records/240 revisions/1 release

ลองใส่ fixture เข้า empty production guard store: ถูกปฏิเสธ `Fixture source cannot enter production database`; store นั้นยังว่าง ลองอ่าน DEMO โดยไม่เปิด opt-in: ไม่คืนคำตอบ DEMO

production ของ ROOT และ ready_package ยังมี cc_heads 41 / cc_revisions 41 / cc_releases 0 hash เชิงตรรกะเหมือนใบตรวจ owner-edit เดิม; ready_package เทียบ baseline ที่เก็บก่อน import รอบนี้ด้วย SOURCE ห้าไฟล์ที่เกี่ยวข้องเหมือนกันทั้ง ROOT/CAND/PACK ไม่มีการเขียนแก้โค้ด production รอบนี้

ใบตรวจ V1 เคยนับเฉพาะตาราง legacy `records/releases` ซึ่งเป็นศูนย์ จึงออก V2 เพิ่ม `cc_heads/cc_revisions/cc_releases` ให้ตรง format กลาง เก็บ V1 ไว้และระบุการแก้ใน V2; hash ในทั้งสองใบตรงกัน

## 9. สิ่งที่ยังไม่มีการยืนยันจากมนุษย์

- ความเหมาะสมของคำแปลและคำอธิบายสำหรับเจ้าของจริง: agent_translated เท่านั้น
- อุปกรณ์ที่ติดตั้งจริง ราคา ตาราง กฎ การแข่งขัน แพ็กเกจ จำนวนคน และช่องทางติดต่อ: เป็นข้อมูลสมมุติทั้งหมด ไม่มีการขอหรืออ้าง owner sign-off
- เรตอายุเกม: unknown เพราะไม่ได้ตรวจ rating source ไม่ใช้เป็นเกณฑ์รับเด็กของศูนย์
- ปุ่มจริง เวอร์ชันจริง รายการเกมจริง และสถานะจองจริง: ไม่ได้ตรวจในรอบนี้; live_binding เป็นตัวอย่าง mapping ไม่ได้ต่อ WordPress

ไม่รัน full GT สองหมื่นเคส ไม่ติดตั้งโมเดลใหม่ ไม่ใช้ผล fixture เป็นข้อสรุปว่า API WordPress หรือสถานะสดถูกต้อง

## 10. แหล่งข้อมูลที่ค้นเอง

ใช้เฉพาะคำอธิบายเกมที่เรียบเรียงสั้น ๆ ส่วนข้อมูลร้านสมมุติ ไม่ถือว่าหน้าผู้พัฒนายืนยันเกมที่มีใน PSU

| เกม | แหล่งผู้พัฒนา/ผู้จัดจำหน่าย |
|---|---|
| Mario Kart 8 Deluxe | [หน้าอ้างอิงทางการ](https://www.nintendo.com/us/store/products/mario-kart-8-deluxe-switch/) |
| Super Smash Bros. Ultimate | [หน้าอ้างอิงทางการ](https://www.nintendo.com/us/store/products/super-smash-bros-ultimate-switch/) |
| Animal Crossing: New Horizons | [หน้าอ้างอิงทางการ](https://www.nintendo.com/us/store/products/animal-crossing-new-horizons-switch/) |
| The Legend of Zelda: Breath of the Wild | [หน้าอ้างอิงทางการ](https://www.nintendo.com/us/store/products/the-legend-of-zelda-breath-of-the-wild-switch/) |
| Minecraft | [หน้าอ้างอิงทางการ](https://www.minecraft.net/en-us/article/what-minecraft) |
| VALORANT | [หน้าอ้างอิงทางการ](https://playvalorant.com/en-us/) |
| Counter-Strike 2 | [หน้าอ้างอิงทางการ](https://store.steampowered.com/app/730/CounterStrike2/) |
| Dota 2 | [หน้าอ้างอิงทางการ](https://store.steampowered.com/app/570/Dota_2/) |
| Fortnite Battle Royale | [หน้าอ้างอิงทางการ](https://www.fortnite.com/@epic/battle-royale?lang=en-US) |
| Rocket League | [หน้าอ้างอิงทางการ](https://www.rocketleague.com/en) |

## 11. ไฟล์หลักฐาน

- [MANIFEST.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/MANIFEST.json)
- [RESEARCH_SOURCES.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/RESEARCH_SOURCES.json)
- [content_final/SUMMARY.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/content_final/SUMMARY.json)
- [content_final/SUMMARY_BY_CATEGORY.csv](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/content_final/SUMMARY_BY_CATEGORY.csv)
- [content_final/QUESTIONS_EXPECTED.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/content_final/QUESTIONS_EXPECTED.json)
- [content_final/ANSWERS_AND_DECISIONS.jsonl](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/content_final/ANSWERS_AND_DECISIONS.jsonl)
- [content_final/FAILURES.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/content_final/FAILURES.json)
- [content_final/EVALUATION_SCOPE.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/content_final/EVALUATION_SCOPE.json)
- [HTTP_SUMMARY.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/HTTP_SUMMARY.json)
- [HTTP_PREVIEW_RESULTS.jsonl](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/HTTP_PREVIEW_RESULTS.jsonl)
- [ACTUAL_CHAT_PIPELINE_SUMMARY.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/ACTUAL_CHAT_PIPELINE_SUMMARY.json)
- [ACTUAL_CHAT_PIPELINE_RESULTS.jsonl](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/ACTUAL_CHAT_PIPELINE_RESULTS.jsonl)
- [LLM_PREFLIGHT.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/LLM_PREFLIGHT.json)
- [LLM_SAMPLE_SUMMARY.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/LLM_SAMPLE_SUMMARY.json)
- [LLM_SAMPLE_RESULTS.jsonl](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/LLM_SAMPLE_RESULTS.jsonl)
- [LLM_REJECTION_DIAGNOSIS.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/LLM_REJECTION_DIAGNOSIS.json)
- [EDIT_AND_GUARD_SUMMARY.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EDIT_AND_GUARD_SUMMARY.json)
- [EDIT_40_RESULTS.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EDIT_40_RESULTS.json)
- [BROWSER_LIST_CHECKS.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/BROWSER_LIST_CHECKS.json)
- [FINAL_PRESERVATION_RECEIPT_V2.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/FINAL_PRESERVATION_RECEIPT_V2.json)
- [DEMO_SCREENSHOT.png](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/DEMO_SCREENSHOT.png)

ผลส่วนที่รันก่อนปรับ scorer/เร่งการรันอยู่ใน log และ content_round2 เดิม เก็บครบ ส่วน `content_final` เท่านั้นเป็นผลหลัก 5,020 เคส

